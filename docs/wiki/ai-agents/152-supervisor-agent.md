# Supervisor Agent（监督者智能体）

> AI Agents · 专题：多智能体协作 · 工程角色定义；职责、权限与真实验收依具体系统为准

## 1. 核心定义

**Supervisor Agent（监督者智能体）**：Supervisor Agent（监督者智能体）是持续检查多 Agent 或长时任务的进度、质量、权限边界与异常状态，并在必要时暂停、重试、升级或重新分配任务的角色。它的主要职责是监督控制，而非代替全部 Worker 生产内容。

**适用边界：**监督者不一定是另一个语言模型，确定性监控器、规则引擎与人工审批更适合某些安全规则。监督结论不能越过业务系统的真实授权，也不能简单因任务超时就重复高风险写动作。

## 2. 形象理解

像施工安全监理记录进度、抽查规范和签发停工通知，但不能凭口头报告确认钢筋质量。

**类比的局限：**监督人员可能信息滞后或遗漏，检查通过只说明当前 gate 达标，不能保证所有未来动作安全。

## 3. 技术原理与核心内容

保存 SupervisorState={task_id,owner,deadline,status,heartbeat,quality_metrics,policy_version}，消费 worker events 与工具 trace。规则可以定义 status=stalled、unsafe、pending_review、complete 等分支；重要行动通过独立执行器落实 pause/cancel/approval。对异步任务使用 monotonic status 和 correlation_id，防止旧完成消息覆盖新失败状态。

## 4. 工程实践与设计权衡

**工程案例：**生产部署协调中，监督者检查单测、安全扫描、运行指标与灰度阈值；出现错误率越界立即阻止下一批发布、通知负责人。停止部署需要确认当前实际 rollout ID，而非从日志文本猜测环境。

**失败模式与验证：**监督者和 Worker 使用同一错误证据互相确认，忽略失联 Worker，状态乱序导致失败被覆盖，错误审批规则放行资金操作。测试心跳失联、重复通知、权限拒绝、异常状态转换和版本漂移。

## 5. 关联知识与易混辨析

Supervisor Agent 侧重监控、策略和异常升级；Reviewer Agent 侧重审阅具体交付物；Critic Agent 侧重指出弱点；Manager Agent 保持整体任务分工和用户答复控制，可兼具监督职责。

## 6. 中等难度面试题（含参考答案）

1. **问：Supervisor 是否应自动重试超时的付款 Worker？** 答：不能。必须先查询实际交易状态，再根据幂等保证与用户授权决定是否重试。
2. **问：如何避免模型自评与监督者循环互相背书？** 答：使用独立测试、权威业务数据、清晰 rubric 与审计日志，不能只汇总自然语言成功宣称。

## 7. 中等难度考试题（含解析）

1. **题：一个任务 SLA=30 秒，最早 heartbeat 在 0 秒，之后 10、20 秒，检查时刻 52 秒，按最后 heartbeat 的 30 秒超时判定是否 stalled？** 解：52−20=32 秒，超过 30 秒，因此 stalled；但不能推断实际外部工具未执行。
2. **题：审批 gate 中三项要求全部通过，当前 pass、pass、unknown，可标为 complete 吗？** 解：不可以。unknown 仍需核查，不能从数量多数推断整体完成。

## 8. 权威来源与延伸阅读

- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：编排者—工作者与评估者—优化者工作流。
- [OpenAI Agents SDK · Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)：Manager、agents-as-tools 与 handoffs 区别。
