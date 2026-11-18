# Handoff Record（任务交接记录）

> AI Agents · 专题：多智能体协作 · 多 Agent 通信、一致性与独立业务验收

## 1. 核心定义

**Handoff Record（任务交接记录）**：Handoff Record（任务交接记录）是记录 Agent、工具或人类之间移交任务时的目标、上下文、负责者、权限边界、进度和确认结果的结构化证据。它支持恢复、追责与避免重复行动，但记录存在不等于交接成功或外部动作已完成。

**适用边界：**交接记录与 Handoff 执行事件不同：前者是证据与审计对象，后者是控制权转移；某些只委派子任务的流程也应保存交接记录但没有转移活跃对话控制。

## 2. 形象理解

像值班交班簿写明问题单号、当前状态、已执行操作、待办风险和接班人签收。

**类比的局限：**交班簿可能遗漏实际发生的设备操作，因此关键状态仍需独立对账。

## 3. 技术原理与核心内容

设计 HandoffRecord={handoff_id,from_agent,to_agent,task_id,goal,context_refs,allowed_scope,artifact_version,pending_tool_ids,ack_at,status}。sender 建议交接，接收方校验输入并 ACK 后才将 active_owner 变更；未 ACK 保持 pending，避免无人负责。对含敏感数据的引用设置 TTL/ACL，审计不可篡改但应最小化私人原文。

## 4. 工程实践与设计权衡

**工程案例：**法务 Agent 将合同异常转交合规专家，记录合同 ID、条款定位、证据版本、预计结果和未核验问题；接收人 ACK 后进行复核。若合同随后改版，旧交接结论失效并通知下一责任人。

**失败模式与验证：**无人确认仍标记 transferred、忘记 pending 付款请求而双执行、把个人资料全文广播、缺 artifact SHA 造成旧结论复用。测试未签收、重复 handoff、版本变化、取消和权限过期。

## 5. 关联知识与易混辨析

Handoff Record 是结构化移交痕迹；Handoff 是活跃 Agent 交接；Inter-Agent Communication 是消息交换过程；Task Delegation 是派给下游任务的更广行为。

## 6. 中等难度面试题（含参考答案）

1. **问：交接发送成功但接收方尚未 ACK，任务应算谁负责？** 答：必须由系统约定所有权转移点。常见做法在 ACK 前保持原责任或标记 pending，防止责任丢失。
2. **问：为什么交接记录要存 pending_tool_ids？** 答：接收方可先核对已提交未确认的外部动作，避免重试造成重复副作用。

## 7. 中等难度考试题（含解析）

1. **题：10 次交接中 8 次被接收方 ACK，按 ACK 衡量的交接完成率？** 解：8/10=80%，不代表对应任务都已完成。
2. **题：记录引用 commit A，实际审稿内容已变为 commit B，能复用原审稿通过结论吗？** 解：不能，需复核版本或重新审稿。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Handoffs](https://openai.github.io/openai-agents-python/handoffs/)：交接目标、输入与控制权转移。
- [W3C · PROV-O](https://www.w3.org/TR/prov-o/)：实体、活动、责任与溯源记录。
