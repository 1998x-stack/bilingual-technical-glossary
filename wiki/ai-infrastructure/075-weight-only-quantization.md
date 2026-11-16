# Weight-Only Quantization（仅权重量化）

> 学科：AI Infrastructure · 专题：推理与服务 · 量化硬件支持和精度约束请核对实现版本

## 1. 核心定义

仅权重量化（Weight-Only Quantization）将模型参数压缩为 INT4/INT8 等低位格式，而推理输入激活通常保持 BF16/FP16 等较高精度（例：W4A16）。它减少权重存储与读取字节数，但未必自动降低激活、KV Cache 和通信缓冲；实际算力效益依赖 mixed-dtype kernel 的实现。

## 2. 形象理解

把固定配方书压缩保存，需要查阅时解码内容，但每天的订单纸张仍是正常大小。配方书省了空间不意味着厨房操作台、原材料和配送时间也会按比例减少。

## 3. 技术原理与核心内容

典型做法按一定 group_size 对权重分组，计算 scale/zero point、舍入并打包低位权重；矩阵乘 kernel 载入时按 group 缩放，与高精度 activation 相乘并在受支持的精度累加。每组需要 metadata，某些 backend 对 group size、对齐、硬件指令有限制。torchao 官方文档描述了 INT4 weight-only 等配置及对应较高精度 activation；不能假设所有 low-bit 算法是同一布局。

## 4. 工程实践与设计权衡

对模型权重占显存大头、batch 不高的在线 LLM，可分别测试 BF16/INT8/INT4 weight-only 的模型文件大小、load time、权重显存、tokens/s、TTFT、输出质量。观察解量化开销是否抵消减少的显存带宽，以及多请求长上下文 KV cache 是否仍然成为主要 OOM 来源。量化分组与校准集必须与发布模型版本绑定。

## 5. 易混概念与边界

Weight-only 可视为一种量化应用范围；W8A8、FP8 动态激活+权重量化会进一步改变激活格式。它也可能由 PTQ 生成或与 QAT 训练流程结合，但不是所有 QAT 都是 weight-only。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 INT4 weight-only 对小 batch 可能更有利？** 答：小 batch 的权重加载相对重复利用更少，减少权重带宽需求可能显著；同时 bit unpack 和 scale 运算有成本，需针对目标 GPU 量测。

2. **问：权重已 INT4 为什么长输入仍会导致 OOM？** 答：KV Cache 随上下文和并发增长，激活、通信及临时工作区仍按其格式占显存；只压缩权重不会消除这些状态。

## 7. 中等难度考试题（含解析）

1. **题：10 亿个权重的理想 BF16 与 INT4 体积分别多少十进制 GB？** 解：BF16 `10^9×2=**2 GB**`；INT4 `10^9×0.5=**0.5 GB**`，不含 scale/元数据。

2. **题：128 个 4-bit 权重为一组，每组有一个 2 字节 scale、无 zero point；scale 元数据折合每权重多少 bit？** 解：一个 scale 有 16 bit；`16/128=**0.125 bit/weight**`，裸 payload 加 scale 合计约 4.125 bit/weight，忽略对齐。

## 8. 权威来源与延伸阅读

- [torchao Weight-only Configurations](https://docs.pytorch.org/ao/stable/workflows/inference.html)：量化数值语义与可用后端的维护者说明。
- [vLLM Quantization](https://docs.vllm.ai/en/latest/features/quantization/)：量化数值语义与可用后端的维护者说明。

> 数值算例使用明确的理想假设，并非实际模型总显存的精确预测。
