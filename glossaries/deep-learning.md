# 深度学习 · Deep Learning

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：500 条 · 专题：18 类**

Neural networks, optimization, computer vision and generation

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 基础概念与张量（24 条）
- 02. 学习范式与数据处理（24 条）
- 03. 神经网络与基础模块（30 条）
- 04. 训练流程与梯度优化（35 条）
- 05. 损失函数、泛化与评估（30 条）
- 06. 卷积网络与计算机视觉（29 条）
- 07. 序列模型与时序学习（22 条）
- 08. 注意力机制与 Transformer（36 条）
- 09. 自监督、对比与表示学习（22 条）
- 10. 自然语言处理与大语言模型（36 条）
- 11. 生成模型与扩散模型（34 条）
- 12. 多模态学习与视觉语言（22 条）
- 13. 图神经网络与结构化学习（19 条）
- 14. 强化学习与对齐（27 条）
- 15. 模型压缩与高效微调（34 条）
- 16. 推理服务与系统部署（33 条）
- 17. 训练系统、分布式与工程（21 条）
- 18. 安全、可解释性与研究方法（22 条）

---

## 01. 基础概念与张量

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Artificial Intelligence (AI) | 人工智能 | AI | 研究与构建具备智能行为的系统。 |
| 2 | Machine Learning (ML) | 机器学习 | ML | 从数据中学习规律并用于预测或决策。 |
| 3 | Deep Learning (DL) | 深度学习 | DL | 使用多层可学习表示进行建模的方法。 |
| 4 | Neural Network (NN) | 神经网络 | NN | 由可学习的连接与非线性变换组成的模型。 |
| 5 | Representation Learning | 表示学习 |  | 自动学习适合下游任务的特征表示。 |
| 6 | Feature | 特征 |  | 描述输入样本的属性或变量。 |
| 7 | Feature Vector | 特征向量 |  | 以数值向量表示一组特征。 |
| 8 | Sample / Instance | 样本 / 实例 |  | 数据集中的一条观测记录。 |
| 9 | Label / Target | 标签 / 目标值 |  | 监督学习所使用的期望输出。 |
| 10 | Dataset | 数据集 |  | 供模型训练、验证或测试的数据集合。 |
| 11 | Training Set | 训练集 |  | 用于更新模型参数的数据。 |
| 12 | Validation Set | 验证集 |  | 用于选择模型或调节超参数的数据。 |
| 13 | Test Set | 测试集 |  | 用于最终评估泛化表现的留出数据。 |
| 14 | Tensor | 张量 |  | 具有任意维数的数值数组。 |
| 15 | Scalar | 标量 |  | 零阶张量；单个数值。 |
| 16 | Vector | 向量 |  | 一阶张量；一维数值数组。 |
| 17 | Matrix | 矩阵 |  | 二阶张量；二维数值数组。 |
| 18 | Tensor Shape | 张量形状 |  | 各维度长度的有序组合。 |
| 19 | Axis / Dimension | 轴 / 维度 |  | 张量的一个索引方向；语境也可指其长度。 |
| 20 | Rank (Tensor Order) | 张量阶数 |  | 张量拥有的轴数；勿与矩阵秩混淆。 |
| 21 | Batch Dimension | 批量维度 |  | 用来索引批内样本的维度。 |
| 22 | Channel | 通道 |  | 表示特征图或图像的特征分量。 |
| 23 | Embedding | 嵌入表示 |  | 对象映射到连续向量空间后的表示。 |
| 24 | Feature Map | 特征图 |  | 网络中间层产生的空间化特征张量。 |

## 02. 学习范式与数据处理

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Supervised Learning | 监督学习 |  | 使用带标签数据学习映射关系。 |
| 2 | Unsupervised Learning | 无监督学习 |  | 从无标签数据中发现结构或模式。 |
| 3 | Self-Supervised Learning (SSL) | 自监督学习 | SSL | 利用数据本身构造学习信号。 |
| 4 | Semi-Supervised Learning | 半监督学习 |  | 联合少量标注与大量未标注数据训练。 |
| 5 | Weak Supervision | 弱监督 |  | 使用不精确或有噪声的监督信号。 |
| 6 | Transfer Learning | 迁移学习 |  | 将已有任务学到的知识用于新任务。 |
| 7 | Multi-Task Learning | 多任务学习 |  | 一个模型联合优化多个相关任务。 |
| 8 | Meta-Learning | 元学习 |  | 学习如何更快适应新任务。 |
| 9 | Few-Shot Learning | 少样本学习 |  | 用极少标注样例学习新任务。 |
| 10 | Zero-Shot Learning | 零样本学习 |  | 在无目标任务标注示例下完成任务。 |
| 11 | Continual Learning | 持续学习 |  | 顺序学习新任务并尽量保留旧知识。 |
| 12 | Online Learning | 在线学习 |  | 数据逐步到来时持续更新模型。 |
| 13 | Curriculum Learning | 课程学习 |  | 按难度或顺序组织训练样本。 |
| 14 | Active Learning | 主动学习 |  | 选择最有价值的样本请求标注。 |
| 15 | Data Preprocessing | 数据预处理 |  | 在训练前清洗、转换或组织数据。 |
| 16 | Data Augmentation | 数据增强 |  | 通过合理变换扩充训练样本多样性。 |
| 17 | Normalization (Data) | 数据归一化 | Data | 将输入尺度映射到约定范围或分布。 |
| 18 | Standardization | 标准化 |  | 常指减均值再除标准差。 |
| 19 | Padding | 填充 |  | 将不同长度输入补齐以便批处理。 |
| 20 | Truncation | 截断 |  | 将超长输入裁剪到长度限制内。 |
| 21 | Data Leakage | 数据泄漏 |  | 训练过程意外使用了不应可见的信息。 |
| 22 | Class Imbalance | 类别不平衡 |  | 不同类别的样本数量差别较大。 |
| 23 | Domain Shift | 领域偏移 |  | 训练和应用场景中的数据分布发生变化。 |
| 24 | Out-of-Distribution (OOD) | 分布外 | OOD | 输入偏离训练数据主要分布的情形。 |

