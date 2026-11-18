# Authorization（授权）

> AI Agents · 专题：MCP：模型上下文协议 · MCP 2026-07-28 及兼容边界；示例数字为教学题设

## 1. 核心定义

**Authorization（授权）**：Authorization（授权）是基于请求者身份、被访问资源、操作及上下文来判定是否允许读取或执行 MCP 能力的机制。认证证明‘是谁’，授权判定‘能够对哪个对象执行什么’，用户意图确认又是第三层独立约束。

**适用边界：**MCP 的 OAuth 类规范针对 HTTP transport 的受保护资源；2026-07-28 仍将授权设计为可选能力。stdio 通常通过进程环境凭证与执行层权限管理，而不应强行套用 HTTP OAuth 重定向流程。任何协议功能发现都不能替代服务端对象级 ACL。

## 2. 形象理解

像企业门禁系统先核实员工工牌，再判断当前员工是否能进入某机房；能进门也不代表可拆卸设备。

**类比的局限：**同一账户能看数据，不意味着可批量删除；token 泄露、过期和跨服务使用都可能造成越权。

## 3. 技术原理与核心内容

HTTP MCP Server 作为 OAuth Resource Server 验证 access_token 的 issuer、audience/resource、expiry 与 scope；Client 使用受信任授权服务器信息，防止混淆攻击。对读取 `orders/123` 做 owner/tenant ACL，对写入工具额外检查 action、参数、审批与幂等键。不得把客户端自报权限或工具描述里的‘已授权’当依据，日志要避免打印完整 bearer token。

## 4. 工程实践与设计权衡

**工程案例：**财务 Agent 接入 ERP MCP Server，用户 A 仅有读取本人订单能力。模型尝试调用 refund(他人订单)，Server 在资源层拒绝，Host 也应显示缺授权；工具存在不等于用户获准执行。

**失败模式与验证：**跨服务 token passthrough、scope 过宽、缓存旧授权、只在 tools/list 过滤不在 tools/call 检查、Host 提示词被注入。用跨租户 IDOR、过期 token、权限撤销和错误 audience 测试。

## 5. 关联知识与易混辨析

Authentication 是识别主体；Authorization 是资源操作许可；User Consent 是明确用户同意；Capability Negotiation 是技术能力声明，不是授予实际权限。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 tools/list 已隐藏退款工具还要在 tools/call 验证权限？** 答：客户端能伪造 RPC/使用旧缓存，Server 必须独立阻止没有授权的真实业务动作。
2. **问：stdio MCP Server 是否应一律执行 OAuth 浏览器重定向？** 答：不是，HTTP 授权规范不适合直接照搬到 stdio，通常基于进程环境与服务器执行权限设计。

## 7. 中等难度考试题（含解析）

1. **题：5 个资源中用户获准访问 2 个，资源权限覆盖率？** 解：2/5=40%；这不是可用性指标。
2. **题：token 的 issuer 与预期不一致，即便 scope 字符串相同可以接受吗？** 解：不可以，必须核对签发者及目标资源。

## 8. 权威来源与延伸阅读

- [MCP · Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)：OAuth 资源服务器与安全约束。
- [RFC 8707 · Resource Indicators](https://www.rfc-editor.org/rfc/rfc8707)：访问令牌 audience/resource 绑定。
