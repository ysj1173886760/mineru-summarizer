# 使用说明

## 快速开始

### 1. 设置API密钥

编辑 `.env` 文件，添加你的API密钥：

```bash
# 使用OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# 或使用Anthropic Claude  
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### 2. 运行测试

确保基础功能正常：

```bash
python test_basic.py
```

### 3. 生成总结

```bash
# 基本用法 - 50%压缩级别
python cli.py summarize ../GFM_SURVEY

# 指定压缩级别和输出文件
python cli.py summarize ../GFM_SURVEY --compression 30 --output summary_30.md

# 查看MinerU数据信息
python cli.py info ../GFM_SURVEY
```

## 压缩级别说明

- **100%**: 完整翻译，保留所有细节
- **70%**: 详细总结，保留主要论点和技术细节  
- **50%**: 标准总结，重点关注核心观点
- **30%**: 简洁总结，只包含重要创新点
- **15%**: 极简总结，1-2句话概括

## 常用命令

```bash
# 使用Claude模型
python cli.py summarize ../GFM_SURVEY --provider anthropic --model claude-3-haiku-20240307

# 不包含图片，生成目录
python cli.py summarize ../GFM_SURVEY --no-images --compression 30

# 调整并发数和分块大小
python cli.py summarize ../GFM_SURVEY --max-concurrent 5 --chunk-size 4000

# 详细输出
python cli.py summarize ../GFM_SURVEY --verbose
```

## 故障排除

1. **API密钥错误**: 检查`.env`文件中的密钥设置
2. **输入目录错误**: 确保目录包含`*_content_list.json`和`full.md`
3. **网络问题**: 检查网络连接，可能需要设置代理
4. **内存不足**: 减少`--max-concurrent`参数

## 输出示例

生成的markdown文件包含：
- 文档标题和生成信息
- 自动生成的目录
- 按原始结构组织的中文总结
- 处理统计信息

输出文件保存为markdown格式，可以用任何markdown编辑器查看。