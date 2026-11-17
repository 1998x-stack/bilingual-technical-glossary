# Alerting（告警）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 具体告警、性能或会计口径需按环境与约定核对

## 1. 核心定义

告警（Alerting）是在可验证监测条件达到阈值并持续一定时长后，对需要行动的人或自动化系统发出通知、升级或触发响应流程的机制。一个高质量告警应对应明确的用户影响或可行动风险，并附负责人、优先级、证据和处置路径；不是任何指标超阈值都应叫醒值班工程师。

## 2. 形象理解

像消防报警系统：适当联用烟感、温度和持续时长减少误报；有人收到报警后还需要知道楼层、疏散通道和操作手册。把全部日常温度波动都推送成警报会形成疲劳。

## 3. 技术原理与核心内容

Prometheus alerting rule 用 PromQL expr、`for` 与可选 `keep_firing_for` 控制 pending/firing/recovery；Alertmanager 负责 grouping、deduplication、routing、inhibition、silences 和 notification repeat intervals。Grafana Alerting 有独立的 rule/contact point/policy 体系。SLO burn-rate 告警用短窗与长窗关联检测大规模错误预算消耗，避免单纯 CPU=90% 阈值无法反映用户体验。通知通道和告警平台自身也要容灾：监控失联/缺失数据是一类特殊失败，不等同正常零错误。

## 4. 工程实践与设计权衡

对在线 LLM API 建立用户级成功率、TTFT P99/阈值 good events、错误预算消耗与 GPU 故障的不同优先级；测试报警的时间窗、`for` 长度、路由接收者、on-call 接力和静默窗口。关联 Runbook、trace 链接、最近发布变更与指标范围；抑制集群失联时大量节点级次生告警，但要保留根因和业务影响告警。每季度统计真正可行动告警率、误报率与平均响应时间，逐步削减噪声。

## 5. 易混概念与边界

告警触发与通知发送不同：rule firing 不保证消息已经送达。告警噪声降低不等于关闭安全/重大 SLO 问题；Silence 抑制通知，Inhibition 根据依赖关系抑制次生告警。Monitoring 是观测，Alerting 是行动入口。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么选择多窗口 SLO burn-rate 而不是只用高 CPU 阈值？** 答：burn-rate 对用户侧错误预算消耗有直接解释，长短窗口组合可兼顾突发重大故障与持续劣化；CPU 过高未必有用户影响。

2. **问：Alertmanager silence 与 inhibition 分别在何时适用？** 答：Silence 按匹配规则在维护期等明确场景主动静默；Inhibition 用已触发的高层告警抑制依赖告警，例如机房网络故障导致成百节点级失败。

## 7. 中等难度考试题（含解析）

1. **题：每分钟收到 600 个等价的实例级错误告警，按 cluster 分组为 6 个通知，通知数下降比例？** 解：`(600−6)/600=**99%**`；分组只减少通知数量，事件并未消失。

2. **题：告警规则 `for: 5m`，条件从 10:00 连续成立到 10:08，假设评估准确每分钟一次，最早约在几点进入 firing？** 解：约 **10:05**。实际受 evaluation interval、时间戳、规则重启和缺失数据影响。

## 8. 权威来源与延伸阅读

- [Prometheus Alerting Rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)：供独立核对上述机制、公式与实施前提的一手资料。
- [Prometheus Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/)：供独立核对上述机制、公式与实施前提的一手资料。
- [Google SRE Workbook Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)：供独立核对上述机制、公式与实施前提的一手资料。

> 数值题仅为学习示例，不是生产硬件压测或会计处理意见。
