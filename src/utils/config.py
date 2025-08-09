from pathlib import Path
from typing import Dict, Any, Optional
import yaml
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    provider: str = "openai"
    model: str = "gpt-4"
    api_key: Optional[str] = None
    temperature: float = 0.3
    max_tokens: int = 4000
    base_url: Optional[str] = None


class ProcessingConfig(BaseModel):
    chunk_size: int = 3000
    overlap: int = 200
    preserve_structure: bool = True
    include_images: bool = True
    max_concurrent: int = 3


class OutputConfig(BaseModel):
    format: str = "markdown"
    language: str = "zh-CN"
    include_toc: bool = True
    include_images: bool = True
    image_path_prefix: str = "./images/"


class CompressionLevel(BaseModel):
    strategy: str
    detail_level: str
    prompt_template: str


class Config(BaseModel):
    llm: LLMConfig = Field(default_factory=LLMConfig)
    processing: ProcessingConfig = Field(default_factory=ProcessingConfig)
    output: OutputConfig = Field(default_factory=OutputConfig)
    compression_levels: Dict[int, CompressionLevel] = Field(default_factory=dict)


def load_config(config_path: Optional[str] = None) -> Config:
    """加载配置文件"""
    load_dotenv()
    
    if config_path is None:
        config_path = Path(__file__).parent.parent.parent / "config" / "default_config.yaml"
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config_data = yaml.safe_load(f)
    
    # 处理环境变量替换
    config_data = _replace_env_vars(config_data)
    
    # 转换compression_levels
    compression_levels = {}
    for level, data in config_data.get('compression_levels', {}).items():
        compression_levels[int(level)] = CompressionLevel(**data)
    config_data['compression_levels'] = compression_levels
    
    return Config(**config_data)


def _replace_env_vars(obj: Any) -> Any:
    """递归替换配置中的环境变量"""
    if isinstance(obj, dict):
        return {k: _replace_env_vars(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_replace_env_vars(item) for item in obj]
    elif isinstance(obj, str) and obj.startswith('${') and obj.endswith('}'):
        env_var = obj[2:-1]
        return os.getenv(env_var, obj)
    else:
        return obj