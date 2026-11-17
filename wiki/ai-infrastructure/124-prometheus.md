# Prometheus（Prometheus 监控系统）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 请按实际版本与观测口径核对技术边界

## 1. 核心定义

Prometheus 是以时间序列为核心的开源监控系统和生态，支持通过 HTTP scrape 指标、带标签的数据模型、PromQL 查询、规则求值与告警管理。典型单节点 Prometheus 自带本地 TSDB 与查询 API；长期保留、跨集群查询或高可用需要 remote write 与额外组件，不应假设默认单机即提供无限历史与无损全局一致性。

## 2. 形象理解

像周期性抄读每台机器的仪表读数，按设备/区域归档，然后用查询语言计算速度、错误率和延迟分布；仪表抄表频率太低会错过短尖峰，而给每位顾客都设独立仪表会压垮档案室。

## 3. 技术原理与核心内容

核心是 metric_name+labels → time series，每条样本包含 timestamp/value。Scrape manager 在设定间隔抓取 `/metrics`，服务发现与 relabeling 过滤维度；PromQL 的 `rate()`/`increase()` 处理 Counter 变化，`sum(rate(...))` 在可用维度聚合，Histogram bucket 可由 `histogram_quantile` 估延迟分位。Rule evaluator 产生 recording/alerting rules，Alertmanager 再处理通知分组等。高 cardinality（例如 request_id、原始 prompt）乘以服务实例会使 series 数爆炸。

## 4. 工程实践与设计权衡

Kubernetes GPU 推理栈采集 node exporter、kube-state-metrics、DCGM exporter 与服务 TTFT/TPOT histograms；明确单位 seconds、bucket 上界、job/instance、model/version 和必要标签。为关键 SLI 设计聚合 recording rules 与多窗口错误预算告警，监测 scrape failures、target down、remote_write queue 和磁盘 retention。将长日志和 trace IDs 放其他后端，用 exemplars 关联，而不是把每次请求变成 Prometheus label。

## 5. 易混概念与边界

Prometheus 与 Grafana 不同：前者负责 scrape/TSDB/PromQL/规则，后者主要提供可视化和跨源查询；Alertmanager 负责通知路由去重/抑制，Prometheus 规则负责触发条件。Summary client-side quantiles 不应在多个 Pod 间平均。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 `rate(requests_total[5m])` 比直接画 Counter 原值更适合看当前 QPS？** 答：Counter 自服务启动累计并可能重置，原值反映历史总量，rate 按窗口估算变化速率并处理常见重置。

2. **问：为何给 latency Histogram 每个请求加 request_id label 会造成问题？** 答：每个新请求可制造独立 series，乘以 bucket 数和实例数造成巨量存储与计算成本。应只保留必要低基数维度，把 ID 放入 traces/logs。

## 7. 中等难度考试题（含解析）

1. **题：Counter 5 分钟内从 10,000 增到 16,000 且无 reset，平均 req/s？** 解：`6000/300=**20 RPS**`。

2. **题：某 histogram 有 20 个桶、100 台实例，每台生成 5 组 label组合，忽略 sum/count，理论 bucket series 数？** 解：`20×100×5=**10,000 series**`，说明 bucket 和标签基数可相乘。

## 8. 权威来源与延伸阅读

- [Prometheus Overview](https://prometheus.io/docs/introduction/overview/)：可核查对应的原始规范、维护者文档及其版本。
- [Prometheus Data Model](https://prometheus.io/docs/concepts/data_model/)：可核查对应的原始规范、维护者文档及其版本。
- [Prometheus Histograms](https://prometheus.io/docs/practices/histograms/)：可核查对应的原始规范、维护者文档及其版本。

> 例题计算使用明确假设，不是实际集群的压测或财务成本报告。
