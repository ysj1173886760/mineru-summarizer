#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinerU PDF解析客户端
用于向MinerU HTTP服务器上传PDF文件并下载解析结果
"""

import os
import sys
import argparse
import requests
import zipfile
import tempfile
from pathlib import Path
from typing import Optional


class MinerUClient:
    """MinerU客户端"""
    
    def __init__(self, server_url: str = "http://localhost:5000"):
        """
        初始化客户端
        
        Args:
            server_url: 服务器地址
        """
        self.server_url = server_url.rstrip('/')
        self.session = requests.Session()
    
    def check_server_health(self) -> bool:
        """检查服务器健康状态"""
        try:
            response = self.session.get(f"{self.server_url}/health", timeout=10)
            return response.status_code == 200
        except Exception:
            return False
    
    def parse_pdf(
        self,
        pdf_path: str,
        output_dir: str,
        lang: str = "ch",
        backend: str = "pipeline",
        method: str = "auto",
        formula_enable: bool = True,
        table_enable: bool = True,
        server_url: Optional[str] = None
    ) -> bool:
        """
        解析PDF文件
        
        Args:
            pdf_path: PDF文件路径
            output_dir: 输出目录路径
            lang: 语言选项
            backend: 解析后端
            method: 解析方法
            formula_enable: 启用公式解析
            table_enable: 启用表格解析
            server_url: VLM服务器URL（可选）
            
        Returns:
            bool: 是否成功
        """
        # 检查PDF文件是否存在
        if not os.path.exists(pdf_path):
            print(f"❌ 错误: PDF文件不存在: {pdf_path}")
            return False
        
        # 检查文件大小
        file_size = os.path.getsize(pdf_path)
        if file_size > 100 * 1024 * 1024:  # 100MB
            print(f"❌ 错误: PDF文件过大 ({file_size / 1024 / 1024:.1f}MB)，最大支持100MB")
            return False
        
        # 创建输出目录
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        print(f"📄 正在上传PDF文件: {pdf_path}")
        print(f"📁 输出目录: {output_dir}")
        print(f"🌐 服务器地址: {self.server_url}")
        print(f"⚙️  配置: lang={lang}, backend={backend}, method={method}")
        
        try:
            # 准备文件和数据
            with open(pdf_path, 'rb') as f:
                files = {'file': (os.path.basename(pdf_path), f, 'application/pdf')}
                data = {
                    'lang': lang,
                    'backend': backend,
                    'method': method,
                    'formula_enable': str(formula_enable).lower(),
                    'table_enable': str(table_enable).lower()
                }
                
                # 添加可选的server_url参数
                if server_url:
                    data['server_url'] = server_url
                
                print("🚀 开始上传和解析...")
                
                # 发送请求
                response = self.session.post(
                    f"{self.server_url}/parse",
                    files=files,
                    data=data,
                    timeout=3600  # 1小时超时
                )
            
            if response.status_code == 200:
                print("✅ 解析完成，正在下载结果...")
                
                # 创建临时文件保存ZIP
                with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_zip:
                    temp_zip.write(response.content)
                    temp_zip_path = temp_zip.name
                
                try:
                    # 解压ZIP文件到临时目录，然后重新整理结构
                    print("📦 正在解压结果...")
                    with tempfile.TemporaryDirectory() as temp_extract_dir:
                        with zipfile.ZipFile(temp_zip_path, 'r') as zip_ref:
                            zip_ref.extractall(temp_extract_dir)
                        
                        # 重新整理文件结构
                        self._reorganize_output(temp_extract_dir, output_dir)
                    
                    print(f"✅ 解析结果已保存到: {output_dir}")
                    
                    # 显示输出文件列表
                    self._show_output_files(output_dir)
                    
                    return True
                    
                finally:
                    # 清理临时ZIP文件
                    try:
                        os.unlink(temp_zip_path)
                    except:
                        pass
            
            else:
                # 解析错误响应
                try:
                    error_info = response.json()
                    print(f"❌ 服务器错误: {error_info.get('error', '未知错误')}")
                except:
                    print(f"❌ 服务器错误: HTTP {response.status_code}")
                return False
                
        except requests.exceptions.Timeout:
            print("❌ 错误: 请求超时，PDF文件可能过大或服务器繁忙")
            return False
        except requests.exceptions.ConnectionError:
            print(f"❌ 错误: 无法连接到服务器 {self.server_url}")
            print("请确保服务器正在运行")
            return False
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
            return False
    
    def _reorganize_output(self, temp_extract_dir: str, output_dir: str):
        """重新整理输出文件结构，使其更容易处理"""
        import shutil
        
        # 创建输出目录
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # 查找解压出来的文件
        temp_path = Path(temp_extract_dir)
        
        # 查找主要的markdown文件（通常在auto目录下）
        md_files = list(temp_path.rglob("*.md"))
        main_md_file = None
        
        # 找到最主要的markdown文件（通常是最大的那个）
        if md_files:
            main_md_file = max(md_files, key=lambda f: f.stat().st_size)
            
            # 复制主markdown文件并重命名为full.md
            shutil.copy2(main_md_file, output_path / "full.md")
            print(f"📝 主文档已复制为: full.md")
        
        # 查找并复制images目录
        for images_dir in temp_path.rglob("images"):
            if images_dir.is_dir():
                dest_images_dir = output_path / "images"
                if dest_images_dir.exists():
                    shutil.rmtree(dest_images_dir)
                shutil.copytree(images_dir, dest_images_dir)
                print(f"🖼️  图片目录已复制: {len(list(dest_images_dir.iterdir()))} 个文件")
                break
        
        # 复制其他有用的文件（JSON, PDF等）
        useful_extensions = {'.json', '.pdf'}
        for file_path in temp_path.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in useful_extensions:
                # 保持相对路径结构，但简化目录层次
                rel_path = file_path.relative_to(temp_path)
                # 简化路径：去掉第一层目录（通常是PDF文件名目录）
                if len(rel_path.parts) > 1:
                    simplified_path = Path(*rel_path.parts[1:])
                else:
                    simplified_path = rel_path
                
                dest_file = output_path / simplified_path
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, dest_file)
        
        print(f"📁 文件结构已重新整理到: {output_dir}")

    def _show_output_files(self, output_dir: str):
        """显示输出文件列表"""
        print("\n📋 输出文件列表:")
        output_path = Path(output_dir)
        
        files_found = False
        for root, dirs, files in os.walk(output_path):
            for file in files:
                file_path = Path(root) / file
                rel_path = file_path.relative_to(output_path)
                file_size = file_path.stat().st_size
                
                # 格式化文件大小
                if file_size < 1024:
                    size_str = f"{file_size}B"
                elif file_size < 1024 * 1024:
                    size_str = f"{file_size / 1024:.1f}KB"
                else:
                    size_str = f"{file_size / (1024 * 1024):.1f}MB"
                
                print(f"  📄 {rel_path} ({size_str})")
                files_found = True
        
        if not files_found:
            print("  (无文件)")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="MinerU PDF解析客户端",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 基本用法
  python client.py document.pdf ./output

  # 指定语言和后端
  python client.py document.pdf ./output --lang en --backend pipeline

  # 使用VLM后端
  python client.py document.pdf ./output --backend vlm-transformers

  # 禁用公式解析
  python client.py document.pdf ./output --no-formula

  # 指定自定义服务器
  python client.py document.pdf ./output --server http://192.168.1.100:5000
        """
    )
    
    parser.add_argument("pdf_path", help="PDF文件路径")
    parser.add_argument("output_dir", help="输出目录路径")
    
    parser.add_argument("--server", default="http://localhost:5000",
                       help="MinerU服务器地址 (默认: http://localhost:5000)")
    parser.add_argument("--lang", default="ch",
                       choices=["ch", "en", "korean", "japan", "chinese_cht", "ta", "te", "ka"],
                       help="语言选项 (默认: ch)")
    parser.add_argument("--backend", default="pipeline",
                       choices=["pipeline", "vlm-transformers", "vlm-sglang-engine", "vlm-sglang-client"],
                       help="解析后端 (默认: pipeline)")
    parser.add_argument("--method", default="auto",
                       choices=["auto", "txt", "ocr"],
                       help="解析方法 (默认: auto)")
    parser.add_argument("--no-formula", action="store_true",
                       help="禁用公式解析")
    parser.add_argument("--no-table", action="store_true",
                       help="禁用表格解析")
    parser.add_argument("--vlm-server-url",
                       help="VLM服务器URL (当backend为vlm-sglang-client时需要)")
    
    args = parser.parse_args()
    
    # 创建客户端
    client = MinerUClient(args.server)
    
    print("=" * 60)
    print("MinerU PDF解析客户端")
    print("=" * 60)
    
    # 检查服务器健康状态
    print("🔍 检查服务器状态...")
    if not client.check_server_health():
        print(f"❌ 无法连接到服务器: {args.server}")
        print("请确保服务器正在运行，或检查服务器地址是否正确")
        sys.exit(1)
    
    print("✅ 服务器连接正常")
    
    # 解析PDF
    success = client.parse_pdf(
        pdf_path=args.pdf_path,
        output_dir=args.output_dir,
        lang=args.lang,
        backend=args.backend,
        method=args.method,
        formula_enable=not args.no_formula,
        table_enable=not args.no_table,
        server_url=args.vlm_server_url
    )
    
    if success:
        print("\n🎉 PDF解析完成！")
        sys.exit(0)
    else:
        print("\n💥 PDF解析失败！")
        sys.exit(1)


if __name__ == "__main__":
    main()
