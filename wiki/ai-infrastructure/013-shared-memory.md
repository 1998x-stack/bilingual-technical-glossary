# Shared Memory（共享内存）

> AI Infra Wiki · Batch 01 · 术语 013/142 · 来源：[AI Infra 原始术语](../../data/ai-infrastructure.tsv)

## 1. 核心定义

**Shared Memory**（**共享内存**）：GPU 线程块内低延迟共享数据的存储区域。

**适用边界：** CUDA shared memory 通常位于 SM 片上，块内线程可读取与写入。解释该术语时应指明具体架构、设备代际或测量口径，不能将理论指标直接等同工程表现。

## 2. 形象理解

共享内存是每个线程块的小型共享工具台；先把常用材料搬到工具台，再让多个线程复用，可少跑远处仓库。

## 3. 技术原理与核心内容

CUDA shared memory 通常位于 SM 片上，块内线程可读取与写入。典型矩阵乘法将 global memory 的 tile 载入 shared memory，以减少重复读取；访问映射到不同 bank 有利于并行，冲突可能导致串行化。

## 4. 工程实践与设计权衡

使用共享内存需考虑加载/同步开销与容量占用。与其为小数据无条件复制，不如分析复用次数、global load 合并、bank conflict 和寄存器压力。

## 5. 易混概念与边界

shared memory 不等于 CPU 主内存，也不等于 L2 cache；它是显式可编程的块内共享存储空间，其生命周期与 block 关联。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么转置矩阵常引入 shared memory？** 答：通过 tile 重排将不连续的 global memory 访问变为较合并的访问，提高有效带宽。
2. **问：shared memory 是否总比 global memory 快？** 答：单次访问通常更低延迟，但数据搬运、屏障与 bank 冲突可能抵消优势。

## 7. 中等难度考试题（含解析）

1. **题：32 个线程访问同一 bank 的 32 个不同地址，与访问 32 个 bank 的地址相比可能发生什么？** 解：前者产生 bank conflict、可能串行化；后者可并行服务。
2. **题：一个块需要 48 KiB 共享内存，SM 可用 96 KiB，忽略其他约束最多驻留多少块？** 解：`floor(96/48)=2` 块。

## 8. 参考资料与延伸学习

- [官方或行业技术资料](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)。请核对所用硬件与文档版本。
- [NVIDIA CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：了解性能度量与优化（不意味着本术语仅适用于 NVIDIA）。

## 9. 知识导航

- [返回 AI Infra Wiki 总目录](README.md)
- [返回术语对照表](../../glossaries/ai-infrastructure.md)

> 说明：题目中的规格与时间均为演示假设，未标注设备型号时不应视为产品实测指标。
