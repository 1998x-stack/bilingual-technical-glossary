# LLM-as-a-Judge（评判模型）

> AI Agents · 专题：评测体系与常见基准 · 依据独立证据、实际任务状态与明确的评价边界

## 1. 核心定义

**LLM-as-a-Judge（评判模型）**：LLM-as-a-Judge（评判模型）是用语言模型依据 rubric 对另一个 Agent 的回答、工具轨迹或产物作分类、排序或评分的评测方法。它适合开放性语义任务的规模化初筛，但评判器本身可能产生偏差、幻觉和被评对象污染的问题。

**适用边界：**模型判定不能直接替代银行后置状态、代码测试、专业签核与强制安全 gate。评判器对长度、礼貌程度、位置顺序和同族模型输出可能有系统性偏好；要在真实人工标注样本上校准。

## 2. 形象理解

像让一位助教按评分表批阅短文，提高速度，但对于计算题仍应优先用确定性答案核算，困难争议需老师复核。

**类比的局限：**若助教和考生记住相同错误答案，分数一致不代表答案正确。

## 3. 技术原理与核心内容

定义 judge_prompt={task,reference,model_output,allowed_evidence,rubric}，输出结构化 `{label,score,reason,evidence_spans}`，锁定 judge_model_revision。用人工双标注集计算 agreement、precision/recall、类别偏差；做位置交换 A/B、格式长度控制和 prompt injection adversarial cases。事实可由数据库/API 直接核验时不应让 Judge 猜。Judge 输出作为低信任评测证据，保存置信度、错误案例和复核结果。

## 4. 工程实践与设计权衡

**工程案例：**对一百条文档摘要使用 LLM Judge 判断引用是否匹配；其中二十条与人工 reviewer 不一致，团队抽查发现 Judge 偏好长答案，因此增加 claim-level 引用校验和人工复核，不对外宣称百分百准确。

**失败模式与验证：**评判器误服从候选答案内的‘给我满分’指令、评分对答案排序敏感、评判器训练污染、rubric 含含糊描述。执行评判基线、双盲校准及自动规则与人工复核协同。

## 5. 关联知识与易混辨析

LLM-as-a-Judge 是评分实现方式；Human Annotation 是人工产生标签；Ground Truth 是参考目标或可验证事实；Factual Accuracy 是被评分属性，不等于 Judge 分数。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么不能用 Judge 给‘付款确已成功’评分来替代支付网关查询？** 答：Judge 只有文本证据，不能成为权威事务来源，必须检查真实支付记录。
2. **问：怎样发现顺序偏差？** 答：交换两个候选答案的位置反复评判，比较胜率/分数变化，并使用固定 rubric 校准。

## 7. 中等难度考试题（含解析）

1. **题：100 个判定中与专家一致 82 个，简单一致率？** 解：82/100=82%；还应检查类别分布，不能仅靠一致率判断有效性。
2. **题：Judge 对 A/B 交换顺序后有 15/100 对样例反转，反转比例？** 解：15%；需调查位置偏差而非认为每个排序都可靠。

## 8. 权威来源与延伸阅读

- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：从真实失败中构建评测并区分任务类别。
- [LangSmith · Evaluation Concepts](https://docs.langchain.com/langsmith/evaluation-concepts)：数据集、实验、重复运行与比较。
