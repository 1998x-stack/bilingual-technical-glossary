# Trajectory Evaluation（轨迹评测）

> AI Agents · 专题：评测体系与常见基准 · 明确分母、独立验证器、证据和安全界限

## 1. 核心定义

**Trajectory Evaluation（轨迹评测）**：Trajectory Evaluation（轨迹评测）是对 Agent 在任务期间选择的中间动作、工具调用、观察结果和状态转换构成的执行序列进行评价，而不仅是检查最后的答案。它可分析低效循环、越权访问、错误重试和虽然最终成功但过程违规的路径。

**适用边界：**不应把模型私有思考文本当作唯一或必须获取的轨迹；重点应记录可观察的消息、工具调用、结果及状态变化。不同的合法工具路径可能同样成功，逐步严格字符串匹配容易误杀可接受替代方案。

## 2. 形象理解

像评价棋手不仅看最终输赢，也分析关键走法是否合理、是否重复无效尝试以及有没有违规落子。

**类比的局限：**不同策略可能用完全不同的中间动作达到同一合法目标，过程评分需要允许多解。

## 3. 技术原理与核心内容

轨迹可序列化为 `τ=(o0,a0,r0,o1,a1,r1,...,oT)`，o 为外部观察，a 为动作，r 为工具返回或后置检查。为每步定义 allowed_tool、precondition、authorization、cost 和 transition invariants。评估可采用 rule-based state machine checker、序列编辑距离、参考轨迹集或审稿 rubric；工具 trace 必须脱敏。按失败类别计算违规比例、重复调用次数和恢复后的行为，而非仅凭最终文本评分。

## 4. 工程实践与设计权衡

**工程案例：**文件整理 Agent 最终正确汇总文件，却曾访问另一个租户的私有目录；Outcome Evaluation 可能误判通过，Trajectory Evaluation 会发现中途越权路径并判整个安全任务不合格。

**失败模式与验证：**轨迹记录缺失工具结果、无限逐字匹配、忽略隐式工具副作用、模型解释与真实行动混淆。使用故意构造的错误工具顺序、非法权限、无界重试及多条合法路径测试。

## 5. 关联知识与易混辨析

Trajectory Evaluation 着重整个动作序列；Trajectory 是序列本体；Process Evaluation 着重规则/程序遵守；Outcome Evaluation 着重最终状态。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么不能只以最终答案评分 Agent 轨迹？** 答：最终正确也可能通过越权、泄密或重复写操作取得，不能接受不安全路径。
2. **问：合法路径不同于参考路径，评测怎么处理？** 答：以语义约束、允许行动集合和结果后置条件判断，不强制只有一个固定调用序列。

## 7. 中等难度考试题（含解析）

1. **题：某轨迹含 12 次工具调用，其中 3 次违反授权，越权率？** 解：3/12=25%。
2. **题：两条合法路径分别用 4 与 7 次调用且都成功，在只考虑调用数的效率指标上哪条更好？** 解：4 次路径成本更低，但完整比较还需真实性能与安全约束。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Tracing](https://openai.github.io/openai-agents-python/tracing/)：模型、工具和 handoff 轨迹。
- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：评估任务成功与错误分类。
