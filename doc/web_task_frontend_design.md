# MinerU Web 任务前端设计

## 概述
计划通过一个轻量化网页体验暴露现有的 `parse_and_summarize.py` 工作流。贡献者将交付一个单页上传界面，并配套 FastAPI 服务：负责保存用户上传的 PDF、调度总结任务、汇报任务进度，直到生成 Markdown 供用户下载。

## 目标
- 支持用户在浏览器上传 PDF，并基于现有流程产出 Markdown 总结。
- 提供可见的任务队列，实时展示状态并在完成后给出下载链接。
- 直接复用 `PDFSummarizer` 类，避免重写 CLI 逻辑。
- 默认部署在单机环境，无外部队列依赖，同时为未来扩展留出空间。

## 非目标
- 用户账号体系、登录鉴权或多租户隔离。
- 水平扩缩或分布式任务协调。
- 在线协同编辑生成的 Markdown。
- 修改 MinerU 或总结流程的核心行为。

## 架构概览
- **前端页面**：基于 FastAPI `Jinja2Templates` 与原生 JS 的单页应用，提供上传表单、任务表格及轮询功能。
- **API 服务**：FastAPI 应用，暴露任务创建、状态查询、结果下载等接口；PDF/Markdown 分别存放在 `var/uploads/`、`var/results/`。
- **任务存储**：使用 SQLite + `SQLModel/SQLAlchemy` 记录任务元数据、文件路径、状态、时间戳与错误信息。
- **执行器**：API 进程中的后台线程（或可选的独立 `python -m mineru.web_worker`）轮训 `PENDING` 任务，锁定后调用 `PDFSummarizer.process_pdf`，写回 `SUCCEEDED`/`FAILED` 状态。
- **配置体系**：服务启动时加载基础配置（参考 `mineru-config.yaml`），前端仅允许修改压缩比例。提交任务时将用户输入与基础配置合并，再调用总结流程。

## 数据模型
```
Task
  id: UUID 主键
  filename: 用户上传的原始文件名
  pdf_path: 本地 PDF 路径
  summary_path: 生成的 Markdown 路径（完成前为空）
  compression: 压缩比例（默认 50）
  polish: 是否启用二次打磨
  mineru_lang/backend/method: 与 CLI 对齐的参数（来源于基础配置）
  status: Enum(PENDING, RUNNING, SUCCEEDED, FAILED)
  created_at, started_at, finished_at: 时间戳
  error_message: 错误描述（可空）
```

## API 契约
- `POST /api/tasks`（multipart/form-data）：接收 `file` 与压缩参数（默认 50），返回任务 JSON。
- `GET /api/tasks`：返回最近任务列表及状态，用于首页表格。
- `GET /api/tasks/{task_id}`：获取单个任务详情，供前端轮询。
- `GET /api/tasks/{task_id}/download`：当 `status == SUCCEEDED` 时返回 Markdown。
- `GET /api/config`：提供压缩选项、默认配置摘要等表单元数据。

所有接口统一返回 JSON，包含 ISO 时间戳与状态字符串；错误响应使用 `{ "error": { "code": ..., "message": ... } }` 结构。

## 任务生命周期
1. 用户提交上传表单，浏览器向 `/api/tasks` 发起 POST。
2. API 保存 PDF 文件，写入一条 `PENDING` 记录，并立即返回任务元数据。
3. 前端每 5 秒轮询 `GET /api/tasks/{id}` 更新表格。
4. 执行器选择最早的 `PENDING` 任务，标记为 `RUNNING`，在独立临时目录中调用 `PDFSummarizer.process_pdf`。
5. 成功后，将生成的 Markdown 移动至 `var/results/{task_id}.md`，更新任务为 `SUCCEEDED` 并写入结果路径；失败时收集 stdout/stderr 写入 `error_message`，状态置为 `FAILED`。
6. 前端检测到状态变化。当任务成功时，展示下载按钮，指向 `/api/tasks/{id}/download`。任务默认长期保留，手动维护即可。

## 前端行为
- 上传前校验 MIME 类型为 `application/pdf`、检查文件大小。
- 任务表格展示文件名、压缩比例、状态标签、创建时间与耗时等字段。
- 任务进入终态（`SUCCEEDED`/`FAILED`）后自动停止轮询，可供用户手动刷新。
- 表单仅暴露压缩比例作为可调参数，其余 MinerU 设置沿用基础配置。
- 失败任务显示错误信息提示，并可通过 `POST /api/tasks/{id}/retry` 重新入队（可选增强）。

## 执行器细节
- 通过事务锁定任务（SQLite 使用立即事务模拟 `SELECT ... FOR UPDATE SKIP LOCKED`），防止并发执行同一任务。
- 依据任务记录与基础配置合并结果拼装参数，调用 `PDFSummarizer.process_pdf`，并将 stdout/stderr 写入 `var/logs/{task_id}.log`。
- `process_pdf` 已管理临时目录；执行器仅在 `DEBUG=1` 时设置 `keep_temp=True`。
- 完成后调整文件权限以便下载，清理临时文件，再提交事务释放锁。

## 配置与部署
- 新增 `mineru/web_config.yaml`，包含上传目录、结果目录、轮询间隔、最大并发、默认总结参数以及引用的基础 MinerU 配置路径。
- 启动时加载基础配置文件（默认 `mineru-config.yaml`），保存在内存中；任务请求时在基础配置副本上覆盖用户指定的压缩比例。
- `.env` 增补 `WEB_UPLOAD_DIR`、`WEB_RESULTS_DIR`、`WEB_POLL_INTERVAL`、`WEB_MAX_FILE_MB` 等键。
- 默认启动命令：`uvicorn mineru.web_app:app --reload`。执行器在 FastAPI 启动钩子中拉起；生产环境可通过 `python -m mineru.web_worker` 独立运行。

## 安全与可靠性
- 该 MVP 面向所有访问者，共用同一页面，不做登录鉴权。
- 强制文件大小上限（默认 50 MB），并对文件名做消毒处理。
- 上传与输出存储于仓库外部目录，统一使用 UUID 文件名避免冲突。
- 服务端再次校验 MIME 类型，拒绝非 PDF。
- 仅通过受控下载接口暴露成果文件；必要时可结合反向代理限制访问范围。
- 若执行器异常退出，任务保持在 `PENDING` 以便重试；可增加监控，超时未处理任务触发报警。

## 后续扩展方向
- 增加简单鉴权或访问保护（如基础密码、Token）。
- 提供任务自动过期与清理策略。
- 引入实时进度条或 websocket 推送。
- 打开更多 MinerU 配置项供高级用户定制。
