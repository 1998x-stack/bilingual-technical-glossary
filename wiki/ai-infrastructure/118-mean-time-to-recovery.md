# Mean Time to Recovery（平均恢复时间 · MTTR）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 时间窗口、请求单位及故障定义须注明

## 1. 核心定义

平均恢复时间（Mean Time to Recovery，MTTR）指故障发生或用户受影响开始，到服务重新满足既定功能与健康条件为止，历次事件持续时间的算术平均。Mean Time To Repair 有时也缩写 MTTR，但后者可能只统计维修动作而非故障检测/恢复验证；生产事故制度必须明确展开、起止与严重度。

## 2. 形象理解

店铺停电后先发现断电，接着呼叫维修、恢复供电、验证支付功能，最后开门营业。只数工程师实际修电的时间并不能表示用户经历的停机。

## 3. 技术原理与核心内容

给每次事故 t_start 与 t_recovered，`MTTR=Σ(t_recovered−t_start)/N`。若逐项阶段严格串行，可分为检测（MTTD）、响应、诊断、缓解、验证/流量恢复；若阶段重叠就不能直接加各阶段的平均值。MTTR 是平均值，容易被大量短故障稀释，故还应报告长尾、P95/P99、重大事件、受影响请求和按严重度分桶的恢复时间。恢复服务不代表所有数据都恢复，RPO 是不同概念。

## 4. 工程实践与设计权衡

在线 LLM incident trace 应记录第一个错误请求、告警时间、on-call 承接、版本回滚、权重重新加载、GPU 预热、readiness 成功和流量恢复；记录 RTO 达标情况。训练系统则测 checkpoint 重放、worker 重建、NCCL 组网与任务重新推进的耗时。做故障注入以验证恢复，而不是为了低 MTTR 提前结束事故状态。

## 5. 易混概念与边界

MTTR 不是 MTBF 或 MTTD，也不是业务目标 RTO。RTO 约束允许的恢复时间，RPO 约束数据可能丢失的恢复点；即使应用可访问，checkpoint 不完整仍可能违反数据恢复目标。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么改进检测可以改善 MTTR 而不一定改善 MTBF？** 答：更快发现与处理可缩短用户受影响时段，但并不改变故障产生频率。要提高 MTBF 通常还需处理根因。

2. **问：为什么报告 MTTR=5min 仍必须展示长尾？** 答：可能是许多 1min 事件与一次 5h 事故的均值，重度事故对用户和错误预算影响不可忽略。

## 7. 中等难度考试题（含解析）

1. **题：故障恢复用时 5、12、8、15min，MTTR？** 解：`(5+12+8+15)/4=**10min**`。

2. **题：检测3min、响应2min、修复7min、验证3min，阶段串行的恢复时长？** 解：`3+2+7+3=**15min**`，若有重叠需用实际事故起止时间。

## 8. 权威来源与延伸阅读

- [Google SRE Managing Incidents](https://sre.google/sre-book/managing-incidents/)：原始资料用于核对相关定义、假设与系统实践。
- [Google SRE Incident Response](https://sre.google/workbook/incident-response/)：原始资料用于核对相关定义、假设与系统实践。
- [Google SRE Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/)：原始资料用于核对相关定义、假设与系统实践。

> 例题仅用于理解公式，不是对任何线上系统可靠性的审定。
