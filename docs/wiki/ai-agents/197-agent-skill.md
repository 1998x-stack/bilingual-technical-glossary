# Agent Skill（智能体技能）

> AI Agents · 专题：A2A：智能体间协议 · 按 A2A 正式规范定义，不将旧版示例当作唯一序列化方式

## 1. 核心定义

**Agent Skill（智能体技能）**：Agent Skill（智能体技能）是 A2A Agent Card 中声明的可执行任务能力，用 `id`、`name`、`description`、`tags` 等字段描述，可能另有 examples、输入输出媒体类型和安全要求。它用于能力匹配与路由，但不是某个固定代码函数的同义词。

**适用边界：**Skill 只描述服务器表示能够处理某类工作，是否真正完成任务需要 SendMessage 与 Task/Artifact 验收。广告式描述不代表专业执照，安全要求和工具权限必须按当前请求核实。

## 2. 形象理解

像服务企业的业务目录中标有‘法律文件摘要’‘技术翻译’等服务项目。

**类比的局限：**目录中的业务名称不能证明服务满足特定法院的执照规定或对某客户拥有文件访问权限。

## 3. 技术原理与核心内容

在 A2A Card 的 `skills` 数组中，每项最少有 id、name、description、tags，可提供 examples、inputModes、outputModes、securityRequirements。Client 根据用户任务与 Skill 描述匹配，并再次判断 AgentInterface、媒体类型和安全能力是否兼容。服务端执行时不可直接信任模型推断的 skill 权限；须独立做认证与输入 schema 验证，返回结构化产物。

## 4. 工程实践与设计权衡

**工程案例：**企业报销 Agent 发布‘policy_lookup’和‘invoice_parse’两个技能。前者可读取公开政策，后者需要用户授权的发票文件；Client 应按用户真实授权选择，不能只看两个 Skill 都能回答‘报销’而发送全部文件。

**失败模式与验证：**Skill 关键词匹配误路由、输入格式错误、过期技能造成资源不存在、未授权访问专用数据。按多语言查询、近义词、权限制约和不支持媒体类型建立评测。

## 5. 关联知识与易混辨析

Agent Skill 是 Agent Card 中的一项能力；MCP Tool 是可调用工具定义；Agent as Tool 是经理封装子 Agent 的调用设计，不能混成 Skill 的协议表现。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Skill 的 tags 只能辅助路由？** 答：标签是元数据，可能模糊或过期；还需要验证任务契约、媒体类型、权限和实际能力。
2. **问：Agent Skill 是否自动提供一个 tools/call 风格方法？** 答：不是。A2A 以消息/任务交互，MCP tools/call 是另一协议。

## 7. 中等难度考试题（含解析）

1. **题：卡片定义 6 个 Skill，用户任务匹配其中 2 个且只获准用 1 个，应选择几个？** 解：只能选择 1 个授权可用的技能。
2. **题：Task 使用不支持的 image/png 输入，可忽略 Card 的 text/plain 限制吗？** 解：不能，需协商兼容媒体类型或拒绝并说明。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Task、Message、Part 的规范结构。
- [A2A · Core Concepts](https://a2a-protocol.org/latest/topics/key-concepts/)：卡片、消息、产物与工作单元。
