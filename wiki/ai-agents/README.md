# AI Agents 深度 Wiki · 内部生产计划

> 权威术语顺序：[AI Agents 中英词表](../../glossaries/ai-agents.md) · **332 条 / 16 专题 / 17 批**。本页只用于编辑、校验和排期，不应出现在公开站点的读者导航。

## 方法与验收

每次只取**连续 20 条**（末批 12 条），逐条完成中文/英文定义及适用边界、形象类比及失效边界、底层机制/数据流、工程案例与权衡、易混概念、**2 道中等面试题和 2 道中等考试题（附完整答案）**、可追溯一手资料。每批单独 PR，评审通过后合并；未写作条目不能标记 ready。

- 源词表：`glossaries/ai-agents.md`；顺序和译名不可凭空调整。
- 长文源稿：`wiki/ai-agents/<NNN>-<slug>.md`；GitHub Pages 镜像：`docs/wiki/ai-agents/`。
- 公开索引：由 `docs/wiki/ai-agents/manifest.json` 与 `scripts/build_wiki_index.py` 生成。读者只使用统一 Explorer 的术语详情，不展示批次表。
- 完成验收：`python scripts/verify_ai_agents_wiki.py`、`python scripts/build_wiki_index.py --check`、`python scripts/verify_wiki_reviews.py --check` 与整库 CI。自动审查不等于专家审稿；`wiki/reviews/ai-agents.json` 的状态保持 pending，直至真实专家审阅。

## 17 批路线图

| 批次 | 编号 | 主题（可能跨专题） | 篇数 | 编辑状态 |
|---|---|---|---:|---|
| 01 | 001–020 | 基础概念与角色 | 20 | drafted_in_pr |
| 02 | 021–040 | 基础概念与角色 / 模型能力与推理 | 20 | drafted_in_pr |
| 03 | 041–060 | 模型能力与推理 / 任务规划与决策 | 20 | drafted_in_pr |
| 04 | 061–080 | 任务规划与决策 / 工具使用与环境交互 | 20 | drafted_in_pr |
| 05 | 081–100 | 工具使用与环境交互 / 上下文、记忆与状态 | 20 | drafted_in_pr |
| 06 | 101–120 | 上下文、记忆与状态 / 检索与知识增强 | 20 | drafted_in_pr |
| 07 | 121–140 | 检索与知识增强 / 工作流与编排模式 | 20 | drafted_in_pr |
| 08 | 141–160 | 工作流与编排模式 / 多智能体协作 | 20 | drafted_in_pr |
| 09 | 161–180 | 多智能体协作 / MCP：模型上下文协议 | 20 | drafted_in_pr |
| 10 | 181–200 | MCP：模型上下文协议 / A2A：智能体间协议 | 20 | drafted_in_pr |
| 11 | 201–220 | A2A：智能体间协议 / 执行状态、持久化与恢复 | 20 | drafted_in_pr |
| 12 | 221–240 | 执行状态、持久化与恢复 / 评测体系与常见基准 | 20 | drafted_in_pr |
| 13 | 241–260 | 评测体系与常见基准 / 安全防护与治理 | 20 | drafted_in_pr |
| 14 | 261–280 | 安全防护与治理 / 智能体攻击与风险 | 20 | 部分 drafted_in_pr（261–270），271–280 planned |
| 15 | 281–300 | 智能体攻击与风险 / 工程化、成本与可观测性 | 20 | planned |
| 16 | 301–320 | 工程化、成本与可观测性 / 开发实践与生态术语 | 20 | planned |
| 17 | 321–332 | 开发实践与生态术语 | 12 | planned |

## 第 1 批知识路径

[第 1 批系统化学习与综合案例](BATCH-01.md)：从 Agent / Agentic System 到 LLM、Framework、Runtime、Loop，再到 Goal、Task、Role、Autonomy、Environment、Observation。

### 已完成候审稿（001–020）

