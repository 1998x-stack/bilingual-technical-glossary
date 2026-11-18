# A2A Task（A2A 任务）

> AI Agents · 专题：A2A：智能体间协议 · 按 A2A 正式规范定义，不将旧版示例当作唯一序列化方式

## 1. 核心定义

**A2A Task（A2A 任务）**：A2A Task（A2A 任务）是具有唯一 ID、状态和可选 Artifact/消息历史的异步或多阶段工作单元，用于跟踪远端 Agent 的协作执行。它区别于一次即时 Message 回复，因为调用者可以在不同时间通过 id 查询状态及产物。

**适用边界：**并非每次 SendMessage 都会创建 Task；简单操作可以直接返回 Message。Task 状态到达 COMPLETED 仍应根据业务目标验证 Artifact 与外部系统，不能仅凭状态字符串推断支付、部署已成功。

## 2. 形象理解

像有唯一编号的维修工单，从提交、处理中、等待信息直到已完成，每个阶段可留记录并交付报告。

**类比的局限：**维修工单完成不证明某台机器已恢复生产，还要现场检查和客户验收。

## 3. 技术原理与核心内容

Task 至少有 `id`,`contextId`,`status`，可能包含 artifacts/history/metadata。Client 使用 SendMessage 创建或引用任务，随后 GetTask 或订阅状态流；状态可以进入 INPUT_REQUIRED 或 AUTH_REQUIRED 等等待态，并在新输入到来后继续。远程 Agent 需保证任务级 ACL，终态不可接受无限制的新工作消息，失败和取消要留下真实原因。

## 4. 工程实践与设计权衡

**工程案例：**调查报告 Agent 返回 task_id，客户会话结束后仍可查询任务。生成期间报告 WORKING，待用户补充日期时 INPUT_REQUIRED，完成后上传带文档 hash 和出处的 Artifact；上游实际审批仍另行验证。

**失败模式与验证：**任务 ID 被当公开凭证、历史消息与产物版本混用、重复创建工单、任务状态不一致、浏览器断线导致结果丢失。用断线轮询、任务所有权、同一请求重试和跨租户 IDOR 验收。

## 5. 关联知识与易混辨析

A2A Task 是可跟踪工作单元；A2A Message 是通信回合；Artifact 是任务产物；Task State 是瞬时状态值；Context ID 用于关联相关任务但不代替唯一 Task ID。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么客户端不能假设每个 SendMessage 都返回 Task？** 答：规范允许简单请求直接返回 Message；必须区分响应类型再决定是否轮询。
2. **问：为什么完成状态还要核验 Artifact？** 答：远端可能标错或返回过期结果，整体业务成功需具体可验证产物及来源支持。

## 7. 中等难度考试题（含解析）

1. **题：10 个 Task 中 6 个 COMPLETED、2 个 FAILED、2 个 WORKING，完成率？** 解：6/10=60%，WORKING 不算终态成功。
2. **题：两个相关任务同属一个 contextId，能因此认为有同一个 task id 吗？** 解：不能。Context ID 是对话/任务分组，Task ID 唯一标识任务。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Task、Message、Part 的规范结构。
- [A2A · Task Lifecycle](https://a2a-protocol.org/latest/topics/life-of-a-task/)：任务状态与补充消息。