## 03. 神经网络与基础模块

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Perceptron | 感知机 |  | 线性加权求和后施加激活或阈值的单元。 |
| 2 | Multilayer Perceptron (MLP) | 多层感知机 | MLP | 由多层全连接变换组成的前馈网络。 |
| 3 | Feedforward Neural Network (FNN) | 前馈神经网络 | FNN | 信息从输入向输出单向传播的网络。 |
| 4 | Fully Connected Layer | 全连接层 |  | 每个输出单元与全部输入单元相连。 |
| 5 | Linear Layer | 线性层 |  | 执行仿射映射 Wx+b；名称沿用惯例。 |
| 6 | Hidden Layer | 隐藏层 |  | 位于输入层和输出层之间的网络层。 |
| 7 | Input Layer | 输入层 |  | 接收模型输入的部分。 |
| 8 | Output Layer | 输出层 |  | 生成预测或表示的最后一层。 |
| 9 | Neuron / Unit | 神经元 / 单元 |  | 进行加权运算与非线性变换的计算单元。 |
| 10 | Weight | 权重 |  | 连接或变换中的可学习系数。 |
| 11 | Bias | 偏置 |  | 仿射变换中的可学习偏移项。 |
| 12 | Parameter | 模型参数 |  | 通过训练数据与优化算法学得的变量。 |
| 13 | Hyperparameter | 超参数 |  | 由研究者或搜索流程指定的训练配置。 |
| 14 | Rectified Linear Unit (ReLU) | 修正线性单元 | ReLU | 激活函数 max(0,x)。 |
| 15 | Leaky ReLU | 带泄漏的 ReLU |  | 负半轴保留小斜率的激活函数。 |
| 16 | Gaussian Error Linear Unit (GELU) | 高斯误差线性单元 | GELU | 常见于 Transformer 的平滑激活函数。 |
| 17 | Sigmoid Function | Sigmoid 函数 |  | 将实数映射到 (0,1) 的 S 形函数。 |
| 18 | Hyperbolic Tangent (tanh) | 双曲正切函数 |  | 将实数映射到 (-1,1) 的激活函数。 |
| 19 | Softmax | Softmax 函数 |  | 把一组分数转为和为 1 的非负权重。 |
| 20 | Swish / SiLU | Swish / Sigmoid 线性单元 |  | 常写作 x·sigmoid(x) 的激活函数。 |
| 21 | Residual Connection | 残差连接 |  | 将模块输入加回其输出以改善优化。 |
| 22 | Skip Connection | 跳跃连接 |  | 绕过部分网络层的信息传递通路。 |
| 23 | Dense Connection | 密集连接 |  | 让层接收多个较早层的输出。 |
| 24 | Normalization Layer | 归一化层 |  | 对激活或表示进行尺度调整的模块。 |
| 25 | Batch Normalization (BatchNorm) | 批归一化 | BatchNorm | 利用批统计量标准化激活的技术。 |
| 26 | Layer Normalization (LayerNorm) | 层归一化 | LayerNorm | 在每个样本内部指定维度上归一化。 |
| 27 | Root Mean Square Norm (RMSNorm) | 均方根归一化 | RMSNorm | 以均方根缩放激活，通常不减均值。 |
| 28 | Group Normalization (GroupNorm) | 组归一化 | GroupNorm | 按通道分组计算归一化统计量。 |
| 29 | Dropout | 随机失活 |  | 训练时随机屏蔽部分激活的正则化方法。 |
| 30 | Stochastic Depth | 随机深度 |  | 训练时随机跳过某些残差分支。 |

## 04. 训练流程与梯度优化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Forward Pass | 前向传播 |  | 从输入计算预测和中间激活的过程。 |
| 2 | Backward Pass | 反向传播阶段 |  | 从损失向前层计算梯度的过程。 |
| 3 | Computational Graph | 计算图 |  | 描述运算及其依赖关系的图结构。 |
| 4 | Automatic Differentiation (Autodiff) | 自动微分 | Autodiff | 沿计算图自动求导的技术。 |
| 5 | Gradient | 梯度 |  | 损失对参数的一阶偏导数组。 |
| 6 | Gradient Descent (GD) | 梯度下降 | GD | 沿损失负梯度方向更新参数。 |
| 7 | Stochastic Gradient Descent (SGD) | 随机梯度下降 | SGD | 使用随机样本或小批量估计梯度。 |
| 8 | Mini-Batch | 小批量 |  | 一次参数更新使用的一组样本。 |
| 9 | Batch Size | 批大小 |  | 单批次使用的样本数或序列数。 |
| 10 | Epoch | 训练轮次 |  | 训练数据被完整遍历一次的周期。 |
| 11 | Iteration / Step | 迭代 / 更新步 |  | 通常指一次优化更新；具体框架定义可能不同。 |
| 12 | Learning Rate (LR) | 学习率 | LR | 控制每次参数更新幅度的系数。 |
| 13 | Learning Rate Scheduler | 学习率调度器 |  | 随训练进程调整学习率的规则。 |
| 14 | Warmup | 学习率预热 |  | 训练初期逐渐增大学习率的策略。 |
| 15 | Cosine Annealing | 余弦退火 |  | 依余弦曲线改变学习率的调度策略。 |
| 16 | Momentum | 动量 |  | 累积历史梯度方向来平滑参数更新。 |
| 17 | Nesterov Accelerated Gradient (NAG) | Nesterov 加速梯度 | NAG | 利用前瞻位置估计梯度的动量方法。 |
| 18 | Adaptive Gradient (AdaGrad) | 自适应梯度算法 | AdaGrad | 按历史平方梯度调整逐参数步长。 |
| 19 | Root Mean Square Propagation (RMSProp) | 均方根传播优化器 | RMSProp | 利用平方梯度移动平均缩放更新量。 |
| 20 | Adaptive Moment Estimation (Adam) | 自适应矩估计 | Adam | 结合梯度一阶和二阶矩估计的优化器。 |
| 21 | AdamW | 解耦权重衰减 Adam |  | 将权重衰减与自适应梯度更新解耦。 |
| 22 | Weight Decay | 权重衰减 |  | 使权重向零收缩的正则化更新。 |
| 23 | Gradient Clipping | 梯度裁剪 |  | 限制梯度范数或数值以稳定训练。 |
| 24 | Gradient Accumulation | 梯度累积 |  | 累积多个微批次梯度后再更新。 |
| 25 | Gradient Checkpointing | 梯度检查点 / 激活重计算 |  | 用重算中间激活换取显存节省。 |
| 26 | Vanishing Gradient | 梯度消失 |  | 深层传播中梯度变得极小的现象。 |
| 27 | Loss Landscape | 损失景观 |  | 模型参数与目标损失之间的几何关系。 |
| 28 | Convergence | 收敛 |  | 优化过程逐渐接近稳定解的状态。 |
| 29 | Early Stopping | 提前停止 |  | 验证指标不再改善时停止训练。 |
| 30 | Random Seed | 随机种子 |  | 用于控制随机过程的初始状态值。 |
| 31 | Initialization | 参数初始化 |  | 指定模型参数训练前的初始值。 |
| 32 | Xavier / Glorot Initialization | Xavier / Glorot 初始化 |  | 按输入输出规模调整初始方差的方法。 |
| 33 | He / Kaiming Initialization | He / Kaiming 初始化 |  | 常用于 ReLU 类网络的参数初始化。 |
| 34 | Mixed-Precision Training | 混合精度训练 |  | 结合不同浮点格式提升训练效率。 |
| 35 | Numerical Stability | 数值稳定性 |  | 计算对舍入误差与溢出的稳健程度。 |

