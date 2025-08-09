import asyncio
from pathlib import Path
from typing import Optional
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser.content_parser import MinerUParser
from src.parser.structure_analyzer import DocumentStructure
from src.summarizer.chunk_processor import ChunkProcessor
from src.summarizer.summary_generator import SummaryGenerator, SummaryPostProcessor
from src.output.markdown_formatter import MarkdownFormatter
from src.utils.config import load_config, Config


class MinerUSummarizer:
    """MinerU内容总结器主类"""
    
    def __init__(self, config: Config):
        self.config = config
        
    async def summarize(
        self, 
        input_dir: Path, 
        output_path: Path,
        compression_level: int = 50
    ) -> None:
        """执行总结任务"""
        print(f"开始处理MinerU数据: {input_dir}")
        print(f"压缩级别: {compression_level}%")
        print(f"输出路径: {output_path}")
        
        # 1. 解析MinerU数据
        print("\n步骤1: 解析MinerU数据...")
        parser = MinerUParser(input_dir)
        content_items, images = parser.parse()
        print(f"解析完成: {len(content_items)} 个内容项, {len(images)} 个图片")
        
        # 2. 分析文档结构
        print("\n步骤2: 分析文档结构...")
        structure_analyzer = DocumentStructure(content_items)
        sections = structure_analyzer.analyze()
        print(f"结构分析完成: {len(sections)} 个主要章节")
        
        if self.config.processing.preserve_structure:
            print("文档结构:")
            structure_analyzer.print_structure()
        
        # 3. 文档分块处理
        print("\n步骤3: 文档分块处理...")
        chunk_processor = ChunkProcessor(self.config.processing)
        flat_sections = structure_analyzer.get_flat_sections()
        chunks = chunk_processor.process_sections(flat_sections)
        
        stats = chunk_processor.get_chunk_stats()
        print(f"分块完成: {stats}")
        
        # 4. 生成总结
        print("\n步骤4: 生成总结...")
        async with SummaryGenerator(self.config) as generator:
            summaries = await generator.generate_summaries(chunks, compression_level)
        
        print(f"总结生成完成: {len(summaries)} 个总结块")
        
        # 5. 计算统计信息
        overall_stats = SummaryPostProcessor.calculate_overall_stats(summaries)
        print(f"总体统计: {overall_stats}")
        
        # 6. 格式化输出
        print("\n步骤5: 格式化输出...")
        formatter = MarkdownFormatter(self.config.output)
        
        # 尝试从原始文档获取标题
        original_title = self._extract_title(content_items)
        
        formatted_content = formatter.format_summaries(
            summaries=summaries,
            original_title=original_title,
            compression_level=compression_level,
            stats=overall_stats
        )
        
        # 7. 保存文件
        formatter.save_to_file(formatted_content, output_path)
        
        print(f"\n✅ 总结完成! 输出文件: {output_path}")
        print(f"原始内容: {overall_stats.get('total_original_tokens', 0):,} tokens")
        print(f"总结内容: {overall_stats.get('total_summary_tokens', 0):,} tokens") 
        print(f"压缩比: {overall_stats.get('overall_compression_ratio', 0):.2%}")
    
    def _extract_title(self, content_items) -> str:
        """从内容中提取标题"""
        for item in content_items[:5]:  # 只检查前5个项目
            if item.type == 'text' and item.text_level == 1:
                return item.text
            if item.type == 'text' and len(item.text) < 100 and not item.text.endswith('.'):
                return item.text
        return "学术论文"


async def main():
    """主函数"""
    # 简单的命令行参数解析
    if len(sys.argv) < 3:
        print("用法: python -m src.main <输入目录> <输出文件> [压缩级别] [配置文件]")
        print("示例: python -m src.main ./GFM_SURVEY ./summary.md 50")
        sys.exit(1)
    
    input_dir = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    compression_level = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    config_path = sys.argv[4] if len(sys.argv) > 4 else None
    
    # 验证输入目录
    if not input_dir.exists():
        print(f"错误: 输入目录不存在: {input_dir}")
        sys.exit(1)
    
    # 加载配置
    try:
        config = load_config(config_path)
        print(f"配置加载完成: LLM提供商={config.llm.provider}, 模型={config.llm.model}")
    except Exception as e:
        print(f"错误: 配置加载失败: {e}")
        sys.exit(1)
    
    # 验证API密钥
    if not config.llm.api_key:
        print("错误: 未配置API密钥，请设置环境变量或配置文件")
        print("OpenAI: 设置 OPENAI_API_KEY")
        print("Anthropic: 设置 ANTHROPIC_API_KEY")
        sys.exit(1)
    
    # 创建总结器并执行
    try:
        summarizer = MinerUSummarizer(config)
        await summarizer.summarize(input_dir, output_path, compression_level)
    except Exception as e:
        print(f"错误: 处理失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())