1. [AI Agent（人工智能智能体）](001-ai-agent.md)
2. [Agentic AI（智能体化人工智能）](002-agentic-ai.md)
3. [Agentic System（智能体系统）](003-agentic-system.md)
4. [Large Language Model (LLM)（大语言模型）](004-large-language-model.md)
5. [Foundation Model（基础模型）](005-foundation-model.md)
6. [Agent Framework（智能体框架）](006-agent-framework.md)
7. [Agent Runtime（智能体运行时）](007-agent-runtime.md)
8. [Agent Loop（智能体循环）](008-agent-loop.md)
9. [Goal（目标）](009-goal.md)
10. [Task（任务）](010-task.md)
11. [Subtask（子任务）](011-subtask.md)
12. [Instruction（指令）](012-instruction.md)
13. [System Prompt（系统提示词）](013-system-prompt.md)
14. [User Prompt（用户提示词）](014-user-prompt.md)
15. [Role（角色）](015-role.md)
16. [Capability（能力）](016-capability.md)
17. [Autonomy（自主性）](017-autonomy.md)
18. [Agency（能动性）](018-agency.md)
19. [Environment（环境）](019-environment.md)
20. [Observation（观察）](020-observation.md)

## 第 2 批知识路径

[第 2 批：Action、推理预算、结构化输出与事实校验](BATCH-02.md)：从 Agent 控制逻辑过渡到推理模型，理解结构约束、推理时搜索、工具协作及错误检测。

### 已完成候审稿（021–040）

21. [Action（动作）](021-action.md)
22. [Termination Condition（终止条件）](022-termination-condition.md)
23. [Reasoning Model（推理模型）](023-reasoning-model.md)
24. [Model Invocation（模型调用）](024-model-invocation.md)
25. [Inference-time Compute（推理时计算）](025-inference-time-compute.md)
26. [Test-time Compute（测试时计算）](026-test-time-compute.md)
27. [Context Window（上下文窗口）](027-context-window.md)
28. [Token（词元）](028-token.md)
29. [Token Budget（词元预算）](029-token-budget.md)
30. [Temperature（温度参数）](030-temperature.md)
31. [Structured Output（结构化输出）](031-structured-output.md)
32. [Constrained Decoding（约束解码）](032-constrained-decoding.md)
33. [Function Calling（函数调用）](033-function-calling.md)
34. [Chain of Thought (CoT)（链式思维）](034-chain-of-thought.md)
35. [Tree of Thoughts (ToT)（思维树）](035-tree-of-thoughts.md)
36. [Self-Consistency（自洽性采样）](036-self-consistency.md)
37. [Reasoning and Acting (ReAct)（推理与行动协同）](037-reasoning-and-acting.md)
38. [Reflection（反思）](038-reflection.md)
39. [Self-Correction（自我纠错）](039-self-correction.md)
40. [Hallucination（幻觉）](040-hallucination.md)

## 第 3 批知识路径

[第 3 批：不确定性与置信校准 → 规划 → 决策理论与前瞻搜索](BATCH-03.md)：从 2 个模型评估条目进入 18 个任务规划与决策条目，特别区分概率估计、执行权限与真正业务完成。

### 已完成候审稿（041–060）

41. [Uncertainty（不确定性）](041-uncertainty.md)
42. [Confidence Calibration（置信度校准）](042-confidence-calibration.md)
43. [Planning（规划）](043-planning.md)
44. [Task Decomposition（任务分解）](044-task-decomposition.md)
45. [Hierarchical Planning（分层规划）](045-hierarchical-planning.md)
46. [High-level Plan（高层计划）](046-high-level-plan.md)
47. [Action Plan（行动计划）](047-action-plan.md)
48. [Adaptive Planning（自适应规划）](048-adaptive-planning.md)
49. [Plan Revision（计划修订）](049-plan-revision.md)
50. [Task Dependency（任务依赖）](050-task-dependency.md)
51. [Task Priority（任务优先级）](051-task-priority.md)
52. [Decision Point（决策点）](052-decision-point.md)
53. [Action Space（行动空间）](053-action-space.md)
54. [State Space（状态空间）](054-state-space.md)
55. [Policy（策略）](055-policy.md)
56. [Utility Function（效用函数）](056-utility-function.md)
57. [Reward Signal（奖励信号）](057-reward-signal.md)
58. [Search Space（搜索空间）](058-search-space.md)
59. [Heuristic Search（启发式搜索）](059-heuristic-search.md)
60. [Lookahead Search（前瞻搜索）](060-lookahead-search.md)