## 05. 损失函数、泛化与评估

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Objective Function | 目标函数 |  | 训练要优化的整体数学目标。 |
| 2 | Loss Function | 损失函数 |  | 衡量预测结果与目标差异的函数。 |
| 3 | Mean Squared Error (MSE) | 均方误差 | MSE | 预测与目标平方差的均值。 |
| 4 | Mean Absolute Error (MAE) | 平均绝对误差 | MAE | 预测与目标绝对差的均值。 |
| 5 | Huber Loss | Huber 损失 |  | 结合平方误差与绝对误差性质的损失。 |
| 6 | Cross-Entropy Loss | 交叉熵损失 |  | 使用目标分布评估预测概率的损失。 |
| 7 | Binary Cross-Entropy (BCE) | 二元交叉熵 | BCE | 用于二分类或多标签预测的交叉熵。 |
| 8 | Negative Log-Likelihood (NLL) | 负对数似然 | NLL | 最大似然估计对应的最小化目标。 |
| 9 | Kullback–Leibler Divergence (KL) | KL 散度 / 相对熵 | KL | 衡量两个概率分布差异的非对称量。 |
| 10 | Jensen–Shannon Divergence (JS) | JS 散度 | JS | 基于 KL 构造的对称分布差异度量。 |
| 11 | L1 Regularization | L1 正则化 |  | 惩罚参数绝对值和以促使稀疏性。 |
| 12 | L2 Regularization | L2 正则化 |  | 惩罚参数平方和以限制参数大小。 |
| 13 | Label Smoothing | 标签平滑 |  | 降低目标分布的过度尖锐程度。 |
| 14 | Overfitting | 过拟合 |  | 拟合训练数据细节而导致泛化欠佳。 |
| 15 | Underfitting | 欠拟合 |  | 模型未充分学习数据中的规律。 |
| 16 | Generalization | 泛化 |  | 模型对未见样本保持表现的能力。 |
| 17 | Generalization Gap | 泛化差距 |  | 训练集和测试集表现之间的差异。 |
| 18 | Bias–Variance Tradeoff | 偏差—方差权衡 |  | 模型复杂度与估计波动间的经典关系。 |
| 19 | Cross-Validation | 交叉验证 |  | 轮换训练/验证划分评估模型的技术。 |
| 20 | Accuracy | 准确率 |  | 预测正确的样本占比。 |
| 21 | Precision | 精确率 / 查准率 |  | 预测为正的样本中真正为正的比例。 |
| 22 | Recall | 召回率 / 查全率 |  | 真实正样本中被识别出来的比例。 |
| 23 | F1 Score | F1 分数 |  | 精确率与召回率的调和平均。 |
| 24 | Confusion Matrix | 混淆矩阵 |  | 统计真实类别与预测类别交叉结果的矩阵。 |
| 25 | Receiver Operating Characteristic (ROC) | 受试者工作特征曲线 | ROC | 展示不同阈值下真阳性率与假阳性率。 |
| 26 | Area Under the ROC Curve (ROC-AUC) | ROC 曲线下面积 | ROC-AUC | 汇总分类器跨阈值排序能力的指标。 |
| 27 | Perplexity (PPL) | 困惑度 | PPL | 语言建模中由平均负对数似然推导的指标。 |
| 28 | Calibration | 概率校准 |  | 预测置信度与实际频率的一致性。 |
| 29 | Ablation Study | 消融实验 |  | 移除或改变组件以分析其贡献。 |
| 30 | Benchmark | 基准测试 |  | 通过统一任务、数据和协议比较方法。 |

## 06. 卷积网络与计算机视觉

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Convolution | 卷积 |  | 利用局部核对输入进行空间滤波的运算。 |
| 2 | Convolutional Neural Network (CNN) | 卷积神经网络 | CNN | 利用卷积层提取局部与层级特征的模型。 |
| 3 | Convolution Kernel / Filter | 卷积核 / 滤波器 |  | 在输入上滑动的可学习权重模板。 |
| 4 | Stride | 步幅 |  | 卷积或池化窗口移动的间隔。 |
| 5 | Padding (Convolution) | 卷积填充 | Convolution | 在边界增加元素以控制输出尺寸。 |
| 6 | Dilation | 空洞率 / 膨胀系数 |  | 在卷积核元素间引入间隔的设置。 |
| 7 | Receptive Field | 感受野 |  | 影响某个输出单元的输入区域。 |
| 8 | Pooling | 池化 |  | 对局部区域进行汇聚与下采样。 |
| 9 | Max Pooling | 最大池化 |  | 取局部区域最大值的池化方法。 |
| 10 | Average Pooling | 平均池化 |  | 取局部区域平均值的池化方法。 |
| 11 | Global Average Pooling (GAP) | 全局平均池化 | GAP | 将每个通道的空间维度求平均。 |
| 12 | Depthwise Convolution | 逐通道卷积 |  | 每个输入通道单独执行卷积。 |
| 13 | Pointwise Convolution | 逐点卷积 |  | 通常指 1×1 卷积以混合通道。 |
| 14 | Depthwise Separable Convolution | 深度可分离卷积 |  | 将逐通道与逐点卷积分解组合。 |
| 15 | Transposed Convolution | 转置卷积 |  | 利用卷积线性算子的转置结构实现可学习上采样。 |
| 16 | Upsampling | 上采样 |  | 提高特征图空间分辨率的操作。 |
| 17 | Downsampling | 下采样 |  | 降低空间分辨率的操作。 |
| 18 | Residual Network (ResNet) | 残差网络 | ResNet | 以残差模块堆叠构建深层网络。 |
| 19 | Visual Geometry Group Network (VGG) | VGG 网络 | VGG | 以连续小卷积核为特征的经典 CNN。 |
| 20 | Inception Module | Inception 模块 |  | 并行使用多尺度卷积分支的模块。 |
| 21 | U-Net | U 形网络 |  | 结合编码器、解码器与跨层连接的架构。 |
| 22 | Object Detection | 目标检测 |  | 预测图像中目标类别与位置的任务。 |
| 23 | Bounding Box | 边界框 |  | 用矩形坐标表示目标所在区域。 |
| 24 | Non-Maximum Suppression (NMS) | 非极大值抑制 | NMS | 去除高度重叠的冗余检测框。 |
| 25 | Semantic Segmentation | 语义分割 |  | 为每个像素预测语义类别。 |
| 26 | Instance Segmentation | 实例分割 |  | 区分同类不同实例的像素区域。 |
| 27 | Image Classification | 图像分类 |  | 预测整幅图像所属类别的任务。 |
| 28 | Vision Transformer (ViT) | 视觉 Transformer | ViT | 将图像切成块并用 Transformer 建模。 |
| 29 | Patch Embedding | 图像块嵌入 |  | 将图像块映射为向量词元的过程。 |

## 07. 序列模型与时序学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Sequence Modeling | 序列建模 |  | 学习有序观测之间依赖关系的任务。 |
| 2 | Time Series | 时间序列 |  | 按时间索引排列的观测数据。 |
| 3 | Recurrent Neural Network (RNN) | 循环神经网络 | RNN | 通过递归状态处理序列输入的网络。 |
| 4 | Hidden State | 隐藏状态 |  | 编码截至当前时间步历史信息的内部状态。 |
| 5 | Long Short-Term Memory (LSTM) | 长短期记忆网络 | LSTM | 通过门控单元改善长依赖建模的 RNN。 |
| 6 | Gated Recurrent Unit (GRU) | 门控循环单元 | GRU | 采用更新门与重置门的循环结构。 |
| 7 | Bidirectional RNN | 双向循环神经网络 |  | 同时从两个方向编码序列上下文。 |
| 8 | Encoder–Decoder | 编码器—解码器 |  | 先编码输入再生成目标表示或序列的结构。 |
| 9 | Sequence-to-Sequence (Seq2Seq) | 序列到序列 | Seq2Seq | 将输入序列映射为输出序列的建模框架。 |
| 10 | Teacher Forcing | 教师强制 |  | 训练解码器时输入真实前一步目标的策略。 |
| 11 | Exposure Bias | 暴露偏差 |  | 训练时真实上下文与推理时模型生成上下文不一致。 |
| 12 | Autoregressive Modeling | 自回归建模 |  | 根据先前输出逐步预测下一元素。 |
| 13 | Non-Autoregressive Modeling | 非自回归建模 |  | 不依赖逐步串行预测完成输出。 |
| 14 | Sequence Length | 序列长度 |  | 序列中时间步或词元的数量。 |
| 15 | Time Step | 时间步 |  | 序列处理中的单个时间位置。 |
| 16 | Temporal Convolutional Network (TCN) | 时序卷积网络 | TCN | 使用时序卷积捕获序列依赖的架构。 |
| 17 | Connectionist Temporal Classification (CTC) | 连接时序分类 | CTC | 处理输入输出未对齐序列的目标函数。 |
| 18 | Beam Search | 束搜索 |  | 每步保留若干高分候选的序列解码方法。 |
| 19 | Greedy Decoding | 贪心解码 |  | 每步选择当前最高分输出的解码方法。 |
| 20 | State Space Model (SSM) | 状态空间模型 | SSM | 使用状态转移与观测方程建模序列。 |
| 21 | Selective State Space Model | 选择性状态空间模型 |  | 根据输入动态调整状态空间参数的结构。 |
| 22 | Mamba | Mamba 模型 |  | 采用选择性状态空间机制的序列模型家族。 |

