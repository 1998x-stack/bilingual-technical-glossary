# AI Agents · 第 4 批（061–080）综合学习与审稿路径

> 权威顺序：[AI Agents 332 词原表](../../glossaries/ai-agents.md)。本材料是内部教学和审稿路线，**不出现在公开 GitHub Pages 的读者导航**。仅真实存在的 20 篇正文进入统一 Explorer 索引。

## 概念路线

`Backtracking → Replanning → Stopping Criterion` 继续上一批规划模块，强调内部搜索回退不等于外部事务回滚。

`Tool → Tool Call → Tool Result` 建立工具生命周期：模型提出执行请求，后端校验权限和参数，真正执行并返回可验证的观察数据。Tool Result 不代表高优先级系统指令。

`Tool Discovery → Tool Registry → Tool Selection → Tool Routing → Tool Schema → Argument Validation` 划分工具集合来源、能力匹配、执行路由与强制安全门控；这六个环节并非同一个过程。

`Function Tool → Web Search Tool → Browser Automation → Computer Use → Code Execution → Command-line Tool → API → Tool Adapter` 对比七类执行形态与统一接入层。

## 工程贯穿案例：仓库采购 Agent

**需求**：Agent 在有限预算内查询供应商库存、比较报价、生成采购单并等待授权。任何实际下单/支付都需要用户明确确认。

1. 规划层：先查询库存与报价，若供应商缺货则重规划**未完成**节点；已提交的采购单需保留事务 ID。
2. 发现层：按当前用户身份列出可信工具。Registry 保存受审查的 schema、版本与路由目标；工具可见不意味着授权通过。
3. 选择与路由层：库存查询与下单工具应严格区分；由可信命名空间路由到正确租户的执行器，不能接受模型自由生成的目标 URL。
4. 执行层：先做 schema 和业务参数校验，检查金额、单位、供应商资质、库存和审批。写操作设置后端支持的幂等标识。
5. 环境层：网页工具结果、搜索摘要、GUI 字幕均是低信任 observation，不得被提升为系统指令。
6. 验收层：只以权威订单状态和收款确认作为成功判据；工具请求超时须归为 unknown 并查事务，不得直接重做付款。

## 中等难度跨概念面试题

**问：**采购 Agent 已发出一笔付款，但工具结果丢失，随后模型回溯到另一个供应商并要求再次付款。系统设计上应该怎样处理？

**参考答案：**先把首笔付款状态标记为 unknown，通过请求 ID/幂等键查权威账务。回溯只对内部搜索候选生效，不能自动撤销外部副作用；若需切换供应商，应保留第一笔付款记录并经过取消/退款或审批流程。工具执行器必须阻止在未知状态下盲目重试。

## 中等难度综合考试题

**题：**Agent 依序运行网页查询 0.8 s、库存 API 0.4 s、模型决策 0.7 s、下单 1.1 s、订单状态核验 0.5 s。若严格串行、忽略排队，总时长是多少？若前两项查询互不依赖可并行，结果又是多少？

**解：**串行时间 `0.8+0.4+0.7+1.1+0.5=3.5 s`；前两项并行时间为 `max(0.8,0.4)+0.7+1.1+0.5=3.1 s`。所有费用、延迟都是题设教学值，不代表系统 benchmark。下单和状态核验存在依赖，不可盲并行。

## 核心权威来源

- [AIMA · Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/)：回溯、规划、终止标准。
- [OpenAI · Function Calling](https://developers.openai.com/api/docs/guides/function-calling)：工具调用和反馈循环。
- [OpenAI · Using tools](https://developers.openai.com/api/docs/guides/tools)：工具配置、检索和执行。
- [MCP · Tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)：列举与调用工具。
- [Playwright · Locators](https://playwright.dev/docs/locators)：浏览器定位。
- [OpenAI · Shell](https://developers.openai.com/api/docs/guides/tools-shell)：受控命令行与代码执行。
- [IETF RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)：HTTP 方法与状态语义。
- [OWASP · Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)：工具输出/外部内容风险。
