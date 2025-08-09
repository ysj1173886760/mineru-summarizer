#!/usr/bin/env python3
"""
检查Claude CLI是否可用
"""

import subprocess
import sys
import asyncio
import tempfile
from pathlib import Path


def check_claude_cli_installed():
    """检查Claude CLI是否已安装"""
    try:
        result = subprocess.run(
            ["claude", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print(f"✅ Claude CLI已安装: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ Claude CLI版本检查失败: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ Claude CLI未找到，请先安装")
        return False
    except Exception as e:
        print(f"❌ Claude CLI检查异常: {e}")
        return False


async def test_claude_cli_simple():
    """简单测试Claude CLI调用"""
    print("\n🧪 测试Claude CLI基本调用...")
    
    test_prompt = "请用中文简单介绍什么是人工智能，不超过50字。"
    
    try:
        # 创建进程
        process = await asyncio.create_subprocess_exec(
            "claude",
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        # 发送prompt并获取响应
        stdout, stderr = await asyncio.wait_for(
            process.communicate(input=test_prompt.encode('utf-8')),
            timeout=30
        )
        
        if process.returncode != 0:
            error_msg = stderr.decode('utf-8', errors='ignore')
            print(f"❌ Claude CLI调用失败: {error_msg}")
            return False
        
        response = stdout.decode('utf-8', errors='ignore').strip()
        
        if response:
            print(f"✅ Claude CLI调用成功")
            print(f"📝 测试响应: {response}")
            return True
        else:
            print(f"❌ Claude CLI返回空响应")
            return False
            
    except asyncio.TimeoutError:
        print(f"❌ Claude CLI调用超时")
        return False
    except Exception as e:
        print(f"❌ Claude CLI调用异常: {e}")
        return False


def main():
    print("🔍 检查Claude CLI环境\n")
    
    # 1. 检查是否安装
    if not check_claude_cli_installed():
        print("\n📋 安装步骤:")
        print("1. 请参考Claude CLI官方文档进行安装")
        print("2. 安装后运行: claude auth login")
        print("3. 再次运行此脚本验证")
        sys.exit(1)
    
    # 2. 测试基本调用
    success = asyncio.run(test_claude_cli_simple())
    
    if success:
        print(f"\n🎉 Claude CLI环境检查通过!")
        print(f"✅ 可以使用V5版本的Claude CLI功能")
        print(f"\n📋 接下来可以:")
        print(f"   python test_v5_claude_cli.py  # 运行完整测试")
        print(f"   python -m src.main_v5 ...     # 使用V5版本生成总结")
    else:
        print(f"\n💥 Claude CLI环境检查失败")
        print(f"\n🔧 可能的解决方案:")
        print(f"   1. 运行 'claude auth login' 进行认证")
        print(f"   2. 检查网络连接")
        print(f"   3. 更新Claude CLI到最新版本")
        print(f"   4. 检查Claude账户状态")
        sys.exit(1)


if __name__ == "__main__":
    main()