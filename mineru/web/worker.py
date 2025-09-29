from __future__ import annotations

import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Optional

from parse_and_summarize import PDFSummarizer

from .config import WebConfig
from .database import TaskRecord, TaskStore

logger = logging.getLogger(__name__)


class TaskWorker:
    """后台轮询执行 PDF 总结任务。"""

    def __init__(
        self,
        config: WebConfig,
        store: TaskStore,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        self.config = config
        self.store = store
        self.loop = loop or asyncio.get_event_loop()
        self._executor = ThreadPoolExecutor(max_workers=config.worker_concurrency)
        self._stop_event = asyncio.Event()
        self._task: Optional[asyncio.Task[None]] = None
        self._summarizer = PDFSummarizer(config.mineru_server)

    def start(self) -> None:
        if self._task is None:
            self._task = self.loop.create_task(self._run())

    async def stop(self) -> None:
        self._stop_event.set()
        if self._task:
            await self._task
        self._executor.shutdown(wait=True)

    async def _run(self) -> None:
        logger.info("Task worker started")
        try:
            while not self._stop_event.is_set():
                record = self.store.acquire_pending_task()
                if not record:
                    await asyncio.sleep(self.config.worker_interval_seconds)
                    continue

                logger.info("Processing task %s", record.id)
                await self._execute(record)
        except asyncio.CancelledError:
            logger.info("Task worker cancelled")
        finally:
            logger.info("Task worker stopped")

    async def _execute(self, record: TaskRecord) -> None:
        output_path = self.config.results_dir / f"{record.id}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        log_path = self.config.logs_dir / f"{record.id}.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        config_path = self._prepare_config(record)

        def _run_job() -> bool:
            with open(log_path, "w", encoding="utf-8") as log_file, redirect_stdout(log_file), redirect_stderr(log_file):
                return self._summarizer.process_pdf(
                    pdf_path=str(record.pdf_path),
                    output_path=str(output_path),
                    compression=record.compression,
                    enable_polish=record.polish,
                    temp_dir=None,
                    keep_temp=self.config.keep_temp_files,
                    config_path=str(config_path),
                    backend=None,
                    mineru_lang=record.mineru_lang,
                    mineru_backend=record.mineru_backend,
                    mineru_method=record.mineru_method,
                    formula_enable=self.config.formula_enable,
                    table_enable=self.config.table_enable,
                    vlm_server_url=None,
                )

        try:
            success = await self.loop.run_in_executor(self._executor, _run_job)
        except Exception as exc:  # pragma: no cover - 防御性捕获
            logger.exception("Task %s failed", record.id)
            self.store.mark_failure(record.id, str(exc))
            return

        if success:
            self.store.mark_success(record.id, output_path)
            logger.info("Task %s succeeded", record.id)
        else:
            message = "PDF summarization failed"
            self.store.mark_failure(record.id, message)
            logger.warning("Task %s failed: %s", record.id, message)

    def _prepare_config(self, record: TaskRecord) -> Path:
        """为任务构建配置文件，允许在基础配置上覆盖部分字段。"""

        # 当前仅暴露压缩比例，配置文件直接引用基础配置即可。
        # 若后续开放更多配置项，可在此处合并 YAML 并写入临时文件。
        return self.config.base_config_path
