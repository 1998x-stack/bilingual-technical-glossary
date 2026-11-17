# Elicitation（用户信息征询）

> AI Agents · 专题：MCP：模型上下文协议 · 以 2026-07-28 规范为当前基准，区分 legacy 模式

## 1. 核心定义

**Elicitation（用户信息征询）**：Elicitation（用户信息征询）是 MCP 工具处理中缺少必要字段或需要用户确认时，通过 Host/Client 向用户请求额外信息的机制。应明示请求用途、字段范围及接受、拒绝与取消状态。

**适用边界：**2025-era 常通过关联请求的 `elicitation/create` 实现；2026-07-28 无会话协议通过 `resultType:input_required` 的 MRTR 描述所需输入，客户端处理后以 `inputResponses` 重试。补齐字段不自动授权任何危险工具。

## 2. 形象理解

报销员在审核报销单时发现缺少差旅日期，向申请人询问后继续检查，而非自己编造日期。

**类比的局限：**用户回答了日期不等于授权付款，更不能把密码要求隐藏在普通征询框中。

## 3. 技术原理与核心内容

Server 发现 required_fields 不足，构造带 schema、来源与 requestState 的补问；Host 确认该请求与当前用户目标关联，阻止钓鱼式 URL/秘密采集。用户选择 accept、decline 或 cancel 后，Client 将响应写入 `inputResponses` 并重新提交原任务。Server 校验 requestState 完整性、业务对象 ID、参数类型、过期时间及授权；严禁将客户端传回数据当高信任指令。

## 4. 工程实践与设计权衡

**工程案例：**智能体办理采购时缺少货币单位，先向用户问 CNY 还是 USD。用户明确选择并核对订单号后继续计算；如果用户拒绝填写，进入等待或停止，不能默认选 CNY 并提交采购。

**失败模式与验证：**暗中默认敏感参数、同一用户被无限补问、保存未经必要的机密、把用户取消当同意、重新提交串错任务 ID。针对拒绝、重放、伪造与多次请求进行 E2E。

## 5. 关联知识与易混辨析

Elicitation 是用户参与的补充输入；Sampling 涉及模型生成（已弃用）；Handoff 是控制权交接；审批授权必须独立审查。

## 6. 中等难度面试题（含参考答案）

1. **问：用户拒绝提供必填字段后能否用模型推测？** 答：对高后果动作不能，应停止或转入获准的替代流程。
2. **问：新版为什么使用 inputResponses？** 答：因为服务器不再向客户端主动发起 RPC，而是通过原调用的多轮返回获取额外输入。

## 7. 中等难度考试题（含解析）

1. **题：共需 3 个必填字段，已提供 2 个，完整比例？** 解：2/3≈66.7%，仍不满足提交。
2. **题：服务端返回 action=cancel 是否能按 accept 执行？** 解：不能，必须遵从取消状态。

## 8. 权威来源与延伸阅读

- [MCP · Elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)：面向用户征询。
- [MCP TS SDK · MRTR](https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28)：input_required 与 inputResponses。
