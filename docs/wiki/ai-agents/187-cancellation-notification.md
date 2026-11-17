# Cancellation Notification（取消通知）

> AI Agents · 专题：MCP：模型上下文协议 · MCP 2026-07-28 及兼容边界；示例数字为教学题设

## 1. 核心定义

**Cancellation Notification（取消通知）**：Cancellation Notification（取消通知）表达调用方不再希望某项正在执行的请求继续。它是协作式取消请求，不是一定撤销已经生效的外部副作用。MCP 对取消的承载方式受版本及传输影响。

**适用边界：**在 2026-07-28 版，stdio 通过 `notifications/cancelled` 发信，Streamable HTTP 通过关闭当前请求响应流表示取消；不能沿用旧版 HTTP 发送取消 POST 的通用说法。Tasks 扩展的长任务取消使用 `tasks/cancel`，与普通 request 取消不同。

## 2. 形象理解

像电话中说‘不要继续处理申请’，客服停止下一步，但已发出的快递不能自动追回。

**类比的局限：**信号到达前可能已经付款或提交代码，取消动作和补偿/撤销事务属于不同阶段。

## 3. 技术原理与核心内容

Client 先标记 request cancellation，按当前 transport 发出对应信号；Server 若接收到请求则尽快停止可停止的后续步骤，释放资源并记录 cancellation_reason。请求 ID 与业务 operation_id 需分开：前者识别 RPC，后者识别可能已提交的事务。对后台任务请采用对应 Tasks Extension 的任务状态与 cancel 操作，并查询真实 outcome；取消只能表示 intent，不保证终态一定是 cancelled。

## 4. 工程实践与设计权衡

**工程案例：**自动生成 PR 的 Agent 在上传文件时被取消；如果 PR 已创建，Client 需读取真实 PR ID 而不是报告‘没有创建’，也不能自动删除未经确认的已有 PR。部署管道可暂停下一阶段，但对已发布版本只能另走受控回滚流程。

**失败模式与验证：**把取消当事务回滚、误取消其他任务、旧 HTTP 取消协议用于新版、取消后的异步结果覆盖已确认状态。测试取消竞态、外部写入回执丢失、错 ID 和双重取消。

## 5. 关联知识与易混辨析

Cancellation Notification 取消进行中的请求；Tasks 扩展 `tasks/cancel` 取消任务；Timeout 是触发条件而非业务操作；Compensation 是逆向补救动作，不能混同取消。

## 6. 中等难度面试题（含参考答案）

1. **问：MCP 2026 HTTP 与 stdio 怎样分别取消正在处理的请求？** 答：HTTP 关闭此请求响应流；stdio 使用 notifications/cancelled，均不能保证业务副作用撤销。
2. **问：为什么超时不能证明数据库写入没有发生？** 答：超时可能是响应链路丢失，Server 可能已经提交；必须按 transaction_id 查询后置条件。

## 7. 中等难度考试题（含解析）

1. **题：操作已完成第一阶段写入、尚有两阶段未做，取消后可以说三个阶段都已撤销吗？** 解：不能；第一阶段需要查询与必要补偿，剩余阶段应停止。
2. **题：任务取消信号重复发送 2 次，真实取消操作次数应如何保证？** 解：幂等地处理，同一请求/任务不应产生不必要的重复副作用。

## 8. 权威来源与延伸阅读

- [MCP · Cancellation](https://modelcontextprotocol.io/specification/2026-07-28/basic/utilities/cancellation)：协作式取消和版本传输区别。
- [MCP · Transport bindings](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)：HTTP 中断流与 stdio 通知。