## 08. 注意力机制与 Transformer

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Attention Mechanism | 注意力机制 |  | 根据相关性对不同信息进行加权聚合。 |
| 2 | Self-Attention | 自注意力 |  | 在同一序列或集合内部计算注意力。 |
| 3 | Cross-Attention | 交叉注意力 |  | 由一个序列查询另一个序列的信息。 |
| 4 | Scaled Dot-Product Attention | 缩放点积注意力 |  | 对 QKᵀ 按维度缩放后归一化并加权 V。 |
| 5 | Query (Q) | 查询向量 |  | 用于检索相关键值信息的向量。 |
| 6 | Key (K) | 键向量 |  | 与查询计算相似度的向量。 |
| 7 | Value (V) | 值向量 |  | 根据注意力权重被汇聚的内容向量。 |
| 8 | Attention Score | 注意力分数 |  | 归一化前表示相关性的数值。 |
| 9 | Attention Weight | 注意力权重 |  | 通常经 Softmax 归一化后的分配系数。 |
| 10 | Attention Mask | 注意力掩码 |  | 限制注意力可见位置的矩阵或规则。 |
| 11 | Padding Mask | 填充掩码 |  | 阻止模型关注补齐位置的掩码。 |
| 12 | Multi-Head Attention (MHA) | 多头注意力 | MHA | 在多个表示子空间中并行计算注意力。 |
| 13 | Grouped-Query Attention (GQA) | 分组查询注意力 | GQA | 多个查询头共享一组键值头的机制。 |
| 14 | Multi-Query Attention (MQA) | 多查询注意力 | MQA | 多个查询头共享一套键值头的机制。 |
| 15 | Attention Head | 注意力头 |  | 独立计算一组 Q、K、V 相关性的分支。 |
| 16 | Transformer | Transformer 架构 |  | 以注意力和前馈模块为核心的序列架构。 |
| 17 | Transformer Encoder | Transformer 编码器 |  | 生成上下文相关输入表示的堆叠结构。 |
| 18 | Transformer Decoder | Transformer 解码器 |  | 按指定可见性规则生成或变换序列的结构。 |
| 19 | Feed-Forward Network (FFN) | 前馈网络子层 | FFN | Transformer 中逐位置应用的非线性映射。 |
| 20 | Position Encoding | 位置编码 |  | 为序列注入位置信息的方式。 |
| 21 | Positional Embedding | 位置嵌入 |  | 通过向量表示位置信息的方式。 |
| 22 | Absolute Position Encoding | 绝对位置编码 |  | 直接表示词元在序列中的绝对位置。 |
| 23 | Relative Position Encoding | 相对位置编码 |  | 将词元间的位置差异融入注意力。 |
| 24 | Rotary Position Embedding (RoPE) | 旋转位置嵌入 | RoPE | 通过向量旋转编码相对位置信息。 |
| 25 | ALiBi | 线性偏置注意力 |  | 按相对位置为注意力分数添加线性偏置。 |
| 26 | Pre-Norm Transformer | 前归一化 Transformer |  | 在子层运算之前应用归一化的结构。 |
| 27 | Post-Norm Transformer | 后归一化 Transformer |  | 在残差相加后应用归一化的结构。 |
| 28 | KV Cache | 键值缓存 |  | 推理时缓存历史位置的键值张量。 |
| 29 | FlashAttention | FlashAttention 算法 |  | 使用分块和 I/O 感知计算加速精确注意力。 |
| 30 | Sliding Window Attention | 滑动窗口注意力 |  | 只关注邻近有限窗口内位置的机制。 |
| 31 | Sparse Attention | 稀疏注意力 |  | 仅对部分位置对计算注意力。 |
| 32 | Linear Attention | 线性注意力 |  | 通过结构变换降低注意力长度复杂度的方法类。 |
| 33 | Long-Context Modeling | 长上下文建模 |  | 处理很长序列依赖与检索的技术。 |
| 34 | Context Window | 上下文窗口 |  | 单次模型处理可用的输入上下文范围。 |
| 35 | Expert Routing | 专家路由 |  | 为输入词元分配专家子网络的过程。 |
| 36 | Load Balancing Loss | 负载均衡损失 |  | 鼓励专家被更均衡使用的辅助目标。 |

## 09. 自监督、对比与表示学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Pretraining | 预训练 |  | 先在较大数据上学习通用表示或能力。 |
| 2 | Fine-Tuning | 微调 |  | 在已有预训练权重上继续适配目标任务。 |
| 3 | Masked Language Modeling (MLM) | 掩码语言建模 | MLM | 根据上下文恢复被遮蔽词元的目标。 |
| 4 | Causal Language Modeling (CLM) | 因果语言建模 | CLM | 按序预测下一个词元的建模目标。 |
| 5 | Denoising Autoencoder | 去噪自编码器 |  | 通过重建受扰输入学习有用表示。 |
| 6 | Autoencoder (AE) | 自编码器 | AE | 将输入压缩编码后再尝试重建的模型。 |
| 7 | Bottleneck Representation | 瓶颈表示 |  | 网络中受容量约束的压缩表示。 |
| 8 | Contrastive Learning | 对比学习 |  | 拉近正样本表示并区分负样本表示。 |
| 9 | Positive Pair | 正样本对 |  | 训练目标希望其表示接近的样本组合。 |
| 10 | Negative Pair | 负样本对 |  | 训练目标希望其表示可区分的样本组合。 |
| 11 | InfoNCE Loss | InfoNCE 损失 |  | 常用于对比学习的归一化分类式损失。 |
| 12 | Temperature Parameter | 温度参数 |  | 调节 Softmax 或对比分数分布尖锐度。 |
| 13 | Triplet Loss | 三元组损失 |  | 约束锚点更接近正样本而远离负样本。 |
| 14 | Metric Learning | 度量学习 |  | 学习可反映语义相似性的距离空间。 |
| 15 | Siamese Network | 孪生网络 |  | 共享参数并比较两个输入表示的网络。 |
| 16 | Momentum Encoder | 动量编码器 |  | 由主网络参数滑动平均维护的编码器。 |
| 17 | Knowledge Distillation | 知识蒸馏 |  | 将教师模型的输出知识迁移到学生模型。 |
| 18 | Student Model | 学生模型 |  | 通过监督信号学习复现教师能力的模型。 |
| 19 | Masked Autoencoder (MAE) | 掩码自编码器 | MAE | 通过重建被掩码图像块学习视觉表示。 |
| 20 | Bootstrap Your Own Latent (BYOL) | BYOL 自监督方法 | BYOL | 通过在线/目标网络学习无显式负样本的表示。 |
| 21 | Contrastive Language–Image Pre-training (CLIP) | 图文对比预训练 | CLIP | 对齐图像和文本表示的对比学习框架。 |
| 22 | Embedding Space Alignment | 嵌入空间对齐 |  | 让不同来源或模态的表示具有可比性。 |

