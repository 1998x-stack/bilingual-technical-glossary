# Checkpointing（检查点保存）

> AI Agents · 专题：执行状态、持久化与恢复 · 以真实运行状态、外部副作用对账和授权范围为工程边界

## 1. 核心定义

**Checkpointing（检查点保存）**：Checkpointing（检查点保存）是 Agent 运行时在步骤完成、状态变更或指定间隔，把可恢复的执行快照写入存储的过程。区别于单个 Checkpoint 对象，它还包括写入频率、隔离粒度、存储耐久性、版本清理和恢复验证策略。

**适用边界：**保存了某个步骤的模型状态，并不意味着外部数据库付款与本地快照已经原子提交。快照可以在节点边界或事件触发，但重放非幂等步骤必须先查外部操作 ID，不能把本地记录当交易事实。

## 2. 形象理解

像长时间编译每完成一个可验收阶段便存一个还原点，断电后可以从最近安全阶段继续，而不是重新编译全部文件。

**类比的局限：**断电前写到外部仓库的文件不会随本地存档回滚，且存档本身可能损坏或过期。

## 3. 技术原理与核心内容

设 checkpoint C_k={thread_id,graph_state,next_nodes,revision,completed_ids,external_operation_ids,created_at}。选择每个 super-step 写入，或在关键 gate 前写入；持久化层应保证快照与版本索引原子更新，采用 optimistic version/compare-and-swap 避免并行进度互盖。恢复读取最近已确认的 snapshot 后，根据业务系统记录核实外部副作用并只重试未提交的动作。LangGraph checkpointer 按 thread_id 记录图状态，而跨线程知识应进入 Store，不能把二者混同。

## 4. 工程实践与设计权衡

**工程案例：**迁移 60 张表的 Agent 每完成 10 张存一个 checkpoint，至第 35 张服务器故障。恢复时从已保存的第 30 张继续核对迁移台账，再验证 31–35 是否已提交；不应直接对这 5 张重复执行 DDL。

**失败模式与验证：**写入前崩溃造成漏记、多个分支同时写同一 revision、损坏快照导致无法恢复、把线程 ID 当授权令牌。用断电位置随机故障注入、快照 checksum 与资源 ACL 验收。

## 5. 关联知识与易混辨析

Checkpointing 是持续生产快照的机制；Checkpoint 是某个时点的记录；Persistence 是存储能力；Durable Execution 还包括副作用处理、重试和恢复策略。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么更频繁 checkpoint 不一定更好？** 答：可缩短重新执行窗口，但增加持久化 I/O、存储成本和并发写竞争，应按工作价值与恢复目标调整。
2. **问：恢复后为什么还要查数据库迁移记录？** 答：外部 DDL 可能执行成功而本地快照未写入，必须根据真实 schema/version 对账才能避免双重执行。

## 7. 中等难度考试题（含解析）

1. **题：50 个任务每 10 个存档一次，完成第 37 个时故障，最近完整存档对应第几个？** 解：第 30 个，至多需要核实第 31–37 的外部状态。
2. **题：一次快照存储耗时 0.2 秒，写入 20 次，合计同步持久化耗时？** 解：20×0.2=4 秒，假设顺序、无重叠。

## 8. 权威来源与延伸阅读

- [LangGraph · Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)：thread-scoped checkpoint 与跨线程 store 区别。
- [LangGraph · Checkpointer vs Store](https://docs.langchain.com/oss/python/langgraph/persistence#checkpointer-vs-store)：短期状态快照与长期数据存储。
