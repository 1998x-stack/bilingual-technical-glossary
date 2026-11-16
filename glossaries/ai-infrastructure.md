# AI 基础设施 · AI Infrastructure / AI Infra

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：142 条 · 专题：8 类**

Accelerators, distributed systems, GPU serving and operations

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 计算硬件与加速器（20 条）
- 02. 互连与网络（19 条）
- 03. 分布式训练（19 条）
- 04. 推理与服务（21 条）
- 05. 调度与容器（18 条）
- 06. 存储与数据管道（14 条）
- 07. 可靠性与可观测性（17 条）
- 08. 成本、能效与资源治理（14 条）

---

## 01. 计算硬件与加速器

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Graphics Processing Unit | 图形处理器 | GPU | 擅长高并行计算的处理器，是 AI 训练与推理的主要加速设备。 |
| 2 | Tensor Processing Unit | 张量处理单元 | TPU | 面向张量计算设计的专用加速芯片。 |
| 3 | Neural Processing Unit | 神经网络处理单元 | NPU | 针对神经网络运算优化的处理器。 |
| 4 | Application-Specific Integrated Circuit | 专用集成电路 | ASIC | 为特定任务设计的集成电路。 |
| 5 | Field-Programmable Gate Array | 现场可编程门阵列 | FPGA | 可在部署后重新配置逻辑功能的芯片。 |
| 6 | Compute Capability | 计算能力版本 |  | NVIDIA GPU 的架构能力标识，影响可用指令与特性。 |
| 7 | Streaming Multiprocessor | 流式多处理器 | SM | GPU 内执行并行线程的主要计算单元。 |
| 8 | Compute Unified Device Architecture | 统一计算设备架构 | CUDA | NVIDIA 的并行计算平台与编程模型。 |
| 9 | Compute Unit | 计算单元 | CU | GPU 等加速器中的逻辑执行资源单元。 |
| 10 | Warp | 线程束 |  | NVIDIA GPU 中通常协同执行的一组线程。 |
| 11 | Thread Block | 线程块 |  | 在 GPU 上调度、共享局部资源的线程集合。 |
| 12 | Register File | 寄存器文件 |  | 处理器中用于存储高速临时变量的寄存器集合。 |
| 13 | Shared Memory | 共享内存 |  | GPU 线程块内低延迟共享数据的存储区域。 |
| 14 | High Bandwidth Memory | 高带宽内存 | HBM | 靠近加速芯片封装的高吞吐内存技术。 |
| 15 | Double Data Rate Memory | 双倍数据速率内存 | DDR | 广泛用于服务器主内存的 DRAM 技术。 |
| 16 | Memory Bandwidth | 内存带宽 |  | 内存系统单位时间可传输的数据量。 |
| 17 | Memory Capacity | 内存容量 |  | 设备可容纳的模型权重、激活与缓存总量。 |
| 18 | Peak FLOPS | 峰值浮点运算性能 | FLOPS | 硬件理论上每秒能执行的浮点运算量。 |
| 19 | Thermal Design Power | 热设计功耗 | TDP | 设备散热设计所参考的功耗指标。 |
| 20 | Power Usage Effectiveness | 电源使用效率 | PUE | 数据中心总能耗与 IT 设备能耗之比。 |

## 02. 互连与网络

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Peripheral Component Interconnect Express | 高速外设互连 | PCIe | 连接 CPU、GPU、网卡与其他设备的总线标准。 |
| 2 | NVLink | 高速 GPU 互连 | NVLink | NVIDIA 提供的高带宽设备互连技术。 |
| 3 | NVSwitch | GPU 互连交换芯片 | NVSwitch | 用于构建多 GPU 高带宽互连拓扑的交换芯片。 |
| 4 | InfiniBand | 无限带宽网络 | IB | 常用于高性能计算集群的低延迟网络技术。 |
| 5 | Remote Direct Memory Access | 远程直接内存访问 | RDMA | 网络设备绕过部分 CPU 路径直接读写远端内存。 |
| 6 | RDMA over Converged Ethernet | 融合以太网上的 RDMA | RoCE | 在以太网基础设施上实现 RDMA 的协议族。 |
| 7 | Ethernet | 以太网 |  | 数据中心广泛采用的有线网络技术。 |
| 8 | Network Interface Card | 网络接口卡 | NIC | 服务器接入计算机网络的硬件接口。 |
| 9 | Data Processing Unit | 数据处理单元 | DPU | 卸载网络、存储与安全等基础设施任务的处理器。 |
| 10 | SmartNIC | 智能网卡 |  | 具备可编程或任务卸载功能的网络接口卡。 |
| 11 | Leaf-Spine Topology | 叶脊网络拓扑 |  | 数据中心常见的多路径、低跳数网络架构。 |
| 12 | Fat-Tree Topology | 胖树拓扑 |  | 通过层次化交换结构提供高带宽通信能力的拓扑。 |
| 13 | Bisection Bandwidth | 二分带宽 |  | 将网络节点分成两半时两侧间的传输能力。 |
| 14 | Network Latency | 网络延迟 |  | 数据从源节点传输到目标节点的耗时。 |
| 15 | Network Throughput | 网络吞吐量 |  | 单位时间网络实际传输的数据量。 |
| 16 | All-Reduce | 全归约通信 |  | 分布式工作节点共同归约数据并获得结果的集合通信操作。 |
| 17 | All-to-All | 全互换通信 |  | 参与节点彼此交换各自数据块的集合通信操作。 |
| 18 | Collective Communication | 集合通信 |  | 多个计算参与者协作完成的数据交换操作。 |
| 19 | NVIDIA Collective Communications Library | NVIDIA 集合通信库 | NCCL | 针对 GPU 集群优化的通信库。 |

