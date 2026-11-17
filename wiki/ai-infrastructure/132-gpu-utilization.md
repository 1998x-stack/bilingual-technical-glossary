# GPU Utilization（GPU 利用率）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 成本、能效与遥测的边界需按产品版本声明

## 1. 核心定义

GPU 利用率（GPU Utilization）必须先说明观测来源。NVIDIA 常见 GPU busy utilization 是采样窗口内至少有一个 kernel 在 GPU 上执行的时间占比，不等于 SM 发射指令活跃程度、Tensor Core 算术利用率、理论 FLOPs 使用比率或有效模型吞吐。DCGM 的 GPU utilization telemetry 与 SM active/SM occupancy/DRAM active 等 profiling 指标具有不同语义和支持条件。

## 2. 形象理解

工厂机器 90% 时间有工件在运转，并不说明机器 90% 的理论产能被有效使用：设备可能大多在等待内存、加工小工件或者生产返工品。

## 3. 技术原理与核心内容

若统计定义是 busy sampling ratio，可抽象为 `U_gpu=busy_samples/total_samples`；不同型号/驱动/DCGM field 的采样周期与测量方式需按版本核实。GPU 可能在 decode 阶段 memory-bound，此时 busy 接近 100%，但 FLOP/s 远低于峰值；preprocess/CPU DataLoader 等待则形成 GPU idle。针对 NVIDIA DCGM，应分别查看新字段 `DCGM_FI_DEV_GPU_UTIL_RATIO`、`DCGM_FI_PROF_SM_ACTIVE`、`DCGM_FI_PROF_DRAM_ACTIVE` 等是否被实际收集；部分传统 GPU_UTIL 百分数字段已被新 ratio 字段替代或弃用。

## 4. 工程实践与设计权衡

AI 平台诊断同时报告 output TPS、TTFT/ITL SLO、GPU busy、SM active、HBM bandwidth、KV occupancy、功耗和 GPU-hours。区分多实例 MIG、time slicing、独立租户与物理设备采样范围；同一时间窗对齐后才做归因。GPU 80% busy 但 SLO 不达标时重点看队列/KV 分配与 preemption，而非简单增加 batch。度量缺失需显式标成 unavailable，不能默认为 0%。

## 5. 易混概念与边界

GPU Utilization（设备忙碌占比）不是 GPU Memory Utilization（显存数据容量/带宽指标），不是 MFU（模型理论 FLOPs 利用率）或计算效率；高 busy 也可能代表过载、用户体验下降或无效工作。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 GPU busy 95% 不等于模型达到 95% 的理论 TFLOPS？** 答：只要窗口里有 kernel 执行就可能计为 busy，而 kernel 可能等待显存、访存不合并或只做少量算术；应配合 SM/Tensor Core 与模型 FLOPs 数据。

2. **问：GPU utilization 很低但显存几乎占满，可能是什么情况？** 答：加载了模型权重与 KV 缓存却没有足够请求，或 CPU/DataLoader/网络成为瓶颈。显存占用和 GPU 算术活跃度是两套度量。

## 7. 中等难度考试题（含解析）

1. **题：1000 个均匀时间采样点中有 780 个判定 GPU busy，样本 busy utilization？** 解：`780/1000=**78%**`；实际设备字段可能有不同测量实现。

2. **题：GPU 开机运行 24h，busy ratio 的时间平均 60%，抽象为等时采样，busy 等效小时？** 解：`24×0.60=**14.4 小时**`，不能据此推导实际 FLOPs 或有用 token 数。

## 8. 权威来源与延伸阅读

- [NVIDIA DCGM Field Identifiers](https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。
- [NVIDIA DCGM Exporter Metrics](https://docs.nvidia.com/datacenter/dcgm/latest/reference/dcgm-exporter-metrics.html)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。
- [NVIDIA CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。

> 数值题仅为题设假设下的教学计算，不替代硬件实测或实际会计核算。
