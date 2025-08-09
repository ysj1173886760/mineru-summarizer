import asyncio
from pathlib import Path
from typing import Optional
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser.chapter_parser import ChapterBasedParser, ChapterChunk
from src.summarizer.llm_client import LLMManager
from src.summarizer.summary_generator import SummaryResult, SummaryPostProcessor
from src.output.markdown_formatter_v2 import MarkdownFormatterV2
from src.utils.config import load_config, Config
from tqdm import tqdm


class MinerUSummarizerV4:
    """MinerU内容总结器 V4版本 - 大章节分片 + 二次打磨"""
    
    def __init__(self, config: Config):
        self.config = config
        
    async def summarize(
        self, 
        input_dir: Path, 
        output_path: Path,
        compression_level: int = 50,
        max_tokens_per_chapter: int = 8000,
        enable_polish: bool = True
    ) -> None:
        """执行总结任务"""
        print(f"🚀 开始处理MinerU数据 (V4版本 - 大章节分片 + 二次打磨): {input_dir}")
        print(f"📊 压缩级别: {compression_level}%")
        print(f"📄 输出路径: {output_path}")
        print(f"📚 最大章节token数: {max_tokens_per_chapter:,}")
        print(f"✨ 二次打磨: {'启用' if enable_polish else '禁用'}")
        
        # 1. 解析Markdown文档
        print("\n步骤1: 按大章节解析Markdown文档...")
        full_md_path = input_dir / "full.md"
        if not full_md_path.exists():
            raise FileNotFoundError(f"未找到full.md文件: {full_md_path}")
        
        parser = ChapterBasedParser(max_tokens_per_chapter=max_tokens_per_chapter)
        chapter_chunks = parser.parse_markdown_file(full_md_path)
        
        print(f"解析完成: {len(chapter_chunks)} 个大章节")
        parser.print_chapter_info(chapter_chunks)
        
        # 2. 生成初步总结
        print(f"\n步骤2: 生成初步总结...")
        summaries = await self._generate_summaries(chapter_chunks, compression_level)
        print(f"初步总结生成完成: {len(summaries)} 个总结块")
        
        # 3. 二次打磨（可选）
        if enable_polish:
            print(f"\n步骤3: 二次打磨总结...")
            polished_summaries = await self._polish_summaries(summaries, compression_level)
            print(f"打磨完成: {len(polished_summaries)} 个精化总结")
            final_summaries = polished_summaries
        else:
            final_summaries = summaries
        
        # 4. 计算统计信息
        overall_stats = SummaryPostProcessor.calculate_overall_stats(final_summaries)
        print(f"总体统计: {overall_stats}")
        
        # 5. 格式化输出
        print(f"\n步骤4: 格式化输出...")
        formatter = MarkdownFormatterV2(self.config.output)
        
        # 从第一个块提取标题
        original_title = self._extract_title(chapter_chunks)
        
        formatted_content = formatter.format_summaries(
            summaries=final_summaries,
            original_title=f"{original_title} (大章节分片{'+ 二次打磨' if enable_polish else ''}版)",
            compression_level=compression_level,
            stats=overall_stats
        )
        
        # 6. 保存文件
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
        """生成初步总结"""
        
        if compression_level not in self.config.compression_levels:
            raise ValueError(f"不支持的压缩级别: {compression_level}")
        
        compression_config = self.config.compression_levels[compression_level]
        
        print(f"开始生成初步总结 (压缩级别: {compression_level}%)")
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

重要要求:
1. 这是一个完整的大章节，请保持内容的连贯性和逻辑完整性
2. 重点突出章节的核心贡献和主要观点
3. 保持学术写作的严谨性和专业性
4. 对于包含多个子章节的内容，请按逻辑顺序组织总结
5. 专有技术名词保持英文原文，不要翻译，包括但不限于：
   - Graph Neural Networks (GNNs)
   - Graph Foundation Models (GFMs) 
   - Transformer
   - Graph Attention Networks (GAT)
   - GraphSAGE
   - Message Passing
   - Node Embedding
   - Graph Convolutional Networks (GCN)
   - Self-supervised Learning
   - Pre-training
   - Fine-tuning
   - In-context Learning
   - Few-shot Learning
   - Zero-shot Learning
   - Knowledge Graph
   - Heterogeneous Graph
   - Homogeneous Graph
   - Graph Isomorphism
   - Graph Pooling
   - Graph Classification
   - Node Classification
   - Link Prediction
   - Graph Generation
   - Graph Anomaly Detection
   - Contrastive Learning
   - Multi-modal Learning
   - Cross-domain Transfer
   - Domain Adaptation

原文内容:
{chunk.content}

