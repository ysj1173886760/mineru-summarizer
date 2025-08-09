#!/usr/bin/env python3

import click
import asyncio
from pathlib import Path
import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, str(Path(__file__).parent))

from src.main import MinerUSummarizer
from src.utils.config import load_config


@click.command()
@click.argument('input_dir', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--output', '-o', type=click.Path(), default='summary.md', 
              help='输出文件路径 (默认: summary.md)')
@click.option('--compression', '-c', type=click.IntRange(15, 100), default=50,
              help='压缩级别 15-100% (默认: 50)')
@click.option('--config', type=click.Path(exists=True), 
              help='配置文件路径 (可选)')
@click.option('--model', type=str, 
              help='LLM模型名称 (覆盖配置文件)')
@click.option('--provider', type=click.Choice(['openai', 'anthropic', 'local']),
              help='LLM提供商 (覆盖配置文件)')
@click.option('--no-images', is_flag=True, default=False,
              help='不包含图片引用')
@click.option('--no-toc', is_flag=True, default=False,
              help='不生成目录')
@click.option('--max-concurrent', type=int, default=3,
              help='最大并发请求数 (默认: 3)')
@click.option('--chunk-size', type=int, default=3000,
              help='分块大小 (默认: 3000)')
@click.option('--verbose', '-v', is_flag=True, default=False,
              help='详细输出')
def main(input_dir, output, compression, config, model, provider, no_images, 
         no_toc, max_concurrent, chunk_size, verbose):
    """
    MinerU内容总结器
    
    将MinerU提取的学术论文数据转换为指定压缩比例的中文总结。
    
    INPUT_DIR: MinerU输出目录，包含content_list.json等文件
    """
    
    input_path = Path(input_dir)
    output_path = Path(output)
    
    # 设置详细输出
    if verbose:
        import logging
        logging.basicConfig(level=logging.INFO)
    
    # 显示基本信息
    click.echo(f"🔧 MinerU内容总结器")
    click.echo(f"📁 输入目录: {input_path}")
    click.echo(f"📄 输出文件: {output_path}")
    click.echo(f"📊 压缩级别: {compression}%")
    
    # 验证输入目录
    required_files = ['content_list.json', 'full.md']
    missing_files = []
    
    for pattern in ['*content_list.json', 'full.md']:
        if not list(input_path.glob(pattern)):
            missing_files.append(pattern)
    
    if missing_files:
        click.echo(f"❌ 错误: 输入目录缺少必要文件: {missing_files}", err=True)
        click.echo("请确保输入目录是有效的MinerU输出目录", err=True)
        sys.exit(1)
    
    # 加载配置
    try:
        app_config = load_config(config)
        click.echo(f"⚙️  配置加载成功")
    except Exception as e:
        click.echo(f"❌ 配置加载失败: {e}", err=True)
        sys.exit(1)
    
    # 命令行参数覆盖配置
    if model:
        app_config.llm.model = model
    if provider:
        app_config.llm.provider = provider
    if no_images:
        app_config.output.include_images = False
    if no_toc:
        app_config.output.include_toc = False
    if max_concurrent:
        app_config.processing.max_concurrent = max_concurrent
    if chunk_size:
        app_config.processing.chunk_size = chunk_size
    
    # 验证API密钥
    if not app_config.llm.api_key:
        click.echo("❌ 错误: 未配置API密钥", err=True)
        if app_config.llm.provider == 'openai':
            click.echo("请设置环境变量: OPENAI_API_KEY", err=True)
        elif app_config.llm.provider == 'anthropic':
            click.echo("请设置环境变量: ANTHROPIC_API_KEY", err=True)
        click.echo("或者在配置文件中设置api_key", err=True)
        sys.exit(1)
    
    # 显示配置信息
    click.echo(f"🤖 LLM提供商: {app_config.llm.provider}")
    click.echo(f"🧠 模型: {app_config.llm.model}")
    click.echo(f"⚡ 并发数: {app_config.processing.max_concurrent}")
    click.echo(f"📦 分块大小: {app_config.processing.chunk_size}")
    
    # 确认处理
    if not click.confirm(f"\n开始处理？"):
        click.echo("已取消")
        sys.exit(0)
    
    # 执行总结
    async def run_summary():
        try:
            summarizer = MinerUSummarizer(app_config)
            await summarizer.summarize(input_path, output_path, compression)
        except KeyboardInterrupt:
            click.echo("\n⏹️  用户中断处理")
            sys.exit(1)
        except Exception as e:
            click.echo(f"\n❌ 处理失败: {e}", err=True)
            if verbose:
                import traceback
                traceback.print_exc()
            sys.exit(1)
    
    # 运行异步任务
    try:
        asyncio.run(run_summary())
    except KeyboardInterrupt:
        click.echo("\n⏹️  用户中断处理")
        sys.exit(1)


@click.group()
def cli():
    """MinerU内容总结器命令行工具"""
    pass


@cli.command()
@click.argument('input_dir', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def info(input_dir):
    """显示MinerU数据的基本信息"""
    input_path = Path(input_dir)
    
    click.echo(f"📁 MinerU数据信息: {input_path}")
    
    # 检查文件
    files_info = []
    
    content_list_files = list(input_path.glob("*content_list.json"))
    if content_list_files:
        files_info.append(f"✅ content_list.json: {content_list_files[0].name}")
    else:
        files_info.append("❌ content_list.json: 未找到")
    
    full_md = input_path / "full.md"
    if full_md.exists():
        size_mb = full_md.stat().st_size / 1024 / 1024
        files_info.append(f"✅ full.md: {size_mb:.1f} MB")
    else:
        files_info.append("❌ full.md: 未找到")
    
    layout_json = input_path / "layout.json"
    if layout_json.exists():
        files_info.append("✅ layout.json: 存在")
    else:
        files_info.append("❌ layout.json: 未找到")
    
    images_dir = input_path / "images"
    if images_dir.exists():
        image_count = len(list(images_dir.glob("*.jpg")) + list(images_dir.glob("*.png")))
        files_info.append(f"✅ images/: {image_count} 个图片")
    else:
        files_info.append("❌ images/: 目录不存在")
    
    for info in files_info:
        click.echo(f"  {info}")
    
    # 尝试解析内容
    if content_list_files:
        try:
            import json
            with open(content_list_files[0], 'r', encoding='utf-8') as f:
                content_data = json.load(f)
            
            text_items = [item for item in content_data if item.get('type') == 'text']
            title_items = [item for item in text_items if item.get('text_level', 0) > 0]
            
            click.echo(f"\n📊 内容统计:")
            click.echo(f"  总文本项: {len(text_items)} 个")
            click.echo(f"  标题项: {len(title_items)} 个")
            
            if title_items:
                click.echo(f"  主要标题:")
                for item in title_items[:5]:  # 显示前5个标题
                    level = item.get('text_level', 1)
                    title = item.get('text', '')[:50]
                    click.echo(f"    {'  ' * (level-1)}• {title}")
        
        except Exception as e:
            click.echo(f"  ⚠️  解析content_list.json失败: {e}")


# 添加子命令到主命令组
cli.add_command(main, name='summarize')

if __name__ == '__main__':
    cli()