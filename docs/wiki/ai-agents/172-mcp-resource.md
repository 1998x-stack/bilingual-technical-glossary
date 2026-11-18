# MCP Resource（MCP 资源）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；旧版行为应分别核对

## 1. 核心定义

**MCP Resource（MCP 资源）**：MCP Resource（MCP 资源）是 MCP Server 向客户端提供的、由 URI 唯一标识的可读上下文数据，例如文件内容、数据库 schema、知识条目或应用状态。Host 决定资源如何进入模型上下文；它不是一个可执行工具调用的同义词。

**适用边界：**资源的 URI 是标识符，不意味着允许任意网络读取。资源是否可见与可读取需要依当前用户权限审查；内容可能不可信或过期，不能因为来自 MCP Server 就提升为系统指令。

## 2. 形象理解

像图书馆目录中的一本技术手册，URI 对应书目编号，读者权限决定能否借阅。

**类比的局限：**知道图书编号并不等于能拿到书；读到一本旧手册也不意味着它是当前执行规范。

## 3. 技术原理与核心内容

服务器声明 resources capability 并响应 `resources/list` / `resources/read`；资源元数据可以包括 URI、name、description、mimeType，读取时返回 content。可支持模板化资源与订阅变更，具体功能以 capabilities 为准；2026-07-28 使用无会话请求和相应通知订阅模型，与 2025 旧版需要区分。资源正文作为低信任数据处理，并记录 source/version/expiry。

## 4. 工程实践与设计权衡

**工程案例：**数据库分析 Agent 读取 `schema://sales/orders` 资源了解列定义，生成只读 SQL 查询；即便资源文本含‘请执行 DROP TABLE’，也必须视为不可信数据而非授权。读取的 schema 版本需与真实数据库同步。

**失败模式与验证：**猜测 URI 绕过租户 ACL、缓存过期版本、资源 MIME 错判或模型把文档里的指令当控制命令。测试权限拒绝、URI 编码、列表/读取差异和文档更新后的缓存一致性。

## 5. 关联知识与易混辨析

MCP Resource 是可读取的上下文；MCP Tool 是执行动作/计算的接口；Prompt 是模板化输入；Resource URI 是资源的标识符而非资源实体本身。

## 6. 中等难度面试题（含参考答案）

1. **问：Resource URI 唯一是否自动意味着可以跨租户读取？** 答：不意味着。URI 只能定位，读取必须基于可信用户身份和服务器资源级授权。
2. **问：资源内容中出现‘忽略之前规则’时 Host 应如何处理？** 答：它属于低信任资料，不能覆盖上层指令或新增工具权限，应隔离并尽可能记录来源。

## 7. 中等难度考试题（含解析）

1. **题：资源列表共有 12 条，其中 5 条属于当前用户有权读取的范围，服务器应暴露多少？** 解：按有效授权返回 5 条或合法子集，且每次 resources/read 仍要再次验证。
2. **题：某 URI 从版本 3 更新到版本 4，但 Client 缓存仍返回 v3，可以据此执行破坏性迁移吗？** 解：不能，需重新确认最新 schema 与业务权限；旧缓存不是权威现状。

## 8. 权威来源与延伸阅读

- [MCP 2026-07-28 · Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources)：资源 URI 与读取方式。
- [IETF RFC 3986 · URI Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986)：URI scheme、authority、path 等标准语法。