## 03. 分布式训练

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Data Parallelism | 数据并行 | DP | 多个设备处理不同训练样本并同步模型参数或梯度。 |
| 2 | Distributed Data Parallel | 分布式数据并行 | DDP | 跨进程同步梯度以并行训练模型的方式。 |
| 3 | Tensor Parallelism | 张量并行 | TP | 将单层张量计算拆分到多个设备执行。 |
| 4 | Pipeline Parallelism | 流水线并行 | PP | 将网络不同层部署到不同设备并以微批流水线执行。 |
| 5 | Expert Parallelism | 专家并行 | EP | 把混合专家模型中的专家分布到多个设备。 |
| 6 | Sequence Parallelism | 序列并行 | SP | 沿序列维拆分部分张量与计算。 |
| 7 | Hybrid Parallelism | 混合并行 |  | 组合数据、张量、流水线等并行策略。 |
| 8 | Fully Sharded Data Parallel | 全分片数据并行 | FSDP | 将参数、梯度及优化器状态分片存放的训练策略。 |
| 9 | Zero Redundancy Optimizer | 零冗余优化器 | ZeRO | 通过分片降低分布式优化过程中的冗余内存占用。 |
| 10 | Gradient Accumulation | 梯度累积 |  | 累计多个微批梯度后再进行一次参数更新。 |
| 11 | Gradient Checkpointing | 梯度检查点 |  | 反向传播时重计算部分激活以节省内存。 |
| 12 | Activation Recomputation | 激活重计算 |  | 使用额外计算换取训练期间更少的激活存储。 |
| 13 | Mixed Precision Training | 混合精度训练 |  | 结合不同数值精度平衡训练速度、显存与稳定性。 |
| 14 | Loss Scaling | 损失缩放 |  | 缩放损失或梯度以减轻低精度计算中的下溢。 |
| 15 | Microbatch | 微批次 |  | 将一个训练批次划分为更小的执行单位。 |
| 16 | Global Batch Size | 全局批量大小 |  | 一次参数更新涉及的全部设备样本总数。 |
| 17 | Checkpoint | 训练检查点 |  | 保存模型、优化器和训练状态以支持恢复。 |
| 18 | Elastic Training | 弹性训练 |  | 允许训练作业在设备数量改变后继续运行。 |
| 19 | Straggler | 慢节点 |  | 在同步并行作业中拖慢整体进度的参与设备。 |

