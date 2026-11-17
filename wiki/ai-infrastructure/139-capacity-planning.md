# Capacity Planning（容量规划）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 按 SLO、租户、资源约束与版本说明结论边界

## 1. 核心定义

容量规划（Capacity Planning）是结合历史与预测需求、服务 SLO、资源形状、增长趋势和风险缓冲，决定未来所需计算/存储/网络容量、硬件类型与部署时点的过程。对于 AI Infrastructure，不能仅用平均 GPU 利用率外推，需要按 prompt/output token 分布、并发、模型显存、KV cache、网络拓扑和故障恢复容量分别建模。

## 2. 形象理解

像城市规划机场容量：依据每天平均乘客数建设登机口会在节假日高峰失效，还必须考虑天气停飞、备用跑道、机型差异和航班到达的突发。

## 3. 技术原理与核心内容

服务容量可以先在同硬件与 SLO 下测单副本 goodput `g`（合格请求/s），以峰值目标到达率 λ 和计划余量 h 估 `N≥ceil(λ/(g×(1−h)))`，但仅在相同请求长度分布、工作负载与近似线性扩展时有效。进一步考虑 N+1 故障保留、AZ loss、模型启动时间、GPU 内存形状、内外网带宽和存储容量水位。训练任务按 step time、GPU-hours、checkpoint 间隔、节点故障和队列等待构建不同容量模型。统计分位、增长情景与 GPU 库存/交付提前期要纳入计划。

## 4. 工程实践与设计权衡

以线上 7/28/90 天按模型/区域/租户聚合的 arrival RPS、input/output token 长度、TTFT/ITL、goodput 和失败率构建基线，做峰值场景、长 prompt 阶段、Spot 中断场景和两区域容灾压力测试。用 Load Testing 得到 SLO 约束下的每节点有效容量，而不是厂家峰值 TFLOPs。结合供应商配额、GPU Operator 驱动预热、模型下载时间、扩容冷启动和预算，设明确采购/预留触发条件。

## 5. 易混概念与边界

容量规划决定长期“需要多少/何种资源”；Autoscaling 决定短期“何时增减”。Average utilization 不是容量界限，GPU busy 也不能直接换算请求吞吐。容量计划必须与可用性 SLO 和故障域假设配套。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么用总 tokens/s 容量规划 LLM API 可能失败？** 答：不同请求有不同输入/输出长度、KV 压力和生成间隔；高输出 TPS 不保证短请求 TTFT 或长请求 ITL SLO，需实测 workload 分布下 goodput。

2. **问：新节点启动需要 8 分钟，如何避免突发流量提前击穿容量？** 答：保留 warm capacity、预测性扩容或队列/限流，设置足够提前的告警阈值，并与节点获取/驱动加载/模型预热时间联动。

## 7. 中等难度考试题（含解析）

1. **题：峰值目标 450 good req/s，每节点在 SLO 下 goodput=75 req/s，规划 20% 容量余量，估最少节点数？** 解：`ceil(450/(75×0.8))=ceil(7.5)=**8 台**`，忽略冗余故障场景。

2. **题：已有 10 台同型节点，每台可提供 60 good req/s，假设 1 台故障且不允许超载，剩余稳态 goodput？** 解：`(10−1)×60=**540 good req/s**`。

## 8. 权威来源与延伸阅读

- [Google SRE Capacity Planning](https://sre.google/sre-book/software-engineering-in-sre/)：用于核对管理机制与性能边界的原始资料。
- [Google SRE Handling Overload](https://sre.google/sre-book/handling-overload/)：用于核对管理机制与性能边界的原始资料。
- [Kubernetes Cluster Autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)：用于核对管理机制与性能边界的原始资料。

> 例题是假设条件下的算术演示，不是对生产多租户安全性或容量的认证。
