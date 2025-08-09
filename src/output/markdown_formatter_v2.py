from typing import List, Dict, Any, Optional
from pathlib import Path
import re
from datetime import datetime
from ..summarizer.summary_generator import SummaryResult, SummaryPostProcessor
from ..utils.config import OutputConfig


class MarkdownFormatterV2:
    """V2版本的Markdown格式化器 - 支持更好的章节排序"""
    
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
            f"- **工具**: MinerU内容总结器 V2"
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
        
        # 收集并排序章节
        sections = []
        for summary in summaries:
            sections.append((summary.section_level, summary.section_title))
        
        # 去重并排序
        seen = set()
        unique_sections = []
        for level, title in sections:
            if (level, title) not in seen:
                seen.add((level, title))
                unique_sections.append((level, title))
        
        # 智能排序：先按章节编号，再按字母顺序
        sorted_sections = self._smart_sort_sections(unique_sections)
        
        # 生成目录项
        for level, title in sorted_sections:
            indent = "  " * (level - 1) if level > 0 else ""
            anchor = self._create_anchor(title)
            toc_parts.append(f"{indent}- [{title}](#{anchor})")
        
        return "\n".join(toc_parts)
    
    def _smart_sort_sections(self, sections: List[tuple]) -> List[tuple]:
        """智能排序章节：按章节编号优先，然后字母顺序"""
        
        def extract_chapter_number(title: str) -> tuple:
            """提取章节编号用于排序"""
            # 匹配各种章节编号格式
            patterns = [
                r'^(\d+)\.(\d+)\.(\d+)\s',  # 1.2.3 格式
                r'^(\d+)\.(\d+)\s',         # 1.2 格式  
                r'^(\d+)\s',                # 1 格式
            ]
            
            for pattern in patterns:
                match = re.match(pattern, title)
                if match:
                    numbers = [int(x) for x in match.groups()]
                    # 补齐到3位数字，便于排序
                    while len(numbers) < 3:
                        numbers.append(0)
                    return tuple(numbers)
            
            # 如果没有匹配到数字，按特殊规则处理
            if title.upper().startswith('ABSTRACT'):
                return (0, 0, 1)  # Abstract排在最前
            elif title.upper().startswith('CONTENTS'):
                return (0, 0, 2)  # Contents排在Abstract后
            elif 'CONCLUSION' in title.upper():
                return (999, 0, 0)  # Conclusion排在最后
            elif 'REFERENCE' in title.upper():
                return (999, 1, 0)  # References排在Conclusion后
            else:
                # 按字母顺序排序，但放在有数字章节之后
                return (900, ord(title[0].upper()) if title else 900, 0)
        
        # 按提取的章节编号排序
        sections_with_sort_key = []
        for level, title in sections:
            sort_key = extract_chapter_number(title)
            sections_with_sort_key.append((sort_key, level, title))
        
        sections_with_sort_key.sort(key=lambda x: x[0])
        
        # 返回排序后的结果
        return [(level, title) for _, level, title in sections_with_sort_key]
    
    def _format_content(self, summaries: List[SummaryResult]) -> str:
        """格式化主要内容"""
        # 按章节合并总结
        section_summaries = SummaryPostProcessor.merge_section_summaries(summaries)
        
        # 创建包含级别信息的章节列表
        sections_with_level = []
        for summary in summaries:
            section_key = f"{summary.section_level}_{summary.section_title}"
            if section_key in section_summaries:
                sections_with_level.append((
                    summary.section_level, 
                    summary.section_title, 
                    section_summaries[section_key]
                ))
                # 避免重复添加
                del section_summaries[section_key]
        
        # 智能排序
        sorted_sections = self._smart_sort_sections([(level, title) for level, title, _ in sections_with_level])
        
        # 重新组织内容
        sorted_sections_with_content = []
        for level, title in sorted_sections:
            # 找到对应的内容
            for orig_level, orig_title, content in sections_with_level:
                if orig_level == level and orig_title == title:
                    sorted_sections_with_content.append((level, title, content))
                    break
        
        # 格式化每个章节
        content_parts = []
        for level, title, content in sorted_sections_with_content:
            formatted_section = self._format_section(level, title, content)
            content_parts.append(formatted_section)
        
        return "\n\n".join(content_parts)
    
    def _format_section(self, level: int, title: str, content: str) -> str:
        """格式化单个章节"""
        # 创建标题
        header_prefix = "#" * 2  # 统一使用 ## 级别
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
            "\n*此文档由MinerU内容总结器V2自动生成，基于Langchain Markdown分割技术。*"
        )
        
        return "\n\n".join(footer_parts)
    
    def save_to_file(self, content: str, output_path: Path) -> None:
        """保存到文件"""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"总结已保存到: {output_path}")