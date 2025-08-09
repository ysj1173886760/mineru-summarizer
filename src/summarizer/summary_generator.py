from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import asyncio
from tqdm import tqdm
from .chunk_processor import Chunk
from .llm_client import LLMManager
from ..utils.config import Config, CompressionLevel


@dataclass
class SummaryResult:
    """总结结果数据类"""
    chunk_id: str
    original_content: str
    summary: str
    section_title: str
    section_level: int
    token_count: int
    compression_ratio: float
    metadata: Dict[str, Any] = None


class SummaryGenerator:
    """总结生成器"""
    
    def __init__(self, config: Config):
        self.config = config
        self.llm_manager = LLMManager(
            config.llm, 
            max_concurrent=config.processing.max_concurrent
        )
        
    async def generate_summaries(
        self, 
        chunks: List[Chunk], 
        compression_level: int
    ) -> List[SummaryResult]:
        """生成总结"""
        if compression_level not in self.config.compression_levels:
            raise ValueError(f"不支持的压缩级别: {compression_level}")
        
        compression_config = self.config.compression_levels[compression_level]
        
        print(f"开始生成总结 (压缩级别: {compression_level}%)")
        print(f"总共需要处理 {len(chunks)} 个文档块")
        
        # 生成提示词
        prompts = self._generate_prompts(chunks, compression_config)
        
        # 批量调用LLM
        with tqdm(total=len(prompts), desc="生成总结") as pbar:
            summaries = []
            batch_size = self.config.processing.max_concurrent
            
            for i in range(0, len(prompts), batch_size):
                batch_prompts = prompts[i:i+batch_size]
                batch_chunks = chunks[i:i+batch_size]
                
                batch_results = await self.llm_manager.batch_generate(batch_prompts)
                
                # 创建结果对象
                for chunk, summary in zip(batch_chunks, batch_results):
                    result = SummaryResult(
                        chunk_id=chunk.id,
                        original_content=chunk.content,
                        summary=summary,
                        section_title=chunk.section_title,
                        section_level=chunk.section_level,
                        token_count=len(summary.split()),
                        compression_ratio=self._calculate_compression_ratio(
                            chunk.content, summary
                        ),
                        metadata={
                            'compression_level': compression_level,
                            'strategy': compression_config.strategy,
                            'original_token_count': chunk.token_count
                        }
                    )
                    summaries.append(result)
                
                pbar.update(len(batch_prompts))
        
        return summaries
    
    def _generate_prompts(
        self, 
        chunks: List[Chunk], 
        compression_config: CompressionLevel
    ) -> List[str]:
        """生成提示词"""
        prompts = []
        
        for chunk in chunks:
            # 基础提示词
            base_prompt = compression_config.prompt_template
            
            # 添加上下文信息
            context_info = ""
            if chunk.context:
                context_info = f"\n\n上下文信息: {chunk.context}"
            
            # 添加章节信息
            section_info = f"\n\n这是来自章节「{chunk.section_title}」(级别 {chunk.section_level}) 的内容。"
            
            # 添加特殊指令
            special_instructions = self._get_special_instructions(
                chunk, compression_config
            )
            
            # 组合完整提示词
            full_prompt = f"""{base_prompt}

{section_info}{context_info}

{special_instructions}

原文内容:
{chunk.content}

请用中文回答："""
            
            prompts.append(full_prompt)
        
        return prompts
    
    def _get_special_instructions(
        self, 
        chunk: Chunk, 
        compression_config: CompressionLevel
    ) -> str:
        """获取特殊指令"""
        instructions = []
        
        # 根据策略添加指令
        if compression_config.strategy == "translate":
            instructions.append("请确保翻译的准确性，特别是专业术语和概念。")
        elif compression_config.strategy == "detailed_summary":
            instructions.append("保留重要的技术细节、实验结果和数据。")
        elif compression_config.strategy == "standard_summary":
            instructions.append("重点关注主要观点、方法论和关键发现。")
        elif compression_config.strategy == "concise_summary":
            instructions.append("只保留最核心的创新点和主要结论。")
        elif compression_config.strategy == "brief_summary":
            instructions.append("用最简洁的语言概括核心内容。")
        
        # 根据内容类型添加指令
        if "![" in chunk.content:
            instructions.append("注意：原文包含图片链接，请在总结中保留这些图片链接，保持其格式不变。")
        
        if chunk.section_level == 1:
            instructions.append("这是主要章节，请确保涵盖该章节的整体结构和主要内容。")
        
        # 学术写作风格指令
        instructions.append("保持学术写作的严谨性和专业性。")
        instructions.append("使用中文学术写作的规范表达方式。")
        
        if not instructions:
            return ""
        
        return "特别要求:\n" + "\n".join(f"- {inst}" for inst in instructions)
    
    def _calculate_compression_ratio(self, original: str, summary: str) -> float:
        """计算压缩比例"""
        original_length = len(original)
        summary_length = len(summary)
        
        if original_length == 0:
            return 0.0
        
        return summary_length / original_length
    
    async def close(self):
        """关闭LLM连接"""
        await self.llm_manager.close()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class SummaryPostProcessor:
    """总结后处理器"""
    
    @staticmethod
    def merge_section_summaries(summaries: List[SummaryResult]) -> Dict[str, str]:
        """合并同一章节的多个总结"""
        section_summaries = {}
        
        # 按章节分组
        sections = {}
        for summary in summaries:
            section_key = f"{summary.section_level}_{summary.section_title}"
            if section_key not in sections:
                sections[section_key] = []
            sections[section_key].append(summary)
        
        # 合并每个章节的总结
        for section_key, section_results in sections.items():
            # 按chunk_id排序确保顺序
            section_results.sort(key=lambda x: x.chunk_id)
            
            merged_content = []
            for result in section_results:
                merged_content.append(result.summary)
            
            section_summaries[section_key] = "\n\n".join(merged_content)
        
        return section_summaries
    
    @staticmethod
    def calculate_overall_stats(summaries: List[SummaryResult]) -> Dict[str, Any]:
        """计算总体统计信息"""
        if not summaries:
            return {}
        
        total_original_tokens = sum(r.metadata.get('original_token_count', 0) for r in summaries)
        total_summary_tokens = sum(r.token_count for r in summaries)
        
        compression_ratios = [r.compression_ratio for r in summaries if r.compression_ratio > 0]
        avg_compression = sum(compression_ratios) / len(compression_ratios) if compression_ratios else 0
        
        return {
            'total_chunks': len(summaries),
            'total_original_tokens': total_original_tokens,
            'total_summary_tokens': total_summary_tokens,
            'overall_compression_ratio': total_summary_tokens / total_original_tokens if total_original_tokens > 0 else 0,
            'average_compression_ratio': avg_compression,
            'sections_processed': len(set(r.section_title for r in summaries))
        }