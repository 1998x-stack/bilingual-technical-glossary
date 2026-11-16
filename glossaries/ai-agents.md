# AI 智能体 · AI Agents

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：332 条 · 专题：16 类**

Planning, tools, protocols, memory and multi-agent systems

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 基础概念与角色（22 条）
- 02. 模型能力与推理（20 条）
- 03. 任务规划与决策（21 条）
- 04. 工具使用与环境交互（22 条）
- 05. 上下文、记忆与状态（21 条）
- 06. 检索与知识增强（18 条）
- 07. 工作流与编排模式（21 条）
- 08. 多智能体协作（21 条）
- 09. MCP：模型上下文协议（24 条）
- 10. A2A：智能体间协议（18 条）
- 11. 执行状态、持久化与恢复（19 条）
- 12. 评测体系与常见基准（26 条）
- 13. 安全防护与治理（16 条）
- 14. 智能体攻击与风险（16 条）
- 15. 工程化、成本与可观测性（26 条）
- 16. 开发实践与生态术语（21 条）

---

## 01. 基础概念与角色

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | AI Agent | 人工智能智能体 |  | 能感知环境、选择行动并朝目标推进的系统 |
| 2 | Agentic AI | 智能体化人工智能 |  | 强调自主决策、规划与行动能力的 AI 系统形态 |
| 3 | Agentic System | 智能体系统 |  | 由模型、状态、工具、执行逻辑等共同构成的完整系统 |
| 4 | Large Language Model (LLM) | 大语言模型 | LLM | 以语言建模为核心，可充当智能体决策引擎 |
| 5 | Foundation Model | 基础模型 |  | 可适配多种下游任务的通用预训练模型 |
| 6 | Agent Framework | 智能体框架 |  | 封装模型、工具、状态、流程等开发能力的软件框架 |
| 7 | Agent Runtime | 智能体运行时 |  | 负责执行、调度、状态维护及资源控制的运行环境 |
| 8 | Agent Loop | 智能体循环 |  | 决策、执行、观察、更新状态的迭代过程 |
| 9 | Goal | 目标 |  | 智能体希望达成的最终结果或约束条件 |
| 10 | Task | 任务 |  | 可以分配、执行和验收的工作单元 |
| 11 | Subtask | 子任务 |  | 从上层任务拆分出的较小工作单元 |
| 12 | Instruction | 指令 |  | 影响模型或智能体行为的明确要求 |
| 13 | System Prompt | 系统提示词 |  | 应用为模型设定的高优先级行为指引 |
| 14 | User Prompt | 用户提示词 |  | 用户提出的需求或输入内容 |
| 15 | Role | 角色 |  | 智能体在业务或协作体系中的职责定位 |
| 16 | Capability | 能力 |  | 智能体可完成的操作或任务范围 |
| 17 | Autonomy | 自主性 |  | 不依赖每一步人工决策而自行推进的程度 |
| 18 | Agency | 能动性 |  | 为实现目标作出选择并影响环境的能力 |
| 19 | Environment | 环境 |  | 智能体获取反馈、采取行动所处的外部世界 |
| 20 | Observation | 观察 |  | 来自工具、用户或环境的输入反馈 |
| 21 | Action | 动作 |  | 改变状态或取得信息的具体操作 |
| 22 | Termination Condition | 终止条件 |  | 决定智能体何时停止继续执行的规则 |

## 02. 模型能力与推理

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Reasoning Model | 推理模型 |  | 为复杂推断和多步问题求解而优化的模型 |
| 2 | Model Invocation | 模型调用 |  | 向模型发送输入并接收响应的过程 |
| 3 | Inference-time Compute | 推理时计算 |  | 模型生成答案阶段所消耗的计算资源 |
| 4 | Test-time Compute | 测试时计算 |  | 推理阶段为提高表现所增加的计算预算 |
| 5 | Context Window | 上下文窗口 |  | 单次模型处理输入与输出的容量范围 |
| 6 | Token | 词元 |  | 模型编码和计费时常用的文本基本单位 |
| 7 | Token Budget | 词元预算 |  | 预留给输入、输出或内部处理的词元配额 |
| 8 | Temperature | 温度参数 |  | 控制输出采样随机性的参数 |
| 9 | Structured Output | 结构化输出 |  | 按预设结构返回结果，例如符合 JSON Schema |
| 10 | Constrained Decoding | 约束解码 |  | 在生成时限制可输出的格式或词元 |
| 11 | Function Calling | 函数调用 |  | 模型按约定格式请求执行外部函数的机制 |
| 12 | Chain of Thought (CoT) | 链式思维 | CoT | 通过中间推理步骤改善复杂任务的提示方法 |
| 13 | Tree of Thoughts (ToT) | 思维树 | ToT | 探索并评估多条候选推理路径的思考方法 |
| 14 | Self-Consistency | 自洽性采样 |  | 聚合多条推理路径的结论以增强稳健性 |
| 15 | Reasoning and Acting (ReAct) | 推理与行动协同 | ReAct | 交替进行推理与外部行动的经典智能体模式 |
| 16 | Reflection | 反思 |  | 依据执行结果评估并修正先前策略 |
| 17 | Self-Correction | 自我纠错 |  | 根据错误信号自行修订输出或行动 |
| 18 | Hallucination | 幻觉 |  | 生成缺乏足够依据或与事实不符的内容 |
| 19 | Uncertainty | 不确定性 |  | 模型或系统对结果可靠性存在的未知程度 |
| 20 | Confidence Calibration | 置信度校准 |  | 使置信度与实际正确率更一致 |

