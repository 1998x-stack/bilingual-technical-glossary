# Interoperability（互操作性）

> AI Agents · 专题：A2A：智能体间协议 · 跨 Agent 状态、授权与可靠执行的工程边界

## 1. 核心定义

**Interoperability（互操作性）**：Interoperability（互操作性）是不同厂商、语言、Agent 框架与部署环境之间，能够依据共同协议交换能力、任务和可检验产物的性质。A2A 通过 Agent Card、协议绑定、统一消息与任务生命周期降低跨实现对接成本。

**适用边界：**通信字段能解析只是语法互通，不代表数据语义、权限、媒体类型或业务目标一致。A2A 可支持 JSONRPC、HTTP+JSON、gRPC 等不同 binding，Client 必须挑选双方可实现的接口。

## 2. 形象理解

像不同国家的铁路采用统一集装箱接口，货物可以换车，但海关规则、单据币种和安全要求仍需检查。

**类比的局限：**接口兼容不意味着软件版本一致，也无法自动消除两家系统对‘完成’的业务定义差异。

## 3. 技术原理与核心内容

互操作可拆为 transport compatibility、protocolVersion、schema compatibility、mediaType、capability、semantic contract 和 authZ。Client 读取 `supportedInterfaces` 和 securitySchemes，选择兼容项，发送符合规范的 Message/Part，验证 Task/Artifact 和状态。对时间、货币、对象 ID、语言编码作明确契约；调用结果有误时提供可区分的错误码、回退路径和端到端 trace。

## 4. 工程实践与设计权衡

**工程案例：**企业内部 Agent 用 Python 实现，外部翻译 Agent 用 Go 实现；双方通过 A2A Task 协作并对齐文字媒体类型。输出中文合同译文后还需对法律实体 ID 与版本做核验，不会因为语言框架不同而丢失来源。

**失败模式与验证：**忽视支持绑定导致请求失败、旧版 Part 格式不兼容、role 枚举误映射、跨厂商授权不一致、同名 skill 意义不同。设计跨 SDK 契约测试、公开/私有卡片互操作矩阵与错误案例。

## 5. 关联知识与易混辨析

Interoperability 是跨实现协作能力；Capability Declaration 是自报支持的特性集合；Task Delegation Protocol 涉及具体委派规则；MCP Tools 层与 A2A Agent 层不能简单等同。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么解析成功的 JSON 不等于语义互操作？** 答：仍需核对媒体类型、对象 ID、状态规则与实际业务前置条件，才能保证同一含义。
2. **问：支持多种 A2A binding 时客户端如何选择？** 答：优先读取 Agent Card 的有序 supportedInterfaces，从中选双方兼容的协议绑定和 URL。

## 7. 中等难度考试题（含解析）

1. **题：系统 A 支持 JSONRPC、gRPC，B 支持 HTTP+JSON、gRPC，共同绑定？** 解：仅 gRPC；仍需核对协议版本和具体身份策略。
2. **题：同一金额数字 100 在两个系统币种分别 USD 与 CNY，可以直接视作同值吗？** 解：不能，需明确货币和汇率基准。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：绑定、能力声明与任务接口。
- [A2A · Official Repository](https://github.com/a2aproject/A2A)：多语言互操作与规范实现。
