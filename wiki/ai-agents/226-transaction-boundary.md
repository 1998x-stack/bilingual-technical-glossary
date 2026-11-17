# Transaction Boundary（事务边界）

> AI Agents · 专题：执行状态、持久化与恢复 · 定义、工程边界、可复算题目与独立事实核验

## 1. 核心定义

**Transaction Boundary（事务边界）**：Transaction Boundary（事务边界）界定一组更新何时开始以及在哪个范围内可以原子提交或回滚。Agent 往往横跨数据库、支付网关、MCP 工具和远程智能体；不同系统的操作通常不在同一个 ACID 事务里，因此需明确各自的提交点。

**适用边界：**跨服务事务的任何写入仍须在实际执行器检查当前身份、资源级权限、用户授权与审批参数版本；本地事务原子性不能替代外部支付或退款授权。PostgreSQL 的 BEGIN/COMMIT 可以原子保护同一数据库内的相关写入，但不会自动撤销第三方付款、邮件发送或外部 API；跨服务失败通常采用 Saga/Compensating Action，而非宣称一次 ROLLBACK 可恢复一切。

## 2. 形象理解

银行内部一本账可将借贷分录一起提交，但已经交给物流公司寄出的合同无法通过数据库回滚直接取回。

**类比的局限：**即使事务成功提交，外部服务可能滞后；系统需要独立对账与恢复机制。

## 3. 技术原理与核心内容

事务内部遵守 `BEGIN → validate → UPDATE → COMMIT/ROLLBACK`。跨服务场景把 T1、T2、T3 分别视为独立提交边界，持久记录 operation_id、业务状态和可选补偿 C_i。为减少数据库写入与发消息的双写不一致，可在同一数据库事务中保存 outbox event，再异步发布；消费者仍按 event_id 去重。对于不可补偿的敏感动作应增加 approval gate 和 postcondition query。

## 4. 工程实践与设计权衡

**工程案例：**订单 Agent 在本地数据库创建订单、用外部支付 API 收款、再通知财务 Agent。第一次事务成功但支付返回 UNKNOWN 时，不应回滚订单后重复收款；应以原 payment_id 查询并更新 pending/paid 状态。

**失败模式与验证：**将第三方 HTTP 200 当成数据库 COMMIT、外发消息重复导致双写、事务锁持续过久、补偿超时被伪装成已回滚。测试在提交前、提交后、消息发出前及后注入崩溃。

## 5. 关联知识与易混辨析

Transaction Boundary 描述局部原子性；Compensating Action 处理跨边界副作用；Execution Log 只是证据记录；Checkpoint 是工作流状态保存，不自动具备数据库 ACID。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么不能依靠本地数据库 ROLLBACK 撤销外部 MCP Tool 触发的转账？** 答：外部系统不参与该本地事务，必须查询真实支付状态并按规则发起冲销或退款。
2. **问：transactional outbox 主要解决什么？** 答：在本地事务里把业务状态与待发事件一起持久提交，降低写库成功但消息未发的双写窗口。

## 7. 中等难度考试题（含解析）

1. **题：同一未提交事务 3 条 SQL 中第 2 条失败，执行 ROLLBACK 后生效条数是多少？** 解：0 条，前提数据库全部操作属于同一事务。
2. **题：外部退款 500 元但手续费 10 元不可退，用户实际净收回多少？** 解：490 元，假设手续费由该用户承担。

## 8. 权威来源与延伸阅读

- [PostgreSQL · Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)：BEGIN、COMMIT、ROLLBACK 与单库原子性。
- [Azure · Compensating Transaction](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction)：多资源工作流的业务补偿。
