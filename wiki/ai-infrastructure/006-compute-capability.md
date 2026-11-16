# Compute Capability（计算能力版本）

> AI Infra Wiki · Batch 01 · 术语 006/142 · 来源：[AI Infra 原始术语](../../data/ai-infrastructure.tsv)

## 1. 核心定义

**Compute Capability**（**计算能力版本**）：NVIDIA GPU 的架构能力标识，影响可用指令与特性。

**精确定义补充：** 它以 major.minor 标识 GPU 能支持的部分 ISA、线程与存储特性及资源限制。关键在于区分**硬件所提供的能力**、**程序的执行模型**和**应用实际获得的性能**。

## 2. 形象理解

Compute Capability 是 NVIDIA 为 GPU 架构特性给出的“能力级别”，类似软件需要识别的硬件指令集版本。

## 3. 技术原理与核心内容

它以 major.minor 标识 GPU 能支持的部分 ISA、线程与存储特性及资源限制。应用编译时常涉及虚拟架构 PTX 与目标机器代码；具体支持取决于 CUDA Toolkit、驱动、编译选项和硬件。

## 4. 工程实践与设计权衡

遇到“不支持的架构”或 kernel 启动失败，应检查设备能力与构建目标，如 nvcc 的 `-gencode` 配置；不能只依据显卡上市年份猜测。

## 5. 易混概念与边界

Compute Capability 不是 CUDA Toolkit 的版本号，也不是显卡算力评分：版本更高不等于所有负载都快。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么在新 GPU 上运行旧二进制有时不兼容？** 答：可能缺少可用机器代码或可 JIT 的 PTX，需结合构建目标与驱动兼容性分析。
2. **问：Compute Capability 如何影响优化？** 答：决定可用指令和硬件能力，例如特定异步拷贝、同步或精度支持。

## 7. 中等难度考试题（含解析）

1. **题：程序只为某单一架构编译了专用机器代码，部署到不同能力设备可能发生什么？** 解：未必能加载或执行，需包含兼容目标代码或合适 PTX。
2. **题：列出核对 CUDA 二进制兼容性时至少三项信息。** 解：GPU 计算能力、编译产物目标架构、驱动/Toolkit 与 PTX/JIT 支持情况。

## 8. 参考资料与延伸学习

- [官方技术资料](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/compute-capabilities.html)（访问时请核对文档版本及具体硬件型号）。
- [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)：可用于深入学习访存、并行效率、性能分析与实际度量。

## 9. 知识导航

- [返回 AI Infra Wiki 总目录](README.md)
- [返回术语对照表](../../glossaries/ai-infrastructure.md)

> 编辑原则：数值例题中的设备能力与开销均为题设或理想假定，不代表具体产品实测值。任何性能结论必须指明硬件、精度、工作负载和测试口径。
