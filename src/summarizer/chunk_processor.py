from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from ..parser.structure_analyzer import Section, DocumentStructure
from ..utils.helpers import count_tokens, truncate_text
from ..utils.config import ProcessingConfig


@dataclass
class Chunk:
    """文档块数据类"""
    id: str
    content: str
    section_title: str
    section_level: int
    token_count: int
    context: Optional[str] = None  # 前后文信息
    metadata: Dict[str, Any] = None


class ChunkProcessor:
    """文档分块处理器"""
    
    def __init__(self, config: ProcessingConfig):
        self.config = config
        self.chunks: List[Chunk] = []
        
    def process_sections(self, sections: List[Section]) -> List[Chunk]:
        """处理章节，生成分块"""
        self.chunks = []
        
        for section in sections:
            section_chunks = self._process_section(section)
            self.chunks.extend(section_chunks)
        
        # 添加上下文信息
        self._add_context_info()
        
        return self.chunks
    
    def _process_section(self, section: Section) -> List[Chunk]:
        """处理单个章节"""
        section_text = self._get_section_text(section)
        
        if not section_text.strip():
            return []
        
        # 计算token数量
        token_count = count_tokens(section_text)
        
        # 如果章节较小，直接返回一个块
        if token_count <= self.config.chunk_size:
            chunk = Chunk(
                id=f"section_{section.title}_{0}",
                content=section_text,
                section_title=section.title,
                section_level=section.level,
                token_count=token_count,
                metadata={
                    'original_section': section,
                    'chunk_index': 0,
                    'total_chunks': 1
                }
            )
            return [chunk]
        
        # 对于较大的章节，进行分块
        return self._split_section(section, section_text)
    
    def _get_section_text(self, section: Section) -> str:
        """获取章节的完整文本"""
        texts = []
        
        # 添加章节标题
        if section.title:
            level_prefix = "#" * section.level
            texts.append(f"{level_prefix} {section.title}")
        
        # 添加内容
        for item in section.content:
            if item.type == 'text':
                texts.append(item.text)
            elif item.type == 'image' and item.image_path:
                texts.append(f"\n![图片]({item.image_path})\n")
        
        # 递归处理子章节
        for subsection in section.subsections:
            subsection_text = self._get_section_text(subsection)
            if subsection_text.strip():
                texts.append(subsection_text)
        
        return '\n\n'.join(texts)
    
    def _split_section(self, section: Section, section_text: str) -> List[Chunk]:
        """分割大章节"""
        chunks = []
        
        # 尝试按子章节分割
        if section.subsections:
            return self._split_by_subsections(section)
        
        # 按段落分割
        paragraphs = section_text.split('\n\n')
        return self._split_by_paragraphs(section, paragraphs)
    
    def _split_by_subsections(self, section: Section) -> List[Chunk]:
        """按子章节分割"""
        chunks = []
        
        # 处理主章节内容（不包括子章节）
        main_content_items = []
        for item in section.content:
            if item.type == 'text':
                main_content_items.append(item.text)
            elif item.type == 'image' and item.image_path:
                main_content_items.append(f"\n![图片]({item.image_path})\n")
        
        if main_content_items:
            main_content = '\n\n'.join(main_content_items)
            if main_content.strip():
                chunk = Chunk(
                    id=f"section_{section.title}_main",
                    content=f"# {section.title}\n\n{main_content}",
                    section_title=section.title,
                    section_level=section.level,
                    token_count=count_tokens(main_content),
                    metadata={
                        'original_section': section,
                        'chunk_type': 'main_content'
                    }
                )
                chunks.append(chunk)
        
        # 处理每个子章节
        for i, subsection in enumerate(section.subsections):
            subsection_chunks = self._process_section(subsection)
            chunks.extend(subsection_chunks)
        
        return chunks
    
    def _split_by_paragraphs(self, section: Section, paragraphs: List[str]) -> List[Chunk]:
        """按段落分割"""
        chunks = []
        current_chunk_content = []
        current_token_count = 0
        chunk_index = 0
        
        # 确保包含标题
        title_text = f"# {section.title}" if section.title else ""
        title_tokens = count_tokens(title_text)
        
        for paragraph in paragraphs:
            if not paragraph.strip():
                continue
            
            para_tokens = count_tokens(paragraph)
            
            # 检查是否需要创建新块
            if (current_token_count + para_tokens + title_tokens > self.config.chunk_size 
                and current_chunk_content):
                
                # 创建当前块
                chunk_content = title_text + '\n\n' + '\n\n'.join(current_chunk_content)
                chunk = Chunk(
                    id=f"section_{section.title}_{chunk_index}",
                    content=chunk_content,
                    section_title=section.title,
                    section_level=section.level,
                    token_count=current_token_count + title_tokens,
                    metadata={
                        'original_section': section,
                        'chunk_index': chunk_index,
                        'paragraph_start': len(chunks) * self.config.chunk_size
                    }
                )
                chunks.append(chunk)
                
                # 重置
                current_chunk_content = []
                current_token_count = 0
                chunk_index += 1
            
            current_chunk_content.append(paragraph)
            current_token_count += para_tokens
        
        # 处理最后一个块
        if current_chunk_content:
            chunk_content = title_text + '\n\n' + '\n\n'.join(current_chunk_content)
            chunk = Chunk(
                id=f"section_{section.title}_{chunk_index}",
                content=chunk_content,
                section_title=section.title,
                section_level=section.level,
                token_count=current_token_count + title_tokens,
                metadata={
                    'original_section': section,
                    'chunk_index': chunk_index,
                    'paragraph_start': len(chunks) * self.config.chunk_size
                }
            )
            chunks.append(chunk)
        
        return chunks
    
    def _add_context_info(self) -> None:
        """为块添加上下文信息"""
        if not self.config.preserve_structure or len(self.chunks) <= 1:
            return
        
        for i, chunk in enumerate(self.chunks):
            context_parts = []
            
            # 添加文档概述（如果是第一个块）
            if i == 0:
                context_parts.append("这是一篇学术论文的开始部分。")
            
            # 添加前一个块的标题信息
            if i > 0:
                prev_chunk = self.chunks[i-1]
                if prev_chunk.section_title != chunk.section_title:
                    context_parts.append(f"前一章节: {prev_chunk.section_title}")
            
            # 添加后一个块的标题信息
            if i < len(self.chunks) - 1:
                next_chunk = self.chunks[i+1]
                if next_chunk.section_title != chunk.section_title:
                    context_parts.append(f"下一章节: {next_chunk.section_title}")
            
            if context_parts:
                chunk.context = " | ".join(context_parts)
    
    def get_chunk_stats(self) -> Dict[str, Any]:
        """获取分块统计信息"""
        if not self.chunks:
            return {}
        
        total_tokens = sum(chunk.token_count for chunk in self.chunks)
        avg_tokens = total_tokens / len(self.chunks)
        
        return {
            'total_chunks': len(self.chunks),
            'total_tokens': total_tokens,
            'avg_tokens_per_chunk': int(avg_tokens),
            'max_tokens': max(chunk.token_count for chunk in self.chunks),
            'min_tokens': min(chunk.token_count for chunk in self.chunks),
            'sections_covered': len(set(chunk.section_title for chunk in self.chunks))
        }