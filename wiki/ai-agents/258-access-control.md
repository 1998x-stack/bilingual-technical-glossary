# Access Control（访问控制）

> AI Agents · 专题：安全防护与治理 · 执行器独立校验身份、资源归属和最小权限

## 1. 核心定义

**Access Control（访问控制）**：Access Control（访问控制）是系统依据可信身份、对象属性、资源归属和操作上下文，决定 Agent 是否允许读取、修改或执行某项能力的强制机制。它适用于工具调用、检索资料、文档访问、工作流状态恢复和跨 Agent 消息等多个入口。

**适用边界：**控制必须发生在最终执行与数据读取端，而非仅靠前端隐藏按钮或模型提示。RBAC、ABAC、ReBAC 等是不同建模方式，具体选择应适应业务；任何一种都不自动解决权限缓存陈旧和多租户对象隔离。

## 2. 形象理解

像图书馆不是只在入口看一次借书证，还会根据每本特藏书的借阅条件决定是否允许借走。

**类比的局限：**同一员工能进入图书馆不意味着有权读取全部保密档案；资源属性和时间也会影响许可。

## 3. 技术原理与核心内容

定义 PEP（Policy Enforcement Point）在 tool/resource endpoint 阻断请求、PDP（Policy Decision Point）读取可信属性与政策计算 permit/deny。`allow(subject,action,resource,environment)` 中包含 tenant、role、resource_owner、approval_version 和 session_context，默认拒绝不完整请求。针对间接对象引用 IDOR，应在每次对象查找后核对所有权，不可仅依赖 URI 不可猜测性。审计 rule_id 与 decision，权限变更必须触发缓存失效。

## 4. 工程实践与设计权衡

**工程案例：**Agent 帮用户读取 GitHub Issues 列表，仓库 A 和 B 的 issue ID 都可能为 42。即使模型拿到 B 的 ID，Server 仍需确定当前 token 是否可访问 B；不能靠 UI 当前显示仓库 A 就推测该查询合法。

**失败模式与验证：**跨租户 IDOR、服务之间信任客户端角色、默认 allow、从工具结果解析‘我已授权’并放行、缓存 ACL 旧值。建立访问矩阵与撤权后重复查询负例。

## 5. 关联知识与易混辨析

Access Control 是执行决策和拦截机制；Authentication 先识别主体；Authorization 是具体许可判断；Sandbox 是限制运行时行为的隔离环境，不能代替对象级 ACL。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么前端按钮隐藏不构成访问控制？** 答：攻击者或模型仍可直接调用 API，必须在服务端对真实主体和对象执行授权检查。
2. **问：RBAC 与 ABAC 有什么关键区别？** 答：RBAC 基于角色赋权，ABAC 根据主体、对象、环境等属性判断，复杂资源级约束常需要后者或组合模型。

## 7. 中等难度考试题（含解析）

1. **题：角色可读 5 个项目，但用户的租户只拥有其中 3 个，实际可读项目最多多少？** 解：交集最多 3 个，仍可能有额外条件。
2. **题：访问检查需四个条件 AND，任何一个缺失时应如何决策？** 解：拒绝并记录缺失原因，敏感操作按 fail-closed。

## 8. 权威来源与延伸阅读

- [OWASP · Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)：默认拒绝、逐次检查和最小权限。
- [NIST SP 800-207 · Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)：每次访问核验、最小权限和边界防护。