## 第 4 批知识路径

[第 4 批：从回溯/重规划到工具发现、调用、计算机使用及适配](BATCH-04.md)：3 条规划决策概念 + 17 条工具与环境交互概念，重点校验工具反馈、权限、提示注入与外部副作用。

### 已完成候审稿（061–080）

61. [Backtracking（回溯）](061-backtracking.md)
62. [Replanning（重规划）](062-replanning.md)
63. [Stopping Criterion（停止准则）](063-stopping-criterion.md)
64. [Tool（工具）](064-tool.md)
65. [Tool Call（工具调用）](065-tool-call.md)
66. [Tool Result（工具结果）](066-tool-result.md)
67. [Tool Selection（工具选择）](067-tool-selection.md)
68. [Tool Routing（工具路由）](068-tool-routing.md)
69. [Tool Schema（工具模式）](069-tool-schema.md)
70. [Argument Validation（参数校验）](070-argument-validation.md)
71. [Tool Discovery（工具发现）](071-tool-discovery.md)
72. [Tool Registry（工具注册表）](072-tool-registry.md)
73. [Function Tool（函数工具）](073-function-tool.md)
74. [Web Search Tool（网络搜索工具）](074-web-search-tool.md)
75. [Browser Automation（浏览器自动化）](075-browser-automation.md)
76. [Computer Use（计算机使用）](076-computer-use.md)
77. [Code Execution（代码执行）](077-code-execution.md)
78. [Command-line Tool (CLI)（命令行工具）](078-command-line-tool.md)
79. [Application Programming Interface (API)（应用程序接口）](079-application-programming-interface.md)
80. [Tool Adapter（工具适配器）](080-tool-adapter.md)

## 第 5 批知识路径

[第 5 批：外部工具恢复、上下文工程与记忆体系](BATCH-05.md)：从 Environment Feedback、Tool Retry 和幂等性出发，跨入 Context Engineering、会话状态及语义/情景/程序性长期记忆与检索，重点检验时效、证据与权限边界。

### 已完成候审稿（081–100）

81. [Environment Feedback（环境反馈）](081-environment-feedback.md)
82. [Tool Retry（工具调用重试）](082-tool-retry.md)
83. [Side Effect（副作用）](083-side-effect.md)
84. [Idempotent Operation（幂等操作）](084-idempotent-operation.md)
85. [Sensitive Action（敏感操作）](085-sensitive-action.md)
86. [Context（上下文）](086-context.md)
87. [Context Engineering（上下文工程）](087-context-engineering.md)
88. [Prompt Engineering（提示词工程）](088-prompt-engineering.md)
89. [Context Injection（上下文注入）](089-context-injection.md)
90. [Context Compression（上下文压缩）](090-context-compression.md)
91. [Conversation History（对话历史）](091-conversation-history.md)
92. [Session（会话）](092-session.md)
93. [Session State（会话状态）](093-session-state.md)
94. [Working Memory（工作记忆）](094-working-memory.md)
95. [Short-term Memory（短期记忆）](095-short-term-memory.md)
96. [Long-term Memory（长期记忆）](096-long-term-memory.md)
97. [Episodic Memory（情景记忆）](097-episodic-memory.md)
98. [Semantic Memory（语义记忆）](098-semantic-memory.md)
99. [Procedural Memory（程序性记忆）](099-procedural-memory.md)
100. [Memory Retrieval（记忆检索）](100-memory-retrieval.md)

