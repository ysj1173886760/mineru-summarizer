import json
from pathlib import Path
from typing import List, Dict, Any, Optional
import re


def count_tokens(text: str) -> int:
    """简单的token计数估算（1个token约等于0.75个英文单词）"""
    words = len(text.split())
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    return int(words * 1.3 + chinese_chars * 1.5)


def truncate_text(text: str, max_tokens: int) -> str:
    """根据token限制截断文本"""
    if count_tokens(text) <= max_tokens:
        return text
    
    # 简单截断策略：按比例截断
    ratio = max_tokens / count_tokens(text)
    target_length = int(len(text) * ratio * 0.9)  # 留10%余量
    return text[:target_length] + "..."


def ensure_dir(path: Path) -> None:
    """确保目录存在"""
    path.mkdir(parents=True, exist_ok=True)


def load_json(file_path: Path) -> Dict[str, Any]:
    """加载JSON文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data: Dict[str, Any], file_path: Path) -> None:
    """保存JSON文件"""
    ensure_dir(file_path.parent)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def clean_text(text: str) -> str:
    """清理文本中的多余空白字符"""
    # 移除多余的空白字符
    text = re.sub(r'\s+', ' ', text)
    # 移除行首行尾空白
    text = text.strip()
    return text


def extract_title_level(text: str) -> Optional[int]:
    """从文本中提取标题级别"""
    # 检查markdown格式标题
    if text.startswith('#'):
        return len(text) - len(text.lstrip('#'))
    return None


def is_likely_title(text: str, text_level: Optional[int] = None) -> bool:
    """判断文本是否可能是标题"""
    if text_level and text_level > 0:
        return True
    
    # 其他启发式规则
    if len(text) < 100 and not text.endswith('.'):
        return True
    
    return False