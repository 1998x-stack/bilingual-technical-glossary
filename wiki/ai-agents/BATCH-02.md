# AI Agents · 第 2 批（021–040）综合学习路径（仅供编审）

> 源词表 [AI Agent](../../glossaries/ai-agents.md)，本材料为编辑研究路线与综合练习。**公共站点不得显示批次、候审状态或审稿信息。**

## 核心知识地图

`Observation → Action → Termination Condition` 回接上一批智能体控制循环；`Model Invocation → Token → Context Window → Token Budget` 构成模型调用的资源约束；`Inference-time Compute / Test-time Compute → Reasoning Model` 描述质量、时间与算力的取舍；`Temperature → Structured Output → Constrained Decoding → Function Calling` 描述采样、输出契约和与工具执行的边界；`CoT → ToT / Self-Consistency → ReAct → Reflection / Self-Correction → Hallucination` 是模型的候选推理、环境反馈与质量保障链。

**不能混淆的五组概念：**
- Action vs Function Calling：行动是决策概念，函数调用只是一种可能的工具接口。
- Inference-time vs Test-time Compute：前者覆盖推理阶段总体计算；后者侧重额外推理预算策略。
- Structured Output vs Factual Correctness：schema 有效不代表业务事实正确。
- CoT vs ToT vs Self-Consistency：单路径推导、思路树搜索、多条路径最终答案聚合三种机制不同。
- Reflection vs Self-Correction：经验总结与当前结果修订相关但不等价，必须结合外部证据。

## 工程贯穿案例：报价与库存 Agent

需求是“查三家供应商现货与价格，选合规方案，生成候审采购单”。先设置 Action 白名单、查询任务与终止条件；模型调用只能在 Context Window 与 Token Budget 内进行。价格与库存由外部查询获取，`function_call` 只是模型提出的操作，执行结果必须记录订单 ID 与状态。候选报价用 Structured Output 校验形式、业务逻辑核验币种、税率、采购授权和供应商名称。复杂选型可利用 ToT/验证器比较多个候选，不能让多数样本替代事实来源。采购提交仍需人为审批和服务端幂等机制。

## 综合中等难度面试题

**问题：**报价 Agent 输出合法 JSON，显示供应商 A 价格 100 元，但数据库当前是 130 元。已设置低 temperature、CoT 和 5 次 Self-Consistency，系统应怎样处理？

**参考答案：**格式与事实是不同层次。必须以授权的权威价格源和有效时间戳核验，保留 request_id、观察时间与引用。低温、多候选和长推理都不能替代外部校验。对报价差异提出再查询或用户确认，写操作保持禁用。

## 综合中等难度考试题

**题：**题设一次初步模型调用耗时 0.8 s，随后 3 次独立报价查询各 0.5、0.7、1.0 s，可全部并发；最终汇总模型调用耗时 0.6 s。忽略排队和传输，总时延下界是多少？若查询串行又是多少？

**解：**并发总时间 `0.8 + max(0.5,0.7,1.0) + 0.6 = 2.4 s`；串行总时间 `0.8 + (0.5+0.7+1.0) + 0.6 = 3.6 s`。下界基于查询相互独立、无限并行资源的教学假设，不代表测量值。

## 参考资料（适用主张需在审稿中逐条核对）

- [ReAct 原始论文](https://arxiv.org/abs/2210.03629)
- [CoT 原始论文](https://proceedings.neurips.cc/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html)
- [ToT 原始论文](https://arxiv.org/abs/2305.10601)
- [Self-Consistency 原始研究](https://research.google/pubs/self-consistency-improves-chain-of-thought-reasoning-in-language-models/)
- [OpenAI Structured Outputs 文档](https://developers.openai.com/api/docs/guides/structured-outputs)
- [OpenAI Function Calling 文档](https://developers.openai.com/api/docs/guides/function-calling)
