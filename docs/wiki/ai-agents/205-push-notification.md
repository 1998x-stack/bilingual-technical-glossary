# Push Notification（推送通知）

> AI Agents · 专题：A2A：智能体间协议 · A2A Task、Message 和 Artifact 的版本化语义

## 1. 核心定义

**Push Notification（推送通知）**：Push Notification（推送通知）是 A2A Server 在任务状态/产物变化时，将通知通过 HTTP webhook 主动发送到 Client 提供的 endpoint，使客户端无须保持流连接或持续轮询。它适合长时后台任务，但需要明确的 webhook 鉴权与重放保护。

**适用边界：**Push Notification 是可选能力，必须由 Agent Card 的 `capabilities.pushNotifications` 声明；服务端不会因为某个客户端填了 URL 就无条件发送数据。Webhook 到达不意味着业务成功，可能重复、乱序或被第三方伪造。

## 2. 形象理解

像物流公司把包裹到站事件主动通知你的系统；短信只是提醒，不是拿到真实签收单。

**类比的局限：**虚假通知或重复短信会让系统误判，安全关键场景需到官方物流系统核对。

## 3. 技术原理与核心内容

Client 为 Task 创建 `TaskPushNotificationConfig`，其中有 webhook url、验证配置、taskId。Server 发生状态变化后发 HTTP POST，payload 使用符合当前协议的 `StreamResponse`（task/message/statusUpdate/artifactUpdate 之一）。接收端校验通知来源、任务归属、鉴权、时效与幂等去重，快速返回 2xx；若需要细节再调用 GetTask。Server 可重试投递，故不能依赖 exactly-once 通知。

## 4. 工程实践与设计权衡

**工程案例：**远端报告 Agent 生成 PDF 后向企业通知服务发送 webhook，接收端只用签名/凭据验证后入队，随后按 task ID 查询 Artifact，再给用户发通知。错误 webhook 不得造成自动支付或任意 URL 抓取。

**失败模式与验证：**客户端提供 SSRF 内网 URL、凭据泄漏、通知重复创建工单、单凭 payload 宣告交易成功、丢失 webhook 未补查。用拒绝鉴权、重复/重放、暂时宕机和终态对账测试。

## 5. 关联知识与易混辨析

Push Notification 是带独立 HTTP 回调的异步通知；Streaming Update 依赖活动连接；GetTask Polling 可在掉线时补偿；MCP 的 notifications/xxx 属另一个协议。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 webhook 接收端要做幂等？** 答：服务端可能因网络错误重复投递同一事件，不能把重复通知当重复业务动作。
2. **问：是否可以对任意用户提交的 webhook URL 发送包含敏感信息的通知？** 答：不能，需校验允许目标、授权、SSRF 与数据最小化。

## 7. 中等难度考试题（含解析）

1. **题：10 个不同任务各发送一次 webhook，网络重试重复发送 3 次，接收 13 次应识别多少唯一任务？** 解：10 个，按 task ID/事件 ID 去重。
2. **题：一个通知只写状态 WORKING，可以直接宣布报告完成吗？** 解：不能，仍需查询 Task 终态与 Artifact。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Artifact、TaskState、事件与通知规则。
- [A2A · Streaming & Async Operations](https://a2a-protocol.org/latest/topics/streaming-and-async/)：轮询、SSE 流与异步任务。
