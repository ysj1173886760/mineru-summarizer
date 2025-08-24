#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF解析与总结完整流程
整合MinerU client和mineru-summarizer，实现从PDF到最终markdown的完整处理流程
"""

import os
import sys
import argparse
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import Optional

# 导入MinerU客户端
from mineru.client import MinerUClient


class PDFSummarizer:
    """PDF解析与总结器"""
    
    def __init__(self, mineru_server: str = "http://localhost:5000"):
        """
        初始化
        
        Args:
            mineru_server: MinerU服务器地址
        """
        self.mineru_client = MinerUClient(mineru_server)
        self.mineru_server = mineru_server
    
    def process_pdf(
        self,
        pdf_path: str,
        output_path: str,
        compression: int = 50,
        enable_polish: bool = False,
        temp_dir: Optional[str] = None,
        keep_temp: bool = False,
        config_path: Optional[str] = None,
        backend: Optional[str] = None,
        mineru_lang: str = "ch",
        mineru_backend: str = "pipeline",
        mineru_method: str = "auto",
        formula_enable: bool = True,
        table_enable: bool = True,
        vlm_server_url: Optional[str] = None
    ) -> bool:
        """
        完整的PDF处理流程：PDF -> MinerU解析 -> mineru-summarizer总结
        
        Args:
            pdf_path: 输入PDF文件路径
            output_path: 最终输出markdown文件路径
            compression: 压缩级别 (30/50/70/100)
            enable_polish: 是否启用二次打磨
            temp_dir: 临时目录（如果为None则自动创建）
            keep_temp: 是否保留临时文件
            config_path: mineru-summarizer配置文件路径
            backend: 强制使用指定后端
            mineru_lang: MinerU语言设置
            mineru_backend: MinerU后端设置
            mineru_method: MinerU解析方法
            formula_enable: 启用公式解析
            table_enable: 启用表格解析
            vlm_server_url: VLM服务器URL
            
        Returns:
            bool: 是否成功
        """
        # 检查PDF文件是否存在
        if not os.path.exists(pdf_path):
            print(f"❌ 错误: PDF文件不存在: {pdf_path}")
            return False
        
        # 检查MinerU服务器健康状态
        print("🔍 检查MinerU服务器状态...")
        if not self.mineru_client.check_server_health():
            print(f"❌ 无法连接到MinerU服务器: {self.mineru_server}")
            print("请确保MinerU服务器正在运行")
            return False
        print("✅ MinerU服务器连接正常")
        
        # 创建或使用临时目录
        if temp_dir:
            temp_dir_path = Path(temp_dir)
            temp_dir_path.mkdir(parents=True, exist_ok=True)
            temp_dir_created = False
        else:
            temp_dir_path = Path(tempfile.mkdtemp(prefix="pdf_summarizer_"))
            temp_dir_created = True
        
        mineru_output_dir = temp_dir_path / "mineru_output"
        
        try:
            print(f"📁 临时目录: {temp_dir_path}")
            print("=" * 60)
            print("第一步: 使用MinerU解析PDF")
            print("=" * 60)
            
            # 第一步: 使用MinerU解析PDF
            success = self.mineru_client.parse_pdf(
                pdf_path=pdf_path,
                output_dir=str(mineru_output_dir),
                lang=mineru_lang,
                backend=mineru_backend,
                method=mineru_method,
                formula_enable=formula_enable,
                table_enable=table_enable,
                server_url=vlm_server_url
            )
            
            if not success:
                print("❌ MinerU解析失败")
                return False
            
            # 检查是否生成了full.md文件
            full_md_path = mineru_output_dir / "full.md"
            if not full_md_path.exists():
                print(f"❌ 错误: 未找到解析结果文件: {full_md_path}")
                print("请检查MinerU解析是否正常完成")
                return False
            
            print(f"✅ MinerU解析完成，生成文件: {full_md_path}")
            
            print("\n" + "=" * 60)
            print("第二步: 使用mineru-summarizer生成总结")
            print("=" * 60)
            
            # 第二步: 使用mineru-summarizer生成总结
            success = self._run_summarizer(
                input_dir=str(mineru_output_dir),
                output_path=output_path,
                compression=compression,
                enable_polish=enable_polish,
                config_path=config_path,
                backend=backend
            )
            
            if not success:
                print("❌ mineru-summarizer处理失败")
                return False
            
            print(f"✅ 总结完成，输出文件: {output_path}")
            
            # 显示文件大小对比
            self._show_size_comparison(pdf_path, full_md_path, output_path)
            
            return True
            
        finally:
            # 清理临时文件
            if not keep_temp and temp_dir_created:
                try:
                    shutil.rmtree(temp_dir_path)
                    print(f"🧹 已清理临时目录: {temp_dir_path}")
                except Exception as e:
                    print(f"⚠️ 清理临时目录失败: {e}")
            elif keep_temp:
                print(f"📁 临时文件保留在: {temp_dir_path}")
    
    def _run_summarizer(
        self,
        input_dir: str,
        output_path: str,
        compression: int,
        enable_polish: bool,
        config_path: Optional[str],
        backend: Optional[str]
    ) -> bool:
        """运行mineru-summarizer"""
        
        # 构建命令
        cmd = ["./mineru-summarizer", input_dir, output_path]
        
        # 添加压缩级别
        cmd.extend(["--compression", str(compression)])
        
        # 添加二次打磨
        if enable_polish:
            cmd.append("--polish")
        
        # 添加配置文件
        if config_path:
            cmd.extend(["--config", config_path])
        
        # 添加后端选择
        if backend:
            cmd.extend(["--backend", backend])
        
        print(f"🚀 运行命令: {' '.join(cmd)}")
        
        try:
            # 运行mineru-summarizer
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=os.getcwd()
            )
            
            # 输出运行结果
            if result.stdout:
                print("标准输出:")
                print(result.stdout)
            
            if result.stderr:
                print("错误输出:")
                print(result.stderr)
            
            if result.returncode == 0:
                print("✅ mineru-summarizer执行成功")
                return True
            else:
                print(f"❌ mineru-summarizer执行失败，退出码: {result.returncode}")
                return False
                
        except Exception as e:
            print(f"❌ 运行mineru-summarizer时出错: {e}")
            return False
    
    def _show_size_comparison(self, pdf_path: str, md_path: Path, summary_path: str):
        """显示文件大小对比"""
        print("\n📊 文件大小对比:")
        
        # PDF文件大小
        pdf_size = os.path.getsize(pdf_path)
        print(f"  📄 原始PDF: {self._format_size(pdf_size)}")
        
        # Markdown文件大小
        if md_path.exists():
            md_size = md_path.stat().st_size
            print(f"  📝 解析结果: {self._format_size(md_size)}")
        
        # 总结文件大小
        if os.path.exists(summary_path):
            summary_size = os.path.getsize(summary_path)
            print(f"  ✨ 最终总结: {self._format_size(summary_size)}")
    
    def _format_size(self, size_bytes: int) -> str:
        """格式化文件大小"""
        if size_bytes < 1024:
            return f"{size_bytes}B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f}KB"
        else:
            return f"{size_bytes / (1024 * 1024):.1f}MB"


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="PDF解析与总结完整流程",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 基本用法
  python parse_and_summarize.py document.pdf summary.md

  # 指定压缩级别和启用打磨
  python parse_and_summarize.py document.pdf summary.md --compression 30 --polish

  # 保留临时文件用于调试
  python parse_and_summarize.py document.pdf summary.md --keep-temp

  # 指定配置文件和后端
  python parse_and_summarize.py document.pdf summary.md --config config.yaml --backend claude_cli

  # 指定MinerU服务器和参数
  python parse_and_summarize.py document.pdf summary.md --mineru-server http://192.168.1.100:5000 --mineru-lang en

流程说明:
  1. 使用MinerU client解析PDF文件，生成markdown
  2. 使用mineru-summarizer对解析结果进行总结
  3. 输出最终的总结markdown文件
        """
    )
    
    # 必需参数
    parser.add_argument("pdf_path", help="输入PDF文件路径")
    parser.add_argument("output_path", help="输出总结文件路径")
    
    # mineru-summarizer参数
    parser.add_argument("--compression", "-c", type=int, default=50,
                       choices=[30, 50, 70, 100],
                       help="压缩级别 (30=精简, 50=标准, 70=详细, 100=翻译)")
    parser.add_argument("--polish", action="store_true",
                       help="启用二次打磨")
    parser.add_argument("--config", 
                       help="mineru-summarizer配置文件路径")
    parser.add_argument("--backend",
                       choices=["llm_api", "claude_cli"],
                       help="强制使用指定后端")
    
    # MinerU参数
    parser.add_argument("--mineru-server", default="http://localhost:5000",
                       help="MinerU服务器地址 (默认: http://localhost:5000)")
    parser.add_argument("--mineru-lang", default="ch",
                       choices=["ch", "en", "korean", "japan", "chinese_cht", "ta", "te", "ka"],
                       help="MinerU语言选项 (默认: ch)")
    parser.add_argument("--mineru-backend", default="pipeline",
                       choices=["pipeline", "vlm-transformers", "vlm-sglang-engine", "vlm-sglang-client"],
                       help="MinerU解析后端 (默认: pipeline)")
    parser.add_argument("--mineru-method", default="auto",
                       choices=["auto", "txt", "ocr"],
                       help="MinerU解析方法 (默认: auto)")
    parser.add_argument("--no-formula", action="store_true",
                       help="禁用公式解析")
    parser.add_argument("--no-table", action="store_true",
                       help="禁用表格解析")
    parser.add_argument("--vlm-server-url",
                       help="VLM服务器URL (当mineru-backend为vlm-sglang-client时需要)")
    
    # 调试参数
    parser.add_argument("--temp-dir",
                       help="指定临时目录路径")
    parser.add_argument("--keep-temp", action="store_true",
                       help="保留临时文件（用于调试）")
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("PDF解析与总结完整流程")
    print("=" * 80)
    print(f"📄 输入PDF: {args.pdf_path}")
    print(f"📝 输出文件: {args.output_path}")
    print(f"🎯 压缩级别: {args.compression}")
    print(f"✨ 二次打磨: {'启用' if args.polish else '禁用'}")
    print(f"🌐 MinerU服务器: {args.mineru_server}")
    print()
    
    # 创建处理器
    processor = PDFSummarizer(args.mineru_server)
    
    # 执行处理
    success = processor.process_pdf(
        pdf_path=args.pdf_path,
        output_path=args.output_path,
        compression=args.compression,
        enable_polish=args.polish,
        temp_dir=args.temp_dir,
        keep_temp=args.keep_temp,
        config_path=args.config,
        backend=args.backend,
        mineru_lang=args.mineru_lang,
        mineru_backend=args.mineru_backend,
        mineru_method=args.mineru_method,
        formula_enable=not args.no_formula,
        table_enable=not args.no_table,
        vlm_server_url=args.vlm_server_url
    )
    
    if success:
        print("\n🎉 PDF解析与总结完成！")
        print(f"📁 输出文件: {args.output_path}")
        sys.exit(0)
    else:
        print("\n💥 PDF解析与总结失败！")
        sys.exit(1)


if __name__ == "__main__":
    main()