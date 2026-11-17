# Interrupt（中断）

> AI Agents · 专题：执行状态、持久化与恢复 · 以真实运行状态、外部副作用对账和授权范围为工程边界

## 1. 核心定义

**Interrupt（中断）**：Interrupt（中断）是在 Agent 或图工作流运行到特定步骤时暂停执行，保存当前位置并等待额外输入、审批或外部系统条件的机制。它是有意暂停，不等于程序崩溃；正确中断需要持久化状态与可验证的恢复身份。

**适用边界：**LangGraph 的 `interrupt()` 是动态中断，可在节点内部触发；恢复时该节点可能从开头重新执行，因而中断前副作用不能随意重复。OpenAI Agents SDK 另通过 `RunResult.interruptions` 和 RunState 处理工具审批，两者 API 不同。

## 2. 形象理解

像工厂生产线在最终包装前等待质检签名，保留产品序列号和检查位置，批准后再继续。

**类比的局限：**生产线停住并不能撤销前面已经加工的零件，也不能由任何路人代签质检单。

## 3. 技术原理与核心内容

在 LangGraph：compile(checkpointer=...)，运行时提供 `thread_id`，节点调用 `interrupt(payload)`；运行器保存状态并返回待处理 payload。收到合法决定后使用 `Command(resume=decision)` 按原 thread_id 重新执行，结果成为 interrupt 调用返回值。由于节点可能重跑，等待点之前的付款/邮件动作需提前拆到独立幂等节点。审批 payload 应包含资源标识、参数哈希、版本、过期时间与最小敏感数据。

## 4. 工程实践与设计权衡

**工程案例：**部署 Agent 完成 CI 后请求‘允许发布 commit abc123 至 staging’，显示差异/风险并暂停。审批人仅对该环境和 SHA 授权；如果代码变为 def456，即使上一审批已同意也必须再次审核。

**失败模式与验证：**没有 checkpointer 导致恢复丢状态、重新执行节点时重复下单、等待凭证被冒用、无限等待没有过期/撤销策略。测试中断前后故障、不同 thread_id 和审批拒绝。

## 5. 关联知识与易混辨析

Interrupt 是执行暂停事件；Human Approval 是一种暂停原因；Resume Execution 是接续动作；Timeout 是时间限制，某个操作超时不自动创建合法恢复点。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 interrupt() 之前不应放不可幂等的发信动作？** 答：恢复时节点可能从头重执行，导致重复发信，应拆独立任务并对账。
2. **问：用户 A 生成的恢复 token 能否给用户 B 用？** 答：不能，恢复必须验证任务归属、实际身份和审批权限。

## 7. 中等难度考试题（含解析）

1. **题：中断前执行了 3 个只读步骤，审批后还需 2 个写步骤，若无重放且每步 1 秒，恢复后剩余时间？** 解：2 秒，忽略审批与调度耗时。
2. **题：审批绑定 SHA=abc，恢复时 SHA=def，能复用批准？** 解：不能，资源版本变化应重新确认。

## 8. 权威来源与延伸阅读

- [LangGraph · Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)：interrupt()、thread_id 和 Command(resume=...)。
- [OpenAI Agents SDK · Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)：RunState 持久化与审批后恢复。
