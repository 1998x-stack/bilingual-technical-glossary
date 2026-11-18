# Termination Condition（终止条件）

> AI Agents · 专题：基础概念与角色 · 通用概念；产品特性以文档版本和模型接口为准

## 1. 核心定义

**Termination Condition（终止条件）**：Termination Condition（终止条件）是智能体运行器判断何时结束本次任务的可执行规则。它可以基于已验证成功、显式失败、超时、用户取消、权限拒绝或资源预算耗尽；终止不必等于完成。

**适用边界：**最终模型回答只是可能的结束信号；高风险业务需要外部可检查的完成谓词。

## 2. 形象理解

像运动比赛的终场哨：赢球、时间到、违规或比赛取消都可能导致结束，但结果含义不同。

**类比的局限：**终止规则并不能保证任务可达，也不能自动撤销之前发生的副作用。

## 3. 技术原理与核心内容

设计 `terminal_state ∈ {succeeded, failed, cancelled, timed_out, budget_exceeded, blocked}`。控制循环每轮先核对硬性上界：`steps <= max_steps`、`elapsed <= deadline`、`tokens <= quota`，再根据验证器检测成功谓词。要区分“模型产出 final”与“业务系统状态达到 success”，并在终止时关闭未完成的待处理任务。

## 4. 工程实践与设计权衡

**工程案例：**报销 Agent 得到“已提交”的文字时，仍需查验审批系统中的报销 ID 和状态；若查验失败，返回带证据的未知状态。对于敏感写操作，终止前还须记录审批及审计轨迹。

**失败模式与验证：**仅限制模型迭代数无法阻止单个工具一直阻塞；只按“没有继续工具调用”退出，会把无权限、幻觉或死循环误报为成功。记录终止原因可以帮助统计失败类别。

## 5. 关联知识与易混辨析

Goal 定义期望结果；Stopping Criterion 是通用的停止准则；Termination Condition 约束一次具体 Agent 运行何时转到终态。

## 6. 中等难度面试题（含参考答案）

1. **问：一个 Agent 每轮都调用失败的检索工具，如何避免无限循环？** 答：设置每工具重试次数、全局 deadline 和最大模型轮数；连续无新信息应重规划或输出失败，并将业务终态和资源终态分别报告。
2. **问：为什么最终回答出现“完成”不能作为唯一成功条件？** 答：语言生成与外部事务执行分离；需要验收谓词检查持久状态、文件存在性或 API 事务 ID，必要时要求人工确认。

## 7. 中等难度考试题（含解析）

1. **题：题设运行最多 8 轮，已执行 6 轮，完成验证器为 false，下一轮将产生 2 次模型调用。若每次调用算一轮，是否还允许？** 解：第 7、8 轮可执行，但用完后必须停止；若仍未成功应标记 budget_exceeded，不得写作 succeeded。
2. **题：列出“用户取消”“成功完成”“超时”三个终止状态及各自应记录的最小证据。** 解：取消：用户/系统取消请求与时间；成功：权威完成记录及验收检查；超时：deadline、已执行步骤与未知副作用，三种终态不可互相替代。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Running agents](https://openai.github.io/openai-agents-python/running_agents/)：运行循环、工具调用、最终输出及最大轮次。
- [OpenAI · A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)：模型、工具、指令和护栏。
