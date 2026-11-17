# AI Infrastructure · 专业术语 Wiki

> 来源：[AI Infra TSV](../../data/ai-infrastructure.tsv) · 142 个术语 · 8 个专题 · 每批 20 个（末批 2 个）。

将原双语词条扩展为独立技术百科文章：精确定义、直观类比、核心机制、工程案例、易混辨析、两道中级面试题及答案、两道中级考试题及解析、权威参考资料。

**状态说明：** Batch 01–08 共 **142 篇已发布**；已完成 **142/142（100%）**。全部词条已有完整技术文章，独立领域专家审稿仍由人工证据台账单独跟踪。。每批独立审阅与校验后合并，计划条目不算完成。

## 批次总览

| Batch | 编号 | 主题 | 篇数 | 状态 |
|---|---|---|---:|---|
| 01 | 001–020 | 计算硬件与加速器 | 20 | 已发布 |
| 02 | 021–040 | 互连与网络、分布式训练 | 20 | 已发布 |
| 03 | 041–060 | 分布式训练、推理与服务 | 20 | 已发布 |
| 04 | 061–080 | 推理与服务、调度与容器 | 20 | 已发布 |
| 05 | 081–100 | 调度与容器、存储与数据 | 20 | 已发布 |
| 06 | 101–120 | 存储与数据、可靠性与可观测性 | 20 | 已发布 |
| 07 | 121–140 | 可靠性与可观测性、成本治理 | 20 | 已发布 |
| 08 | 141–142 | 成本、能效与资源治理 | 2 | 已发布 |

## Batch 02 综合学习路径

阅读 [Batch 02：互连与网络 → 数据并行训练](BATCH-02.md)，串起硬件互连、网络拓扑、集合通信与 DDP 性能调优。

## Batch 03 综合学习路径

阅读 [分布式训练 → 在线推理服务](BATCH-03.md)，重点区分并行维度、显存/通信、训练数值和服务治理。

## Batch 04 综合学习路径

阅读 [推理指标 → KV 管理 → 服务量化与部署](BATCH-04.md)；此路径仅用于仓库作者组织资料，不会出现在公开 Explorer 的导航栏。

## Batch 06 综合学习路径

阅读 [AI 数据链路 → SLI/SLO/SLA → 故障恢复和可观测性](BATCH-06.md)。此路线仅用于内部写作与审校，不出现在读者页面。

## Batch 07–08 综合学习路径

阅读 [可观测性 → 混沌工程 → GPU 效率 → FinOps 成本治理](BATCH-07.md)，以及 [Spot / Reserved Instance 采购与容量语义](BATCH-08.md)。以下路线仅供仓库作者研究，不在公开 Explorer 显示批次进度。

## 逐批术语清单

### Batch 01: 计算硬件与加速器

1. [Graphics Processing Unit（图形处理器）](001-graphics-processing-unit.md) · `GPU` · 已编写
2. [Tensor Processing Unit（张量处理单元）](002-tensor-processing-unit.md) · `TPU` · 已编写
3. [Neural Processing Unit（神经网络处理单元）](003-neural-processing-unit.md) · `NPU` · 已编写
4. [Application-Specific Integrated Circuit（专用集成电路）](004-application-specific-integrated-circuit.md) · `ASIC` · 已编写
5. [Field-Programmable Gate Array（现场可编程门阵列）](005-field-programmable-gate-array.md) · `FPGA` · 已编写
6. [Compute Capability（计算能力版本）](006-compute-capability.md) · 已编写
7. [Streaming Multiprocessor（流式多处理器）](007-streaming-multiprocessor.md) · `SM` · 已编写
8. [Compute Unified Device Architecture（统一计算设备架构）](008-compute-unified-device-architecture.md) · `CUDA` · 已编写
9. [Compute Unit（计算单元）](009-compute-unit.md) · `CU` · 已编写
10. [Warp（线程束）](010-warp.md) · 已编写
11. [Thread Block（线程块）](011-thread-block.md) · 已编写
12. [Register File（寄存器文件）](012-register-file.md) · 已编写
13. [Shared Memory（共享内存）](013-shared-memory.md) · 已编写
14. [High Bandwidth Memory（高带宽内存）](014-high-bandwidth-memory.md) · `HBM` · 已编写
15. [Double Data Rate Memory（双倍数据速率内存）](015-double-data-rate-memory.md) · `DDR` · 已编写
16. [Memory Bandwidth（内存带宽）](016-memory-bandwidth.md) · 已编写
17. [Memory Capacity（内存容量）](017-memory-capacity.md) · 已编写
18. [Peak FLOPS（峰值浮点运算性能）](018-peak-flops.md) · `FLOPS` · 已编写
19. [Thermal Design Power（热设计功耗）](019-thermal-design-power.md) · `TDP` · 已编写
20. [Power Usage Effectiveness（电源使用效率）](020-power-usage-effectiveness.md) · `PUE` · 已编写

