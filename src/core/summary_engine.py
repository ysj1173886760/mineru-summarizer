import asyncio
from pathlib import Path
from typing import List, Optional, Dict, Any
from datetime import datetime
from tqdm import tqdm

from ..config.unified_config import UnifiedConfig
from .document_parser import DocumentParser, DocumentChunk
from .backend_manager import BackendManager, BackendProtocol
from .checkpoint_manager import (
    CheckpointManager,
    CheckpointState,
    SummaryResult,
    print_checkpoints_table,
)
from ..output.markdown_formatter_v2 import MarkdownFormatterV2


class SummaryEngine:
    """统一的总结引擎"""

    def __init__(self, config: UnifiedConfig):
        self.config = config
        self.checkpoint_manager = (
            CheckpointManager(Path(config.processing.checkpoint_dir))
            if config.processing.enable_checkpoint
            else None
        )

    async def summarize(
        self,
        input_dir: Path,
        output_path: Path,
        compression_level: int = 50,
        resume_session: Optional[str] = None,
        debug_pairs: bool = False,
    ) -> None:
        """执行总结任务"""

        if resume_session:
            await self._resume_summarize(resume_session, debug_pairs)
        else:
            await self._new_summarize(
                input_dir, output_path, compression_level, debug_pairs
            )

    async def _new_summarize(
        self,
        input_dir: Path,
        output_path: Path,
        compression_level: int,
        debug_pairs: bool = False,
    ) -> None:
        """新的总结任务"""

        print(f"🚀 开始处理MinerU数据 (统一版本): {input_dir}")
        print(f"📊 压缩级别: {compression_level}%")
        print(f"📄 输出路径: {output_path}")
        print(f"📚 最大章节token数: {self.config.processing.max_tokens_per_chapter:,}")
        print(f"🤖 后端: {self.config.backend.type}")
        print(f"✨ 二次打磨: {'启用' if self.config.polish.enabled else '禁用'}")
        print(f"💾 检查点: {'启用' if self.config.processing.enable_checkpoint else '禁用'}")
        if debug_pairs:
            print(f"🔍 Debug模式: 将保存所有(原文,总结)对到 {output_path.parent / 'debug_pairs'}")

        # 1. 解析Markdown文档
        print("\n步骤1: 按大章节解析Markdown文档...")
        full_md_path = input_dir / "full.md"
        if not full_md_path.exists():
            raise FileNotFoundError(f"未找到full.md文件: {full_md_path}")

        parser = DocumentParser(self.config.processing.max_tokens_per_chapter)
        chapter_chunks = parser.parse_markdown_file(full_md_path)

        print(f"解析完成: {len(chapter_chunks)} 个大章节")
        parser.print_statistics(chapter_chunks)

        # 2. 创建检查点状态（如果启用）
        state = None
        if self.checkpoint_manager:
            session_id = self.checkpoint_manager.create_session_id(
                input_dir, compression_level
            )
            state = CheckpointState(
                session_id=session_id,
                input_dir=str(input_dir.absolute()),
                output_path=str(output_path.absolute()),
                compression_level=compression_level,
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
                error_log=[],
            )

            # 保存初始检查点
            self.checkpoint_manager.save_checkpoint(state, chapters=chapter_chunks)
            print(f"💾 已创建会话: {session_id}")

        # 3. 生成初步总结
        print(f"\n步骤2: 生成初步总结...")
        summaries = await self._generate_summaries_with_checkpoint(
            chapter_chunks,
            compression_level,
            state,
            debug_pairs=debug_pairs,
            output_path=output_path,
        )
        print(f"初步总结生成完成: {len(summaries)} 个总结块")

        # 4. 二次打磨（可选）
        final_summaries = summaries
        if self.config.polish.enabled and summaries:
            print(f"\n步骤3: 二次打磨总结...")
            if state:
                state.current_stage = "polish"
                state.processed_chapters = 0
                state.completed_chapter_ids = []
                self.checkpoint_manager.save_checkpoint(state, summaries=summaries)

            polished_summaries = await self._polish_summaries_with_checkpoint(
                summaries,
                compression_level,
                state,
                debug_pairs=debug_pairs,
                output_path=output_path,
            )
            print(f"打磨完成: {len(polished_summaries)} 个精化总结")
            final_summaries = polished_summaries

        # 5. 完成处理
        await self._finalize_summary(
            final_summaries, state, chapter_chunks, output_path, compression_level
        )

        # 生成debug索引文件（如果启用）
        if debug_pairs:
            await self._create_debug_index(output_path, final_summaries)

    async def _resume_summarize(
        self, session_id: str, debug_pairs: bool = False
    ) -> None:
        """恢复总结任务"""
        if not self.checkpoint_manager:
            raise ValueError("检查点功能未启用，无法恢复会话")

        print(f"🔄 恢复会话: {session_id}")

        # 加载检查点
        try:
            (
                state,
                chapters,
                summaries,
                polished_summaries,
            ) = self.checkpoint_manager.load_checkpoint(session_id)
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
                chapters,
                state.compression_level,
                state,
                existing_summaries=summaries,
                debug_pairs=debug_pairs,
                output_path=Path(state.output_path),
            )

            # 检查是否需要打磨
            if self.config.polish.enabled and summaries:
                print(f"\n开始二次打磨...")
                state.current_stage = "polish"
                state.processed_chapters = 0
                state.completed_chapter_ids = []
                self.checkpoint_manager.save_checkpoint(state, summaries=summaries)

                polished_summaries = await self._polish_summaries_with_checkpoint(
                    summaries,
                    state.compression_level,
                    state,
                    debug_pairs=debug_pairs,
                    output_path=Path(state.output_path),
                )
                final_summaries = polished_summaries
            else:
                final_summaries = summaries

        elif state.current_stage == "polish":
            # 继续二次打磨
            print("\n继续二次打磨...")
            polished_summaries = await self._polish_summaries_with_checkpoint(
                summaries,
                state.compression_level,
                state,
                existing_polished=polished_summaries,
                debug_pairs=debug_pairs,
                output_path=Path(state.output_path),
            )
            final_summaries = polished_summaries

        elif state.current_stage == "completed":
            print("✅ 会话已完成，生成最终输出...")
            final_summaries = polished_summaries if polished_summaries else summaries
        else:
            print(f"❌ 未知状态: {state.current_stage}")
            return

        # 完成处理
        await self._finalize_summary(
            final_summaries,
            state,
            chapters,
            Path(state.output_path),
            state.compression_level,
        )

    async def _generate_summaries_with_checkpoint(
        self,
        chapter_chunks: List[DocumentChunk],
        compression_level: int,
        state: Optional[CheckpointState] = None,
        existing_summaries: List[SummaryResult] = None,
        debug_pairs: bool = False,
        output_path: Optional[Path] = None,
    ) -> List[SummaryResult]:
        """带检查点的总结生成"""

        if compression_level not in self.config.compression_levels:
            raise ValueError(f"不支持的压缩级别: {compression_level}")

        compression_config = self.config.compression_levels[compression_level]

        # 初始化结果列表
        summaries = existing_summaries or []
        completed_ids = set(state.completed_chapter_ids if state else [])
        failed_ids = set(state.failed_chapter_ids if state else [])

        # 过滤需要处理的章节
        pending_chunks = [
            chunk
            for chunk in chapter_chunks
            if chunk.id not in completed_ids and chunk.id not in failed_ids
        ]

        if not pending_chunks:
            print("✅ 所有章节已处理完成")
            return summaries

        print(
            f"📝 需要处理 {len(pending_chunks)} 个章节 (跳过 {len(completed_ids)} 个已完成, {len(failed_ids)} 个失败)"
        )

        # 创建后端
        backend = BackendManager.create_backend(self.config)

        # 创建debug目录（如果启用）
        debug_dir = None
        if debug_pairs and output_path:
            debug_dir = output_path.parent / "debug_pairs" / "initial_summaries"
            debug_dir.mkdir(parents=True, exist_ok=True)
            print(f"🔍 Debug: 初步总结pairs将保存到 {debug_dir}")

        # 处理章节 - 按原始顺序处理
        async with backend:
            with tqdm(
                total=len(pending_chunks), desc="生成总结", initial=len(completed_ids)
            ) as pbar:
                # 按chunk.id排序确保处理顺序正确
                pending_chunks_sorted = sorted(pending_chunks, key=lambda x: x.id)
                # 逐个处理以便实时保存检查点
                for chunk in pending_chunks_sorted:
                    try:
                        # 构建提示词
                        full_prompt = self._build_summary_prompt(
                            chunk, compression_config, compression_level
                        )

                        # 调用后端
                        summary_text = await backend.single_generate(full_prompt)

                        # 创建结果对象
                        result = SummaryResult(
                            chunk_id=chunk.id,
                            original_content=chunk.content,
                            summary=summary_text,
                            section_title=chunk.chapter_title,
                            section_level=chunk.chapter_level,
                            token_count=len(summary_text.split()),
                            compression_ratio=self._calculate_compression_ratio(
                                chunk.content, summary_text
                            ),
                            metadata={
                                "compression_level": compression_level,
                                "original_token_count": chunk.token_count,
                                "sub_sections": chunk.sub_sections,
                                "backend_type": self.config.backend.type,
                                "polished": False,
                            },
                        )

                        summaries.append(result)

                        # 保存debug pair（如果启用）
                        if debug_dir:
                            await self._save_debug_pair(
                                debug_dir,
                                chunk.id,
                                chunk.chapter_title,
                                chunk.content,
                                summary_text,
                                "initial_summary",
                                compression_level,
                            )

                        if state:
                            state.completed_chapter_ids.append(chunk.id)
                            state.processed_chapters = len(state.completed_chapter_ids)

                            # 每处理一个章节就保存检查点
                            self.checkpoint_manager.save_checkpoint(
                                state, summaries=summaries
                            )

                        pbar.update(1)

                    except Exception as e:
                        if state:
                            error_info = {
                                "chunk_id": chunk.id,
                                "chapter_title": chunk.chapter_title,
                                "error": str(e),
                                "timestamp": datetime.now().isoformat(),
                            }
                            state.failed_chapter_ids.append(chunk.id)
                            state.error_log.append(error_info)

                            print(f"\n❌ 章节处理失败: {chunk.chapter_title}")
                            print(f"   错误: {str(e)}")

                            # 保存失败状态
                            self.checkpoint_manager.save_checkpoint(
                                state, summaries=summaries
                            )

                            # 如果是限流错误，提示用户
                            if (
                                "RATE_LIMIT_ERROR" in str(e)
                                or "rate limit" in str(e).lower()
                            ):
                                print(f"⏸️ 检测到限流错误，已保存检查点")
                                print(
                                    f"   可以稍后运行以下命令恢复: mineru-summarizer --resume {state.session_id}"
                                )
                                break
                        else:
                            print(f"\n❌ 章节处理失败: {chunk.chapter_title}")
                            print(f"   错误: {str(e)}")

                        pbar.update(1)

        return summaries

    async def _polish_summaries_with_checkpoint(
        self,
        summaries: List[SummaryResult],
        compression_level: int,
        state: Optional[CheckpointState] = None,
        existing_polished: List[SummaryResult] = None,
        debug_pairs: bool = False,
        output_path: Optional[Path] = None,
    ) -> List[SummaryResult]:
        """带检查点的二次打磨"""

        # 初始化结果列表
        polished_summaries = existing_polished or []
        completed_ids = set(state.completed_chapter_ids if state else [])
        failed_ids = set(state.failed_chapter_ids if state else [])

        # 过滤需要处理的总结
        pending_summaries = [
            s
            for s in summaries
            if s.chunk_id not in completed_ids and s.chunk_id not in failed_ids
        ]

        if not pending_summaries:
            print("✅ 所有总结已打磨完成")
            return polished_summaries

        print(f"🎨 需要打磨 {len(pending_summaries)} 个总结")

        # 创建后端（打磨时降低并发数）
        polish_config = self.config
        polish_config.processing.max_concurrent = max(
            1,
            int(
                self.config.processing.max_concurrent
                * self.config.polish.concurrent_ratio
            ),
        )
        backend = BackendManager.create_backend(polish_config)

        # 创建debug目录（如果启用）
        debug_dir = None
        if debug_pairs and output_path:
            debug_dir = output_path.parent / "debug_pairs" / "polished_summaries"
            debug_dir.mkdir(parents=True, exist_ok=True)
            print(f"🔍 Debug: 打磨后总结pairs将保存到 {debug_dir}")

        # 处理打磨
        async with backend:
            with tqdm(
                total=len(pending_summaries), desc="打磨总结", initial=len(completed_ids)
            ) as pbar:
                for summary in pending_summaries:
                    try:
                        # 构建打磨提示词
                        polish_prompt = self._build_polish_prompt(
                            summary, compression_level
                        )

                        # 调用打磨
                        polished_text = await backend.single_generate(polish_prompt)

                        # 创建打磨后的结果
                        polished_result = SummaryResult(
                            chunk_id=summary.chunk_id,
                            original_content=summary.original_content,
                            summary=polished_text,
                            section_title=summary.section_title,
                            section_level=summary.section_level,
                            token_count=len(polished_text.split()),
                            compression_ratio=self._calculate_compression_ratio(
                                summary.original_content, polished_text
                            ),
                            metadata={
                                **summary.metadata,
                                "polished": True,
                                "original_summary_tokens": summary.token_count,
                                "polish_improvement_ratio": len(polished_text.split())
                                / summary.token_count
                                if summary.token_count > 0
                                else 1.0,
                            },
                        )

                        polished_summaries.append(polished_result)

                        # 保存debug pair（如果启用）
                        if debug_dir:
                            await self._save_debug_pair(
                                debug_dir,
                                summary.chunk_id,
                                summary.section_title,
                                summary.summary,
                                polished_text,
                                "polish",
                                compression_level,
                            )

                        if state:
                            state.completed_chapter_ids.append(summary.chunk_id)
                            state.processed_chapters = len(state.completed_chapter_ids)

                            # 保存检查点
                            self.checkpoint_manager.save_checkpoint(
                                state, polished_summaries=polished_summaries
                            )

                        pbar.update(1)

                    except Exception as e:
                        if state:
                            error_info = {
                                "chunk_id": summary.chunk_id,
                                "chapter_title": summary.section_title,
                                "error": str(e),
                                "timestamp": datetime.now().isoformat(),
                                "stage": "polish",
                            }
                            state.failed_chapter_ids.append(summary.chunk_id)
                            state.error_log.append(error_info)

                            print(f"\n❌ 打磨失败: {summary.section_title}")
                            print(f"   错误: {str(e)}")

                            # 保存失败状态
                            self.checkpoint_manager.save_checkpoint(
                                state, polished_summaries=polished_summaries
                            )

                            # 检查限流
                            if (
                                "RATE_LIMIT_ERROR" in str(e)
                                or "rate limit" in str(e).lower()
                            ):
                                print(f"⏸️ 检测到限流错误，已保存检查点")
                                print(
                                    f"   可以稍后运行以下命令恢复: mineru-summarizer --resume {state.session_id}"
                                )
                                break
                        else:
                            print(f"\n❌ 打磨失败: {summary.section_title}")
                            print(f"   错误: {str(e)}")

                        pbar.update(1)

        return polished_summaries

    def _build_summary_prompt(
        self,
        chunk: DocumentChunk,
        compression_config: Dict[str, str],
        compression_level: int,
    ) -> str:
        """构建总结提示词"""
        context_info = f"\n\n章节标题: {chunk.chapter_title}"
        if chunk.sub_sections:
            context_info += f"\n子章节: {', '.join(chunk.sub_sections[:5])}"
            if len(chunk.sub_sections) > 5:
                context_info += f" (还有{len(chunk.sub_sections)-5}个子章节)"
        context_info += f"\n章节规模: {chunk.token_count:,} tokens"

        full_prompt = f"""{compression_config['prompt_template']}

{context_info}

重要要求:
1. 这是一个完整的大章节，请保持内容的连贯性和逻辑完整性
2. 重点突出章节的核心贡献和主要观点
3. 保持学术写作的严谨性和专业性
4. 对于包含多个子章节的内容，请按逻辑顺序组织总结
5. 如果原文中有图片链接（格式如![](images/xxx.jpg)），请中保留这些图片链接，如果文中有对图片的相关描述可以简要提及。不要输出任何原文中没有的图片链接
7. 专有技术名词保持英文原文，不要翻译，包括但不限于：
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

        return full_prompt

    def _build_polish_prompt(
        self, summary: SummaryResult, compression_level: int
    ) -> str:
        """构建打磨提示词"""
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
7. 如果原文中有图片链接（格式如![](images/xxx.jpg)），请中保留这些图片链接，如果文中有对图片的相关描述可以简要提及。不要输出任何原文中没有的图片链接

需要保持英文的技术术语（请勿翻译）:
Graph Neural Networks (GNNs), Graph Foundation Models (GFMs), Transformer, Graph Attention Networks (GAT), GraphSAGE, Message Passing, Node Embedding, Graph Convolutional Networks (GCN), Self-supervised Learning, Pre-training, Fine-tuning, In-context Learning, Few-shot Learning, Zero-shot Learning, Knowledge Graph, Heterogeneous Graph, Homogeneous Graph, Graph Isomorphism, Graph Pooling, Graph Classification, Node Classification, Link Prediction, Graph Generation, Graph Anomaly Detection, Contrastive Learning, Multi-modal Learning, Cross-domain Transfer, Domain Adaptation

原始总结:
{summary.summary}

请输出打磨后的总结，直接给出最终结果，不要包含说明性文字："""

        return polish_prompt

    def _calculate_compression_ratio(self, original: str, summary: str) -> float:
        """计算压缩比例"""
        original_length = len(original)
        summary_length = len(summary)

        if original_length == 0:
            return 0.0

        return summary_length / original_length

    def _extract_title(self, chunks: List[DocumentChunk]) -> str:
        """从文档块中提取标题"""
        for chunk in chunks:
            if chunk.chapter_level == 1 and not chunk.chapter_title.startswith(
                "Chapter"
            ):
                return chunk.chapter_title
        return "学术论文"

    async def _finalize_summary(
        self,
        summaries: List[SummaryResult],
        state: Optional[CheckpointState],
        chapters: List[DocumentChunk],
        output_path: Path,
        compression_level: int,
    ) -> None:
        """完成总结处理"""
        if not summaries:
            print("❌ 没有成功生成的总结")
            return

        # 计算统计信息
        overall_stats = self._calculate_overall_stats(summaries)
        print(f"总体统计: {overall_stats}")

        # 格式化输出
        print(f"\n步骤: 格式化输出...")
        formatter = MarkdownFormatterV2(self.config.output)

        # 从第一个块提取标题
        original_title = self._extract_title(chapters)

        formatted_content = formatter.format_summaries(
            summaries=summaries,
            original_title=f"{original_title} ({'打磨版' if self.config.polish.enabled else '标准版'})",
            compression_level=compression_level,
            stats=overall_stats,
        )

        # 保存文件
        formatter.save_to_file(formatted_content, output_path)

        # 更新状态为完成
        if state:
            state.current_stage = "completed"
            self.checkpoint_manager.save_checkpoint(state, summaries=summaries)

        print(f"\n✅ 总结完成! 输出文件: {output_path}")
        print(f"📊 原始内容: {overall_stats.get('total_original_tokens', 0):,} tokens")
        print(f"📝 总结内容: {overall_stats.get('total_summary_tokens', 0):,} tokens")
        print(f"🎯 压缩比: {overall_stats.get('overall_compression_ratio', 0):.2%}")
        if state:
            print(f"💾 会话ID: {state.session_id}")

        if state and state.failed_chapter_ids:
            print(f"⚠️ 失败章节数: {len(state.failed_chapter_ids)}")
            print("   可以查看检查点文件了解详细错误信息")

    def _calculate_overall_stats(
        self, summaries: List[SummaryResult]
    ) -> Dict[str, Any]:
        """计算整体统计信息"""
        if not summaries:
            return {}

        total_original_tokens = sum(
            s.metadata.get("original_token_count", 0) for s in summaries
        )
        total_summary_tokens = sum(s.token_count for s in summaries)

        overall_compression_ratio = (
            total_summary_tokens / total_original_tokens
            if total_original_tokens > 0
            else 0
        )

        return {
            "total_chunks": len(summaries),
            "total_original_tokens": total_original_tokens,
            "total_summary_tokens": total_summary_tokens,
            "overall_compression_ratio": overall_compression_ratio,
            "average_compression_ratio": sum(s.compression_ratio for s in summaries)
            / len(summaries),
            "sections_processed": len(summaries),
        }

    def list_checkpoints(self) -> None:
        """列出检查点"""
        if not self.checkpoint_manager:
            print("❌ 检查点功能未启用")
            return

        checkpoints = self.checkpoint_manager.list_checkpoints()
        print_checkpoints_table(checkpoints)

    def clean_checkpoints(self, keep_days: int = 7) -> None:
        """清理检查点"""
        if not self.checkpoint_manager:
            print("❌ 检查点功能未启用")
            return

        self.checkpoint_manager.clean_old_checkpoints(keep_days)

    async def _save_debug_pair(
        self,
        debug_dir: Path,
        chunk_id: str,
        title: str,
        original_text: str,
        summary_text: str,
        stage: str,
        compression_level: int,
    ) -> None:
        """保存debug pair到文件"""
        try:
            # 创建安全的文件名
            safe_title = "".join(
                c for c in title if c.isalnum() or c in (" ", "-", "_")
            ).strip()
            safe_title = safe_title.replace(" ", "_")[:50]  # 限制长度

            filename = f"{chunk_id}_{safe_title}.md"
            file_path = debug_dir / filename

            # 创建markdown格式的内容
            content = f"""# Debug Pair: {title}

**Chunk ID:** {chunk_id}  
**Stage:** {stage}  
**Compression Level:** {compression_level}%  
**Timestamp:** {datetime.now().isoformat()}

## 原始内容

```markdown
{original_text}
```

## 总结内容

```markdown
{summary_text}
```

## 统计信息

- 原始字符数: {len(original_text):,}
- 总结字符数: {len(summary_text):,}
- 压缩比: {len(summary_text) / len(original_text) * 100:.1f}%
- 原始token数(估算): {len(original_text.split()):,}
- 总结token数(估算): {len(summary_text.split()):,}

---
*Generated by MinerU Summarizer Debug Mode*
"""

            # 写入文件
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

        except Exception as e:
            print(f"⚠️ 保存debug pair失败: {e}")
            # 不抛出异常，避免影响主流程

    async def _create_debug_index(
        self, output_path: Path, summaries: List[SummaryResult]
    ) -> None:
        """创建debug索引文件"""
        try:
            debug_base_dir = output_path.parent / "debug_pairs"
            index_path = debug_base_dir / "INDEX.md"

            # 生成索引内容
            content = f"""# Debug Pairs 索引

**生成时间:** {datetime.now().isoformat()}  
**输出文件:** {output_path.name}  
**总结数量:** {len(summaries)}

## 文件结构

```
debug_pairs/
├── INDEX.md                    # 本索引文件
├── initial_summaries/          # 初步总结的(原文,总结)对
│   ├── chapter_001_*.md
│   └── ...
└── polished_summaries/         # 打磨后的(初步总结,打磨总结)对
    ├── chapter_001_*.md
    └── ...
```

## 分片总结列表

| 序号 | Chunk ID | 标题 | 状态 | 初步总结文件 | 打磨总结文件 |
|------|----------|------|------|-------------|-------------|
"""

            # 添加每个分片的信息
            initial_dir = debug_base_dir / "initial_summaries"
            polished_dir = debug_base_dir / "polished_summaries"

            for i, summary in enumerate(summaries, 1):
                # 创建安全的标题
                safe_title = "".join(
                    c
                    for c in summary.section_title
                    if c.isalnum() or c in (" ", "-", "_")
                ).strip()
                safe_title = safe_title.replace(" ", "_")[:50]

                initial_file = f"{summary.chunk_id}_{safe_title}.md"
                polished_file = (
                    f"{summary.chunk_id}_{safe_title}.md"
                    if summary.metadata.get("polished", False)
                    else "N/A"
                )

                status = "已打磨" if summary.metadata.get("polished", False) else "仅初步总结"

                initial_link = (
                    f"[{initial_file}](initial_summaries/{initial_file})"
                    if (initial_dir / initial_file).exists()
                    else "N/A"
                )
                polished_link = (
                    f"[{polished_file}](polished_summaries/{polished_file})"
                    if polished_file != "N/A"
                    and (polished_dir / polished_file).exists()
                    else "N/A"
                )

                content += f"| {i} | {summary.chunk_id} | {summary.section_title} | {status} | {initial_link} | {polished_link} |\n"

            content += f"""

## 使用说明

1. **初步总结文件夹** (`initial_summaries/`): 包含原始章节内容和对应的初步总结
2. **打磨总结文件夹** (`polished_summaries/`): 包含初步总结和经过打磨后的最终总结
3. 每个文件都包含详细的统计信息，包括字符数、token数、压缩比等
4. 文件命名格式: `{{chunk_id}}_{{safe_title}}.md`

## 统计汇总

- 总分片数: {len(summaries)}
- 已打磨分片数: {sum(1 for s in summaries if s.metadata.get('polished', False))}
- 平均压缩比: {sum(s.compression_ratio for s in summaries) / len(summaries) * 100:.1f}%

---
*Generated by MinerU Summarizer Debug Mode*
"""

            # 写入索引文件
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"🔍 Debug索引文件已生成: {index_path}")

        except Exception as e:
            print(f"⚠️ 生成debug索引失败: {e}")
            # 不抛出异常，避免影响主流程
