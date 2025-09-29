from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml


@dataclass
class WebConfig:
    """Web 服务配置项。"""

    uploads_dir: Path
    results_dir: Path
    logs_dir: Path
    database_path: Path
    poll_interval_seconds: float
    worker_interval_seconds: float
    worker_concurrency: int
    max_file_mb: int
    base_config_path: Path
    default_compression: int
    mineru_server: str
    mineru_lang: str
    mineru_backend: str
    mineru_method: str
    formula_enable: bool
    table_enable: bool
    keep_temp_files: bool = False

    @property
    def max_file_bytes(self) -> int:
        return self.max_file_mb * 1024 * 1024


def load_web_config(path: Optional[Path] = None) -> WebConfig:
    """加载 Web 层配置。"""

    if path is None:
        path = Path(__file__).resolve().parent.parent / "web_config.yaml"

    with open(path, "r", encoding="utf-8") as fh:
        raw = yaml.safe_load(fh) or {}

    base_dir = path.parent.parent  # repo 根目录

    def _as_path(value: Optional[str], default: str) -> Path:
        resolved = Path(value or default)
        if not resolved.is_absolute():
            resolved = (base_dir / resolved).resolve()
        return resolved

    return WebConfig(
        uploads_dir=_as_path(raw.get("uploads_dir"), "var/uploads"),
        results_dir=_as_path(raw.get("results_dir"), "var/results"),
        logs_dir=_as_path(raw.get("logs_dir"), "var/logs"),
        database_path=_as_path(raw.get("database_path"), "var/web_tasks.db"),
        poll_interval_seconds=float(raw.get("poll_interval_seconds", 5)),
        worker_interval_seconds=float(raw.get("worker_interval_seconds", 2)),
        worker_concurrency=int(raw.get("worker_concurrency", 1)),
        max_file_mb=int(raw.get("max_file_mb", 50)),
        base_config_path=_as_path(raw.get("base_config_path"), "mineru-config.yaml"),
        default_compression=int(raw.get("default_compression", 50)),
        mineru_server=str(raw.get("mineru_server", "http://localhost:5000")),
        mineru_lang=str(raw.get("mineru_lang", "ch")),
        mineru_backend=str(raw.get("mineru_backend", "pipeline")),
        mineru_method=str(raw.get("mineru_method", "auto")),
        formula_enable=bool(raw.get("formula_enable", True)),
        table_enable=bool(raw.get("table_enable", True)),
        keep_temp_files=bool(raw.get("keep_temp_files", False)),
    )