## 10. 自然语言处理与大语言模型

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Natural Language Processing (NLP) | 自然语言处理 | NLP | 让计算机理解、处理或生成自然语言。 |
| 2 | Language Model (LM) | 语言模型 | LM | 对语言序列的概率或下一个词元建模。 |
| 3 | Large Language Model (LLM) | 大语言模型 | LLM | 通常由海量数据训练的大规模语言模型。 |
| 4 | Foundation Model | 基础模型 |  | 在广泛数据上预训练、可适配多任务的模型。 |
| 5 | Decoder-Only Model | 纯解码器模型 |  | 以解码器堆叠为主体的语言模型架构。 |
| 6 | Encoder-Only Model | 纯编码器模型 |  | 以双向上下文表征为主的架构。 |
| 7 | Encoder–Decoder Model | 编码器—解码器模型 |  | 联合编码输入和解码输出的架构。 |
| 8 | Bidirectional Encoder Representations from Transformers (BERT) | BERT 模型 | BERT | 以掩码语言建模等目标训练的编码器模型。 |
| 9 | Generative Pre-trained Transformer (GPT) | 生成式预训练 Transformer | GPT | 通常指基于自回归 Transformer 的模型体系。 |
| 10 | Text-to-Text Transfer Transformer (T5) | 文本到文本迁移 | T5 | 把多类 NLP 任务统一为文本生成任务的模型。 |
| 11 | Token | 词元 |  | 文本经过分词器切分后的基本符号单位。 |
| 12 | Vocabulary | 词表 |  | 分词器可识别的词元集合。 |
| 13 | Byte Pair Encoding (BPE) | 字节对编码 | BPE | 反复合并高频符号对构建子词词表。 |
| 14 | WordPiece | WordPiece 分词 |  | 以子词单元构建词表的分词算法家族。 |
| 15 | SentencePiece | SentencePiece |  | 直接从原始文本训练分词器的工具与方法。 |
| 16 | Special Token | 特殊词元 |  | 标记边界、角色或控制信息的专用词元。 |
| 17 | Beginning-of-Sequence (BOS) | 序列起始词元 | BOS | 标记一段序列开始的位置。 |
| 18 | End-of-Sequence (EOS) | 序列结束词元 | EOS | 标记序列结束的位置。 |
| 19 | Next-Token Prediction | 下一词元预测 |  | 根据前文预测紧接词元的训练任务。 |
| 20 | Instruction Tuning | 指令微调 |  | 通过指令—响应样本优化任务遵循能力。 |
| 21 | Supervised Fine-Tuning (SFT) | 监督微调 | SFT | 用有监督示例进一步训练预训练模型。 |
| 22 | In-Context Learning (ICL) | 上下文学习 | ICL | 不更新参数，仅靠上下文示例适配任务。 |
| 23 | Prompt | 提示词 / 提示 |  | 提供给模型以引导输出的输入内容。 |
| 24 | Prompt Engineering | 提示工程 |  | 设计与优化输入以改善模型行为。 |
| 25 | System Prompt | 系统提示 |  | 指定模型角色与高优先级行为约束的输入。 |
| 26 | Few-Shot Prompting | 少样本提示 |  | 在提示中包含少量示例。 |
| 27 | Chain-of-Thought (CoT) Prompting | 思维链提示 |  | 引导模型生成中间推理步骤的提示方式。 |
| 28 | Retrieval-Augmented Generation (RAG) | 检索增强生成 | RAG | 先检索外部信息再辅助模型生成。 |
| 29 | Dense Retrieval | 稠密检索 |  | 使用向量表示及相似度查找文档。 |
| 30 | Sparse Retrieval | 稀疏检索 |  | 基于词项稀疏表示匹配文档。 |
| 31 | Reranker | 重排序器 |  | 对初步检索候选重新计算相关性排名。 |
| 32 | Vector Database | 向量数据库 |  | 支持向量索引和近邻检索的数据系统。 |
| 33 | Hallucination | 幻觉 |  | 模型输出表面可信但不受事实支持的内容。 |
| 34 | Grounding | 事实依据锚定 |  | 使生成内容与可验证信息源建立对应。 |
| 35 | Tool Calling / Function Calling | 工具调用 / 函数调用 |  | 模型按接口格式请求外部工具执行操作。 |
| 36 | Agentic Workflow | 智能体式工作流 |  | 模型结合规划、工具与反馈完成多步任务。 |

## 11. 生成模型与扩散模型

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Generative Model | 生成模型 |  | 学习数据分布并合成新样本的模型。 |
| 2 | Discriminative Model | 判别模型 |  | 学习输入到类别或目标的区分性映射。 |
| 3 | Maximum Likelihood Estimation (MLE) | 最大似然估计 | MLE | 通过最大化观测数据概率拟合模型。 |
| 4 | Latent Variable Model | 潜变量模型 |  | 使用隐含随机变量解释观测数据。 |
| 5 | Variational Autoencoder (VAE) | 变分自编码器 | VAE | 借助变分推断学习可采样潜变量模型。 |
| 6 | Evidence Lower Bound (ELBO) | 证据下界 | ELBO | 变分推断中用于近似优化对数似然的下界。 |
| 7 | Reparameterization Trick | 重参数化技巧 |  | 把随机采样改写为可微的确定性变换。 |
| 8 | Generative Adversarial Network (GAN) | 生成对抗网络 | GAN | 生成器与判别器通过对抗目标联合训练。 |
| 9 | Generator | 生成器 |  | 从随机输入或条件信息生成样本的网络。 |
| 10 | Discriminator | 判别器 |  | 对样本真实性或类别进行区分的网络。 |
| 11 | Mode Collapse | 模式崩溃 |  | 生成器只覆盖真实数据分布中的少数模式。 |
| 12 | Normalizing Flow | 归一化流 |  | 用可逆变换构造可计算密度的生成模型。 |
| 13 | Diffusion Model | 扩散模型 |  | 通过逐步加噪与学习去噪进行生成的模型。 |
| 14 | Denoising Diffusion Probabilistic Model (DDPM) | 去噪扩散概率模型 | DDPM | 利用马尔可夫加噪和反向去噪进行生成的框架。 |
| 15 | Denoising Diffusion Implicit Model (DDIM) | 去噪扩散隐式模型 | DDIM | 支持非马尔可夫与较少采样步数的采样方式。 |
| 16 | Forward Diffusion Process | 前向扩散过程 |  | 逐步对数据加入噪声的过程。 |
| 17 | Reverse Diffusion Process | 逆向扩散过程 |  | 从噪声逐步恢复样本的生成过程。 |
| 18 | Noise Schedule | 噪声调度 |  | 控制各扩散时间步噪声强度的规则。 |
| 19 | Noise Prediction | 噪声预测 |  | 训练网络估计加到样本上的噪声。 |
| 20 | Denoising Score Matching | 去噪分数匹配 |  | 通过去噪目标学习对数密度梯度的方法。 |
| 21 | Score Function | 分数函数 |  | 概率密度对输入的对数梯度。 |
| 22 | Score-Based Generative Model | 基于分数的生成模型 |  | 学习分布分数并用动力系统采样。 |
| 23 | Latent Diffusion Model (LDM) | 潜空间扩散模型 | LDM | 在压缩潜在空间而非像素空间运行扩散。 |
| 24 | Guidance Scale | 引导强度 |  | 控制条件生成中引导作用大小的系数。 |
| 25 | Sampling Step | 采样步数 |  | 生成过程执行的迭代去噪次数。 |
| 26 | Scheduler (Diffusion) | 扩散采样调度器 | Diffusion | 决定从一个噪声状态更新到下一个状态的规则。 |
| 27 | Flow Matching | 流匹配 |  | 通过回归目标速度场学习连续生成流的方法。 |
| 28 | Rectified Flow | 整流流 |  | 学习较直的概率流路径的连续生成方法。 |
| 29 | Consistency Model | 一致性模型 |  | 学习不同噪声时间状态间一致映射的模型。 |
| 30 | Text-to-Image (T2I) | 文生图 | T2I | 根据文本提示生成图像的任务。 |
| 31 | Image-to-Image (I2I) | 图生图 | I2I | 以现有图像为条件生成另一图像。 |
| 32 | Inpainting | 局部重绘 / 图像修复 |  | 在指定掩码区域内生成或恢复内容。 |
| 33 | Outpainting | 外扩绘图 |  | 将图像内容延伸到原始边界之外。 |
| 34 | Conditional Generation | 条件生成 |  | 根据类别、文本或其他约束生成内容。 |

