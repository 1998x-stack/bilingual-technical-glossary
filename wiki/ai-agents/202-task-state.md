# Task State（任务状态）

> AI Agents · 专题：A2A：智能体间协议 · A2A Task、Message 和 Artifact 的版本化语义

## 1. 核心定义

**Task State（任务状态）**：Task State（任务状态）是 A2A Task 当前生命周期阶段的枚举，客户端根据它决定继续等待、补充信息、获取产物或终止处理。规范区分已提交、执行中、中断等待、完成、失败、取消和拒绝等状态。

**适用边界：**必须使用对应协议版本的枚举值而不是随意写 `running/done`：当前 A2A 包括 `TASK_STATE_SUBMITTED`、`TASK_STATE_WORKING`、`TASK_STATE_COMPLETED`、`TASK_STATE_FAILED`、`TASK_STATE_CANCELED`、`TASK_STATE_INPUT_REQUIRED`、`TASK_STATE_AUTH_REQUIRED`、`TASK_STATE_REJECTED` 等。中断状态不是终态。

## 2. 形象理解

像邮政件有已揽收、运输中、需补地址、已签收、退回等状态，各自对应不同处理规则。

**类比的局限：**状态显示‘已签收’可能只是远端确认，仍需核实签收人和交付对象。

## 3. 技术原理与核心内容

Task.status 包含 `state`、可选 message 与 timestamp；Client 使用 GetTask 获取权威当前状态，订阅事件作为实时辅助。终态（COMPLETED/FAILED/CANCELED/REJECTED）通常不再接受面向原 Task 的新工作消息；INPUT_REQUIRED/AUTH_REQUIRED 可由用户动作继续。对于未指定和响应过期应保守处理，严禁把状态从 FAILED 无凭据回退为 WORKING。

## 4. 工程实践与设计权衡

**工程案例：**客户 Agent 查询远端数据治理任务，最初 SUBMITTED，处理时 WORKING，缺少访问授权时 AUTH_REQUIRED；用户完成授权后继续到 COMPLETED。汇总器必须查最终 Artifact，并且核对该用户确实有权读取。

**失败模式与验证：**把 AUTH_REQUIRED 当已授权、把状态文字当真实付款、旧事件覆盖新终态、恶意跨任务状态泄漏。通过枚举表、无效转移、消息乱序和任务访问控制测试。

## 5. 关联知识与易混辨析

Task State 是当前枚举值；Task Lifecycle 是一系列合法状态变迁；Streaming Update 是事件传递方式；Artifact 是结果内容，可能在任务工作中就部分出现。

## 6. 中等难度面试题（含参考答案）

1. **问：INPUT_REQUIRED 是失败终态吗？** 答：不是，是中断等待信息，可在新的合法输入到达后继续。
2. **问：AUTH_REQUIRED 是否表示系统已经有执行权限？** 答：相反，是还需要额外授权；不能把进入该状态当作审批通过。

## 7. 中等难度考试题（含解析）

1. **题：10 个 Task 中 6 COMPLETED、2 FAILED、2 INPUT_REQUIRED，成功完成比例？** 解：6/10=60%；等待输入的不算完成。
2. **题：一个任务处于 TASK_STATE_REJECTED，能自动重试原任务当成正常 WORKING 吗？** 解：不能，REJECTED 为终态，应按规范发起新的合法任务或向用户解释。

## 8. 权威来源与延伸阅读

- [A2A · Protocol Specification](https://a2a-protocol.org/latest/specification/)：Artifact、TaskState、事件与通知规则。
- [A2A · Life of a Task](https://a2a-protocol.org/latest/topics/life-of-a-task/)：多轮与终态规则。
