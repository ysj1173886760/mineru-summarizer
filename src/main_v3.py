import asyncio
from pathlib import Path
from typing import Optional
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser.chapter_parser import ChapterBasedParser, ChapterChunk
from src.summarizer.llm_client import LLMManager
from src.summarizer.summary_generator import SummaryGenerator, SummaryResult, SummaryPostProcessor
from src.output.markdown_formatter_v2 import MarkdownFormatterV2
from src.utils.config import load_config, Config
from tqdm import tqdm


class MinerUSummarizerV3:
    """MinerU内容总结器 V3版本 - 基于大章节分片"""
    
    def __init__(self, config: Config):
        self.config = config
        
    async def summarize(
        self, 
        input_dir: Path, 
        output_path: Path,
        compression_level: int = 50,
        max_tokens_per_chapter: int = 8000
    ) -> None:
        """执行总结任务"""
        print(f"🚀 开始处理MinerU数据 (V3版本 - 大章节分片): {input_dir}")
        print(f"📊 压缩级别: {compression_level}%")
        print(f"📄 输出路径: {output_path}")
        print(f"📚 最大章节token数: {max_tokens_per_chapter:,}")
        
        # 1. 解析Markdown文档
        print("\n步骤1: 按大章节解析Markdown文档...")
        full_md_path = input_dir / "full.md"
        if not full_md_path.exists():
            raise FileNotFoundError(f"未找到full.md文件: {full_md_path}")
        
        parser = ChapterBasedParser(max_tokens_per_chapter=max_tokens_per_chapter)
        chapter_chunks = parser.parse_markdown_file(full_md_path)
        
        print(f"解析完成: {len(chapter_chunks)} 个大章节")
        parser.print_chapter_info(chapter_chunks)
        
        # 2. 生成总结
        print(f"\n步骤2: 生成总结...")
        summaries = await self._generate_summaries(chapter_chunks, compression_level)
        print(f"总结生成完成: {len(summaries)} 个总结块")
        
        # 3. 计算统计信息
        overall_stats = SummaryPostProcessor.calculate_overall_stats(summaries)
        print(f"总体统计: {overall_stats}")
        
        # 4. 格式化输出
        print(f"\n步骤3: 格式化输出...")
        formatter = MarkdownFormatterV2(self.config.output)
        
        # 从第一个块提取标题
        original_title = self._extract_title(chapter_chunks)
        
        formatted_content = formatter.format_summaries(
            summaries=summaries,
            original_title=f"{original_title} (大章节分片版)",
            compression_level=compression_level,
            stats=overall_stats
        )
        
        # 5. 保存文件
        formatter.save_to_file(formatted_content, output_path)
        
        print(f"\n✅ 总结完成! 输出文件: {output_path}")
        print(f"📊 原始内容: {overall_stats.get('total_original_tokens', 0):,} tokens")
        print(f"📝 总结内容: {overall_stats.get('total_summary_tokens', 0):,} tokens") 
        print(f"🎯 压缩比: {overall_stats.get('overall_compression_ratio', 0):.2%}")
    
    async def _generate_summaries(
        self, 
        chapter_chunks: list[ChapterChunk], 
        compression_level: int
    ) -> list[SummaryResult]:
        """生成总结"""
        
        if compression_level not in self.config.compression_levels:
            raise ValueError(f"不支持的压缩级别: {compression_level}")
        
        compression_config = self.config.compression_levels[compression_level]
        
        print(f"开始生成总结 (压缩级别: {compression_level}%)")
        print(f"总共需要处理 {len(chapter_chunks)} 个大章节")
        
        # 生成提示词
        prompts = []
        for chunk in chapter_chunks:
            # 构建章节上下文信息
            context_info = f"\n\n章节标题: {chunk.chapter_title}"
            if chunk.sub_sections:
                context_info += f"\n子章节: {', '.join(chunk.sub_sections[:5])}"
                if len(chunk.sub_sections) > 5:
                    context_info += f" (还有{len(chunk.sub_sections)-5}个子章节)"
            context_info += f"\n章节规模: {chunk.token_count:,} tokens"
            
            # 构建完整提示词
            full_prompt = f"""{compression_config.prompt_template}

{context_info}

特别要求:
- 这是一个完整的大章节，请保持内容的连贯性和逻辑完整性
- 重点突出章节的核心贡献和主要观点
- 保持学术写作的严谨性和专业性
- 对于包含多个子章节的内容，请按逻辑顺序组织总结

原文内容:
{chunk.content}

请用中文回答："""
            
            prompts.append(full_prompt)
        
        # 批量调用LLM
        summaries = []
        async with LLMManager(
            self.config.llm, 
            max_concurrent=self.config.processing.max_concurrent
        ) as llm_manager:
            
            with tqdm(total=len(prompts), desc="生成总结") as pbar:
                batch_size = self.config.processing.max_concurrent
                
                for i in range(0, len(prompts), batch_size):
                    batch_prompts = prompts[i:i+batch_size]
                    batch_chunks = chapter_chunks[i:i+batch_size]
                    
                    batch_results = await llm_manager.batch_generate(batch_prompts)
                    
                    # 创建结果对象
                    for chunk, summary in zip(batch_chunks, batch_results):
                        result = SummaryResult(
                            chunk_id=chunk.id,
                            original_content=chunk.content,
                            summary=summary,
                            section_title=chunk.chapter_title,
                            section_level=chunk.chapter_level,
                            token_count=len(summary.split()),
                            compression_ratio=self._calculate_compression_ratio(
                                chunk.content, summary
                            ),
                            metadata={
                                'compression_level': compression_level,
                                'strategy': compression_config.strategy,
                                'original_token_count': chunk.token_count,
                                'sub_sections': chunk.sub_sections,
                                'chapter_parser': 'V3'
                            }
                        )
                        summaries.append(result)
                    
                    pbar.update(len(batch_prompts))
        
        return summaries
    
    def _calculate_compression_ratio(self, original: str, summary: str) -> float:
        """计算压缩比例"""
        original_length = len(original)
        summary_length = len(summary)
        
        if original_length == 0:
            return 0.0
        
        return summary_length / original_length
    
    def _extract_title(self, chunks: list[ChapterChunk]) -> str:
        """从文档块中提取标题"""
        for chunk in chunks:
            if chunk.chapter_level == 1 and not chunk.chapter_title.startswith('Chapter'):
                return chunk.chapter_title
        return "学术论文"