## 03. 任务规划与决策

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Planning | 规划 |  | 为完成目标制定后续行动序列的过程 |
| 2 | Task Decomposition | 任务分解 |  | 将复杂目标拆解为可执行步骤 |
| 3 | Hierarchical Planning | 分层规划 |  | 在不同粒度上组织目标、计划与动作 |
| 4 | High-level Plan | 高层计划 |  | 定义总体方向和主要阶段的计划 |
| 5 | Action Plan | 行动计划 |  | 明确具体步骤、依赖与执行顺序的计划 |
| 6 | Adaptive Planning | 自适应规划 |  | 根据环境反馈持续调整后续行动 |
| 7 | Plan Revision | 计划修订 |  | 因失败、反馈或变化而修改计划 |
| 8 | Task Dependency | 任务依赖 |  | 一个任务必须等待其他任务完成的约束 |
| 9 | Task Priority | 任务优先级 |  | 在资源有限时对任务执行顺序排序 |
| 10 | Decision Point | 决策点 |  | 需要在若干候选行动中选择的节点 |
| 11 | Action Space | 行动空间 |  | 智能体可选择执行的动作集合 |
| 12 | State Space | 状态空间 |  | 任务或环境可能处于的状态集合 |
| 13 | Policy | 策略 |  | 将观察或状态映射为行动的规则 |
| 14 | Utility Function | 效用函数 |  | 刻画不同结果偏好或收益的函数 |
| 15 | Reward Signal | 奖励信号 |  | 用于反馈行动价值或目标达成程度的信号 |
| 16 | Search Space | 搜索空间 |  | 需要探索的可能方案集合 |
| 17 | Heuristic Search | 启发式搜索 |  | 利用经验评价加快候选方案探索 |
| 18 | Lookahead Search | 前瞻搜索 |  | 评估未来若干步结果再做当前选择 |
| 19 | Backtracking | 回溯 |  | 发现当前路径不佳时退回并尝试其他路径 |
| 20 | Replanning | 重规划 |  | 环境变化或执行失败后重新形成计划 |
| 21 | Stopping Criterion | 停止准则 |  | 由时间、成本、成功或安全约束决定是否停止 |

## 04. 工具使用与环境交互

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Tool | 工具 |  | 智能体可调用的外部能力或操作接口 |
| 2 | Tool Call | 工具调用 |  | 向某一工具提交参数并请求执行 |
| 3 | Tool Result | 工具结果 |  | 工具执行后返回的内容、状态或错误 |
| 4 | Tool Selection | 工具选择 |  | 根据任务需求决定调用哪个工具 |
| 5 | Tool Routing | 工具路由 |  | 将调用请求分派给匹配的工具或执行器 |
| 6 | Tool Schema | 工具模式 |  | 描述工具名称、参数、类型及约束的结构 |
| 7 | Argument Validation | 参数校验 |  | 验证工具入参格式、类型和取值范围 |
| 8 | Tool Discovery | 工具发现 |  | 动态查找可用工具与能力的过程 |
| 9 | Tool Registry | 工具注册表 |  | 集中登记和检索工具定义的目录 |
| 10 | Function Tool | 函数工具 |  | 以函数形式暴露给智能体的可调用能力 |
| 11 | Web Search Tool | 网络搜索工具 |  | 检索公开网页内容的外部工具 |
| 12 | Browser Automation | 浏览器自动化 |  | 通过浏览器操作网页的自动化方式 |
| 13 | Computer Use | 计算机使用 |  | 通过屏幕、鼠标、键盘等操作图形界面 |
| 14 | Code Execution | 代码执行 |  | 在受控环境中运行程序以求解或处理数据 |
| 15 | Command-line Tool (CLI) | 命令行工具 | CLI | 通过终端命令完成操作的工具 |
| 16 | Application Programming Interface (API) | 应用程序接口 | API | 软件系统间约定的调用接口 |
| 17 | Tool Adapter | 工具适配器 |  | 封装不同服务接口差异的连接组件 |
| 18 | Environment Feedback | 环境反馈 |  | 外部操作对真实状态的响应 |
| 19 | Tool Retry | 工具调用重试 |  | 在特定失败条件下重新执行调用 |
| 20 | Side Effect | 副作用 |  | 读取结果以外对外部状态产生的改变 |
| 21 | Idempotent Operation | 幂等操作 |  | 重复执行不引入额外状态变化的操作 |
| 22 | Sensitive Action | 敏感操作 |  | 涉及财务、权限、删除等较高风险的操作 |

