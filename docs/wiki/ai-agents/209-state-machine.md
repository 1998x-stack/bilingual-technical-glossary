# State Machine（状态机）

> AI Agents · 专题：执行状态、持久化与恢复 · 跨 Agent 状态、授权与可靠执行的工程边界

## 1. 核心定义

**State Machine（状态机）**：State Machine（状态机）是一种以有限或结构化状态集合、事件/动作及合法转移规则描述系统行为的形式化模型。Agent 工作流和 A2A Task 都可以用状态机刻画，以阻止无效跳转、维持任务安全不变量和可恢复的执行记录。

**适用边界：**状态机本身只是逻辑模型，不能保证持久化、幂等或真实外部事务；若需要跨进程恢复，还须 checkpoint、事件日志和后置条件验证。A2A 任务的枚举状态仅是某个具体协议的状态机实例，并不涵盖所有内部 Agent 状态。

## 2. 形象理解

像交通灯的红黄绿转换规则，明确何时能进入下一状态；无法仅根据‘应该绿灯了’推断路口真的安全。

**类比的局限：**规则描述正确仍可能因信号灯硬件损坏或传感器错误失效，执行必须核验外部事实。

## 3. 技术原理与核心内容

状态机记为 M=(S,Σ,δ,s0,F)，S 为状态集合，Σ 为事件，δ:S×Σ→S 为有条件转移函数，s0 初始态，F 终态集合。实现可用 transition table 约束 SUBMITTED→WORKING→COMPLETED/FAILED 等路径，禁止从 COMPLETED 静默回退 WORKING。并发更新使用 expected_version/CAS，外部写入通过 idempotency_key 与真实事务 ID 关联。Graph 节点和状态字段要区分，某个 LLM 声明并不自动触发状态转移。

## 4. 工程实践与设计权衡

**工程案例：**自动化发布流程中，状态 pending_build→testing→awaiting_approval→deploying→verified；任何未通过审批就转到 deploying 的事件被状态机拒绝。重启后从 checkpoint 继续，但若部署状态 unknown 应先查询平台实际版本。

**失败模式与验证：**跳过审批 gate、事件乱序、重放请求产生双付款、终态被旧消息覆盖、状态字段未持久化。用 property-based tests、非法状态边、并发 CAS 失败及故障注入验证。

## 5. 关联知识与易混辨析

State Machine 描述合法转移；State Graph 可以在节点/条件边上实现复杂处理；Checkpoint 是时点状态快照；Task State 是协议中某个状态值。

## 6. 中等难度面试题（含参考答案）

1. **问：状态机与 checkpoint 解决的是同一个问题吗？** 答：不是，状态机规定什么可转，checkpoint 记录某时刻状态以恢复；两者需要配合。
2. **问：为什么不能从 COMPLETED 因一条旧事件回退 WORKING？** 答：这违反合法生命周期且可能重复执行动作，需要版本顺序与权威终态检查。

## 7. 中等难度考试题（含解析）

1. **题：状态集合有 5 个值，合法有向边 6 条，是否必然存在循环？** 解：不必然，需检查具体边，不能只看数量判定。
2. **题：订单状态从 pending→approved→paid，共发生几次状态转移？** 解：2 次；不代表每次外部操作都已被真实验证。

## 8. 权威来源与延伸阅读

- [LangGraph · Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)：状态图、节点和条件边。
- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：绑定、能力声明与任务接口。