## 12. 多模态学习与视觉语言

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Modality | 模态 |  | 文本、图像、音频、视频等信息形式。 |
| 2 | Multimodal Learning | 多模态学习 |  | 联合建模两种或多种信息模态。 |
| 3 | Vision-Language Model (VLM) | 视觉语言模型 | VLM | 联合处理视觉输入和语言信息的模型。 |
| 4 | Multimodal Large Language Model (MLLM) | 多模态大语言模型 | MLLM | 整合多模态输入能力的大语言模型。 |
| 5 | Vision Encoder | 视觉编码器 |  | 将图像或视频映射为特征表示的网络。 |
| 6 | Text Encoder | 文本编码器 |  | 将文本映射为上下文向量的网络。 |
| 7 | Audio Encoder | 音频编码器 |  | 将语音或声音映射为向量表示的模块。 |
| 8 | Cross-Modal Alignment | 跨模态对齐 |  | 学习不同模态表示之间的对应关系。 |
| 9 | Early Fusion | 早期融合 |  | 在输入或浅层表示阶段融合多模态信息。 |
| 10 | Late Fusion | 后期融合 |  | 在各模态独立建模后合并结果。 |
| 11 | Image Captioning | 图像描述生成 |  | 根据图像生成自然语言描述。 |
| 12 | Visual Question Answering (VQA) | 视觉问答 | VQA | 结合图像回答自然语言问题。 |
| 13 | Optical Character Recognition (OCR) | 光学字符识别 | OCR | 从图像中识别文字内容。 |
| 14 | Automatic Speech Recognition (ASR) | 自动语音识别 | ASR | 把语音信号转换为文本。 |
| 15 | Text-to-Speech (TTS) | 文本转语音 | TTS | 将文本合成为语音。 |
| 16 | Speech Synthesis | 语音合成 |  | 生成可听语音波形或特征。 |
| 17 | Speech-to-Text (STT) | 语音转文本 | STT | 将语音输入转写为文字的任务。 |
| 18 | Speaker Diarization | 说话人分段归属 |  | 标记录音中不同说话者的发言区间。 |
| 19 | Contrastive Audio–Text Learning | 音文对比学习 |  | 对齐音频与文本表示的学习方式。 |
| 20 | Video Understanding | 视频理解 |  | 识别、定位或推断视频中的内容与事件。 |
| 21 | Temporal Grounding | 时间定位 |  | 将文本描述与视频中的时间片段对应。 |
| 22 | Multimodal Retrieval | 多模态检索 |  | 使用一种或多种模态查询另一模态内容。 |

## 13. 图神经网络与结构化学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Graph Neural Network (GNN) | 图神经网络 | GNN | 在图结构上聚合邻居信息的神经模型。 |
| 2 | Graph | 图 |  | 由节点与边组成的关系结构。 |
| 3 | Node / Vertex | 节点 / 顶点 |  | 图中的实体或对象。 |
| 4 | Edge | 边 |  | 连接节点并表达关系的结构。 |
| 5 | Adjacency Matrix | 邻接矩阵 |  | 表示节点两两连接关系的矩阵。 |
| 6 | Edge Feature | 边特征 |  | 描述图中边属性的向量。 |
| 7 | Message Passing | 消息传递 |  | 节点通过邻接关系交换并聚合信息的机制。 |
| 8 | Neighborhood Aggregation | 邻域聚合 |  | 从相邻节点信息构造节点表示的操作。 |
| 9 | Graph Convolutional Network (GCN) | 图卷积网络 | GCN | 利用图结构传播和变换特征的架构。 |
| 10 | Graph Attention Network (GAT) | 图注意力网络 | GAT | 对不同邻居分配注意力权重的 GNN。 |
| 11 | GraphSAGE | 图采样与聚合网络 |  | 通过邻居采样和聚合学习节点表示的方法。 |
| 12 | Graph Isomorphism Network (GIN) | 图同构网络 | GIN | 强调图结构区分能力的 GNN 架构。 |
| 13 | Heterogeneous Graph | 异构图 |  | 包含多种节点或边类型的图。 |
| 14 | Knowledge Graph | 知识图谱 |  | 使用实体与关系表示知识的图结构。 |
| 15 | Graph Embedding | 图嵌入 |  | 将节点、边或整体图映射到向量空间。 |
| 16 | Node Classification | 节点分类 |  | 预测图中节点类别的任务。 |
| 17 | Link Prediction | 链接预测 |  | 预测节点之间是否存在或将出现连接。 |
| 18 | Graph Classification | 图分类 |  | 对整个图赋予类别标签的任务。 |
| 19 | Oversmoothing | 过平滑 |  | 深层 GNN 中节点表征趋于相似的现象。 |

