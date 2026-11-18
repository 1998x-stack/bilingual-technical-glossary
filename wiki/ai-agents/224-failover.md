# Failover（故障转移）

> AI Agents · 专题：执行状态、持久化与恢复 · 时延、恢复和外部事务的真实边界

## 1. 核心定义

**Failover（故障转移）**：Failover（故障转移）是当 Agent、工具服务或依赖实例不可用时，依据健康检查与恢复策略把新的工作负载转给备用节点、区域或降级处理路径。目的是维持可用性，不能把备用系统视为自动拥有相同的权限、版本和真实事务状态。

**适用边界：**主节点无法回应不意味着它已停止写入。活动-备份切换可能造成 split-brain、重复请求和旧数据读取；对于支付或库存等高后果操作，必须使用一致性的操作 ID、资源所有权和 fencing token。

## 2. 形象理解

像列车因线路中断被转至备用轨道，但调度中心必须先确认主轨道是否仍有列车，以免两列车争用同一区段。

**类比的局限：**备用轨道不同可能限速或不支持相同载重，切换并不是零成本或零风险。

## 3. 技术原理与核心内容

探针 health_readiness 与 liveness 区分：readiness 表示是否可以接受新任务，liveness 判断是否需要重启。调度器检测连续失效后按 failover policy 转移 owner lease、检查 checkpoint revision、未决 operation_id 与备用部署版本；只在 fencing 生效后允许新 owner 写同一资源。进行限流和重试隔离，防止故障传播。

## 4. 工程实践与设计权衡

**工程案例：**合同分析 Agent 所在节点宕机，新节点从 Postgres checkpoint 恢复任务，继续处理尚未提交的 PDF 章节；对于原节点可能已发出的邮件，先查通知业务日志，不能重发。若备用区域数据同步延迟，需要告知用户结果尚未确认。

**失败模式与验证：**双主提交、备机代码/工具版本不兼容、心跳抖动引发反复迁移、把健康探针误作业务正确性证明。演练区域不可用、网络分区、状态滞后和争用锁。

## 5. 关联知识与易混辨析

Failover 是执行者/资源切换；Retry 是同类调用再试；Load Balancing 是正常负载分配；Disaster Recovery 是更广的灾难恢复计划。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么故障转移前需要 fencing/lease？** 答：避免旧主节点恢复后与新主节点同时操作同一资源，造成 split-brain 和重复写入。
2. **问：备用服务返回成功但数据版本旧一周，还能宣称恢复完成吗？** 答：不能，必须检查复制滞后、资源版本和业务成功谓词。

## 7. 中等难度考试题（含解析）

1. **题：主节点失效检测 5 秒，切换 3 秒，备用恢复 4 秒，理论恢复时间？** 解：5+3+4=12 秒，忽略检查与网络延迟。
2. **题：两个节点同时自称 primary，正确的处理原则？** 解：用一致性租约/任期与 fencing，只有持有效写权的节点可以提交。

## 8. 权威来源与延伸阅读

- [Azure · Health Endpoint Monitoring](https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring)：主备节点健康检测与切换依据。
- [Azure · Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)：持续故障隔离与快速失败。