## 04. 推理与服务

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Inference Server | 推理服务器 |  | 接收请求并执行模型前向计算的服务组件。 |
| 2 | Model Serving | 模型服务化 |  | 将模型封装为可管理、可访问的在线服务。 |
| 3 | Time to First Token | 首词元延迟 | TTFT | 从请求发出到输出首个词元的等待时间。 |
| 4 | Time per Output Token | 每输出词元耗时 | TPOT | 生成阶段输出相邻词元的平均时间。 |
| 5 | Inter-Token Latency | 词元间延迟 | ITL | 输出连续词元之间的时间间隔。 |
| 6 | Tokens per Second | 每秒词元数 | TPS | 模型单位时间处理或生成的词元数量。 |
| 7 | Requests per Second | 每秒请求数 | RPS | 服务单位时间完成或接收的请求数量，须说明口径。 |
| 8 | Prefill | 预填充阶段 |  | 处理已有输入上下文并生成初始 KV 缓存的推理阶段。 |
| 9 | Decode | 逐词元解码阶段 |  | 基于缓存逐步生成新词元的推理阶段。 |
| 10 | Key-Value Cache | 键值缓存 | KV Cache | 复用注意力层历史键和值的缓存。 |
| 11 | Paged Attention | 分页注意力 |  | 以分页式内存管理方式组织推理 KV 缓存的技术。 |
| 12 | Continuous Batching | 连续批处理 |  | 推理过程中动态加入和退出请求以提升利用率。 |
| 13 | Dynamic Batching | 动态批处理 |  | 根据请求到达情况组合待执行样本的批处理方式。 |
| 14 | Speculative Decoding | 推测解码 |  | 先由较小模型预测候选词元再由目标模型验证以加速生成。 |
| 15 | Disaggregated Prefill and Decode | 预填充与解码分离 | PD Disaggregation | 将预填充和解码阶段部署在不同资源池。 |
| 16 | Quantization | 量化 |  | 使用更低位宽数值表示权重或激活以降低资源需求。 |
| 17 | Weight-Only Quantization | 仅权重量化 |  | 只降低模型权重表示精度的量化方式。 |
| 18 | Post-Training Quantization | 训练后量化 | PTQ | 在模型训练完成后执行精度压缩。 |
| 19 | Quantization-Aware Training | 量化感知训练 | QAT | 训练时模拟量化误差以改善量化后性能。 |
| 20 | Model Sharding | 模型分片 |  | 将单个模型拆分存放或运行于多个设备。 |
| 21 | Hot Reload | 热重载 |  | 不完全停止服务而更新模型或配置。 |

## 05. 调度与容器

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Container | 容器 |  | 隔离应用运行环境的操作系统级虚拟化单元。 |
| 2 | Container Image | 容器镜像 |  | 用于构建容器运行环境的只读文件层集合。 |
| 3 | Docker | Docker 容器平台 |  | 常用的容器镜像构建及运行工具集。 |
| 4 | Kubernetes | 容器编排系统 | K8s | 自动部署、扩缩容和管理容器化工作负载的平台。 |
| 5 | Pod | 容器组 |  | Kubernetes 中共同调度的一个或多个容器。 |
| 6 | Node | 集群节点 |  | 为工作负载提供计算资源的物理机或虚拟机。 |
| 7 | GPU Operator | GPU 运维算子 |  | 自动化部署 GPU 驱动和相关运行组件的控制器。 |
| 8 | Device Plugin | 设备插件 |  | 向 Kubernetes 暴露专用硬件资源的扩展接口。 |
| 9 | Job | 批处理任务 |  | 执行一次性或有限期任务的工作负载对象。 |
| 10 | CronJob | 定时任务 |  | 按日程周期性创建 Job 的 Kubernetes 对象。 |
| 11 | Horizontal Pod Autoscaler | Pod 水平自动伸缩器 | HPA | 根据指标自动调整 Pod 副本数的控制器。 |
| 12 | Cluster Autoscaler | 集群自动扩缩容器 | CA | 根据调度需求调整节点数量的组件。 |
| 13 | Scheduler | 调度器 |  | 根据资源与策略将工作负载分配到节点。 |
| 14 | Resource Quota | 资源配额 |  | 限制命名空间等租户可使用的资源上限。 |
| 15 | Node Affinity | 节点亲和性 |  | 通过规则引导工作负载选择目标节点。 |
| 16 | Taint and Toleration | 污点与容忍 |  | 控制哪些工作负载可以调度到特定节点。 |
| 17 | Gang Scheduling | 成组调度 |  | 让一组相关作业资源共同满足条件后启动。 |
| 18 | Preemption | 抢占 |  | 为高优先级工作负载回收被占用资源的调度机制。 |

## 06. 存储与数据管道

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Object Storage | 对象存储 |  | 通过对象与键管理大规模非结构化数据的存储系统。 |
| 2 | Block Storage | 块存储 |  | 以固定大小的数据块提供存储读写能力。 |
| 3 | Distributed File System | 分布式文件系统 | DFS | 将文件数据与元信息分布到多台机器的系统。 |
| 4 | Network File System | 网络文件系统 | NFS | 让客户端通过网络访问远端文件的协议与实现。 |
| 5 | Parallel File System | 并行文件系统 |  | 多个节点并行访问共享文件数据的存储架构。 |
| 6 | Storage Throughput | 存储吞吐量 |  | 单位时间从存储系统读取或写入的数据量。 |
| 7 | Input/Output Operations per Second | 每秒输入输出操作数 | IOPS | 衡量存储系统随机读写操作速率的指标。 |
| 8 | Data Lake | 数据湖 |  | 存放结构化与非结构化原始数据的集中存储体系。 |
| 9 | Data Pipeline | 数据管道 |  | 将数据采集、转换、验证与传输串联的工作流。 |
| 10 | Data Shard | 数据分片 |  | 把完整数据集划分成可独立访问的子集。 |
| 11 | Data Loader | 数据加载器 |  | 负责读取、采样、批处理并向训练器供数的组件。 |
| 12 | Prefetching | 预取 |  | 提前读取或准备未来需要的数据以减少等待。 |
| 13 | Cache Hit Rate | 缓存命中率 |  | 请求的数据已存在于缓存中的比例。 |
| 14 | Content Delivery Network | 内容分发网络 | CDN | 通过地理分布式边缘节点加速内容交付。 |

