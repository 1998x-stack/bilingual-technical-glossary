# Factual Accuracy（事实准确性）

> AI Agents · 专题：评测体系与常见基准 · 来源核验、场景适用与工程边界

## 1. 核心定义

**Factual Accuracy（事实准确性）**：Factual Accuracy（事实准确性）是输出中的事实性陈述与可验证现实及可靠权威来源相符合的程度。它不仅判断模型是否忠于当前检索上下文，更要审查实体、时间、数字、单位、来源可信度和适用版本。

**适用边界：**事实‘准确’也需明确评测参考时间与环境，尤其对快速变化的 API 规范、价格、政策与软件版本。无法确认的结论应标 unknown/needs_review，而非为提高分数虚构一个确定值；只看模型评分会产生共享错误。

## 2. 形象理解

像审计员核对报告中的交易金额，不只检查它是否与草稿一致，还要追溯银行流水和合法凭证。

**类比的局限：**官方来源也可能有版本更新或纠错，不能脱离时间和范围绝对化判断。

## 3. 技术原理与核心内容

为每条可检验 claim 建立 `{entity,predicate,value,unit,valid_at,source_id,version}`，与独立可信 reference record 对齐。计算 accuracy 可按正确 claim 数/有效判定 claim 总数，另报 unverified、critical errors。数值设置 tolerance 和单位换算，版本化 API 检查官方规范；事实核验可先确定性查数据库/代码运行，再由专业审阅处理争议。评测报告还应说明来源选择、冲突处理及置信区间，避免将两条相关证据误当独立投票。

## 4. 工程实践与设计权衡

**工程案例：**AI Agent Wiki 写‘某版本 MCP 采用 initialize’时，审稿应读取指定版本规范并核对时间；如果把 2025 旧版规则误套 2026，虽然引用了 MCP 官网，事实准确性仍不合格。

**失败模式与验证：**官方页面已更新但旧缓存未失效、金额单位混淆、未经验证的人名/日期、模型多次一致却共享同一幻觉。用包含过期标准、冲突来源、货币差异和可重现数学错误的评测集校准。

## 5. 关联知识与易混辨析

Factual Accuracy 对照外部真实事实；Faithfulness 对照已给上下文；Outcome Evaluation 针对最终任务结果；Citation/Attribution 是证据标注机制，不能天然等同真实性。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么源文档忠实复述与事实准确性会出现不同结果？** 答：源文档可能过时或错误，忠实度高但与当前权威事实不符。
2. **问：如何审查‘版本 X 的接口必须调用 initialize’？** 答：锁定版本号与规范发布时间，读取对应官方文档/实现契约，而非凭当前通用记忆。

## 7. 中等难度考试题（含解析）

1. **题：20 条可核验事实断言中 17 条正确、2 条错误、1 条无法核验，按所有条目保守准确率？** 解：17/20=85%，另单独披露 1 条 unknown。
2. **题：120 美分与 1.20 美元是否数值等价？** 解：在 100 美分=1 美元的单位关系下是等价的，但还需确认是同一币种。

## 8. 权威来源与延伸阅读

- [Ragas · Faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)：检索证据支持的断言比例。
- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：明确判断标准与逐类错误分析。
