# Timeout（超时）

> AI Agents · 专题：执行状态、持久化与恢复 · 时延、恢复和外部事务的真实边界

## 1. 核心定义

**Timeout（超时）**：Timeout（超时）是在等待工具调用、模型推断或任务执行超过预先设置的时间限额后，停止等待、触发取消或将状态标记为未知/失败的机制。它是保护资源与延迟的措施，不是对外部操作未发生的证明。

**适用边界：**连接超时、读取超时与总调用超时覆盖的阶段不同；硬中断进程是否能停止后端副作用取决于执行环境。对有副作用的操作，一旦出现 timeout，不能把 UNKNOWN 当作 FAILED 并立刻用新交易 ID 重试。

## 2. 形象理解

像电话响铃 30 秒无人接便挂机，但这并不能告诉你对方是否已经在后台处理了请求。

**类比的局限：**挂断电话不等于撤回刚刚发出的邮件，外部业务仍可能继续完成。

## 3. 技术原理与核心内容

设置 connect_timeout、read_timeout、total_timeout，并在调用栈传播剩余 deadline。客户端超时后记录 `{request_id,operation_id,elapsed,phase}` 与取消信号，异步任务通过 status/get 查询权威状态。服务端应在关键可取消节点检查 cancellation_token，限制线程/连接数，区分 timeout vs business_reject。对连续失败可使用退避或 circuit breaker，但不能忽略剩余预算。

## 4. 工程实践与设计权衡

**工程案例：**工单创建 Agent 规定工具调用 4 秒 timeout；API 第 4 秒断线，但后端可能完成。Agent 先使用 idempotency_key 查该工单是否存在，再决定提交后续通知，避免重复创建两张工单。

**失败模式与验证：**层级超时未统一造成上游先放弃而下游一直工作、误把网络超时记成功、耗尽线程池、重试大量非幂等工具。进行服务端慢响应、连接半开、失败回执和事务重复检测测试。

## 5. 关联知识与易混辨析

Timeout 是持续时间上限；Deadline 是绝对时间终点；Cancellation 是请求停止的行为；Retry Policy 决定超时后是否及如何再试。

## 6. 中等难度面试题（含参考答案）

1. **问：一次 RPC 超时意味着服务端未执行吗？** 答：不意味着，可能已执行但响应丢失，需要权威状态查询。
2. **问：为什么总超时与读取超时应分开？** 答：连接建立、读取响应和全链路预算是不同阶段，单一配置可能让某一步无限拖延整体。

## 7. 中等难度考试题（含解析）

1. **题：单次工具 timeout=5 秒，连续 3 次都在上限超时，忽略等待时间，累计工具等待上限？** 解：3×5=15 秒；实际还需受整体 deadline 约束。
2. **题：总体预算还剩 2 秒，但子工具配置 10 秒，合理请求时长上限？** 解：不超过剩余 2 秒，并扣除必要的结束/汇报开销。

## 8. 权威来源与延伸阅读

- [Amazon Builders' Library · Timeouts, retries, and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)：deadline 传递、随机抖动和重试放大。
- [AWS Step Functions · Error Handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)：任务超时、重试与 catch 状态转换。
