# Human Annotation（人工标注）

> AI Agents · 专题：评测体系与常见基准 · 依据独立证据、实际任务状态与明确的评价边界

## 1. 核心定义

**Human Annotation（人工标注）**：Human Annotation（人工标注）是人类根据任务定义和评分准则对样本、模型输出或动作轨迹赋予标签、偏好、分数或错误原因的过程。它常用于建立 Ground Truth、校准 Judge 和发现自动化评测遗漏的失败模式。

**适用边界：**有人标注不代表已经成为合格的独立专业审查；标注质量受到领域经验、上下文完整性、培训和付费/时间压力影响。不能把自动化模型评分冒充真人签字，也不能在无授权条件下向标注员暴露用户敏感数据。

## 2. 形象理解

像两名经过训练的医学影像阅片者依据统一规则做判断，分歧再由资深专家仲裁，而不是只记录一个未注明身份的勾选框。

**类比的局限：**人类意见可受偏见与疲劳影响，多个标注员一致也不能替代外部事实核验。

## 3. 技术原理与核心内容

设计标注指南 rubric、标签例子与边界，要求每条 LabelRecord={case_id,artifact_sha,annotator_id,reviewed_at,label,rationale,source_refs,rubric_version}。为部分样本安排至少两人独立标注，统计 raw agreement、Cohen κ 或 Krippendorff α 视任务而定；对冲突条目做 blind adjudication。高风险数据需脱敏、访问控制与保留期限，变更被标注 artifact 的 SHA 后旧标签不再自动有效。

## 4. 工程实践与设计权衡

**工程案例：**AI Agent Wiki 词条的技术定义评审时，独立 reviewer 逐条核对官方资料、数学算例和版本差异；自动结构 CI 只能证明格式，不能自动将 reviews ledger 从 pending 改成 approved。

**失败模式与验证：**标注泄漏用户隐私、把一份模型自评复制成几十份人工意见、低一致性却不仲裁、签核不绑定正文版本。建立分歧追踪、双盲复核与数据撤权测试。

## 5. 关联知识与易混辨析

Human Annotation 是产生标签的流程；Human Review 是更广的专业审查；Ground Truth 是被作为目标的参考；Human Approval 是执行敏感动作的授权，不能与标签混同。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么专业 Wiki 审稿需要正文 SHA 和 reviewer ID？** 答：明确谁在何时对哪份不可混淆的文本做过审核，后续修改应触发重新审查。
2. **问：高一致率为什么也不能证明事实绝对正确？** 答：标注员可能共享错误的参考资料或培训偏差，必须有权威来源和外部 oracle。

## 7. 中等难度考试题（含解析）

1. **题：两位标注员对 40 条样例有 34 条相同标签，简单一致率？** 解：34/40=85%，尚不能代替考虑随机一致的 κ。
2. **题：20 篇文档里只有 12 篇经有效人工审核，可称全部完成审核吗？** 解：不能，实际完成率为 12/20=60%，其余保持 pending。

## 8. 权威来源与延伸阅读

- [NIST · AI RMF Playbook](https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-playbook)：人类判断、标注和风险证据。
- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：从真实失败中构建评测并区分任务类别。
