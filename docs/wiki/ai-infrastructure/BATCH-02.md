# Batch 02 · 互连与网络 → 数据并行训练（021–040）

> TERM/ATLAS · AI Infrastructure Wiki · 20 篇 · [返回完整索引](README.md) · [Issue #22](https://github.com/1998x-stack/bilingual-technical-glossary/issues/22)

## 研究目标

让多 GPU 从单机扩展到集群，首先要回答：**数据从哪条链路走、通信语义是什么、流量在哪里聚集、同步消耗几轮？**

## 从本地设备到分布式训练

```text
      GPU / HBM
         ├── 同节点：NVLink ↔ NVSwitch ↔ GPU
         └── I/O：PCIe ↔ NIC / DPU
                             │
                    InfiniBand 或 Ethernet + RoCE
                             │
                    Leaf-Spine / Fat-tree 网络
                             │
                    All-Reduce / All-to-All
                             │
                         NCCL / DDP
```

这是抽象数据路径，不代表所有架构强制经过相同设备：新型跨节点 NVLink 网络和专用交换 fabric 等可能不同。

## 推荐阅读与知识依赖

1. **设备与主机互连：** [PCIe](021-peripheral-component-interconnect-express.md) → [NVLink](022-nvlink.md) → [NVSwitch](023-nvswitch.md)。先查清 GPU 数据实际经过哪些链路。
2. **网络语义：** [InfiniBand](024-infiniband.md)、[RDMA](025-remote-direct-memory-access.md)、[RoCE](026-rdma-over-converged-ethernet.md)、[Ethernet](027-ethernet.md)。分清网络、协议与内存访问原语。
3. **端点与卸载：** [NIC](028-network-interface-card.md)、[DPU](029-data-processing-unit.md)、[SmartNIC](030-smartnic.md)。判断 CPU、网络设备各做哪些工作。
4. **网络拓扑和容量：** [Leaf-Spine](031-leaf-spine-topology.md) → [Fat-tree](032-fat-tree-topology.md) → [二分带宽](033-bisection-bandwidth.md)。计算路径、过订阅和跨半区瓶颈。
5. **性能模型：** [延迟](034-network-latency.md) 与 [吞吐](035-network-throughput.md) 必须分开测；还要关注长尾和实测 payload。
6. **分布式通信：** [All-Reduce](036-all-reduce.md)、[All-to-All](037-all-to-all.md) 和 [Collective Communication](038-collective-communication.md) → [NCCL](039-nvidia-collective-communications-library.md) → [Data Parallelism](040-data-parallelism.md)。

## 五个中级工程案例

| 场景 | 先问的问题 | 应收集的证据 |
|---|---|---|
| 单机 8 卡 All-Reduce 很慢 | 是 NVLink 还是 PCIe 降级？ | GPU topology、P2P、NCCL tests、算法选择 |
| 多机梯度同步卡住 | NIC 或路由/拥塞影响？ | NIC counters、IB/RoCE、NCCL rank 日志 |
| RoCE p99 抖动 | ECN、PFC 或队列积压？ | pause、CNP、drop、ECN、队列指标 |
| MoE 的 All-to-All 卡住 | 专家负载不均或网络 cut 不足？ | token 路由、进出流矩阵、二分带宽 |
| DDP 扩卡没有收益 | 通信是否盖过计算？ | backward trace、bucket、global batch |

## 关键公式：正确使用的条件

- `T≈α+n/β`：α 是启动开销，n 是字节数，β 是有效吞吐带宽；只适用于指定测量口径下的简化模型。
- `Oversubscription = ΣDownlink / ΣUplink`：必须明确端口方向，数值越高表示跨 Leaf 时潜在争用越强。
- `Ring All-Reduce per-rank traffic≈2(p-1)S/p`：理想环算法，p 个 rank、每 rank 输入 S 字节；不同 NCCL 算法结果不同。
- `All-to-All 有向进程对 = p(p−1)`：不计自发送，不等价于建立同样多的 TCP 连接。
- `Global batch = world_size × microbatch_per_rank × accumulation_steps`：假定各 rank 相同大小且每轮累积只更新一次。

## 官方资料与原始论文

- [PCI-SIG PCI Express Base](https://pcisig.com/specification-overview/pci-express-base)
- [NVIDIA NVLink Fabric Manager](https://docs.nvidia.com/datacenter/tesla/fabric-manager-user-guide/)
- [NVIDIA Cumulus Linux RoCE](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-40/Network-Solutions/RDMA-over-Converged-Ethernet-RoCE/)
- [NCCL Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)
- [PyTorch DistributedDataParallel](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html)
- [Al-Fares 等，SIGCOMM 2008](https://doi.org/10.1145/1402958.1402967)