## 第 6 批知识路径

[第 6 批：Memory Lifecycle / 状态恢复 → RAG 检索链路](BATCH-06.md)：从长期记忆的写入、巩固、遗忘与恢复，过渡到知识库摄取、切分、Embedding、向量/关键词/混合检索、重排序和查询改写。

### 已完成候审稿（101–120）

101. [Memory Write（记忆写入）](101-memory-write.md)
102. [Memory Consolidation（记忆巩固）](102-memory-consolidation.md)
103. [Memory Forgetting（记忆遗忘）](103-memory-forgetting.md)
104. [State Snapshot（状态快照）](104-state-snapshot.md)
105. [State Restoration（状态恢复）](105-state-restoration.md)
106. [User Preference（用户偏好）](106-user-preference.md)
107. [Retrieval-Augmented Generation (RAG)（检索增强生成）](107-retrieval-augmented-generation.md)
108. [Agentic Retrieval（智能体式检索）](108-agentic-retrieval.md)
109. [Knowledge Base (KB)（知识库）](109-knowledge-base.md)
110. [Document Ingestion（文档摄取）](110-document-ingestion.md)
111. [Chunking（文本切分）](111-chunking.md)
112. [Chunk（文本块）](112-chunk.md)
113. [Embedding（嵌入向量）](113-embedding.md)
114. [Vector Database（向量数据库）](114-vector-database.md)
115. [Vector Search（向量检索）](115-vector-search.md)
116. [Semantic Search（语义检索）](116-semantic-search.md)
117. [Keyword Search（关键词检索）](117-keyword-search.md)
118. [Hybrid Search（混合检索）](118-hybrid-search.md)
119. [Reranking（重排序）](119-reranking.md)
120. [Query Rewriting（查询改写）](120-query-rewriting.md)

## 第 7 批知识路径（121–140 · 20 篇）

[第 7 批：多跳检索、证据链与工作流编排](BATCH-07.md)：已完整完成第 7 批的 20 篇候审稿。第 8 批前 10 篇同属本次用户指定的 30 篇增量。

### 已完成候审稿（121–140）

121. [Multi-hop Retrieval（多跳检索）](121-multi-hop-retrieval.md)
122. [Knowledge Graph (KG)（知识图谱）](122-knowledge-graph.md)
123. [Source Attribution（来源归因）](123-source-attribution.md)
124. [Evidence Chain（证据链）](124-evidence-chain.md)
125. [Workflow（工作流）](125-workflow.md)
126. [Agent Orchestration（智能体编排）](126-agent-orchestration.md)
127. [Chaining（链式处理）](127-chaining.md)
128. [Prompt Chaining（提示链）](128-prompt-chaining.md)
129. [Routing Pattern（路由模式）](129-routing-pattern.md)
130. [Parallelization（并行化）](130-parallelization.md)
131. [Aggregation Pattern（汇总模式）](131-aggregation-pattern.md)
132. [Orchestrator–Workers（编排者—工作者模式）](132-orchestrator-workers.md)
133. [Evaluator–Optimizer（评估者—优化者模式）](133-evaluator-optimizer.md)
134. [Plan-and-Execute（计划后执行）](134-plan-and-execute.md)
135. [Reactive Execution（反应式执行）](135-reactive-execution.md)
136. [Sequential Execution（顺序执行）](136-sequential-execution.md)
137. [Conditional Branch（条件分支）](137-conditional-branch.md)
138. [Control Flow（控制流）](138-control-flow.md)
139. [Data Flow（数据流）](139-data-flow.md)
140. [Directed Acyclic Graph (DAG)（有向无环图）](140-directed-acyclic-graph.md)

## 第 8 批知识路径（141–160 · 完整 20 篇）

[第 8 批：状态图、扇出扇入与多 Agent](BATCH-08.md)：在本轮补齐 151–160，现已完成整个第 8 批 20 篇候审稿；各篇仍 pending 专家审稿。

### 已完成候审稿（141–150）

