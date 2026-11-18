# Agent Evaluation（智能体评测）

> AI Agents · 专题：评测体系与常见基准 · 定义、工程边界、可复算题目与独立事实核验

## 1. 核心定义

**Agent Evaluation（智能体评测）**：Agent Evaluation（智能体评测）是对 Agent 在特定任务、环境、工具授权和预算限制下实现真实目标的系统性检验，兼顾最终交付、行动轨迹、安全约束、效率和可追溯证据。与传统语言模型 QA 打分不同，Agent 测试应检查外部世界是否真的发生预期变化。

**适用边界：**模拟器成绩不一定可迁移到生产；测试环境、工具权限、样本分布及重试策略都影响成绩。单一 LLM judge 分数不能覆盖确定性业务约束和高风险操作的负面测试。

## 2. 形象理解

评测自动驾驶不能只看规划语言是否流畅，必须在模拟道路验证红灯停车、异常处理和最终到达。

**类比的局限：**模拟道路不可能覆盖全部环境，需真实环境的安全分层与上线后监控。

## 3. 技术原理与核心内容

定义 EvalCase={task_id,input,environment_snapshot,allowed_actions,expected_state,safety_constraints,oracle,cost_budget}。使用 ScriptedModel 测控制流工具契约，沙箱运行真实 API/文件状态完成端到端回归；计算 Task Success、Tool-call Accuracy、Action Success、p95 latency、token cost 和越权频率。对随机模型多次运行报告均值与区间，按领域/风险级分组，保留 task_id、trace、版本与失败路径。

## 4. 工程实践与设计权衡

**工程案例：**为 GitHub PR 创建 Agent 设计测试：不仅确认回复中含 PR URL，还要在测试仓库查询真实 PR、正确 base/head、被更改文件和 CI，注入只读权限、冲突分支与超时行为。

**失败模式与验证：**用泄漏的训练题评测、模型自评取代 oracle、只看最后一句而不检查副作用、总体均值掩盖严重越权。实施隔离 holdout、独立验收和错误分类复盘。

## 5. 关联知识与易混辨析

Agent Evaluation 是完整评测活动；Benchmark 是规范的共同测试体系；Eval Set 是待测样例；Trajectory/Process/Outcome 分别观察轨迹、步骤规范和最终状态。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Agent 最终文字正确还可能评测失败？** 答：可能未实际完成工具动作、曾越权读取、重复付款或违反时间/费用限制。
2. **问：如何让 Tool-call 路由的回归可重复？** 答：固定工具 schema、模型步骤、环境 fixture 和所需参数，另以真实集成环境测试外部服务。

## 7. 中等难度考试题（含解析）

1. **题：100 个任务中 80 个答案正确，其中 5 个伴有越权行为，且成功需无越权，最多多少满足完整成功？** 解：75 个，即 75%。
2. **题：三个子领域各 10 道题，成功 8、6、9 道，整体成功率？** 解：23/30≈76.7%。

## 8. 权威来源与延伸阅读

- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：评价任务、评分与错误分析。
- [OpenAI Agents SDK · Testing](https://openai.github.io/openai-agents-python/testing/)：ScriptedModel 确定性测试与真实环境测试分工。
