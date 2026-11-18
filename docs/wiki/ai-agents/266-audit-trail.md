# Audit Trail（审计跟踪）

> AI Agents · 专题：安全防护与治理 · 防止不可信内容跨越执行授权与信任边界

## 1. 核心定义

**Audit Trail（审计跟踪）**：Audit Trail（审计跟踪）是一组能按主体、时间、资源、动作和真实结果追溯 Agent 关键决策及业务操作的记录链。它需特别记录认证、授权、人工批准、工具参数、执行状态和外部事务 ID，以便安全审查与事故复盘。

**适用边界：**审计日志不等于模型生成的步骤总结。系统可能存在异步日志丢失或滞后；即使 trace 记录了 tool_call=success，也须与外部业务账本/仓库状态核对。审计还要遵守隐私保留规则，不能无限制收集完整 prompt 和 secret。

## 2. 形象理解

像工厂在每个关键环节保留可核验的签章、批次号和验收记录，事后可以重建责任链，而非依赖当事人记忆。

**类比的局限：**记录本身仍可能被篡改或漏记，需要访问限制、完整性机制和外部事实交叉验证。

## 3. 技术原理与核心内容

AuditEvent={event_id,actor_id,tenant_id,task_id,trace_id,operation_id,resource_id,resource_revision,action,decision,policy_version,approver_id,timestamp,outcome}。将用户授权/业务批准与工具执行分为独立事件，使用 append-only/WORM 存储、链式哈希或受控签名及访问审计提高完整性。采用 NIST AU 审计控制思路，校准时间、监控事件缺口，并定期将外部 payment_id/commit SHA 与记录对账；对敏感字段做脱敏和最短必要保留。

## 4. 工程实践与设计权衡

**工程案例：**生产删除 Agent 必须在审计记录中关联‘谁批准删除何资源’‘模型选择什么工具’‘服务端执行返回什么’及‘资源是否真实消失’。若审核通过但执行失败，要保留两种不同状态，不能写成删除成功。

**失败模式与验证：**由模型写不可校验的日志、跨租户可查看审计内容、将密钥写入日志、日志可以随业务用户任意修改、时间戳不足以追踪。用篡改检测、缺日志、权限撤销和真实业务对账验证。

## 5. 关联知识与易混辨析

Audit Trail 强调责任和可追溯的记录链；Execution Log 强调运行事件；Trace 强调跨服务相关性；Human Review 是对内容作判断而非日志本身。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么审计记录应同时包含 approval_id 和 operation_id？** 答：批准与真实执行是两件事，关联两者才能判断是否使用了有效批准和是否真的产生副作用。
2. **问：为什么模型说‘我已写入审计日志’不能作唯一证据？** 答：模型文本并不证明受控存储发生 append，应以审计后端的真实记录和完整性机制核查。

## 7. 中等难度考试题（含解析）

1. **题：100 个敏感工具调用中 96 个有完整 actor/resource/outcome 记录，完整审计覆盖率？** 解：96/100=96%，需进一步排查缺失 4 个的风险。
2. **题：某审核 ID 关联操作 A，却实际执行操作 B，能认定审计授权正确吗？** 解：不能，必须核对 action、resource 和参数哈希是否一致。

## 8. 权威来源与延伸阅读

- [NIST SP 800-53 · Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)：审计记录、访问控制和系统安全。
- [OpenTelemetry · Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)：trace/span、事件时间和可追溯性。
