# AI Agents · 第 7 批（121–140）学习路径、研究来源与审稿

> 本文是内部编辑/审稿资料。读者使用统一 Explorer 的词条页，不应看到批次表。权威顺序来自 [AI Agents 词表](../../glossaries/ai-agents.md)。

## 多跳检索与证据归因（121–124）

从 Multi-hop Retrieval 开始，理解跨文档桥接查询：每一跳都必须保留实体 ID、时间条件、原文证据及来源。Knowledge Graph 可用 RDF 三元组与 SPARQL 路径，但图上的边不自动代表真相；Source Attribution 解决主张的来源归属，Evidence Chain 解决多个证据之间如何支持最终结论。特别区分事实支持路径与模型内部未公开推理。

## 编排模式与角色（125–135）

Workflow 强调可测试、可复核的处理步骤；Agent Orchestration 负责执行调度、权限、检查点与错误恢复。Prompt Chaining 为多轮模型调用添加中间 gate；Routing Pattern 决定专业子流程；Parallelization 降低关键路径延迟，但增加并发资源与汇总复杂性。Orchestrator–Workers 动态拆解未知子任务，Evaluator–Optimizer 反复评价与优化并应有 max_rounds。

Plan-and-Execute 将规划与执行分离，Reactive Execution 每步根据环境反馈行动；生产系统常混合二者，仍须对外部副作用做对账和授权。

## 依赖图与状态（136–140）

Sequential Execution、Conditional Branch、Control Flow、Data Flow、DAG 有不同关注点。数据流定义字段、单位、schema、权限与来源；控制流定义何时执行以及失败/取消的分支；DAG 无有向环，可以拓扑排序。真正的循环将在第 8 批 State Graph 中表达。

## 工程综合案例：软件发布

团队要求从仓库构建和证据查询开始，到执行 CI、安全扫描与人工批准，最终灰度发布。

1. 多跳检索源文档、依赖变更与发布规则，逐项记录出处和版本。
2. 构建节点 A 先运行，测试 B 与扫描 C 在 A 结束后并行，审批 D 等待两个子任务的成功证据。
3. 汇总时按 task_id 去重，不把未知或超时当通过；任何真实发布动作需执行层权限和独立 gate。
4. 对部署超时保持 unknown 并查询权威系统，不能无条件重复发布。
5. 输出报告把结论映射到 CI run、原始规范和实际部署版本。

## 中等难度面试题

**问：**为什么编排器不能根据三个 Worker 全部回答“成功”就立即启动部署？

**参考答案：**Worker 自述不是实际成功证据。编排器必须关联每个任务的输入版本、CI 状态、扫描结果、审批范围和外部权威系统；缺任何强制门控均不能放行。

## 中等难度考试题

**题：**构建 A 为 2 分钟，单测 B 为 3 分钟、安全扫描 C 为 5 分钟，两者均依赖 A；审批 D 为 1 分钟并依赖 B/C。求资源充足且无排队时的关键路径总时长。

**解：**依赖 A→(B || C)→D，时间为 2+max(3,5)+1=8 分钟；不是全串行的 11 分钟，仍需考虑人工审批等待。

## 权威一手来源

- [HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering（EMNLP 2018）](https://aclanthology.org/D18-1259/)
- [W3C RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/)
- [W3C SPARQL 1.1](https://www.w3.org/TR/sparql11-query/)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic · Building Effective Agents Cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/README.md)
- [LangGraph · Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [Python · TopologicalSorter](https://docs.python.org/3/library/graphlib.html)

## 审稿要点

逐项核对来源与具体断言、DAG 时间推导、并发数据竞争与工具副作用的处理。CI 结构化验证不是领域专家审阅，review ledger 保持 pending。
