# MinerU内容总结器 - 统一版本

智能处理MinerU提取的学术论文内容，生成高质量中文总结的工具。

## ✨ 特性

- 🔍 **智能分章**: 基于Markdown header进行大章节分片，自动过滤无关内容
- 🔄 **多后端支持**: 支持LLM API和Claude CLI双后端，可随时切换
- 💾 **断点续传**: 检查点机制防止限流中断，支持会话恢复
- ✨ **二次打磨**: 可选的内容质量提升功能
- 🎯 **压缩灵活**: 30%/50%/70%三档压缩比例
- 🔤 **术语保护**: 自动保持专业技术名词的英文原文
- 🖼️ **图片上传**: 根据配置自动检测MD文件中的本地图片，上传到S3并替换为公网链接

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

output:
  upload_images: true      # 是否在总结后自动上传图片

s3:
  enabled: true            # 启用S3图片上传功能
  access_key_id: ${S3_ACCESS_KEY_ID}
  secret_access_key: ${S3_SECRET_ACCESS_KEY}
  bucket_name: ${S3_BUCKET_NAME}
  endpoint_url: ${S3_ENDPOINT_URL}  # 可选，支持自定义端点
  region_name: us-east-1
  path_prefix: images/
  public_url_template: https://your-domain.com/{bucket}/{key}
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

#### 🖼️ 图片上传

图片上传功能现在通过配置文件控制，在总结完成后自动执行：

```yaml
# 在配置文件中设置
output:
  upload_images: true    # 启用自动上传图片

s3:
  enabled: true          # 必须同时启用S3配置
  # ... S3其他配置
```

```bash
# 运行总结，会在结束后自动上传图片
./mineru-summarizer paper_output summary.md --config config.yaml
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
  upload_images: true          # 自动上传图片

s3:
  enabled: true                 # 启用S3图片上传功能
  access_key_id: your_key       # S3访问密钥
  secret_access_key: your_secret # S3密钥
  bucket_name: my-bucket        # S3存储桶名
  endpoint_url: https://s3.amazonaws.com  # 可选，自定义端点
  region_name: us-east-1        # 区域
  path_prefix: images/          # 存储路径前缀
  public_url_template: https://cdn.example.com/{bucket}/{key}  # 可选，自定义URL模板
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

## 🖼️ 图片上传功能详解

### 功能特点

- ✅ **自动集成**: 总结完成后根据配置自动上传图片
- ✅ **自动检测**: 识别MD文件中的本地图片引用（支持 `![](path)` 和 `<img src="path">` 格式）
- ✅ **智能跳过**: 自动跳过网络图片链接（http/https开头）
- ✅ **去重上传**: 基于文件内容哈希避免重复上传相同图片
- ✅ **批量处理**: 一次处理文件中的所有本地图片引用
- ✅ **安全配置**: 支持环境变量，避免敏感信息泄露

### 工作流程

1. **扫描文件**: 使用正则表达式查找所有图片引用
2. **过滤筛选**: 跳过网络链接，只处理本地路径
3. **路径解析**: 解析相对路径为绝对路径
4. **上传处理**: 
   - 生成基于内容哈希的唯一文件名
   - 检查S3中是否已存在（避免重复上传）
   - 上传文件并设置公共读权限
5. **链接替换**: 将本地路径替换为S3公网URL
6. **保存结果**: 将处理后的内容写入输出文件

### S3配置说明

#### 必需配置
- `enabled`: 必须设置为 `true`
- `access_key_id`: S3访问密钥ID
- `secret_access_key`: S3访问密钥
- `bucket_name`: S3存储桶名称

#### 可选配置
- `endpoint_url`: 自定义S3端点（支持其他S3兼容存储）
- `region_name`: 区域名称（默认: us-east-1）
- `path_prefix`: 存储路径前缀（默认: images/）
- `public_url_template`: 自定义URL模板，支持CDN等

#### 环境变量支持
```bash
export S3_ACCESS_KEY_ID="your_access_key"
export S3_SECRET_ACCESS_KEY="your_secret_key"
export S3_BUCKET_NAME="your_bucket"
export S3_ENDPOINT_URL="https://your-endpoint.com"
```

### 使用示例

#### 自动上传图片的总结流程

1. **设置配置文件**：
```yaml
output:
  upload_images: true    # 启用自动上传

s3:
  enabled: true
  # ... S3配置
```

2. **运行总结命令**：
```bash
./mineru-summarizer paper_output summary.md --config config.yaml
```

3. **自动处理图片**：
假设总结后的MD文件包含：
```markdown
# 文档标题

这里有一张图片：
![示例图片](./images/example.png)

还有HTML格式的图片：
<img src="../photos/chart.jpg" alt="图表" width="500">

网络图片会被跳过：
![网络图片](https://example.com/image.png)
```

图片上传后，本地路径会被自动替换为S3公网链接：
```markdown
# 文档标题

这里有一张图片：
![示例图片](https://your-domain.com/bucket/images/example_a1b2c3d4.png)

还有HTML格式的图片：
<img src="https://your-domain.com/bucket/images/chart_e5f6g7h8.jpg" alt="图表" width="500">

网络图片会被跳过：
![网络图片](https://example.com/image.png)
```

## TODO(sheep):

- [] 删除无效代码，只保留mineru-summarizer的代码
- [] 不依赖mineru的输出格式，只使用md文件做切片+翻译
- [x] 图片上传到oss中，并生成图片链接

## 🤝 贡献

欢迎提交Issues和Pull Requests来改进工具！

## 📄 许可证

MIT License
