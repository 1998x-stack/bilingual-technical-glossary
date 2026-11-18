# AI Agents · Batch 16 内部学习路径（301–320）

> 本阶段仅 301–310 已完成候审稿，311–320 仍 planned。批次页面只供编辑，不能出现在公开 Explorer。

## 第一阶段：成本、模型用量与可靠性（301–310）

Token Usage → Cost per Task → Cost Budget → Cost–Quality Trade-off → Caching 是优化成本的核心路径；Lifecycle Hook → Circuit Breaker → SLO → SLA → Alerting 则把系统恢复与业务目标连接。

- [Token Usage（词元用量）](301-token-usage.md)
- [Cost per Task（单任务成本）](302-cost-per-task.md)
- [Cost Budget（成本预算）](303-cost-budget.md)
- [Cost–Quality Trade-off（成本—质量权衡）](304-cost-quality-trade-off.md)
- [Caching（缓存）](305-caching.md)
- [Lifecycle Hook（回调钩子）](306-lifecycle-hook.md)
- [Circuit Breaker（断路器）](307-circuit-breaker.md)
- [Service Level Objective (SLO)（服务级别目标）](308-service-level-objective.md)
- [Service Level Agreement (SLA)（服务级别协议）](309-service-level-agreement.md)
- [Alerting（告警）](310-alerting.md)

## 综合工程案例

搭建一个检索、摘要和写入的三阶段 Agent：设共享 token/cost 预算、缓存隔离、幂等写入、限流/熔断、SLO 与错误预算告警。对故障注入场景分别统计任务真实完成率、P95 以及每次成功任务费用。补齐 311–320 的运行手册、SDK、Skills 与 Schema 后，再检查从开发到生产的完整闭环。
