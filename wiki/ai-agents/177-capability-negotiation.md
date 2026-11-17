# Capability Negotiation（能力协商）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；legacy initialize 行为按旧版单独说明

## 1. 核心定义

**Capability Negotiation（能力协商）**：Capability Negotiation（能力协商）是 MCP 通信双方明确支持哪些协议功能、可选扩展和交互模式的过程。旧版在 initialize 阶段交换 capabilities；2026-07-28 现代规范把客户端能力放到每个请求元数据中，服务端在发现信息及响应中描述所支持能力。

**适用边界：****现代版不是沿用旧版握手**；可选的 server/discover 用于提前了解服务器能力和版本，但每请求都必须声明相关元数据。声明某 capability 不意味着调用者获得其下所有工具的资源权限。

## 2. 形象理解

像设备通信前双方核对支持的编解码器和功能清单，但功能支持不等于用户已经购买或获准使用。

**类比的局限：**双方都能传输文件不意味着可以访问任何用户的全部文件；功能兼容和资源授权是两层检查。

## 3. 技术原理与核心内容

旧版双方在 initialize Request/Result 中发送 protocolVersion、clientCapabilities/serverCapabilities；现代版客户端请求 `_meta` 包括 `io.modelcontextprotocol/protocolVersion`、`io.modelcontextprotocol/clientCapabilities` 等，并可调用 `server/discover` 获取服务端支持的能力及版本。可选扩展由 capabilities.extensions 显式协商，未声明的扩展不应假设可用。Server 仍需按请求凭证限制可见 tools/resources。

## 4. 工程实践与设计权衡

**工程案例：**Agent Host 想使用异步 Tasks 扩展，必须确认双方声明对应扩展；不支持时按普通工具调用能力降级或返回清晰错误。即使扩展可用，用户没有删除文档权限时仍应拒绝删除请求。

**失败模式与验证：**未协商扩展直接调用私有方法、用旧版 initialize 与只支持 2026 新版的服务器交互、将 tools capability 等同工具授权、列表缓存跨租户泄漏。测试不同版本能力矩阵、缺少扩展和权限边界。

## 5. 关联知识与易混辨析

Capability Negotiation 确定双方支持的功能集合；Protocol Version Negotiation 确定使用的语法与生命周期版本；Tool Listing 是在特定授权下列出具体工具；AuthZ 是独立执行权限核验。

## 6. 中等难度面试题（含参考答案）

1. **问：2026-07-28 版是否还要求先 initialize 才能协商能力？** 答：不要求；按请求传递版本和客户端能力，server/discover 可选预先发现。
2. **问：服务端声明 resources capability 就允许访问全部资源吗？** 答：不是，列表和读取仍按有效凭证、资源归属和访问策略过滤。

## 7. 中等难度考试题（含解析）

1. **题：客户端支持工具与资源两项功能，服务端只支持工具，双方可用公共功能集合？** 解：仅工具（intersection={tools}），不能假定资源能力可用。
2. **题：一个可选扩展只有 Server 声明、Client 未声明，可直接使用吗？** 解：不应，须按规范确认双方对扩展的支持。

## 8. 权威来源与延伸阅读

- [MCP 2026-07-28 · Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)：按请求版本、扩展与新版互操作。
- [MCP 2026-07-28 · Specification](https://modelcontextprotocol.io/specification/2026-07-28)：无会话基础协议和 JSON-RPC 2.0。