请用中文回答，但保持上述英文技术术语："""
            
            prompts.append(full_prompt)
        
        # 批量调用LLM
        summaries = []
        async with LLMManager(
            self.config.llm, 
            max_concurrent=self.config.processing.max_concurrent
        ) as llm_manager:
            
            with tqdm(total=len(prompts), desc="生成初步总结") as pbar:
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
                                'chapter_parser': 'V4',
                                'polished': False
                            }
                        )
                        summaries.append(result)
                    
                    pbar.update(len(batch_prompts))
        
        return summaries
    
    async def _polish_summaries(
        self,
        summaries: list[SummaryResult],
        compression_level: int
    ) -> list[SummaryResult]:
        """二次打磨总结"""
        
        print(f"开始二次打磨 {len(summaries)} 个总结")
        
        # 生成打磨提示词
        polish_prompts = []
        for summary in summaries:
            polish_prompt = f"""你是一名专业的学术论文编辑，请对以下中文总结进行打磨和优化。

章节标题: {summary.section_title}
压缩级别: {compression_level}%

打磨要求:
1. 语言润色：提升表达的流畅性和准确性，使用更地道的中文学术表达
2. 逻辑优化：确保论点清晰，逻辑链条完整，重点突出
3. 术语统一：确保专有技术名词使用一致，保持英文原文
4. 结构完善：优化段落结构，提升可读性
5. 信息密度：在保持{compression_level}%信息量的基础上，提升信息的价值密度
6. 学术规范：符合中文学术写作规范，保持严谨性

需要保持英文的技术术语（请勿翻译）:
Graph Neural Networks (GNNs), Graph Foundation Models (GFMs), Transformer, Graph Attention Networks (GAT), GraphSAGE, Message Passing, Node Embedding, Graph Convolutional Networks (GCN), Self-supervised Learning, Pre-training, Fine-tuning, In-context Learning, Few-shot Learning, Zero-shot Learning, Knowledge Graph, Heterogeneous Graph, Homogeneous Graph, Graph Isomorphism, Graph Pooling, Graph Classification, Node Classification, Link Prediction, Graph Generation, Graph Anomaly Detection, Contrastive Learning, Multi-modal Learning, Cross-domain Transfer, Domain Adaptation

原始总结:
{summary.summary}

请输出打磨后的总结，直接给出最终结果，不要包含说明性文字："""
            
            polish_prompts.append(polish_prompt)
        
        # 批量打磨
        polished_summaries = []
        async with LLMManager(
            self.config.llm, 
            max_concurrent=max(1, self.config.processing.max_concurrent // 2)  # 降低并发以提高质量
        ) as llm_manager:
            
            with tqdm(total=len(polish_prompts), desc="打磨总结") as pbar:
                batch_size = max(1, self.config.processing.max_concurrent // 2)
                
                for i in range(0, len(polish_prompts), batch_size):
                    batch_prompts = polish_prompts[i:i+batch_size]
                    batch_summaries = summaries[i:i+batch_size]
                    
                    batch_results = await llm_manager.batch_generate(batch_prompts)
                    
                    # 创建打磨后的结果对象
                    for original_summary, polished_text in zip(batch_summaries, batch_results):
                        polished_result = SummaryResult(
                            chunk_id=original_summary.chunk_id,
                            original_content=original_summary.original_content,
                            summary=polished_text,
                            section_title=original_summary.section_title,
                            section_level=original_summary.section_level,
                            token_count=len(polished_text.split()),
                            compression_ratio=self._calculate_compression_ratio(
                                original_summary.original_content, polished_text
                            ),
                            metadata={
                                **original_summary.metadata,
                                'polished': True,
                                'original_summary_tokens': original_summary.token_count,
                                'polish_improvement_ratio': len(polished_text.split()) / original_summary.token_count if original_summary.token_count > 0 else 1.0
                            }
                        )
                        polished_summaries.append(polished_result)
                    
                    pbar.update(len(batch_prompts))
        
        return polished_summaries
    
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
        print("用法: python -m src.main_v4 <输入目录> <输出文件> [压缩级别] [最大章节token数] [是否打磨] [配置文件]")
        print("示例: python -m src.main_v4 ./GFM_SURVEY ./summary_v4.md 30 8000 true")
        sys.exit(1)
    
    input_dir = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    compression_level = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    max_tokens_per_chapter = int(sys.argv[4]) if len(sys.argv) > 4 else 8000
    enable_polish = sys.argv[5].lower() == 'true' if len(sys.argv) > 5 else True
    config_path = sys.argv[6] if len(sys.argv) > 6 else None
    
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
        summarizer = MinerUSummarizerV4(config)
        await summarizer.summarize(
            input_dir, 
            output_path, 
            compression_level, 
            max_tokens_per_chapter,
            enable_polish
        )
    except Exception as e:
        print(f"❌ 错误: 处理失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())