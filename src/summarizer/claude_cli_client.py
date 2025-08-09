import asyncio
import subprocess
import tempfile
import json
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class ClaudeCLIConfig:
    """Claude CLI配置"""
    project_name: Optional[str] = None  # 项目名称
    model: Optional[str] = None         # 模型名称
    max_tokens: int = 4000              # 最大token数
    temperature: float = 0.3            # 温度参数
    timeout: int = 120                  # 超时时间（秒）


class ClaudeCLIManager:
    """Claude CLI客户端管理器"""
    
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
                stderr=asyncio.subprocess.PIPE
            )
            
            # 将prompt通过stdin传入
            stdout, stderr = await asyncio.wait_for(
                process.communicate(input=prompt.encode('utf-8')),
                timeout=self.config.timeout
            )
            
            if process.returncode != 0:
                error_msg = stderr.decode('utf-8', errors='ignore')
                logger.error(f"Claude CLI执行失败: {error_msg}")
                # 如果是认证错误，提供更友好的错误信息
                if "authentication" in error_msg.lower() or "login" in error_msg.lower():
                    raise RuntimeError("Claude CLI认证失败，请运行 'claude auth login' 进行认证")
                raise RuntimeError(f"Claude CLI执行失败: {error_msg}")
            
            response = stdout.decode('utf-8', errors='ignore').strip()
            
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
            logger.error(f"Claude CLI调用异常: {e}")
            return f"抱歉，生成总结时出现异常: {str(e)}"
    
    def test_claude_cli(self) -> bool:
        """测试Claude CLI是否可用"""
        try:
            result = subprocess.run(
                ["claude", "--version"],
                capture_output=True,
                text=True,
                timeout=10
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


def test_claude_cli_connection():
    """测试Claude CLI连接"""
    print("🧪 测试Claude CLI连接...")
    
    config = ClaudeCLIConfig(
        project_name=None,  # 可以指定项目名
        model=None,         # 使用默认模型
        max_tokens=500,
        temperature=0.1,
        timeout=30
    )
    
    manager = ClaudeCLIManager(config, max_concurrent=1)
    
    # 测试CLI是否可用
    if not manager.test_claude_cli():
        print("❌ Claude CLI不可用")
        return False
    
    # 测试简单调用
    async def test_call():
        async with manager:
            test_prompt = "请用中文简单介绍什么是Graph Neural Networks，不超过100字。"
            try:
                response = await manager.single_generate(test_prompt)
                print(f"✅ Claude CLI测试成功")
                print(f"📝 测试响应: {response[:200]}...")
                return True
            except Exception as e:
                print(f"❌ Claude CLI调用失败: {e}")
                return False
    
    return asyncio.run(test_call())


if __name__ == "__main__":
    # 设置日志
    logging.basicConfig(level=logging.INFO)
    
    # 运行测试
    success = test_claude_cli_connection()
    if success:
        print("\n🎉 Claude CLI集成测试通过!")
    else:
        print("\n💥 Claude CLI集成测试失败")
        print("\n📋 解决方案:")
        print("1. 确保已安装Claude CLI: pip install claude-cli")
        print("2. 确保已配置认证: claude auth login")
        print("3. 检查CLI版本: claude --version")