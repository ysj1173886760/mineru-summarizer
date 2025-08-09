from typing import List, Dict, Any, Optional
from pathlib import Path
import re
from datetime import datetime
from ..summarizer.summary_generator import SummaryResult, SummaryPostProcessor
from ..utils.config import OutputConfig
from ..parser.structure_analyzer import Section


class MarkdownFormatter:
    """Markdown格式化器"""
    
    def __init__(self, config: OutputConfig):
        self.config = config
        
    def format_summaries(
        self, 
        summaries: List[SummaryResult],
        original_title: str = "",
        compression_level: int = 50,
        stats: Optional[Dict[str, Any]] = None
    ) -> str:
        """格式化总结为Markdown"""
        
        # 构建文档头部
        header = self._build_header(original_title, compression_level, stats)
        
        # 生成目录
        toc = ""
        if self.config.include_toc:
            toc = self._generate_toc(summaries)
        
        # 格式化内容
        content = self._format_content(summaries)
        
        # 构建完整文档
        full_document = []
        
        if header:
            full_document.append(header)
        
        if toc:
            full_document.append(toc)
        
        if content:
            full_document.append(content)
        
        # 添加文档尾部
        footer = self._build_footer(stats)
        if footer:
            full_document.append(footer)
        
        return "\n\n".join(full_document)
    
    def _build_header(
        self, 
        original_title: str, 
        compression_level: int,
        stats: Optional[Dict[str, Any]] = None
    ) -> str:
        """构建文档头部"""
        header_parts = []
        
        # 主标题
        if original_title:
            title = f"{original_title} - 中文总结 ({compression_level}%)"
        else:
            title = f"学术论文中文总结 ({compression_level}%)"
        
        header_parts.append(f"# {title}")
        
        # 生成信息
        generation_info = [
            f"- **压缩级别**: {compression_level}%",
            f"- **生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"- **工具**: MinerU内容总结器"
        ]
        
        if stats:
            generation_info.extend([
                f"- **原始块数**: {stats.get('total_chunks', 'N/A')}",
                f"- **处理章节数**: {stats.get('sections_processed', 'N/A')}",
                f"- **压缩比**: {stats.get('overall_compression_ratio', 0):.2%}"
            ])
        
        header_parts.append("## 生成信息\n" + "\n".join(generation_info))
        
        return "\n\n".join(header_parts)
    
    def _generate_toc(self, summaries: List[SummaryResult]) -> str:
        """生成目录"""
        toc_parts = ["## 目录"]
        
        # 按章节分组并排序
        sections = {}
        for summary in summaries:
            section_key = (summary.section_level, summary.section_title)
            if section_key not in sections:
                sections[section_key] = True
        
        # 生成目录项
        sorted_sections = sorted(sections.keys(), key=lambda x: (x[0], x[1]))
        
        for level, title in sorted_sections:
            indent = "  " * (level - 1)
            anchor = self._create_anchor(title)
            toc_parts.append(f"{indent}- [{title}](#{anchor})")
        
        return "\n".join(toc_parts)
    
    def _format_content(self, summaries: List[SummaryResult]) -> str:
        """格式化主要内容"""
        # 按章节合并总结
        section_summaries = SummaryPostProcessor.merge_section_summaries(summaries)
        
        # 按章节级别和标题排序
        sorted_sections = []
        for section_key, content in section_summaries.items():
            # 从section_key中提取级别和标题
            parts = section_key.split('_', 1)
            if len(parts) == 2:
                level = int(parts[0])
                title = parts[1]
                sorted_sections.append((level, title, content))
        
        sorted_sections.sort(key=lambda x: (x[0], x[1]))
        
        # 格式化每个章节
        content_parts = []
        for level, title, content in sorted_sections:
            formatted_section = self._format_section(level, title, content)
            content_parts.append(formatted_section)
        
        return "\n\n".join(content_parts)
    
    def _format_section(self, level: int, title: str, content: str) -> str:
        """格式化单个章节"""
        # 创建标题
        header_prefix = "#" * (level + 1)  # +1 因为文档标题已经是 #
        section_header = f"{header_prefix} {title}"
        
        # 处理内容中的图片引用
        formatted_content = self._process_image_references(content)
        
        # 清理格式
        formatted_content = self._clean_formatting(formatted_content)
        
        return f"{section_header}\n\n{formatted_content}"
    
    def _process_image_references(self, content: str) -> str:
        """处理图片引用"""
        if not self.config.include_images:
            # 移除图片引用
            content = re.sub(r'!\[.*?\]\(.*?\)', '[图片已省略]', content)
            return content
        
        # 更新图片路径
        def replace_image_path(match):
            alt_text = match.group(1)
            original_path = match.group(2)
            
            # 如果是相对路径，添加前缀
            if not original_path.startswith(('http://', 'https://', '/')):
                new_path = f"{self.config.image_path_prefix}{Path(original_path).name}"
                return f"![{alt_text}]({new_path})"
            
            return match.group(0)
        
        content = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_image_path, content)
        return content
    
    def _clean_formatting(self, content: str) -> str:
        """清理格式问题"""
        # 移除多余的空行
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # 确保列表格式正确
        content = re.sub(r'\n(\s*[-*+])', r'\n\1', content)
        
        # 清理段落开头的空格
        lines = content.split('\n')
        cleaned_lines = []
        for line in lines:
            if line.strip() and not line.startswith(('#', '-', '*', '+')):
                cleaned_lines.append(line.strip())
            else:
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def _create_anchor(self, title: str) -> str:
        """创建锚点链接"""
        # 移除特殊字符，保留中文、英文、数字
        anchor = re.sub(r'[^\w\u4e00-\u9fff\s-]', '', title)
        # 替换空格为连字符
        anchor = re.sub(r'\s+', '-', anchor.strip())
        # 转为小写（英文部分）
        return anchor.lower()
    
    def _build_footer(self, stats: Optional[Dict[str, Any]] = None) -> str:
        """构建文档尾部"""
        if not stats:
            return ""
        
        footer_parts = ["---", "## 统计信息"]
        
        stat_items = [
            f"- **总处理块数**: {stats.get('total_chunks', 'N/A')}",
            f"- **原始总token数**: {stats.get('total_original_tokens', 'N/A'):,}",
            f"- **总结总token数**: {stats.get('total_summary_tokens', 'N/A'):,}",
            f"- **整体压缩比**: {stats.get('overall_compression_ratio', 0):.2%}",
            f"- **平均压缩比**: {stats.get('average_compression_ratio', 0):.2%}",
            f"- **处理章节数**: {stats.get('sections_processed', 'N/A')}"
        ]
        
        footer_parts.append("\n".join(stat_items))
        
        # 添加生成说明
        footer_parts.append(
            "\n*此文档由MinerU内容总结器自动生成，基于学术论文的MinerU提取数据。*"
        )
        
        return "\n\n".join(footer_parts)
    
    def save_to_file(self, content: str, output_path: Path) -> None:
        """保存到文件"""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"总结已保存到: {output_path}")


class HTMLFormatter:
    """HTML格式化器（可选扩展）"""
    
    def __init__(self, config: OutputConfig):
        self.config = config
    
    def markdown_to_html(self, markdown_content: str) -> str:
        """将Markdown转换为HTML（简单实现）"""
        try:
            import markdown
            md = markdown.Markdown(extensions=['toc', 'tables', 'fenced_code'])
            return md.convert(markdown_content)
        except ImportError:
            print("警告: 需要安装markdown库才能生成HTML格式")
            return markdown_content