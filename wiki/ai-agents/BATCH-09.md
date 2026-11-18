# AI Agents · 第 9 批（161–180）学习路径与审稿规范

> 权威源词表：[AI Agents 332 条](../../glossaries/ai-agents.md)。本页仅供内部编辑与专家审阅；公众 Wiki 通过统一 Explorer 路由到具体术语页面，不应显示批次规划。

## 一、协作基础设施与冲突（161–166）

**Message Bus → Consensus → Conflict Resolution → Role Specialization → Handoff Record → Coordination Failure**。

- Message Bus 定义消息传递，不保证外部写入端到端 exactly-once。message_id、task_id、correlation_id 各自有不同责任。
- 应用层多 Agent 投票与分布式复制算法中的严格一致性协议并不相同；多数意见更不能绕过强制安全/权限 gate。
- 处理事实冲突要对齐对象、环境、时间、数据版本与权威来源；处理并发写冲突要使用 CAS/事务等控制。
- Handoff Record 只有在接收者 ACK 并确认有效任务上下文后才代表一次可靠交接，不意味着交接的业务事项已经完成。
- Coordination Failure 可能发生在所有 Worker 单独都输出 success 的情况下，需按全局任务状态与真实业务结果诊断。

## 二、MCP 角色、发现与调用（167–176）

**MCP Host → MCP Client → MCP Server** 是三个职责：Host 管理面向用户的应用与多个 Client；Client 按约定版本发送 RPC；Server 暴露工具、资源与提示模板。

- MCP Tool：`tools/list` 发现，`tools/call` 执行；输入 JSON Schema 不等于执行授权。
- MCP Resource：`resources/list` 与 `resources/read`，通过 URI 识别可读数据，URI 不是认证凭证。
- MCP Prompt：`prompts/list` 与 `prompts/get` 产生模板化消息，不自动拥有系统指令优先级。
- Resource URI：需遵守 URI 语法、服务端对象级 ACL、路径规范化和来源记录。
- Tool Invocation：JSON-RPC 成功 / Tool isError / 业务后置条件是三个不同的状态层次。

## 三、MCP 2025 与 2026 协议的关键差异（177–180）

**不要把旧版协议的 initialize 会话生命周期写成所有 MCP 版本都必须执行的步骤。**

| 项目 | Legacy：2025-11-25 及更早 | Modern：2026-07-28 |
|---|---|---|
| 通信生命周期 | `initialize` + `notifications/initialized` 握手 | 无会话核心；不需要 `initialize` |
| 版本 | 会话启动时协商/记录 | 每条请求以 `_meta.io.modelcontextprotocol/protocolVersion` 声明 |
| 能力 | 初始化阶段交换 capabilities | 每请求附客户端能力；服务器提供 `server/discover` |
| 发现 | 从初始化结果获知服务能力 | 服务端必须实现 `server/discover`；客户端可选主动调用 |
| 无法支持的版本 | 按旧版握手规则拒绝或选择兼容版本 | `UnsupportedProtocolVersionError`，可包含受支持版本列表 |
| 服务器主动请求 | 旧版支持特定 server→client RPC | 新版改为 Multi Round-Trip Requests 等请求范围内交互 |
| stdio | newline-delimited JSON-RPC，日志 stderr | 相同 framing，**但请求元数据和生命周期不同** |

- 现代的每请求 `_meta` 中必须包含协议版本与客户端能力；不能用裸 JSON-RPC 例子误导为完整 MCP 请求。
- tools/list 可分页，按当前认证 scope 返回工具集合；按现代规范结果应支持受控缓存与确定性排序。
- stdio 子进程的 stdout 只能输出 MCP 规范消息，调试信息应该写 stderr。传输层不负责业务权限。
- 按用户/租户身份限制工具和资源，对敏感动作要求明确确认、服务端真实授权和审计。消息中的工具输出永远不能提升为上层系统指令。

## 综合案例：IDE 的本地 MCP 工具与多 Agent 协作

任务：用户要求检查仓库并提交经确认的代码修改。Host 管理 Git MCP Client 和代码索引 MCP Client；两个 Server 提供不同工具与资源。

1. 对 2026 版服务可先 `server/discover`，或直接以合规 `_meta` 发请求；对仅支持 2025 版的服务应走 `initialize` 握手。
2. 用 `tools/list` 与 `resources/list` 获取当前允许的能力和资料。仓库代码段作为低信任数据，不可改变安全规则。
3. Manager 分派 Worker 只读分析并保留 task_id；Reviewer 按实际 git revision 查验证据；协调器按结果版本进行汇合。
4. 如果修改需要写入，Host 再检查用户意图、目标文件权限与审批。执行器以工具调用 ID 和业务文件版本审计。
5. 工具超时后不要假设写入失败；必须查询 Git 状态、文件哈希或 commit SHA，避免重复提交。
6. 最终报告区分代码修改真实状态、CI 结果、专业审稿 pending 与模型建议，不把 Agent 自评当作独立审核。

## 中等面试题（综合）

**问：**为什么一个客户端在 2025 与 2026 两个 MCP Server 上可发现相同工具名，但不能复用完全相同的初始化流程？

**参考答案：**工具名是能力层标识；协议版本决定会话和消息元数据。2025-11-25 的服务采用 initialize 握手，2026-07-28 的服务无会话并要求每条请求携带协议版本、能力，可能用 server/discover 提前发现。还需按 server_id/工具名做命名空间隔离和独立授权。

## 中等考试题（综合）

**题：**Host 收到 12 条 Worker 回执，涉及 10 个不同任务 ID，其中 2 条重复。业务 gate 要求全部 10 个任务成功；虽然有 10 个不同 ID，但一个任务状态为 unknown，能否提交部署？

**解：**不能。回执按 task_id 去重得到 10 个任务，仅覆盖率达到 100%；业务成功要求所有任务经外部检查为成功。unknown 必须对账或补证，部署 gate 保持 pending。

## 主要权威资料

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP Specification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)
- [MCP Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [MCP Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources)
- [MCP stdio transport](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)
- [AutoGen（多 Agent 协作论文）](https://arxiv.org/abs/2308.08155)
- [OpenAI Agents SDK · Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)

## 独立审稿清单

1. 核实所有 MCP 方法、字段名及版本差异是否对应所引规范。
2. 对比工具/资源/提示权限与来源，查有无错误地将检索数据视作系统指令。
3. 检查所有面试/考试题答案的公式、边界条件及数字。
4. 审查真实服务端授权、幂等与重试设计，不因模型文字声明成功就跳过验证。
5. 专家审稿必须有真实 reviewer 身份、日期与正文 SHA256；当前所有 161–180 条仍为 `pending`。
