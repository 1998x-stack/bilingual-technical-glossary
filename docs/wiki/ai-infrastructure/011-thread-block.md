# Thread Block（线程块）

> AI Infra Wiki · Batch 01 · 术语 011/142 · 来源：[AI Infra 原始术语](../../data/ai-infrastructure.tsv)

## 1. 核心定义

**Thread Block**（**线程块**）：在 GPU 上调度、共享局部资源的线程集合。

**适用边界：** CUDA 将线程组织为 block，再将 block 组织为 grid。解释该术语时应指明具体架构、设备代际或测量口径，不能将理论指标直接等同工程表现。

## 2. 形象理解

把 block 当成一支能互相交流的工作小队：队内线程可以共享片上暂存区并进行块内同步；不同小队不应假定天然同时运行。

## 3. 技术原理与核心内容

CUDA 将线程组织为 block，再将 block 组织为 grid。常规 block 被调度到一个 SM 执行，块内线程共享 shared memory，并可借助 `__syncthreads()` 完成块级同步。较新的 cluster 机制是进一步的跨块协作能力，不能混同于普通 block。

## 4. 工程实践与设计权衡

选择 block 大小时要平衡并行度、寄存器、共享内存和尾部浪费。通常从 128/256 等 32 的整数倍测试，但不能用单一参数断言最优。

## 5. 易混概念与边界

Block 不是 warp：一个 block 通常含多个 warp；block 内不同 warp 可通过同步协作，而 warp 是执行调度的基本线程组。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么将 block 从 128 线程增大到 1024 线程不一定加速？** 答：每个 block 占用更多寄存器/共享内存，可能降低 SM 上同时驻留的 block 数，减少延迟隐藏。
2. **问：块内同步与跨 block 同步有何区别？** 答：`__syncthreads()` 作用于一个 block；普通 kernel 不能靠它做全 grid 同步。

## 7. 中等难度考试题（含解析）

1. **题：处理 1,000 个元素，blockDim.x=256，至少要多少个 block？** 解：`ceil(1000/256)=4`，多出来的 24 个线程需要边界检查。
2. **题：为什么 `if (threadIdx.x < 16) __syncthreads()` 可能出错？** 解：块级屏障要求参与线程满足正确的收敛规则，只有部分线程抵达会形成死锁或未定义行为。

## 8. 参考资料与延伸学习

- [官方或行业技术资料](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)。请核对所用硬件与文档版本。
- [NVIDIA CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：了解性能度量与优化（不意味着本术语仅适用于 NVIDIA）。

## 9. 知识导航

- [返回 AI Infra Wiki 总目录](README.md)
- [返回术语对照表](../../glossaries/ai-infrastructure.md)

> 说明：题目中的规格与时间均为演示假设，未标注设备型号时不应视为产品实测指标。
