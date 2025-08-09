import asyncio
from pathlib import Path
from typing import Optional, List
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser.chapter_parser import ChapterBasedParser, ChapterChunk
from src.summarizer.claude_cli_client import ClaudeCLIManager, ClaudeCLIConfig
from src.summarizer.summary_generator import SummaryResult, SummaryPostProcessor
from src.output.markdown_formatter_v2 import MarkdownFormatterV2
from src.utils.config import load_config, Config
from src.utils.checkpoint import CheckpointManager, CheckpointState, print_checkpoints_table
from tqdm import tqdm
from datetime import datetime


class MinerUSummarizerV6:
    """MinerU内容总结器 V6版本 - 带检查点恢复功能的Claude CLI版本"""
    
    def __init__(self, config: Config, checkpoint_dir: Path = None):
        self.config = config
        self.checkpoint_manager = CheckpointManager(checkpoint_dir)
        
    async def summarize(
        self, 
        input_dir: Path, 
        output_path: Path,
        compression_level: int = 50,
        max_tokens_per_chapter: int = 8000,
        enable_polish: bool = True,
        claude_project: Optional[str] = None,
        claude_model: Optional[str] = None,
        resume_session: Optional[str] = None
    ) -> None:
        """执行总结任务"""
        
        if resume_session:
            # 恢复执行
            await self._resume_summarize(resume_session)
        else:
            # 新的执行
            await self._new_summarize(
                input_dir, output_path, compression_level, max_tokens_per_chapter,
                enable_polish, claude_project, claude_model
            )
    
    async def _new_summarize(
        self,
        input_dir: Path, 
        output_path: Path,
        compression_level: int,
        max_tokens_per_chapter: int,
        enable_polish: bool,
        claude_project: Optional[str],
        claude_model: Optional[str]
    ) -> None:
        """新的总结任务"""
        
        print(f"🚀 开始处理MinerU数据 (V6版本 - 带检查点的Claude CLI): {input_dir}")
        print(f"📊 压缩级别: {compression_level}%")
        print(f"📄 输出路径: {output_path}")
        print(f"📚 最大章节token数: {max_tokens_per_chapter:,}")
        print(f"✨ 二次打磨: {'启用' if enable_polish else '禁用'}")
        print(f"🤖 Claude项目: {claude_project or '默认'}")
        print(f"🧠 Claude模型: {claude_model or '默认'}")
        
        # 1. 解析Markdown文档
        print("\n步骤1: 按大章节解析Markdown文档...")
        full_md_path = input_dir / "full.md"
        if not full_md_path.exists():
            raise FileNotFoundError(f"未找到full.md文件: {full_md_path}")
        
        parser = ChapterBasedParser(max_tokens_per_chapter=max_tokens_per_chapter)
        chapter_chunks = parser.parse_markdown_file(full_md_path)
        
        print(f"解析完成: {len(chapter_chunks)} 个大章节")
        parser.print_chapter_info(chapter_chunks)
        
        # 2. 创建检查点状态
        session_id = self.checkpoint_manager.create_session_id(input_dir, compression_level)
        state = CheckpointState(
            session_id=session_id,
            input_dir=str(input_dir.absolute()),
            output_path=str(output_path.absolute()),
            compression_level=compression_level,
            max_tokens_per_chapter=max_tokens_per_chapter,
            enable_polish=enable_polish,
            claude_project=claude_project,
            claude_model=claude_model,
            total_chapters=len(chapter_chunks),
            processed_chapters=0,
            current_stage="initial_summary",
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
            chapters_file="",
            summaries_file="",
            polished_summaries_file=None,
            completed_chapter_ids=[],
            failed_chapter_ids=[],
            error_log=[]
        )
        
        # 保存初始检查点
        self.checkpoint_manager.save_checkpoint(state, chapters=chapter_chunks)
        print(f"💾 已创建会话: {session_id}")
        
        # 3. 生成初步总结
        print(f"\n步骤2: 生成初步总结...")
        summaries = await self._generate_summaries_with_checkpoint(
            chapter_chunks, compression_level, claude_project, claude_model, state
        )
        print(f"初步总结生成完成: {len(summaries)} 个总结块")
        
        # 4. 二次打磨（可选）
        final_summaries = summaries
        if enable_polish and summaries:
            print(f"\n步骤3: 二次打磨总结...")
            state.current_stage = "polish"
            state.processed_chapters = 0  # 重置进度用于打磨阶段
            state.completed_chapter_ids = []
            self.checkpoint_manager.save_checkpoint(state, summaries=summaries)
            
            polished_summaries = await self._polish_summaries_with_checkpoint(
                summaries, compression_level, claude_project, claude_model, state
            )
            print(f"打磨完成: {len(polished_summaries)} 个精化总结")
            final_summaries = polished_summaries
        
        # 5. 完成处理
        await self._finalize_summary(final_summaries, state, chapter_chunks)
    
    async def _resume_summarize(self, session_id: str) -> None:
        """恢复总结任务"""
        print(f"🔄 恢复会话: {session_id}")
        
        # 加载检查点
        try:
            state, chapters, summaries, polished_summaries = self.checkpoint_manager.load_checkpoint(session_id)
        except FileNotFoundError:
            print(f"❌ 检查点不存在: {session_id}")
            return
        
        print(f"📊 恢复状态: {state.current_stage}")
        print(f"📈 已完成: {len(state.completed_chapter_ids)}/{state.total_chapters}")
        print(f"❌ 失败数量: {len(state.failed_chapter_ids)}")
        
        if state.current_stage == "initial_summary":
            # 继续生成初步总结
            print("\n继续生成初步总结...")
            summaries = await self._generate_summaries_with_checkpoint(
                chapters, state.compression_level, state.claude_project, state.claude_model, state,
                existing_summaries=summaries
            )
            
            # 检查是否需要打磨
            if state.enable_polish and summaries:
                print(f"\n开始二次打磨...")
                state.current_stage = "polish"
                state.processed_chapters = 0
                state.completed_chapter_ids = []
                self.checkpoint_manager.save_checkpoint(state, summaries=summaries)
                
                polished_summaries = await self._polish_summaries_with_checkpoint(
                    summaries, state.compression_level, state.claude_project, state.claude_model, state
                )
                final_summaries = polished_summaries
            else:
                final_summaries = summaries
                
        elif state.current_stage == "polish":
            # 继续二次打磨
            print("\n继续二次打磨...")
            polished_summaries = await self._polish_summaries_with_checkpoint(
                summaries, state.compression_level, state.claude_project, state.claude_model, state,
                existing_polished=polished_summaries
            )
            final_summaries = polished_summaries
            
        elif state.current_stage == "completed":
            print("✅ 会话已完成，生成最终输出...")
            final_summaries = polished_summaries if polished_summaries else summaries
        else:
            print(f"❌ 未知状态: {state.current_stage}")
            return
        
        # 完成处理
        await self._finalize_summary(final_summaries, state, chapters)
    
    async def _generate_summaries_with_checkpoint(
        self,
        chapter_chunks: List[ChapterChunk],
        compression_level: int,
        claude_project: Optional[str],
        claude_model: Optional[str],
        state: CheckpointState,
        existing_summaries: List[SummaryResult] = None
    ) -> List[SummaryResult]:
        """带检查点的总结生成"""
        
        if compression_level not in self.config.compression_levels:
            raise ValueError(f"不支持的压缩级别: {compression_level}")
        
        compression_config = self.config.compression_levels[compression_level]
        
        # 初始化结果列表
        summaries = existing_summaries or []
        completed_ids = set(state.completed_chapter_ids)
        failed_ids = set(state.failed_chapter_ids)
        
        # 过滤需要处理的章节
        pending_chunks = [chunk for chunk in chapter_chunks 
                         if chunk.id not in completed_ids and chunk.id not in failed_ids]
        
        if not pending_chunks:
            print("✅ 所有章节已处理完成")
            return summaries
        
        print(f"📝 需要处理 {len(pending_chunks)} 个章节 (跳过 {len(completed_ids)} 个已完成, {len(failed_ids)} 个失败)")
        
        # 创建Claude CLI管理器
        claude_config = ClaudeCLIConfig(
            project_name=claude_project,
            model=claude_model,
            max_tokens=self.config.llm.max_tokens,
            temperature=self.config.llm.temperature,
            timeout=180
        )
        
        # 处理章节
        async with ClaudeCLIManager(
            claude_config, 
            max_concurrent=self.config.processing.max_concurrent
        ) as claude_manager:
            
            with tqdm(total=len(pending_chunks), desc="生成总结", initial=len(completed_ids)) as pbar:
                # 逐个处理以便实时保存检查点
                for chunk in pending_chunks:
                    try:
                        # 构建提示词
                        context_info = f"\n\n章节标题: {chunk.chapter_title}"
                        if chunk.sub_sections:
                            context_info += f"\n子章节: {', '.join(chunk.sub_sections[:5])}"
                            if len(chunk.sub_sections) > 5:
                                context_info += f" (还有{len(chunk.sub_sections)-5}个子章节)"
                        context_info += f"\n章节规模: {chunk.token_count:,} tokens"
                        
                        full_prompt = f"""{compression_config.prompt_template}

{context_info}

重要要求:
1. 这是一个完整的大章节，请保持内容的连贯性和逻辑完整性
2. 重点突出章节的核心贡献和主要观点
3. 保持学术写作的严谨性和专业性
4. 对于包含多个子章节的内容，请按逻辑顺序组织总结
5. 专有技术名词保持英文原文，不要翻译，包括但不限于：
   - Graph Neural Networks (GNNs), Graph Foundation Models (GFMs), Transformer
   - Graph Attention Networks (GAT), GraphSAGE, Message Passing, Node Embedding
   - Graph Convolutional Networks (GCN), Self-supervised Learning, Pre-training
   - Fine-tuning, In-context Learning, Few-shot Learning, Zero-shot Learning
   - Knowledge Graph, Heterogeneous Graph, Homogeneous Graph, Graph Isomorphism
   - Graph Pooling, Graph Classification, Node Classification, Link Prediction
   - Graph Generation, Graph Anomaly Detection, Contrastive Learning
   - Multi-modal Learning, Cross-domain Transfer, Domain Adaptation

原文内容:
{chunk.content}

请用中文回答，但保持上述英文技术术语："""
                        
                        # 调用Claude CLI
                        summary_text = await claude_manager.single_generate(full_prompt)
                        
                        # 创建结果对象
                        result = SummaryResult(
                            chunk_id=chunk.id,
                            original_content=chunk.content,
                            summary=summary_text,
                            section_title=chunk.chapter_title,
                            section_level=chunk.chapter_level,
                            token_count=len(summary_text.split()),
                            compression_ratio=self._calculate_compression_ratio(chunk.content, summary_text),
                            metadata={
                                'compression_level': compression_level,
                                'strategy': compression_config.strategy,
                                'original_token_count': chunk.token_count,
                                'sub_sections': chunk.sub_sections,
                                'chapter_parser': 'V6',
                                'claude_cli': True,
                                'claude_project': claude_project,
                                'claude_model': claude_model,
                                'polished': False
                            }
                        )
                        
                        summaries.append(result)
                        state.completed_chapter_ids.append(chunk.id)
                        state.processed_chapters = len(state.completed_chapter_ids)
                        
                        # 每处理一个章节就保存检查点
                        self.checkpoint_manager.save_checkpoint(state, summaries=summaries)
                        
                        pbar.update(1)
                        
                    except Exception as e:
                        error_info = {
                            'chunk_id': chunk.id,
                            'chapter_title': chunk.chapter_title,
                            'error': str(e),
                            'timestamp': datetime.now().isoformat()
                        }
                        state.failed_chapter_ids.append(chunk.id)
                        state.error_log.append(error_info)
                        
                        print(f"\n❌ 章节处理失败: {chunk.chapter_title}")
                        print(f"   错误: {str(e)}")
                        
                        # 保存失败状态
                        self.checkpoint_manager.save_checkpoint(state, summaries=summaries)
                        
                        # 如果是限流错误，提示用户
                        if "rate limit" in str(e).lower() or "429" in str(e):
                            print(f"⏸️ 检测到限流错误，已保存检查点")
                            print(f"   可以稍后运行以下命令恢复: python -m src.main_v6 --resume {state.session_id}")
                            break
                        
                        pbar.update(1)
        
        return summaries
    
    async def _polish_summaries_with_checkpoint(
        self,
        summaries: List[SummaryResult],
        compression_level: int,
        claude_project: Optional[str],
        claude_model: Optional[str],
        state: CheckpointState,
        existing_polished: List[SummaryResult] = None
    ) -> List[SummaryResult]:
        """带检查点的二次打磨"""
        
        # 初始化结果列表
        polished_summaries = existing_polished or []
        completed_ids = set(state.completed_chapter_ids)
        failed_ids = set(state.failed_chapter_ids)
        
        # 过滤需要处理的总结
        pending_summaries = [s for s in summaries 
                           if s.chunk_id not in completed_ids and s.chunk_id not in failed_ids]
        
        if not pending_summaries:
            print("✅ 所有总结已打磨完成")
            return polished_summaries
        
        print(f"🎨 需要打磨 {len(pending_summaries)} 个总结")
        
        # 创建Claude CLI管理器
        claude_config = ClaudeCLIConfig(
            project_name=claude_project,
            model=claude_model,
            max_tokens=self.config.llm.max_tokens,
            temperature=0.2,
            timeout=120
        )
        
        # 处理打磨
        async with ClaudeCLIManager(
            claude_config, 
            max_concurrent=max(1, self.config.processing.max_concurrent // 2)
        ) as claude_manager:
            
            with tqdm(total=len(pending_summaries), desc="打磨总结", initial=len(completed_ids)) as pbar:
                for summary in pending_summaries:
                    try:
                        # 构建打磨提示词
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
                        
                        # 调用打磨
                        polished_text = await claude_manager.single_generate(polish_prompt)
                        
                        # 创建打磨后的结果
                        polished_result = SummaryResult(
                            chunk_id=summary.chunk_id,
                            original_content=summary.original_content,
                            summary=polished_text,
                            section_title=summary.section_title,
                            section_level=summary.section_level,
                            token_count=len(polished_text.split()),
                            compression_ratio=self._calculate_compression_ratio(summary.original_content, polished_text),
                            metadata={
                                **summary.metadata,
                                'polished': True,
                                'original_summary_tokens': summary.token_count,
                                'polish_improvement_ratio': len(polished_text.split()) / summary.token_count if summary.token_count > 0 else 1.0
                            }
                        )
                        
                        polished_summaries.append(polished_result)
                        state.completed_chapter_ids.append(summary.chunk_id)
                        state.processed_chapters = len(state.completed_chapter_ids)
                        
                        # 保存检查点
                        self.checkpoint_manager.save_checkpoint(state, polished_summaries=polished_summaries)
                        
                        pbar.update(1)
                        
                    except Exception as e:
                        error_info = {
                            'chunk_id': summary.chunk_id,
                            'chapter_title': summary.section_title,
                            'error': str(e),
                            'timestamp': datetime.now().isoformat(),
                            'stage': 'polish'
                        }
                        state.failed_chapter_ids.append(summary.chunk_id)
                        state.error_log.append(error_info)
                        
                        print(f"\n❌ 打磨失败: {summary.section_title}")
                        print(f"   错误: {str(e)}")
                        
                        # 保存失败状态
                        self.checkpoint_manager.save_checkpoint(state, polished_summaries=polished_summaries)
                        
                        # 检查限流
                        if "rate limit" in str(e).lower() or "429" in str(e):
                            print(f"⏸️ 检测到限流错误，已保存检查点")
                            print(f"   可以稍后运行以下命令恢复: python -m src.main_v6 --resume {state.session_id}")
                            break
                        
                        pbar.update(1)
        
        return polished_summaries
    
    async def _finalize_summary(self, summaries: List[SummaryResult], state: CheckpointState, chapters: List[ChapterChunk]) -> None:
        """完成总结处理"""
        if not summaries:
            print("❌ 没有成功生成的总结")
            return
        
        # 计算统计信息
        overall_stats = SummaryPostProcessor.calculate_overall_stats(summaries)
        print(f"总体统计: {overall_stats}")
        
        # 格式化输出
        print(f"\n步骤: 格式化输出...")
        formatter = MarkdownFormatterV2(self.config.output)
        
        # 从第一个块提取标题
        original_title = self._extract_title(chapters)
        
        formatted_content = formatter.format_summaries(
            summaries=summaries,
            original_title=f"{original_title} (V6 检查点版{'+ 二次打磨' if state.enable_polish else ''})",
            compression_level=state.compression_level,
            stats=overall_stats
        )
        
        # 保存文件
        output_path = Path(state.output_path)
        formatter.save_to_file(formatted_content, output_path)
        
        # 更新状态为完成
        state.current_stage = "completed"
        self.checkpoint_manager.save_checkpoint(state, summaries=summaries)
        
        print(f"\n✅ 总结完成! 输出文件: {output_path}")
        print(f"📊 原始内容: {overall_stats.get('total_original_tokens', 0):,} tokens")
        print(f"📝 总结内容: {overall_stats.get('total_summary_tokens', 0):,} tokens") 
        print(f"🎯 压缩比: {overall_stats.get('overall_compression_ratio', 0):.2%}")
        print(f"💾 会话ID: {state.session_id}")
        
        if state.failed_chapter_ids:
            print(f"⚠️ 失败章节数: {len(state.failed_chapter_ids)}")
            print("   可以查看检查点文件了解详细错误信息")
    
    def _calculate_compression_ratio(self, original: str, summary: str) -> float:
        """计算压缩比例"""
        original_length = len(original)
        summary_length = len(summary)
        
        if original_length == 0:
            return 0.0
        
        return summary_length / original_length
    
    def _extract_title(self, chunks: List[ChapterChunk]) -> str:
        """从文档块中提取标题"""
        for chunk in chunks:
            if chunk.chapter_level == 1 and not chunk.chapter_title.startswith('Chapter'):
                return chunk.chapter_title
        return "学术论文"


async def main():
    """主函数"""
    # 简单的命令行参数解析
    if len(sys.argv) < 2:
        print("用法:")
        print("  新任务: python -m src.main_v6 <输入目录> <输出文件> [压缩级别] [最大章节token数] [是否打磨] [Claude项目] [Claude模型]")
        print("  恢复任务: python -m src.main_v6 --resume <会话ID>")
        print("  列出检查点: python -m src.main_v6 --list")
        print("  清理检查点: python -m src.main_v6 --clean [保留天数]")
        print("示例:")
        print("  python -m src.main_v6 ./GFM_SURVEY ./summary_v6.md 30 8000 true")
        print("  python -m src.main_v6 --resume abc123def456")
        print("  python -m src.main_v6 --list")
        sys.exit(1)
    
    # 加载配置
    try:
        config = load_config()
        print(f"✅ 配置加载完成: 使用Claude CLI")
    except Exception as e:
        print(f"❌ 错误: 配置加载失败: {e}")
        sys.exit(1)
    
    # 创建总结器
    checkpoint_dir = Path(".checkpoints")
    summarizer = MinerUSummarizerV6(config, checkpoint_dir)
    
    # 处理命令行参数
    if sys.argv[1] == "--list":
        # 列出检查点
        checkpoints = summarizer.checkpoint_manager.list_checkpoints()
        print_checkpoints_table(checkpoints)
        sys.exit(0)
    
    elif sys.argv[1] == "--clean":
        # 清理检查点
        keep_days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
        summarizer.checkpoint_manager.clean_old_checkpoints(keep_days)
        sys.exit(0)
    
    elif sys.argv[1] == "--resume":
        # 恢复会话
        if len(sys.argv) < 3:
            print("❌ 错误: 请提供会话ID")
            sys.exit(1)
        
        session_id = sys.argv[2]
        try:
            await summarizer.summarize(
                input_dir=Path("."),  # 占位符，会从检查点加载
                output_path=Path("."),  # 占位符，会从检查点加载
                resume_session=session_id
            )
        except Exception as e:
            print(f"❌ 错误: 恢复失败: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    
    else:
        # 新任务
        if len(sys.argv) < 3:
            print("❌ 错误: 新任务需要提供输入目录和输出文件")
            sys.exit(1)
        
        input_dir = Path(sys.argv[1])
        output_path = Path(sys.argv[2])
        compression_level = int(sys.argv[3]) if len(sys.argv) > 3 else 50
        max_tokens_per_chapter = int(sys.argv[4]) if len(sys.argv) > 4 else 8000
        enable_polish = sys.argv[5].lower() == 'true' if len(sys.argv) > 5 else True
        claude_project = sys.argv[6] if len(sys.argv) > 6 else None
        claude_model = sys.argv[7] if len(sys.argv) > 7 else None
        
        # 验证输入目录
        if not input_dir.exists():
            print(f"错误: 输入目录不存在: {input_dir}")
            sys.exit(1)
        
        full_md_path = input_dir / "full.md"
        if not full_md_path.exists():
            print(f"错误: 未找到full.md文件: {full_md_path}")
            sys.exit(1)
        
        # 测试Claude CLI
        from src.summarizer.claude_cli_client import ClaudeCLIConfig, ClaudeCLIManager
        claude_config = ClaudeCLIConfig(project_name=claude_project, model=claude_model)
        claude_manager = ClaudeCLIManager(claude_config)
        
        if not claude_manager.test_claude_cli():
            print("❌ 错误: Claude CLI不可用")
            print("解决方案:")
            print("1. 安装Claude CLI")
            print("2. 登录认证: claude auth login")
            print("3. 检查版本: claude --version")
            sys.exit(1)
        
        # 执行总结
        try:
            await summarizer.summarize(
                input_dir, 
                output_path, 
                compression_level, 
                max_tokens_per_chapter,
                enable_polish,
                claude_project,
                claude_model
            )
        except Exception as e:
            print(f"❌ 错误: 处理失败: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())