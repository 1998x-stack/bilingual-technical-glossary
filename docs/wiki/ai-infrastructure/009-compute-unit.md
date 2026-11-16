# Compute Unit（计算单元 · CU）

> AI Infra Wiki · Batch 01 · 术语 009/142 · 来源：[AI Infra 原始术语](../../data/ai-infrastructure.tsv)

## 1. 核心定义

**Compute Unit**（**计算单元**，CU）：GPU 等加速器中的逻辑执行资源单元。

**精确定义补充：** 在 AMD GPU 的 ROCm/HIP 文档中，CU 是核心执行块，包含指令调度、向量与标量计算资源、寄存器和本地共享数据存储等。关键在于区分**硬件所提供的能力**、**程序的执行模型**和**应用实际获得的性能**。

## 2. 形象理解

Compute Unit 是加速器内的“计算车间”，但各厂商 CU 所含的 SIMD、寄存器与缓存层次并不统一。

## 3. 技术原理与核心内容

在 AMD GPU 的 ROCm/HIP 文档中，CU 是核心执行块，包含指令调度、向量与标量计算资源、寄存器和本地共享数据存储等。不同架构的 wavefront 宽度、CU 组成与执行组织可能不同。

## 4. 工程实践与设计权衡

优化 HIP kernel 时应检查 wavefront、工作组大小、寄存器压力和局部数据共享；比较设备时不能用 CU 数量直接换算 NVIDIA SM 数量或 TFLOPS。

## 5. 易混概念与边界

CU 在 AMD 语境中更具体；与 NVIDIA SM 功能角色相近但不是统一标准的等价单元。

## 6. 中等难度面试题（含参考答案）

1. **问：两块 GPU 的 CU 数相同，为什么性能差很多？** 答：每 CU 执行宽度、频率、矩阵单元、内存系统、架构代际均不同。
2. **问：为什么需要考虑 wavefront 宽度？** 答：它影响分支发散、线程映射和数据并行粒度，而且不同架构可能不同。

## 7. 中等难度考试题（含解析）

1. **题：若架构 A 为每 wavefront 32 线程，128 线程工作组包含多少个 wavefront？** 解：4 个；不是所有 AMD GPU 都固定为 32。
2. **题：在比较 CUDA 与 HIP 版本的矩阵乘法时，最应固定哪类实验条件？** 解：问题尺寸、数值精度、数据布局和测量口径，再报告各自设备与编译环境。

## 8. 参考资料与延伸学习

- [官方技术资料](https://rocmdocs.amd.com/projects/HIP/en/develop/understand/hardware_implementation.html)（访问时请核对文档版本及具体硬件型号）。
- [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：可用于深入学习访存、并行效率、性能分析与实际度量。

## 9. 知识导航

- [返回 AI Infra Wiki 总目录](../README.md)
- [返回术语对照表](../../glossaries/ai-infrastructure.md)

> 编辑原则：数值例题中的设备能力与开销均为题设或理想假定，不代表具体产品实测值。任何性能结论必须指明硬件、精度、工作负载和测试口径。
