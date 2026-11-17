# Tool Listing (tools/list)（工具列表）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；旧版行为应分别核对

## 1. 核心定义

**Tool Listing (tools/list)（工具列表）**：Tool Listing（工具列表，`tools/list`）是 MCP Client 向 Server 请求当前授权下可用工具元数据的标准方法，用于模型/Host 发现有哪些功能、各自描述和参数 schema。它是发现操作，而不是自动执行工具。

**适用边界：**工具列表可能为空，并可因授权范围或配置变化而不同；2026-07-28 规范不允许它仅作为连接状态副作用任意变化。支持分页和缓存策略时客户端必须正确跟随 cursor 与过期规则，不能只读首页就当全量。

## 2. 形象理解

像银行网站根据客户身份显示可用功能菜单，但显示某项菜单并不意味着此次转账已获批准。

**类比的局限：**菜单可能缓存过期，实际业务授权仍要在执行请求时核对。

## 3. 技术原理与核心内容

JSON-RPC 请求 `{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{"cursor":"..."}}`。Server 声明 tools capability，并返回工具集合，工具项包含 name/inputSchema 等元数据及可选字段；协议版本 2026 要求请求 `_meta` 带版本和能力，即示例的完整请求需要补充元数据。列表按请求的认证 scope 过滤，并使用 deterministic ordering 便于缓存；工具变化通过相应变更通知/订阅机制处理。

## 4. 工程实践与设计权衡

**工程案例：**IDE 有两个 MCP Server，一个负责仓库，一个负责工单。Host 将各自 tools/list 结果加服务命名空间，用户撤回仓库访问权限后重新发现，只显示合法工具；不能靠旧缓存调用过期删除接口。

**失败模式与验证：**分页丢条目、缓存跨租户泄漏工具列表、重复名称导致路由误选、将工具说明文字中的恶意指令放进高权限提示。用不同 token、多个 cursor、列表变更和同名服务测试。

## 5. 关联知识与易混辨析

Tool Listing 是查询能力清单；Tool Invocation 执行选中的具体方法；Capability Negotiation 声明双方支持哪类协议能力；Resource Listing 列出可读资源而非可执行函数。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 tools/list 不能直接作为当前操作授权？** 答：列表仅表示可能可用的能力，执行仍须检查当前身份、资源归属、参数及敏感动作批准。
2. **问：2026 版本中的 tools/list 结果能否根据同一连接之前调用过什么而任意变化？** 答：规范禁止这种纯连接状态副作用；可以因每次请求携带的授权 scope 和真实配置变化而变化。

## 7. 中等难度考试题（含解析）

1. **题：某列表分页共三页，每页分别 5、5、2 个工具，完整数量？** 解：5+5+2=12 个，不可只读首页就认为共 5 个。
2. **题：相同工具名出现在两个不同 Server，Host 应如何识别？** 解：以 server_id+tool_name 复合标识或显式命名空间路由，避免误调用。

## 8. 权威来源与延伸阅读

- [MCP 2026-07-28 · Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)：工具 schema、列表发现与调用语义。
- [MCP · Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)：按请求版本、能力声明与互操作。
