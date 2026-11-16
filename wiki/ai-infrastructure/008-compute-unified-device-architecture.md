# Compute Unified Device Architecture（统一计算设备架构 · CUDA）

> AI Infra Wiki · Batch 01 · 术语 008/142 · 来源：[AI Infra 原始术语](../../data/ai-infrastructure.tsv)

## 1. 核心定义

**Compute Unified Device Architecture**（**统一计算设备架构**，CUDA）：NVIDIA 的并行计算平台与编程模型。

**精确定义补充：** CUDA C++ 使用 host 代码与 `__global__` kernel；通过 grid、block、thread 组织并行执行，并通过设备内存管理、stream、event 调度和同步。关键在于区分**硬件所提供的能力**、**程序的执行模型**和**应用实际获得的性能**。

## 2. 形象理解

CUDA 可以理解为连接开发者与 NVIDIA GPU 的整套工具链：语言扩展、运行时、编译器、库和调试分析工具，而不是芯片本身。

## 3. 技术原理与核心内容

CUDA C++ 使用 host 代码与 `__global__` kernel；通过 grid、block、thread 组织并行执行，并通过设备内存管理、stream、event 调度和同步。CUDA 架构还涉及驱动 API、PTX 和设备机器码。

## 4. 工程实践与设计权衡

生产系统优先使用 cuBLAS、cuDNN 等成熟库；定制 kernel 时测量数据搬运、线程配置与访存，切勿假设所有 GPU 都支持 CUDA。

## 5. 易混概念与边界

CUDA ≠ NVIDIA GPU 硬件；CUDA ≠ cuDNN：后者是其生态中的深度学习加速库；CUDA kernel ≠ CPU 线程。

## 6. 中等难度面试题（含参考答案）

1. **问：CUDA stream 为什么能提升吞吐？** 答：允许在依赖关系满足时异步排队并潜在重叠内核、拷贝，但是否并发取决于设备能力与资源。
2. **问：CPU 与 GPU 的同步开销为什么值得关注？** 答：错误的逐步同步会打断异步流水、降低吞吐。

## 7. 中等难度考试题（含解析）

1. **题：给定 gridDim.x=10、blockDim.x=256，理论创建多少线程？** 解：10×256=2,560；不代表它们同时运行。
2. **题：用哪个表达式计算一维全局线程索引？** 解：`blockIdx.x * blockDim.x + threadIdx.x`；越界时需要边界判断。

## 8. 参考资料与延伸学习

- [官方技术资料](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)（访问时请核对文档版本及具体硬件型号）。
- [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：可用于深入学习访存、并行效率、性能分析与实际度量。

## 9. 知识导航

- [返回 AI Infra Wiki 总目录](../README.md)
- [返回术语对照表](../../glossaries/ai-infrastructure.md)

> 编辑原则：数值例题中的设备能力与开销均为题设或理想假定，不代表具体产品实测值。任何性能结论必须指明硬件、精度、工作负载和测试口径。
