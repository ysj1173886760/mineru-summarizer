import asyncio
import aiohttp
from typing import Dict, Any, Optional, List
from abc import ABC, abstractmethod
import openai
from anthropic import AsyncAnthropic
from ..utils.config import LLMConfig
import json


class LLMClient(ABC):
    """LLM客户端抽象基类"""
    
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> str:
        """生成文本"""
        pass
    
    @abstractmethod
    async def close(self):
        """关闭客户端连接"""
        pass


class OpenAIClient(LLMClient):
    """OpenAI客户端"""
    
    def __init__(self, config: LLMConfig):
        self.config = config
        if config.base_url:
            self.client = openai.AsyncOpenAI(
                api_key=config.api_key,
                base_url=config.base_url
            )
        else:
            self.client = openai.AsyncOpenAI(api_key=config.api_key)
    
    async def generate(self, prompt: str, **kwargs) -> str:
        """使用OpenAI API生成文本"""
        try:
            response = await self.client.chat.completions.create(
                model=self.config.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"OpenAI API调用失败: {str(e)}")
    
    async def close(self):
        """关闭客户端"""
        await self.client.close()


class AnthropicClient(LLMClient):
    """Anthropic Claude客户端"""
    
    def __init__(self, config: LLMConfig):
        self.config = config
        self.client = AsyncAnthropic(api_key=config.api_key)
    
    async def generate(self, prompt: str, **kwargs) -> str:
        """使用Anthropic API生成文本"""
        try:
            response = await self.client.messages.create(
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                **kwargs
            )
            return response.content[0].text
        except Exception as e:
            raise Exception(f"Anthropic API调用失败: {str(e)}")
    
    async def close(self):
        """关闭客户端"""
        await self.client.close()


class LocalClient(LLMClient):
    """本地模型客户端（通过HTTP API）"""
    
    def __init__(self, config: LLMConfig):
        self.config = config
        self.session = aiohttp.ClientSession()
    
    async def generate(self, prompt: str, **kwargs) -> str:
        """调用本地模型API"""
        if not self.config.base_url:
            raise ValueError("本地模型需要配置base_url")
        
        try:
            payload = {
                "model": self.config.model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": self.config.temperature,
                "max_tokens": self.config.max_tokens,
                **kwargs
            }
            
            async with self.session.post(
                f"{self.config.base_url}/chat/completions",
                json=payload,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status != 200:
                    raise Exception(f"HTTP {response.status}: {await response.text()}")
                
                result = await response.json()
                return result["choices"][0]["message"]["content"]
        
        except Exception as e:
            raise Exception(f"本地模型API调用失败: {str(e)}")
    
    async def close(self):
        """关闭客户端"""
        await self.session.close()


class LLMManager:
    """LLM管理器，支持并发控制和重试"""
    
    def __init__(self, config: LLMConfig, max_concurrent: int = 3):
        self.config = config
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.client = self._create_client()
        
    def _create_client(self) -> LLMClient:
        """根据配置创建客户端"""
        if self.config.provider == "openai":
            return OpenAIClient(self.config)
        elif self.config.provider == "anthropic":
            return AnthropicClient(self.config)
        elif self.config.provider == "local":
            return LocalClient(self.config)
        else:
            raise ValueError(f"不支持的LLM提供商: {self.config.provider}")
    
    async def generate_with_retry(self, prompt: str, max_retries: int = 3, **kwargs) -> str:
        """带重试的文本生成"""
        last_error = None
        
        for attempt in range(max_retries):
            try:
                async with self.semaphore:
                    result = await self.client.generate(prompt, **kwargs)
                    return result
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    # 指数退避
                    wait_time = (2 ** attempt) + 1
                    await asyncio.sleep(wait_time)
                    continue
                break
        
        raise Exception(f"重试{max_retries}次后仍失败: {str(last_error)}")
    
    async def batch_generate(self, prompts: List[str], **kwargs) -> List[str]:
        """批量生成文本"""
        tasks = []
        for prompt in prompts:
            task = self.generate_with_retry(prompt, **kwargs)
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # 处理异常
        final_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"警告: 第{i+1}个请求失败: {str(result)}")
                final_results.append(f"[生成失败: {str(result)}]")
            else:
                final_results.append(result)
        
        return final_results
    
    async def close(self):
        """关闭客户端"""
        await self.client.close()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()