async def main():
    """主函数"""
    # 简单的命令行参数解析
    if len(sys.argv) < 3:
        print("用法: python -m src.main_v3 <输入目录> <输出文件> [压缩级别] [最大章节token数] [配置文件]")
        print("示例: python -m src.main_v3 ./GFM_SURVEY ./summary_v3.md 30 8000")
        sys.exit(1)
    
    input_dir = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    compression_level = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    max_tokens_per_chapter = int(sys.argv[4]) if len(sys.argv) > 4 else 8000
    config_path = sys.argv[5] if len(sys.argv) > 5 else None
    
    # 验证输入目录
    if not input_dir.exists():
        print(f"错误: 输入目录不存在: {input_dir}")
        sys.exit(1)
    
    full_md_path = input_dir / "full.md"
    if not full_md_path.exists():
        print(f"错误: 未找到full.md文件: {full_md_path}")
        sys.exit(1)
    
    # 加载配置
    try:
        config = load_config(config_path)
        print(f"✅ 配置加载完成: LLM提供商={config.llm.provider}, 模型={config.llm.model}")
    except Exception as e:
        print(f"❌ 错误: 配置加载失败: {e}")
        sys.exit(1)
    
    # 验证API密钥
    if not config.llm.api_key:
        print("❌ 错误: 未配置API密钥，请设置环境变量或配置文件")
        print("OpenAI: 设置 OPENAI_API_KEY")
        print("Anthropic: 设置 ANTHROPIC_API_KEY")
        sys.exit(1)
    
    # 创建总结器并执行
    try:
        summarizer = MinerUSummarizerV3(config)
        await summarizer.summarize(
            input_dir, 
            output_path, 
            compression_level, 
            max_tokens_per_chapter
        )
    except Exception as e:
        print(f"❌ 错误: 处理失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())