## 14. 强化学习与对齐

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Reinforcement Learning (RL) | 强化学习 | RL | 通过与环境交互最大化长期回报的学习。 |
| 2 | Agent (RL) | 智能体 | RL | 依据观测选择动作的决策主体。 |
| 3 | Environment | 环境 |  | 执行动作并反馈状态与奖励的系统。 |
| 4 | State | 状态 |  | 环境用于描述当前情形的信息。 |
| 5 | Observation | 观测 |  | 智能体实际接收到的环境信息。 |
| 6 | Reward | 奖励 |  | 环境给出的即时反馈信号。 |
| 7 | Return | 回报 |  | 未来奖励的累计量，常包含折扣。 |
| 8 | Policy | 策略 |  | 从状态或观测到动作分布的映射。 |
| 9 | Value Function | 价值函数 |  | 估计状态或状态动作的预期回报。 |
| 10 | State-Value Function V(s) | 状态价值函数 |  | 按策略从某状态出发的期望回报。 |
| 11 | Action-Value Function Q(s,a) | 动作价值函数 |  | 在状态采取动作后按策略继续的期望回报。 |
| 12 | Advantage Function | 优势函数 |  | 动作价值相对状态价值的增量。 |
| 13 | Discount Factor (γ) | 折扣因子 |  | 控制未来奖励相对重要性的系数。 |
| 14 | Markov Decision Process (MDP) | 马尔可夫决策过程 | MDP | 用状态、动作、转移和奖励刻画决策问题。 |
| 15 | Bellman Equation | 贝尔曼方程 |  | 刻画价值与下一步价值递推关系的方程。 |
| 16 | Exploration vs. Exploitation | 探索与利用 |  | 尝试未知动作与使用现有最优认知之间的取舍。 |
| 17 | Q-Learning | Q 学习 |  | 学习最优动作价值函数的离策略方法。 |
| 18 | Deep Q-Network (DQN) | 深度 Q 网络 | DQN | 使用神经网络近似 Q 值的强化学习算法。 |
| 19 | Policy Gradient | 策略梯度 |  | 直接优化参数化策略期望回报的方法。 |
| 20 | Actor–Critic | 行动者—评论家 |  | 结合策略网络与价值评估网络的框架。 |
| 21 | Proximal Policy Optimization (PPO) | 近端策略优化 | PPO | 通过限制策略更新幅度稳定训练的算法。 |
| 22 | Reward Model (RM) | 奖励模型 | RM | 根据输出估计偏好或质量分数的模型。 |
| 23 | Reinforcement Learning from Human Feedback (RLHF) | 人类反馈强化学习 | RLHF | 借助人类偏好信号优化模型行为的流程。 |
| 24 | Direct Preference Optimization (DPO) | 直接偏好优化 | DPO | 通过偏好对直接优化策略的目标。 |
| 25 | Preference Dataset | 偏好数据集 |  | 包含候选回答比较或选择记录的数据。 |
| 26 | Alignment | 对齐 |  | 使模型行为更符合目标、偏好与约束。 |
| 27 | Offline Reinforcement Learning | 离线强化学习 |  | 仅使用预收集轨迹数据学习策略。 |

## 15. 模型压缩与高效微调

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Parameter-Efficient Fine-Tuning (PEFT) | 参数高效微调 | PEFT | 只训练较少参数适配预训练模型的技术。 |
| 2 | Low-Rank Adaptation (LoRA) | 低秩适配 | LoRA | 用低秩矩阵更新近似权重变化的微调方法。 |
| 3 | Quantized LoRA (QLoRA) | 量化低秩适配 | QLoRA | 结合低比特基座权重与 LoRA 微调的方法。 |
| 4 | Adapter Layer | 适配器层 |  | 插入网络并训练少量新参数的模块。 |
| 5 | Prefix Tuning | 前缀微调 |  | 学习可训练前缀状态来引导模型。 |
| 6 | Prompt Tuning | 提示微调 |  | 优化连续软提示向量的技术。 |
| 7 | Full Fine-Tuning | 全参数微调 |  | 更新基座模型全部或绝大部分参数。 |
| 8 | Frozen Weights | 冻结权重 |  | 训练期间保持不变的模型参数。 |
| 9 | Checkpoint | 检查点 |  | 保存参数及可选优化器状态的训练快照。 |
| 10 | State Dictionary (state_dict) | 状态字典 |  | 框架中存储模型参数与缓冲区的映射。 |
| 11 | Data Parallelism (DP) | 数据并行 | DP | 复制模型并处理不同数据分片的训练方式。 |
| 12 | Distributed Data Parallel (DDP) | 分布式数据并行 | DDP | 跨多设备同步梯度的并行方式。 |
| 13 | Tensor Parallelism (TP) | 张量并行 | TP | 将单个层的张量运算拆分到多设备。 |
| 14 | Pipeline Parallelism (PP) | 流水线并行 | PP | 把不同模型层放在不同设备分阶段执行。 |
| 15 | Model Parallelism | 模型并行 |  | 将同一模型的计算分布在多设备上。 |
| 16 | Sequence Parallelism (SP) | 序列并行 | SP | 沿序列维度拆分部分计算与激活。 |
| 17 | Expert Parallelism (EP) | 专家并行 | EP | 将 MoE 专家网络分散至不同设备。 |
| 18 | Fully Sharded Data Parallel (FSDP) | 全分片数据并行 | FSDP | 分片参数、梯度及优化器状态的并行方法。 |
| 19 | Zero Redundancy Optimizer (ZeRO) | 零冗余优化 | ZeRO | 通过跨设备分片训练状态降低显存占用。 |
| 20 | Micro-Batch | 微批次 |  | 一次流水线阶段或累积步骤处理的少量样本。 |
| 21 | Global Batch Size | 全局批大小 |  | 一次全局优化更新所覆盖的总样本量。 |
| 22 | All-Reduce | 全归约 |  | 聚合各设备数据并将结果回传给所有设备。 |
| 23 | All-Gather | 全收集 |  | 从各设备收集分片供所有设备使用。 |
| 24 | Gradient Synchronization | 梯度同步 |  | 在设备间协调梯度以保持一致更新。 |
| 25 | Automatic Mixed Precision (AMP) | 自动混合精度 | AMP | 自动选择部分运算的浮点精度。 |
| 26 | Brain Floating Point 16 (BF16) | 脑浮点 16 位格式 | BF16 | 指数范围接近 FP32 的低精度浮点格式。 |
| 27 | Float16 (FP16) | 16 位浮点格式 | FP16 | 常用于加速与节省显存的半精度格式。 |
| 28 | Float32 (FP32) | 32 位浮点格式 | FP32 | 广泛使用的单精度浮点数表示。 |
| 29 | Loss Scaling | 损失缩放 |  | 放大损失以减轻低精度梯度下溢。 |
| 30 | Gradient Overflow | 梯度溢出 |  | 数值超出浮点表示范围导致异常。 |
| 31 | Activation Offloading | 激活卸载 |  | 将部分激活转移到主存等低成本存储。 |
| 32 | Optimizer State | 优化器状态 |  | 动量、梯度矩等训练过程中保存的辅助量。 |
| 33 | Training Throughput | 训练吞吐量 |  | 单位时间处理的样本或词元数量。 |
| 34 | Hardware Utilization | 硬件利用率 |  | 计算设备实际被工作负载使用的程度。 |

