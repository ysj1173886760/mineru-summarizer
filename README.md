# MinerU内容总结器 - 统一版本

智能处理MinerU提取的学术论文内容，生成高质量中文总结的工具。

## ✨ 特性

- 🔍 **智能分章**: 基于Markdown header进行大章节分片，自动过滤无关内容
- 🔄 **多后端支持**: 支持LLM API和Claude CLI双后端，可随时切换
- 💾 **断点续传**: 检查点机制防止限流中断，支持会话恢复
- ✨ **二次打磨**: 可选的内容质量提升功能
- 🎯 **压缩灵活**: 30%/50%/70%三档压缩比例
- 🔤 **术语保护**: 自动保持专业技术名词的英文原文

## 🚀 快速开始

### 1. 生成配置文件

```bash
./mineru-summarizer --init-config
```

这会生成 `mineru-config.yaml` 配置模板，包含所有必要设置。

### 2. 编辑配置文件

根据需要修改配置：

```yaml
backend:
  type: claude_cli          # 或 llm_api
  model: gpt-4             # Claude CLI模型
  api_key: ${OPENAI_API_KEY}  # LLM API密钥（如使用）
  base_url: ${OPENAI_BASE_URL}
  temperature: 0.3
  max_tokens: 4000

processing:
  enable_checkpoint: true
  max_concurrent: 3
  max_tokens_per_chapter: 8000
  
polish:
  enabled: false           # 是否启用二次打磨
  temperature: 0.2
```

### 3. 基础使用

```bash
# 默认50%压缩比
./mineru-summarizer /path/to/mineru/output summary.md

# 指定压缩比和配置
./mineru-summarizer /path/to/mineru/output summary.md \
  --compression 30 \
  --config mineru-config.yaml

# 启用二次打磨
./mineru-summarizer /path/to/mineru/output summary.md \
  --polish
```

## 📖 详细用法

### 命令行参数

```
位置参数:
  input_dir             输入目录 (包含full.md)
  output_file           输出文件路径

可选参数:
  --compression, -c {30,50,70}    压缩级别 (30=精简, 50=标准, 70=详细)
  --polish                        启用二次打磨
  --config CONFIG                 配置文件路径
  --backend {llm_api,claude_cli}  强制使用指定后端
  --resume RESUME                 恢复指定会话ID
  --list-checkpoints              列出所有检查点
  --clean-checkpoints DAYS        清理N天前的检查点
  --init-config                   生成配置文件模板
  --validate                      验证配置和后端
```

### 使用场景

#### 📝 基础总结

```bash
# 使用默认设置
./mineru-summarizer paper_output summary.md

# 精简总结（30%压缩）
./mineru-summarizer paper_output summary.md -c 30

# 详细总结（70%压缩）
./mineru-summarizer paper_output summary.md -c 70
```

#### 🔄 后端切换

```bash
# 使用Claude CLI（推荐）
./mineru-summarizer paper_output summary.md --backend claude_cli

# 使用LLM API
./mineru-summarizer paper_output summary.md --backend llm_api
```

#### ✨ 高质量总结

```bash
# 启用二次打磨
./mineru-summarizer paper_output summary.md --polish

# 组合使用：详细总结 + 二次打磨
./mineru-summarizer paper_output summary.md -c 70 --polish
```

#### 💾 中断恢复

```bash
# 查看可恢复的会话
./mineru-summarizer --list-checkpoints

# 恢复指定会话
./mineru-summarizer --resume 7aade255bdbc

# 清理旧检查点
./mineru-summarizer --clean-checkpoints 7
```

#### 🔧 配置管理

```bash
# 验证配置
./mineru-summarizer --validate --config my-config.yaml

# 重新生成配置模板
./mineru-summarizer --init-config
```

## 📁 输入要求

输入目录应包含MinerU的提取结果：

```
input_dir/
├── full.md              # 必需：完整文档内容
├── content_list.json    # 可选：内容结构信息
├── layout.json          # 可选：布局信息
└── images/              # 可选：图片目录
```

## ⚙️ 配置详解

### 后端配置

#### Claude CLI后端（推荐）
```yaml
backend:
  type: claude_cli
  model: gpt-4            # 或 claude-3-5-sonnet-20241022
  temperature: 0.3
  max_tokens: 4000
```

#### LLM API后端
```yaml
backend:
  type: llm_api
  provider: openai        # openai/azure/anthropic等
  api_key: ${API_KEY}
  base_url: ${BASE_URL}
  model: gpt-4
  temperature: 0.3
```

### 处理配置

```yaml
processing:
  enable_checkpoint: true        # 启用检查点
  checkpoint_dir: .checkpoints   # 检查点目录
  max_concurrent: 3             # 并发数
  max_tokens_per_chapter: 8000  # 章节最大token数
```

### 输出配置

```yaml
output:
  format: markdown              # 输出格式
  language: zh-CN              # 输出语言
  include_toc: true            # 包含目录
```

## 🔍 压缩级别说明

- **30% (精简)**: 只保留最核心的创新点和结论
- **50% (标准)**: 平衡详细程度，包含主要观点和发现  
- **70% (详细)**: 保留详细内容，包含方法、实验和分析

## 🛠️ 故障排除

### 常见问题

1. **限流错误**
   ```bash
   ⏸️ 检测到限流错误，已保存检查点
   可以稍后运行以下命令恢复: ./mineru-summarizer --resume session_id
   ```
   解决：等待一段时间后使用 `--resume` 恢复

2. **配置错误**
   ```bash
   ./mineru-summarizer --validate --config your-config.yaml
   ```
   
3. **后端连接失败**
   - Claude CLI: 确保已安装并认证
   - LLM API: 检查API密钥和网络连接

### 调试模式

设置环境变量启用调试：
```bash
export DEBUG=1
./mineru-summarizer paper_output summary.md
```

## 📊 性能优化

- **并发设置**: 根据API限制调整 `max_concurrent`
- **章节大小**: 调整 `max_tokens_per_chapter` 平衡质量和速度
- **检查点**: 长文档建议启用 `enable_checkpoint`

## TODO(sheep):

- [] 删除无效代码，只保留mineru-summarizer的代码
- [] 不依赖mineru的输出格式，只使用md文件做切片+翻译
- [] 图片上传到oss中，并生成图片链接

## 🤝 贡献

欢迎提交Issues和Pull Requests来改进工具！

## 📄 许可证

MIT License
