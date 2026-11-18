# AI Agents · 第 11 批（201–220）学习路径 · 本轮先完成 201–210

> 该批仍以 canonical 20 条为单位。**已写作 201–210 的前 10 篇；211–220 保持 planned**，不计入已完成 Wiki。本文为内部审稿说明，不在面向读者的 GitHub Pages 展示编辑进度。

## 1. 从 Task 到 Artifact（201–208）

- **Artifact（201）**：Task 的实际输出，一个 Artifact 具有 artifactId 和至少一个 Part；Message 表示沟通，不应当成最终文件。
- **Task State（202）**：状态包括 SUBMITTED、WORKING、INPUT_REQUIRED、AUTH_REQUIRED、COMPLETED、FAILED、CANCELED、REJECTED 等，尤其要区分等待信息、等待授权与终态。
- **Task Lifecycle（203）**：先检查合法状态变更，再进行消息与产物对账。COMPLETED 是远程任务状态，不会自动证明银行/部署等外部业务成功。
- **Streaming Update（204）**：Send Streaming Message 与 Subscribe to Task 依赖 capabilities.streaming；断线后的状态完整性应通过 GetTask 补偿。
- **Push Notification（205）**：异步 webhook 按 task/event id 验证来源、重放/重复与任务归属，不能当作 exactly-once 业务消息队列。
- **Interoperability（206） / Capability Declaration（207）**：支持相同规范但语义不同的系统仍须核对任务、媒体类型、认证、版本与字段含义。
- **Task Delegation Protocol（208）**：此术语是任务委派契约的泛称；不能编造一个所谓 A2A 标准的 `tasks/delegate` RPC。当前 A2A 使用 SendMessage + Task + Artifact 形成协作。

## 2. 状态机与执行恢复（209–210）

- **State Machine**：有限状态集合、事件、转移函数与终态；实现要阻止失败旧事件覆盖真实完成状态、审批之前进入支付阶段等非法跳转。
- **Checkpoint**：保存某一时刻的状态快照以便恢复，但不能保证外部写事务和本地快照原子提交。重启后要根据 operation_id 查业务系统再决定继续哪个节点。

## 3. 贯穿案例：跨公司报告生成与状态恢复

一个订单数据审核 Agent 向远端 A2A 报表 Agent 发送任务。Remote Agent 在 WORKING 时发状态流，在 AUTH_REQUIRED 时请求真实凭证，得到许可后生成 PDF Artifact 并达到 COMPLETED。

上游仍要核验 Artifact 中订单号与合同版本；若服务端 webhooks 重复发送两次“完成”事件，客户端用 task_id 与事件 ID 去重，不应生成重复付款。上游工作流中断后通过 Checkpoint 恢复，但必须先查外部订单/付款状态，避免重放已有副作用。任务中的最终审计材料应绑定来源、hash 和执行器状态。

## 4. 中等面试题

**问：**为什么一个工作流的远程 A2A 任务 COMPLETED 和本地 checkpoint 均显示成功，仍不能证明款项已支付？

**参考答案：**两种记录都是执行系统的状态，可能与实际银行事务异步或不一致。支付成功必须由权威账本上的交易 ID、状态、金额、收款人和授权范围证明，必要时使用幂等键对账。

## 5. 中等考试题

**题：**生成 50 份报告，其中 27 份在权威文件系统核验存在，15 份正在生成，8 份失败。实际可验证完成率与尚未完成数各是多少？

**解：**完成率 27/50=54%，未完成 50−27=23 份（包括进行中 15、失败 8）。Checkpoint 不能凭状态自述把后 23 份变成成功。

## 6. 一手参考

- [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/)
- [A2A · Core Concepts](https://a2a-protocol.org/latest/topics/key-concepts/)
- [A2A · Life of a Task](https://a2a-protocol.org/latest/topics/life-of-a-task/)
- [A2A · Streaming and Asynchronous Operations](https://a2a-protocol.org/latest/topics/streaming-and-async/)
- [LangGraph · Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)
- [LangGraph · Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph · Durable Execution](https://docs.langchain.com/oss/python/langgraph/durable-execution)

## 7. 下次编辑范围与审稿

下一轮先补齐 **211–220**（Checkpointing、Persistence、Durable Execution 等），再进入第 12 批的 221–240。继续采用 20 条/批结构。专家审稿 pending，核对 A2A 正式状态名/字段、Webhook 幂等和快照恢复时外部副作用重放的安全边界。