## 05. 上下文、记忆与状态

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Context | 上下文 |  | 模型当前可利用的任务、对话与外部信息 |
| 2 | Context Engineering | 上下文工程 |  | 设计、选择、组织和更新模型输入信息 |
| 3 | Prompt Engineering | 提示词工程 |  | 设计提示内容以引导模型完成任务 |
| 4 | Context Injection | 上下文注入 |  | 向当前模型输入补充检索或业务信息 |
| 5 | Context Compression | 上下文压缩 |  | 在尽量保留关键内容时缩减输入体量 |
| 6 | Conversation History | 对话历史 |  | 按时序保存的用户和智能体交互记录 |
| 7 | Session | 会话 |  | 承载一段持续交互及其状态的逻辑范围 |
| 8 | Session State | 会话状态 |  | 当前会话中维护的变量和执行上下文 |
| 9 | Working Memory | 工作记忆 |  | 当前任务短期需要的信息集合 |
| 10 | Short-term Memory | 短期记忆 |  | 用于近期任务或会话的临时信息 |
| 11 | Long-term Memory | 长期记忆 |  | 跨任务或跨会话保留的信息 |
| 12 | Episodic Memory | 情景记忆 |  | 记录特定经历、事件及其结果的记忆 |
| 13 | Semantic Memory | 语义记忆 |  | 以事实、概念和知识为核心的记忆 |
| 14 | Procedural Memory | 程序性记忆 |  | 保存做事步骤、策略与技能的记忆 |
| 15 | Memory Retrieval | 记忆检索 |  | 按当前目标取回相关记忆内容 |
| 16 | Memory Write | 记忆写入 |  | 将新信息保存至记忆存储 |
| 17 | Memory Consolidation | 记忆巩固 |  | 整理、去重或概括既有记忆 |
| 18 | Memory Forgetting | 记忆遗忘 |  | 根据规则删除或降权不再有用的信息 |
| 19 | State Snapshot | 状态快照 |  | 特定时刻的任务或运行状态副本 |
| 20 | State Restoration | 状态恢复 |  | 从已保存的状态继续运行 |
| 21 | User Preference | 用户偏好 |  | 用户长期或临时表达的风格与约束偏好 |

## 06. 检索与知识增强

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Retrieval-Augmented Generation (RAG) | 检索增强生成 | RAG | 先获取相关外部信息，再据此生成答案 |
| 2 | Agentic Retrieval | 智能体式检索 |  | 由智能体动态规划查询和检索路径 |
| 3 | Knowledge Base (KB) | 知识库 | KB | 组织保存领域事实或文档的系统 |
| 4 | Document Ingestion | 文档摄取 |  | 将文档解析并纳入检索系统的过程 |
| 5 | Chunking | 文本切分 |  | 将长文档分解为较小检索单元 |
| 6 | Chunk | 文本块 |  | 切分后的一段可索引内容 |
| 7 | Embedding | 嵌入向量 |  | 将文本等内容编码为稠密向量表示 |
| 8 | Vector Database | 向量数据库 |  | 存储和检索向量表示的数据系统 |
| 9 | Vector Search | 向量检索 |  | 依据向量相似性寻找候选内容 |
| 10 | Semantic Search | 语义检索 |  | 根据语义相关性而非仅字面匹配检索 |
| 11 | Keyword Search | 关键词检索 |  | 基于词项匹配的搜索方式 |
| 12 | Hybrid Search | 混合检索 |  | 组合语义检索与关键词检索的策略 |
| 13 | Reranking | 重排序 |  | 对候选搜索结果进行更精细的相关性排序 |
| 14 | Query Rewriting | 查询改写 |  | 将用户问题改写为更适合检索的表达 |
| 15 | Multi-hop Retrieval | 多跳检索 |  | 通过多个关联证据步骤完成检索 |
| 16 | Knowledge Graph (KG) | 知识图谱 | KG | 用实体和关系表示结构化知识的图 |
| 17 | Source Attribution | 来源归因 |  | 明确回答所依赖的原始信息来源 |
| 18 | Evidence Chain | 证据链 |  | 将结论与可追溯支持材料对应的路径 |

