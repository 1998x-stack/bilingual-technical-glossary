# Quantization（量化）

> 学科：AI Infrastructure · 专题：推理与服务 · 量化硬件支持和精度约束请核对实现版本

## 1. 核心定义

量化（Quantization）将权重、激活或 KV Cache 中的数值映射为较低位宽或有限可表示集合，以减少存储/访存、利用低精度硬件或控制成本。线性整数量化常写成 `q=clamp(round(x/scale)+zero_point,qmin,qmax)`，反量化 `x_hat=scale×(q−zero_point)`；具体精度取决于 scale 选择、granularity、舍入和异常值处理。

## 2. 形象理解

用 0.1 精度的刻度代替 0.001 精度的刻度，账本记录更短，但无法区分落在同一刻度里的细节；超过刻度范围的数字会饱和截断。压缩不等于无损，也不意味着读取与计算必然更快。

## 3. 技术原理与核心内容

量化分 per-tensor、per-channel、per-group；对称/非对称；静态/动态激活；INT8、INT4、FP8 等数值系统。scale 和 zero-point 也占元数据空间，低位编码需要 bit packing 和有时额外的 dequantize kernel。低位矩阵乘可能直接利用整数/浮点专用硬件，也可能先转换至 BF16 再计算。注意 outliers、Attention Softmax、LayerNorm、KV 精度等敏感位置。

## 4. 工程实践与设计权衡

先建立 BF16/FP16 效果、时延、吞吐及显存基线，随后分别测试 W8A8、W4A16 或 FP8 的已支持实现；对代表性输入校准，按不同请求长度/批次报告任务准确率、P95 时延、显存 peak 和成本。硬件不支持对应 low-bit kernel 时，位宽更小可能反而变慢。实测必须区分模型权重体积和运行时 KV/workspace。

## 5. 易混概念与边界

量化不是剪枝，也不等于普通 mixed precision；PTQ 是训练完成后压缩，QAT 在训练时模拟量化数值。Weight-only 只压缩权重，不能把模型中所有激活都算作 4-bit。

## 6. 中等难度面试题（含参考答案）

1. **问：同样 INT4 为何两种方法的效果可能不同？** 答：group size、calibration、outliers、scale、zero point 与 rounding 不同，还可能有不同矩阵乘内核和高精度累积。必须按目标模型/数据量测。

2. **问：权重从 BF16 到 INT4，为什么总显存不一定变为四分之一？** 答：其它激活、KV Cache、scale metadata、对齐和 kernel workspace 没有同比缩小，模型还可能有多副本或临时解量化。

## 7. 中等难度考试题（含解析）

1. **题：10,000,000 参数 BF16 每参数2字节、INT4理想0.5字节，不含其它开销，裸权重体积？** 解：BF16 **20MB**，INT4 **5MB**（十进制）；仅权重 payload 比例 1/4。

2. **题：对称量化 scale=0.1、z=0，x=0.26，采用就近取整，q 和反量化误差？** 解：q=`round(2.6)=**3**`；反量化 0.3，绝对误差 `|0.3−0.26|=**0.04**`。

## 8. 权威来源与延伸阅读

- [torchao Quantized Inference](https://docs.pytorch.org/ao/stable/workflows/inference.html)：量化数值语义与可用后端的维护者说明。
- [torchao Quantization Overview](https://docs.pytorch.org/ao/stable/contributing/quantization_overview.html)：量化数值语义与可用后端的维护者说明。

> 数值算例使用明确的理想假设，并非实际模型总显存的精确预测。
