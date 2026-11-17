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
| 03 | 041–060 | 模型能力与推理 / 任务规划与决策 | 20 | planned |
| 04 | 061–080 | 任务规划与决策 / 工具使用与环境交互 | 20 | planned |
| 05 | 081–100 | 工具使用与环境交互 / 上下文、记忆与状态 | 20 | planned |
| 06 | 101–120 | 上下文、记忆与状态 / 检索与知识增强 | 20 | planned |
| 07 | 121–140 | 检索与知识增强 / 工作流与编排模式 | 20 | planned |
| 08 | 141–160 | 工作流与编排模式 / 多智能体协作 | 20 | planned |
| 09 | 161–180 | 多智能体协作 / MCP：模型上下文协议 | 20 | planned |
| 10 | 181–200 | MCP：模型上下文协议 / A2A：智能体间协议 | 20 | planned |
| 11 | 201–220 | A2A：智能体间协议 / 执行状态、持久化与恢复 | 20 | planned |
| 12 | 221–240 | 执行状态、持久化与恢复 / 评测体系与常见基准 | 20 | planned |
| 13 | 241–260 | 评测体系与常见基准 / 安全防护与治理 | 20 | planned |
| 14 | 261–280 | 安全防护与治理 / 智能体攻击与风险 | 20 | planned |
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

## 人工审稿要求

逐篇检查来源与论断匹配、算例的数学步骤、技术版本与安全边界；对任何需修改事实的文章保留改动记录。分支存在候审稿不等于已经合并，也不等于经过独立专家认证。