## 07. 工作流与编排模式

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Workflow | 工作流 |  | 按既定控制逻辑组织步骤和工具的处理过程 |
| 2 | Agent Orchestration | 智能体编排 |  | 协调多步骤、模型、工具与智能体之间的执行 |
| 3 | Chaining | 链式处理 |  | 让前一阶段的输出成为后一阶段的输入 |
| 4 | Prompt Chaining | 提示链 |  | 由多个串联的模型调用完成任务 |
| 5 | Routing Pattern | 路由模式 |  | 将输入分配给适当的后续处理路径 |
| 6 | Parallelization | 并行化 |  | 同时执行可独立完成的多个子任务 |
| 7 | Aggregation Pattern | 汇总模式 |  | 合并多路执行输出形成统一结果 |
| 8 | Orchestrator–Workers | 编排者—工作者模式 |  | 中心编排者动态分解任务并分派工作者 |
| 9 | Evaluator–Optimizer | 评估者—优化者模式 |  | 生成、评价、反馈与再生成的迭代模式 |
| 10 | Plan-and-Execute | 计划后执行 |  | 先形成计划，再按步骤实施的组织方式 |
| 11 | Reactive Execution | 反应式执行 |  | 依据即时观察快速决定下一步行动 |
| 12 | Sequential Execution | 顺序执行 |  | 按固定顺序逐步完成各环节 |
| 13 | Conditional Branch | 条件分支 |  | 根据判断结果选择不同后续路径 |
| 14 | Control Flow | 控制流 |  | 决定程序或流程步骤的执行顺序 |
| 15 | Data Flow | 数据流 |  | 信息在各任务节点之间传递的关系 |
| 16 | Directed Acyclic Graph (DAG) | 有向无环图 | DAG | 无环的任务依赖结构，常用于工作流编排 |
| 17 | State Graph | 状态图 |  | 以状态和状态转移描述执行过程的图结构 |
| 18 | Loop Node | 循环节点 |  | 允许依据条件重复执行的流程节点 |
| 19 | Fan-out | 扇出 |  | 将一项工作分派到多条并行路径 |
| 20 | Fan-in | 扇入 |  | 汇集多条路径的执行结果 |
| 21 | Gate Check | 门控检查 |  | 决定流程能否进入下一阶段的校验 |

## 08. 多智能体协作

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Multi-Agent System (MAS) | 多智能体系统 | MAS | 两个或多个智能体共同完成任务的系统 |
| 2 | Specialist Agent | 专业智能体 |  | 面向特定知识域或任务的智能体 |
| 3 | Generalist Agent | 通用智能体 |  | 能处理多类任务的智能体 |
| 4 | Manager Agent | 管理者智能体 |  | 总体协调其他智能体工作的角色 |
| 5 | Coordinator Agent | 协调者智能体 |  | 负责同步、分配和整合协作工作的角色 |
| 6 | Worker Agent | 工作者智能体 |  | 接受具体任务并返回结果的执行角色 |
| 7 | Supervisor Agent | 监督者智能体 |  | 监控进度、质量或决策的角色 |
| 8 | Reviewer Agent | 审查者智能体 |  | 对生成内容或执行结果进行独立检查 |
| 9 | Critic Agent | 批评者智能体 |  | 找出方案中的问题与改进空间 |
| 10 | Inter-Agent Communication | 代理间通信 |  | 智能体之间交换消息和状态的过程 |
| 11 | Task Delegation | 任务委派 |  | 将任务交由另一个智能体承担 |
| 12 | Handoff | 控制权交接 |  | 将后续处理控制权转移给另一智能体 |
| 13 | Agent as Tool | 智能体即工具 |  | 由主智能体调用专家智能体且保持自身控制权 |
| 14 | Shared Memory | 共享记忆 |  | 多个智能体共同访问的记忆数据 |
| 15 | Blackboard | 共享黑板 |  | 智能体协作读写的公共工作区 |
| 16 | Message Bus | 消息总线 |  | 在组件或智能体间转发消息的通信基础设施 |
| 17 | Consensus | 共识 |  | 多个参与者形成共同判断或决定的机制 |
| 18 | Conflict Resolution | 冲突解决 |  | 处理多智能体输出不一致的方法 |
| 19 | Role Specialization | 角色分工 |  | 依据能力为智能体分配不同职责 |
| 20 | Handoff Record | 任务交接记录 |  | 记录委派内容、上下文和交接结果的信息 |
| 21 | Coordination Failure | 协作失效 |  | 由误解、冲突或依赖问题导致的协作故障 |