## 16. 推理服务与系统部署

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Inference | 推理 |  | 使用训练好的模型产生预测或生成内容。 |
| 2 | Serving | 模型服务化 |  | 通过服务接口提供模型推理能力。 |
| 3 | Inference Latency | 推理延迟 |  | 请求到达后获得结果所需的时间。 |
| 4 | Time to First Token (TTFT) | 首词元时间 | TTFT | 从请求到返回首个生成词元的延迟。 |
| 5 | Time per Output Token (TPOT) | 每输出词元耗时 | TPOT | 连续生成阶段每个词元的平均耗时。 |
| 6 | Throughput | 吞吐量 |  | 单位时间完成的请求数或词元数。 |
| 7 | Requests per Second (RPS) | 每秒请求数 | RPS | 服务每秒处理请求的数量。 |
| 8 | Tokens per Second (TPS) | 每秒词元数 | TPS | 单位时间生成或处理的词元数量。 |
| 9 | Decoding Phase | 解码阶段 |  | 自回归模型逐步生成后续词元的阶段。 |
| 10 | Batching | 批处理 |  | 合并多个请求或样本以提高计算效率。 |
| 11 | Dynamic Batching | 动态批处理 |  | 运行时按请求到达情况组合批次。 |
| 12 | Continuous Batching | 连续批处理 |  | 在生成过程中动态加入或退出请求。 |
| 13 | Quantization | 量化 |  | 以更低比特宽度表示权重或激活。 |
| 14 | Post-Training Quantization (PTQ) | 训练后量化 | PTQ | 在模型训练完成后进行低比特转换。 |
| 15 | Quantization-Aware Training (QAT) | 量化感知训练 | QAT | 在训练中模拟低比特误差以适应量化。 |
| 16 | Weight-Only Quantization | 仅权重量化 |  | 主要压缩模型权重而保持较高精度激活。 |
| 17 | Pruning | 剪枝 |  | 移除不重要权重、通道或结构以减少计算。 |
| 18 | Structured Pruning | 结构化剪枝 |  | 按通道、注意力头等结构单元裁剪。 |
| 19 | Unstructured Pruning | 非结构化剪枝 |  | 按单个权重等不规则元素裁剪。 |
| 20 | Speculative Decoding | 推测解码 |  | 草稿模型提议词元并由目标模型并行验证。 |
| 21 | Draft Model | 草稿模型 |  | 在推测解码中提出候选词元的较小模型。 |
| 22 | Model Compilation | 模型编译 |  | 将计算图优化为适合硬件执行的形式。 |
| 23 | Kernel Fusion | 算子融合 |  | 将多个运算合并以减少访存与启动开销。 |
| 24 | Operator / Kernel | 算子 / 计算核 |  | 实现特定张量运算的执行单元。 |
| 25 | CUDA | CUDA 并行计算平台 |  | NVIDIA 的 GPU 计算平台与编程生态。 |
| 26 | GPU (Graphics Processing Unit) | 图形处理器 |  | 适合高度并行数值运算的处理器。 |
| 27 | TPU (Tensor Processing Unit) | 张量处理器 |  | 面向机器学习计算设计的加速器。 |
| 28 | ONNX (Open Neural Network Exchange) | 开放神经网络交换格式 |  | 跨框架表示模型计算图的格式与生态。 |
| 29 | TensorRT | TensorRT 推理优化工具 |  | NVIDIA 面向推理优化的工具集。 |
| 30 | PagedAttention | 分页式注意力缓存管理 |  | 以分页管理 KV 缓存缓解内存碎片的技术。 |
| 31 | Memory Bandwidth | 内存带宽 |  | 单位时间能够传输的数据量。 |
| 32 | Memory Footprint | 内存占用 |  | 模型、激活与缓存所占用的内存规模。 |
| 33 | Out-of-Memory (OOM) | 内存不足 | OOM | 模型运行所需内存超出可用容量的错误。 |

## 17. 训练系统、分布式与工程

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Robustness | 鲁棒性 |  | 模型在扰动或环境变化下保持性能的能力。 |
| 2 | Adversarial Example | 对抗样本 |  | 有意构造以诱发错误预测的输入。 |
| 3 | Adversarial Training | 对抗训练 |  | 加入对抗扰动样本以提高稳健性。 |
| 4 | Distribution Drift | 分布漂移 |  | 上线后输入或目标统计分布随时间变化。 |
| 5 | Model Monitoring | 模型监控 |  | 持续检测性能、数据质量与运行状态。 |
| 6 | Explainability | 可解释性 |  | 理解模型预测原因及行为机制的程度。 |
| 7 | Interpretability | 可理解性 / 可解释性 |  | 使模型内部机制或预测易于理解的性质。 |
| 8 | Feature Attribution | 特征归因 |  | 估计输入特征对预测结果的贡献。 |
| 9 | Saliency Map | 显著性图 |  | 用热图展示对预测较敏感的输入位置。 |
| 10 | Fairness (Machine Learning) | 机器学习公平性 |  | 评估并减轻模型对不同群体的不合理差异。 |
| 11 | Privacy-Preserving Learning | 隐私保护学习 |  | 训练或应用时降低泄露敏感信息的风险。 |
| 12 | Differential Privacy (DP) | 差分隐私 | DP | 通过限制单条记录对结果影响提供隐私保证。 |
| 13 | Federated Learning (FL) | 联邦学习 | FL | 数据留在各端，协同训练共享模型的范式。 |
| 14 | Membership Inference Attack | 成员推断攻击 |  | 推测某条数据是否出现在训练集中的攻击。 |
| 15 | Model Inversion Attack | 模型反演攻击 |  | 利用模型输出或参数推断敏感输入信息。 |
| 16 | Prompt Injection | 提示注入 |  | 恶意输入试图改变模型对指令的遵循行为。 |
| 17 | Jailbreak | 越狱攻击 |  | 诱使模型绕过既定安全或行为限制的输入。 |
| 18 | Red Teaming | 红队测试 |  | 主动寻找模型风险、漏洞或失效方式的测试。 |
| 19 | Reproducibility | 可复现性 |  | 按照描述的条件重新得到一致研究结果的能力。 |
| 20 | Model Card | 模型卡片 |  | 说明模型用途、限制和评估结果的文档。 |
| 21 | Data Card / Datasheet | 数据卡片 / 数据说明书 |  | 记录数据来源、组成、用途与风险的文档。 |

## 18. 安全、可解释性与研究方法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Linear Algebra | 线性代数 |  | 研究向量、矩阵及线性映射的数学领域。 |
| 2 | Calculus | 微积分 |  | 研究变化率、积分与极限的数学领域。 |
| 3 | Probability Distribution | 概率分布 |  | 描述随机变量取值规律的数学对象。 |
| 4 | Expectation | 期望 |  | 随机变量按概率加权的平均值。 |
| 5 | Variance | 方差 |  | 随机变量围绕期望波动程度的度量。 |
| 6 | Covariance | 协方差 |  | 刻画两个随机变量共同变化的程度。 |
| 7 | Jacobian Matrix | 雅可比矩阵 |  | 向量值函数对输入变量的一阶偏导矩阵。 |
| 8 | Hessian Matrix | 海森矩阵 |  | 标量函数对变量的二阶偏导矩阵。 |
| 9 | Chain Rule | 链式法则 |  | 复合函数求导的基本法则。 |
| 10 | Matrix Multiplication | 矩阵乘法 |  | 通过行列内积组合线性变换的运算。 |
| 11 | Dot Product | 点积 / 内积 |  | 按分量乘积求和得到标量的运算。 |
| 12 | Hadamard Product | 哈达玛积 |  | 两个同形状张量逐元素相乘。 |
| 13 | Element-wise Operation | 逐元素运算 |  | 分别对张量各对应元素执行运算。 |
| 14 | Broadcasting | 广播机制 |  | 按兼容维度扩展数组进行运算的规则。 |
| 15 | Reshape | 变形 / 重塑 |  | 在元素总数不变时改变张量形状。 |
| 16 | Transpose | 转置 |  | 交换张量的若干轴或矩阵行列。 |
| 17 | Concatenation (Concat) | 拼接 | Concat | 沿指定轴连接多个张量。 |
| 18 | Reduction | 归约运算 |  | 沿指定轴求和、求均值或最大值等。 |
| 19 | Singular Value Decomposition (SVD) | 奇异值分解 | SVD | 将矩阵分解为奇异向量和奇异值。 |
| 20 | Eigenvalue / Eigenvector | 特征值 / 特征向量 |  | 满足线性变换比例关系的标量与向量。 |
| 21 | Cosine Similarity | 余弦相似度 |  | 以向量夹角的余弦衡量方向相似性。 |
| 22 | Euclidean Distance | 欧几里得距离 |  | 向量之间的直线距离。 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/deep-learning.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
