# Memory Retrieval（记忆检索）

> AI Agents · 专题：上下文、记忆与状态 · 概念与实际框架行为以来源和版本为准

## 1. 核心定义

**Memory Retrieval（记忆检索）**：Memory Retrieval（记忆检索）是 Agent 依据当前目标、可信身份和上下文，从可访问的记忆存储中查找相关经验、事实或流程，经过过滤与核验后供后续决策使用的过程。检索的相关性不自动等于准确性或执行授权。

**适用边界：**仅凭向量相似度可能召回其他租户、旧版本或错误记录；应把访问控制和时效过滤放在可信存储/检索层，外部事实需要再次查证。

## 2. 形象理解

像档案员按主题寻找历史档案，同时检查调用者权限、档案时效和原始出处。

**类比的局限：**找到一份相似的旧文件，不意味着它适用于当前情况，更不能直接取代现行制度。

## 3. 技术原理与核心内容

可以建立 query formulation → authorization filter(owner,namespace,ACL) → keyword/vector/hybrid retrieval → reranking → freshness/conflict checks → provenance → context injection 的管线。对于精确 ID/业务号优先结构化或关键词检索；对语义案例用向量匹配，再按环境版本与结果证据筛选。评估 precision@k、recall@k、MRR、任务成功率、越权泄漏率与延迟，并对最新业务状态回查权威接口。

## 4. 工程实践与设计权衡

**工程案例：**排障 Agent 查询最近类似数据库延迟事件，从授权的情景记忆找出上次追踪号、错误日志与修复措施。操作前核对当前数据库版本、负载与真实权限；若不符，记忆只能提供假设。

**失败模式与验证：**跨租户召回敏感事件、向量库中的已删除条目仍可检索、过期经验替代实时事实、top-k 过大挤出当前任务约束。负向测试包括 ACL 绕过、过期、删除传播与错误结果支持证据。

## 5. 关联知识与易混辨析

Memory Retrieval 检索既存记忆；Knowledge Retrieval 可检索外部文档与数据库；Context Injection 决定检索结果如何进入本轮输入；Memory Write 负责验证后保存/更新记忆。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么记忆向量检索之前需要权限过滤？** 答：高语义相似度可能跨用户匹配私人记录，必须依可信登录身份在存储或检索阶段限制 owner、tenant 和访问范围。
2. **问：如何区分检索‘相关’和检索‘可靠’？** 答：相关性用 recall/precision 等度量；可靠性还要核对来源、版本、真实任务结果与证据支持率，不能只看 embedding 分数。

## 7. 中等难度考试题（含解析）

1. **题：一个查询共有 8 条相关记忆，top-5 返回 5 条其中 4 条相关，precision@5 和 recall@5 是多少？** 解：precision@5=4/5=80%，recall@5=4/8=50%。
2. **题：检索到三年前记录‘删除生产日志无需审批’，现在可以执行吗？** 解：不能。记忆不是权限，必须查现行授权策略并完成高风险动作确认。

## 8. 权威来源与延伸阅读

- [LangGraph · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)：语义、情景与程序性记忆及检索。
- [Lewis 等 · Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)：检索增强生成的知识访问模型。
