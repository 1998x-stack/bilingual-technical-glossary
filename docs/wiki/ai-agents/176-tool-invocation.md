# Tool Invocation (tools/call)（工具执行）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；legacy initialize 行为按旧版单独说明

## 1. 核心定义

**Tool Invocation (tools/call)（工具执行）**：Tool Invocation（工具执行，`tools/call`）是 MCP Client 向 MCP Server 请求执行某个已发现工具的标准方法，通常带工具名和参数对象；服务端验证请求和真实业务授权后执行，并返回内容、结构化结果或错误状态。

**适用边界：**调用 MCP Tool 并不意味着该工具一定无副作用，也不证明业务事务已完成。协议 RPC 成功、工具业务成功和最终用户目标成功是三层不同的状态；对付款/删除等动作必须另做权限与幂等保护。

## 2. 形象理解

像顾客填表并提交一个业务柜台请求，柜台接单和实际办理成功是两件不同的事。

**类比的局限：**表单格式正确不能证明付款已经到账；网络超时也不能证明此前一次转账未执行。

## 3. 技术原理与核心内容

典型 JSON-RPC 包含 `method:"tools/call"`、`params:{name,arguments}`、id；2026-07-28 额外要求每个请求的 `_meta` 带协议版本及能力信息。服务器对 JSON Schema、权限、参数语义与副作用进行独立检查；回执可包含 `content`, `structuredContent`, `isError`。如果业务未完成即返回 pending，应记录真实事务 ID，客户端不可将模型描述作为 final success。

## 4. 工程实践与设计权衡

**工程案例：**项目管理 Agent 调用 `create_issue`，后端根据当前仓库权限创建工单并返回 issue_id。若连接断开，先按 idempotency_key 或唯一业务字段查询是否创建过，避免一次用户请求生成两条重复工单。

**失败模式与验证：**把工具失败 isError 忽略、将 HTTP 200 视为到账、超时无差别重试、错用另一个 Server 的同名工具。通过真实写状态、重复请求和授权撤回的 E2E 验证。

## 5. 关联知识与易混辨析

Tool Listing（tools/list）只是发现工具；Tool Invocation（tools/call）真正请求执行；MCP Tool 是被调用的能力定义；Agent Action 可能通过其他协议或本地 API 实现，不限 MCP。

## 6. 中等难度面试题（含参考答案）

1. **问：工具调用返回 content 文本‘已完成’，但 isError=true，应怎样判断？** 答：工具明确标记错误，不能声称执行成功；应结合结构化状态和业务系统核验。
2. **问：网络断开后重新执行 tools/call 会有什么风险？** 答：上次写操作可能已提交，重发可能重复副作用；需服务端幂等或权威状态查询。

## 7. 中等难度考试题（含解析）

1. **题：题设工具先返回 HTTP 200，但业务 status=pending，是否已达到‘订单创建完成’？** 解：没有。传输成功不等于业务终态，须查订单 ID 对应的权威状态。
2. **题：Client 连续调用两个工具分别使用请求 id=10 和 11，11 先返回，如何对应结果？** 解：按 JSON-RPC id 对应，不按到达顺序。

## 8. 权威来源与延伸阅读

- [MCP 2026-07-28 · Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)：tools/call 消息、输入与结果错误。
- [MCP 2026-07-28 · Base Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic)：请求、响应、通知、ID 与 resultType。
