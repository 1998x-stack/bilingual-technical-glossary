# Energy per Token（每词元能耗）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 成本、能效与遥测的边界需按产品版本声明

## 1. 核心定义

每词元能耗（Energy per Token）是在定义边界内消耗的电能除以相同边界内生成或处理的 token 数，常用 J/token 或 Wh/千 token。它必须说明输入/输出 token 的分母、是否包含空闲/CPU/网络/存储/制冷及 PUE、测量时间窗与模型质量/SLO，否则不同报告不可比。

## 2. 形象理解

像配送服务每送达一个合格包裹的平均耗油量：高速运送更多包裹可以摊薄固定开销，但如果漏送、退件或频繁返工，就应以实际成功交付的包裹为分母。

## 3. 技术原理与核心内容

能量 `E=∫P(t)dt`，离散采样可近似 `E≈Σ P_i×Δt_i`，其中 1W·s=1J。按 GPU telemetry 可读取功率与 DCGM 累计能源 counter；需要考虑设备支持、counter reset、采样精度和能量边界。若窗口 GPU 用电 E_gpu、产出 N_out，则 `J/output_token=E_gpu/N_out`；若要机房全量估算，可以引入 CPU/网络/存储等电能以及 PUE，但 PUE 不能直接用来替代真实全平台测量。大 batch 可能降低 J/token 而增加用户尾部时延，比较时必须加 SLO 约束。

## 4. 工程实践与设计权衡

给推理压测保留相同 workload、输入/输出长度、模型版本、量化、并发、硬件温度和测量窗口；报告 GPU-only J/token 与 estimated facility J/token 分开。对 Prefix cache 命中率、speculative decode、动态批处理做敏感性分析，防止只测短输出/不计 prefill 而虚报节能。使用可用的 DCGM energy counter 或外部 PDU 能耗计并核对时序，结合电价与 carbon intensity 才能进一步估算费用和碳排。

## 5. 易混概念与边界

Energy per Token 测能耗，Cost per Million Tokens 测财务成本，Energy Efficiency 可写 tokens/J；功率 W 是瞬时速率，不等于能量 J。要明确设备级、节点级和机房级边界，不能把瞬时 GPU TDP 当作实际功率。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么只用 GPU 标称 TDP×运行秒数估能耗可能不准确？** 答：TDP 是设计热/功率预算而非持续实测功率；实际 load、DVFS、温度和 idle 变化，需积分测量功率或用能源计数器。

2. **问：为何 J/token 降低但生产节能不一定成立？** 答：可能通过加大批量增加排队、失败重试、额外 CPU/网络开销，或分母混入无效 tokens；需比较相同 SLO 与整个系统能耗边界。

## 7. 中等难度考试题（含解析）

1. **题：平均 GPU 实测功率 400W，运行 100s，输出 20,000 tokens，GPU-only J/token？** 解：`400×100/20000=**2 J/token**`，不含其它系统。

2. **题：GPU-only 总能耗 5kWh，估算 facility PUE=1.2 且假设所有 IT 能耗均来自此 GPU，估 facility 能耗？** 解：`5×1.2=**6kWh**`；现实还要计 CPU/网络/存储与设备功耗，题设为简化边界。

## 8. 权威来源与延伸阅读

- [NVIDIA DCGM Exporter Metrics](https://docs.nvidia.com/datacenter/dcgm/latest/reference/dcgm-exporter-metrics.html)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。
- [NVIDIA DCGM Fields](https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。
- [FinOps Sustainability Capability](https://www.finops.org/framework/capabilities/sustainability/)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。

> 数值题仅为题设假设下的教学计算，不替代硬件实测或实际会计核算。
