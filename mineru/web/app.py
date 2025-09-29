from __future__ import annotations

import asyncio
import logging
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional
from uuid import uuid4

from fastapi import Depends, FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from .config import WebConfig, load_web_config
from .database import TaskRecord, TaskStatus, TaskStore
from .worker import TaskWorker

logger = logging.getLogger(__name__)

app = FastAPI(title="MinerU Summarizer Web")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.state.app_state = None


class TaskResponse(BaseModel):
    id: str
    filename: str
    compression: int
    status: str
    created_at: datetime
    started_at: Optional[datetime]
    finished_at: Optional[datetime]
    error_message: Optional[str]
    download_url: Optional[str]


class ConfigResponse(BaseModel):
    max_file_mb: int
    default_compression: int
    compression_options: list[int]
    poll_interval_seconds: float


@dataclass
class AppState:
    config: WebConfig
    store: TaskStore
    worker: TaskWorker


def get_state() -> AppState:
    state: Optional[AppState] = getattr(app.state, "app_state", None)
    if state is None:
        raise RuntimeError("App state not initialised")
    return state


@app.on_event("startup")
async def on_startup() -> None:
    logging.basicConfig(level=logging.INFO)
    config = load_web_config()
    config.uploads_dir.mkdir(parents=True, exist_ok=True)
    config.results_dir.mkdir(parents=True, exist_ok=True)
    config.logs_dir.mkdir(parents=True, exist_ok=True)

    store = TaskStore(config.database_path)

    if not config.base_config_path.exists():
        raise FileNotFoundError(f"Base config path {config.base_config_path} not found")

    loop = asyncio.get_running_loop()
    worker = TaskWorker(config=config, store=store, loop=loop)
    worker.start()

    app.state.app_state = AppState(config=config, store=store, worker=worker)
    logger.info("Web app started")


@app.on_event("shutdown")
async def on_shutdown() -> None:
    state: Optional[AppState] = getattr(app.state, "app_state", None)
    if state:
        await state.worker.stop()
    logger.info("Web app stopped")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, state: AppState = Depends(get_state)) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "default_compression": state.config.default_compression,
            "compression_options": [30, 50, 70, 100],
            "max_file_mb": state.config.max_file_mb,
            "poll_interval": state.config.poll_interval_seconds,
        },
    )


@app.get("/api/config", response_model=ConfigResponse)
async def read_config(state: AppState = Depends(get_state)) -> ConfigResponse:
    return ConfigResponse(
        max_file_mb=state.config.max_file_mb,
        default_compression=state.config.default_compression,
        compression_options=[30, 50, 70, 100],
        poll_interval_seconds=state.config.poll_interval_seconds,
    )


@app.post("/api/tasks", response_model=TaskResponse)
async def create_task(
    request: Request,
    file: UploadFile = File(...),
    compression: Optional[int] = Form(None),
    state: AppState = Depends(get_state),
) -> TaskResponse:
    config = state.config

    if file.content_type not in {"application/pdf", "application/octet-stream"}:
        raise HTTPException(status_code=400, detail="仅支持 PDF 文件")

    if compression is not None:
        try:
            compression_value = int(compression)
        except (TypeError, ValueError) as exc:
            raise HTTPException(status_code=400, detail="压缩比例格式错误") from exc
    else:
        compression_value = config.default_compression
    if compression_value not in {30, 50, 70, 100}:
        raise HTTPException(status_code=400, detail="不支持的压缩比例")

    task_id = uuid4().hex
    filename = os.path.basename(file.filename) if file.filename else f"upload_{task_id}.pdf"
    pdf_path = config.uploads_dir / f"{task_id}.pdf"

    size_acc = 0
    with pdf_path.open("wb") as destination:
        while True:
            chunk = await file.read(1024 * 1024)
            if not chunk:
                break
            size_acc += len(chunk)
            if size_acc > config.max_file_bytes:
                pdf_path.unlink(missing_ok=True)
                raise HTTPException(status_code=400, detail="文件超出大小限制")
            destination.write(chunk)
    await file.close()

    record = state.store.create_task(
        task_id=task_id,
        filename=filename,
        pdf_path=pdf_path,
        compression=compression_value,
        polish=False,
        mineru_lang=config.mineru_lang,
        mineru_backend=config.mineru_backend,
        mineru_method=config.mineru_method,
    )

    return _to_response(record)


@app.get("/api/tasks", response_model=list[TaskResponse])
async def list_tasks(state: AppState = Depends(get_state)) -> list[TaskResponse]:
    records = state.store.list_tasks(limit=30)
    return [_to_response(r) for r in records]


@app.get("/api/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: str, state: AppState = Depends(get_state)) -> TaskResponse:
    record = state.store.get_task(task_id)
    if not record:
        raise HTTPException(status_code=404, detail="任务不存在")
    return _to_response(record)


@app.post("/api/tasks/{task_id}/retry", response_model=TaskResponse)
async def retry_task(task_id: str, state: AppState = Depends(get_state)) -> TaskResponse:
    record = state.store.get_task(task_id)
    if not record:
        raise HTTPException(status_code=404, detail="任务不存在")
    if record.status != TaskStatus.FAILED:
        raise HTTPException(status_code=400, detail="仅失败任务可以重试")
    if not record.pdf_path.exists():
        raise HTTPException(status_code=410, detail="原始 PDF 已丢失，无法重试")

    updated = state.store.retry_failed_task(task_id)
    if not updated:
        raise HTTPException(status_code=500, detail="重试任务时发生错误")
    return _to_response(updated)


@app.get("/api/tasks/{task_id}/download")
async def download_task(task_id: str, state: AppState = Depends(get_state)) -> FileResponse:
    record = state.store.get_task(task_id)
    if not record or record.status != TaskStatus.SUCCEEDED or not record.summary_path:
        raise HTTPException(status_code=404, detail="任务尚未完成")
    return FileResponse(
        path=record.summary_path,
        filename=f"{record.filename.rsplit('.', 1)[0]}_summary.md",
        media_type="text/markdown",
    )


def _to_response(record: TaskRecord) -> TaskResponse:
    return TaskResponse(
        id=record.id,
        filename=record.filename,
        compression=record.compression,
        status=record.status,
        created_at=record.created_at,
        started_at=record.started_at,
        finished_at=record.finished_at,
        error_message=record.error_message,
        download_url=f"/api/tasks/{record.id}/download" if record.summary_path and record.status == TaskStatus.SUCCEEDED else None,
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:  # pragma: no cover - 宽泛异常处理
    logger.exception("Unhandled exception: %s", exc)
    return JSONResponse(status_code=500, content={"error": {"code": "INTERNAL_ERROR", "message": str(exc)}})
