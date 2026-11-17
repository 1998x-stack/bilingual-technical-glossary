# Metrics（指标数据）

> 学科：AI Infrastructure · 专题：可靠性与可观测性 · 时间窗口、请求单位及故障定义须注明

## 1. 核心定义

指标数据（Metrics）是系统运行中的结构化数值观测，通常表示为指标名称、类型、标签、数值和时间戳，并被采集为可查询的时间序列。Prometheus 常见核心类型是 Counter、Gauge、Histogram 和 Summary；选择合适的数据模型、单位、低基数标签和聚合口径比大量堆砌仪表板更重要。

## 2. 形象理解

汽车仪表板里当前速度是 Gauge，累计里程是 Counter，历次刹车耗时的分布可用 Histogram；单次行程录像则更像 Trace，不能当成可直接聚合的时速数字。

## 3. 技术原理与核心内容

Counter 累计只增但进程重启可清零，使用 `rate(counter[5m])` 估每秒增速；Gauge 能升能降。Classic Histogram 产生累计 `_bucket{le}`、`_sum`、`_count`，Native Histogram 在 Prometheus 中有专门的结构与合并语义；Summary 的 client-side quantiles 不应跨实例直接平均求全局 P99。Histogram quantile 使用桶近似/插值，桶边界决定精度；阈值型请求 SLI 可以直接使用合适桶计数算 good/total。高基数用户 ID 或随机请求 ID 将显著放大时间序列数。

## 4. 工程实践与设计权衡

推理服务可分别暴露 `requests_total` counter、`time_to_first_token_seconds` histogram、`waiting_requests` gauge、`kv_cache_usage_ratio` gauge，并为所有时延统一 seconds 单位。按 model/region/status 等低基数标签划分，避免把 prompt 内容和敏感用户信息送进指标；跨实例计算请求 P99 时要先汇聚 histogram buckets，再用统一分布估计，不能平均各 Pod 的 P99。

## 5. 易混概念与边界

Metrics 是遥测形式，SLI 是业务测量定义，SLO 是目标。Counter 原值不是每秒 RPS；Gauge 可下降，所以不应机械 `rate()`；Summary quantiles 不适合不同进程全局汇总。

## 6. 中等难度面试题（含参考答案）

1. **问：为何不能平均10个Pod的P99延迟来表示集群P99？** 答：分位数不具线性可加性，各 Pod 的流量和尾部分布不一样。需合并原始观测或 histogram 桶后再计算。

2. **问：为什么 Counter 指标通常先用 rate() 再告警？** 答：Counter 记录自启动累计事件并可能重启清零，原值不代表当前压力；用时间窗差分速率描述短期负载和错误比率。

## 7. 中等难度考试题（含解析）

1. **题：某 Counter 在60秒从50,000增至53,000，且没有重置，平均RPS？** 解：`(53000−50000)/60=**50req/s**`。

2. **题：Histogram 记录10,000次请求，其中 le=0.5s累计桶有9,400次，0.5s阈值达标率？** 解：`9400/10000=**94%**`；前提是桶计数与总请求计数口径相同。

## 8. 权威来源与延伸阅读

- [Prometheus Metric Types](https://prometheus.io/docs/concepts/metric_types/)：原始资料用于核对相关定义、假设与系统实践。
- [Prometheus Histograms and Summaries](https://prometheus.io/docs/practices/histograms/)：原始资料用于核对相关定义、假设与系统实践。
- [OpenTelemetry Metrics](https://opentelemetry.io/docs/concepts/signals/metrics/)：原始资料用于核对相关定义、假设与系统实践。

> 例题仅用于理解公式，不是对任何线上系统可靠性的审定。
