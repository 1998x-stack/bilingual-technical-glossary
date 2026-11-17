# Capability Declaration（能力声明）

> AI Agents · 专题：A2A：智能体间协议 · 跨 Agent 状态、授权与可靠执行的工程边界

## 1. 核心定义

**Capability Declaration（能力声明）**：Capability Declaration（能力声明）是远程 Agent 在 Agent Card 中公开自身支持的协议绑定、流式/推送特性、技能、媒体类型和扩展范围，使 Client 在实际调用前做兼容性与适用性判断。它属于接口元数据，不是对每个用户的授权证明。

**适用边界：**`capabilities.streaming` 或 `pushNotifications` 只表示 Server 宣告支持相应操作，是否执行仍取决于 Client 选择的绑定和用户权限。Agent Card 应随版本更新，不能因上一次返回成功就长期忽略新能力。

## 2. 形象理解

像产品技术规格表列出支持蓝牙和 Wi-Fi，却并不意味着访客有权使用内部管理网络。

**类比的局限：**规格书可能是旧版，实际设备可能关闭了某个功能，仍需探测运行状态。

## 3. 技术原理与核心内容

Card 中 `supportedInterfaces` 声明 binding/endpoint/protocolVersion，`capabilities` 声明 streaming、pushNotifications、extensions 等，`skills` 含可支持任务。Client 判断功能交集并遵循必需扩展；Server 在请求时再次校验 capability，未支持 streaming/push 时返回规范错误。使用 version 与 ETag 更新卡片，安全敏感描述只在认证的扩展卡片提供。

## 4. 工程实践与设计权衡

**工程案例：**一个企业报告 Agent Card 声明支持推送通知但不支持 streaming。Client 为异步任务配置经认证 webhook 而非强行请求 SSE；如果当前用户未授权读取报告，Server 应拒绝，即便能力声明为 true。

**失败模式与验证：**能力夸大、部署后忘记更新 Card、扩展 required 条件被忽略、缓存跨用户泄漏敏感技能、以 declared=true 跳过 resource ACL。做功能矩阵、能力关闭、Card 过期和越权测试。

## 5. 关联知识与易混辨析

Capability Declaration 是对外宣告功能；Agent Skill 是具体可办理的工作类型；Agent Discovery 负责寻找卡片；授权负责允许谁访问什么。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 streaming=true 不代表所有用户都能获取实时数据？** 答：能力支持与权限分离，服务端仍须验证任务与用户范围。
2. **问：Client 遇到不支持的 required 扩展该怎么办？** 答：应拒绝不兼容调用或按明确契约降级，不能默默忽略必要约束。

## 7. 中等难度考试题（含解析）

1. **题：Client 支持 streaming 和 push，Server 只支持 push，共同可用能力？** 解：只有 push。
2. **题：卡片列出 5 个 Skill，但本用户可见 2 个，应按几个进行最终授权路由？** 解：最多 2 个，并在调用时再次校验。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：绑定、能力声明与任务接口。
- [A2A · Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/)：可信卡片、能力与来源。