## 09. MCP：模型上下文协议

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Model Context Protocol (MCP) | 模型上下文协议 | MCP | 连接 AI 应用与外部工具、资源和能力的开放协议 |
| 2 | MCP Host | MCP 主机 |  | 管理一个或多个 MCP 客户端的宿主应用 |
| 3 | MCP Client | MCP 客户端 |  | 与 MCP 服务器建立协议连接的组件 |
| 4 | MCP Server | MCP 服务器 |  | 向客户端提供工具、资源和提示模板的服务 |
| 5 | MCP Tool | MCP 工具 |  | 供模型发现和调用的服务器端工具能力 |
| 6 | MCP Resource | MCP 资源 |  | 服务器提供的可读内容或数据 |
| 7 | MCP Prompt | MCP 提示模板 |  | 服务器公开的可复用提示或消息模板 |
| 8 | Resource URI (URI) | 资源标识符 | URI | 用于定位或识别 MCP 资源的统一标识符 |
| 9 | Tool Listing (tools/list) | 工具列表 |  | 客户端获取服务器工具列表的标准请求 |
| 10 | Tool Invocation (tools/call) | 工具执行 |  | 客户端请求服务器调用指定工具的标准操作 |
| 11 | Capability Negotiation | 能力协商 |  | 连接建立时协商支持的协议特性 |
| 12 | Protocol Version Negotiation | 协议版本协商 |  | 确定通信双方采用的兼容协议版本 |
| 13 | JSON-RPC | JSON 远程过程调用 |  | MCP 核心消息交互所用的远程调用协议形式 |
| 14 | Standard Input/Output Transport (stdio) | 标准输入输出传输 |  | 通过本地进程标准输入与输出传递消息 |
| 15 | Streamable HTTP Transport | 流式 HTTP 传输 |  | 基于 HTTP 的 MCP 消息传输方式 |
| 16 | Sampling | 采样请求 |  | 服务器通过客户端请求模型生成内容的能力 |
| 17 | Elicitation | 用户信息征询 |  | 服务器经客户端请求用户提供必要信息的机制 |
| 18 | Roots | 根目录 |  | 客户端向服务器声明的文件系统工作范围 |
| 19 | Completion | 参数自动补全 |  | 针对部分提示或资源参数给出补全候选 |
| 20 | Progress Notification | 进度通知 |  | 向调用方报告长任务的执行进度 |
| 21 | Cancellation Notification | 取消通知 |  | 通知对方取消一个进行中的请求 |
| 22 | Authorization | 授权 |  | 决定请求者能否访问特定资源或操作的机制 |
| 23 | MCP Extension | MCP 扩展 |  | 在核心协议之外协商启用的可选功能 |
| 24 | MCP Apps | MCP 应用 |  | 支持在对话环境中展示交互式界面的扩展方案 |

## 10. A2A：智能体间协议

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Agent2Agent Protocol (A2A) | 智能体间协议 | A2A | 用于独立智能体之间互通与协作的开放协议 |
| 2 | A2A Client | A2A 客户端 |  | 发起代理间消息或任务请求的一方 |
| 3 | A2A Server | A2A 服务器 |  | 对外提供智能体能力并响应请求的一方 |
| 4 | Remote Agent | 远程智能体 |  | 通过网络暴露服务、由其他系统调用的智能体 |
| 5 | Agent Card | 智能体名片 |  | 描述智能体地址、能力与鉴权方式的机器可读元数据 |
| 6 | Agent Discovery | 智能体发现 |  | 查找可用远程智能体及其能力的过程 |
| 7 | Agent Skill | 智能体技能 |  | Agent Card 中声明的可提供任务能力 |
| 8 | A2A Task | A2A 任务 |  | 具有身份和生命周期的协作工作单元 |
| 9 | A2A Message | A2A 消息 |  | 通信双方交换的指令、说明或结果消息 |
| 10 | Message Part | 消息片段 |  | 消息中承载文本、文件或结构化数据的内容单元 |
| 11 | Artifact | 任务产物 |  | 智能体完成任务后返回的文档或其他成果 |
| 12 | Task State | 任务状态 |  | 反映协作任务当前进展的状态值 |
| 13 | Task Lifecycle | 任务生命周期 |  | 任务从创建、执行到完成或失败的状态变化 |
| 14 | Streaming Update | 流式更新 |  | 在任务执行期间逐步推送进度或结果 |
| 15 | Push Notification | 推送通知 |  | 由服务侧主动发送任务事件通知 |
| 16 | Interoperability | 互操作性 |  | 不同厂商或框架的系统协同工作的能力 |
| 17 | Capability Declaration | 能力声明 |  | 公布智能体支持的操作、格式和特性 |
| 18 | Task Delegation Protocol | 任务委派协议 |  | 对跨智能体任务转交与结果回收的约定泛称 |

