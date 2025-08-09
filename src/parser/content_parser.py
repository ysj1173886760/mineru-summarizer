from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import json
from dataclasses import dataclass
from ..utils.helpers import load_json, clean_text


@dataclass
class ContentItem:
    """内容项数据类"""
    type: str
    text: str
    text_level: Optional[int] = None
    page_idx: Optional[int] = None
    bbox: Optional[List[float]] = None
    image_path: Optional[str] = None


@dataclass 
class ImageInfo:
    """图片信息数据类"""
    path: str
    bbox: List[float]
    page_idx: int


class MinerUParser:
    """MinerU输出数据解析器"""
    
    def __init__(self, input_dir: Path):
        self.input_dir = Path(input_dir)
        self.content_items: List[ContentItem] = []
        self.images: List[ImageInfo] = []
        
    def parse(self) -> Tuple[List[ContentItem], List[ImageInfo]]:
        """解析MinerU输出数据"""
        # 解析content_list.json
        self._parse_content_list()
        
        # 解析layout.json获取图片信息
        self._parse_layout()
        
        # 关联图片和文本
        self._associate_images()
        
        return self.content_items, self.images
    
    def _parse_content_list(self) -> None:
        """解析content_list.json文件"""
        content_list_files = list(self.input_dir.glob("*_content_list.json"))
        if not content_list_files:
            raise FileNotFoundError("未找到content_list.json文件")
        
        content_list_path = content_list_files[0]
        content_data = load_json(content_list_path)
        
        for item in content_data:
            if item.get('type') == 'text':
                content_item = ContentItem(
                    type=item['type'],
                    text=clean_text(item['text']),
                    text_level=item.get('text_level'),
                    page_idx=item.get('page_idx')
                )
                self.content_items.append(content_item)
    
    def _parse_layout(self) -> None:
        """解析layout.json获取图片信息"""
        layout_path = self.input_dir / "layout.json"
        if not layout_path.exists():
            print("警告: 未找到layout.json文件，无法获取图片位置信息")
            return
        
        layout_data = load_json(layout_path)
        pdf_info = layout_data.get('pdf_info', [])
        
        for page_idx, page_info in enumerate(pdf_info):
            self._extract_images_from_page(page_info, page_idx)
    
    def _extract_images_from_page(self, page_info: Dict[str, Any], page_idx: int) -> None:
        """从页面信息中提取图片"""
        # 检查图片块
        for block in page_info.get('para_blocks', []):
            if block.get('type') == 'image':
                # 查找对应的图片文件
                image_files = list(self.input_dir.glob("images/*.jpg")) + \
                             list(self.input_dir.glob("images/*.png"))
                
                if image_files:
                    # 简单策略：按页面顺序匹配图片
                    # 更复杂的匹配可以基于bbox坐标
                    image_info = ImageInfo(
                        path=str(image_files[len(self.images) % len(image_files)]),
                        bbox=block.get('bbox', []),
                        page_idx=page_idx
                    )
                    self.images.append(image_info)
    
    def _associate_images(self) -> None:
        """关联图片和文本内容"""
        # 简单策略：将图片插入到相同页面的文本之间
        for image in self.images:
            # 找到相同页面的文本项
            page_items = [item for item in self.content_items 
                         if item.page_idx == image.page_idx]
            
            if page_items:
                # 在适当位置插入图片引用
                image_item = ContentItem(
                    type="image",
                    text=f"![图片]({image.path})",
                    page_idx=image.page_idx,
                    image_path=image.path
                )
                
                # 插入到页面文本的中间位置
                insert_idx = len([item for item in self.content_items 
                                if item.page_idx <= image.page_idx])
                self.content_items.insert(insert_idx, image_item)
    
    def get_markdown_content(self) -> str:
        """获取完整的markdown内容"""
        full_md_path = self.input_dir / "full.md"
        if full_md_path.exists():
            with open(full_md_path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""
    
    def get_images_dir(self) -> Path:
        """获取图片目录路径"""
        return self.input_dir / "images"