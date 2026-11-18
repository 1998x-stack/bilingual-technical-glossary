# Tool-call Accuracy（工具调用正确率）

> AI Agents · 专题：评测体系与常见基准 · 明确分母、独立验证器、证据和安全界限

## 1. 核心定义

**Tool-call Accuracy（工具调用正确率）**：Tool-call Accuracy（工具调用正确率）是 Agent 在需要调用工具的决策点上选择合适工具、填写合法且语义正确的参数，并满足调用时机和授权范围的比例。它评估调用意图与规范，不能单凭工具返回 OK 判断选择正确。

**适用边界：**正确工具名不代表调用正确：订单 ID、币种、日期、tenant 和写权限可能错误。一次任务可能包含多个调用，不同计数方式（per-call、per-decision、per-task）必须在报告中注明。

## 2. 形象理解

像实验员不仅要选对仪器，还要把样本放对、调好量程并遵守实验授权。

**类比的局限：**选对仪器不代表测量结果准确；实验环境和设备本身也可能故障。

## 3. 技术原理与核心内容

为每个决策点定义 oracle={allowed_tool_names,argument_constraints,preconditions,resource_scope}，计算 `accurate_calls/eligible_calls`。工具 schema 可在确定性执行前验证类型，语义检查用引用 ID/实际权限/单位；对允许多个工具达成同一目标的场景，应定义可接受集合，避免把有效替代路线误判。记录 false_positive_invocations（不该调用却调用）和 missed_calls（该调用却不调用），不能只看成功发出的请求。

## 4. 工程实践与设计权衡

**工程案例：**Agent 应查询用户自己的订单，正确调用 `get_order(order_id=123,tenant_id=A)`；若工具名正确但 tenant=A 之外的订单也被查询，属于越权且应判失败。对生产删除工具即使 schema 合法也需独立审批。

**失败模式与验证：**只匹配工具名、未测不必要调用、把 tool 200 当 accuracy、评测未考虑动态工具列表和权限。对同名工具、边界参数、禁用工具及工具不可用场景构建测试。

## 5. 关联知识与易混辨析

Tool-call Accuracy 衡量工具调用决策；Action Success Rate 判断外部动作是否达到目标；Trajectory Evaluation 观察整个调用序列；Task Success 是总体目标。

## 6. 中等难度面试题（含参考答案）

1. **问：选对 `search` 工具但参数泄漏别人的客户 ID 算准确吗？** 答：不准确且可能严重违规，工具调用准确性必须包含语义与权限约束。
2. **问：为什么需要统计不该调用工具却调用的事件？** 答：仅对已调用样本算正确率会忽略误触发写操作与不必要资源消耗。

## 7. 中等难度考试题（含解析）

1. **题：共 80 个应调用的决策点，其中 68 次工具+参数完全正确，accuracy？** 解：68/80=85%。
2. **题：已调用 20 次且 18 次正确，但还有 5 个应调用却遗漏，按全部可评决策点计算为多少？** 解：18/(20+5)=72%，假设 20 次均对应应调用决策。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Testing](https://openai.github.io/openai-agents-python/testing/)：模型/工具调用的可重复测试边界。
- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：评估任务成功与错误分类。
