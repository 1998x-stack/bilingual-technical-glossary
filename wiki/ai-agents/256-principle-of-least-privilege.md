# Principle of Least Privilege (PoLP)（最小权限原则 · PoLP）

> AI Agents · 专题：安全防护与治理 · 执行器独立校验身份、资源归属和最小权限

## 1. 核心定义

**Principle of Least Privilege (PoLP)（最小权限原则）**：Principle of Least Privilege（PoLP，最小权限原则）要求给 Agent、用户、服务账户或工具的权限严格限定为完成当前任务所需的最小操作、资源、时间和范围，以减少误操作和模型受攻击后产生的后果。它是执行层安全设计原则，不是一条提示词提醒。

**适用边界：**最小权限不意味着所有 Agent 永远只读：当任务合法需要写入时，可经过独立审批授予短时、单对象、参数绑定的写权限。执行后的权限应按需要撤回，不能因为模型声称用户同意就永久保存管理员 token。

## 2. 形象理解

像工程师临时领取某机房某柜的钥匙，只能在维护窗口打开指定机柜，而不是得到整个园区的万能钥匙。

**类比的局限：**任务范围改变时可能需要新的授权，过度狭窄的权限也会影响正常工作，需可审计的申请流程。

## 3. 技术原理与核心内容

定义 Capability={subject,action,resource,tenant,expires_at,constraints}，使用资源级 ACL、短时凭证和服务端 scope 校验，在每次 tool call 重新验证，而非仅在 `tools/list` 过滤。不同 Agent 与 Server 使用各自的最小权限 token，避免 token passthrough 与 confused deputy。定期清点未使用权限，删除共享 admin key；对付款/删除使用 action-specific approval_hash。

## 4. 工程实践与设计权衡

**工程案例：**代码分析 Agent 只需读取指定仓库的指定 commit，不应提供 push、合并 PR 或删除分支的权限。需要写测试 PR 时先经过可验证的审批，授权限定目标 repo、分支和时间窗口。

**失败模式与验证：**应用用 root 凭证执行只读搜索、所有子 Agent 继承主 Agent 的权限、长期 token 存入提示、权限撤销但缓存仍允许操作。测试横向越权、撤权、过期和错误 tenant。

## 5. 关联知识与易混辨析

PoLP 是权限最小化原则；Permission Scope 是某凭证的具体范围；Access Control 是强制决策机制；Sandbox 限制运行时资源，两者应联合使用。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么最小权限是应对 prompt injection 的关键控制？** 答：即使模型被恶意资料诱导，执行层没有越权能力就不能直接删除或泄漏无权资源。
2. **问：为什么工具说明里写‘只读’不等于真正只读？** 答：说明由外部服务提供且可能过时或恶意，需后端校验真实允许动作和权限。

## 7. 中等难度考试题（含解析）

1. **题：一个工具可操作 100 个仓库，用户任务仅需访问 2 个，原则上应该授权多少？** 解：只授权需要的 2 个及对应操作，不开放另外 98 个。
2. **题：用户对文件 A 有 read，但没有 write，模型生成写请求，后端应如何处理？** 解：拒绝写操作，不能因模型输出合法 schema 就批准。

## 8. 权威来源与延伸阅读

- [NIST SP 800-207 · Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)：每次访问核验、最小权限和边界防护。
- [OWASP · Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)：默认拒绝、逐次检查和最小权限。
