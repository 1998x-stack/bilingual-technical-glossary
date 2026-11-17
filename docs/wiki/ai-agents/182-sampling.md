# Sampling（采样请求）

> AI Agents · 专题：MCP：模型上下文协议 · 以 2026-07-28 规范为当前基准，区分 legacy 模式

## 1. 核心定义

**Sampling（采样请求）**：Sampling（采样请求）原指 MCP Server 借用 Client/Host 持有的模型能力完成一次模型生成，旧版常见方法 `sampling/createMessage`。从 MCP 2026-07-28 起，这一特性已正式标注 deprecated，仍提供迁移期兼容。

**适用边界：**旧版允许关联现有调用的 server→client 请求；新版无会话协议不再发送这类主动 RPC，新 Server 更推荐直接通过受控 API 调用模型提供方，特殊兼容场景可使用 `input_required` 的 MRTR。

## 2. 形象理解

像受委托写报告的服务在中途向委托人借用一个语言专家，得到的是建议，不是业务审批。

**类比的局限：**模型可能虚构答案或处理隐私数据，是否允许采样、选择模型及收费必须清楚。

## 3. 技术原理与核心内容

legacy 请求可包含 messages、模型偏好和输出约束，Host 决定是否受理。现代服务可以返回 `resultType:input_required`，客户端再以 `inputResponses` 和不可信 opaque `requestState` 重试原请求；需要次数上限与状态校验。优先的现代设计是服务端自行按权限使用 LLM provider API，记录 token 成本、模型版本及来源。

## 4. 工程实践与设计权衡

**工程案例：**合同解析工具需概括五页条款：旧版可请求 Host 模型产生摘要，现代 MCP Server 更宜通过自己的受控模型接口完成，且先最小化传入的敏感字段。最终合同金额仍须原文定位验证。

**失败模式与验证：**把 deprecated API 当推荐新能力、无界多轮采样、将低信任检索文本提升为指令、采样结果未经验证写进支付表。通过拒绝、超时、版本与预算耗尽测试。

## 5. 关联知识与易混辨析

Sampling 是请求模型生成；Elicitation 请求人补充信息；MCP Prompt 是可复用模板。三个对象的权限与生命周期都不同。

## 6. 中等难度面试题（含参考答案）

1. **问：2026 规范中 sampling/createMessage 的状态是什么？** 答：已弃用但兼容，新的实现推荐直接调用模型提供方 API，不应依赖旧的主动请求模型。
2. **问：为什么采样回复不能证明用户已授权付款？** 答：生成文本不等于可信用户确认，执行必须依真实凭证与服务端校验。

## 7. 中等难度考试题（含解析）

1. **题：采样一次输入 700、输出 300 token，重复 4 次共多少？** 解：4×(700+300)=4000 token。
2. **题：最多 MRTR 3 轮，第 3 轮仍未满足要求可以无限继续吗？** 解：不能，应终止为 incomplete 或安全降级。

## 8. 权威来源与延伸阅读

- [MCP Python SDK · Sampling/roots](https://py.sdk.modelcontextprotocol.io/v2/handlers/sampling-and-roots/)：弃用但仍兼容。
- [MCP · 2026 release](https://blog.modelcontextprotocol.io/posts/2026-07-28/)：无会话与多轮输入。
