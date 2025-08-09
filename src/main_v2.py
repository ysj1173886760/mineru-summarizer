import asyncio
from pathlib import Path
from typing import Optional
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser.markdown_parser import MarkdownDocumentParser, MarkdownChunk
from src.summarizer.llm_client import LLMManager
from src.summarizer.summary_generator import SummaryGenerator, SummaryResult, SummaryPostProcessor
from src.output.markdown_formatter_v2 import MarkdownFormatterV2
from src.utils.config import load_config, Config
from tqdm import tqdm


class MinerUSummarizerV2:
    """MinerU内容总结器 V2版本 - 基于Langchain Markdown分割"""
    
    def __init__(self, config: Config):
        self.config = config
        
    async def summarize(
        self, 
        input_dir: Path, 
        output_path: Path,
        compression_level: int = 50
    ) -> None:
        """执行总结任务"""
        print(f"🚀 开始处理MinerU数据 (V2版本): {input_dir}")
        print(f"📊 压缩级别: {compression_level}%")
        print(f"📄 输出路径: {output_path}")
        
        # 1. 解析Markdown文档
        print("\n步骤1: 解析Markdown文档...")
        full_md_path = input_dir / "full.md"
        if not full_md_path.exists():
            raise FileNotFoundError(f"未找到full.md文件: {full_md_path}")
        
        parser = MarkdownDocumentParser(
            chunk_size=self.config.processing.chunk_size,
            chunk_overlap=self.config.processing.overlap
        )
        
        markdown_chunks = parser.parse_markdown_file(full_md_path)
        print(f"解析完成: {len(markdown_chunks)} 个文档块")
        
        # 显示文档结构
        if self.config.processing.preserve_structure:
            parser.print_hierarchy(markdown_chunks)
        
        # 2. 生成总结
        print(f"\n步骤2: 生成总结...")
        summaries = await self._generate_summaries(markdown_chunks, compression_level)
        print(f"总结生成完成: {len(summaries)} 个总结块")
        
        # 3. 计算统计信息
        overall_stats = SummaryPostProcessor.calculate_overall_stats(summaries)
        print(f"总体统计: {overall_stats}")
        
        # 4. 格式化输出
        print(f"\n步骤3: 格式化输出...")
        formatter = MarkdownFormatterV2(self.config.output)
        
        # 从第一个块提取标题
        original_title = self._extract_title(markdown_chunks)
        
        formatted_content = formatter.format_summaries(
            summaries=summaries,
            original_title=original_title,
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
        markdown_chunks: list[MarkdownChunk], 
        compression_level: int
    ) -> list[SummaryResult]:
        """生成总结"""
        
        if compression_level not in self.config.compression_levels:
            raise ValueError(f"不支持的压缩级别: {compression_level}")
        
        compression_config = self.config.compression_levels[compression_level]
        
        print(f"开始生成总结 (压缩级别: {compression_level}%)")
        print(f"总共需要处理 {len(markdown_chunks)} 个文档块")
        
        # 生成提示词
        prompts = []
        for chunk in markdown_chunks:
            # 构建上下文信息
            context_info = ""
            if chunk.headers:
                header_path = " > ".join([h[1] for h in chunk.headers])
                context_info = f"\n\n章节路径: {header_path}"
            
            # 构建完整提示词
            full_prompt = f"""{compression_config.prompt_template}

{context_info}

特别要求:
- 保持学术写作的严谨性和专业性
- 使用中文学术写作的规范表达方式
- 如果内容很短或只是目录，请简洁地用中文描述其作用

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
                    batch_chunks = markdown_chunks[i:i+batch_size]
                    
                    batch_results = await llm_manager.batch_generate(batch_prompts)
                    
                    # 创建结果对象
                    for chunk, summary in zip(batch_chunks, batch_results):
                        # 确定章节标题和级别
                        section_title = chunk.headers[0][1] if chunk.headers else "Unknown"
                        section_level = chunk.headers[0][0] if chunk.headers else 1
                        
                        result = SummaryResult(
                            chunk_id=chunk.id,
                            original_content=chunk.content,
                            summary=summary,
                            section_title=section_title,
                            section_level=section_level,
                            token_count=len(summary.split()),
                            compression_ratio=self._calculate_compression_ratio(
                                chunk.content, summary
                            ),
                            metadata={
                                'compression_level': compression_level,
                                'strategy': compression_config.strategy,
                                'original_token_count': chunk.token_count,
                                'headers': chunk.headers,
                                'langchain_metadata': chunk.metadata
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
    
    def _extract_title(self, chunks: list[MarkdownChunk]) -> str:
        """从文档块中提取标题"""
        for chunk in chunks:
            if chunk.headers and chunk.headers[0][0] == 1:
                return chunk.headers[0][1]
        return "学术论文"


async def main():
    """主函数"""
    # 简单的命令行参数解析
    if len(sys.argv) < 3:
        print("用法: python -m src.main_v2 <输入目录> <输出文件> [压缩级别] [配置文件]")
        print("示例: python -m src.main_v2 ./GFM_SURVEY ./summary_v2.md 30")
        sys.exit(1)
    
    input_dir = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    compression_level = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    config_path = sys.argv[4] if len(sys.argv) > 4 else None
    
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
        summarizer = MinerUSummarizerV2(config)
        await summarizer.summarize(input_dir, output_path, compression_level)
    except Exception as e:
        print(f"❌ 错误: 处理失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())