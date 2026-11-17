# GPU Memory Utilization（显存利用率）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 成本、能效与遥测的边界需按产品版本声明

## 1. 核心定义

显存利用率（GPU Memory Utilization）是容易混淆的术语：一类是已分配显存容量占总可用容量的比例 `used_bytes/total_bytes`；另一类如 NVIDIA 的 memory utilization / memory copy utilization 则指采样窗口中显存读写活动的比例，并非已用空间占比。两种数字不能混用，DCGM 的 FB_USED/FB_FREE 与 MEMORY_UTIL_RATIO 更应分开命名。

## 2. 形象理解

像图书馆的座位使用率和图书借阅频率：座位全被占满不代表每分钟都有大量借阅行为；内存容量用得满也不说明 HBM 带宽达到峰值。

## 3. 技术原理与核心内容

容量型利用率可写 `U_capacity=FB_USED/(FB_USED+FB_FREE)`，须明确 reserved/unavailable/driver 分配、MIG partition 与进程粒度。PyTorch `memory_allocated()` 表示张量占用，`memory_reserved()` 表示 allocator 管理/缓存的总量，二者不等于 nvidia-smi 设备级 FB_USED。访存活动/带宽指标需看 `DCGM_FI_DEV_MEMORY_UTIL_RATIO`、`DCGM_FI_PROF_DRAM_ACTIVE` 或 profiling bytes/s；注意最新 DCGM 对部分旧字段有弃用说明。高容量意味着再分配 KV block 可能 OOM，但高容量未必意味着显存带宽饱和。

## 4. 工程实践与设计权衡

LLM 服务调参应同时追踪模型权重、量化元数据、每 rank KV cache、临时 workspace、CUDA Graph pool、PyTorch allocator 与碎片化。GPU 内存使用率 90% 时可以高效运行且不 OOM，也可能下一次长上下文请求立刻耗尽；要看最大请求形状与预留阈值。对 MIG partition、vGPU、多租户场景，应按实际分区容量和内存隔离能力统计，避免物理总显存与租户可用显存混分母。

## 5. 易混概念与边界

GPU Memory Utilization 可能指容量或内存控制器忙碌时间，必须用清晰字段名区分。它与 GPU Utilization 的 kernel busy、MFU 的计算量利用率、KV Cache hit rate 不是同一概念。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 80GB GPU 里已用 70GB，却不说明 HBM 带宽接近饱和？** 答：已用容量是静态分配量，可能由不活跃模型权重占据；带宽需根据每秒读写字节或 DRAM active 独立测量。

2. **问：PyTorch reserved 比 allocated 大很多是否必然是内存泄漏？** 答：不必然。Caching allocator 预留空闲块以复用，reserved 包含缓存；需检查 allocated/active、fragmentation、峰值请求和真实 OOM。

## 7. 中等难度考试题（含解析）

1. **题：可用 FB 容量 80GiB、已用 60GiB，容量利用率？** 解：`60/80=**75%**`，前提是全量容量可供当前进程使用。

2. **题：PyTorch allocator reserved=50GiB、allocated=38GiB，已保留但当前未被张量使用的量？** 解：`50−38=**12GiB**`，可能是缓存/碎片，不能直接判定泄漏。

## 8. 权威来源与延伸阅读

- [NVIDIA DCGM Field Identifiers](https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。
- [NVIDIA DCGM Exporter](https://docs.nvidia.com/datacenter/dcgm/latest/reference/dcgm-exporter-metrics.html)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。
- [PyTorch CUDA Memory Management](https://docs.pytorch.org/docs/stable/notes/cuda.html#memory-management)：可用于核查该指标定义、硬件语义与工程实现的官方或原始资料。

> 数值题仅为题设假设下的教学计算，不替代硬件实测或实际会计核算。
