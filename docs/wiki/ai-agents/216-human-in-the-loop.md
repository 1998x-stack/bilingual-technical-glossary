# Human-in-the-loop (HITL)（人工介入 · HITL）

> AI Agents · 专题：执行状态、持久化与恢复 · 工程事故防护与可恢复性以业务事实为准

## 1. 核心定义

**Human-in-the-loop (HITL)（人工介入）**：Human-in-the-loop（HITL，人工介入）是在 Agent 自动化流程的关键时点要求人类提供判断、纠错、审核或批准，并把决定反馈到可恢复执行器的治理机制。它不仅是一条‘请人工审核’的提示词，而是带身份、职责和结果审计的真实控制路径。

**适用边界：**人工介入不代表所有人都能批准所有动作；谁有权审查、在什么时间对哪个版本做决定必须清楚。某些低风险操作可以自动执行，但重大资金、生产删除和法律承诺要与独立业务权限控制衔接。

## 2. 形象理解

像飞机自动驾驶可以执行常规航段，但重大异常和超出自动系统适用条件的决策要交给具备资格的飞行员。

**类比的局限：**有人在场并不确保判断正确，必须向人展示充分的事实、风险与替代方案，而不只给一个‘同意’按钮。

## 3. 技术原理与核心内容

运行器在敏感 tool_call 前计算 risk_gate(action,resource,user,parameters)，生成 `{approval_id,tool_call_id,scope,version,reason,expires_at}`，暂停并持久化状态。OpenAI Agents SDK 中 `needs_approval` 会产生 `RunResult.interruptions`，将 `result.to_state()` 保存后由 `state.approve/reject` 决定，再交给 Runner 继续；嵌套 Agent 的中断也要从外层恢复。采用 per-call 决定，谨慎使用 sticky always_approve，因为不同 Agent 的相同工具名可能共享批准作用域。

## 4. 工程实践与设计权衡

**工程案例：**采购 Agent 准备以 20,000 元向供应商提交合同，系统展示供应商 ID、总金额、税率和附件 SHA，并要求有采购权限的人签核。若附件或金额变化，已批准的调用失效，重新校验并进入等待。

**失败模式与验证：**提示词声称已获人工授权、审批被跨用户重用、批准过期未阻止调用、对下游子 Agent 的审批意外放行。测试越权、版本变动、拒绝、重复批准和审计完整性。

## 5. 关联知识与易混辨析

HITL 是人参与控制的总体模式；Human Review 检查产物；Human Approval 许可具体动作；Interrupt 是暂停的技术机制，不一定需要人工。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 HITL 不能仅通过让模型问一句‘你同意吗’实现？** 答：需要可信身份、参数绑定、状态持久化和真实执行层 gate，否则模型可误解回复或被提示注入绕过。
2. **问：什么情况下不应该使用 sticky always_approve？** 答：不同目标、执行者或权限可能共享同一工具名时，粘性批准容易跨调用扩大授权，应选按 tool_call_id 的单次批准。

## 7. 中等难度考试题（含解析）

1. **题：12 个高风险动作中 9 个得到有效人工许可，3 个未获准，可执行多少？** 解：最多 9 个，且仍须分别验证执行时资源、审批版本和业务权限。
2. **题：审批所见金额 5000、实际提交金额 7000，能直接使用原批准吗？** 解：不能，批准绑定参数发生变化，应拒绝并重新申请。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · HITL](https://openai.github.io/openai-agents-python/human_in_the_loop/)：needs_approval、RunState 与审批持久化。
- [NIST · AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)：治理、监督、风险与测量。
