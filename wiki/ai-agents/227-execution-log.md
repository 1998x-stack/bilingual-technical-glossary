# Execution Log（执行日志）

> AI Agents · 专题：执行状态、持久化与恢复 · 定义、工程边界、可复算题目与独立事实核验

## 1. 核心定义

**Execution Log（执行日志）**：Execution Log（执行日志）是以结构化事件记录 Agent 决策、工具调用、状态迁移、外部资源变更和错误的时间线，用于审计、事故排查、恢复与性能评测。日志必须区分‘模型提议’‘工具请求已发送’与‘实际业务后置条件已验证’。

**适用边界：**日志不自动构成外部付款或部署的权威凭证；分布式异步采集可能丢记录或乱序，trace ID 也不能替代租户访问控制。输入/输出中可能包含敏感数据，不得为了可观测性任意上传完整提示词和账户资料。

## 2. 形象理解

如飞机黑匣子记录操纵指令、仪表状态和异常告警，事故后还需结合地面雷达与维修记录核实事件。

**类比的局限：**黑匣子可能遗漏其他系统的独立动作；一次记录‘命令已发出’与命令被执行是不同事件。

## 3. 技术原理与核心内容

建议 Event={timestamp,observed_timestamp,trace_id,span_id,run_id,step_id,tool_call_id,operation_id,event_type,status,resource_version}。OpenTelemetry Logs 数据模型标准化 Timestamp、ObservedTimestamp、TraceId、SpanId；OpenAI Agents SDK tracing 可包含 generation、tool、handoff、guardrail spans。按 task/operation 关联，使用不可随意修改的审计后端并限制保留期。敏感字段在同一个自有 exporter 内完成脱敏再发送，而非先泄漏再补救。

## 4. 工程实践与设计权衡

**工程案例：**部署 Agent 日志记录 CI run、待审批 SHA、调用部署工具的请求以及部署平台实际 digest。超时后根据 operation_id 重新查真实版本，补写权威后置状态；不能用 Agent 先前说‘部署成功’的文本覆盖事实。

**失败模式与验证：**日志泄漏 Bearer Token、两个 Worker 的事件错配、异步导出过程中丢失、仅凭 span success 就判定银行到账。测试脱敏、追踪相关 ID、断线、过期数据和跨租户访问。

## 5. 关联知识与易混辨析

Execution Log 是事件序列；Trace 通过 span 树描述端到端路径；Checkpoint 保存可恢复状态；Outcome Evaluation 检查最终交付。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 trace 中 tool-call span success 不必然说明最终业务成功？** 答：span 可能仅表示客户端调用返回，业务事务仍 pending；需读取权威后置条件。
2. **问：如何避免日志中意外出现隐私数据？** 答：选择 allowlist 字段、敏感参数遮蔽、专用 exporter 内 fail-closed 脱敏、合理 TTL 和访问控制。

## 7. 中等难度考试题（含解析）

1. **题：模型 span 2 个、工具 span 3 个、数据库 span 2 个，合计？** 解：2+3+2=7 个 span。
2. **题：时间戳相差 5 秒，可以单独用它推断 RPC 耗时 5 秒吗？** 解：不能，网络延迟、队列与时钟偏差可能存在，应以同一时钟域的运行时度量核实。

## 8. 权威来源与延伸阅读

- [OpenTelemetry · Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)：Timestamp、TraceId、SpanId 与结构化日志。
- [OpenAI Agents SDK · Tracing](https://openai.github.io/openai-agents-python/tracing/)：generation、tool、handoff 和 guardrail span。
