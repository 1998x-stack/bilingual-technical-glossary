# A2A Server（A2A 服务器）

> AI Agents · 专题：A2A：智能体间协议 · 以 A2A 最新正式规范为依据，和旧版消息模型须区分

## 1. 核心定义

**A2A Server（A2A 服务器）**：A2A Server（A2A 服务器）是对外提供 A2A 合规服务端接口的远程 Agent 或 Agent 系统，发布 Agent Card 让客户端发现其技能、输入输出格式和认证要求，并处理消息、任务和产物请求。

**适用边界：**A2A Server 不意味着单一 LLM 进程；背后可包含工作流、工具或多个 Worker。服务器执行真实副作用前须检验用户/客户端授权，不能仅凭 Agent Card 中说支持某项 Skill 就允许所有人使用。

## 2. 形象理解

像专业服务公司的统一收件与查询窗口：对外声明可办理哪些业务，内部如何分工可以保持不透明。

**类比的局限：**菜单写着‘报表生成’并不证明服务有真实数据源，也不代表请求者可以看所有客户的报表。

## 3. 技术原理与核心内容

服务端提供可发现的 Agent Card，按 selected AgentInterface 接收与解码请求，检查身份、租户和输入媒体类型。处理 SendMessage 时可以直接返回 Message 或创建 Task；对 Task 提供 GetTask、CancelTask、可声明的 streaming/push 通道。任务状态应绑定 id/contextId，Artifact 关联产出并可提供版本/来源，终态不能被随意继续写入消息。

## 4. 工程实践与设计权衡

**工程案例：**一个报表 Agent Server 支持 JSONRPC 和 HTTP+JSON 两种接口，Agent Card 按偏好排序并声明输入数据类型。客户端请求月报后服务端创建任务，扫描数据时严格按当前企业租户读取，完成后提供 PDF 和统计 JSON Artifact。

**失败模式与验证：**Agent Card 宣称不存在的能力、未检查实际媒体类型、跨租户 GetTask 泄漏、推送 webhook 可被滥用成 SSRF。进行完整认证、任务所有权和异常状态的协议一致性测试。

## 5. 关联知识与易混辨析

A2A Server 是远端 Agent 服务；MCP Server 主要提供工具、资源与提示；内部 Worker 或 LLM 不必直接面对 A2A 协议。

## 6. 中等难度面试题（含参考答案）

1. **问：A2A Server 返回 TASK_STATE_COMPLETED 是否能证明外部付款完成？** 答：不能，仍需支付账本的权威事务状态；协议任务终态与外部业务终态独立。
2. **问：为什么不能让任何人用猜到的 task ID 调用 GetTask？** 答：Task ID 是标识符不是认证凭据，必须做任务级资源授权。

## 7. 中等难度考试题（含解析）

1. **题：某 Server 受理 30 个任务，24 个完成、3 个失败、3 个工作中，已完成任务占比？** 解：24/30=80%，另外 6 个不能假称完成。
2. **题：Agent Card 声明不支持 streaming，客户端却强行请求流式操作，应如何处理？** 解：应拒绝不支持能力的操作或使用允许的降级方式。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：核心概念、操作与服务绑定。
- [A2A · Life of a Task](https://a2a-protocol.org/latest/topics/life-of-a-task/)：任务状态与异步生命周期。
