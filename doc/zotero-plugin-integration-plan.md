# Zotero插件集成方案

## 项目概述

将mineru-summarizer集成到Zotero插件中，实现对导入PDF文档的智能解析和总结功能。用户可以通过手动触发的方式对选中的PDF文档进行处理。

## 技术架构

### 1. 插件开发框架

**选择方案：Bootstrap Plugin (Zotero 7)**
- 开发模板：`windingwind/zotero-plugin-template`
- 开发语言：TypeScript + JavaScript
- 架构特点：
  - 无需重启Zotero即可加载/卸载插件
  - 支持现代化开发工具链
  - 提供热重载和调试功能
  - 兼容Zotero 7的新架构

### 2. 核心集成策略

**A. 事件监听机制**
```javascript
// 注册事件监听器
const notifierCallback = {
  notify: async (event, type, ids, extraData) => {
    // 仅用于状态监控，不自动触发处理
    if (type === 'item' && event === 'add') {
      // 可选：记录新导入的PDF以便后续处理
    }
  }
};

Zotero.Notifier.registerObserver(notifierCallback, ['item']);
```

**B. 外部工具调用**
```javascript
// 调用mineru-summarizer
async function triggerParseAndSummarize(item) {
  const pdfPath = item.getFilePath();
  const outputPath = generateOutputPath(item);
  
  // 使用Zotero内置API执行Python脚本
  await Zotero.Utilities.Internal.exec('python', [
    '/path/to/mineru-summarizer/parse_and_summarize.py',
    '--input', pdfPath,
    '--output', outputPath,
    '--config', '/path/to/mineru-config.yaml'
  ]);
  
  // 将生成的总结附加到Zotero条目
  await attachSummaryToItem(item, outputPath);
}
```

## 用户交互设计

### 1. 手动触发方式

**A. 右键菜单集成**
```javascript
const menuItem = {
  id: "mineru-parse-summarize",
  label: "Parse and Summarize with MinerU",
  onCommand: async (event) => {
    const selectedItems = ZoteroPane.getSelectedItems();
    await handleParseAndSummarize(selectedItems);
  },
  // 仅在选中PDF或文章时显示
  condition: () => {
    const items = ZoteroPane.getSelectedItems();
    return items.some(item => 
      item.isPDFAttachment() || 
      item.getField('itemType') === 'journalArticle'
    );
  }
};
```

**B. 工具栏按钮**
- 位置：Zotero主工具栏
- 功能：处理当前选中的PDF文档
- 图标：自定义MinerU图标

**C. 菜单栏选项**
- 位置：Tools菜单
- 标签："Parse with MinerU..."
- 功能：打开批量处理对话框

**D. 快捷键支持**
- 快捷键：Ctrl+Shift+M (Windows/Linux) / Cmd+Shift+M (Mac)
- 功能：对选中项目执行解析和总结

### 2. 用户界面元素

**进度显示**
```javascript
function showProgressWindow(totalItems) {
  const progressWin = new Zotero.ProgressWindow();
  progressWin.changeHeadline("MinerU Processing");
  progressWin.show();
  
  return {
    updateProgress: (current, message) => {
      progressWin.addDescription(`${current}/${totalItems}: ${message}`);
      progressWin.updateProgress(current, totalItems);
    },
    close: () => progressWin.startCloseTimer(2000)
  };
}
```

**批量处理对话框**
- 选择处理选项
- 覆盖现有总结的选项
- 进度指示和取消功能

## 文件管理策略

### 1. 存储方案

**输出文件存储**
```javascript
function generateOutputPath(item) {
  const attachmentDir = Zotero.Attachments.getStorageDirectory(item);
  return OS.Path.join(attachmentDir.path, 'mineru-summary.md');
}
```

**支持格式**
- 主要格式：Markdown (.md)
- 备选格式：纯文本 (.txt)、JSON (.json)

**文件关联**
- 总结文件作为子附件存储到对应的Zotero条目
- 自动添加标签标识已处理的文档

