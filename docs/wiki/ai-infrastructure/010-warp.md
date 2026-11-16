# Warp（线程束）

> AI Infra Wiki · Batch 01 · 术语 010/142 · 来源：[AI Infra 原始术语](../../data/ai-infrastructure.tsv)

## 1. 核心定义

**Warp**（**线程束**）：NVIDIA GPU 中通常协同执行的一组线程。

**精确定义补充：** NVIDIA CUDA 的 warp 通常为 32 个线程，遵循 SIMT 执行模型。关键在于区分**硬件所提供的能力**、**程序的执行模型**和**应用实际获得的性能**。

## 2. 形象理解

Warp 像车间里按共同节拍协作的一小组工人：执行同一段程序，但遇到不同条件分支时部分工人会暂时等待。

## 3. 技术原理与核心内容

NVIDIA CUDA 的 warp 通常为 32 个线程，遵循 SIMT 执行模型。warp 内线程可持有不同数据与控制流；分支发散可能造成执行路径串行化。warp 调度用于在其他 warp 等待访存时隐藏延迟。

## 4. 工程实践与设计权衡

优化时尽可能保证相邻线程访存合并、避免不必要的 warp 内发散；但正确同步与内存可见性必须遵循编程模型，不能凭“同 warp 一定同步”臆测。

## 5. 易混概念与边界

Warp 是 NVIDIA CUDA 术语；AMD 使用 wavefront，宽度随架构可能为 32 或 64；SIMT 也不等于传统 SIMD 机器指令。

## 6. 中等难度面试题（含参考答案）

1. **问：一个 warp 中 16 个线程进入 if、另 16 个进入 else，会发生什么？** 答：两个分支路径可能分别执行，部分 lane 被屏蔽，导致有效并行利用率下降。
2. **问：为什么 blockSize 选 160 是合理的起点之一？** 答：160 是 32 的整数倍，不产生尾部不满的 warp，但是否最优仍需实际测试。

## 7. 中等难度考试题（含解析）

1. **题：一个 block 含 100 个线程，需要多少 warp？** 解：`ceil(100/32)=4`，最后一个 warp 有 28 个未使用 lane。
2. **题：若某条件分支两侧代价相近且每侧 16 lane，直观上为什么比全体同路慢？** 解：需为两条路径分别执行指令，实际损失取决于控制流与编译器优化。

## 8. 参考资料与延伸学习

- [官方技术资料](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)（访问时请核对文档版本及具体硬件型号）。
- [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：可用于深入学习访存、并行效率、性能分析与实际度量。

## 9. 知识导航

- [返回 AI Infra Wiki 总目录](../README.md)
- [返回术语对照表](../../glossaries/ai-infrastructure.md)

> 编辑原则：数值例题中的设备能力与开销均为题设或理想假定，不代表具体产品实测值。任何性能结论必须指明硬件、精度、工作负载和测试口径。
