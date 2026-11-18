# Safety Confirmation（安全确认）

> AI Agents · 专题：安全防护与治理 · 明确安全边界、执行权限与可验证的用户决定

## 1. 核心定义

**Safety Confirmation（安全确认）**：Safety Confirmation（安全确认）是在 Agent 即将执行高影响、不可逆或超出日常预期的动作前，向具备权限的用户清楚展示目标资源、具体参数、风险和后果，并获取明确、可验证的继续执行决定。它不是对用户‘在吗’式的笼统发问。

**适用边界：**确认动作必须和 AuthN、AuthZ、真实业务执行器配合；用户点击确认不自动获得任何资源权限。对付款、删除生产资源等操作，应绑定操作 SHA/arguments_hash、审批有效期、resource_revision，参数变化后不得复用旧确认。

## 2. 形象理解

像银行转账最后一步展示收款人、账号尾号与金额，让用户确认确实是这笔交易，而不是确认‘允许所有以后转账’。

**类比的局限：**确认的人可能被骗，界面可能展示不完整信息，仍要强制政策限制、反欺诈检查与权限核验。

## 3. 技术原理与核心内容

构造 Confirmation={actor_id,action,resource_id,arguments_hash,policy_version,expires_at,nonce,decision}。Host 展示有效参数、可能副作用和取消选项；通过用户明确交互签署，后端验证可信身份、时间窗、nonce、目标参数和 object_acl，再提交真实操作。拒绝、超时、参数变更皆 fail-closed；不允许模型从自由文本中自行推断‘已批准’。同时记录工具与交易 ID，区分确认成功和交易最终完成。

## 4. 工程实践与设计权衡

**工程案例：**运维 Agent 提议删除 staging 环境三台测试机器，确认界面精确列出资源 ID、环境与不可逆数据影响。若 Agent 在执行前把 staging 改成 production，参数哈希不匹配，后端必须阻止删除并重新确认。

**失败模式与验证：**批准界面不显示收款人、确认状态无限有效、另一个 Agent 用同名工具复用批准、点击后 UI 假装成功却未提交。测试目标资源突变、拒绝、过期和跨用户重放。

## 5. 关联知识与易混辨析

Safety Confirmation 是对具体高后果动作的确认；Human Approval 更强调具有职权的审批主体；Guardrail 是各阶段保护；AuthZ 决定真实资源许可。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么确认必须绑定具体参数哈希？** 答：防止用户确认的金额/目标和模型最终执行内容不同，形成审批漂移。
2. **问：用户确认后系统凭证过期还能执行吗？** 答：不能，执行端仍需有效认证授权；确认不能替代资源权限。

## 7. 中等难度考试题（含解析）

1. **题：审批确认金额 300，执行请求变为 500，应怎样处理？** 解：拒绝旧确认、要求重新授权。
2. **题：一个批量删除动作包含 5 个明确资源，执行前发现资源列表增加 1 个，可以沿用原批准吗？** 解：不能，应按最新列表重新展示风险和获得有效确认。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)：工具批准、拒绝与暂停恢复。
- [OWASP · Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)：执行端每次授权和默认拒绝。