## 11. 执行状态、持久化与恢复

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | State Machine | 状态机 |  | 以状态与转移规则控制流程的模型 |
| 2 | Checkpoint | 检查点 |  | 保存执行状态以支持恢复的记录 |
| 3 | Checkpointing | 检查点保存 |  | 周期性或事件驱动地写入状态快照 |
| 4 | Persistence | 持久化 |  | 让执行数据在进程结束后仍被保存 |
| 5 | Durable Execution | 持久执行 |  | 中断、失败或重启后能够继续执行的机制 |
| 6 | Interrupt | 中断 |  | 在满足条件时暂停执行等待外部处理 |
| 7 | Resume Execution | 恢复执行 |  | 使用已保存状态继续未完成任务 |
| 8 | Human-in-the-loop (HITL) | 人工介入 | HITL | 在关键决策或操作节点引入人工参与 |
| 9 | Human Review | 人工审核 |  | 由人检查模型建议或执行结果 |
| 10 | Human Approval | 人工批准 |  | 敏感操作执行前取得明确人工许可 |
| 11 | Recoverable Error | 可恢复错误 |  | 可通过重试、纠正或恢复继续处理的错误 |
| 12 | Retry Policy | 重试策略 |  | 确定失败时何时以及如何重新尝试的规则 |
| 13 | Exponential Backoff | 指数退避 |  | 重试等待时间按指数增长的节流方法 |
| 14 | Timeout | 超时 |  | 超出允许执行时长而中止操作的机制 |
| 15 | Deadline | 截止期限 |  | 任务或步骤必须结束的时间界限 |
| 16 | Failover | 故障转移 |  | 主执行路径不可用时切换至备用路径 |
| 17 | Compensating Action | 补偿操作 |  | 用于抵消已执行步骤影响的后续操作 |
| 18 | Transaction Boundary | 事务边界 |  | 界定一组状态更新原子性范围的位置 |
| 19 | Execution Log | 执行日志 |  | 按时间记录动作、状态和结果的日志 |

## 12. 评测体系与常见基准

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Agent Evaluation | 智能体评测 |  | 衡量智能体完成真实任务能力的系统性测试 |
| 2 | Benchmark | 评测基准 |  | 由任务、环境和评分规则构成的标准化测试集 |
| 3 | Evaluation Dataset (Eval Set) | 评测集 |  | 用于验证系统性能的一组样例或任务 |
| 4 | Task Success Rate | 任务成功率 |  | 在定义的任务集合中成功完成任务的比例 |
| 5 | End-to-end Success Rate | 端到端成功率 |  | 从接收任务到最终交付全流程的成功比例 |
| 6 | Tool-call Accuracy | 工具调用正确率 |  | 选用正确工具并提供正确参数的比例 |
| 7 | Action Success Rate | 动作成功率 |  | 执行动作后达到预期环境结果的比例 |
| 8 | Trajectory Evaluation | 轨迹评测 |  | 评价中间行动序列而非仅最终答案 |
| 9 | Trajectory | 轨迹 |  | 任务期间发生的推理、调用、反馈和状态序列 |
| 10 | Outcome Evaluation | 结果评测 |  | 重点检查最终产物是否满足目标 |
| 11 | Process Evaluation | 过程评测 |  | 检查执行步骤、证据和控制是否合理 |
| 12 | Faithfulness | 忠实度 |  | 生成结论是否得到给定证据支持的程度 |
| 13 | Factual Accuracy | 事实准确性 |  | 输出中的事实与可靠来源一致的程度 |
| 14 | Robustness | 鲁棒性 |  | 面对噪声、异常与环境变化时的稳定程度 |
| 15 | Reproducibility | 可复现性 |  | 在明确条件下重现评测结果的能力 |
| 16 | LLM-as-a-Judge | 评判模型 |  | 使用语言模型对其他输出进行评分的方法 |
| 17 | Ground Truth | 黄金答案 |  | 用于判定任务目标或正确性的参考结果 |
| 18 | Human Annotation | 人工标注 |  | 由人工制定标签或评价结果 |
| 19 | Regression Test | 回归测试 |  | 验证版本更新未破坏既有能力的测试 |
| 20 | Scenario-based Evaluation | 基于场景的评测 |  | 围绕真实用户工作情境设计的评测 |
| 21 | GAIA | GAIA 基准 |  | 测试通用 AI 助手处理多步骤真实任务的基准 |
| 22 | SWE-bench | SWE-bench |  | 基于真实软件仓库问题评测代码修复能力的基准 |
| 23 | WebArena | WebArena |  | 评估网页环境中长程操作能力的基准 |
| 24 | OSWorld | OSWorld |  | 评估计算机操作系统环境任务的基准 |
| 25 | tau-bench | τ-bench |  | 评估带工具与交互约束的真实任务执行能力的基准 |
| 26 | Berkeley Function Calling Leaderboard (BFCL) | 伯克利函数调用榜单 | BFCL | 测试函数调用及相关能力的一组评测 |

