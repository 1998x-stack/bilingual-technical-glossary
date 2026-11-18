# Permission Scope（权限范围）

> AI Agents · 专题：安全防护与治理 · 执行器独立校验身份、资源归属和最小权限

## 1. 核心定义

**Permission Scope（权限范围）**：Permission Scope（权限范围）是授权系统用来限定某身份能够对哪些资源、采用哪些操作以及在何种上下文使用能力的界限，常表现在 OAuth scope、API token 权限和对象级 ACL 中。Scope 是授权策略的一部分，不是具体任务完成证明。

**适用边界：**OAuth scope 字符串本身不能证明某对象属于该用户：`orders:read` 常仅表明操作类型，还须对象级验证 tenant/order_id。即使 access token 有 scope，也需检查 issuer、audience/resource、有效期和签名。

## 2. 形象理解

像公司门禁卡标有‘可进入三楼’，但三楼的某个受限档案室仍要再核对个人权限。

**类比的局限：**权限范围的名字可能宽泛，服务端仍要理解真实业务语义和用户身份，不能只判断字符串包含 write。

## 3. 技术原理与核心内容

Resource Server 验证可信 access_token、subject、audience、expiry 和 scopes；对每次 operation 计算 `allow=valid_token ∧ action_in_scope ∧ object_acl ∧ business_gate`。在 MCP HTTP 授权场景使用 OAuth Resource Indicators 防止 token 被另一服务复用。用户任务的 repo_id、tenant_id、amount 等必须由可信请求上下文核对，不能只靠模型传入字段。对授权范围变更清理缓存，并用 least privilege 设计短时/可撤权 token。

## 4. 工程实践与设计权衡

**工程案例：**财务 Agent 的 token 具有 `invoices:read`，本轮只能读取公司 A 的发票。模型根据网页提示尝试访问公司 B 的 invoice_id，服务端虽看到相同 scope 仍应因对象级 ACL 拒绝。

**失败模式与验证：**缺 audience 检查被其他服务 token 误用、scope 过宽、只按 URL 前缀判断租户、token 过期但缓存仍有效。做 cross-tenant IDOR、错误资源指示符、撤销后重试测试。

## 5. 关联知识与易混辨析

Permission Scope 表示授予的操作范围；Authentication 判定调用者身份；Authorization 是一次访问许可决策；Agent Capability Declaration 是技术支持声明而非真实访问授权。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 orders:read 不意味着可读任何租户订单？** 答：scope 只是功能类型，还需每次资源归属和租户 ACL 检查。
2. **问：为什么访问令牌要绑定 audience？** 答：阻止某服务签发/使用的 token 被转用到不同资源服务器，减少 token passthrough 风险。

## 7. 中等难度考试题（含解析）

1. **题：一名用户有 read scope 和自己 3/10 个订单的对象权限，可合法读取几个？** 解：最多 3 个，必须同时满足 scope 与对象 ACL。
2. **题：token 已过期但包含 admin 字符串，后端是否应接受？** 解：不应，合法签名、签发者、资源和有效期都是必要条件。

## 8. 权威来源与延伸阅读

- [IETF RFC 6749 · OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)：令牌、scopes 和资源访问授权。
- [IETF RFC 8707 · Resource Indicators](https://www.rfc-editor.org/rfc/rfc8707)：资源 audience 与访问令牌绑定。
