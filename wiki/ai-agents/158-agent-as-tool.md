# Agent as Tool（智能体即工具）

> AI Agents · 专题：多智能体协作 · 多 Agent 协作模式与信任边界；SDK API 以版本文档为准

## 1. 核心定义

**Agent as Tool（智能体即工具）**：Agent as Tool（智能体即工具）是把专业 Agent 封装成具有明确输入/输出契约的工具，由主 Agent 在需要时调用并消费其结果。主 Agent 保留对话所有权与整体计划，可借助多个专家输出综合答复。

**适用边界：**Agent-as-tool 并不意味着工具只能返回文本，也不保证专家输出准确；子 Agent 可能间接调用其允许的真实工具。与 Handoff 的核心区别是控制权是否移交，而不是模型调用次数。

## 2. 形象理解

像总工程师调用实验室做专项测试，实验室送来报告，但由总工程师决定如何整合和汇报。

**类比的局限：**实验室报告不能凭一纸结论代替原始仪器读数；总工程师也不能让实验室越权获取个人数据。

## 3. 技术原理与核心内容

在 Agents SDK 中可通过 `specialist_agent.as_tool(tool_name=...,tool_description=...)` 生成工具，经理工具调用携带 bounded input，Runner 执行子 Agent，之后以标准结果返回经理。为子 Agent 限制上下文、可访问文件、模型预算和循环深度；经理用结果 ID、证据和状态验收，不把下游回答直接当支付/部署成功。

## 4. 工程实践与设计权衡

**工程案例：**产品文档 Agent 同时调用‘法律条款解释 Agent’与‘代码示例检查 Agent’，收集两者可定位依据后生成统一技术 Wiki。原始问题和最终答案仍归主 Agent，某一专家失败要标记缺失而非编造通过。

**失败模式与验证：**全量上下文透传、Agent 工具自我递归、子任务没有超时、用自然语言成功标记覆盖真实失败。可设置 tool_timeout、handoff_count=0（如果不允许交接）及输出 JSON Schema，对下游引用进行核验。

## 5. 关联知识与易混辨析

Agent as Tool 是经理保留控制权的调用模式；Handoff 改变活跃 Agent；Worker Agent 是执行角色；Orchestrator–Workers 通过动态任务拆解可能大量使用 Agent-as-tool，但概念范围更大。

## 6. 中等难度面试题（含参考答案）

1. **问：Manager 调用专家后谁对最终用户答复负责？** 答：Manager 保留对话控制与最终整合责任；子 Agent 提供受限结果，经理仍需查证关键事实。
2. **问：为什么应给 Agent-as-tool 配置结构化输出？** 答：有助于字段类型、状态、来源和失败的验证，减少自然语言解析含混和工具串线。

## 7. 中等难度考试题（含解析）

1. **题：主 Agent 调用两个 Specialist，串行时各 2s 和 3s，再整合 1s，总时长？** 解：2+3+1=6 秒；若真实可并行才可能降低关键路径。
2. **题：经理收到两个专家结果，一个 status=unknown，一个 status=ok，能宣告两项全部完成吗？** 解：不能，第一项未确认，应要求补证或返回部分完成状态。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Agents as tools](https://openai.github.io/openai-agents-python/tools/)：经理保持控制的 Agent 工具调用。
- [OpenAI Agents SDK · Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)：Manager 与 Handoff 设计权衡。