## 13. 安全防护与治理

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Guardrail | 护栏 |  | 在输入、工具和输出阶段执行的约束或检查 |
| 2 | Policy Constraint | 策略约束 |  | 系统必须遵守的规则与边界 |
| 3 | Principle of Least Privilege (PoLP) | 最小权限原则 | PoLP | 只授予完成任务所需的最小访问能力 |
| 4 | Permission Scope | 权限范围 |  | 对允许访问的资源和操作进行限定 |
| 5 | Access Control | 访问控制 |  | 基于身份和策略决定资源使用权限 |
| 6 | Authentication (AuthN) | 身份认证 | AuthN | 验证调用者或执行主体身份的过程 |
| 7 | Authorization (AuthZ) | 访问授权 | AuthZ | 确认已认证主体可以执行哪些操作 |
| 8 | Sandbox | 沙箱 |  | 隔离代码和工具运行以限制不良影响的环境 |
| 9 | Safety Confirmation | 安全确认 |  | 高影响动作前对目标和风险进行再次确认 |
| 10 | Human Oversight | 人类监督 |  | 人对智能体目标、权限与高风险行为实施监督 |
| 11 | Refusal | 拒绝执行 |  | 系统对不被允许的请求予以拒绝 |
| 12 | Safe Fallback | 安全回退 |  | 不满足执行条件时转向风险更低的操作 |
| 13 | Audit Trail | 审计跟踪 |  | 能够追溯关键操作、授权与结果的记录 |
| 14 | Security Boundary | 安全边界 |  | 隔离不同信任等级组件或数据的界线 |
| 15 | Trust Boundary | 信任边界 |  | 输入从低信任来源进入高信任域的边界 |
| 16 | Data Minimization | 数据最小化 |  | 只收集和传输完成任务必需的数据 |

## 14. 智能体攻击与风险

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Prompt Injection | 提示词注入 |  | 利用恶意指令影响模型或智能体行为的攻击 |
| 2 | Indirect Prompt Injection | 间接提示词注入 |  | 通过网页、文件、工具输出等外部内容注入指令 |
| 3 | Tool-output Poisoning | 工具输出投毒 |  | 篡改工具返回内容以误导后续决策 |
| 4 | Memory Poisoning | 记忆投毒 |  | 把恶意信息写入记忆影响未来行为 |
| 5 | Goal Hijacking | 目标劫持 |  | 使智能体偏离原任务转而服务攻击者目标 |
| 6 | Tool Misuse | 工具滥用 |  | 在不合适情境下使用合法工具造成风险 |
| 7 | Privilege Escalation | 权限提升 |  | 获得超出原授权范围的权限 |
| 8 | Data Exfiltration | 数据外泄 |  | 未经授权将敏感信息转移到外部 |
| 9 | Sensitive Data Exposure | 敏感信息暴露 |  | 在上下文、日志或输出中泄漏敏感数据 |
| 10 | Unauthorized Action | 越权操作 |  | 执行超出主体权限或用户许可的动作 |
| 11 | Excessive Autonomy | 过度自主性 |  | 缺少足够监督而独立执行高风险行为 |
| 12 | Excessive Agency | 过度代理权限 |  | 因功能、权限或自主性过大导致的系统风险 |
| 13 | Supply Chain Attack | 供应链攻击 |  | 经依赖、工具或第三方服务引入攻击 |
| 14 | Tool Poisoning | 工具投毒 |  | 通过恶意工具定义、元数据或结果诱导不安全行为 |
| 15 | Prompt Leakage | 提示词泄漏 |  | 系统内部提示或隐藏配置被不当披露 |
| 16 | Denial of Wallet (DoW) | 成本耗尽攻击 | DoW | 通过重复调用耗尽推理或工具预算的攻击 |

