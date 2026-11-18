# Evaluation Dataset (Eval Set)（评测集）

> AI Agents · 专题：评测体系与常见基准 · 定义、工程边界、可复算题目与独立事实核验

## 1. 核心定义

**Evaluation Dataset (Eval Set)（评测集）**：Evaluation Dataset（Eval Set，评测集）是为检验 Agent 能力而准备的有版本、有输入、预期行为、环境 fixture 和评分依据的样例集合。评测集不应只包含正常问答，还要覆盖权限边界、工具错误、多轮恢复与与真实业务语义对齐的失败场景。

**适用边界：**训练集、调参开发集和真正 holdout 测试集必须合理隔离。对同一公开评测集反复修改 prompt 会过拟合，单次得分不能替代跨用户/项目分布和隐私处理审计。

## 2. 形象理解

像期末考试题库既包含基础知识题，也有综合与反例题，而原题不能提前流进学生训练材料。

**类比的局限：**样例正确不等于覆盖真实世界，标签本身也可能需要专业复核。

## 3. 技术原理与核心内容

存储 EvalCase={case_id,input,environment_fixture,reference_sources,expected_outcome,allowed_tools,rubric,tags,version}。依据用户群、专业子领域和风险等级做分层抽样，输入与验证 oracle 分离；对任务状态可用确定性检查器，对开放生成可用校准后的人工 rubric 或 LLM-as-a-Judge。每次运行记录覆盖率、成功率、置信范围、case-level failure，并对新版本评测集保留迁移说明。

## 4. 工程实践与设计权衡

**工程案例：**AI Agent Wiki 的 Eval Set 包含术语中英对应、来源支持断言、数学推导、PR 创建是否真实、越权访问以及断线恢复，共 120 项；实际用户敏感信息先取得合法授权并脱敏，避免混进公开测试库。

**失败模式与验证：**泄露真实客户资料、相似任务跨 train/test、错误标签、只测简单场景、没有记录未执行项。用标签双人复核、权限控制、数据来源记录与覆盖率报告。

## 5. 关联知识与易混辨析

Eval Set 是评测样例；Benchmark 还定义环境/运行协议；Rubric 是评分规则；Outcome Evaluation 是结果检查方式。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么模型开发时不能只优化同一组 holdout 题？** 答：会对固定题集过拟合并失去泛化估计，应维护隔离测试和新数据增量。
2. **问：生产失败样例怎样安全进入评测集？** 答：先确认合法使用范围、脱敏、权限与保留期，再以可复现 fixture 和评分标准保存。

## 7. 中等难度考试题（含解析）

1. **题：120 条样例中有 20 条权限相关，比例是多少？** 解：20/120≈16.7%。
2. **题：40 条样例有 10 条因环境异常没有运行，覆盖率是多少？** 解：(40−10)/40=75%，须单独披露未运行原因。

## 8. 权威来源与延伸阅读

- [LangSmith · Evaluation Concepts](https://docs.langchain.com/langsmith/evaluation-concepts)：评测数据、实验与评分器。
- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：评价任务、评分与错误分析。
