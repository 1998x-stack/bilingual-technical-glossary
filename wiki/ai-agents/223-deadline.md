# Deadline（截止期限）

> AI Agents · 专题：执行状态、持久化与恢复 · 时延、恢复和外部事务的真实边界

## 1. 核心定义

**Deadline（截止期限）**：Deadline（截止期限）是某个任务必须停止、返回或达到可验收状态的绝对时间点，常用单调时钟下的剩余时间预算传播到每个下游调用。与单次 Timeout 不同，它约束完整工作流的总时长。

**适用边界：**Deadline 到期并不自动取消已经产生的外部副作用或表明业务失败；对于人工审批和长任务，可能需要异步延续/升级策略。系统墙钟可能跳变，计算剩余时长应尽量使用单调时钟，并考虑跨服务时钟偏移。

## 2. 形象理解

像机场登机截止时间：办理、安检和行李托运每一步都必须在剩余时间内安排，而不能每一步重新获得完整的一小时。

**类比的局限：**登机门关闭不意味着此前托运行李自动撤回，仍需处理滞留的业务状态。

## 3. 技术原理与核心内容

令截止时刻 D，当前单调时间 now，剩余预算 `remaining=max(0,D−now)`。调用下游前为序列化、网络和最终回报预留 margin，设置 `child_timeout=min(configured_timeout,remaining−margin)`；若为非正立即 fail-fast。重试策略每次计算新 remaining，不应每次都重置全局 Deadline。跟踪任务 start/deadline/owner 并提供超时升级或 async Task 返回。

## 4. 工程实践与设计权衡

**工程案例：**报告 Agent 用户要求 30 秒内初步给出结论，检索耗费 12 秒、模型处理 10 秒后仅余 8 秒；剩余深度审阅任务应在 8 秒约束内返回 partial 和来源，或按用户授权改为异步，而非继续无界处理。

**失败模式与验证：**每层都重置 30 秒导致 end-to-end 变成几分钟、墙钟调整造成负等待、剩余时间不足时仍启动大模型。用逐层预算传递、时钟漂移、取消和队列等待场景验收。

## 5. 关联知识与易混辨析

Deadline 是绝对完成边界；Timeout 限制某次操作；Retry Budget 限制再试；SLA 是服务目标/承诺，可能包含多个统计指标。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么在重试时不能每次重新给 30 秒总预算？** 答：会突破原先的端到端截止时间，产生不可预测尾延迟和资源占用。
2. **问：如果某子步骤剩余预算已经为零应怎么办？** 答：不要再启动新昂贵操作，应停止并返回明确的 partial/timeout 状态或走异步升级。

## 7. 中等难度考试题（含解析）

1. **题：总 deadline 距开始 30 秒，已运行 12+10 秒，还剩多少？** 解：30−12−10=8 秒。
2. **题：当前剩余 6 秒，必须预留 1 秒汇报，子工具最多可用多久？** 解：最多 5 秒，忽略其他网络开销。

## 8. 权威来源与延伸阅读

- [Amazon Builders' Library · Timeouts, retries, and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)：deadline 传递、随机抖动和重试放大。
- [AWS Step Functions · Error Handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)：任务超时、重试与 catch 状态转换。
