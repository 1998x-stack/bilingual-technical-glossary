# AI Agents · 第 5 批（081–100）综合学习与审稿路径

> 官方术语顺序以 [AI Agents 332 条原词表](../../glossaries/ai-agents.md) 为准。本材料供内部编辑审稿，不放入网站的读者导航。仅真实存在的词条正文在统一 Explorer 中建立详情索引。

## 核心学习路线

**执行可靠性层**：Environment Feedback → Tool Retry → Side Effect → Idempotent Operation → Sensitive Action。

**上下文管理层**：Context → Context Engineering → Prompt Engineering → Context Injection → Context Compression。

**状态与记忆层**：Conversation History → Session → Session State → Working Memory → Short-term Memory → Long-term Memory → Episodic Memory / Semantic Memory / Procedural Memory → Memory Retrieval。

### 关键区分

- **工具结果 ≠ 业务成功**：HTTP 202/200 不能自动证明付款、退款或订单完成；未知写入先查权威事务 ID，再谈重试。
- **幂等 ≠ 无副作用**：重复同一意图不会叠加预期业务效果，但读写日志和响应码仍可能不同。需服务端正确实现幂等键和参数指纹。
- **上下文工程 ≠ 提示词工程**：前者管理指令、历史、工具描述、状态、检索资料以及记忆的全生命周期；后者侧重提示表达和示例。
- **Context Injection ≠ Prompt Injection**：前者按权限提供业务资料，后者利用不可信文本试图改变更高权限的指令。
- **Conversation History ≠ Session State ≠ Memory**：历史是事件流，状态是当前控制信息，记忆是被选择/维护的可复用知识。
- **情景 / 语义 / 程序性记忆**：分别回答发生过什么、知道什么、怎样去做。它们均可能过时或错误，必须保留 provenance。
- **记忆检索 ≠ 当前事实核验**：向量相似度不提供真实权限、证据可靠性或实时状态。

## 工程案例：企业退款与售后 Agent

用户询问“上次退款到哪里了”，流程如下：

1. 在可信用户身份下读取本次 Session State 和已授权订单 ID，不能从另一客户的历史获取记录。
2. 通过记忆检索找到相关情景：上次请求的 payment_id、时间和返回状态；这些只是查账线索。
3. 调用只读订单/支付接口查询权威结果并记录时间戳。查询失败时有限重试，遵守超时、退避和速率限制。
4. 若服务端显示 pending/unknown，不能再次调用创建退款。先用业务幂等键查实际状态，再依据授权和用户确认设计下一步。
5. 长会话使用 Context Compression 保留未结算交易 ID、约束和引用，不把旧消息或网页指令升级为权限。
6. 真正成功的验收依赖账务完成记录，不依赖模型说“已经到账”。

## 中等面试综合题

**问：**售后 Agent 在写退款接口超时后，把“上次成功处理类似故障”的 Episodic Memory 读入上下文。它应如何行动？

**答：**情景记忆只是历史经验，不保证当前请求未执行。必须保留未知事务状态，以支付 ID 和幂等键查询权威系统；若首次已执行，不重复写入。若后端支持同键同参数幂等重试，也要遵守重试预算及审批。记忆或历史话术不可替代授权与实际账务。

## 中等考试综合题

**题：**一个支持工具重试的 Agent 在一次只读请求失败后使用指数退避，基础间隔 0.5 秒，延迟上限 4 秒。连续四个等待阶段按 k=0、1、2、3 计算，忽略 jitter，总等待多少？若三层服务各尝试 3 次，最坏底层请求数是多少？

**解：**等待为 0.5、1、2、4 秒，合计 7.5 秒。三层各最多 3 次可能放大至 3³=27 次底层调用。实际服务需限制总重试次数和超时预算，并按幂等语义决定可否重试。

## 核心来源

- [IETF RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)：安全与幂等方法语义。
- [AWS · Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)：业务幂等键与重复请求。
- [AWS · Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)：重试与故障放大。
- [Anthropic · Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)：上下文优化。
- [OpenAI Agents SDK · Sessions](https://openai.github.io/openai-agents-python/sessions/)：会话历史及连续运行。
- [LangGraph · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)：短期、长期及记忆类型。
- [CoALA · Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427)：情景/语义/程序性记忆。
- [OWASP · Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)：敏感动作与最小权限。
