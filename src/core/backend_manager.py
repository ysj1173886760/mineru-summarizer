import asyncio
import subprocess
import tempfile
import json
from pathlib import Path
from typing import List, Optional, Protocol, Dict, Any
from dataclasses import dataclass
import logging
import aiohttp

try:
    from openai import AsyncOpenAI
    from anthropic import AsyncAnthropic

    OPENAI_AVAILABLE = True
    ANTHROPIC_CLIENT_AVAILABLE = True
except ImportError:
    AsyncOpenAI = None
    AsyncAnthropic = None
    OPENAI_AVAILABLE = False
    ANTHROPIC_CLIENT_AVAILABLE = False

from ..config.unified_config import UnifiedConfig, LLMAPIConfig, ClaudeCLIConfig

logger = logging.getLogger(__name__)


class BackendProtocol(Protocol):
    """后端接口协议"""

    async def single_generate(self, prompt: str) -> str:
        """生成单个回复"""
        ...

    async def batch_generate(self, prompts: List[str]) -> List[str]:
        """批量生成回复"""
        ...

    async def __aenter__(self):
        """异步上下文管理器入口"""
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器出口"""
        ...


@dataclass
class GenerationRequest:
    """生成请求"""

    prompt: str
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None


class LLMAPIBackend:
    """LLM API后端"""

    def __init__(self, config: LLMAPIConfig, max_concurrent: int = 3):
        self.config = config
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.session: Optional[aiohttp.ClientSession] = None
        self.openai_client: Optional[AsyncOpenAI] = None
        self.anthropic_client: Optional[AsyncAnthropic] = None

    async def __aenter__(self):
        # 初始化OpenAI客户端
        if self.config.provider == "openai" and OPENAI_AVAILABLE:
            self.openai_client = AsyncOpenAI(
                api_key=self.config.api_key,
                base_url=self.config.base_url,
                timeout=self.config.timeout,
            )
        # 初始化Anthropic客户端
        elif self.config.provider == "anthropic" and ANTHROPIC_CLIENT_AVAILABLE:
            self.anthropic_client = AsyncAnthropic(
                api_key=self.config.api_key, timeout=self.config.timeout
            )
        else:
            # 回退到aiohttp
            self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.openai_client:
            await self.openai_client.close()
        if self.anthropic_client:
            await self.anthropic_client.close()
        if self.session:
            await self.session.close()

    async def single_generate(self, prompt: str) -> str:
        """生成单个回复"""
        async with self.semaphore:
            return await self._call_api(prompt)

    async def batch_generate(self, prompts: List[str]) -> List[str]:
        """批量生成回复"""
        tasks = [self.single_generate(prompt) for prompt in prompts]
        return await asyncio.gather(*tasks)

    async def _call_api(self, prompt: str) -> str:
        """调用LLM API"""
        try:
            if self.config.provider == "openai":
                if self.openai_client and OPENAI_AVAILABLE:
                    return await self._call_openai_client(prompt)
                else:
                    return await self._call_openai_api(prompt)
            elif self.config.provider == "anthropic":
                if self.anthropic_client and ANTHROPIC_CLIENT_AVAILABLE:
                    return await self._call_anthropic_client(prompt)
                else:
                    return await self._call_anthropic_api(prompt)
            else:
                raise ValueError(f"不支持的提供商: {self.config.provider}")
        except Exception as e:
            error_msg = str(e)
            logger.error(f"LLM API调用失败: {error_msg}")
            print(f"❌ LLM API请求失败: {error_msg}")
            return f"抱歉，生成总结时出现问题: {error_msg}"

    async def _call_openai_client(self, prompt: str) -> str:
        """使用AsyncOpenAI客户端调用API"""
        try:
            response = await self.openai_client.chat.completions.create(
                model=self.config.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            error_msg = str(e)
            # 检查限流错误
            if "rate limit" in error_msg.lower() or "429" in error_msg:
                raise RuntimeError("RATE_LIMIT_ERROR")
            # 提供更友好的错误信息
            if "401" in error_msg:
                error_msg += "\n   可能原因: API密钥无效或未设置"
            elif "403" in error_msg:
                error_msg += "\n   可能原因: API密钥权限不足"
            elif "404" in error_msg:
                error_msg += "\n   可能原因: 模型不存在或base_url配置错误"
            raise RuntimeError(f"OpenAI API请求失败: {error_msg}")

    async def _call_anthropic_client(self, prompt: str) -> str:
        """使用AsyncAnthropic客户端调用API"""
        try:
            response = await self.anthropic_client.messages.create(
                model=self.config.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
            )
            return response.content[0].text.strip()
        except Exception as e:
            error_msg = str(e)
            # 检查限流错误
            if "rate limit" in error_msg.lower() or "429" in error_msg:
                raise RuntimeError("RATE_LIMIT_ERROR")
            # 提供更友好的错误信息
            if "401" in error_msg:
                error_msg += "\n   可能原因: API密钥无效或未设置"
            elif "403" in error_msg:
                error_msg += "\n   可能原因: API密钥权限不足"
            raise RuntimeError(f"Anthropic API请求失败: {error_msg}")

    async def _call_openai_api(self, prompt: str) -> str:
        """调用OpenAI兼容API"""
        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.config.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }

        # 构造API URL，确保格式正确
        if self.config.base_url:
            # 移除尾部斜杠，确保URL格式正确
            base_url = self.config.base_url.rstrip("/")
            # 如果base_url已经包含v1，则只添加chat/completions
            if base_url.endswith("/v1"):
                url = f"{base_url}/chat/completions"
            else:
                url = f"{base_url}/v1/chat/completions"
        else:
            url = "https://api.openai.com/v1/chat/completions"

        logger.debug(f"调用OpenAI API: {url}")

        timeout = aiohttp.ClientTimeout(total=self.config.timeout)
        async with self.session.post(
            url, json=payload, headers=headers, timeout=timeout
        ) as response:
            if response.status != 200:
                error_text = await response.text()
                error_detail = f"HTTP {response.status}: {error_text}"

                # 提供更详细的错误信息
                if response.status == 405:
                    error_detail += (
                        f"\n   请求URL: {url}\n   可能原因: URL路径错误或API端点不支持POST方法"
                    )
                elif response.status == 404:
                    error_detail += (
                        f"\n   请求URL: {url}\n   可能原因: API端点不存在，请检查base_url配置"
                    )
                elif response.status == 401:
                    error_detail += "\n   可能原因: API密钥无效或未设置"
                elif response.status == 403:
                    error_detail += "\n   可能原因: API密钥权限不足"

                # 检查是否是限流错误
                if response.status == 429 or "rate limit" in error_text.lower():
                    raise RuntimeError("RATE_LIMIT_ERROR")
                raise RuntimeError(f"OpenAI API请求失败: {error_detail}")

            result = await response.json()
            return result["choices"][0]["message"]["content"].strip()

    async def _call_anthropic_api(self, prompt: str) -> str:
        """调用Anthropic API"""
        headers = {
            "x-api-key": self.config.api_key,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01",
        }

        payload = {
            "model": self.config.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }

        url = "https://api.anthropic.com/v1/messages"
        logger.debug(f"调用Anthropic API: {url}")

        timeout = aiohttp.ClientTimeout(total=self.config.timeout)
        async with self.session.post(
            url, json=payload, headers=headers, timeout=timeout
        ) as response:
            if response.status != 200:
                error_text = await response.text()
                error_detail = f"HTTP {response.status}: {error_text}"

                # 提供更详细的错误信息
                if response.status == 405:
                    error_detail += (
                        f"\n   请求URL: {url}\n   可能原因: URL路径错误或API端点不支持POST方法"
                    )
                elif response.status == 404:
                    error_detail += f"\n   请求URL: {url}\n   可能原因: API端点不存在"
                elif response.status == 401:
                    error_detail += "\n   可能原因: API密钥无效或未设置"
                elif response.status == 403:
                    error_detail += "\n   可能原因: API密钥权限不足"

                # 检查是否是限流错误
                if response.status == 429 or "rate limit" in error_text.lower():
                    raise RuntimeError("RATE_LIMIT_ERROR")
                raise RuntimeError(f"Anthropic API请求失败: {error_detail}")

            result = await response.json()
            return result["content"][0]["text"].strip()


class ClaudeCLIBackend:
    """Claude CLI后端"""

    def __init__(self, config: ClaudeCLIConfig, max_concurrent: int = 3):
        self.config = config
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def single_generate(self, prompt: str) -> str:
        """生成单个回复"""
        async with self.semaphore:
            return await self._call_claude_cli(prompt)

    async def batch_generate(self, prompts: List[str]) -> List[str]:
        """批量生成回复"""
        tasks = [self.single_generate(prompt) for prompt in prompts]
        return await asyncio.gather(*tasks)

    async def _call_claude_cli(self, prompt: str) -> str:
        """调用Claude CLI"""
        try:
            # 构建命令 - 使用 --print 模式进行非交互式输出
            cmd = ["claude", "--print"]

            # 添加模型参数（如果指定）
            if self.config.model:
                cmd.extend(["--model", self.config.model])

            # 执行命令
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            # 将prompt通过stdin传入
            stdout, stderr = await asyncio.wait_for(
                process.communicate(input=prompt.encode("utf-8")),
                timeout=self.config.timeout,
            )

            if process.returncode != 0:
                error_msg = stderr.decode("utf-8", errors="ignore")
                logger.error(f"Claude CLI执行失败: {error_msg}")

                # 检查限流错误
                if "rate limit" in error_msg.lower() or "429" in error_msg:
                    raise RuntimeError("RATE_LIMIT_ERROR")

                # 如果是认证错误，提供更友好的错误信息
                if (
                    "authentication" in error_msg.lower()
                    or "login" in error_msg.lower()
                ):
                    raise RuntimeError("Claude CLI认证失败，请运行 'claude auth login' 进行认证")
                raise RuntimeError(f"Claude CLI执行失败: {error_msg}")

            response = stdout.decode("utf-8", errors="ignore").strip()

            if not response:
                logger.warning("Claude CLI返回空响应")
                return "抱歉，生成总结时出现问题，请稍后重试。"

            return response

        except asyncio.TimeoutError:
            logger.error(f"Claude CLI调用超时 (>{self.config.timeout}s)")
            return "抱歉，生成总结超时，请稍后重试。"
        except FileNotFoundError:
            logger.error("Claude CLI未找到，请确保已安装并在PATH中")
            raise RuntimeError("Claude CLI未找到，请确保已安装Claude CLI工具")
        except Exception as e:
            if str(e) == "RATE_LIMIT_ERROR":
                raise e  # 传播限流错误
            logger.error(f"Claude CLI调用异常: {e}")
            return f"抱歉，生成总结时出现异常: {str(e)}"

    def test_cli_available(self) -> bool:
        """测试Claude CLI是否可用"""
        try:
            result = subprocess.run(
                ["claude", "--version"], capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                logger.info(f"Claude CLI版本: {result.stdout.strip()}")
                return True
            else:
                logger.error(f"Claude CLI测试失败: {result.stderr}")
                return False
        except FileNotFoundError:
            logger.error("Claude CLI未找到")
            return False
        except Exception as e:
            logger.error(f"Claude CLI测试异常: {e}")
            return False


class BackendManager:
    """后端管理器工厂"""

    @staticmethod
    def create_backend(config: UnifiedConfig) -> BackendProtocol:
        """创建后端实例"""
        if isinstance(config.backend, LLMAPIConfig):
            return LLMAPIBackend(config.backend, config.processing.max_concurrent)
        elif isinstance(config.backend, ClaudeCLIConfig):
            return ClaudeCLIBackend(config.backend, config.processing.max_concurrent)
        else:
            raise ValueError(f"不支持的后端类型: {type(config.backend)}")

    @staticmethod
    def validate_backend(config: UnifiedConfig) -> bool:
        """验证后端配置"""
        if isinstance(config.backend, LLMAPIConfig):
            if not config.backend.api_key:
                print("❌ LLM API密钥未配置")
                return False
            print(f"✅ LLM API后端: {config.backend.provider}/{config.backend.model}")
            return True

        elif isinstance(config.backend, ClaudeCLIConfig):
            backend = ClaudeCLIBackend(config.backend)
            if not backend.test_cli_available():
                print("❌ Claude CLI不可用")
                print("   解决方案:")
                print("   1. 安装Claude CLI")
                print("   2. 运行 'claude auth login' 进行认证")
                return False
            print(f"✅ Claude CLI后端: {config.backend.model or '默认模型'}")
            return True

        else:
            print(f"❌ 不支持的后端类型: {type(config.backend)}")
            return False