### 2. 配置管理

**插件设置面板**
```javascript
const settings = {
  mineruPath: '/path/to/mineru-summarizer',
  configPath: '/path/to/mineru-config.yaml',
  outputFormat: 'markdown',
  autoTag: true,
  tagName: 'mineru-processed',
  overwriteExisting: false
};
```

## 开发实施计划

### Phase 1: 基础框架搭建
1. **环境设置**
   - 克隆zotero-plugin-template
   - 配置TypeScript开发环境
   - 设置调试和热重载

2. **基础结构**
   - 实现插件生命周期管理
   - 添加基本的事件监听器
   - 创建配置管理系统

### Phase 2: 核心功能实现
1. **文件处理**
   - 实现PDF文件检测和路径获取
   - 集成外部命令执行功能
   - 处理mineru-summarizer输出结果

2. **Zotero集成**
   - 将总结文件附加到条目
   - 实现自动标签添加
   - 处理重复处理的情况

### Phase 3: 用户界面开发
1. **交互元素**
   - 实现右键菜单选项
   - 添加工具栏按钮
   - 创建菜单栏选项

2. **用户反馈**
   - 实现进度指示器
   - 添加错误提示和处理
   - 创建批量处理对话框

### Phase 4: 优化和测试
1. **性能优化**
   - 异步处理防止UI阻塞
   - 队列管理避免并发过多
   - 缓存机制避免重复处理

2. **错误处理**
   - 依赖检查（Python、mineru-summarizer）
   - 文件权限验证
   - 网络连接和超时处理

3. **测试验证**
   - 单元测试和集成测试
   - 多平台兼容性测试
   - 用户体验测试

## 技术要点

### 1. 依赖管理
- **系统要求**：Python 3.8+
- **依赖检查**：启动时验证mineru-summarizer可用性
- **安装指导**：提供依赖安装和配置说明

### 2. 错误处理机制
```javascript
async function processItem(item) {
  try {
    // 验证文件存在
    if (!await OS.File.exists(pdfPath)) {
      throw new Error('PDF file not found');
    }
    
    // 执行处理
    await executeMineru(item);
    
  } catch (error) {
    Zotero.logError(`Processing failed: ${error.message}`);
    // 用户友好的错误提示
    Zotero.alert(null, "MinerU Error", `Failed to process: ${error.message}`);
  }
}
```

### 3. 性能考虑
- **异步处理**：使用Promise和async/await
- **队列管理**：限制并发处理数量
- **内存管理**：及时释放大文件资源
- **缓存策略**：避免重复处理相同文档

## 部署和分发

### 1. 插件打包
- 使用template提供的构建脚本
- 生成.xpi安装文件
- 包含必要的依赖和配置文件

### 2. 安装说明
1. 下载插件.xpi文件
2. 在Zotero中选择Tools > Add-ons
3. 点击齿轮图标 > Install Add-on From File
4. 选择.xpi文件并安装
5. 重启Zotero完成安装

### 3. 配置指导
1. 安装Python和required dependencies
2. 配置mineru-summarizer路径
3. 设置API keys（如需要）
4. 测试插件功能

## 维护和更新

### 1. 版本管理
- 遵循语义化版本控制
- 提供更新日志和兼容性说明
- 支持自动更新检查

### 2. 用户支持
- 提供详细的使用文档
- 创建问题反馈渠道
- 定期更新和bug修复

---

## 附录

### A. 相关资源
- [Zotero Plugin Template](https://github.com/windingwind/zotero-plugin-template)
- [Zotero Plugin Development Documentation](https://www.zotero.org/support/dev/client_coding/plugin_development)
- [Zotero 7 Developer Guide](https://forums.zotero.org/discussion/105825/how-to-develop-a-zotero-7-plugin)

### B. 示例配置文件
参考项目根目录的`mineru-config.yaml`进行插件配置管理。

---

*文档创建日期：2025-08-24*  
*版本：v1.0*  
*状态：方案设计完成*