# Authentication (AuthN)（身份认证 · AuthN）

> AI Agents · 专题：安全防护与治理 · 执行器独立校验身份、资源归属和最小权限

## 1. 核心定义

**Authentication (AuthN)（身份认证）**：Authentication（AuthN，身份认证）是系统验证调用者或执行主体确实拥有所声称身份的过程，可能采用密码/多因素、OAuth/OIDC 令牌、客户端证书或受信任服务账户凭证。它解决‘你是谁’，而不是‘你能操作什么资源’。

**适用边界：**已认证登录不代表获得全部系统权限；模型在文本中自称‘管理员’不是身份证明。不同 Agent 之间的代理认证与最终用户身份可能不同，须避免混淆代理服务 token 与用户委派许可。

## 2. 形象理解

像进入大楼前核验员工证件和二次验证，确认人员身份后仍要检查其能否进入特定实验室。

**类比的局限：**持有证件也可能因被盗、到期或被吊销而无效，认证还需要会话生命周期管理。

## 3. 技术原理与核心内容

对 OIDC/JWT 等验证 signature、issuer、audience、expiry、nonce/绑定上下文，敏感动作可要求 MFA/step-up authentication。服务账户通过工作负载身份而非把长期密钥嵌入 Prompt；TLS 保护传输，私钥/密钥存放在可信安全边界。对浏览器应用的 session 应设置正确 cookie 安全属性与 CSRF 防护。认证结果只提供可信 subject，业务 endpoint 再使用 ACL/ABAC 做 Authorization。

## 4. 工程实践与设计权衡

**工程案例：**Agent 为用户访问云端仓库，Host 通过受支持的登录流程获得有限时效 token；读取私有 repo 前，Git 服务验证 token 的签名与 subject，再检查仓库的 read permission。Agent 无权因用户在消息里复制别人 token 就绕过授权政策。

**失败模式与验证：**缺失 JWT audience 检查、使用日志中的旧 Bearer Token、凭模型输出的用户 ID 假冒登录、混用服务和用户 token。以伪造签名、过期会话、撤销和错 issuer/audience 测试。

## 5. 关联知识与易混辨析

AuthN 证明身份；AuthZ 决定允许操作；Permission Scope 限定权限；Human Approval 是对具体动作的明确许可；四者不能互相替代。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么‘模型知道账号姓名’不等于通过身份认证？** 答：名称只是文本，服务端需要密码学凭证或可信登录会话建立身份。
2. **问：认证成功后为什么还需要 AuthZ？** 答：同一主体对不同资源和动作的权限各异，登录不能证明有访问敏感对象的许可。

## 7. 中等难度考试题（含解析）

1. **题：某系统需 AuthN、AuthZ 两条件同时为真，认证真、授权假时可否读取？** 解：不可以，AND 判定为 false。
2. **题：token 到期时间为 10:00，当前 10:01，在无其他允许宽限的条件下应怎样处理？** 解：视为已过期而拒绝，并通过合法刷新/重新认证流程恢复。

## 8. 权威来源与延伸阅读

- [NIST SP 800-63B-4 · Authentication](https://pages.nist.gov/800-63-4/sp800-63b.html)：认证证明强度、令牌和会话管理。
- [NIST SP 800-207 · Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)：每次访问核验、最小权限和边界防护。
