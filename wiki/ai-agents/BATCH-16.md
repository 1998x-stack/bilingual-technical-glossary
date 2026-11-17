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

## 第二阶段：工程工具与规范（311–320，候审）

从 Runbook 的可靠运维开始，依次学习 ADK/SDK 的架构边界，接着掌握 Skill Package、Discovery、Invocation，再到 Instruction File、Tool Manifest、Schema Definition 与 JSON Schema。重点是将静态描述、实际工具权限和可验证业务后置状态分离。

- [Runbook（运行手册）](311-runbook.md)
- [Agent Development Kit (ADK)（智能体开发工具包）](312-agent-development-kit.md)
- [Software Development Kit (SDK)（软件开发工具包）](313-software-development-kit.md)
- [Skill Package（技能包）](314-skill-package.md)
- [Skill Discovery（技能发现）](315-skill-discovery.md)
- [Skill Invocation（技能调用）](316-skill-invocation.md)
- [Instruction File（指令文件）](317-instruction-file.md)
- [Tool Manifest（工具清单）](318-tool-manifest.md)
- [Schema Definition（模式定义）](319-schema-definition.md)
- [JSON Schema（JSON 模式）](320-json-schema.md)

## 质量验证建议

利用 Agent Skills 格式校验和 JSON Schema Draft 2020-12 验证字段语义，在受控环境中模拟动态工具注册、恶意描述、跨租户资源 ID 与缺失必填字段；运行真实浏览器术语详情页 E2E、审稿台账与关联索引验证。新增条目尚未完成独立人工专业审核。
