# Fan-in（扇入）

> AI Agents · 专题：工作流与编排模式 · 图编排、同步和权限边界；SDK 特性以对应版本文档为准

## 1. 核心定义

**Fan-in（扇入）**：Fan-in（扇入）是工作流中多个上游分支在共同后继节点汇合的拓扑模式。扇入节点通常等待必要上游满足条件，再汇总结果或作统一决策；它的核心问题是同步、缺失结果、重复消息和冲突处理。

**适用边界：**Fan-in 不强制所有分支都成功才继续，具体是 all、any、quorum 还是 timeout 取决于业务策略。物理汇合节点不自动等于语义正确的 Aggregation Pattern。

## 2. 形象理解

像项目验收会议收集法务、性能和安全三份审查意见，等必要意见齐全后才能作发布决定。

**类比的局限：**参加会议人数齐全不意味着每项审查通过，缺失的高风险意见不能用多数投票掩盖。

## 3. 技术原理与核心内容

运行器跟踪 expected_task_ids、received_results、deadline 和 join_policy；使用 correlation_id 和幂等去重，确保分支重试不会被统计两次。all-of join 需所有必需任务完成，quorum join 需指定数量的有效投票，且针对敏感门控可能强制特定子集全部通过。合并前验证 schema、版本、租户与来源，并保留 partial 状态以便恢复。

## 4. 工程实践与设计权衡

**工程案例：**发布 Agent 将单测、依赖扫描和许可证检查 fan-in 到部署审批。即使 2/3 已通过，只要安全扫描未完成，仍不能宣布通过全部 gate。

**失败模式与验证：**按到达顺序而非 task_id 配对、重试重复计票、超时被解释为通过、等待永远不会返回的分支。用乱序、重复、迟到、取消和权限拒绝测试验证 join 策略。

## 5. 关联知识与易混辨析

Fan-in 是流程拓扑上的汇合；Aggregation Pattern 是如何汇总值的语义；Gate Check 负责验证是否允许继续；Fan-out 是上游分发，二者常配对。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 fan-in 不应只计算已收到结果数量？** 答：可能收到同一任务的重复回执，必须按 task_id 去重，并核对必需任务集合及状态。
2. **问：何时适合 quorum join 而不是 all-of？** 答：当业务允许一定数量独立结果达标即可继续；对法律、安全等必需审查通常需要 all-of 或更严格规则。

## 7. 中等难度考试题（含解析）

1. **题：期望 5 个不同 task_id，收到 6 条消息，其中一个 task_id 出现两次，且其余四个都出现，是否完成 all-of？** 解：是，去重后恰好 5 个必需 ID 都已收到；还须检查它们的完成状态。
2. **题：三项强制检查中两项成功、一项超时，all-of gate 应返回成功吗？** 解：不应，必须维持 pending/failed/unknown，并按策略处理超时。

## 8. 权威来源与延伸阅读

- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：工作流 gate、并行化、循环边界。
- [LangGraph · Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)：状态图、条件路由与图式执行。
