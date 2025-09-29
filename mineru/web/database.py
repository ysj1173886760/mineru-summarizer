from __future__ import annotations

import sqlite3
import threading
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional, Sequence


class TaskStatus:
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"

    TERMINAL = {SUCCEEDED, FAILED}


@dataclass
class TaskRecord:
    id: str
    filename: str
    pdf_path: Path
    summary_path: Optional[Path]
    compression: int
    polish: bool
    mineru_lang: str
    mineru_backend: str
    mineru_method: str
    status: str
    created_at: datetime
    started_at: Optional[datetime]
    finished_at: Optional[datetime]
    error_message: Optional[str]


class TaskStore:
    """基于 SQLite 的任务存储。"""

    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path
        self._lock = threading.Lock()
        database_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.database_path, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    filename TEXT NOT NULL,
                    pdf_path TEXT NOT NULL,
                    summary_path TEXT,
                    compression INTEGER NOT NULL,
                    polish INTEGER NOT NULL,
                    mineru_lang TEXT NOT NULL,
                    mineru_backend TEXT NOT NULL,
                    mineru_method TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    started_at TEXT,
                    finished_at TEXT,
                    error_message TEXT
                )
                """
            )
            conn.execute("CREATE INDEX IF NOT EXISTS idx_tasks_status_created ON tasks(status, created_at)")

    def create_task(
        self,
        *,
        task_id: str,
        filename: str,
        pdf_path: Path,
        compression: int,
        polish: bool,
        mineru_lang: str,
        mineru_backend: str,
        mineru_method: str,
    ) -> TaskRecord:
        now = datetime.utcnow()
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO tasks (id, filename, pdf_path, summary_path, compression, polish,
                                   mineru_lang, mineru_backend, mineru_method, status,
                                   created_at)
                VALUES (?, ?, ?, NULL, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    task_id,
                    filename,
                    str(pdf_path),
                    compression,
                    1 if polish else 0,
                    mineru_lang,
                    mineru_backend,
                    mineru_method,
                    TaskStatus.PENDING,
                    now.isoformat(),
                ),
            )
        return TaskRecord(
            id=task_id,
            filename=filename,
            pdf_path=pdf_path,
            summary_path=None,
            compression=compression,
            polish=polish,
            mineru_lang=mineru_lang,
            mineru_backend=mineru_backend,
            mineru_method=mineru_method,
            status=TaskStatus.PENDING,
            created_at=now,
            started_at=None,
            finished_at=None,
            error_message=None,
        )

    def list_tasks(self, limit: int = 20) -> Sequence[TaskRecord]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT * FROM tasks
                ORDER BY datetime(created_at) DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
        return [self._row_to_record(row) for row in rows]

    def get_task(self, task_id: str) -> Optional[TaskRecord]:
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        return self._row_to_record(row) if row else None

    def acquire_pending_task(self) -> Optional[TaskRecord]:
        """拉取并标记最早的待处理任务。"""

        with self._lock:
            with self._connect() as conn:
                conn.execute("BEGIN IMMEDIATE")
                row = conn.execute(
                    """
                    SELECT * FROM tasks
                    WHERE status = ?
                    ORDER BY datetime(created_at)
                    LIMIT 1
                    """,
                    (TaskStatus.PENDING,),
                ).fetchone()
                if not row:
                    conn.rollback()
                    return None
                now_iso = datetime.utcnow().isoformat()
                updated = conn.execute(
                    """
                    UPDATE tasks
                    SET status = ?, started_at = ?, error_message = NULL
                    WHERE id = ? AND status = ?
                    """,
                    (TaskStatus.RUNNING, now_iso, row["id"], TaskStatus.PENDING),
                )
                if updated.rowcount == 0:
                    conn.rollback()
                    return None
                conn.commit()
                task_id = row["id"]
        return self.get_task(task_id)

    def mark_success(self, task_id: str, summary_path: Path) -> None:
        now = datetime.utcnow().isoformat()
        with self._connect() as conn:
            conn.execute(
                """
                UPDATE tasks
                SET status = ?, summary_path = ?, finished_at = ?
                WHERE id = ?
                """,
                (TaskStatus.SUCCEEDED, str(summary_path), now, task_id),
            )

    def mark_failure(self, task_id: str, error_message: str) -> None:
        now = datetime.utcnow().isoformat()
        with self._connect() as conn:
            conn.execute(
                """
                UPDATE tasks
                SET status = ?, finished_at = ?, error_message = ?
                WHERE id = ?
                """,
                (TaskStatus.FAILED, now, error_message, task_id),
            )

    def retry_failed_task(self, task_id: str) -> Optional[TaskRecord]:
        with self._lock:
            with self._connect() as conn:
                conn.execute("BEGIN IMMEDIATE")
                row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
                if not row:
                    conn.rollback()
                    return None
                if row["status"] != TaskStatus.FAILED:
                    conn.rollback()
                    return self._row_to_record(row)
                conn.execute(
                    """
                    UPDATE tasks
                    SET status = ?, started_at = NULL, finished_at = NULL,
                        summary_path = NULL, error_message = NULL
                    WHERE id = ?
                    """,
                    (TaskStatus.PENDING, task_id),
                )
                conn.commit()
        return self.get_task(task_id)

    def _row_to_record(self, row: sqlite3.Row) -> TaskRecord:
        return TaskRecord(
            id=row["id"],
            filename=row["filename"],
            pdf_path=Path(row["pdf_path"]),
            summary_path=Path(row["summary_path"]) if row["summary_path"] else None,
            compression=int(row["compression"]),
            polish=bool(row["polish"]),
            mineru_lang=row["mineru_lang"],
            mineru_backend=row["mineru_backend"],
            mineru_method=row["mineru_method"],
            status=row["status"],
            created_at=datetime.fromisoformat(row["created_at"]),
            started_at=datetime.fromisoformat(row["started_at"]) if row["started_at"] else None,
            finished_at=datetime.fromisoformat(row["finished_at"]) if row["finished_at"] else None,
            error_message=row["error_message"],
        )
