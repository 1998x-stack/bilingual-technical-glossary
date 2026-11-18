# Task Lifecycle（任务生命周期）

> AI Agents · 专题：A2A：智能体间协议 · A2A Task、Message 和 Artifact 的版本化语义

## 1. 核心定义

**Task Lifecycle（任务生命周期）**：Task Lifecycle（任务生命周期）是 A2A Task 从受理、处理中、可能被中断、最终成功或终止的一系列合法状态转换及关联事件。设计生命周期需要同时考虑任务身份、补充消息、超时、取消、产物和外部事务一致性。

**适用边界：**A2A 的工作单元不是简单的 `queued→running→success` 三态模型；服务端可能直接回复 Message 而没有 Task，也可能在 INPUT_REQUIRED、AUTH_REQUIRED 等中断状态等待交互。Task 完成与外部业务提交仍须分别验收。

## 2. 形象理解

像一个研发需求从受理、开发、待补材料、测试到验收，出现外部审批时会暂停而非直接失败。

**类比的局限：**流程状态图完整不证明每个步骤真实执行，必须留工具日志、数据版本和审批证据。

## 3. 技术原理与核心内容

典型路径 `SUBMITTED→WORKING→COMPLETED`，也可能从 WORKING 转至 INPUT_REQUIRED/AUTH_REQUIRED 再恢复，或转 FAILED、CANCELED、REJECTED。客户端遵守 Task ID，使用 SendMessage 补充现存任务，GetTask 与流式事件获取状态；对终态避免重复提交原任务内容。Server 以持久任务记录保存状态、artifactIds、owner 和时间戳，对超时/未知外部写操作需再次对账。

## 4. 工程实践与设计权衡

**工程案例：**合同翻译远程 Agent 开始翻译时 WORKING，识别到目标语种不明确则 INPUT_REQUIRED；用户选择后恢复，生成 artifactId 指向最终译文并 COMPLETE。若此前已发出签署申请，不能因重新运行 Task 就重复提交签署。

**失败模式与验证：**结束后仍允许写入、断线导致无记录、重复请求创建两个 Task、乱序消息覆盖实际终态。设计状态转换表、故障注入和重试幂等验证。

## 5. 关联知识与易混辨析

Task Lifecycle 是状态变迁模型；Task State 是某时刻状态；Checkpoint 是本地恢复快照；A2A 协议只提供任务语义，执行器如何持久化和审计仍要自己实现。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 A2A 任务不一定总有 SUBMITTED 状态记录？** 答：简单操作可直接返回 Message 不建 Task；即使建了 Task，也可能很快进入后续状态。
2. **问：发生通信超时怎么确认任务有没有完成？** 答：保留 task ID，使用 GetTask/权威后端状态核验并防止副作用重放。

## 7. 中等难度考试题（含解析）

1. **题：任务经历 SUBMITTED→WORKING→INPUT_REQUIRED→WORKING→COMPLETED，共记录多少次状态值？** 解：5 个状态快照，状态转换为 4 次。
2. **题：任务在 FAILED 后收到旧的 WORKING 更新，是否应直接覆盖？** 解：不应，须核对事件版本和任务的权威终态。

## 8. 权威来源与延伸阅读

- [A2A · Life of a Task](https://a2a-protocol.org/latest/topics/life-of-a-task/)：多轮与终态规则。
- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Artifact、TaskState、事件与通知规则。