## 15. 工程化、成本与可观测性

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Observability | 可观测性 |  | 通过日志、指标和追踪理解系统内部行为 |
| 2 | Tracing | 追踪 |  | 记录一次任务跨模型和工具的执行路径 |
| 3 | Trace | 追踪记录 |  | 代表一次端到端运行的关联事件集合 |
| 4 | Span | 跨度 |  | 追踪中描述一个操作片段的记录 |
| 5 | Distributed Tracing | 分布式追踪 |  | 跨多个服务关联请求和操作的跟踪技术 |
| 6 | Logging | 日志记录 |  | 持续记录执行事件和关键上下文 |
| 7 | Metrics Monitoring | 指标监控 |  | 采集成功率、延迟和用量等数值 |
| 8 | Structured Logging | 结构化日志 |  | 以可解析字段形式记录执行信息 |
| 9 | Correlation ID | 相关标识符 |  | 用于关联同一任务不同组件记录的标识 |
| 10 | Latency | 延迟 |  | 从请求到响应或某一步操作的耗时 |
| 11 | Throughput | 吞吐量 |  | 单位时间内处理的请求或任务数量 |
| 12 | Concurrency | 并发 |  | 多个任务在重叠时间区间内推进 |
| 13 | Parallelism | 并行 |  | 多个计算操作在同一时刻执行 |
| 14 | Rate Limiting | 速率限制 |  | 限制单位时间的调用次数或资源消耗 |
| 15 | Quota | 请求配额 |  | 约定周期内可使用的调用或资源总量 |
| 16 | Token Usage | 词元用量 |  | 调用过程中消耗的输入、输出等词元数量 |
| 17 | Cost per Task | 单任务成本 |  | 完成一个任务平均消耗的资源或费用 |
| 18 | Cost Budget | 成本预算 |  | 为任务设置的最高可接受费用 |
| 19 | Cost–Quality Trade-off | 成本—质量权衡 |  | 在答案质量和执行资源之间做取舍 |
| 20 | Caching | 缓存 |  | 复用已计算或已获取结果以降低延迟和费用 |
| 21 | Lifecycle Hook | 回调钩子 |  | 在执行生命周期指定事件触发的扩展函数 |
| 22 | Circuit Breaker | 断路器 |  | 故障率升高时暂时阻断调用的保护机制 |
| 23 | Service Level Objective (SLO) | 服务级别目标 | SLO | 对可用性、时延等服务质量的内部目标 |
| 24 | Service Level Agreement (SLA) | 服务级别协议 | SLA | 对外承诺并约定责任的服务质量条件 |
| 25 | Alerting | 告警 |  | 在指标异常或规则触发时发送通知的机制 |
| 26 | Runbook | 运行手册 |  | 面对常见事故或操作场景的标准处理步骤 |

## 16. 开发实践与生态术语

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Agent Development Kit (ADK) | 智能体开发工具包 | ADK | 供开发者构建智能体的工具与组件集合 |
| 2 | Software Development Kit (SDK) | 软件开发工具包 | SDK | 封装 API、类型和开发辅助功能的工具包 |
| 3 | Skill Package | 技能包 |  | 包含可复用指令、参考资料与辅助脚本的能力资产包 |
| 4 | Skill Discovery | 技能发现 |  | 识别当前可用技能和适用场景的过程 |
| 5 | Skill Invocation | 技能调用 |  | 按任务需求加载或执行技能的过程 |
| 6 | Instruction File | 指令文件 |  | 存放特定环境中行为规则的配置文档 |
| 7 | Tool Manifest | 工具清单 |  | 描述可用工具、用途与参数的声明文件 |
| 8 | Schema Definition | 模式定义 |  | 声明数据结构、类型和必填字段的规范 |
| 9 | JSON Schema | JSON 模式 |  | 用于描述和校验 JSON 数据结构的标准 |
| 10 | Orchestration Graph | 编排图 |  | 以节点和边表达任务步骤及转移关系的图 |
| 11 | Node | 节点 |  | 工作流或状态图中的执行单元 |
| 12 | Edge | 边 |  | 描述节点之间连接或转移的关系 |
| 13 | Prompt Template | 提示模板 |  | 通过变量插值生成模型输入的模板 |
| 14 | Environment Variable | 环境变量 |  | 向程序传递配置的系统级键值参数 |
| 15 | Secrets Management | 密钥管理 |  | 安全存储、分发和轮换敏感凭据 |
| 16 | Development Environment | 开发环境 |  | 用于构建、调试和测试系统的运行条件 |
| 17 | Staging Environment | 暂存环境 |  | 在正式上线前模拟生产场景的验证环境 |
| 18 | Production Environment | 生产环境 |  | 向真实用户提供正式服务的运行环境 |
| 19 | Version Control | 版本控制 |  | 追踪代码和配置修改历史的机制 |
| 20 | Continuous Integration (CI) | 持续集成 | CI | 频繁合并并自动测试代码变更的实践 |
| 21 | Continuous Delivery (CD) | 持续交付 | CD | 自动化构建和发布准备的软件交付实践 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/ai-agents.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
