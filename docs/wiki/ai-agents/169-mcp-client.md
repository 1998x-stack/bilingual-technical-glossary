# MCP Client（MCP 客户端）

> AI Agents · 专题：MCP：模型上下文协议 · 截至 2026-11 的协议版本须区分 2025-11-25 与 2026-07-28

## 1. 核心定义

**MCP Client（MCP 客户端）**：MCP Client（MCP 客户端）是 Host 内部与 MCP Server 使用协议交互的逻辑组件，负责请求编码、版本与能力处理、响应关联、传输和错误传播。客户端通常对应特定服务器或服务入口，但其具体数量和生命周期由 Host 实现决定。

**适用边界：**2025-11-25 的 Client 通常通过 initialize 建立有状态会话；2026-07-28 的现代协议是无会话、按请求携带元数据，不能把客户端的某个进程对象误认为协议强制存在的持久连接。

## 2. 形象理解

像办公室的网络打印客户端驱动，负责与打印服务按规范通信，而用户决定要打印什么，打印机服务决定能否执行。

**类比的局限：**驱动能发出正确格式的请求不代表用户对所有文档或打印机都有访问权。

## 3. 技术原理与核心内容

客户端接口可抽象 `request(method,params,meta,auth)->Result`，为每次请求生成唯一 id 并与响应 id 匹配。现代版可选先发 server/discover 决定版本，随后每个请求在 `_meta` 包含 protocolVersion 和 clientCapabilities，版本不匹配时按错误类型选择兼容版本；stdio 用换行 JSON-RPC，HTTP 按绑定规则发送。客户端应限制输出/超时、处理工具业务 isError 与 JSON-RPC 协议错误。

## 4. 工程实践与设计权衡

**工程案例：**AI 编辑器的 Client 查询 tools/list、resources/list，并按当前用户 token 调用只读查询工具。接到 HTTP 断连时记录请求 id 和未知业务状态，不能对有副作用的工具自动重发而不核实。

**失败模式与验证：**响应 id 复用造成并发错配、错误地用 initialize 与现代服务器交互、泄露 Bearer Token、将协议错误当业务成功。测试版本不匹配、乱序结果、取消、授权撤回及无法解析响应。

## 5. 关联知识与易混辨析

MCP Client 是协议通信组件；MCP Host 是包含模型和用户交互的应用；MCP Server 提供资源和工具；Session 在旧版连接生命周期里是协议概念，不能套用到新版请求模型。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么新版 MCP Client 不需要先发 initialize？** 答：2026-07-28 将协议版本/能力放进每个请求的元数据，可通过 server/discover 做可选发现，而不是建立会话握手。
2. **问：调用返回 JSON-RPC error 与 CallToolResult.isError 有何不同？** 答：前者反映协议/请求层异常；后者通常用于已到达工具但业务执行失败，Host 应分别处理。

## 7. 中等难度考试题（含解析）

1. **题：Client 发出 id=17 的 tools/list，请求同时还有 id=18 的 tools/call，18 先返回。能按返回顺序匹配吗？** 解：不能，必须按 JSON-RPC id 匹配各自请求。
2. **题：客户端偏好 2026-07-28，服务返回 UnsupportedProtocolVersionError 支持 2025-11-25，下一步？** 解：仅在客户端也实现旧版时选择兼容协议并走旧版握手；否则报告不兼容。

## 8. 权威来源与延伸阅读

- [MCP · Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)：按请求版本、server/discover 与旧版互操作。
- [MCP 2026-07-28 · Specification](https://modelcontextprotocol.io/specification/2026-07-28)：当前无会话协议核心与主机—客户端—服务器架构。
