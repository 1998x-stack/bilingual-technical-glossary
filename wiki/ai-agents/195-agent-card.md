# Agent Card（智能体名片）

> AI Agents · 专题：A2A：智能体间协议 · 以 A2A 最新正式规范为依据，和旧版消息模型须区分

## 1. 核心定义

**Agent Card（智能体名片）**：Agent Card（智能体名片）是 A2A Server 发布的结构化元数据文档，说明自身身份、服务端点、协议绑定、能力、Agent Skill、输入输出媒体类型和认证要求。它是 Agent Discovery 与安全互操作的入口，但不是自动授信凭证。

**适用边界：**当前 A2A 的 `supportedInterfaces` 可包含多个按偏好排序的接口，各个接口需声明 URL、binding、protocolVersion；不同规范版本的旧字段不应未经兼容层直接使用。安全敏感技能或内部 endpoint 不应全部公开在匿名 Agent Card。

## 2. 形象理解

像企业对外名片和业务目录，客户看到地址、可办理事项和联系要求，之后还要签署合同与核验身份。

**类比的局限：**名片上的资质陈述可能过期或伪造，知道服务入口不等于有权调用任何业务能力。

## 3. 技术原理与核心内容

Card 定义 `name`, `description`, `version`, `supportedInterfaces`, `capabilities`, `defaultInputModes`, `defaultOutputModes`, `skills` 及可选安全描述。客户端通过 `/.well-known/agent-card.json`、可信 Registry 或配置获得它，按 ETag/Cache-Control 更新；必要时验证签名与 TLS 域名。敏感信息可由经授权的 Extended Agent Card 分级披露，不能在普通公开卡片中放静态 token。

## 4. 工程实践与设计权衡

**工程案例：**企业 Agent Registry 维护法律审查和财务审查两个卡片。查询‘政策解释’时选择支持 `text/plain` 输入的法律专员，验证身份和 skill；若卡片过期显示不存在的服务地址，客户端需重新发现或拒绝派工。

**失败模式与验证：**过期名片导致路由错误、证书/URL 未校验、Agent Skill 描述夸大、公开了内部地址或密钥、忽视 capabilities.pushNotifications 为 false。做伪造卡片、缓存过期、认证失败与不兼容绑定测试。

## 5. 关联知识与易混辨析

Agent Card 是整个远程 Agent 的服务描述；Agent Skill 是其中一项具体能力；MCP Tool Listing 是工具调用清单，不是 Agent Card 的同义物。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Agent Card 不应包含静态 API 密钥？** 答：卡片可能被广泛发现和缓存，明文凭据会泄漏，应使用独立认证流程与受限卡片。
2. **问：supportedInterfaces 顺序有什么意义？** 答：客户端应按偏好顺序选自己支持的接口并使用对应 endpoint 与协议版本。

## 7. 中等难度考试题（含解析）

1. **题：Card 列出 3 个绑定，Client 只支持其中第 2 个，应选择哪个？** 解：选择第 2 个兼容绑定，而不能强行使用第 1 个。
2. **题：用户仅授权 1/4 个 Skill，能凭卡片显示其余 3 个就调用吗？** 解：不能，服务端仍需按资源和操作授权。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：核心概念、操作与服务绑定。
- [A2A · Agent Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/)：Agent Card 发现、安全与缓存。
