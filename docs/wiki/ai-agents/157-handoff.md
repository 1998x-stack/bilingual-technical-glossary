# Handoff（控制权交接）

> AI Agents · 专题：多智能体协作 · 多 Agent 协作模式与信任边界；SDK API 以版本文档为准

## 1. 核心定义

**Handoff（控制权交接）**：Handoff（控制权交接）是将正在进行的用户交互或任务控制转移给另一个 Agent，使接收方成为后续步骤的活跃处理者的模式。在 OpenAI Agents SDK 的典型 handoff 中，专员接管当前轮剩余工作，与 manager-as-tools 保留经理控制不同。

**适用边界：**handoff 的具体会话边界、工具结果包装和输入过滤随 SDK 而异；它不自动转交主 Agent 全部权限或所有隐私聊天。控制权迁移不等于业务事务已提交，也不一定是永久转移。

## 2. 形象理解

像客服前台将正在处理的申诉转交给专门的账务人员，让该人员直接继续与客户对话。

**类比的局限：**转接电话不等于转交全部账户密码，历史转述也未必可作为付款授权。

## 3. 技术原理与核心内容

运行器记录 active_agent、handoff_target、handoff_reason、input_context和事件 correlation_id。建立允许目标列表，必要时使用 input_filter 筛除不相关敏感数据，并依据目标权限重建工具目录。交接后接收者的 instructions 与 tools 成为有效执行配置；旧审批不能不加校验重用。对多次转交设置最大跳数，避免 Agent A⇄B 无限路由。

## 4. 工程实践与设计权衡

**工程案例：**差旅助手识别到复杂的发票争议，按已批准政策将对话交给财务专员，传送报销单 ID 和争议条款。接收专员可以要求补证，但不能仅凭对话交接就执行付款；操作仍需业务审批。

**失败模式与验证：**handoff loop、上下文丢关键约束、把用户隐私发给不相关专员、未明确标记谁是当前活跃 Agent、移交失败却报告完成。测多轮路由、上下文最小化和回退。

## 5. 关联知识与易混辨析

Handoff 转移活跃对话控制；Agent as Tool 调用子 Agent 后返回经理继续答复；Task Delegation 是更广的子任务分配；Handoff Record 保存交接证据与版本。

## 6. 中等难度面试题（含参考答案）

1. **问：什么时候 handoff 优于 agent-as-tool？** 答：当领域专员需要直接与用户继续对话或持有当前轮决策控制，而不必每步由经理代理回复时。
2. **问：为什么交接时需要 input_filter？** 答：以最小化无关敏感数据、缓解提示注入和角色边界污染，只传达完成任务必需的上下文。

## 7. 中等难度考试题（含解析）

1. **题：会话最多允许 3 次 handoff，当前已发生 3 次又提出第 4 次，如何处理？** 解：拒绝新的交接并进入回退/人工路径，避免无限循环。
2. **题：handoff 后接收 Agent 只有只读权限，能因委派方拥有写权限而直接创建退款吗？** 解：不能。接收者必须遵守自身有效工具范围与用户授权。

## 8. 权威来源与延伸阅读

- [OpenAI Agents SDK · Handoffs](https://openai.github.io/openai-agents-python/handoffs/)：控制权转移、输入过滤和移交上下文。
- [OpenAI Agents SDK · Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)：Manager 与 Handoff 设计权衡。
