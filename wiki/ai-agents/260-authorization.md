# Authorization (AuthZ)（访问授权 · AuthZ）

> AI Agents · 专题：安全防护与治理 · 执行器独立校验身份、资源归属和最小权限

## 1. 核心定义

**Authorization (AuthZ)（访问授权）**：Authorization（AuthZ，访问授权）是对已建立或可信绑定的主体身份，在具体操作、资源和上下文下是否被许可的判断。它是 Agent 执行工具、读取资料、修改状态或触发外部事务时必须具备的服务端保护，而不是模型自述已获批准。

**适用边界：**与 MCP Authorization 词条相关，但这里讨论跨 Agent 系统通用的 AuthZ；OAuth scopes 只是判断输入之一，不能跳过数据库 owner/tenant ACL。用户审批、模型规则解释、服务端授权和工具业务成功是四种不同状态。

## 2. 形象理解

像登机时工作人员先确认旅客身份，再判断其是否持有该航班与座位的有效登机资格；同名旅客不能坐上任意飞机。

**类比的局限：**授权与资格可能随时间、票务状态和取消动作改变，出示旧许可不代表当前仍有效。

## 3. 技术原理与核心内容

在每次执行端调用 `authorize(subject,resource,action,context)`，决策遵循 default-deny。可信身份来自登录/工作负载 token；资源通过 owner、tenant、classification 和 revision 绑定；策略还包括时间、金额、审批范围。对跨服务 MCP/A2A 工具设置目标 audience，避免 token passthrough；敏感动作要求 parameter_hash 与审批签名，检查时点与执行时点版本变化，防 TOCTOU。记录 permit/deny 与 policy_version 供审计。

## 4. 工程实践与设计权衡

**工程案例：**代码 Agent 持有只读 Git token，用户说‘快合并 PR #52’。系统先识别仓库资源、真实 Git 权限与合并策略；没有 write/merge 许可时必须拒绝执行或请求合法的额外授权，即便 CI 全绿也一样。

**失败模式与验证：**只在服务启动时检查权限、工具列表缓存跨用户、仅凭‘管理员’提示词授权、审批绑定旧 commit SHA、未经权限查询就调用删除 API。以 revoke、跨租户、参数突变和错误 target resource 验证。

## 5. 关联知识与易混辨析

AuthZ 是一次操作是否允许的判定；AuthN 是主体身份认证；Scope 是授权范围表达；Guardrail 是前后处理阶段检查，不能取代后端真实授权。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 AuthZ 必须对每个对象分别检查？** 答：相同 API 不同对象有不同 owner、tenant 与分类，允许调用方法不代表对所有资源都有权。
2. **问：用户批准删除文件 A，Agent 将参数改为文件 B 能使用旧批准吗？** 答：不能；批准与对象和参数哈希绑定，变更必须重审且执行器继续查 ACL。

## 7. 中等难度考试题（含解析）

1. **题：token 有 tools:write scope，但资源 ACL 拒绝对目标对象写入，最终授权决策？** 解：拒绝，必要条件未全部满足。
2. **题：策略允许工作日 9:00–17:00 执行变更，18:00 请求即使 role 合法怎么办？** 解：拒绝或走允许的审批/延期流程，不绕过环境条件。

## 8. 权威来源与延伸阅读

- [OWASP · Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)：默认拒绝、逐次检查和最小权限。
- [IETF RFC 6749 · OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)：令牌、scopes 和资源访问授权。
