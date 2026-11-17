# AI Agents · 第 3 批（041–060）综合学习路径（仅供编审）

> 本研究路线来自 [AI Agents 原词表](../../glossaries/ai-agents.md) 第 041–060 条，供内容审稿与课程设计。公开页面继续保持**术语 → 详情**，不暴露 Batch 信息或编辑进度。

## 贯穿主线

建立一条可验证的长链路：

`Uncertainty → Confidence Calibration → Planning → Task Decomposition → Hierarchical Planning → High-level Plan → Action Plan → Adaptive Planning → Plan Revision → Task Dependency → Task Priority → Decision Point → Action Space / State Space → Policy → Utility Function → Reward Signal → Search Space → Heuristic Search → Lookahead Search`

它涵盖从**不知道什么**、到**规划要做什么**、再到**怎样选择动作**与**怎样验证行为的后果**。两个重要边界：

- 业务权限/安全是硬约束，应在计算效用、优先级或模型决策之前过滤；模型的概率/奖励分数不构成执行许可。
- 计划与实际环境不同步时，先确认已发生的外部副作用，再修订尚未完成的节点；不可直接重播整条任务链。

## 原理地图与跨概念辨析

| 研究问题 | 核心术语 | 要验证的事实 |
|---|---|---|
| 如何判断模型“知道自己不知道”？ | Uncertainty、Confidence Calibration | 置信度的校准不等于高准确率；ECE 依赖分桶与校验样本 |
| 长任务如何展开？ | Planning、Task Decomposition、Hierarchical Planning | HTN 分解/任务依赖满足性优先于自然语言的表面合理性 |
| 环境变化后怎么调整？ | Adaptive Planning、Plan Revision | 已执行副作用不可当作可安全重播的文本步骤 |
| 哪个任务优先？ | Task Dependency、Task Priority、Decision Point | 先检查就绪/授权，再给可执行节点排序 |
| 怎样定义可选动作与世界？ | Action Space、State Space、Policy | MDP 策略只是决策映射；部分观察不等于真实状态 |
| 怎样选择好解？ | Utility Function、Reward Signal、Search Space、Heuristic Search、Lookahead Search | 效用、即时奖励、搜索代价和可验证目标是不同概念 |

## 综合案例：库存调拨 Agent

用户要求在预算 5000 元内将三个仓库库存调拨到目标门店，且严禁重复出库。

1. **建模**：库存数量、在途状态、已提交事务 ID 组成状态；网络响应缺失归为 unknown，不应猜测“失败”。
2. **规划**：先查询库存/限额，再估算运输，再选调拨方案；创建 DAG，只把已就绪的节点送入调度。
3. **决策**：合法动作先做权限、库存与预算过滤；对合法候选计算成本/缺货风险，再由策略选择。
4. **执行与修订**：工具超时先按幂等键查账；若库存变动，保留已完成事务，只修订受影响节点及下游。
5. **结束验收**：通过权威库存记录、调拨事务状态与门店签收确认，而非模型声称“任务完成”。

## 中等难度综合面试题

**问：**为什么一个能用 A* 找到低成本路线的 Agent 仍可能在真实生产中造成重复调拨？

**答：**A* 只在其图模型、成本及最优性条件下解决搜索问题；业务副作用执行仍需后端事务、幂等键、权限与状态恢复。重试时把工具超时误判为“未提交”可能重放动作。应将计划优化、执行控制和权威状态验证分开设计。

## 中等难度综合考试题

**题：**库存调拨计划中，步骤 A 查询仓库需要 2 s，B 与 C 分别计算两条运输方案需要 4 s 与 3 s（均依赖 A，可并行）；D 审批需要 5 s（依赖 B、C）。求无资源争用时的关键路径时延。若提交审批前又需要 1 s 的权限检查，新的总时延是多少？

**解：**原 DAG 的关键路径 A→B→D，耗时 `2+4+5=11 s`；权限检查若在 D 之前串行执行，增至 `11+1=12 s`。该算例是教学假设，不是实际系统的测量数据。安全检查不可为节省 1 s 而省略。

## 参考资料

- [Russell / Norvig · Artificial Intelligence: A Modern Approach（第 4 版）](https://aima.cs.berkeley.edu/)：第 3、11、12、15–16 章
- [Sutton / Barto · Reinforcement Learning: An Introduction（第 2 版）](https://mitpress.mit.edu/9780262039246/reinforcement-learning/)：MDP、Policy、Reward
- [Guo 等 · On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html)：校准定义与方法
- [Georgievski / Aiello · HTN Planning（2015）](https://www.sciencedirect.com/science/article/pii/S0004370215000247)：分层规划
- [Fox / Long · PDDL2.1（2003）](https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume20/fox03a-html/JAIRpddl.html)：动作时序与资源
- [Hart / Nilsson / Raphael · A*（1968）](https://doi.org/10.1109/TSSC.1968.300136)：启发式搜索
