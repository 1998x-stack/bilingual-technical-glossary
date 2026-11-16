# Loss Scaling（损失缩放）

> 学科：AI Infrastructure · 专题：分布式训练 · 相关框架实现请核对所引用版本

## 1. 核心定义

损失缩放（Loss Scaling）是在低精度反向传播前，将损失乘以缩放因子 S，使部分很小的梯度暂时进入 FP16 等格式可表示的范围；更新参数前再对梯度除以 S，还原原始量级。主要针对梯度**下溢**，过大缩放会触发溢出，故通常采用动态缩放。

## 2. 形象理解

要称量一粒极轻的粉末，先扩大可测信号，再按倍率换算回原来的重量。但如果放大到仪器饱和，数据便无效，需要减小倍率并重做测量。类比不保证乘法过程无舍入误差。

## 3. 技术原理与核心内容

设原损失 L 和参数 θ，反向对 `S·L` 求导得 `S·∇L`；合法更新应在裁剪和优化器步之前乘以 `1/S`。PyTorch `GradScaler` 在检测到 `inf`/`NaN` 梯度后跳过对应 optimizer step、降低或调整缩放系数；数值正常时可逐步调高。结合 gradient accumulation，**一个有效 batch 内保持 scale 不变**，在所有微步累积完再 unscale、clip、step、update。BF16 的指数范围较大，通常不需要像 FP16 那样依赖缩放，但仍可能有其它数值问题。

## 4. 工程实践与设计权衡

追踪 `scaler.get_scale()`、跳过更新比例、梯度 norm 和损失曲线；如果 scale 长期下降应检查真实溢出源，而不是强制固定更大的数值。诊断顺序是确认 autocast dtype、单步 FP32 基线、异常层/softmax、未缩放前裁剪和多 optimizer 步顺序。多个 optimizer 在同一有效 batch 中的 scaler 使用要遵循 API。

## 5. 易混概念与边界

Loss scaling **不改变理论上的最优学习率**；若已经正确反缩放，真实梯度与未缩放数学上等价。它区别于把 loss 除以累积步数的 **gradient averaging**：后者改变所求有效 batch 的权重，前者是临时数值表示技巧。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么裁剪梯度必须发生在 unscale 后？** 答：若先裁剪，裁剪阈值作用在 S 倍的梯度上，会使本意的阈值被误解释为阈值/S，造成错误更新。先调用 `scaler.unscale_(optimizer)`，然后 clip、scaler.step、update。

2. **问：scale 提高后训练出现 NaN，自动缩放为什么可能会跳过 step？** 答：过大的 scaled gradient 可能 FP16 溢出成 inf；GradScaler 检测后放弃该 optimizer 更新并调低缩放，防止用非有限梯度污染权重。持续异常需要定位数值不稳定，而不能无限依赖跳步。

## 7. 中等难度考试题（含解析）

1. **题：真实梯度 `g=2×10^-8`、缩放 `S=4096`，scaled gradient 的数值为多少？** 解：`4096×2×10^-8=**8.192×10^-5**`，已达到 FP16 的正常值数量级；正确更新前再除以 4096 得到原始 `2×10^-8`。

2. **题：未缩放梯度向量 `(3,4)`，S=128，要求最大 L2 norm=1；正确裁剪后的梯度向量是多少？** 解：原范数 `sqrt(3²+4²)=5`；正确先反缩放再裁剪，乘 `1/5`，得到 **(0.6,0.8)**。若误用 scaled 范数 640 直接用阈值 1，则更新会错误缩小。

## 8. 权威来源与延伸阅读

- [PyTorch AMP Examples: Scaled Gradients](https://docs.pytorch.org/docs/stable/notes/amp_examples.html)：梯度累积与裁剪的 unscale 顺序。
- [PyTorch AMP API](https://docs.pytorch.org/docs/stable/amp.html)：动态缩放与跳步机制。

> 示例值为题设下的教学计算；硬件、数值格式和框架实现的实测结果以可复现实验为准。
