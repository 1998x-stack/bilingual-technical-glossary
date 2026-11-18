# AI Agents · 第 10 批（181–200）综合学习与审稿路径

> 本文件是内部编写/审稿路线，源词条编号唯一以 [AI Agents 332 条词表](../../glossaries/ai-agents.md) 为准。公众 GitHub Pages 使用统一 Wiki Explorer 直接打开具体术语页，不展示批次状态。

## 1. MCP 2026：传输、输入与安全（181–190）

- **Streamable HTTP Transport**：当前 2026-07-28 规范请求使用每次 HTTP POST + 可选请求范围 SSE，淘汰旧版长 GET stream 与协议会话；头/体版本一致性和 Origin 检查不可省略。
- **Sampling / Roots**：从 2026-07-28 起均为 deprecated，最低保留一年兼容窗口。Sampling 优先迁移到模型提供方 API，Roots 优先用显式工具参数/Resource URI/Server 配置；Roots 从来不是沙箱。
- **Elicitation**：继续作为用户输入征询，通过新版 MRTR 的 `resultType: input_required` 与 `inputResponses` 形成多轮流程。敏感凭据必须使用可信 URL 模式，而不是普通表单，Host 应允许用户拒绝与取消。
- **Completion / Progress**：`completion/complete` 补全 Prompt/Resource 参数；`notifications/progress` 依 progressToken 关联活动请求。通知的进度不是外部事务成功证据。
- **Cancellation**：新版 HTTP 关闭请求对应 SSE 响应流；stdio 发送 `notifications/cancelled`。长时 Tasks 扩展的 `tasks/cancel` 又属于不同接口，取消并不保证所有副作用回滚。
- **Authorization / MCP Extension / MCP Apps**：HTTP OAuth 资源服务器需验证 issuer/audience/scope 与资源对象权限。扩展显式协商，MCP Apps 通过 ui:// 资源在受限 iframe 中呈现；UI 内点击按钮仍需 Host/Server 真实授权。

## 2. A2A：发现、能力与消息（191–200）

- **A2A** 是不同 Agent 之间的协作协议；**MCP** 连接 AI 应用与外部工具、资源和提示，两者不等同。
- **A2A Client / Server / Remote Agent**：客户端根据 Agent Card 的 `supportedInterfaces` 选择自己支持的绑定、版本和 URL；服务端可由多 Agent 组成，不一定是一个 LLM。
- **Agent Card / Discovery / Skill**：通过 well-known、Registry 或私有配置发现；卡片只展示能力而不自动授信。Skill 的 id/name/tags/examples 是描述，不是工具授权。
- **Task / Message / Part**：SendMessage 可以直接返回 Message，也可能创建可按 ID 跟踪的 Task。Message 是交流回合，不保证全部保留在 history；Part 在当前版本使用 `text/raw/url/data` 恰选一项，不要套旧版 `kind` 字段。

## 3. 贯穿工程案例：多 Agent 文档审核

用户要求研发 Agent 将合同附件交给财务专家核验。
1. Host 先通过 MCP 的受限只读 Tool 获取有权访问的合同版本，并检查来源与 ACL。
2. Host 对请求中的敏感字段使用最小披露。若缺司法辖区，由 Elicitation 经用户确认补充；绝不通过普通表单索要 API Key。
3. 上游 A2A Client 从经过验证的 Agent Card 选择符合法律审查技能与媒体类型的 Agent。
4. 将任务以 Message/Part 交给 Remote Agent，获取 Task ID 和 current State；查询实际 Artifact 后才进行整体业务验收。
5. 如工具或 A2A 网络超时，先核对真实外部事务和 Task 是否存在，再决定是否重试，不重复创建订单/付款。
6. 对所有已完成、未确认、拒绝和待人工审批事项分别报告，不能把模型的 natural-language done 当专业签核。

## 4. 中等面试题

**问：**为什么 MCP Apps 的 ui:// 资源与 A2A Agent Card 都不能作为授权凭据？

**参考答案：**二者分别是界面资源标识和远程能力描述。用户身份、资源 ACL、可执行动作、实际订单参数与审批需要由 Host/Server 的独立安全机制校验；远程数据的提示词不可以升级为系统指令。

## 5. 中等考试题

**题：**Agent Card 宣告 5 项能力，但客户端仅支持其中 3 项，当前用户获准使用其中 2 项，其中 1 项当下不可用。最多有多少项可执行？

**解：**最多 1 项；技术能力交集、身份权限和运行时可用性必须逐层过滤，不能把五项卡片声明等同为可调用权限。

## 6. 主要原始资料

- [MCP · 2026 Specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP · Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- [MCP · Sampling/Roots 的弃用说明](https://py.sdk.modelcontextprotocol.io/deprecated/)
- [MCP · Elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)
- [MCP · Cancellation](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation)
- [MCP · Progress](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress)
- [MCP Apps · 官方扩展](https://apps.extensions.modelcontextprotocol.io/)
- [A2A · 最新正式规范](https://a2a-protocol.org/latest/specification/)
- [A2A · Agent Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/)

## 7. 人工审稿

逐项核验协议状态、来源及版本，特别是 Sampling/Roots deprecated、MRTR、表单 vs URL 模式、取消的传输差异、A2A Part 序列化和 Agent Card 安全性。所有候审稿状态保持 pending，不能将结构校验等同独立领域专家认证。
