# Durable Execution（持久执行）

> AI Agents · 专题：执行状态、持久化与恢复 · 以真实运行状态、外部副作用对账和授权范围为工程边界

## 1. 核心定义

**Durable Execution（持久执行）**：Durable Execution（持久执行）是系统在服务重启、网络中断、临时错误或等待人工审批后，仍能依据已提交状态继续未完成任务的执行模式。它依赖持久化，但还必须协调外部副作用、幂等、重试边界、工作所有权和最终状态验证。

**适用边界：**持久执行不是 exactly-once 的魔法保证。跨多个 API 的支付/发信/数据库修改往往没有统一事务；如果工具成功但运行器未记录成功，恢复必须先查询后端 operation_id 再决定是否重放。

## 2. 形象理解

像物流长途运输的接力记录，司机换班后接着运输已在途的货物，而不是从出发地再发一件同样的包裹。

**类比的局限：**运输进度记录不意味着货物状态没有变化，换班时仍要核对车辆、封签和当前所在地点。

## 3. 技术原理与核心内容

使用 durable state `{run_id,step_id,status,revision,tool_call_id,operation_id,deadline}` 和可恢复队列。执行前持久保存 intent 与幂等键，工具写入后提交成功证据，再标记步骤完成；崩溃恢复检查未决 intent 的外部真实状态。将不可重放副作用独立包装为任务节点，用 workflow version 和状态迁移规则处理部署后代码升级。中断需要统一 resume token/线程标识，但该标识不应当作免鉴权通行证。

## 4. 工程实践与设计权衡

**工程案例：**采购 Agent 创建支付请求后网络断开。重启从存储恢复到 pending_payment，先查询支付网关的 payment_id；如果已成功，则继续生成收据；若确认为未提交且仍有授权，才用相同 idempotency_key 安全重试。

**失败模式与验证：**无限重试导致双付款、保存状态的版本不兼容、Agent 恢复后原审批已过期、重放已发送邮件。做崩溃于调用前/调用中/调用后、网络分区和授权变更的端到端演练。

## 5. 关联知识与易混辨析

Durable Execution 是正确继续执行的整体保障；Persistence 保证数据不随进程丢失；Checkpointing 管理快照；Resume Execution 是某一次重新启动未完成任务的动作。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么能恢复上下文的 Agent 不一定具有持久执行能力？** 答：上下文记忆不能保证副作用已提交状态、任务幂等和失败处理，一恢复就重放写操作可能造成事故。
2. **问：哪个操作必须优先保证 idempotency_key？** 答：会产生真实副作用而网络回执不可靠的写操作，尤其支付、创建订单、发送通知。

## 7. 中等难度考试题（含解析）

1. **题：流程 8 步，前 5 步经后端核实完成，恢复后最多还有几步需要完成？** 解：8−5=3 步，前提没有新增依赖。
2. **题：一个转账请求超时后查询到 payment_id 为 succeeded，可否再创建同金额转账？** 解：不可，应该复用已完成事务结果并继续后续流程。

## 8. 权威来源与延伸阅读

- [LangGraph · Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)：thread-scoped checkpoint 与跨线程 store 区别。
- [AWS Step Functions · Standard vs Express](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html)：工作流持久性、执行历史与重试差别。
