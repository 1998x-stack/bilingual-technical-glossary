# Regression Test（回归测试）

> AI Agents · 专题：评测体系与常见基准 · 环境、数据版本和授权范围均为评测前提

## 1. 核心定义

**Regression Test（回归测试）**：Regression Test（回归测试）是在 Agent 模型、工具 schema、提示、规则或网站实现发生变化后，重复运行已知重要任务与失败案例，确认旧行为没有意外退化的测试。对 Agent 而言，既要检查最终产物，也应验证工具权限和实际外部状态。

**适用边界：**回归测试是必要而非充分保证，历史样例不能覆盖未来所有风险。只检查‘模型输出含关键词’可能掩盖错误工具调用和越权行为；对随机生成结果不要要求所有自然语言逐字相同。

## 2. 形象理解

像每次升级汽车刹车系统后重做基础制动、湿地打滑、紧急避让测试，避免改好一项却破坏另一项。

**类比的局限：**反复通过旧道路测试不能保证全新极端天气没有未知故障，仍需要探索性和真实世界监控。

## 3. 技术原理与核心内容

把失败事件归档为 `RegressionCase={id,input,fixture,tool_schema_version,expected_postconditions,forbidden_actions,reference_sha}`。使用 Mock/ScriptedModel 测分支、schema 与拒绝逻辑；真实服务 E2E 校验 GitHub issue 是否创建、payment_id 是否存在、资源权限是否遵守。分离 deterministic tests 与随机性分布统计，设置 CI gate，例如安全违规 0 容忍、关键任务 success 不下降。每次构建记录 commit/模型/评判器版本以保证可比较。

## 4. 工程实践与设计权衡

**工程案例：**模型优化后 PR Agent 写作更流畅，但偶尔会绕过代码扫描。团队为该失败增加固定回归任务：注入未通过的 CI，要求执行系统不得发起 merge；同时检查无论提示怎样改变工具 ACL 都不能被模型自述突破。

**失败模式与验证：**回归集只加成功案例、未锁定依赖导致伪失败、用字符串匹配误杀合法替代路线、同一测试因共享数据库污染结果。通过隔离 fixture、权限对照和 CI 构建阻断测试。

## 5. 关联知识与易混辨析

Regression Test 保证已知性质不退化；Benchmark 用统一环境比较系统；Scenario-based Evaluation 重现真实情境；Unit Test 检查更小的逻辑单元。

## 6. 中等难度面试题（含参考答案）

1. **问：Agent 更换模型后为什么要重跑权限负面测试？** 答：模型可能改变工具路由/参数，必须由执行层真实验证旧安全边界仍被保持。
2. **问：回归测试能否仅依据自然语言输出完全一致？** 答：不适合大多数 Agent 任务，应按语义后置条件和安全谓词判断，允许合法表达差异。

## 7. 中等难度考试题（含解析）

1. **题：一次变更后回归用例 120 个，112 通过、5 失败、3 未执行，完整通过率？** 解：112/120≈93.3%，应单独披露 3 个未执行。
2. **题：100 个旧案例新增 20 个安全负例，当前全部通过 108 个，合计成功率？** 解：108/(100+20)=90%，同时需披露安全负例自身通过数。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Testing](https://openai.github.io/openai-agents-python/testing/)：脚本化模型、工具契约和可重复运行。
- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：失败样本回归、梯度式分类评测。