### Batch 02: 互连与网络、分布式训练

21. [Peripheral Component Interconnect Express（高速外设互连）](021-peripheral-component-interconnect-express.md) · `PCIe` · 已发布
22. [NVLink（高速 GPU 互连）](022-nvlink.md) · `NVLink` · 已发布
23. [NVSwitch（GPU 互连交换芯片）](023-nvswitch.md) · `NVSwitch` · 已发布
24. [InfiniBand（无限带宽网络）](024-infiniband.md) · `IB` · 已发布
25. [Remote Direct Memory Access（远程直接内存访问）](025-remote-direct-memory-access.md) · `RDMA` · 已发布
26. [RDMA over Converged Ethernet（融合以太网上的 RDMA）](026-rdma-over-converged-ethernet.md) · `RoCE` · 已发布
27. [Ethernet（以太网）](027-ethernet.md) · 已发布
28. [Network Interface Card（网络接口卡）](028-network-interface-card.md) · `NIC` · 已发布
29. [Data Processing Unit（数据处理单元）](029-data-processing-unit.md) · `DPU` · 已发布
30. [SmartNIC（智能网卡）](030-smartnic.md) · 已发布
31. [Leaf-Spine Topology（叶脊网络拓扑）](031-leaf-spine-topology.md) · 已发布
32. [Fat-Tree Topology（胖树拓扑）](032-fat-tree-topology.md) · 已发布
33. [Bisection Bandwidth（二分带宽）](033-bisection-bandwidth.md) · 已发布
34. [Network Latency（网络延迟）](034-network-latency.md) · 已发布
35. [Network Throughput（网络吞吐量）](035-network-throughput.md) · 已发布
36. [All-Reduce（全归约通信）](036-all-reduce.md) · 已发布
37. [All-to-All（全互换通信）](037-all-to-all.md) · 已发布
38. [Collective Communication（集合通信）](038-collective-communication.md) · 已发布
39. [NVIDIA Collective Communications Library（NVIDIA 集合通信库）](039-nvidia-collective-communications-library.md) · `NCCL` · 已发布
40. [Data Parallelism（数据并行）](040-data-parallelism.md) · `DP` · 已发布

### Batch 03: 分布式训练、推理与服务

41. [Distributed Data Parallel（分布式数据并行）](041-distributed-data-parallel.md) · `DDP` · 已发布
42. [Tensor Parallelism（张量并行）](042-tensor-parallelism.md) · `TP` · 已发布
43. [Pipeline Parallelism（流水线并行）](043-pipeline-parallelism.md) · `PP` · 已发布
44. [Expert Parallelism（专家并行）](044-expert-parallelism.md) · `EP` · 已发布
45. [Sequence Parallelism（序列并行）](045-sequence-parallelism.md) · `SP` · 已发布
46. [Hybrid Parallelism（混合并行）](046-hybrid-parallelism.md) · 已发布
47. [Fully Sharded Data Parallel（全分片数据并行）](047-fully-sharded-data-parallel.md) · `FSDP` · 已发布
48. [Zero Redundancy Optimizer（零冗余优化器）](048-zero-redundancy-optimizer.md) · `ZeRO` · 已发布
49. [Gradient Accumulation（梯度累积）](049-gradient-accumulation.md) · 已发布
50. [Gradient Checkpointing（梯度检查点）](050-gradient-checkpointing.md) · 已发布
51. [Activation Recomputation（激活重计算）](051-activation-recomputation.md) · 已发布
52. [Mixed Precision Training（混合精度训练）](052-mixed-precision-training.md) · 已发布
53. [Loss Scaling（损失缩放）](053-loss-scaling.md) · 已发布
54. [Microbatch（微批次）](054-microbatch.md) · 已发布
55. [Global Batch Size（全局批量大小）](055-global-batch-size.md) · 已发布
56. [Checkpoint（训练检查点）](056-checkpoint.md) · 已发布
57. [Elastic Training（弹性训练）](057-elastic-training.md) · 已发布
58. [Straggler（慢节点）](058-straggler.md) · 已发布
59. [Inference Server（推理服务器）](059-inference-server.md) · 已发布
60. [Model Serving（模型服务化）](060-model-serving.md) · 已发布

