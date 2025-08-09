from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from .content_parser import ContentItem
from ..utils.helpers import is_likely_title


@dataclass
class Section:
    """文档章节数据类"""
    title: str
    level: int
    content: List[ContentItem]
    subsections: List['Section']
    start_idx: int
    end_idx: int


class DocumentStructure:
    """文档结构分析器"""
    
    def __init__(self, content_items: List[ContentItem]):
        self.content_items = content_items
        self.sections: List[Section] = []
        
    def analyze(self) -> List[Section]:
        """分析文档结构"""
        self.sections = self._build_hierarchy()
        return self.sections
    
    def _build_hierarchy(self) -> List[Section]:
        """构建层级结构"""
        if not self.content_items:
            return []
        
        # 识别标题和内容项
        sections = []
        current_section = None
        content_buffer = []
        
        for idx, item in enumerate(self.content_items):
            if self._is_section_title(item):
                # 保存前一个章节
                if current_section:
                    current_section.content.extend(content_buffer)
                    current_section.end_idx = idx - 1
                    sections.append(current_section)
                
                # 创建新章节
                current_section = Section(
                    title=item.text,
                    level=item.text_level or 1,
                    content=[],
                    subsections=[],
                    start_idx=idx,
                    end_idx=idx
                )
                content_buffer = []
            else:
                # 添加到内容缓冲区
                content_buffer.append(item)
        
        # 处理最后一个章节
        if current_section:
            current_section.content.extend(content_buffer)
            current_section.end_idx = len(self.content_items) - 1
            sections.append(current_section)
        elif content_buffer:
            # 如果没有找到任何标题，创建一个默认章节
            default_section = Section(
                title="内容",
                level=1,
                content=content_buffer,
                subsections=[],
                start_idx=0,
                end_idx=len(self.content_items) - 1
            )
            sections.append(default_section)
        
        # 构建嵌套结构
        return self._nest_sections(sections)
    
    def _is_section_title(self, item: ContentItem) -> bool:
        """判断是否为章节标题"""
        if item.type != 'text':
            return False
        
        # 基于text_level判断
        if item.text_level and item.text_level > 0:
            return True
        
        # 基于启发式规则
        return is_likely_title(item.text)
    
    def _nest_sections(self, sections: List[Section]) -> List[Section]:
        """将扁平的章节列表转换为嵌套结构"""
        if not sections:
            return []
        
        result = []
        stack = []
        
        for section in sections:
            # 弹出级别更高或相等的章节
            while stack and stack[-1].level >= section.level:
                stack.pop()
            
            if stack:
                # 作为子章节添加
                stack[-1].subsections.append(section)
            else:
                # 作为顶级章节添加
                result.append(section)
            
            stack.append(section)
        
        return result
    
    def get_sections_by_level(self, level: int) -> List[Section]:
        """获取指定级别的所有章节"""
        result = []
        
        def collect_sections(sections: List[Section]):
            for section in sections:
                if section.level == level:
                    result.append(section)
                collect_sections(section.subsections)
        
        collect_sections(self.sections)
        return result
    
    def get_section_content_text(self, section: Section) -> str:
        """获取章节的纯文本内容"""
        content_texts = []
        
        # 添加标题
        content_texts.append(section.title)
        
        # 添加内容
        for item in section.content:
            if item.type == 'text':
                content_texts.append(item.text)
            elif item.type == 'image' and item.image_path:
                content_texts.append(f"[图片: {item.image_path}]")
        
        # 递归添加子章节
        for subsection in section.subsections:
            content_texts.append(self.get_section_content_text(subsection))
        
        return '\n\n'.join(content_texts)
    
    def print_structure(self, sections: Optional[List[Section]] = None, indent: int = 0) -> None:
        """打印文档结构（调试用）"""
        if sections is None:
            sections = self.sections
        
        for section in sections:
            prefix = "  " * indent
            print(f"{prefix}- {section.title} (Level {section.level})")
            print(f"{prefix}  Content items: {len(section.content)}")
            if section.subsections:
                self.print_structure(section.subsections, indent + 1)
    
    def get_flat_sections(self) -> List[Section]:
        """获取扁平化的章节列表（按原始顺序）"""
        result = []
        
        def collect_sections(sections: List[Section]):
            for section in sections:
                result.append(section)
                collect_sections(section.subsections)
        
        collect_sections(self.sections)
        return result