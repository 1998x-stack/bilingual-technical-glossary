# Human Review（人工审核）

> AI Agents · 专题：执行状态、持久化与恢复 · 工程事故防护与可恢复性以业务事实为准

## 1. 核心定义

**Human Review（人工审核）**：Human Review（人工审核）是由人对模型建议、检索证据、代码变更或业务产物作独立检查并给出问题清单、修正要求或审核结论的过程。它侧重产物质量与事实正确性，可以是 Human-in-the-loop 的一部分，但不必然授予系统执行某个动作的权限。

**适用边界：**人点击‘看过’不等于专家签核，也不表示已审查具体内容版本。对于技术 Wiki、医疗、法律等高风险资料，应明确审查者身份、专业范围、版本哈希和结论证据，不能用 CI 通过伪造人工审核。

## 2. 形象理解

像代码仓库的 Pull Request 审查：工程师逐行指出并发、边界或安全问题，再由提交者修改并重新检查。

**类比的局限：**人类 reviewer 也可能错漏；没有可重现测试和原始资料支持的评论不能自动保证代码正确。

## 3. 技术原理与核心内容

定义 ReviewRecord={artifact_sha,reviewer_id,reviewed_at,rubric_version,findings,decision,scope}。Reviewer 查看原始产物与来源、检查高风险主张、复算数值和测试可复现性，输出 needs_changes、approved 或 unclear。后续产物修改应使旧批准在受影响范围失效；自动校验、模型评审和真人审查记录必须分开保存。需要两人审批时应核对 reviewer 身份与独立性。

## 4. 工程实践与设计权衡

**工程案例：**AI Agent Wiki 增加 30 篇术语后，CI 验证 8 章节、引用格式与镜像，真人专业审核还要确认技术定义、MCP/A2A 版本差异、数学推导和引用是否支持断言。在真正审核之前 ledger 只能标为 pending。

**失败模式与验证：**复用旧 SHA 的审核、用 LLM 评分替代专家、审核人和作者为同一角色不披露、错误引用没有核查。通过故意造错的公式、无关来源、正文变更后签核失效测试。

## 5. 关联知识与易混辨析

Human Review 是质量检查活动；Human Approval 是对明确操作放行；Reviewer Agent 是自动评审角色；Trace/CI 是辅助证据而非人类专业资质。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Human Review 需要绑定 artifact SHA？** 答：内容更新后原评论不一定有效，哈希能明确究竟审查了哪个版本，避免把旧签核套到新文档。
2. **问：为什么结构化校验通过还不能把专家审稿置为 approved？** 答：测试只检查事先编写的规则，不证明每条技术结论、来源与例题都经专业人士独立核实。

## 7. 中等难度考试题（含解析）

1. **题：30 篇文档有 18 篇经真实专家签核，完成审核比例？** 解：18/30=60%，其余应继续 pending。
2. **题：10 道题人工确认 8 道正确，另 2 道未核实，可以声称 100% 正确吗？** 解：不能，只能说 8 道已核实，另 2 道待审。

## 8. 权威来源与延伸阅读

- [NIST · AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)：治理、监督、风险与测量。
- [OpenAI Agents SDK · HITL](https://openai.github.io/openai-agents-python/human_in_the_loop/)：needs_approval、RunState 与审批持久化。
