# A2A Message（A2A 消息）

> AI Agents · 专题：A2A：智能体间协议 · 按 A2A 正式规范定义，不将旧版示例当作唯一序列化方式

## 1. 核心定义

**A2A Message（A2A 消息）**：A2A Message（A2A 消息）是 Client 与远端 Agent 交换意图、说明、补充信息或交互内容的结构化回合，包含发送方 `role` 与一个或多个 `parts`。它与 Task 和 Artifact 协同工作，但不应默认用于承载最终交付文件。

**适用边界：**官方规范强调消息和 Artifact 的职责分离：Message 用于发起任务、澄清和状态沟通；产出应优先放入 Task 的 Artifacts。Task history 不保证保存所有瞬时消息，关键事实不能仅依赖未持久化聊天。

## 2. 形象理解

像工单里的沟通记录：‘请补充需求’属于消息，而最终出具的合同审查报告是交付文件。

**类比的局限：**消息内容可能是低信任输入，含有‘立即付款’也不会自动获得执行权限。

## 3. 技术原理与核心内容

当前规范的 Message 具有 `role`、`parts`、messageId，可选 taskId/contextId/referenceTaskIds 等。role 值采用 `ROLE_USER` 与 `ROLE_AGENT` 等规范枚举；Part 可以包含 text、raw、url 或 data。Client 发送新消息前核对目标 Task 是否允许继续输入，终态任务不应随意接受修改；对输入做 MIME、大小与 ACL 检查。

## 4. 工程实践与设计权衡

**工程案例：**用户向翻译 Agent 提供中文技术段落作为 Message，Agent 回应需要确定目标地区；用户补充要求后，Agent 产生 Artifact，保存已译文本。上游只展示必要消息，不把它视为可编辑的后台文件。

**失败模式与验证：**把 Message 当不可篡改证据、误用旧版 role 字符串、终态任务继续写入、越权读取 history、恶意输入提示注入。用多轮、断线、非法 MIME、任务状态和跨租户消息测试。

## 5. 关联知识与易混辨析

Message 是对话单元；Part 是消息的内容片段；Artifact 是任务输出；Task 保存生命周期；Inter-Agent Communication 是更广通信过程。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么最终 PDF 更适合放 Artifact 而不是 Message 文本里？** 答：规范建议分离沟通和产出，Artifact 可承载文件及元数据，更易持久化与复核。
2. **问：任务历史是否必然包括所有发送过的消息？** 答：不保证，瞬时消息可能不持久化，关键审计要单独记录。

## 7. 中等难度考试题（含解析）

1. **题：一个 Message 由 text、data 两个 Part 组成，Part 总数？** 解：2 个，每个应遵守当前协议的 OneOf 字段规则。
2. **题：一个请求携带了非法 Part 同时含 text 和 raw，是否合规？** 解：不合规，当前 Part 必须只选择 text/raw/url/data 中一种。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Task、Message、Part 的规范结构。
- [A2A · Core Concepts](https://a2a-protocol.org/latest/topics/key-concepts/)：卡片、消息、产物与工作单元。