### Batch 04: 推理与服务、调度与容器

61. [Time to First Token（首词元延迟）](061-time-to-first-token.md) · `TTFT` · 已发布
62. [Time per Output Token（每输出词元耗时）](062-time-per-output-token.md) · `TPOT` · 已发布
63. [Inter-Token Latency（词元间延迟）](063-inter-token-latency.md) · `ITL` · 已发布
64. [Tokens per Second（每秒词元数）](064-tokens-per-second.md) · `TPS` · 已发布
65. [Requests per Second（每秒请求数）](065-requests-per-second.md) · `RPS` · 已发布
66. [Prefill（预填充阶段）](066-prefill.md) · 已发布
67. [Decode（逐词元解码阶段）](067-decode.md) · 已发布
68. [Key-Value Cache（键值缓存）](068-key-value-cache.md) · `KV Cache` · 已发布
69. [Paged Attention（分页注意力）](069-paged-attention.md) · 已发布
70. [Continuous Batching（连续批处理）](070-continuous-batching.md) · 已发布
71. [Dynamic Batching（动态批处理）](071-dynamic-batching.md) · 已发布
72. [Speculative Decoding（推测解码）](072-speculative-decoding.md) · 已发布
73. [Disaggregated Prefill and Decode（预填充与解码分离）](073-disaggregated-prefill-and-decode.md) · `PD Disaggregation` · 已发布
74. [Quantization（量化）](074-quantization.md) · 已发布
75. [Weight-Only Quantization（仅权重量化）](075-weight-only-quantization.md) · 已发布
76. [Post-Training Quantization（训练后量化）](076-post-training-quantization.md) · `PTQ` · 已发布
77. [Quantization-Aware Training（量化感知训练）](077-quantization-aware-training.md) · `QAT` · 已发布
78. [Model Sharding（模型分片）](078-model-sharding.md) · 已发布
79. [Hot Reload（热重载）](079-hot-reload.md) · 已发布
80. [Container（容器）](080-container.md) · 已发布

### Batch 05: 调度与容器、存储与数据

81. [Container Image（容器镜像）](081-container-image.md) · 已发布
82. [Docker（Docker 容器平台）](082-docker.md) · 已发布
83. [Kubernetes（容器编排系统）](083-kubernetes.md) · `K8s` · 已发布
84. [Pod（容器组）](084-pod.md) · 已发布
85. [Node（集群节点）](085-node.md) · 已发布
86. [GPU Operator（GPU 运维算子）](086-gpu-operator.md) · 已发布
87. [Device Plugin（设备插件）](087-device-plugin.md) · 已发布
88. [Job（批处理任务）](088-job.md) · 已发布
89. [CronJob（定时任务）](089-cronjob.md) · 已发布
90. [Horizontal Pod Autoscaler（Pod 水平自动伸缩器）](090-horizontal-pod-autoscaler.md) · `HPA` · 已发布
91. [Cluster Autoscaler（集群自动扩缩容器）](091-cluster-autoscaler.md) · `CA` · 已发布
92. [Scheduler（调度器）](092-scheduler.md) · 已发布
93. [Resource Quota（资源配额）](093-resource-quota.md) · 已发布
94. [Node Affinity（节点亲和性）](094-node-affinity.md) · 已发布
95. [Taint and Toleration（污点与容忍）](095-taint-and-toleration.md) · 已发布
96. [Gang Scheduling（成组调度）](096-gang-scheduling.md) · 已发布
97. [Preemption（抢占）](097-preemption.md) · 已发布
98. [Object Storage（对象存储）](098-object-storage.md) · 已发布
99. [Block Storage（块存储）](099-block-storage.md) · 已发布
100. [Distributed File System（分布式文件系统）](100-distributed-file-system.md) · `DFS` · 已发布