141. [State Graph（状态图）](141-state-graph.md)
142. [Loop Node（循环节点）](142-loop-node.md)
143. [Fan-out（扇出）](143-fan-out.md)
144. [Fan-in（扇入）](144-fan-in.md)
145. [Gate Check（门控检查）](145-gate-check.md)
146. [Multi-Agent System (MAS)（多智能体系统）](146-multi-agent-system.md)
147. [Specialist Agent（专业智能体）](147-specialist-agent.md)
148. [Generalist Agent（通用智能体）](148-generalist-agent.md)
149. [Manager Agent（管理者智能体）](149-manager-agent.md)
150. [Coordinator Agent（协调者智能体）](150-coordinator-agent.md)

### 补齐第 8 批（151–160）

151. [Worker Agent（工作者智能体）](151-worker-agent.md)
152. [Supervisor Agent（监督者智能体）](152-supervisor-agent.md)
153. [Reviewer Agent（审查者智能体）](153-reviewer-agent.md)
154. [Critic Agent（批评者智能体）](154-critic-agent.md)
155. [Inter-Agent Communication（代理间通信）](155-inter-agent-communication.md)
156. [Task Delegation（任务委派）](156-task-delegation.md)
157. [Handoff（控制权交接）](157-handoff.md)
158. [Agent as Tool（智能体即工具）](158-agent-as-tool.md)
159. [Shared Memory（共享记忆）](159-shared-memory.md)
160. [Blackboard（共享黑板）](160-blackboard.md)

## 第 9 批知识路径（161–180 · 完整 20 篇）

[第 9 批：多 Agent 消息与协作故障 → MCP 2026-07-28 协议考古](BATCH-09.md)：前六篇聚焦通信总线、共识、冲突与交接；后十四篇涵盖 MCP 基础角色、工具资源、协议发现、版本/能力协商、JSON-RPC 和 stdio，并明确 2025-11-25 与 2026-07-28 生命周期差异。

### 已完成候审稿（161–180）

161. [Message Bus（消息总线）](161-message-bus.md)
162. [Consensus（共识）](162-consensus.md)
163. [Conflict Resolution（冲突解决）](163-conflict-resolution.md)
164. [Role Specialization（角色分工）](164-role-specialization.md)
165. [Handoff Record（任务交接记录）](165-handoff-record.md)
166. [Coordination Failure（协作失效）](166-coordination-failure.md)
167. [Model Context Protocol (MCP)（模型上下文协议）](167-model-context-protocol.md)
168. [MCP Host（MCP 主机）](168-mcp-host.md)
169. [MCP Client（MCP 客户端）](169-mcp-client.md)
170. [MCP Server（MCP 服务器）](170-mcp-server.md)
171. [MCP Tool（MCP 工具）](171-mcp-tool.md)
172. [MCP Resource（MCP 资源）](172-mcp-resource.md)
173. [MCP Prompt（MCP 提示模板）](173-mcp-prompt.md)
174. [Resource URI (URI)（资源标识符）](174-resource-uri.md)
175. [Tool Listing (tools/list)（工具列表）](175-tool-listing.md)
176. [Tool Invocation (tools/call)（工具执行）](176-tool-invocation.md)
177. [Capability Negotiation（能力协商）](177-capability-negotiation.md)
178. [Protocol Version Negotiation（协议版本协商）](178-protocol-version-negotiation.md)
179. [JSON-RPC（JSON 远程过程调用）](179-json-rpc.md)
180. [Standard Input/Output Transport (stdio)（标准输入输出传输）](180-standard-input-output-transport.md)

## 第 10 批（181–200 · 完整 20 篇）

[第 10 批学习路径：MCP 2026 传输与扩展 → A2A Agent Card、Task、Message](BATCH-10.md)：来源优先核验 2026-07-28 MCP 与 A2A 正式规范，区分 Sampling/Roots 弃用状态及 Elicitation MRTR。

