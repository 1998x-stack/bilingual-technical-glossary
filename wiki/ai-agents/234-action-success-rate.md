# Action Success Rate（动作成功率）

> AI Agents · 专题：评测体系与常见基准 · 明确分母、独立验证器、证据和安全界限

## 1. 核心定义

**Action Success Rate（动作成功率）**：Action Success Rate（动作成功率）是智能体实际执行的环境动作在执行后达到预期可观察状态的比例，可用于衡量工具动作在真实业务系统或沙箱中的可靠性。它需要检查后置条件而非仅依据调用返回码或模型自述。

**适用边界：**动作的安全性与正确性是不同维度：未经授权删除可能技术上成功，但绝不应被评为合格 Agent 行为。对 timeout、部分提交与中断后的 unknown 状态应单独记录，不可把它们直接当成功。

## 2. 形象理解

像机器人伸手抓起杯子，发出了抓取命令不是成功，必须确认杯子已被稳定抓住且没有打碎。

**类比的局限：**单个动作成功不代表完整工作流达到目标，后续动作可能失败或造成新的副作用。

## 3. 技术原理与核心内容

对 action_i 定义 expected_postcondition_i，执行后读取 authoritative state，计算 `ASR=verified_successful_actions/all_attempted_actions`，并分 readonly 与 side-effect、工具类型、重试次数报告。对重复尝试按业务 operation_id 识别唯一动作，避免重试膨胀分母或多计成功。高风险动作先通过 authorization gate，错误执行后即使完成也应报告 policy violation。

## 4. 工程实践与设计权衡

**工程案例：**发布 Agent 调用 deploy(commit=A) 返回 HTTP 200，但生产服务仍运行 B，Action Success=0；后来查询显示 A 已实际部署，重新验证后才能更改状态。环境受限时需保守标注 unknown。

**失败模式与验证：**凭状态码推定动作成功、错用旧缓存验证、重复 retry 被计作多个成功动作、跨区域状态不一致。执行同任务不同网络延迟、权限拒绝和最终一致性等待测试。

## 5. 关联知识与易混辨析

Action Success Rate 面向真实动作结果；Tool-call Accuracy 面向模型决策/参数；E2E 成功需要全任务满足；Process Evaluation 涵盖安全与过程合法性。

## 6. 中等难度面试题（含参考答案）

1. **问：HTTP 200 为什么不能直接代表 Action Success？** 答：服务端可能只是接受异步请求，业务还 pending；需要实际目标状态验证。
2. **问：执行成功的未经授权动作是否可计作完整任务成功？** 答：不可，技术动作达成应与安全合规指标分开，完整成功需要授权。

## 7. 中等难度考试题（含解析）

1. **题：20 次动作中 15 次经确认达成目标、3 次失败、2 次 unknown，保守 ASR？** 解：15/20=75%；unknown 单独报告。
2. **题：5 次同一个 operation_id 的网络重试实际只产生 1 笔成功付款，按唯一业务操作应计几次成功？** 解：1 次，避免重复计数。

## 8. 权威来源与延伸阅读

- [OpenAI · Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)：评估任务成功与错误分类。
- [OpenAI Agents SDK · Testing](https://openai.github.io/openai-agents-python/testing/)：模型/工具调用的可重复测试边界。
