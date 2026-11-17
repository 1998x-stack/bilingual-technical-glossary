# Stopping Criterion（停止准则）

> AI Agents · 专题：任务规划与决策 · 通用工程概念；具体行为以平台、协议与版本为准

## 1. 核心定义

**Stopping Criterion（停止准则）**：Stopping Criterion（停止准则）是判断搜索、Agent 循环、工具重试或计划执行在何时应停止的可测试规则，可依据成功谓词、失败、轮数、费用、deadline 和安全约束。停止并不自动意味着任务成功。

**适用边界：**Stopping Criterion 是单条或一组停止判断；Termination Condition 描述具体 Agent 进入终态的控制机制。二者相关，但后者还需要状态上报和资源清理。

## 2. 形象理解

考试达到答题验收标准可以交卷，考试时间结束也必须停止，但不能因此宣布全部答案正确。

**类比的局限：**“时间到”只能说明停止原因，不能证明用户的业务目标已经完成。

## 3. 技术原理与核心内容

可定义 stop=verified_success OR steps≥K OR now≥deadline OR spent≥budget OR unsafe。运行器按原因转为 succeeded、failed、timed_out、budget_exceeded、blocked 或 cancelled，并记录最后的工具结果与未完成事项。为防止单工具挂起，必须把单次调用超时、任务总体 deadline 与取消信号传递结合起来。

## 4. 工程实践与设计权衡

**工程案例：**故障诊断 Agent 最多查 8 次日志。第 4 次通过可复核证据确认根因可以提前停止；若 8 次都没有证据，则报告无法确认与已做检查，而不是硬编“已修复”。

**失败模式与验证：**只限制模型轮数却不限制单次网络 I/O，会永久挂起；只凭模型 final 消息当成功导致错误验收。自动化测试应覆盖越过边界的一轮、用户主动取消以及预算提前耗尽。

## 5. 关联知识与易混辨析

Goal Predicate 是成功验证条件的一部分；Stopping Criterion 决定是否停止；Termination Condition 包括终态、原因、关闭等待任务和汇报的完整逻辑。

## 6. 中等难度面试题（含参考答案）

1. **问：循环预算耗尽的任务应怎样汇报？** 答：明确 reason=budget_exceeded、已完成与未完成步骤，成功标识必须来自独立业务验收，不能将预算耗尽包装为完成。
2. **问：为什么有最大 10 轮仍可能无法保证 Agent 退出？** 答：某一轮的工具或远程网络请求可能一直阻塞，应设置每请求超时、总体 deadline、取消传播与等待收敛。

## 7. 中等难度考试题（含解析）

1. **题：最多 6 轮，现已执行 5 轮且未成功，是否还能执行 2 轮？** 解：最多再执行 1 轮，第 6 轮未成功就以次数上限终止。
2. **题：任务第 3 轮已满足成功谓词，预算尚有 4 轮，能否提前退出？** 解：应该退出，并记录成功证据；不应为用尽预算继续执行可能产生副作用的操作。

## 8. 权威来源与延伸阅读

- [Russell、Norvig · Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/)：回溯搜索、决策和规划基础。
- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：代理循环与工具工程实践。
