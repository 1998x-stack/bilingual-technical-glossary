# Grafana（Grafana 可视化平台）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 请按实际版本与观测口径核对技术边界

## 1. 核心定义

Grafana 是面向多种数据源的可视化、查询与告警平台，可用 dashboard、panel、变量与 annotations 展示 Prometheus 指标、日志和分布式 trace。Grafana 本身不是 GPU 驱动、Prometheus TSDB 或日志采集协议；数据是否存在、是否实时、能否跨租户读取取决于 data source、权限与实际查询后端。

## 2. 形象理解

像控制室的综合大屏：仪表读数、事故日志和故障路径可以从不同系统汇入同一屏，但大屏不会自动修复机器，且显示的“绿色”取决于查询规则是否正确。

## 3. 技术原理与核心内容

Dashboard 由 panels 与查询、transformations、variables、annotations 组成；Prometheus data source 使用 PromQL，Loki 使用 LogQL，Tempo/Jaeger 可查询 traces。Grafana Alerting 把查询/表达式组成规则，再通过 contact points、notification policies 与 silences 管理通知。Dashboard variables 可以改变查询范围，但高基数、宽时间窗口和过细 step 可能产生昂贵查询。Org、folder、data-source 与 RBAC 的访问控制需结合后端权限，不能认为屏幕不显示某租户就证明数据隔离。

## 4. 工程实践与设计权衡

建设 AI Infra 控制台可分四层：业务 SLO、服务 TTFT/ITL/TPS、GPU 利用率/显存、存储/NIC 以及成本；每个 panel 标注时间窗、单位、模型/地区过滤条件。使用 drilldown 从 SLO error budget 跳到相关 trace 和 incident logs；通过 dashboard-as-code、版本管理、review 与预警测试减少配置漂移。对管理员 API 密钥、数据源凭证与用户访问权限设置最小权限。

## 5. 易混概念与边界

Grafana dashboard 是可视化和查询组合，不等于 SLO 证明；Grafana Alerting 与 Prometheus Alertmanager 可共存但路由体系不同。一个绿色 panel 不能覆盖未采样的租户或错误分母。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么看见“GPU Utilization 90%”不应直接认定服务运行高效？** 答：GPU busy 采样比率不同于 SM/Tensor Core 有效利用、output TPS、SLO goodput；panel 需要同时关联业务量和用户延迟。

2. **问：如何避免 Grafana Dashboard 变量引起越权数据访问？** 答：应在后端/数据源/租户查询权限落实隔离，Dashboard 控件只是 UI，用户可能直接调用查询 API；敏感 label 也需过滤。

## 7. 中等难度考试题（含解析）

1. **题：四个等时长区间的 GPU utilization 为 20%、40%、60%、80%，简单时间平均值？** 解：`(20+40+60+80)/4=**50%**`，若区间长度不同需加权。

2. **题：dashboard 每 15s 查询一次，连续 1h 且查询无失败，总查询次数？** 解：`3600/15=**240 次**`；若多个 panels，各自查询量还要相加。

## 8. 权威来源与延伸阅读

- [Grafana Dashboards](https://grafana.com/docs/grafana/latest/dashboards/)：可核查对应的原始规范、维护者文档及其版本。
- [Grafana Data Sources](https://grafana.com/docs/grafana/latest/datasources/)：可核查对应的原始规范、维护者文档及其版本。
- [Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/)：可核查对应的原始规范、维护者文档及其版本。

> 例题计算使用明确假设，不是实际集群的压测或财务成本报告。
