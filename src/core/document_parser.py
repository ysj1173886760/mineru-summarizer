from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from langchain_text_splitters import MarkdownHeaderTextSplitter
import logging

logger = logging.getLogger(__name__)


def count_tokens(text: str) -> int:
    """简单的token计数"""
    return len(text.split())


@dataclass
class DocumentChunk:
    """文档块"""
    id: str
    content: str
    metadata: Dict[str, Any]
    token_count: int
    chapter_title: str
    chapter_level: int
    sub_sections: List[str]


class DocumentParser:
    """统一的文档解析器 - 基于V3的markdown header分割"""
    
    def __init__(self, max_tokens_per_chapter: int = 8000):
        self.max_tokens_per_chapter = max_tokens_per_chapter
        
        # 只按一级标题分割（V3特性）
        self.headers_to_split_on = [
            ("#", "Header 1"),
        ]
        
        # 创建markdown标题分割器
        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.headers_to_split_on,
            strip_headers=False
        )
    
    def parse_markdown_file(self, file_path: Path) -> List[DocumentChunk]:
        """解析Markdown文件，保持章节的原始顺序"""
        
        # 读取markdown内容
        with open(file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # 清理内容
        markdown_content = self._clean_markdown(markdown_content)
        
        # 按一级标题分割
        header_chunks = self.markdown_splitter.split_text(markdown_content)
        
        final_chunks = []
        skipped_chapters = []
        chunk_index = 0  # 用于保持顺序的索引
        
        for i, chunk in enumerate(header_chunks):
            # 提取章节信息
            chapter_title = chunk.metadata.get('Header 1', f'Chapter {i+1}')
            
            # 过滤不需要总结的章节
            if self._should_skip_chapter(chapter_title):
                skipped_chapters.append(chapter_title)
                continue
            
            token_count = count_tokens(chunk.page_content)
            sub_sections = self._extract_sub_sections(chunk.page_content)
            
            if token_count <= self.max_tokens_per_chapter:
                # 章节大小合适，直接使用，保持原始顺序
                chapter_chunk = DocumentChunk(
                    id=f"chapter_{chunk_index:03d}",  # 使用3位数编号确保排序正确
                    content=chunk.page_content,
                    metadata=chunk.metadata,
                    token_count=token_count,
                    chapter_title=chapter_title,
                    chapter_level=1,
                    sub_sections=sub_sections
                )
                final_chunks.append(chapter_chunk)
                chunk_index += 1
            else:
                # 章节太大，按二级标题分割，保持原始顺序
                sub_chunks = self._split_large_chapter(chunk, chunk_index)
                final_chunks.extend(sub_chunks)
                chunk_index += len(sub_chunks)
        
        if skipped_chapters:
            print(f"🚫 跳过的章节: {', '.join(skipped_chapters)}")
        
        return final_chunks
    
    def _should_skip_chapter(self, chapter_title: str) -> bool:
        """判断是否应该跳过某个章节"""
        skip_keywords = [
            'references',      # 参考文献
            'bibliography',    # 参考书目
            'contents',        # 目录
            'table of contents', # 目录
            'appendix',        # 附录
            'acknowledgments', # 致谢
            'acknowledgements', # 致谢
        ]
        
        title_lower = chapter_title.lower().strip()
        
        # 检查是否包含跳过关键词
        for keyword in skip_keywords:
            if keyword in title_lower:
                return True
        
        # 检查是否只是章节标题页（通常很短且只包含标题）
        if len(chapter_title.strip()) < 5:
            return True
            
        return False
    
    def _split_large_chapter(self, chunk, chapter_index: int) -> List[DocumentChunk]:
        """分割过大的章节，保持原始顺序"""
        # 创建包含二级标题的分割器
        sub_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
            ],
            strip_headers=False
        )
        
        sub_chunks = sub_splitter.split_text(chunk.page_content)
        result = []
        
        chapter_title = chunk.metadata.get('Header 1', f'Chapter {chapter_index+1}')
        
        for j, sub_chunk in enumerate(sub_chunks):
            token_count = count_tokens(sub_chunk.page_content)
            sub_title = sub_chunk.metadata.get('Header 2', f'Section {j+1}')
            sub_sections = self._extract_sub_sections(sub_chunk.page_content)
            
            chapter_chunk = DocumentChunk(
                id=f"chapter_{chapter_index:03d}_{j:03d}",  # 使用3位数编号确保排序正确
                content=sub_chunk.page_content,
                metadata=sub_chunk.metadata,
                token_count=token_count,
                chapter_title=f"{chapter_title} - {sub_title}",
                chapter_level=2,
                sub_sections=sub_sections
            )
            result.append(chapter_chunk)
        
        return result
    
    def _extract_sub_sections(self, content: str) -> List[str]:
        """提取内容中的子章节标题"""
        lines = content.split('\n')
        sub_sections = []
        
        for line in lines:
            line = line.strip()
            if line.startswith('##') and not line.startswith('###'):
                # 二级标题
                title = line.replace('##', '').strip()
                sub_sections.append(title)
            elif line.startswith('###'):
                # 三级标题
                title = line.replace('###', '').strip()
                sub_sections.append(f"  {title}")  # 缩进表示层级
        
        return sub_sections
    
    def _clean_markdown(self, content: str) -> str:
        """清理markdown内容"""
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # 跳过空行太多的情况
            if line.strip():
                cleaned_lines.append(line)
            elif not cleaned_lines or cleaned_lines[-1].strip():
                # 保留必要的空行
                cleaned_lines.append('')
        
        return '\n'.join(cleaned_lines)
    
    def get_statistics(self, chunks: List[DocumentChunk]) -> Dict[str, Any]:
        """获取统计信息"""
        stats = {
            'total_chapters': len(chunks),
            'total_tokens': sum(chunk.token_count for chunk in chunks),
            'chapters': [],
            'token_distribution': {}
        }
        
        for chunk in chunks:
            chapter_info = {
                'title': chunk.chapter_title,
                'level': chunk.chapter_level,
                'tokens': chunk.token_count,
                'sub_sections_count': len(chunk.sub_sections),
                'sub_sections': chunk.sub_sections[:5]  # 只显示前5个
            }
            stats['chapters'].append(chapter_info)
        
        # 统计token分布
        token_ranges = [(0, 1000), (1000, 3000), (3000, 5000), (5000, 10000), (10000, float('inf'))]
        for start, end in token_ranges:
            range_key = f"{start}-{end if end != float('inf') else 'inf'}"
            count = len([c for c in chunks if start <= c.token_count < end])
            stats['token_distribution'][range_key] = count
        
        return stats
    
    def print_statistics(self, chunks: List[DocumentChunk]) -> None:
        """打印统计信息"""
        stats = self.get_statistics(chunks)
        
        print("📚 文档解析统计:")
        print(f"   总章节数: {stats['total_chapters']}")
        print(f"   总token数: {stats['total_tokens']:,}")
        
        print("\n📖 章节详情:")
        for i, chapter in enumerate(stats['chapters'][:10]):  # 只显示前10个
            level_prefix = "  " * (chapter['level'] - 1)
            print(f"   {i+1}. {level_prefix}{chapter['title']}")
            print(f"      Tokens: {chapter['tokens']:,}, 子章节: {chapter['sub_sections_count']}")
            if chapter['sub_sections']:
                for sub in chapter['sub_sections'][:3]:  # 只显示前3个子章节
                    print(f"         • {sub}")
        
        if len(stats['chapters']) > 10:
            print(f"   ... 还有 {len(stats['chapters']) - 10} 个章节")
        
        print("\n📊 Token分布:")
        for range_key, count in stats['token_distribution'].items():
            print(f"   {range_key} tokens: {count} 个章节")