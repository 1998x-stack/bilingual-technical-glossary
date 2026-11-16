# Quantization-Aware Training（量化感知训练 · QAT）

> 学科：AI Infrastructure · 专题：推理与服务 · 具体实现应核对官方接口及版本

## 1. 核心定义

量化感知训练（Quantization-Aware Training，QAT）在训练或微调时引入**伪量化（fake quantization）**，使参数与梯度在训练中感知目标低位部署的舍入和截断误差，以争取更好的最终量化质量。训练阶段通常仍保留浮点参数及梯度，假量化前向模拟低位值，不代表整条训练链路真实以 INT4 算术执行。

## 2. 形象理解

建筑师设计家具时就使用最终工厂可加工的离散尺寸刻度，学习怎样避开无法生产的细节；相比做完精密设计后再强行取整，更有机会保持功能。设计过程中仍可能用高精度图纸与优化工具。

## 3. 技术原理与核心内容

典型 fake quantize：`q=clamp(round(x/s)+z,qmin,qmax)`，前向使用 `x_fq=s(q−z)` 作为近似输入；为了让离散 round 操作参与梯度传播，训练实现常用 straight-through estimator（STE）等近似，因而不是严格的普通连续求导。训练后需调用转换/导出路径生成受目标 backend 支持的实际低位权重及 kernel 配置。量化位宽、per-group scale、训练策略和 observer 更新时机影响准确率。

## 4. 工程实践与设计权衡

部署低位模型时，先用 PTQ 建立成本和精度基线；若精度低于业务阈值，采用 QAT fine-tune，并同时评估训练计算预算、数据许可和收敛稳定性。特别检查量化模型训练时的内存峰值（浮点 master weights 仍可能存在）、校准域外输入、INT4 导出是否被硬件支持，以及部署后生成质量与安全回归。

## 5. 易混概念与边界

QAT 与 PTQ 的主要区别是**训练中显式模拟量化并优化模型**；量化训练（例如 float8 matmul 直接运行前向/反向）可能使用真实低位硬件指令，不必等同于 fake-quant QAT。

## 6. 中等难度面试题（含参考答案）

1. **问：QAT 的 fake quant 为何要保留浮点权重？** 答：低位 round 不可微；训练常保留浮点可更新参数，用 STE 或其它近似将梯度传回，导出时再真实 pack 为低位。

2. **问：为什么 QAT 完成后仍要做 backend 实测？** 答：训练中的 fake quant 数值模拟不意味着导出低位 kernel 的布局、scale、累积精度完全相同；性能还依赖硬件指令、batch 与解包开销。

## 7. 中等难度考试题（含解析）

1. **题：理论 8-bit 对称有符号范围 [-127,127]，scale=0.2，x=1.13，忽略 tie 特例，q 与反量化值？** 解：`round(1.13/0.2)=round(5.65)=**6**`，反量化 **1.2**，误差 `1.2−1.13=**0.07**`。

2. **题：量化部署要求准确率≥94%，PTQ 测得 92.5%，QAT 测得 94.4%；哪个满足阈值，提升了多少百分点？** 解：只有 QAT 的 **94.4%** 达标；相较 PTQ 增加 `94.4−92.5=**1.9 个百分点**`，不是 1.9% 相对提升。

## 8. 权威来源与延伸阅读

- [torchao QAT Workflow](https://docs.pytorch.org/ao/stable/workflows/qat.html)：用于核对相关技术机制与版本边界的官方资料。
- [torchao Quantization Workflows](https://docs.pytorch.org/ao/stable/workflows/index.html)：用于核对相关技术机制与版本边界的官方资料。

> 题中数字为教学假设，不是任何设备、服务或容器环境的真实压测结果。