181. [Streamable HTTP Transport（流式 HTTP 传输）](181-streamable-http-transport.md)
182. [Sampling（采样请求）](182-sampling.md)
183. [Elicitation（用户信息征询）](183-elicitation.md)
184. [Roots（根目录）](184-roots.md)
185. [Completion（参数自动补全）](185-completion.md)
186. [Progress Notification（进度通知）](186-progress-notification.md)
187. [Cancellation Notification（取消通知）](187-cancellation-notification.md)
188. [Authorization（授权）](188-authorization.md)
189. [MCP Extension（MCP 扩展）](189-mcp-extension.md)
190. [MCP Apps（MCP 应用）](190-mcp-apps.md)
191. [Agent2Agent Protocol (A2A)（智能体间协议）](191-agent2agent-protocol.md)
192. [A2A Client（A2A 客户端）](192-a2a-client.md)
193. [A2A Server（A2A 服务器）](193-a2a-server.md)
194. [Remote Agent（远程智能体）](194-remote-agent.md)
195. [Agent Card（智能体名片）](195-agent-card.md)
196. [Agent Discovery（智能体发现）](196-agent-discovery.md)
197. [Agent Skill（智能体技能）](197-agent-skill.md)
198. [A2A Task（A2A 任务）](198-a2a-task.md)
199. [A2A Message（A2A 消息）](199-a2a-message.md)
200. [Message Part（消息片段）](200-message-part.md)

## 第 11 批（201–220 · 完整 20 篇）

[第 11 批学习路径：A2A Artifact → 状态机、持久执行与人工审批](BATCH-11.md)：本轮补齐 211–220，20 篇候审稿已完整成稿，专家审核仍 pending。

201. [Artifact（任务产物）](201-artifact.md)
202. [Task State（任务状态）](202-task-state.md)
203. [Task Lifecycle（任务生命周期）](203-task-lifecycle.md)
204. [Streaming Update（流式更新）](204-streaming-update.md)
205. [Push Notification（推送通知）](205-push-notification.md)
206. [Interoperability（互操作性）](206-interoperability.md)
207. [Capability Declaration（能力声明）](207-capability-declaration.md)
208. [Task Delegation Protocol（任务委派协议）](208-task-delegation-protocol.md)
209. [State Machine（状态机）](209-state-machine.md)
210. [Checkpoint（检查点）](210-checkpoint.md)

### 第 11 批本轮补齐（211–220）

211. [Checkpointing（检查点保存）](211-checkpointing.md)
212. [Persistence（持久化）](212-persistence.md)
213. [Durable Execution（持久执行）](213-durable-execution.md)
214. [Interrupt（中断）](214-interrupt.md)
215. [Resume Execution（恢复执行）](215-resume-execution.md)
216. [Human-in-the-loop (HITL)（人工介入）](216-human-in-the-loop.md)
217. [Human Review（人工审核）](217-human-review.md)
218. [Human Approval（人工批准）](218-human-approval.md)
219. [Recoverable Error（可恢复错误）](219-recoverable-error.md)
220. [Retry Policy（重试策略）](220-retry-policy.md)

## 第 12 批（221–240 · 完整 20 篇）

[第 12 批学习路径：恢复机制与评测基准](BATCH-12.md)：涵盖重试、事务/日志、Agent 评测、轨迹、忠实度和事实准确性；本批 20 篇长文全部候审。

