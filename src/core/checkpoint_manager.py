import json
import pickle
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import hashlib

from .document_parser import DocumentChunk


@dataclass
class SummaryResult:
    """总结结果"""

    chunk_id: str
    original_content: str
    summary: str
    section_title: str
    section_level: int
    token_count: int
    compression_ratio: float
    metadata: Dict[str, Any]


@dataclass
class CheckpointState:
    """检查点状态"""

    session_id: str
    input_dir: str
    output_path: str
    compression_level: int

    # 执行状态
    total_chapters: int
    processed_chapters: int
    current_stage: str  # 'initial_summary' | 'polish' | 'completed'

    # 时间戳
    created_at: str
    updated_at: str

    # 数据文件路径
    chapters_file: str
    summaries_file: str
    polished_summaries_file: Optional[str]

    # 完成状态
    completed_chapter_ids: List[str]
    failed_chapter_ids: List[str]
    error_log: List[Dict[str, str]]


class CheckpointManager:
    """检查点管理器"""

    def __init__(self, checkpoint_dir: Path = None):
        self.checkpoint_dir = checkpoint_dir or Path(".checkpoints")
        self.checkpoint_dir.mkdir(exist_ok=True)

    def create_session_id(self, input_dir: Path, compression_level: int) -> str:
        """创建会话ID"""
        # 基于输入目录和参数生成唯一ID
        content = f"{input_dir.absolute()}_{compression_level}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        return hashlib.md5(content.encode()).hexdigest()[:12]

    def save_checkpoint(
        self,
        state: CheckpointState,
        chapters: List[DocumentChunk] = None,
        summaries: List[SummaryResult] = None,
        polished_summaries: List[SummaryResult] = None,
    ) -> None:
        """保存检查点"""
        session_dir = self.checkpoint_dir / state.session_id
        session_dir.mkdir(exist_ok=True)

        # 更新时间戳
        state.updated_at = datetime.now().isoformat()

        # 保存状态文件
        state_file = session_dir / "state.json"
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(asdict(state), f, indent=2, ensure_ascii=False)

        # 保存数据文件
        if chapters is not None:
            chapters_file = session_dir / "chapters.pkl"
            with open(chapters_file, "wb") as f:
                pickle.dump(chapters, f)
            state.chapters_file = str(chapters_file)

        if summaries is not None:
            summaries_file = session_dir / "summaries.pkl"
            with open(summaries_file, "wb") as f:
                pickle.dump(summaries, f)
            state.summaries_file = str(summaries_file)

        if polished_summaries is not None:
            polished_file = session_dir / "polished_summaries.pkl"
            with open(polished_file, "wb") as f:
                pickle.dump(polished_summaries, f)
            state.polished_summaries_file = str(polished_file)

        # 再次保存状态（更新文件路径）
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(asdict(state), f, indent=2, ensure_ascii=False)

        print(f"💾 检查点已保存: {state.session_id}")
        print(f"   已处理: {state.processed_chapters}/{state.total_chapters} 章节")
        print(f"   当前阶段: {state.current_stage}")
        print(f"   失败数量: {len(state.failed_chapter_ids)}")

    def load_checkpoint(
        self, session_id: str
    ) -> tuple[
        CheckpointState,
        List[DocumentChunk],
        List[SummaryResult],
        Optional[List[SummaryResult]],
    ]:
        """加载检查点"""
        session_dir = self.checkpoint_dir / session_id
        if not session_dir.exists():
            raise FileNotFoundError(f"检查点不存在: {session_id}")

        # 加载状态
        state_file = session_dir / "state.json"
        with open(state_file, "r", encoding="utf-8") as f:
            state_dict = json.load(f)

        state = CheckpointState(**state_dict)

        # 加载数据
        chapters = []
        if state.chapters_file and Path(state.chapters_file).exists():
            with open(state.chapters_file, "rb") as f:
                chapters = pickle.load(f)

        summaries = []
        if state.summaries_file and Path(state.summaries_file).exists():
            with open(state.summaries_file, "rb") as f:
                summaries = pickle.load(f)

        polished_summaries = None
        if (
            state.polished_summaries_file
            and Path(state.polished_summaries_file).exists()
        ):
            with open(state.polished_summaries_file, "rb") as f:
                polished_summaries = pickle.load(f)

        print(f"📂 检查点已加载: {session_id}")
        print(f"   创建时间: {state.created_at}")
        print(f"   更新时间: {state.updated_at}")
        print(f"   当前阶段: {state.current_stage}")
        print(f"   进度: {state.processed_chapters}/{state.total_chapters}")

        return state, chapters, summaries, polished_summaries

    def list_checkpoints(self) -> List[Dict[str, Any]]:
        """列出所有检查点"""
        checkpoints = []

        for session_dir in self.checkpoint_dir.iterdir():
            if session_dir.is_dir():
                state_file = session_dir / "state.json"
                if state_file.exists():
                    try:
                        with open(state_file, "r", encoding="utf-8") as f:
                            state_dict = json.load(f)

                        checkpoints.append(
                            {
                                "session_id": state_dict["session_id"],
                                "input_dir": state_dict["input_dir"],
                                "compression_level": state_dict["compression_level"],
                                "current_stage": state_dict["current_stage"],
                                "progress": f"{state_dict['processed_chapters']}/{state_dict['total_chapters']}",
                                "created_at": state_dict["created_at"],
                                "updated_at": state_dict["updated_at"],
                                "failed_count": len(
                                    state_dict.get("failed_chapter_ids", [])
                                ),
                            }
                        )
                    except Exception as e:
                        print(f"⚠️ 无法读取检查点 {session_dir.name}: {e}")

        # 按更新时间排序
        checkpoints.sort(key=lambda x: x["updated_at"], reverse=True)
        return checkpoints

    def clean_old_checkpoints(self, keep_days: int = 7) -> None:
        """清理旧的检查点文件"""
        cutoff_time = datetime.now().timestamp() - (keep_days * 24 * 3600)
        cleaned_count = 0

        for session_dir in self.checkpoint_dir.iterdir():
            if session_dir.is_dir():
                state_file = session_dir / "state.json"
                if state_file.exists():
                    try:
                        with open(state_file, "r", encoding="utf-8") as f:
                            state_dict = json.load(f)

                        created_time = datetime.fromisoformat(
                            state_dict["created_at"]
                        ).timestamp()
                        if created_time < cutoff_time:
                            # 删除整个会话目录
                            import shutil

                            shutil.rmtree(session_dir)
                            cleaned_count += 1
                            print(f"🗑️ 已清理检查点: {session_dir.name}")
                    except Exception as e:
                        print(f"⚠️ 清理检查点失败 {session_dir.name}: {e}")

        if cleaned_count > 0:
            print(f"✅ 已清理 {cleaned_count} 个过期检查点")
        else:
            print("ℹ️ 没有过期的检查点需要清理")

    def delete_checkpoint(self, session_id: str) -> bool:
        """删除指定检查点"""
        session_dir = self.checkpoint_dir / session_id
        if session_dir.exists():
            try:
                import shutil

                shutil.rmtree(session_dir)
                print(f"🗑️ 已删除检查点: {session_id}")
                return True
            except Exception as e:
                print(f"❌ 删除检查点失败: {e}")
                return False
        else:
            print(f"⚠️ 检查点不存在: {session_id}")
            return False


def print_checkpoints_table(checkpoints: List[Dict[str, Any]]) -> None:
    """打印检查点表格"""
    if not checkpoints:
        print("📭 没有找到检查点")
        return

    print(f"\n📋 发现 {len(checkpoints)} 个检查点:")
    print("=" * 120)
    print(
        f"{'会话ID':<12} {'输入目录':<25} {'压缩':<4} {'阶段':<15} {'进度':<10} {'失败':<4} {'更新时间':<19}"
    )
    print("-" * 120)

    for cp in checkpoints:
        print(
            f"{cp['session_id']:<12} {cp['input_dir'][-24:]:<25} "
            f"{cp['compression_level']:<4}% {cp['current_stage']:<15} "
            f"{cp['progress']:<10} {cp['failed_count']:<4} {cp['updated_at'][:19]}"
        )

    print("=" * 120)
