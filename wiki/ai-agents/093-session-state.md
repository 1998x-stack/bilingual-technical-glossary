# Session State（会话状态）

> AI Agents · 专题：上下文、记忆与状态 · 通用会话与记忆工程；具体框架行为以对应文档为准

## 1. 核心定义

**Session State（会话状态）**：Session State（会话状态）是 Agent 在某个会话范围内维护的当前工作变量与控制信息，例如任务阶段、已验证实体 ID、未完成工具调用、预算、审批状态和失败原因。它是运行器的结构化事实，而不是模型自然语言输出的简单拼接。

**适用边界：**Session State 可能只在内存中，也可能持久化为 checkpoint；必须定义哪些字段是权威、哪些只是模型建议。会话状态与全局业务数据库真实状态仍有区别。

## 2. 形象理解

像工地交接班表：当前施工到哪一步、哪些材料已到、哪个安全审批还待确认。

**类比的局限：**交接表可能滞后于现场施工；涉及付款或库存变化时仍要查询真实系统。

## 3. 技术原理与核心内容

建议定义 State={session_id,task_id,status,tool_calls,verified_facts,pending_approvals,usage,version}。每步依据合法状态机进行转移，如 `pending → in_progress → waiting_approval → succeeded/failed`；持久化 checkpoint 带版本与更新时间，避免并发覆盖。对于工具超时保留 unknown，并记录服务端事务 ID；摘要不能删除这类控制信息。

## 4. 工程实践与设计权衡

**工程案例：**旅行预订 Agent 在进入支付环节前保存航班 ID、票价有效期、乘客确认、未完成支付请求 ID。即使对话摘要压缩，支付状态仍由独立结构化数据和后端查询恢复。

**失败模式与验证：**只凭模型回复“完成”更新 state=succeeded、并发会话写入覆盖、checkpoint 不含版本或已执行副作用、状态恢复后再次下单。测试崩溃恢复、并发 CAS 冲突与状态转换合法性。

## 5. 关联知识与易混辨析

Session State 是当前流程的结构化运行状态；Conversation History 是事件回放；Working Memory 是完成当前任务需要的活跃信息集合，可能跨出 state 中的键值字段。

## 6. 中等难度面试题（含参考答案）

1. **问：Agent 输出“任务已完成”时，Session State 可以立即写 succeeded 吗？** 答：不能。应由外部验收规则确认任务状态和副作用后写入；模型文本仅提供候选结论。
2. **问：为什么关键业务变量不能只保存在自然语言摘要里？** 答：摘要可能丢失或篡改 ID、权限和交易状态；应结构化保存可验证字段，原文和证据引用可独立存储。

## 7. 中等难度考试题（含解析）

1. **题：状态版本初始为 7，两条并发请求都读取 7，A 成功将其更新为 8，B 再用 expected_version=7 写入，正确结果？** 解：B 应发生版本冲突并拒绝覆盖或重读重试，不能无声覆盖 A 的已提交状态。
2. **题：退款接口已返回 unknown，模型在会话里写了 succeeded，系统应以哪个作后续状态基础？** 解：不能信任模型自述；应保留 unknown，查询权威支付系统获得成功或失败证据后再转换。

## 8. 权威来源与延伸阅读

- [LangGraph · Memory overview](https://docs.langchain.com/oss/python/concepts/memory)：thread 级短期记忆、状态与跨会话存储。
- [OpenAI Agents SDK · Sessions](https://openai.github.io/openai-agents-python/sessions/)：会话历史读取、保存与不同会话存储实现。