### Batch 06: 存储与数据、可靠性与可观测性

101. [Network File System（网络文件系统）](101-network-file-system.md) · `NFS` · 已发布
102. [Parallel File System（并行文件系统）](102-parallel-file-system.md) · 已发布
103. [Storage Throughput（存储吞吐量）](103-storage-throughput.md) · 已发布
104. [Input/Output Operations per Second（每秒输入输出操作数）](104-input-output-operations-per-second.md) · `IOPS` · 已发布
105. [Data Lake（数据湖）](105-data-lake.md) · 已发布
106. [Data Pipeline（数据管道）](106-data-pipeline.md) · 已发布
107. [Data Shard（数据分片）](107-data-shard.md) · 已发布
108. [Data Loader（数据加载器）](108-data-loader.md) · 已发布
109. [Prefetching（预取）](109-prefetching.md) · 已发布
110. [Cache Hit Rate（缓存命中率）](110-cache-hit-rate.md) · 已发布
111. [Content Delivery Network（内容分发网络）](111-content-delivery-network.md) · `CDN` · 已发布
112. [Service Level Objective（服务级别目标）](112-service-level-objective.md) · `SLO` · 已发布
113. [Service Level Indicator（服务级别指标）](113-service-level-indicator.md) · `SLI` · 已发布
114. [Service Level Agreement（服务级别协议）](114-service-level-agreement.md) · `SLA` · 已发布
115. [Availability（可用性）](115-availability.md) · 已发布
116. [Reliability（可靠性）](116-reliability.md) · 已发布
117. [Mean Time Between Failures（平均故障间隔时间）](117-mean-time-between-failures.md) · `MTBF` · 已发布
118. [Mean Time to Recovery（平均恢复时间）](118-mean-time-to-recovery.md) · `MTTR` · 已发布
119. [Observability（可观测性）](119-observability.md) · 已发布
120. [Metrics（指标数据）](120-metrics.md) · 已发布

### Batch 07: 可靠性与可观测性、成本治理

121. [Logs（日志）](121-logs.md) · 已发布
122. [Distributed Tracing（分布式链路追踪）](122-distributed-tracing.md) · 已发布
123. [OpenTelemetry（开放遥测）](123-opentelemetry.md) · `OTel` · 已发布
124. [Prometheus（Prometheus 监控系统）](124-prometheus.md) · 已发布
125. [Grafana（Grafana 可视化平台）](125-grafana.md) · 已发布
126. [Alerting（告警）](126-alerting.md) · 已发布
127. [Load Testing（负载测试）](127-load-testing.md) · 已发布
128. [Chaos Engineering（混沌工程）](128-chaos-engineering.md) · 已发布
129. [Total Cost of Ownership（总体拥有成本）](129-total-cost-of-ownership.md) · `TCO` · 已发布
130. [Capital Expenditure（资本性支出）](130-capital-expenditure.md) · `CapEx` · 已发布
131. [Operating Expenditure（运营性支出）](131-operating-expenditure.md) · `OpEx` · 已发布
132. [GPU Utilization（GPU 利用率）](132-gpu-utilization.md) · 已发布
133. [GPU Memory Utilization（显存利用率）](133-gpu-memory-utilization.md) · 已发布
134. [Compute Efficiency（计算效率）](134-compute-efficiency.md) · 已发布
135. [Energy per Token（每词元能耗）](135-energy-per-token.md) · 已发布
136. [Cost per Million Tokens（每百万词元成本）](136-cost-per-million-tokens.md) · 已发布
137. [Workload Consolidation（工作负载整合）](137-workload-consolidation.md) · 已发布
138. [Multi-Tenancy（多租户）](138-multi-tenancy.md) · 已发布
139. [Capacity Planning（容量规划）](139-capacity-planning.md) · 已发布
140. [Autoscaling（自动扩缩容）](140-autoscaling.md) · 已发布

### Batch 08: 成本、能效与资源治理

141. [Spot Instance（竞价实例）](141-spot-instance.md) · 已发布
142. [Reserved Instance（预留实例）](142-reserved-instance.md) · 已发布

