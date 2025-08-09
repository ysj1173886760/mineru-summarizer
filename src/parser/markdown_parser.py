from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from ..utils.helpers import count_tokens


@dataclass
class MarkdownChunk:
    """Markdown文档块"""
    id: str
    content: str
    metadata: Dict[str, Any]
    token_count: int
    headers: List[tuple]  # [(level, title), ...]


class MarkdownDocumentParser:
    """基于Langchain的Markdown文档解析器"""
    
    def __init__(self, chunk_size: int = 3000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # 定义标题分割器的层级
        self.headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"), 
            ("###", "Header 3"),
            ("####", "Header 4"),
            ("#####", "Header 5"),
            ("######", "Header 6"),
        ]
        
        # 创建markdown标题分割器
        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.headers_to_split_on,
            strip_headers=False
        )
        
        # 创建字符分割器（用于处理过长的块）
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=count_tokens,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def parse_markdown_file(self, file_path: Path) -> List[MarkdownChunk]:
        """解析Markdown文件"""
        
        # 读取markdown内容
        with open(file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # 清理内容
        markdown_content = self._clean_markdown(markdown_content)
        
        # 第一步：按标题分割
        header_chunks = self.markdown_splitter.split_text(markdown_content)
        
        # 第二步：处理过长的块
        final_chunks = []
        for i, chunk in enumerate(header_chunks):
            token_count = count_tokens(chunk.page_content)
            
            if token_count <= self.chunk_size:
                # 块大小合适，直接使用
                markdown_chunk = MarkdownChunk(
                    id=f"chunk_{i}",
                    content=chunk.page_content,
                    metadata=chunk.metadata,
                    token_count=token_count,
                    headers=self._extract_headers(chunk.metadata)
                )
                final_chunks.append(markdown_chunk)
            else:
                # 块太大，需要进一步分割
                sub_chunks = self.text_splitter.split_text(chunk.page_content)
                for j, sub_chunk in enumerate(sub_chunks):
                    sub_token_count = count_tokens(sub_chunk)
                    markdown_chunk = MarkdownChunk(
                        id=f"chunk_{i}_{j}",
                        content=sub_chunk,
                        metadata=chunk.metadata,
                        token_count=sub_token_count,
                        headers=self._extract_headers(chunk.metadata)
                    )
                    final_chunks.append(markdown_chunk)
        
        return final_chunks
    
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
    
    def _extract_headers(self, metadata: Dict[str, Any]) -> List[tuple]:
        """从metadata中提取标题层级信息"""
        headers = []
        for key, value in metadata.items():
            if key.startswith('Header ') and value:
                level = int(key.split(' ')[1])
                headers.append((level, value))
        
        # 按层级排序
        headers.sort(key=lambda x: x[0])
        return headers
    
    def get_chunk_hierarchy(self, chunks: List[MarkdownChunk]) -> Dict[str, Any]:
        """分析文档块的层次结构"""
        hierarchy = {
            'total_chunks': len(chunks),
            'total_tokens': sum(chunk.token_count for chunk in chunks),
            'sections': {},
            'chunk_distribution': {}
        }
        
        # 统计各个标题下的块数量
        for chunk in chunks:
            if chunk.headers:
                # 使用最高级别的标题作为主分类
                main_header = chunk.headers[0][1] if chunk.headers else 'Unknown'
                if main_header not in hierarchy['sections']:
                    hierarchy['sections'][main_header] = {
                        'chunks': 0,
                        'tokens': 0,
                        'level': chunk.headers[0][0] if chunk.headers else 0
                    }
                
                hierarchy['sections'][main_header]['chunks'] += 1
                hierarchy['sections'][main_header]['tokens'] += chunk.token_count
        
        # 统计token分布
        token_ranges = [(0, 500), (500, 1000), (1000, 2000), (2000, 3000), (3000, float('inf'))]
        for start, end in token_ranges:
            range_key = f"{start}-{end if end != float('inf') else 'inf'}"
            count = len([c for c in chunks if start <= c.token_count < end])
            hierarchy['chunk_distribution'][range_key] = count
        
        return hierarchy
    
    def print_hierarchy(self, chunks: List[MarkdownChunk]) -> None:
        """打印文档层次结构"""
        hierarchy = self.get_chunk_hierarchy(chunks)
        
        print("📊 文档结构分析:")
        print(f"   总块数: {hierarchy['total_chunks']}")
        print(f"   总token数: {hierarchy['total_tokens']:,}")
        
        print("\n📚 章节分布:")
        sections = sorted(hierarchy['sections'].items(), 
                         key=lambda x: x[1]['level'])
        for section, info in sections:
            level_prefix = "  " * (info['level'] - 1)
            print(f"   {level_prefix}• {section}: {info['chunks']} 块, {info['tokens']:,} tokens")
        
        print("\n📈 Token分布:")  
        for range_key, count in hierarchy['chunk_distribution'].items():
            print(f"   {range_key} tokens: {count} 块")


def main():
    """测试函数"""
    parser = MarkdownDocumentParser(chunk_size=2000, chunk_overlap=100)
    
    # 测试解析GFM_SURVEY的full.md
    md_file = Path("../GFM_SURVEY/full.md")
    if md_file.exists():
        print(f"解析文件: {md_file}")
        chunks = parser.parse_markdown_file(md_file)
        
        parser.print_hierarchy(chunks)
        
        print(f"\n前3个块的内容预览:")
        for i, chunk in enumerate(chunks[:3]):
            print(f"\n块 {i+1} (ID: {chunk.id}):")
            print(f"   Headers: {chunk.headers}")
            print(f"   Tokens: {chunk.token_count}")
            print(f"   Content preview: {chunk.content[:200]}...")
    else:
        print(f"文件不存在: {md_file}")


if __name__ == "__main__":
    main()