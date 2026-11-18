# Streamable HTTP Transport（流式 HTTP 传输）

> AI Agents · 专题：MCP：模型上下文协议 · 以 2026-07-28 规范为当前基准，区分 legacy 模式

## 1. 核心定义

**Streamable HTTP Transport（流式 HTTP 传输）**：Streamable HTTP Transport（流式 HTTP 传输）把 MCP JSON-RPC 消息封装为面向单一端点的 HTTP POST，请求可以用普通 JSON 回复或返回仅属于该请求的 SSE 流。它定义网络封装而非工具业务逻辑。

**适用边界：**2026-07-28 无会话核心要求每请求提供 `_meta` 协议版本与能力，并要求按规范映射 `Mcp-Method`/`Mcp-Name` 等请求头；不应将旧版 `Mcp-Session-Id`、GET 长流、Last-Event-ID 恢复语义推广到新版。

## 2. 形象理解

像线上柜台收到一张申请单，可以一次给出结果，也可以在当前申请的响应流里分段提供进度。

**类比的局限：**连接被中断不等于银行业务失败，HTTP 200 也不等于真实付款到账。

## 3. 技术原理与核心内容

Client 向固定 MCP endpoint 发送 JSON-RPC POST；Server 验证 body、请求头与身份，返回 `application/json` 或 `text/event-stream`。SSE 只对应当前请求并传送协议响应/通知；现代客户端通过关闭当前响应流表达取消。网关可按头字段限流但不能替代 payload 校验。对未知结果的写操作使用 operation_id 或幂等键查询权威状态，不能换 RPC id 盲目重复执行。

## 4. 工程实践与设计权衡

**工程案例：**研发 Agent 通过远程 HTTP MCP Tool 扫描仓库，服务端以 SSE 返回阶段性进度。浏览器突然断开时，Agent 先查扫描/PR 的实际状态；存在 PR 时不再次创建，且凭用户当前授权才允许继续。

**失败模式与验证：**头/消息体声明不一致、代理缓存跨租户工具响应、HTTP 断流即报告失败、以旧版 GET 监听变更。用 Content-Type、header-body 一致性、取消与跨租户攻击测试。

## 5. 关联知识与易混辨析

Streamable HTTP 是传输；JSON-RPC 是消息格式；MCP Tool 是执行功能；A2A Streaming 另有任务协议与事件结构，两种 SSE 不可直接互换。

## 6. 中等难度面试题（含参考答案）

1. **问：新版 HTTP MCP 取消请求时的核心信号是什么？** 答：关闭对应响应流；不同于旧版通过 HTTP POST 通知 cancelled。
2. **问：HTTP 状态码成功就能认定业务提交成功吗？** 答：不能；要验证工具结果、后端事务记录与用户授权。

## 7. 中等难度考试题（含解析）

1. **题：三段响应流累计传送 20、30、50 KB 业务负载，总量？** 解：100 KB，忽略 framing。
2. **题：请求头 Mcp-Name 与 body 的实际工具名不一致，如何处理？** 解：应拒绝协议不一致请求，不能任意选择其一执行。

## 8. 权威来源与延伸阅读

- [MCP · Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)：stdio/HTTP 封装与取消。
- [MCP · Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)：HTTP POST、SSE 响应。
