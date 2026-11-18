# Protocol Version Negotiation（协议版本协商）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；legacy initialize 行为按旧版单独说明

## 1. 核心定义

**Protocol Version Negotiation（协议版本协商）**：Protocol Version Negotiation（协议版本协商）是 MCP Client 与 Server 确定共同支持的协议版本和对应通信规则的兼容过程。MCP 当前存在两种生命周期：2025-11-25 及更早版本使用 initialize 会话握手，2026-07-28 新版使用每请求版本声明且不再要求握手。

**适用边界：**2026-07-28 版本严格意义上**没有单独的版本协商握手**：客户端可先通过 server/discover 查询支持版本，也可以发出带期望版本的请求并处理不支持版本的错误。旧版由 initialize 中确定会话版本，不能直接混用。

## 2. 形象理解

像两台设备约定共同能理解的通信标准；旧设备需要开机时一次握手，新设备则每封请求表明采用哪个标准。

**类比的局限：**双方都说支持同一版本，不等于身份可信、工具有授权或网络传输不会故障。

## 3. 技术原理与核心内容

在 modern 模式中，每个请求 `_meta.io.modelcontextprotocol/protocolVersion` 明确标注版本；如果 Server 不支持，应返回 UnsupportedProtocolVersionError（规范示例错误码 -32022），在 data.supported 中列出可支持版本，Client 再选择其也实现的版本重试。server/discover 必须由现代 Server 支持，但客户端不必先调用。旧版初始化时如果对方返回不同版本，客户端需检查本身是否支持才继续。

## 4. 工程实践与设计权衡

**工程案例：**IDE 接入两种 MCP Server，其中 A 支持 2026-07-28，B 仅支持 2025-11-25。Host 的 Client 适配层选择 A 的无会话 `_meta` 路径与 B 的 initialize 握手路径，各自单独验证 capabilities、凭证和调用状态。

**失败模式与验证：**把 initialize 的 serverInfo 当现代版必需结构、把新版每请求元数据遗漏、版本错误后无限盲重试、将协商兼容误认为已获授权。构建现代/旧版/未知版本矩阵与互操作契约测试。

## 5. 关联知识与易混辨析

Protocol Version Negotiation 确定消息格式和生命周期；Capability Negotiation 确定扩展与功能；Session State 是应用工作流状态而不是现代 MCP 的协议会话。

## 6. 中等难度面试题（含参考答案）

1. **问：MCP 2026-07-28 的 server/discover 是否是每个 Client 调用其它方法前的强制握手？** 答：不是；现代服务器必须实现 discovery，但客户端可以直接发合规请求，再处理不支持版本错误。
2. **问：服务器返回支持 2025-11-25，客户端只实现 2026-07-28，该怎么办？** 答：没有互相支持的版本，应报告不兼容而非假装旧版能运行。

## 7. 中等难度考试题（含解析）

1. **题：客户端版本集合 {2025-11-25,2026-07-28}，服务端只支持 2025-11-25，可选版本是什么？** 解：只能选择 2025-11-25，并按 legacy initialize 生命周期通信。
2. **题：Client 发 2026-07-28，Server 不支持；正确错误码示例是多少？** 解：-32022，且应在错误数据中列出支持版本供兼容处理。

## 8. 权威来源与延伸阅读

- [MCP 2026-07-28 · Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)：按请求版本、扩展与新版互操作。
- [MCP 2025-11-25 · Specification](https://modelcontextprotocol.io/specification/2025-11-25)：initialize 会话握手的旧版行为。
