# MCP Prompt（MCP 提示模板）

> AI Agents · 专题：MCP：模型上下文协议 · 依据 MCP 2026-07-28 规范；旧版行为应分别核对

## 1. 核心定义

**MCP Prompt（MCP 提示模板）**：MCP Prompt（MCP 提示模板）是 Server 提供给客户端的可重用提示或消息序列模板，可带命名参数，帮助用户在 Host 中调用标准化的任务指导。它通过 `prompts/list` 发现，并由 `prompts/get` 填入参数生成消息内容。

**适用边界：**Prompt 不是 Tool，也不表示 Server 有权修改 Host 的 system 指令。模板可能来自外部、包含低信任内容，Host 必须决定如何展示、选择和应用；模板内容不应成为执行敏感动作的授权证明。

## 2. 形象理解

像专家机构提供的标准申请表与说明模板，用户选择并填写后由应用按既有规则处理。

**类比的局限：**填写模板不能替代真实身份验证与审批，模板描述本身也可能过期。

## 3. 技术原理与核心内容

服务端注册 prompt name、description 与 arguments，Client 调用 `prompts/list` 发现模板，`prompts/get` 携带参数获取一组消息。Python MCP SDK 的提示函数可返回 str 或消息列表，并可支持用户消息中嵌入资源。现代协议下每请求仍附 `_meta`，提示模板可以配合自动补全但不能把用户提供的字符串无校验地用于高权限 API。

## 4. 工程实践与设计权衡

**工程案例：**软件维护工具提供 `review_diff` Prompt，参数为 git revision 与审查目标；Host 先校验该 revision 是否用户授权访问，再用模板形成审查上下文。即便模板强调‘自动合并’，实际 merge 仍需独立用户授权与 CI gate。

**失败模式与验证：**模板参数导致跨仓库读取、注入不可信引用、误把模板定义当系统指令、会话变更后缓存陈旧。测试参数缺失/非法、权限拒绝、版本过期和恶意模板文本。

## 5. 关联知识与易混辨析

MCP Prompt 是可复用任务输入模板；Tool 是可执行函数；Resource 是可读数据；Prompt Engineering 是设计提示的更广实践，并不等同某个特定协议对象。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 prompts/get 返回消息不应自动成为最高权限系统指令？** 答：服务器提供的是模板化内容，Host 应结合用户选择、信任级别和应用政策决定使用；不能让外部模板突破指令层级。
2. **问：Prompt 与 Resource 的核心区别？** 答：Prompt 组织面向用户/模型的模板消息及参数，Resource 提供由 URI 标识的可读数据；两者可配合但用途不同。

## 7. 中等难度考试题（含解析）

1. **题：一个 Prompt 有两个必填参数 project 和 revision，调用仅提供 project，应如何处理？** 解：应按模板参数契约返回缺参错误，而不能任意假定 revision。
2. **题：模板生成 4 条消息，Host 最终只选 2 条纳入上下文，能说 Server 仅生成 2 条吗？** 解：不能。Server 生成 4 条，Host 选择与实际可见上下文是另外的处理阶段。

## 8. 权威来源与延伸阅读

- [MCP Python SDK · Prompts](https://py.sdk.modelcontextprotocol.io/servers/prompts/)：提示模板、参数及 prompts/list/prompts/get。
- [MCP 2026-07-28 · Specification](https://modelcontextprotocol.io/specification/2026-07-28)：工具、资源、提示的协议定位。
