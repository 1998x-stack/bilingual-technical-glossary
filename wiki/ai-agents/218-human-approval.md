# Human Approval（人工批准）

> AI Agents · 专题：执行状态、持久化与恢复 · 工程事故防护与可恢复性以业务事实为准

## 1. 核心定义

**Human Approval（人工批准）**：Human Approval（人工批准）是指定权限主体针对某个明确的待执行动作、资源、参数和有效期作出允许或拒绝决定，以控制 Agent 触发真实外部副作用。它比一般审核更强调授权动作的范围、有效性和不可越界。

**适用边界：**批准通常不能从自然语言‘没问题’中任意推断，尤其对付款、删库和生产部署。默认只批准当前 tool_call_id/具体资源，除非业务政策明确允许可撤销的更广批准；执行系统仍需服务端 ACL。

## 2. 形象理解

像财务主管批准‘向供应商 A 支付发票 #123 金额 5000 元’，而不是批准‘以后所有供应商随时付款’。

**类比的局限：**主管批准的付款还可能因银行限制失败；批准是前置授权，不是外部事务成功回执。

## 3. 技术原理与核心内容

签核记录 `{approval_id,actor_id,action,resource_id,arguments_hash,policy_version,expires_at,decision}`；执行时验证主体真实身份与权限、目标参数哈希、有效期和是否已撤销，成功后写一次性消费记录。OpenAI Agents SDK 可以通过 `needs_approval=True` 暂停工具调用，`state.approve(interruption)` 单独批准；不同权限的执行器不应复用 global sticky permission，防止批准漂移。

## 4. 工程实践与设计权衡

**工程案例：**运维 Agent 计划回滚生产版本 v4→v3，审批显示环境、受影响租户、目标 image digest 和回滚计划。审批人只允许在指定维护窗口执行；如果目标 digest 更新或窗口过去，须重新批准。

**失败模式与验证：**TOCTOU 参数变化、审批人伪造、过期 token 重放、不同工具同名却共享永远批准状态、实际权限执行器缺二次校验。用参数突变、跨账户操作、审批撤销及重复请求用例验证。

## 5. 关联知识与易混辨析

Human Approval 是对动作的许可；Human Review 关注内容与质量；Human-in-the-loop 是整体介入模式；Gate Check 可用程序、人工或组合决策实现。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么一次 approval 应绑定 arguments_hash？** 答：防止审批展示的金额或资源在执行前悄悄变化，让旧许可放行新动作。
2. **问：审批已经 granted 但执行时用户权限被收回，可以继续吗？** 答：不可以，仍须按执行时的当前身份、资源 ACL 和业务政策验证。

## 7. 中等难度考试题（含解析）

1. **题：最多 5 个付款请求，得到 3 个有效批准、1 个拒绝、1 个 pending，可尝试执行几个？** 解：最多 3 个，还要检查当前有效权限。
2. **题：发起审批时资源 revision=11，执行时=12，按版本绑定应发生什么？** 解：拒绝沿用旧审批，进入复核或重新申请。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · HITL](https://openai.github.io/openai-agents-python/human_in_the_loop/)：needs_approval、RunState 与审批持久化。
- [LangGraph · Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)：人工暂停、Command(resume=...) 和状态检查点。
