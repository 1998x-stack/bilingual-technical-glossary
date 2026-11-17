# Streaming Update（流式更新）

> AI Agents · 专题：A2A：智能体间协议 · A2A Task、Message 和 Artifact 的版本化语义

## 1. 核心定义

**Streaming Update（流式更新）**：Streaming Update（流式更新）是 A2A 在任务执行期间逐步发送当前 Task、状态变化和 Artifact 片段的机制，降低长任务等待的感知延迟。当前规范支持 Send Streaming Message 和 Subscribe to Task 等操作，事件可以通过受支持的网络绑定传送。

**适用边界：**流式传输不保证客户端在断线后收到所有历史状态消息；对最终事实和产物应使用 GetTask 补偿查询。流式需要 Agent Card 的 `capabilities.streaming` 支持，不可假定所有远程 Agent 都具备。

## 2. 形象理解

像观众实时查看赛事播报，知道比分变化，但断线后要到官方赛果页面补全最终成绩。

**类比的局限：**播报不代表最终签署成绩，每条增量消息也可能没有归档。

## 3. 技术原理与核心内容

服务先返回 Task 或单条 Message；Task 流中发送 `TaskStatusUpdateEvent` / `TaskArtifactUpdateEvent` 等包装事件，当前 `StreamResponse` 通过恰有一种 task/message/statusUpdate/artifactUpdate 字段区分。客户端按 taskId、artifactId、事件顺序更新视图；文件片段处理 append 标记，终态应关闭流。支持多客户端订阅时，相同任务的活动流应按生成顺序传播；重连后以 GetTask 获取最新完整状态。

## 4. 工程实践与设计权衡

**工程案例：**报告生成 Agent 流式返回‘数据整理、图表制作、PDF 输出’阶段，用户可以及时看到进度。断网重连后，UI 用 GetTask 取最终 Task 和 Artifact，而非根据最后看到的 70% 自认失败。

**失败模式与验证：**按消息到达顺序而非 taskId 合并、局部 chunk 丢失、在 stream 异常关闭后报告成功、在不支持 streaming 的 Agent 上强行调用。以断线/重连、两个并发订阅者、乱序及部分产物测试。

## 5. 关联知识与易混辨析

Streaming Update 是实时推送给保持连接的客户端；Push Notification 通过独立 webhook 异步通知；Polling 是反复 GetTask；三者具有不同连接与安全要求。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 streaming 断线后还需要 GetTask？** 答：规范不保证所有历史状态消息可从流中完整恢复，GetTask 返回当前权威状态与产物。
2. **问：一个不声明 streaming 的 Agent 是否必须支持 SendStreamingMessage？** 答：不是，客户端要先检查 Agent Card 的能力并选择其他受支持模式。

## 7. 中等难度考试题（含解析）

1. **题：任务一次返回 1 个 Task 事件、3 个状态事件、2 个产物更新，流中共多少事件？** 解：1+3+2=6 个。
2. **题：收到 `statusUpdate` 和 `artifactUpdate` 两个字段在同一个 StreamResponse 中，是否合法？** 解：不合法，当前响应包装是 OneOf，恰含一种。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Artifact、TaskState、事件与通知规则。
- [A2A · Streaming & Async Operations](https://a2a-protocol.org/latest/topics/streaming-and-async/)：轮询、SSE 流与异步任务。
