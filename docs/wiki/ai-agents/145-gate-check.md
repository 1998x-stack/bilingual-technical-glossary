# Gate Check（门控检查）

> AI Agents · 专题：工作流与编排模式 · 图编排、同步和权限边界；SDK 特性以对应版本文档为准

## 1. 核心定义

**Gate Check（门控检查）**：Gate Check（门控检查）是在工作流进入下一阶段前，对必要条件、证据、资源权限、质量标准或人工批准进行强制验证的控制点。它既可以是程序化谓词，也可以组合专业评审，但对安全关键约束应由执行器硬性执行。

**适用边界：**Gate Check 不等于简单的模型自评或一条提示词；一个检查通过不能代表全部后续风险都消失，实际执行时仍需复核权限和当前状态。

## 2. 形象理解

像机场登机前查证件、登机牌和安全要求；任一强制条件不满足就不能放行。

**类比的局限：**通过登机口不代表飞机已抵达目的地；门控检查只确保阶段前置条件，不是最终业务验收。

## 3. 技术原理与核心内容

可定义 gate(state)=all(required_preconditions) && authorized(action,resource) && evidence_verified；输出 `pass | reject | pending` 以及 reason_codes、checked_version 和审计时间。模型评分可以作为辅助信号，写操作必须经过身份/业务权限检查。异步人工审批需要可恢复 waiting_approval 状态、批准有效期和具体参数快照，防止批准后目标变化产生 TOCTOU。

## 4. 工程实践与设计权衡

**工程案例：**支付 Agent 在最终提交前核对用户身份、收款账户、金额、风控评分和明确审批；如果审批时金额为 500，而提交时参数变为 800，gate 必须拒绝而不是复用旧批准。

**失败模式与验证：**只检查‘模型说通过’、不覆盖 unknown、审批签名与参数版本不绑定、没有审计记录、失败仍继续。测试数值边界、权限过期、并发修改与越权路径绕过。

## 5. 关联知识与易混辨析

Gate Check 是阶段性可否继续的判定；Conditional Branch 选择不同后继；Termination Condition 决定整个 Agent 是否结束；Human-in-the-loop 是某些 gate 的审批来源。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么门控要绑定本次实际参数与资源版本？** 答：否则批准可能对已变更的金额或资源生效，存在典型 TOCTOU 风险；必须核对实际即将执行的对象与范围。
2. **问：什么情况下 gate 需要 pending 而不是 pass/fail 二值？** 答：外部审批或异步验证仍未完成时，不能把未知当允许，也未必已经确定拒绝。

## 7. 中等难度考试题（含解析）

1. **题：付款审批阈值是金额严格大于 500 元才需复核，500 与 501 分别如何？** 解：按该单一阈值 500 不触发，501 触发；二者仍需其他权限和风控条件。
2. **题：5 个强制 gate 条件中 4 个通过、1 个未知，是否可以继续写入？** 解：不可以。all-of 条件未全部满足，应 pending 并核查未知项。

## 8. 权威来源与延伸阅读

- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：工作流 gate、并行化、循环边界。
- [LangGraph · Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)：状态检查点、恢复与容错。
