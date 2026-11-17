# Compute Efficiency（计算效率）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 成本、能效与遥测的边界需按产品版本声明

## 1. 核心定义

计算效率（Compute Efficiency）描述系统将可用计算资源转化为有用工作量的程度，必须明确定义分子和分母。AI 训练常用模型 FLOPs 利用率（Model FLOPs Utilization，MFU）估算有效模型前后向 FLOPs/s 与 GPU 理论峰值 FLOPs/s 的比；在线推理则常结合 SLO goodput、输出 token/GPU-second 和成本/有效 token。不同工作负载不能只凭 GPU busy ratio 比较计算效率。

## 2. 形象理解

流水线 90% 时间都在运行但大量返工，设备并不一定高效；有用产品/小时与可用理论最大产出比，比“是否开机”更接近效率。

## 3. 技术原理与核心内容

对明确精度与硬件峰值的训练负载，可以写 `MFU=model_FLOPs_per_step/(step_time×N_GPU×peak_FLOPs_per_GPU)`；model FLOPs 估算需包括架构、token 数、前后向、attention 长度和稀疏/混合专家路径。MFU 是近似模型计算利用率，不等于硬件 FLOPs utilization（可能包括通信以外的重算）、H100 峰值数字或 GPU busy。Roofline 模型以运算强度 `FLOPs/byte` 与算力/带宽上界解释 memory-bound 与 compute-bound 之间的差异；decode 阶段在低 batch 可能更受权重/KV 读取限制。

## 4. 工程实践与设计权衡

训练优化按 step time 拆 compute、collective communication、input pipeline 和 checkpoint，记录 MFU 与 loss/quality 保持一致；混合精度与 FlashAttention 可能同时改变 kernel 表现和 FLOPs 模型假设。推理侧评估同模型/输入输出分布及 SLO 下的 goodput/GPU-hour、KV preemption、能耗与成本；若高并发把尾延迟推过 SLO，TPS 增长并不等于有效效率提高。

## 5. 易混概念与边界

Compute Efficiency 是总称；MFU 是特定计算模型的比值，HFU 可包含额外实际执行运算，GPU busy ratio 是设备活动采样，Tensor Core utilization 是特定算术单元行为，不能互换。

## 6. 中等难度面试题（含参考答案）

1. **问：MFU 从 40% 提升至 55%，是否一定说明训练加速且模型质量不变？** 答：必须保证相同模型、精度、FLOPs 假设、批量、loss/quality 和 GPU 硬件；改变 FLOPs 估算或隐藏训练无效步骤也会让指标失真。

2. **问：为何 decode 的 GPU busy 100% 仍可能有很低 MFU？** 答：每 token 需要频繁读取权重/KV，而低 batch 运算强度有限，设备有 kernel 但 FLOP/s 远低于理论峰值。

## 7. 中等难度考试题（含解析）

1. **题：模型每 step 的理论有效 FLOPs=800 TFLOPs，8 GPUs 各峰值 100 TFLOPs/s，step time=2s，估 MFU？** 解：`800/(8×100×2)=**50%**`，仅基于题设的 FLOPs 模型。

2. **题：服务在 60s 内完成 120,000 个符合 SLO 的输出 tokens，使用 4 GPUs，good tokens/GPU-second？** 解：`120000/(60×4)=**500 tokens/GPU-s**`，不能直接与不同 tokenizer/模型质量比较。

## 8. 权威来源与延伸阅读

- [PaLM paper MFU discussion](https://arxiv.org/abs/2204.02311)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。
- [NVIDIA CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。
- [vLLM Benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。

> 数值题仅为题设假设下的教学计算，不替代硬件实测或实际会计核算。
