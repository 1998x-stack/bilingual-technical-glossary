# Reviewer Agent（审查者智能体）

> AI Agents · 专题：多智能体协作 · 工程角色定义；职责、权限与真实验收依具体系统为准

## 1. 核心定义

**Reviewer Agent（审查者智能体）**：Reviewer Agent（审查者智能体）是对其他 Agent 的交付物进行独立质量检查、证据核验和规范符合性评估的角色。它可以产出可定位的缺陷、测试结果和修改建议，但通常不应自动替代真实专家或业务审批签核。

**适用边界：**Reviewer 的‘独立’是职责和输入隔离程度，不自动意味着模型误差独立。尤其法律、医学、安全等领域，LLM 评审通过不等于获得专业认证；审稿台账不能伪造 reviewer 身份和 SHA。

## 2. 形象理解

像代码 PR 由另一位工程师检查类型、性能与安全，而不是只问作者自己‘是否写得好’。

**类比的局限：**审查者可能与作者共享误解；若看不到原始源代码和可执行测试，仅对摘要评论会遗漏关键问题。

## 3. 技术原理与核心内容

定义 ReviewRequest={artifact_id,revision,requirements,source_refs,rubric}，输出 finding 列表（location,severity,evidence,fix）和 decision（pass/needs_changes/unknown）。对可验证项运行脚本、单测、schema 和源引用匹配；对于高主观风险使用人工复核。每轮改稿须使旧 review 失效或绑定新 artifact SHA，阻止‘旧通过’沿用到新版本。

## 4. 工程实践与设计权衡

**工程案例：**技术 Wiki 30 篇稿件由 Reviewer 对逐篇中英文定义、公式、URL、例题和镜像哈希生成机器审查结果。专业专家尚未签核前，review ledger 保持 pending；只把 CI green 标记为结构校验通过。

**失败模式与验证：**只按文章长度评分忽略事实错误、引用链接存在但不支持论断、把一篇评审结论套到全部文件、审稿 SHA 不匹配。针对错误数学、故意无效证据及权限字段缺失设置负面测试。

## 5. 关联知识与易混辨析

Reviewer Agent 按验收标准评审具体产物；Critic Agent 更强调找弱点与改进方向；Supervisor Agent 关注整个任务过程；Human Expert Review 是另一层真实专业责任。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 Reviewer 的评审应绑定 artifact SHA？** 答：内容修改后旧意见可能不再适用，绑定哈希可防止已通过的评价被错误套用到新版本。
2. **问：引用 URL 可以打开，是否证明技术断言有据可查？** 答：不能，还须检查具体正文片段、适用版本及结论是否从来源正当推出。

## 7. 中等难度考试题（含解析）

1. **题：30 篇正文中 27 篇镜像与源稿逐字节相同，镜像一致率？** 解：27/30=90%；剩余 3 篇必须修复后才算完整通过。
2. **题：Reviewer 发现数学题算错但模型自评‘优秀’，应该记录什么？** 解：记录可复算错误和未通过状态，不应根据语言流畅性覆盖确定性验收失败。

## 8. 权威来源与延伸阅读

- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：编排者—工作者与评估者—优化者工作流。
- [W3C · PROV-O](https://www.w3.org/TR/prov-o/)：活动、实体及责任主体的证据追踪。
