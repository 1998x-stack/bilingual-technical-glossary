# MCP Tool（MCP 工具）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；旧版行为应分别核对

## 1. 核心定义

**MCP Tool（MCP 工具）**：MCP Tool（MCP 工具）是 MCP Server 公开的一种可由 AI 应用发现和调用的功能，通常代表查询、计算或对外部系统采取动作。工具由名称、描述和输入参数 schema 定义，并通过 `tools/list` 发现、`tools/call` 请求执行。

**适用边界：**Tool 不等于纯函数：某些工具会修改数据库、发送消息或支付。因此模型‘能看到’工具与当前用户‘获准执行’是两回事。工具列表按请求授权可能不同，输出内容也不能当作高优先级指令。

## 2. 形象理解

像银行柜台对外提供‘查余额’和‘转账’两个窗口，每个窗口有办理材料及权限要求。

**类比的局限：**柜台写着能转账并不意味着所有客户都能转任何账户；调用成功返回也可能需要进一步业务核验。

## 3. 技术原理与核心内容

Server 声明 tools capability，工具描述含 name、description、inputSchema，可选 outputSchema 等。Client 通过 tools/list 获取元数据，调用时用 `tools/call` 传 `{name,arguments}`。现代 2026 规范所有请求还需 `_meta` 协议信息。Server 对参数做 schema 与业务校验，调用结果可带 content/structuredContent，业务失败用 isError，JSON-RPC error 区分协议级失败。

## 4. 工程实践与设计权衡

**工程案例：**订单 Agent 仅能查本人订单；tools/list 按用户凭证暴露查询工具。若执行‘取消订单’，应校验订单 owner、状态、确认与幂等；即使模型生成合法 JSON，也不能绕过业务授权。

**失败模式与验证：**输入 schema 合法但越权、工具描述中的数据提示注入、业务失败被解释为成功、重复写操作、同名工具路由错误。用越权、边界值、部分提交、模型恶意输出与版本兼容集成测试。

## 5. 关联知识与易混辨析

MCP Tool 是可执行能力；MCP Resource 是以 URI 命名的可读资料；MCP Prompt 是可复用模板；Tool Invocation 是一次具体调用事件。

## 6. 中等难度面试题（含参考答案）

1. **问：inputSchema 校验通过是否可以自动执行删库工具？** 答：不能；执行层仍需身份、资源归属、业务条件、用户批准以及后置审计。
2. **问：isError 与 JSON-RPC error 如何区分？** 答：前者通常是工具已经运行但业务失败；后者描述协议层或方法调用层失败，客户端应分别处理。

## 7. 中等难度考试题（含解析）

1. **题：一个 Server 定义 10 个 Tool，当前用户只授权其中 4 个，tools/list 应返回全部吗？** 解：不应，基于当前 token/scopes 返回适当可见集合；题设是 4 个。
2. **题：创建订单 tools/call 超时，但 Server 可能已提交，是否可换新的请求 ID 直接重试？** 解：不能只凭超时认定未执行；要查业务订单 ID 或使用可靠服务端幂等键。

## 8. 权威来源与延伸阅读

- [MCP 2026-07-28 · Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)：工具 schema、列表发现与调用语义。
- [MCP 2026-07-28 · Specification](https://modelcontextprotocol.io/specification/2026-07-28)：工具、资源、提示的协议定位。
