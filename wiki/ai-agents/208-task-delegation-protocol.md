# Task Delegation Protocol（任务委派协议）

> AI Agents · 专题：A2A：智能体间协议 · 跨 Agent 状态、授权与可靠执行的工程边界

## 1. 核心定义

**Task Delegation Protocol（任务委派协议）**：Task Delegation Protocol（任务委派协议）是对跨 Agent 工作转交时任务目标、输入、身份、生命周期、验收和结果回收的一组约定的泛称。在 A2A 实践中，可以组合 Agent Card 发现、SendMessage、Task/Status/Artifact 和鉴权实现委派，**不是现行 A2A 规范中另立的一个同名必需方法**。

**适用边界：**不能凭“委派协议”四个字虚构 A2A `tasks/delegate` 标准 RPC；具体任务由已支持的 A2A operation 创建并跟踪。管理者与远程 Agent 各保留独立权限，委派不会让下游拥有上游全部数据或付款许可。

## 2. 形象理解

像公司间外包一项审核业务，合同写明任务号、交付物、负责人和时间，而不是把全部内部系统账号交给承包商。

**类比的局限：**任务被对方接收不意味着验收通过；远程报告可能与上游目标不一致。

## 3. 技术原理与核心内容

可约定 Delegation={requester,assignee,task_id,goal,input_refs,scope,deadline,acceptance_tests}，以 Agent Card 的支持能力选择目标，通过 SendMessage 创建/继续 Task，记录 Task ID 与 contextId；远端返回状态和 Artifacts。上游在任务完成后核对 artifact 来源、版本和业务成功谓词。若任务取消、需要授权或未知，要按明确生命周期状态继续处理；重复派发需业务幂等/关联 ID。

## 4. 工程实践与设计权衡

**工程案例：**研发 Agent 让外部兼容性测试 Agent 在特定 commit 上跑测试，发送仓库公开镜像、目标系统版本和测试标准。远端报告 Artifact 含 CI 链接，主 Agent 验证对应 SHA 后决定是否进入人工合并。

**失败模式与验证：**把委派成功当结果完成、任务 ID 丢失、重复执行、远端数据越权、将 Task status=COMPLETED 当测试实际通过。测试中断、失败、重新派单、错 SHA 与媒体类型。

## 5. 关联知识与易混辨析

Task Delegation Protocol 是协作契约泛称；A2A 是具体开放协议；Handoff 还涉及对话控制权转移；Agent as Tool 可实现内部委派而不使用 A2A。

## 6. 中等难度面试题（含参考答案）

1. **问：A2A 是否定义强制名叫 tasks/delegate 的标准方法？** 答：没有，A2A 用 SendMessage、Task 与状态/Artifact 语义承载委派流程。
2. **问：为什么远端返回 COMPLETED 后仍需上游验收？** 答：状态是远端声明，必须核查任务约束、产物内容、来源、提交版本和权限。

## 7. 中等难度考试题（含解析）

1. **题：委派 20 个任务，18 个验收通过、2 个远端回复成功但缺 Artifact，真实验收完成率？** 解：18/20=90%，不能把缺产物的两项算入。
2. **题：同一付费子任务因超时重复派发，最关键保护是什么？** 解：稳定任务 ID、业务幂等键和权威外部状态核对。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：绑定、能力声明与任务接口。
- [A2A · Core Concepts](https://a2a-protocol.org/latest/topics/key-concepts/)：Agent Card、Task/Message/Artifact。
