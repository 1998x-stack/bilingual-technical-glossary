# MCP Server（MCP 服务器）

> AI Agents · 专题：MCP：模型上下文协议 · 截至 2026-11 的协议版本须区分 2025-11-25 与 2026-07-28

## 1. 核心定义

**MCP Server（MCP 服务器）**：MCP Server（MCP 服务器）是向 MCP Client 暴露工具、可读资源和提示模板等能力的服务端组件。它实现协议消息处理、能力声明、请求校验和资源访问控制，可能是本地 stdio 子进程或远程 Streamable HTTP 服务。

**适用边界：**MCP Server 不必包含 LLM，也不代表 API 的每个操作都是安全可调用的工具。2026-07-28 规范采用无会话核心，服务端处理请求应依据每次请求的版本、能力与授权；旧版可采用 initialize。

## 2. 形象理解

像一个标准化的服务柜台，提供业务目录、可查资料和办理接口，客户必须按流程出示权限并填写参数。

**类比的局限：**柜台有某项服务不意味着任何来访者都能办理，返回的文件也不一定是可信指令。

## 3. 技术原理与核心内容

服务端维护 tools/resources/prompts capability 集合，并响应 `tools/list`, `tools/call`, `resources/list`, `resources/read`, `prompts/list`, `prompts/get`。2026 版本需支持 server/discover 和每请求 `_meta`，根据认证 token 决定可见工具与资源集合。工具输入验证使用 inputSchema，输出支持结构化结果与错误区分；stdio 必须只向 stdout 发送协议消息，日志应进 stderr。

## 4. 工程实践与设计权衡

**工程案例：**一个内部 ERP Server 只暴露客户授权的查询工具与特定订单资源，调用写入工具时再次检查订单归属、参数和人工审批。即使 Host 已过滤，服务端仍承担真实业务授权与审计责任。

**失败模式与验证：**工具默认全量暴露、把 JSON Schema 当唯一安全边界、stdout 打印日志破坏 stdio framing、过时 list 缓存、无会话服务器依赖旧版私有状态。需按协议版本运行契约测试、未授权检索、输入边界值与并发执行验证。

## 5. 关联知识与易混辨析

MCP Server 是协议服务角色；MCP Tool 是可被列出/调用的函数；MCP Resource 是以 URI 标识的读取数据；MCP Prompt 是可选择模板，不能与业务 API 或大模型同义。

## 6. 中等难度面试题（含参考答案）

1. **问：MCP Server 能否仅靠 Client 提示词限制删除操作？** 答：不能，真实授权和业务前置条件必须由服务端验证，还要检查当前身份和审批。
2. **问：在 stdio Server 中 stdout 能输出调试日志吗？** 答：不能，stdout 是协议帧通道，日志应走 stderr，避免客户端解析错误。

## 7. 中等难度考试题（含解析）

1. **题：Server 暴露 8 个工具，但当前用户只有 3 个 scope 允许的工具，tools/list 应暴露多少？** 解：应只暴露当前授权许可的集合（题设为 3 个），执行时仍需再次授权检查。
2. **题：某 Server 仅支持 modern 请求，但调用方传 legacy initialize，应把它当现代版本有效请求吗？** 解：不能，须遵守对应版本生命周期或返回兼容性错误，而不是静默混用。

## 8. 权威来源与延伸阅读

- [MCP 2026-07-28 · Specification](https://modelcontextprotocol.io/specification/2026-07-28)：当前无会话协议核心与主机—客户端—服务器架构。
- [MCP · Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)：工具发现、调用和能力声明。
