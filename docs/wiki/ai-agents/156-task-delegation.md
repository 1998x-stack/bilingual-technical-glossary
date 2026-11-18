# Task Delegation（任务委派）

> AI Agents · 专题：多智能体协作 · 多 Agent 协作模式与信任边界；SDK API 以版本文档为准

## 1. 核心定义

**Task Delegation（任务委派）**：Task Delegation（任务委派）是由一个 Agent 或编排器把明确的目标、输入、约束和验收责任分配给另一个 Agent，并跟踪其执行结果的过程。有效委派是受控任务契约，不只是发送一句‘帮我做一下’。

**适用边界：**委派不意味着委派者可扩张被委派者权限，也不总是交出最终对话控制权。一次子任务完成与总任务完成有区别；不可逆副作用要在每一层严格授权。

## 2. 形象理解

像项目负责人给工程师下发带任务号、交付标准和截止日期的工单，工程师完成后回传结果和证据。

**类比的局限：**任务交出并不意味着负责人自动免责，执行者也未必能访问所有项目资料。

## 3. 技术原理与核心内容

构造 Delegation={task_id,requester,assignee,objective,allowed_resources,deadline,output_schema,acceptance_tests}。派工前检查能力与最小权限、数据保密级别、并发文件冲突；接受后保存状态 assigned→running→completed/failed/unknown。回执应携带证据和任务 ID，经理验证后才推进下游。过期委派及重复任务应由 TTL 和 idempotency_key 约束。

## 4. 工程实践与设计权衡

**工程案例：**金融对账 Agent 派发‘核对交易 1001–1100’给只读 Worker，要求返回差异 ID、来源和计算校验；Worker 无权自动发起补款。汇总器发现重复或缺失区间后重新派单，而非把全部工单标为成功。

**失败模式与验证：**含糊目标导致偏离、授予不必要的账户凭据、重复派发同一付款任务、无统一 ID 导致结果串线。测试超时、拒绝委派、失联与重新派发后的外部状态。

## 5. 关联知识与易混辨析

Task Delegation 是子任务职责分配；Handoff 是活跃控制权转移；Agent as Tool 是委派的一种实现；Coordinator Agent 管理委派和同步，但并不一定生产最终结果。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么委派请求应定义验收标准？** 答：否则下游自然语言 done 无法判定实际完成；结构化输出和证据支持是整体成功的必要条件。
2. **问：任务超时后如何安全地重新委派？** 答：先核对外部动作状态，标识原任务/幂等键与资源锁，确保不会双执行或跨授权范围转移。

## 7. 中等难度考试题（含解析）

1. **题：100 个交易按每个 Worker 25 个且区间互斥，至少需要多少个 Worker 任务？** 解：100/25=4 个任务。
2. **题：两个 Agent 被委派同一个 transfer_id 的付款并都发起写入，主要控制缺失是什么？** 解：缺少可靠的委派去重、服务端幂等/原子锁与实际授权控制。

## 8. 权威来源与延伸阅读

- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：子任务拆解与有界委派。
- [OpenAI Agents SDK · Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)：Manager 与 Handoff 设计权衡。
