# Outcome Evaluation（结果评测）

> AI Agents · 专题：评测体系与常见基准 · 来源核验、场景适用与工程边界

## 1. 核心定义

**Outcome Evaluation（结果评测）**：Outcome Evaluation（结果评测）是以 Agent 执行后得到的最终答案、产物或外部环境状态是否符合用户目标为中心的评价方式。它通常适合有明确后置条件的任务，但应与安全门控和过程质量检查配合。

**适用边界：**若只看最终文本，可能错把未发生的付款、无效 PR 或过期报告当成功。某些任务存在多个等价正确答案，需要语义/业务 oracle 而非严格字符串匹配；无法验证的结果应标 unknown。

## 2. 形象理解

像烘焙比赛先检查最后蛋糕是否可食、符合重量和配方要求，而不是只看厨师写的制作说明。

**类比的局限：**成品好吃并不证明制作过程符合卫生规定；高风险任务需独立过程审计。

## 3. 技术原理与核心内容

定义 outcome_oracle(y,world_final,requirements)→pass/fail/unknown，输入包括 output artifact hash、真实数据库状态、测试环境快照和允许误差。数值任务用 tolerance 检查，代码任务运行隐藏测试，文档任务对引用和逻辑约束采用人工/校准评审。计算已核实完成的比例，分开报告无法访问外部状态的样例及严重安全违规。将终态观测版本绑定原始用户需求与 request_id。

## 4. 工程实践与设计权衡

**工程案例：**GitHub PR Agent 说‘PR #20 已创建’时，评测到仓库实际查询 PR #20 的 head/base、文件差异与 CI，不接受自然语言 URL 自述。即使目标 PR 存在，但修改了无关敏感文件也应被判为不合格。

**失败模式与验证：**只看回复流畅度、缓存到旧部署版本、忽略成本/安全、不同数据版本下 oracle 不兼容。用伪造任务成功、真实状态不匹配、多个合法答案和隐私负例验证。

## 5. 关联知识与易混辨析

Outcome Evaluation 聚焦最终状态；Process Evaluation 检查合规的中间步骤；Trajectory Evaluation 检查整个序列；Task Success Rate 是可汇总的成功比例。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么最终答案看似正确仍需查环境后置条件？** 答：Agent 可能没调用工具或工具失败，真正任务成功要求外部对象状态符合目标。
2. **问：结果有多种合法表述，如何避免过度依赖 exact match？** 答：按任务语义约束、明确可接受集合和权威事实检查，不必要求自然语言逐字相同。

## 7. 中等难度考试题（含解析）

1. **题：50 个任务最终产物 40 个通过验收、5 个失败、5 个未知，保守结果通过率？** 解：40/50=80%，未知另报。
2. **题：一个数值目标 100±2，输出 101.5 是否在容差内？** 解：是，因为 |101.5−100|=1.5≤2。

## 8. 权威来源与延伸阅读

- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：明确判断标准与逐类错误分析。
- [LangSmith · Evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts)：dataset、实验与评估结果。
