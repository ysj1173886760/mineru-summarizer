from pathlib import Path
from typing import Optional, Dict, Any, Literal
import yaml
import os
from dataclasses import dataclass


@dataclass
class BackendConfig:
    """后端配置基类"""
    type: Literal["llm_api", "claude_cli"]


@dataclass
class LLMAPIConfig(BackendConfig):
    """LLM API后端配置"""
    type: Literal["llm_api"] = "llm_api"
    provider: str = "openai"
    model: str = "gpt-4"
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    temperature: float = 0.3
    max_tokens: int = 4000
    timeout: int = 120


@dataclass
class ClaudeCLIConfig(BackendConfig):
    """Claude CLI后端配置"""
    type: Literal["claude_cli"] = "claude_cli"
    project_name: Optional[str] = None
    model: Optional[str] = None
    timeout: int = 180


@dataclass
class ProcessingConfig:
    """处理配置"""
    max_tokens_per_chapter: int = 8000
    max_concurrent: int = 3
    enable_checkpoint: bool = True
    checkpoint_dir: str = ".checkpoints"


@dataclass
class PolishConfig:
    """打磨配置"""
    enabled: bool = False
    temperature: float = 0.2
    concurrent_ratio: float = 0.5  # 打磨时的并发比例


@dataclass
class OutputConfig:
    """输出配置"""
    format: str = "markdown"
    language: str = "zh-CN"
    include_toc: bool = True
    include_images: bool = True
    image_path_prefix: str = "./images/"


@dataclass
class UnifiedConfig:
    """统一配置"""
    backend: BackendConfig
    processing: ProcessingConfig
    polish: PolishConfig
    output: OutputConfig
    compression_levels: Dict[int, Dict[str, str]]


def load_unified_config(config_path: Optional[Path] = None) -> UnifiedConfig:
    """加载统一配置"""
    
    # 默认配置文件路径
    if config_path is None:
        config_path = Path(__file__).parent / "config.yaml"
    
    # 加载YAML配置
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config_dict = yaml.safe_load(f)
    except FileNotFoundError:
        config_dict = {}
    
    # 解析后端配置
    backend_config = config_dict.get("backend", {})
    backend_type = backend_config.get("type", "llm_api")
    
    if backend_type == "llm_api":
        backend = LLMAPIConfig(
            provider=backend_config.get("provider", "openai"),
            model=backend_config.get("model", "gpt-4"),
            api_key=backend_config.get("api_key") or os.getenv("OPENAI_API_KEY"),
            base_url=backend_config.get("base_url") or os.getenv("OPENAI_BASE_URL"),
            temperature=backend_config.get("temperature", 0.3),
            max_tokens=backend_config.get("max_tokens", 4000),
            timeout=backend_config.get("timeout", 120)
        )
    elif backend_type == "claude_cli":
        backend = ClaudeCLIConfig(
            project_name=backend_config.get("project_name"),
            model=backend_config.get("model"),
            timeout=backend_config.get("timeout", 180)
        )
    else:
        raise ValueError(f"不支持的后端类型: {backend_type}")
    
    # 解析其他配置
    processing_config = config_dict.get("processing", {})
    processing = ProcessingConfig(
        max_tokens_per_chapter=processing_config.get("max_tokens_per_chapter", 8000),
        max_concurrent=processing_config.get("max_concurrent", 3),
        enable_checkpoint=processing_config.get("enable_checkpoint", True),
        checkpoint_dir=processing_config.get("checkpoint_dir", ".checkpoints")
    )
    
    polish_config = config_dict.get("polish", {})
    polish = PolishConfig(
        enabled=polish_config.get("enabled", False),
        temperature=polish_config.get("temperature", 0.2),
        concurrent_ratio=polish_config.get("concurrent_ratio", 0.5)
    )
    
    output_config = config_dict.get("output", {})
    output = OutputConfig(
        format=output_config.get("format", "markdown"),
        language=output_config.get("language", "zh-CN"),
        include_toc=output_config.get("include_toc", True),
        include_images=output_config.get("include_images", True)
    )
    
    # 压缩级别配置
    compression_levels = config_dict.get("compression_levels", {
        30: {
            "strategy": "concise_summary",
            "prompt_template": "请对以下英文学术文本进行简洁的中文总结，保留30%的信息量，只包含最重要的创新点和结论。要求：直接输出总结内容，不要添加关于总结过程的说明性文字："
        },
        50: {
            "strategy": "standard_summary",
            "prompt_template": "请对以下英文学术文本进行中文总结，保留50%的信息量，重点关注核心观点和主要发现。要求：直接输出总结内容，不要添加关于总结过程的说明性文字："
        },
        70: {
            "strategy": "detailed_summary",
            "prompt_template": "请对以下英文学术文本进行详细的中文总结，保留70%的信息量，包含主要论点、方法和结果。要求：直接输出总结内容，不要添加关于总结过程的说明性文字："
        }
    })
    
    return UnifiedConfig(
        backend=backend,
        processing=processing,
        polish=polish,
        output=output,
        compression_levels=compression_levels
    )


def save_config_template(output_path: Path) -> None:
    """保存配置模板"""
    template = {
        "backend": {
            "type": "claude_cli",  # 或 "llm_api"
            # LLM API配置
            "provider": "openai",
            "model": "gpt-4",
            "api_key": "${OPENAI_API_KEY}",
            "base_url": "${OPENAI_BASE_URL}",
            "temperature": 0.3,
            "max_tokens": 4000,
            "timeout": 120,
            # Claude CLI配置  
            "project_name": None,
            # "model": "sonnet-3-5",
        },
        "processing": {
            "max_tokens_per_chapter": 8000,
            "max_concurrent": 3,
            "enable_checkpoint": True,
            "checkpoint_dir": ".checkpoints"
        },
        "polish": {
            "enabled": False,
            "temperature": 0.2,
            "concurrent_ratio": 0.5
        },
        "output": {
            "format": "markdown",
            "language": "zh-CN",
            "include_toc": True,
            "include_images": True
        },
        "compression_levels": {
            30: {
                "strategy": "concise_summary",
                "prompt_template": "请对以下英文学术文本进行简洁的中文总结，保留30%的信息量，只包含最重要的创新点和结论。专有技术名词保持英文原文，包括：Graph Neural Networks (GNNs), Graph Foundation Models (GFMs), Transformer, Pre-training, Fine-tuning等。要求：直接输出总结内容，不要添加关于总结过程的说明性文字："
            },
            50: {
                "strategy": "standard_summary", 
                "prompt_template": "请对以下英文学术文本进行中文总结，保留50%的信息量，重点关注核心观点和主要发现。专有技术名词保持英文原文。要求：直接输出总结内容，不要添加关于总结过程的说明性文字："
            },
            70: {
                "strategy": "detailed_summary",
                "prompt_template": "请对以下英文学术文本进行详细的中文总结，保留70%的信息量，包含主要论点、方法和结果。专有技术名词保持英文原文。要求：直接输出总结内容，不要添加关于总结过程的说明性文字："
            }
        }
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(template, f, default_flow_style=False, allow_unicode=True, indent=2)
    
    print(f"✅ 配置模板已保存到: {output_path}")


if __name__ == "__main__":
    # 生成配置模板
    template_path = Path(__file__).parent / "config_template.yaml"
    save_config_template(template_path)