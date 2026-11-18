# Checkpoint（检查点）

> AI Agents · 专题：执行状态、持久化与恢复 · 跨 Agent 状态、授权与可靠执行的工程边界

## 1. 核心定义

**Checkpoint（检查点）**：Checkpoint（检查点）是 Agent 或工作流在某一执行时刻保存的状态快照，用于失败、中断或用户切换后恢复任务，而不必从头重新推理全部步骤。快照常包含任务 ID、状态值、已完成节点、输入版本及待验证外部动作。

**适用边界：**Checkpoint 不等于完整数据库备份，更不能自动撤销外部已发生的支付、通知或部署。单靠持久化模型对话文本不足以证明真实业务结果，应配合权限、事务 ID 与业务系统对账。

## 2. 形象理解

像游戏存档记录角色当前位置、道具与任务进度，重新载入可继续，但现实已发送的邮件不会因读档而消失。

**类比的局限：**存档可能不包含其他进程的最新事实，恢复后必须重新验证环境与资源版本。

## 3. 技术原理与核心内容

以 thread_id/task_id 绑定 checkpoint 的 state、next_nodes、tool_results、created_at 与 revision，持久化到可靠存储。LangGraph 的 checkpointer 可按线程维护图状态快照，允许 time travel/interrupt/resume 等能力；恢复时先验证 source_version、用户 ACL 和外部副作用 operation_id，再运行未完成节点。高风险写入采用幂等与事务对账，防止 checkpoint 写入前后崩溃造成重复执行。

## 4. 工程实践与设计权衡

**工程案例：**Agent 协助迁移 50 个数据表，第 27 个完成后节点中断。恢复时从 checkpoint 找到已确认成功的前 27 个，但必须从数据库 schema migration 表复核提交记录，不能因本地快照写着成功就重做或跳过。

**失败模式与验证：**状态快照与外部系统不一致、用户撤权后恢复仍可读取、存档未加密、并行分支 checkpoint 覆盖、恢复重放非幂等副作用。用在 checkpoint 前/后注入崩溃、版本变化与跨租户恢复测试。

## 5. 关联知识与易混辨析

Checkpoint 是单次状态保存；Checkpointing 是产生和维护快照的过程；Persistence 是存储不随进程消失；Durable Execution 组合恢复、幂等与后置条件，范围更大。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么恢复后仍需对账外部事务？** 答：快照与外部副作用不是原子提交，可能出现一边已成功另一边未记录的竞态。
2. **问：Checkpointing 和持久执行是否同义？** 答：不是，检查点只是机制之一，完整持久执行还包含恢复策略、重试、幂等和安全边界。

## 7. 中等难度考试题（含解析）

1. **题：共 50 个任务，27 个经权威系统确认完成，剩余多少？** 解：50−27=23 个。
2. **题：某操作在 checkpoint 前已提交成功，但 checkpoint 写入失败，重启后正确做法是什么？** 解：先按 operation_id 查询外部系统，确认后跳过重复写入并修复状态。

## 8. 权威来源与延伸阅读

- [LangGraph · Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)：线程检查点和执行恢复。
- [LangGraph · Durable Execution](https://docs.langchain.com/oss/python/langgraph/durable-execution)：幂等、副作用与任务恢复。
