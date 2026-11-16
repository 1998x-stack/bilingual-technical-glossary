# Streaming Multiprocessor（流式多处理器 · SM）

> AI Infra Wiki · Batch 01 · 术语 007/142 · 来源：[AI Infra 原始术语](../../data/ai-infrastructure.tsv)

## 1. 核心定义

**Streaming Multiprocessor**（**流式多处理器**，SM）：GPU 内执行并行线程的主要计算单元。

**精确定义补充：** NVIDIA SM 包括 warp 调度、执行管线、寄存器与片上共享资源。关键在于区分**硬件所提供的能力**、**程序的执行模型**和**应用实际获得的性能**。

## 2. 形象理解

SM 可以想成 GPU 工厂中的一间车间：它容纳若干线程块，将线程划为多个 warp 交替执行以隐藏等待。

## 3. 技术原理与核心内容

NVIDIA SM 包括 warp 调度、执行管线、寄存器与片上共享资源。一个线程块分配给某个 SM 执行；同一 SM 可同时驻留多个块，受寄存器、共享内存、warp/线程等硬件上限共同约束。

## 4. 工程实践与设计权衡

调优时不要只盯着 SM 数目：每线程寄存器过多或每块共享内存过大，会限制驻留块数；高 occupancy 也不是唯一目标，应结合指令并行和实际延迟。

## 5. 易混概念与边界

SM 是 NVIDIA 特定硬件术语；AMD Compute Unit 是相近层次的概念，但结构并非一一等价。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么减少一个 kernel 的寄存器消耗可能加速它？** 答：可能提高每个 SM 可驻留 warp 数，改善延迟隐藏；若导致寄存器溢出反而可能变慢。
2. **问：线程块能否同时分散在两个 SM 上执行？** 答：常规 CUDA 线程块作为一个调度单位驻留一个 SM；新架构的 block cluster 为跨块协作引入额外能力。

## 7. 中等难度考试题（含解析）

1. **题：一个 SM 有 64 Ki 个 32-bit 寄存器，每线程需 64 个，忽略其他限制最多容纳多少线程？** 解：65,536/64=1,024 线程。
2. **题：为什么上述 1,024 线程不一定真的能驻留？** 解：仍受每块资源分配粒度、线程/warp 上限和共享内存等限制。

## 8. 参考资料与延伸学习

- [官方技术资料](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)（访问时请核对文档版本及具体硬件型号）。
- [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：可用于深入学习访存、并行效率、性能分析与实际度量。

## 9. 知识导航

- [返回 AI Infra Wiki 总目录](README.md)
- [返回术语对照表](../../glossaries/ai-infrastructure.md)

> 编辑原则：数值例题中的设备能力与开销均为题设或理想假定，不代表具体产品实测值。任何性能结论必须指明硬件、精度、工作负载和测试口径。
