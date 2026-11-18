# Conditional Branch（条件分支）

> AI Agents · 专题：工作流与编排模式 · 系统架构与执行依赖；技术语义依具体工具契约验证

## 1. 核心定义

**Conditional Branch（条件分支）**：Conditional Branch（条件分支）是执行流程根据一个可计算的谓词或业务规则，选择不同后继步骤的控制结构。条件通常由当前结构化状态、已验证工具结果或用户批准决定，不应由未经核实的自然语言结果单独控制高风险动作。

**适用边界：**分支只规定怎样选择路径，不代表某条路径必然安全；分支谓词与工具权限、版本和数据时效是不同检查。多个条件重叠时需要清晰的优先级和默认路径。

## 2. 形象理解

像航班登机口按‘证件检查通过’进入登机通道，否则进入人工服务区；不同结果触发不同流程。

**类比的局限：**证件扫描设备可能故障，条件为真还要检查人员是否适用该权限。

## 3. 技术原理与核心内容

例如 `if verified_payment: issue_receipt elif pending: poll_status else: report_failure`。在状态图中边可由 router(state) 决定；条件谓词必须是可测试的稳定字段，处理 missing/unknown/default 情况，避免未覆盖条件直接落入高权限分支。对跨节点共享状态引入状态版本与条件表达审计。

## 4. 工程实践与设计权衡

**工程案例：**报销 Agent 将 status=approved 路由到只允许提交已授权请求的节点，将 status=requires_review 路由人工复核，将 status=denied 路由拒绝回复；若状态未知，不能默认 approved。

**失败模式与验证：**把字符串包含‘成功’当作业务状态，错误条件优先级，边界值漏掉、模型误判触发越权路径。使用决策表、覆盖所有 enum 的单测与 E2E 权限负例。

## 5. 关联知识与易混辨析

Conditional Branch 是 if/else 类型控制；Routing Pattern 可按语义选择不同专业处理器；Control Flow 包括顺序、分支、循环和并发，不只是条件分支。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么必须设计 unknown 分支？** 答：外部系统可能超时或返回不完整，未知不能被当成 true 或 false 的高风险动作依据，应进入查询/人工复核。
2. **问：状态图中的条件边能否直接使用模型自评‘已经通过’？** 答：不能对重要业务步骤直接依赖模型自述；应通过确定性规则和权威来源检查。

## 7. 中等难度考试题（含解析）

1. **题：订单状态为 approved、pending、denied 的概率分别 0.6、0.3、0.1，100 次独立请求的期望进入 approved 分支次数？** 解：100×0.6=60 次，实际次数会有波动。
2. **题：分支代码 `if x>=10: A else: B`，x=10 会走哪里？** 解：走 A；边界条件为大于等于。

## 8. 权威来源与延伸阅读

- [LangGraph · Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)：有向状态图、节点、边与循环路由。
- [Anthropic · Building effective agents](https://www.anthropic.com/research/building-effective-agents)：顺序链式、路由与编排工作流。