## 07. 可靠性与可观测性

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Service Level Objective | 服务级别目标 | SLO | 服务性能或可靠性指标的目标值。 |
| 2 | Service Level Indicator | 服务级别指标 | SLI | 用于量化服务质量的可测指标。 |
| 3 | Service Level Agreement | 服务级别协议 | SLA | 服务方对服务质量作出的正式承诺。 |
| 4 | Availability | 可用性 |  | 服务在指定时间窗口内可正常使用的程度。 |
| 5 | Reliability | 可靠性 |  | 系统在目标条件下持续正确工作的能力。 |
| 6 | Mean Time Between Failures | 平均故障间隔时间 | MTBF | 连续故障之间的平均运行时长。 |
| 7 | Mean Time to Recovery | 平均恢复时间 | MTTR | 系统从故障恢复到正常状态的平均时间。 |
| 8 | Observability | 可观测性 |  | 通过外部信号推断系统内部运行状态的能力。 |
| 9 | Metrics | 指标数据 |  | 数值化描述系统性能、容量或错误状态的测量数据。 |
| 10 | Logs | 日志 |  | 按照时间记录的系统事件与运行消息。 |
| 11 | Distributed Tracing | 分布式链路追踪 |  | 跨服务关联单次请求处理过程的追踪技术。 |
| 12 | OpenTelemetry | 开放遥测 | OTel | 提供指标、日志和追踪采集标准的可观测性项目。 |
| 13 | Prometheus | Prometheus 监控系统 |  | 用于采集与查询时间序列指标的监控系统。 |
| 14 | Grafana | Grafana 可视化平台 |  | 常用于监控数据查询与仪表盘展示的工具。 |
| 15 | Alerting | 告警 |  | 当监控指标满足预设触发条件时通知负责方。 |
| 16 | Load Testing | 负载测试 |  | 在可控压力下测量系统性能和稳定性的测试。 |
| 17 | Chaos Engineering | 混沌工程 |  | 主动注入故障以验证系统韧性的工程方法。 |

## 08. 成本、能效与资源治理

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Total Cost of Ownership | 总体拥有成本 | TCO | 涵盖购置、运维和退役等全生命周期成本。 |
| 2 | Capital Expenditure | 资本性支出 | CapEx | 用于购买或建设长期资产的投入。 |
| 3 | Operating Expenditure | 运营性支出 | OpEx | 服务和设备持续运行产生的经常性开销。 |
| 4 | GPU Utilization | GPU 利用率 |  | 衡量 GPU 计算活动或资源忙碌程度的指标，口径依工具而异。 |
| 5 | GPU Memory Utilization | 显存利用率 |  | 已使用加速器内存占总容量的比例。 |
| 6 | Compute Efficiency | 计算效率 |  | 实际有效计算与理论容量或资源成本的比值。 |
| 7 | Energy per Token | 每词元能耗 |  | 模型推理处理或生成单个词元所耗费的能量。 |
| 8 | Cost per Million Tokens | 每百万词元成本 |  | 以百万词元为单位的模型服务定价或内部成本。 |
| 9 | Workload Consolidation | 工作负载整合 |  | 将多个任务合并调度以提高资源效率。 |
| 10 | Multi-Tenancy | 多租户 |  | 单套基础设施为多个逻辑隔离的租户提供服务。 |
| 11 | Capacity Planning | 容量规划 |  | 预测未来需求并规划计算、网络和存储资源。 |
| 12 | Autoscaling | 自动扩缩容 |  | 根据实时负载调整服务实例或计算资源。 |
| 13 | Spot Instance | 竞价实例 |  | 价格较低但可能被云平台回收的计算实例。 |
| 14 | Reserved Instance | 预留实例 |  | 通过承诺用量换取资源价格或可用性安排的云实例。 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/ai-infrastructure.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
