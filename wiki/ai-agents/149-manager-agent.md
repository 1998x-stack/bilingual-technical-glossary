# Manager Agent（管理者智能体）

> AI Agents · 专题：多智能体协作 · 多智能体角色和可复核的工程能力边界

## 1. 核心定义

**Manager Agent（管理者智能体）**：Manager Agent（管理者智能体）是在多智能体系统中保留对总体任务、子 Agent 调用及最终输出负责权的角色。它通常选择专业 Agent 作为工具、核对其输出并向用户给出统一结果；这与真正将控制权交给专业 Agent 的 handoff 模式不同。

**适用边界：**Manager Agent 不是企业管理权限的来源，其工具授权仍以可信系统身份为准。集中管理可提高统一审计和责任清晰度，但也可能形成延迟/上下文瓶颈。

## 2. 形象理解

像项目负责人安排专家调查，自己核对交付清单与结论并向客户做最终汇报。

**类比的局限：**负责人收集了报告不代表报告里所有事实正确，也不意味有权绕过专家的保密要求。

## 3. 技术原理与核心内容

在 agents-as-tools 架构中 Manager 调用 specialist.as_tool(task,context_subset)，等待工具式结果、保留 conversation owner，再进行 synthesis 和 final verification。必须传递最小化上下文和明确任务 scope，设置 max_delegations、cost_budget、timeout。经理还要在汇总时区分已验证事实、未经确认的下游陈述与执行器真实事务状态。

## 4. 工程实践与设计权衡

**工程案例：**客户服务平台中的 Manager 负责用户回复，分别调用账单查询和配送查询两个 Specialist，合并已确认的信息后答复；若需要退款，则必须走独立审批工具，不因下游 Agent 说‘可以退款’就越过执行层。

**失败模式与验证：**经理将完整私人聊天发送给无关 Agent、反复委派导致 token 暴涨、多个 Worker 相互矛盾时只采纳最先返回者、统一安全门控被错误绕开。以 trace、汇总证据与任务成功率评估。

## 5. 关联知识与易混辨析

Manager Agent 保留最终答复和委派控制；Coordinator Agent 偏重协作同步与任务对接；Orchestrator–Workers 是动态拆分的整体模式；Handoff 会转移活跃对话所有权。

## 6. 中等难度面试题（含参考答案）

1. **问：Manager 模式与 handoff 的最重要差别？** 答：Manager 保持面向用户的控制并把子 Agent 当受限工具；handoff 将该部分对话的活跃控制交给 Specialist。
2. **问：Manager 对专家回答进行整合，如何防止虚构‘已完成’？** 答：用权威工具状态、任务 ID 和后置条件验证，不把 Specialist 的自然语言自评当外部事实。

## 7. 中等难度考试题（含解析）

1. **题：Manager 调用两个 Specialist，耗时 1.2、2.0 秒，理想并行且汇总 0.5 秒，总时延？** 解：max(1.2,2.0)+0.5=2.5 秒；未计调度开销。
2. **题：下游账单 Agent 只返回 pending，而 Manager 输出‘退款成功’，核心错误？** 解：未验证真实账务终态，把等待中误判为成功；需要保持 pending 并查事务。

## 8. 权威来源与延伸阅读

- [OpenAI · Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)：经理保留最终响应控制与专家交接模式。
- [OpenAI Agents SDK · Agents](https://openai.github.io/openai-agents-python/agents/)：Agent 配置、工具与 handoff。
