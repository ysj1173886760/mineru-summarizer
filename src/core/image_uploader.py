"""
图片上传模块
负责检测MD文件中的本地图片引用，上传到S3并替换链接
"""

import re
import os
from pathlib import Path
from typing import List, Tuple, Dict, Optional
from urllib.parse import urlparse, urljoin
import hashlib
import mimetypes

try:
    import oss2
    from oss2.exceptions import OssError, NoSuchBucket, AccessDenied
    OSS2_AVAILABLE = True
except ImportError:
    OSS2_AVAILABLE = False

from ..config.unified_config import UnifiedConfig


class ImageUploader:
    """图片上传器"""
    
    def __init__(self, config: UnifiedConfig, dry_run: bool = False):
        self.config = config
        self.s3_config = config.s3
        self.oss_bucket = None
        self.dry_run = dry_run
        
        if not OSS2_AVAILABLE:
            raise ImportError("需要安装oss2库: pip install oss2")
        
        if not self.s3_config.enabled:
            raise ValueError("OSS配置未启用，请在配置文件中设置 s3.enabled: true")
        
        self._validate_s3_config()
        
        if not dry_run:
            self._init_oss_client()
    
    def _validate_s3_config(self):
        """验证OSS配置"""
        required_fields = ['access_key_id', 'secret_access_key', 'bucket_name', 'endpoint_url']
        missing_fields = []
        
        for field in required_fields:
            value = getattr(self.s3_config, field)
            if not value:
                missing_fields.append(field)
        
        if missing_fields:
            raise ValueError(f"OSS配置缺少必需字段: {', '.join(missing_fields)}")
    
    def _init_oss_client(self):
        """初始化OSS客户端"""
        try:
            print(f"init oss with config {self.s3_config}")
            
            # 创建OSS认证对象
            auth = oss2.Auth(self.s3_config.access_key_id, self.s3_config.secret_access_key)
            
            # 创建Bucket对象
            self.oss_bucket = oss2.Bucket(auth, self.s3_config.endpoint_url, self.s3_config.bucket_name)
            
            # 测试连接 - 尝试获取bucket信息
            bucket_info = self.oss_bucket.get_bucket_info()
            print(f"✅ OSS连接成功，使用存储桶: {self.s3_config.bucket_name}")
            
        except AccessDenied:
            raise ValueError("OSS认证失败，请检查access_key_id和secret_access_key")
        except NoSuchBucket:
            raise ValueError(f"存储桶不存在: {self.s3_config.bucket_name}")
        except OssError as e:
            raise ValueError(f"OSS连接失败: {e}")
        except Exception as e:
            raise ValueError(f"初始化OSS客户端失败: {e}")
    
    def find_local_images(self, md_content: str, base_dir: Path) -> List[Dict]:
        """
        查找MD内容中的本地图片引用
        
        Returns:
            List[Dict]: [{"match": re.Match, "local_path": Path, "is_valid": bool}, ...]
        """
        # 匹配Markdown图片语法: ![alt](path) 和 <img src="path">
        image_patterns = [
            r'!\[([^\]]*)\]\(([^)]+)\)',  # ![alt](path)
            r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>',  # <img src="path">
        ]
        
        found_images = []
        
        for pattern in image_patterns:
            for match in re.finditer(pattern, md_content):
                if pattern.startswith('!'):  # ![alt](path) 格式
                    image_path = match.group(2)
                else:  # <img> 格式
                    image_path = match.group(1)
                
                # 跳过网络链接
                if self._is_url(image_path):
                    continue
                
                # 解析本地路径
                local_path = self._resolve_local_path(image_path, base_dir)
                is_valid = local_path.exists() and local_path.is_file()
                
                found_images.append({
                    "match": match,
                    "image_path": image_path,
                    "local_path": local_path,
                    "is_valid": is_valid
                })
        
        return found_images
    
    def _is_url(self, path: str) -> bool:
        """判断路径是否为URL"""
        try:
            result = urlparse(path)
            return bool(result.scheme and result.netloc)
        except:
            return False
    
    def _resolve_local_path(self, image_path: str, base_dir: Path) -> Path:
        """解析本地图片路径"""
        if os.path.isabs(image_path):
            return Path(image_path)
        else:
            return base_dir / image_path
    
    def upload_image(self, local_path: Path) -> str:
        """
        上传单个图片到S3
        
        Returns:
            str: 图片的公网URL
        """
        if not local_path.exists():
            raise FileNotFoundError(f"图片文件不存在: {local_path}")
        
        # 生成S3对象键
        s3_key = self._generate_s3_key(local_path)
        
        if self.dry_run:
            # Dry run模式，只返回预期的URL
            public_url = self._get_public_url(s3_key)
            print(f"🔍 [DRY RUN] 将上传: {local_path.name} -> {s3_key} -> {public_url}")
            return public_url
        
        # 检查是否已存在
        if self._object_exists(s3_key):
            print(f"📄 图片已存在，跳过上传: {s3_key}")
            return self._get_public_url(s3_key)
        
        # 获取MIME类型
        mime_type, _ = mimetypes.guess_type(str(local_path))
        if not mime_type:
            mime_type = 'application/octet-stream'
        
        try:
            # 上传文件
            print(f"⬆️ 正在上传: {local_path.name} -> {s3_key}")
            
            # 使用OSS2 SDK上传文件
            headers = {
                'Content-Type': mime_type
            }
            
            # 直接上传文件，OSS2会自动处理编码问题
            result = self.oss_bucket.put_object_from_file(s3_key, str(local_path), headers=headers)
            
            public_url = self._get_public_url(s3_key)
            print(f"✅ 上传成功: {public_url}")
            return public_url
            
        except OssError as e:
            raise RuntimeError(f"上传失败: {e}")
    
    def _generate_s3_key(self, local_path: Path) -> str:
        """生成S3对象键"""
        # 使用文件内容生成哈希，避免重复上传相同文件
        with open(local_path, 'rb') as f:
            content_hash = hashlib.md5(f.read()).hexdigest()[:8]
        
        # 保留原始文件名和扩展名
        name_without_ext = local_path.stem
        ext = local_path.suffix
        
        # 格式: prefix/filename_hash.ext
        s3_key = f"{self.s3_config.path_prefix}{name_without_ext}_{content_hash}{ext}"
        
        # 确保路径符合S3规范
        s3_key = s3_key.replace('\\', '/').lstrip('/')
        
        return s3_key
    
    def _object_exists(self, s3_key: str) -> bool:
        """检查OSS对象是否存在"""
        try:
            return self.oss_bucket.object_exists(s3_key)
        except OssError:
            return False
    
    def _get_public_url(self, s3_key: str) -> str:
        """获取对象的公网URL"""
        if self.s3_config.public_url_template:
            # 使用自定义URL模板
            return self.s3_config.public_url_template.format(
                bucket=self.s3_config.bucket_name,
                key=s3_key
            )
        elif self.s3_config.endpoint_url:
            # 根据不同的S3服务提供商生成URL
            base_url = self.s3_config.endpoint_url.rstrip('/')
            
            if 'aliyuncs.com' in base_url:
                # 阿里云OSS格式: https://bucket.endpoint/key
                endpoint_without_protocol = base_url.replace('https://', '').replace('http://', '')
                return f"https://{self.s3_config.bucket_name}.{endpoint_without_protocol}/{s3_key}"
            else:
                # 其他S3兼容服务: https://endpoint/bucket/key
                return f"{base_url}/{self.s3_config.bucket_name}/{s3_key}"
        else:
            # 使用标准AWS S3 URL格式
            return f"https://{self.s3_config.bucket_name}.s3.{self.s3_config.region_name}.amazonaws.com/{s3_key}"
    
    def process_markdown_file(self, md_file_path: Path) -> Tuple[str, Dict]:
        """
        处理Markdown文件，上传本地图片并替换链接
        
        Returns:
            Tuple[str, Dict]: (处理后的内容, 统计信息)
        """
        print(f"🔍 分析文件: {md_file_path}")
        
        # 读取文件内容
        with open(md_file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # 查找本地图片
        base_dir = md_file_path.parent
        found_images = self.find_local_images(original_content, base_dir)
        
        if not found_images:
            print("📄 未找到本地图片引用")
            return original_content, {"total": 0, "uploaded": 0, "skipped": 0, "errors": 0}
        
        print(f"📸 找到 {len(found_images)} 个图片引用")
        
        # 统计信息
        stats = {"total": len(found_images), "uploaded": 0, "skipped": 0, "errors": 0}
        
        # 按位置倒序处理，避免位置偏移
        found_images.sort(key=lambda x: x["match"].start(), reverse=True)
        
        processed_content = original_content
        
        for img_info in found_images:
            match = img_info["match"]
            local_path = img_info["local_path"]
            
            if not img_info["is_valid"]:
                print(f"⚠️ 图片文件不存在，跳过: {img_info['image_path']}")
                stats["errors"] += 1
                continue
            
            try:
                # 上传图片
                public_url = self.upload_image(local_path)
                
                # 替换链接
                original_match = match.group(0)
                if original_match.startswith('!['):
                    # Markdown格式: ![alt](path)
                    alt_text = match.group(1)
                    new_link = f"![{alt_text}]({public_url})"
                else:
                    # HTML格式: <img src="path">
                    new_link = re.sub(
                        r'src=["\'][^"\']+["\']',
                        f'src="{public_url}"',
                        original_match
                    )
                
                # 替换内容
                start, end = match.span()
                processed_content = processed_content[:start] + new_link + processed_content[end:]
                
                stats["uploaded"] += 1
                
            except Exception as e:
                print(f"❌ 处理图片失败 {local_path}: {e}")
                stats["errors"] += 1
        
        return processed_content, stats
    
    def process_markdown_content(self, content: str, base_dir: Path) -> Tuple[str, Dict]:
        """
        处理Markdown内容字符串
        
        Args:
            content: Markdown内容
            base_dir: 相对路径的基准目录
        
        Returns:
            Tuple[str, Dict]: (处理后的内容, 统计信息)
        """
        print(f"🔍 分析Markdown内容...")
        
        # 查找本地图片
        found_images = self.find_local_images(content, base_dir)
        
        if not found_images:
            print("📄 未找到本地图片引用")
            return content, {"total": 0, "uploaded": 0, "skipped": 0, "errors": 0}
        
        print(f"📸 找到 {len(found_images)} 个图片引用")
        
        # 统计信息
        stats = {"total": len(found_images), "uploaded": 0, "skipped": 0, "errors": 0}
        
        # 按位置倒序处理，避免位置偏移
        found_images.sort(key=lambda x: x["match"].start(), reverse=True)
        
        processed_content = content
        
        for img_info in found_images:
            match = img_info["match"]
            local_path = img_info["local_path"]
            
            if not img_info["is_valid"]:
                print(f"⚠️ 图片文件不存在，跳过: {img_info['image_path']}")
                stats["errors"] += 1
                continue
            
            try:
                # 上传图片
                public_url = self.upload_image(local_path)
                
                # 替换链接
                original_match = match.group(0)
                if original_match.startswith('!['):
                    # Markdown格式: ![alt](path)
                    alt_text = match.group(1)
                    new_link = f"![{alt_text}]({public_url})"
                else:
                    # HTML格式: <img src="path">
                    new_link = re.sub(
                        r'src=["\'][^"\']+["\']',
                        f'src="{public_url}"',
                        original_match
                    )
                
                # 替换内容
                start, end = match.span()
                processed_content = processed_content[:start] + new_link + processed_content[end:]
                
                stats["uploaded"] += 1
                
            except Exception as e:
                print(f"❌ 处理图片失败 {local_path}: {e}")
                stats["errors"] += 1
        
        return processed_content, stats