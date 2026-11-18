# Resume Execution（恢复执行）

> AI Agents · 专题：执行状态、持久化与恢复 · 以真实运行状态、外部副作用对账和授权范围为工程边界

## 1. 核心定义

**Resume Execution（恢复执行）**：Resume Execution（恢复执行）是从持久化检查点或暂停状态取回任务，再以补充输入或已确认事件继续运行的过程。它重点解决如何安全地接续执行，而非简单重复之前的 prompt 或从头再请求全部工具。

**适用边界：**不同框架 API 各不相同：LangGraph 用 thread_id 加 `Command(resume=...)` 恢复动态中断；OpenAI Agents SDK 用序列化 `RunState` 在审批决定后调用 Runner 继续。它们都不替代业务资源授权。

## 2. 形象理解

像换班司机根据经过签署的行车日志、车辆实际位置和剩余路线继续驾驶，而不是重新开一辆车运同一货物。

**类比的局限：**行车日志可能延迟，恢复前仍要查看车辆当前真实位置和载货状态。

## 3. 技术原理与核心内容

算法可分为 `load state → authenticate actor → verify revision/TTL → reconcile external_operation_ids → validate resume payload → advance next step`。对有 side effects 的未决操作先查权威服务，用 idempotency_key 处理仍需重发的请求。恢复接口应该验证合法状态转换，拒绝终态任务再次接受新工作，所有决定记录 trace_id 和 reviewer_id；恢复失败时保留可再试状态而非无审计覆盖旧快照。

## 4. 工程实践与设计权衡

**工程案例：**审稿 Agent 审核 40 篇后等待专家对高风险公式确认，专家签核后以相同工作流 ID 恢复。程序检查文章当前 commit SHA 与签核绑定 SHA 相同，才把状态从 awaiting_review 推进到 publish_candidate；否则重新中断。

**失败模式与验证：**恢复误选另一个租户的 checkpoint、审批状态丢失、用过期模型输出覆盖当前资料、重复部署。用相同/不同 thread_id、并发恢复、重复决定和 schema 版本变化测试。

## 5. 关联知识与易混辨析

Resume Execution 是具体接续动作；Durable Execution 设计保证整个系统可恢复；Interrupt 主动暂停；Checkpointing 负责在暂停前保存可靠状态。

## 6. 中等难度面试题（含参考答案）

1. **问：恢复一个已支付订单为什么需要先查 payment_id？** 答：支付提交可能早于 checkpoint 成功，直接重复写入会产生双重付款。
2. **问：为什么 resume payload 必须验证任务版本？** 答：批准可能针对旧文件、旧金额或旧用户，变化后不可无条件沿用。

## 7. 中等难度考试题（含解析）

1. **题：完整流程 10 步，已核验完成 7 步，恢复需执行多少步？** 解：10−7=3 步，假设路径不变。
2. **题：同一工作流收到两个相同的恢复请求，如何避免双重执行？** 解：基于版本 CAS、任务锁和业务幂等键，第二个应返回当前状态而非再次提交。

## 8. 权威来源与延伸阅读

- [LangGraph · Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)：interrupt()、thread_id 和 Command(resume=...)。
- [OpenAI Agents SDK · Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)：RunState 持久化与审批后恢复。
