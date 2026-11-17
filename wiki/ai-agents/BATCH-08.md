# AI Agents · 第 8 批（141–160）学习路径 · 当前仅完成 141–150

> **部分完成说明：**按照权威源词表，本批仍有 20 条。此次用户要求新增 30 篇，故在完整第 7 批 121–140 之外，写完本批 141–150 共 10 篇；剩余 151–160 尚未写作，不标记 ready。仅供内部编辑和审稿，不显示在 GitHub Pages 读者导航。

## 已完成 141–150

状态图（State Graph）允许条件路径与受控循环；Loop Node 负责观察—行动—验收闭环，配置实际超时/次数上界。Fan-out 按任务范围和权限分派，Fan-in 按 task_id/同步规则汇合；Gate Check 在关键写动作前检查授权、证据和真实业务状态。

Multi-Agent System 由多个角色组成，可能通过消息、共享环境或分层调用协同。Specialist Agent 聚焦专用能力；Generalist Agent 支持跨域任务；Manager Agent 常保留面向用户的最终答复，Coordinator Agent 则偏重同步、任务归属、版本冲突和进度协调。这些角色可能有交集，但必须以运行时控制权和工具权限区分，不仅靠角色名称。

## 工程综合案例：多模块软件升级

1. Manager 接到更新请求，将仓库分析拆给多个 Specialist。Coordinator 追踪 task_id、依赖、截止时间。
2. Fan-out 可并行分析前端、数据库和接口，但两个 Worker 不应无协调地写同一配置文件。
3. Fan-in 等待必需的单测、依赖扫描、安全检查，按任务 ID 去重，缺失结果不能当成功。
4. 部署 Gate Check 以实际 CI 结果、部署身份与审批参数为依据。
5. 一次部署超时标记 unknown，通过权威发布系统核对状态，再恢复后续节点。
6. Agent 反馈只作为观测，不自动构成真实业务成功或人员授权。

## 中等难度面试题

**问：**Manager Agent 与 Specialist Handoff 的控制权差异是什么？

**参考答案：**Manager 把 Specialist 当受限工具调用，自己保留用户对话及最终答复；handoff 则将后续部分对话交由专业 Agent 接管。两者都要处理上下文过滤与真实权限检查。

## 中等难度考试题

**题：**30 个任务、每个 2 秒，允许 5 个任务同时执行；全部完成后另需 1 秒汇总。理想情况下总耗时？

**解：**ceil(30/5)×2+1=13 秒，未计队列/调度开销；若任何强制安全检查失败，不能将整体标为成功。

## 后续范围

第 8 批继续编写 **151–160**，从 Worker Agent 开始。未来完成这一半批次时，将整个第 8 批视为 drafted_in_pr；不需更改原 20 条批次大小或已发布索引。

## 主要一手资料

- [LangGraph · Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)
- [LangGraph · Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [OpenAI · Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)
- [OpenAI Agents SDK · Agents](https://openai.github.io/openai-agents-python/agents/)
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)

## 审稿标准

专门核对 graph 循环、fan-in 结果去重、多 Agent 权限/资源隔离与 manager/handoff 控制权。学科专家签核需独立审稿记录；不因为 CI 通过而修改 pending。
