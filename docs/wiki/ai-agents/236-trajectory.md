# Trajectory（轨迹）

> AI Agents · 专题：评测体系与常见基准 · 来源核验、场景适用与工程边界

## 1. 核心定义

**Trajectory（轨迹）**：Trajectory（轨迹）是 Agent 在执行任务期间经历的可观察事件序列，包含输入、环境观察、模型动作选择、工具调用、返回结果、状态变更以及可能的人工批准。它是评测和事故复盘的基础数据，不等同模型私有的思维链文本。

**适用边界：**不应为了评测而要求泄露模型不可公开的内部推理，也不应把模型口头‘已经查过’当成真实工具轨迹。轨迹需明确采样丢失、时钟不同步、隐私脱敏和哪些外部状态未被日志捕获。

## 2. 形象理解

像高山徒步的 GPS 轨迹，记录实际走过的路线、停留点与环境，但不能凭路线图推断登山者的全部内心想法。

**类比的局限：**GPS 可能漏点或漂移，真实违规/伤害还需其他数据来源独立确认。

## 3. 技术原理与核心内容

一条轨迹可表示为 τ=[(t_i,agent_i,state_i,observation_i,action_i,tool_result_i,operation_id_i)]。Tool call、handoff、checkpoint、approval 等作为 typed events，使用 trace_id/span_id 和 task_id 建立关联；同一次用户任务可能跨多个服务和模型调用。应在日志写入前按敏感数据政策做允许列表脱敏，记录资源版本与事件可信等级。用于评分时分别采用 outcome oracle、过程约束和成本统计。

## 4. 工程实践与设计权衡

**工程案例：**软件发布 Agent 的轨迹保留 git diff、CI run、扫描结果、人工批准、deploy ID 和生产核验。仅有聊天回复‘部署完毕’不构成真实轨迹；若 CI scan 被跳过，轨迹能揭示不合规路径。

**失败模式与验证：**只保存自然语言摘要、多个 Worker 乱序结果错配、trace 中泄漏凭证、日志缺失被误认为动作没发生。通过并发 trace、断连、外部事务和脱敏异常测试验收。

## 5. 关联知识与易混辨析

Trajectory 是可观察执行记录；Trajectory Evaluation 是对它的质量评分；Execution Log 是承载轨迹的事件存储方式；Chain-of-Thought 不应作为唯一或必需轨迹来源。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么模型自述不等于 Agent 的实际 Trajectory？** 答：自述可能虚构或遗漏行动，真实轨迹需要可关联的工具请求、结果与环境后置条件。
2. **问：Agent 轨迹跨多个 Worker 应如何合并？** 答：按 task_id、trace_id、span_id 和各自时间/版本建立关系，不简单按消息到达顺序拼接。

## 7. 中等难度考试题（含解析）

1. **题：一次任务有 4 个模型步骤、3 个工具调用、2 次审批记录，共多少个事件？** 解：4+3+2=9 个可记录事件，假设互不重叠。
2. **题：轨迹记录 12 次工具调用，其中 2 次因日志故障缺失详细结果，可以说覆盖完整吗？** 解：不能，详细结果覆盖率至多 10/12≈83.3%。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Tracing](https://openai.github.io/openai-agents-python/tracing/)：可观察的 model/tool/handoff 事件。
- [OpenTelemetry · Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)：关联 trace 与外部事实日志。