221. [Exponential Backoff（指数退避）](221-exponential-backoff.md)
222. [Timeout（超时）](222-timeout.md)
223. [Deadline（截止期限）](223-deadline.md)
224. [Failover（故障转移）](224-failover.md)
225. [Compensating Action（补偿操作）](225-compensating-action.md)
226. [Transaction Boundary（事务边界）](226-transaction-boundary.md)
227. [Execution Log（执行日志）](227-execution-log.md)
228. [Agent Evaluation（智能体评测）](228-agent-evaluation.md)
229. [Benchmark（评测基准）](229-benchmark.md)
230. [Evaluation Dataset (Eval Set)（评测集）](230-evaluation-dataset.md)
231. [Task Success Rate（任务成功率）](231-task-success-rate.md)
232. [End-to-end Success Rate（端到端成功率）](232-end-to-end-success-rate.md)
233. [Tool-call Accuracy（工具调用正确率）](233-tool-call-accuracy.md)
234. [Action Success Rate（动作成功率）](234-action-success-rate.md)
235. [Trajectory Evaluation（轨迹评测）](235-trajectory-evaluation.md)
236. [Trajectory（轨迹）](236-trajectory.md)
237. [Outcome Evaluation（结果评测）](237-outcome-evaluation.md)
238. [Process Evaluation（过程评测）](238-process-evaluation.md)
239. [Faithfulness（忠实度）](239-faithfulness.md)
240. [Factual Accuracy（事实准确性）](240-factual-accuracy.md)

## 第 13 批（241–260 · 完整 20 篇）

[第 13 批学习路径：Agent Benchmark → Guardrail → PoLP/AuthN/AuthZ](BATCH-13.md)：覆盖 GAIA、SWE-bench、WebArena、OSWorld、τ-bench、BFCL V4 以及模型评分器的偏差控制、执行层授权。

241. [Robustness（鲁棒性）](241-robustness.md)
242. [Reproducibility（可复现性）](242-reproducibility.md)
243. [LLM-as-a-Judge（评判模型）](243-llm-as-a-judge.md)
244. [Ground Truth（黄金答案）](244-ground-truth.md)
245. [Human Annotation（人工标注）](245-human-annotation.md)
246. [Regression Test（回归测试）](246-regression-test.md)
247. [Scenario-based Evaluation（基于场景的评测）](247-scenario-based-evaluation.md)
248. [GAIA（GAIA 基准）](248-gaia.md)
249. [SWE-bench（SWE-bench）](249-swe-bench.md)
250. [WebArena（WebArena）](250-webarena.md)
251. [OSWorld（OSWorld）](251-osworld.md)
252. [tau-bench（τ-bench）](252-tau-bench.md)
253. [Berkeley Function Calling Leaderboard (BFCL)（伯克利函数调用榜单）](253-berkeley-function-calling-leaderboard.md)
254. [Guardrail（护栏）](254-guardrail.md)
255. [Policy Constraint（策略约束）](255-policy-constraint.md)
256. [Principle of Least Privilege (PoLP)（最小权限原则）](256-principle-of-least-privilege.md)
257. [Permission Scope（权限范围）](257-permission-scope.md)
258. [Access Control（访问控制）](258-access-control.md)
259. [Authentication (AuthN)（身份认证）](259-authentication.md)
260. [Authorization (AuthZ)（访问授权）](260-authorization.md)

## 第 14 批（261–280 · 已完成前 10 篇）

[第 14 批学习路径：Sandbox → Trust Boundary → Prompt Injection](BATCH-14.md)：本轮完成 261–270；**271–280 仍 planned，不应标记 ready**。第 14 批继续保留 20 条/批的原始计划。

261. [Sandbox（沙箱）](261-sandbox.md)
262. [Safety Confirmation（安全确认）](262-safety-confirmation.md)
263. [Human Oversight（人类监督）](263-human-oversight.md)
264. [Refusal（拒绝执行）](264-refusal.md)
265. [Safe Fallback（安全回退）](265-safe-fallback.md)
266. [Audit Trail（审计跟踪）](266-audit-trail.md)
267. [Security Boundary（安全边界）](267-security-boundary.md)
268. [Trust Boundary（信任边界）](268-trust-boundary.md)
269. [Data Minimization（数据最小化）](269-data-minimization.md)
270. [Prompt Injection（提示词注入）](270-prompt-injection.md)

## 人工审稿要求

逐篇检查来源与论断匹配、算例的数学步骤、技术版本与安全边界；对任何需修改事实的文章保留改动记录。分支存在候审稿不等于已经合并，也不等于经过独立专家认证。
