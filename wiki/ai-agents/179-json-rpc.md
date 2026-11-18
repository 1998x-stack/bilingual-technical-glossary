# JSON-RPC（JSON 远程过程调用）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；legacy initialize 行为按旧版单独说明

## 1. 核心定义

**JSON-RPC（JSON 远程过程调用）**：JSON-RPC 是一种基于 JSON 的轻量远程过程调用消息规范，使用 `jsonrpc`、`id`、`method`、`params` 和 `result/error` 等字段编码请求与响应。MCP 的基础消息采用 JSON-RPC 2.0，并额外规定版本化元数据、结果结构和可用消息模式。

**适用边界：**JSON-RPC 是消息级协议，不规定工具权限、业务动作安全或底层网络传输。MCP 2026 版在 JSON-RPC 之上增加 `_meta` 及结果 `resultType` 等具体约束；不能把裸 JSON-RPC 可用就等同完整 MCP 实现。

## 2. 形象理解

像统一格式的快递面单：包含编号、收件动作与参数，回复凭编号归还结果；它不保证包裹内容合法。

**类比的局限：**请求结构符合规范也不意味着服务器有权执行它，响应已送达也不证明业务完成。

## 3. 技术原理与核心内容

JSON-RPC Request 典型结构为 `{"jsonrpc":"2.0","id":7,"method":"tools/list","params":{}}`；Response 带相同 id 并且有 result 或 error。Notification 不带 id，通常不期待普通响应。MCP 2026 现代约定客户端向服务端发起请求、服务端回应，并采用 request-scoped 通知及 multi round-trip 回应额外输入，服务端不再主动发送 JSON-RPC requests。每个请求 `_meta` 必须携带版本/能力；结果对象需包含 `resultType`。

## 4. 工程实践与设计权衡

**工程案例：**Agent Host 同时发出两个 requests（id=7 查询工具、id=8 执行只读工具），id=8 先返回。Client 以 id 对应而非按时间顺序处理，检查 response.resultType 与工具业务字段，防止跨任务结果串线。

**失败模式与验证：**重复 id 匹配错误、把 notification 当 request、解析不完整 JSON、将 JSON-RPC error 与工具 isError 混淆、将旧版服务端主动请求逻辑套到 modern。用并发、取消、无效 ID 和格式拒绝测试。

## 5. 关联知识与易混辨析

JSON-RPC 定义 RPC 消息格式；MCP 基于它定义资源/工具能力和生命周期；stdio/Streamable HTTP 决定消息 framing 与传输；Tool Invocation 是方法 `tools/call` 的具体业务语义。

## 6. 中等难度面试题（含参考答案）

1. **问：JSON-RPC 的 id 为什么重要？** 答：它用于将并发回复准确关联原请求；响应到达顺序与请求发出顺序可能不同。
2. **问：现代 MCP 直接使用纯 JSON-RPC 2.0 消息就一定合规吗？** 答：不一定，还需满足 MCP 的请求 `_meta`、resultType、版本与方法/传输规则。

## 7. 中等难度考试题（含解析）

1. **题：同一 Client 同时发送 id=12、13、14，响应按 14、12、13 到达，是否应重新编号？** 解：不应，按各自 id 关联并处理。
2. **题：一条消息包含 method 但没有 id，按 JSON-RPC 概念应视为什么？** 解：通常是 Notification，不应等待普通请求响应，仍需按 MCP 允许的消息模式检查。

## 8. 权威来源与延伸阅读

- [MCP 2026-07-28 · Base Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic)：请求、响应、通知、ID 与 resultType。
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)：JSON-RPC request、response 和 error 的底层格式。
