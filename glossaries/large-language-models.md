# 大语言模型 LLM · Large Language Models

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：419 条 · 专题：16 类**

Tokenization, transformer, training, inference and alignment

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 基础概念与模型类别（24 条）
- 02. 数据、词元与文本表示（26 条）
- 03. 网络结构与 Transformer（25 条）
- 04. 预训练目标与训练策略（24 条）
- 05. 训练优化与分布式技术（29 条）
- 06. 指令微调与模型适配（28 条）
- 07. 偏好优化与人类反馈（18 条）
- 08. 提示工程与上下文学习（25 条）
- 09. 推理、解码与采样（26 条）
- 10. 模型推理加速与服务（33 条）
- 11. 检索增强生成与知识库（34 条）
- 12. Agent 与工具使用（25 条）
- 13. 多模态大模型（22 条）
- 14. 评测与基准（32 条）
- 15. 安全、对齐与可信性（29 条）
- 16. LLMOps 与部署工程（19 条）

---

## 01. 基础概念与模型类别

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Artificial Intelligence (AI) | 人工智能 | AI | 使计算系统执行感知、推理、生成或决策任务的广泛领域。 |
| 2 | Machine Learning (ML) | 机器学习 | ML | 从数据中学习模式，而非依赖逐条编写规则。 |
| 3 | Deep Learning (DL) | 深度学习 | DL | 以多层神经网络为核心的机器学习方法。 |
| 4 | Natural Language Processing (NLP) | 自然语言处理 | NLP | 计算机处理、理解或生成人类语言的技术领域。 |
| 5 | Generative AI (GenAI) | 生成式人工智能 | GenAI | 根据学习到的分布生成文本、图像、音频等内容。 |
| 6 | Language Model (LM) | 语言模型 | LM | 为词元序列建立概率模型，可用于预测或生成文本。 |
| 7 | Large Language Model (LLM) | 大语言模型 | LLM | 以大规模参数与数据训练的语言模型；规模边界并不严格统一。 |
| 8 | Foundation Model (FM) | 基础模型 | FM | 能迁移或适配多种下游任务的大规模预训练模型。 |
| 9 | Small Language Model (SLM) | 小语言模型 | SLM | 相对紧凑、适合资源受限环境的语言模型，非严格参数等级。 |
| 10 | Pre-trained Model | 预训练模型 |  | 先在广泛数据上学习，再被用于推理或进一步适配的模型。 |
| 11 | Base Model | 基座模型 |  | 通常指尚未充分指令对齐、主要保留预训练能力的模型。 |
| 12 | Instruction-tuned Model | 指令微调模型 |  | 经过指令示例训练，更擅长遵循自然语言任务要求。 |
| 13 | Chat Model | 对话模型 |  | 针对多轮交互、角色消息格式优化的语言模型。 |
| 14 | Reasoning Model | 推理模型 |  | 针对多步推理任务优化的模型；其内部实现因模型而异。 |
| 15 | Decoder-only Model | 仅解码器模型 |  | 使用因果注意力预测后续词元的常见生成架构。 |
| 16 | Encoder-only Model | 仅编码器模型 |  | 主要产生输入的上下文表示，常用于理解类任务。 |
| 17 | Encoder–Decoder Model | 编码器—解码器模型 |  | 将输入编码后由解码器生成输出的序列到序列架构。 |
| 18 | Autoregressive Model | 自回归模型 |  | 将序列概率拆解为逐步预测下一个词元的条件概率。 |
| 19 | Masked Language Model (MLM) | 掩码语言模型 | MLM | 通过恢复被遮盖的词元学习上下文表示。 |
| 20 | Causal Language Model (CLM) | 因果语言模型 | CLM | 以不查看未来词元为约束学习序列预测。 |
| 21 | Mixture of Experts (MoE) | 混合专家模型 | MoE | 用路由机制选择部分专家子网络参与计算。 |
| 22 | Dense Model | 稠密模型 |  | 常指每个词元经过同一组主要参数计算的模型。 |
| 23 | Open-weight Model | 开放权重模型 |  | 模型参数可获取，但不等同于完整开源或无限制许可。 |
| 24 | Proprietary Model | 专有模型 |  | 模型权重或关键实现由提供方控制、通常不公开。 |

## 02. 数据、词元与文本表示

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Corpus | 语料库 |  | 用于训练、测试或研究的文本或其他数据集合。 |
| 2 | Dataset | 数据集 |  | 经过组织并用于训练、验证或评测的样本集合。 |
| 3 | Training Set | 训练集 |  | 直接用于更新模型参数的数据部分。 |
| 4 | Validation Set | 验证集 |  | 用于调参、早停及模型选择的留出数据。 |
| 5 | Test Set | 测试集 |  | 原则上只用于最终泛化评估的独立数据。 |
| 6 | Data Curation | 数据整理与筛选 |  | 收集、过滤、清洗、去重、标注和质量控制的过程。 |
| 7 | Data Deduplication | 数据去重 |  | 移除相同或高度相似样本，降低重复学习与泄漏。 |
| 8 | Data Contamination | 数据污染 |  | 训练数据混入评测题目或答案等，导致评估失真。 |
| 9 | Data Leakage | 数据泄漏 |  | 模型在训练或评估中意外获得本不应可见的信息。 |
| 10 | Synthetic Data | 合成数据 |  | 由模型、程序或模拟过程生成的训练数据。 |
| 11 | Data Mixture | 数据混合比例 |  | 不同来源、领域或语言数据在训练中的配比。 |
| 12 | Curriculum Learning | 课程学习 |  | 按难度或特定顺序组织训练样本的方法。 |
| 13 | Token | 词元 |  | 分词器输出的基本离散单位，未必等于一个汉字或单词。 |
| 14 | Tokenizer | 分词器 |  | 将原始文本映射为词元及其 ID 的工具或算法。 |
| 15 | Vocabulary | 词表 |  | 分词器定义的可用词元及其编号集合。 |
| 16 | Byte Pair Encoding (BPE) | 字节对编码 | BPE | 通过迭代合并高频片段学习子词的分词方法。 |
| 17 | WordPiece | 词片分词 |  | 通过构造子词词表来表示词语的分词算法。 |
| 18 | Unigram Language Model Tokenization | 一元语言模型分词 |  | 从候选子词词表中选择能较好解释语料的分词方式。 |
| 19 | Beginning-of-Sequence (BOS) Token | 序列起始词元 |  | 标记输入或生成序列开始的位置。 |
| 20 | End-of-Sequence (EOS) Token | 序列结束词元 |  | 指示序列终止，常与停止生成相关。 |
| 21 | Padding Token (PAD) | 填充词元 | PAD | 将不同长度样本对齐为批量张量时使用的占位符。 |
| 22 | Token ID | 词元编号 |  | 词元在词表中的整数标识。 |
| 23 | Sequence Length | 序列长度 |  | 输入或输出中的词元数量。 |
| 24 | Embedding | 嵌入向量 |  | 把离散对象映射到连续数值向量空间的表示。 |
| 25 | Embedding Matrix | 嵌入矩阵 |  | 存放各词元可学习向量的参数矩阵。 |
| 26 | Semantic Similarity | 语义相似度 |  | 衡量文本或向量在语义上的接近程度。 |

## 03. 网络结构与 Transformer

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Neural Network | 神经网络 |  | 由参数化计算层构成、通过数据优化的函数模型。 |
| 2 | Parameter | 参数 |  | 训练过程中被学习的权重或偏置等数值。 |
| 3 | Weight | 权重 |  | 决定输入特征如何影响输出的可训练参数。 |
| 4 | Bias | 偏置 |  | 在线性变换中额外加入的可训练偏移项。 |
| 5 | Activation | 激活值 |  | 网络前向计算过程中产生的中间结果。 |
| 6 | Hidden State | 隐藏状态 |  | 某一层对当前位置或序列产生的内部表示。 |
| 7 | Tensor | 张量 |  | 带有形状和数据类型的多维数组。 |
| 8 | Embedding Dimension | 嵌入维度 |  | 词元嵌入向量包含的数值维度。 |
| 9 | Hidden Size | 隐藏层宽度 |  | Transformer 主要隐藏状态向量的维度。 |
| 10 | Depth | 网络深度 |  | 模型堆叠的层数或计算阶段数。 |
| 11 | Transformer | Transformer 架构 |  | 以注意力和前馈网络等模块构建的序列建模架构。 |
| 12 | Transformer Block | Transformer 模块 |  | 通常由注意力、前馈网络、残差和归一化组成。 |
| 13 | Feed-Forward Network (FFN) | 前馈网络 | FFN | 对各位置表示独立施加的非线性变换子网络。 |
| 14 | Activation Function | 激活函数 |  | 向神经网络引入非线性能力的函数。 |
| 15 | Gaussian Error Linear Unit (GELU) | 高斯误差线性单元 | GELU | Transformer 中常见的平滑激活函数。 |
| 16 | SwiGLU | SwiGLU 门控激活 |  | 结合 Swish 与门控线性单元的前馈结构。 |
| 17 | Residual Connection | 残差连接 |  | 把子模块输入与输出相加以帮助深层网络训练。 |
| 18 | Layer Normalization (LayerNorm) | 层归一化 | LayerNorm | 对样本内指定特征维度进行标准化的模块。 |
| 19 | Root Mean Square Normalization (RMSNorm) | 均方根归一化 | RMSNorm | 使用均方根进行缩放的归一化方法。 |
| 20 | Pre-Norm | 前置归一化 |  | 在注意力或前馈子层之前进行归一化的结构。 |
| 21 | Post-Norm | 后置归一化 |  | 在子层及残差结合之后归一化的结构。 |
| 22 | Output Head | 输出头 |  | 将隐藏状态映射到词表分数或任务输出的模块。 |
| 23 | Logits | 未归一化分数 |  | Softmax 之前的预测分数，通常并非概率。 |
| 24 | Softmax | 归一化指数函数 |  | 将分数转换为和为 1 的非负概率分布。 |
| 25 | Weight Tying | 权重共享绑定 |  | 使输入嵌入和输出投影等模块复用同一参数矩阵。 |

## 04. 预训练目标与训练策略

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Attention Mechanism | 注意力机制 |  | 根据相关性加权整合序列中不同位置的信息。 |
| 2 | Self-Attention | 自注意力 |  | 同一序列内的位置互相计算相关性并聚合信息。 |
| 3 | Cross-Attention | 交叉注意力 |  | 一组查询对另一组来源的键和值进行注意力计算。 |
| 4 | Query (Q) | 查询向量 |  | 注意力中用于检索相关信息的向量。 |
| 5 | Key (K) | 键向量 |  | 注意力中与查询匹配、形成相关性分数的向量。 |
| 6 | Value (V) | 值向量 |  | 按注意力权重汇总、传递信息的向量。 |
| 7 | Scaled Dot-Product Attention | 缩放点积注意力 |  | 将 Q 与 K 的点积缩放并归一化后加权 V。 |
| 8 | Multi-Head Attention (MHA) | 多头注意力 | MHA | 并行计算多个注意力头，再融合不同表示子空间。 |
| 9 | Grouped-Query Attention (GQA) | 分组查询注意力 | GQA | 多组查询头共享较少的键值头以降低开销。 |
| 10 | Multi-Head Latent Attention (MLA) | 多头潜在注意力 | MLA | 通过低维潜在表示压缩键值相关存储的注意力结构。 |
| 11 | Attention Head | 注意力头 |  | 独立计算一组 Q、K、V 注意力的子单元。 |
| 12 | Attention Score | 注意力分数 |  | 衡量查询与键匹配程度的中间数值。 |
| 13 | Attention Weight | 注意力权重 |  | 经归一化后用于加权值向量的系数。 |
| 14 | Attention Mask | 注意力掩码 |  | 限制某些位置参与注意力的掩码，具体语义依实现而异。 |
| 15 | Causal Mask | 因果掩码 |  | 阻止当前位置读取未来词元的注意力约束。 |
| 16 | Bidirectional Attention | 双向注意力 |  | 允许当前位置利用两侧上下文信息的注意力方式。 |
| 17 | Sliding Window Attention (SWA) | 滑动窗口注意力 | SWA | 主要关注局部窗口内词元的稀疏注意力设计。 |
| 18 | Sparse Attention | 稀疏注意力 |  | 仅计算部分词元对之间的注意力连接。 |
| 19 | Positional Encoding | 位置编码 |  | 为缺乏天然顺序感知的网络提供位置线索。 |
| 20 | Rotary Position Embedding (RoPE) | 旋转位置嵌入 | RoPE | 用旋转变换编码相对位置信息的常见方法。 |
| 21 | Relative Position Bias | 相对位置偏置 |  | 在注意力分数中注入词元相对距离的偏置。 |
| 22 | Attention with Linear Biases (ALiBi) | 线性偏置注意力 | ALiBi | 通过与距离相关的线性偏置引入位置信息。 |
| 23 | Context Window | 上下文窗口 |  | 模型一次计算可利用的上下文范围，通常以词元计。 |
| 24 | Long-context Modeling | 长上下文建模 |  | 使模型更有效处理较长输入、保持检索和推理能力。 |

## 05. 训练优化与分布式技术

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Pretraining | 预训练 |  | 在大规模数据上先学习通用模式的训练阶段。 |
| 2 | Fine-tuning | 微调 |  | 从已有权重出发，用新数据继续训练以适配目标。 |
| 3 | Next-token Prediction (NTP) | 下一词元预测 | NTP | 依据先前词元预测紧随其后的词元。 |
| 4 | Language Modeling Objective | 语言建模目标 |  | 用来衡量语言模型预测质量的训练优化目标。 |
| 5 | Cross-Entropy Loss | 交叉熵损失 |  | 衡量目标分布与预测概率分布差异的常用损失。 |
| 6 | Negative Log-Likelihood (NLL) | 负对数似然 | NLL | 最大似然训练中常用的负对数目标函数。 |
| 7 | Gradient | 梯度 |  | 损失函数对模型参数的偏导数组合。 |
| 8 | Gradient Descent | 梯度下降 |  | 沿梯度反方向更新参数的优化思想。 |
| 9 | Stochastic Gradient Descent (SGD) | 随机梯度下降 | SGD | 使用小批样本近似全量梯度更新参数。 |
| 10 | Adam Optimizer | Adam 优化器 |  | 结合梯度一、二阶矩估计的自适应优化算法。 |
| 11 | AdamW | AdamW 优化器 |  | 将权重衰减与 Adam 梯度更新解耦的变体。 |
| 12 | Learning Rate (LR) | 学习率 | LR | 控制每次参数更新幅度的超参数。 |
| 13 | Learning Rate Scheduler | 学习率调度器 |  | 按照训练进度动态调整学习率的方法。 |
| 14 | Warmup | 学习率预热 |  | 训练初期逐步提高学习率的安排。 |
| 15 | Weight Decay | 权重衰减 |  | 抑制参数过大、帮助正则化的更新机制。 |
| 16 | Gradient Clipping | 梯度裁剪 |  | 限制梯度大小以减轻梯度爆炸。 |
| 17 | Gradient Accumulation | 梯度累积 |  | 跨多个小批次累积梯度再进行一次更新。 |
| 18 | Batch Size | 批大小 |  | 一次参数更新相关的样本数；需区分微批和全局批。 |
| 19 | Microbatch | 微批次 |  | 一次设备前向或反向计算处理的较小数据批。 |
| 20 | Epoch | 训练轮次 |  | 遍历一次定义好的训练数据集。 |
| 21 | Training Step | 训练步 |  | 通常指一次优化器参数更新，具体平台定义可能不同。 |
| 22 | Checkpoint | 模型检查点 |  | 保存权重、优化器及训练进度等状态的快照。 |
| 23 | Loss Scaling | 损失缩放 |  | 混合精度训练中减轻小梯度下溢的技术。 |
| 24 | Mixed Precision Training | 混合精度训练 |  | 组合多种数值精度以平衡性能、显存和稳定性。 |
| 25 | Distributed Training | 分布式训练 |  | 跨多个计算设备协同训练模型。 |
| 26 | Data Parallelism (DP) | 数据并行 | DP | 在多个设备上复制模型并处理不同数据子批。 |
| 27 | Tensor Parallelism (TP) | 张量并行 | TP | 将某些张量运算拆分到多个设备执行。 |
| 28 | Pipeline Parallelism (PP) | 流水线并行 | PP | 将不同模型层放在不同设备上流水执行。 |
| 29 | Scaling Laws | 规模定律 |  | 描述性能随参数、数据或计算量变化的经验关系。 |

## 06. 指令微调与模型适配

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Post-training | 后训练 |  | 预训练后用于提升指令遵循、对齐或特定能力的训练阶段。 |
| 2 | Instruction Tuning | 指令微调 |  | 用指令—回答样本训练模型遵循任务说明。 |
| 3 | Supervised Fine-tuning (SFT) | 监督微调 | SFT | 利用带目标回答的示例直接优化模型输出。 |
| 4 | Alignment | 模型对齐 |  | 使模型行为更符合指定意图、规范与价值目标的过程。 |
| 5 | Preference Data | 偏好数据 |  | 包含相对更优与更差回答等比较信号的数据。 |
| 6 | Preference Optimization | 偏好优化 |  | 根据偏好比较信息改进模型输出分布的方法。 |
| 7 | Reward Model (RM) | 奖励模型 | RM | 为模型输出或轨迹提供质量或偏好分数的模型。 |
| 8 | Reinforcement Learning (RL) | 强化学习 | RL | 通过奖励信号学习策略以最大化预期回报。 |
| 9 | Reinforcement Learning from Human Feedback (RLHF) | 基于人类反馈的强化学习 | RLHF | 利用人类偏好相关奖励信号进行策略优化的训练范式。 |
| 10 | Reinforcement Learning from AI | 基于人工智能反馈的强化 |  | 使用 AI 产生的反馈信号辅助对齐优化。 |
| 11 | Policy | 策略 |  | 给定状态或上下文后产生动作或输出的分布。 |
| 12 | Reference Policy | 参考策略 |  | 在偏好或强化学习中用于限制策略偏移的对照模型。 |
| 13 | Reward | 奖励 |  | 对行为或输出质量的标量评价信号。 |
| 14 | Trajectory / Rollout | 轨迹／采样展开 |  | 策略与环境交互或模型生成的一段完整经历。 |
| 15 | Advantage Function | 优势函数 |  | 衡量某动作相对基准期望回报的增益。 |
| 16 | Value Function | 价值函数 |  | 估计状态或状态—动作组合未来累计回报的函数。 |
| 17 | Proximal Policy Optimization (PPO) | 近端策略优化 | PPO | 限制策略更新幅度的常用强化学习算法。 |
| 18 | Group Relative Policy Optimization (GRPO) | 组相对策略优化 | GRPO | 利用同题多条生成结果的组内相对信号优化策略。 |
| 19 | Direct Preference Optimization (DPO) | 直接偏好优化 | DPO | 从偏好对构建目标直接优化策略，无需单独在线策略 RL环节。 |
| 20 | Kahneman–Tversky Optimization (KTO) | 卡尼曼—特沃斯基优化 | KTO | 使用偏好效用思想、可处理二元好坏反馈的对齐方法。 |
| 21 | Odds Ratio Preference Optimization (ORPO) | 优势比偏好优化 | ORPO | 将监督学习与偏好约束结合的优化方法。 |
| 22 | KL Penalty | KL 惩罚项 |  | 限制更新后策略偏离参考策略的正则化项。 |
| 23 | Rejection Sampling | 拒绝采样 |  | 生成多条候选后按照规则或评分筛选样本。 |
| 24 | Best-of-N Sampling | N 选一采样 |  | 生成 N 个候选，再依据评分选择较优结果。 |
| 25 | Process Reward Model (PRM) | 过程奖励模型 | PRM | 对推理中间步骤质量提供评价的模型。 |
| 26 | Outcome Reward Model (ORM) | 结果奖励模型 | ORM | 主要根据最终答案或结果进行评分的模型。 |
| 27 | Verifiable Reward | 可验证奖励 |  | 可由测试、规则或确定性检验产生的奖励信号。 |
| 28 | Reward Hacking | 奖励投机 |  | 模型利用奖励定义缺陷得到高分但未实现真实目标。 |

## 07. 偏好优化与人类反馈

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Parameter-efficient Fine-tuning (PEFT) | 参数高效微调 | PEFT | 只更新少量附加或选定参数来适配模型。 |
| 2 | Full Fine-tuning | 全参数微调 |  | 更新模型全部或绝大部分可训练权重。 |
| 3 | Low-Rank Adaptation (LoRA) | 低秩适配 | LoRA | 以低秩增量矩阵调整权重，减少可训练参数。 |
| 4 | LoRA Rank | LoRA 秩 |  | 控制低秩增量矩阵维度与表达容量的超参数。 |
| 5 | LoRA Alpha | LoRA 缩放系数 |  | 控制低秩更新对原模型影响幅度的配置参数。 |
| 6 | Quantized Low-Rank Adaptation (QLoRA) | 量化低秩适配 | QLoRA | 将基座权重低比特量化并训练 LoRA 适配器。 |
| 7 | Adapter | 适配器模块 |  | 插入模型的少量可训练层或参数。 |
| 8 | Prefix Tuning | 前缀微调 |  | 学习可插入各层注意力计算的连续前缀表示。 |
| 9 | Prompt Tuning | 软提示微调 |  | 学习连续提示向量，通常不更新主体模型权重。 |
| 10 | Low-Rank Decomposition | 低秩分解 |  | 用较低秩矩阵近似高维权重或更新。 |
| 11 | Knowledge Distillation | 知识蒸馏 |  | 用教师模型输出信号训练更小或更快的学生模型。 |
| 12 | Teacher Model | 教师模型 |  | 向学生模型提供目标分布、标签或中间信号的模型。 |
| 13 | Student Model | 学生模型 |  | 在蒸馏过程中学习教师行为的模型。 |
| 14 | Pruning | 模型剪枝 |  | 移除部分连接、权重、通道或结构以降低开销。 |
| 15 | Model Merging | 模型合并 |  | 结合两个或多个模型权重或更新以整合能力。 |
| 16 | Task Vector | 任务向量 |  | 用微调前后权重差表征某种训练更新方向。 |
| 17 | Continual Learning | 持续学习 |  | 在学习新任务时尽量维持已有能力的训练方法。 |
| 18 | Catastrophic Forgetting | 灾难性遗忘 |  | 模型学习新内容后显著损失既有能力的现象。 |

## 08. 提示工程与上下文学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Prompt | 提示词／提示 |  | 提供给模型以影响其输出的输入文本或多模态内容。 |
| 2 | Prompt Engineering | 提示词工程 |  | 设计、测试和改进提示以提高任务表现的方法。 |
| 3 | System Prompt | 系统提示 |  | 由系统层提供的高优先级行为或任务指令。 |
| 4 | Developer Message | 开发者消息 |  | 应用开发者提供的指令消息，优先级依平台规则。 |
| 5 | User Message | 用户消息 |  | 用户向模型提交的请求或内容。 |
| 6 | Assistant Message | 助手消息 |  | 模型此前生成的对话轮次或内容。 |
| 7 | Chat Template | 对话模板 |  | 将多角色消息序列编码为模型所需词元格式的规则。 |
| 8 | Role Delimiter | 角色分隔符 |  | 标记不同消息角色或边界的特殊结构或词元。 |
| 9 | Instruction Hierarchy | 指令层级 |  | 不同来源指令存在优先顺序的处理原则。 |
| 10 | Zero-shot Prompting | 零样本提示 |  | 不提供任务示例、直接描述任务让模型完成。 |
| 11 | One-shot Prompting | 单样本提示 |  | 在提示中给出一个任务示例。 |
| 12 | Few-shot Prompting | 少样本提示 |  | 在提示中给出少量示例以引导模型行为。 |
| 13 | In-context Learning (ICL) | 上下文学习 | ICL | 模型仅利用当前上下文示例适应任务，而不更新权重。 |
| 14 | Chain-of-Thought (CoT) Prompting | 思维链提示 |  | 引导模型使用中间推理步骤完成任务的提示方法。 |
| 15 | Self-Consistency | 自洽性采样 |  | 比较多条推理或答案路径以提升最终选择质量。 |
| 16 | Tree of Thoughts (ToT) | 思维树 | ToT | 将多条候选推理分支组织为搜索树的方法。 |
| 17 | ReAct (Reason + Act) | 推理与行动交替 |  | 在推理、工具调用及观察之间迭代的代理范式。 |
| 18 | Structured Output | 结构化输出 |  | 要求输出遵循指定字段、类型或数据结构。 |
| 19 | JSON Schema | JSON 模式规范 |  | 描述 JSON 数据应有字段、类型和约束的规则。 |
| 20 | Constrained Decoding | 约束解码 |  | 在生成过程中限制输出符合格式、语法或词表约束。 |
| 21 | Context Engineering | 上下文工程 |  | 组织系统指令、检索内容、工具结果及历史消息的整体设计。 |
| 22 | Context Budget | 上下文预算 |  | 为提示、检索材料、历史与输出预留的词元配额。 |
| 23 | Context Truncation | 上下文截断 |  | 因长度限制而裁剪或舍弃部分输入内容。 |
| 24 | Lost in the Middle | 中间信息易遗漏现象 |  | 长上下文中，模型对中间位置证据利用不充分的现象。 |
| 25 | Prompt Compression | 提示压缩 |  | 在保留关键任务信息的前提下降低提示长度。 |

## 09. 推理、解码与采样

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Inference | 推理／推断 |  | 在不进行常规参数训练时运行模型得到输出的过程。 |
| 2 | Decoding | 解码 |  | 从模型输出概率分布逐步构造词元序列的过程。 |
| 3 | Greedy Decoding | 贪心解码 |  | 每一步选择当前概率最高的词元。 |
| 4 | Sampling | 随机采样 |  | 按设定概率分布随机选择后续词元。 |
| 5 | Temperature | 温度参数 |  | 调整分布尖锐程度，影响采样随机性。 |
| 6 | Top-k Sampling | Top-k 采样 |  | 每步仅在概率最高的 k 个候选词元内采样。 |
| 7 | Top-p / Nucleus Sampling | Top-p／核采样 |  | 在累计概率达到阈值 p 的最小候选集合中采样。 |
| 8 | Min-p Sampling | Min-p 采样 |  | 按相对于最高概率的比例阈值过滤候选词元。 |
| 9 | Beam Search | 束搜索 |  | 每一步保留若干高分序列候选继续扩展。 |
| 10 | Beam Width | 束宽度 |  | 束搜索中并行保留的候选序列数量。 |
| 11 | Repetition Penalty | 重复惩罚 |  | 对已出现词元施加分数修正以降低重复。 |
| 12 | Frequency Penalty | 频率惩罚 |  | 根据词元已出现次数调节再次生成的倾向。 |
| 13 | Presence Penalty | 出现惩罚 |  | 根据词元是否出现过调整生成倾向。 |
| 14 | Maximum Output Tokens | 最大输出词元数 |  | 一次响应允许生成的词元上限。 |
| 15 | Log Probability (Logprob) | 对数概率 | Logprob | 模型对某词元或序列赋予的概率取对数。 |
| 16 | Token Probability | 词元概率 |  | 模型在特定上下文对候选词元给出的条件概率。 |
| 17 | Entropy | 信息熵 |  | 衡量模型预测分布不确定性的统计量。 |
| 18 | Perplexity (PPL) | 困惑度 | PPL | 由平均负对数似然推导的语言建模指标，越低通常越好。 |
| 19 | Test-time Compute | 测试时计算量 |  | 在回答时额外投入的计算预算，如生成更多候选或搜索。 |
| 20 | Test-time Scaling | 测试时扩展 |  | 通过增加推理阶段计算资源改善问题求解表现。 |
| 21 | Reasoning Trace | 推理轨迹 |  | 推理过程中的步骤表示或记录，未必完整可见。 |
| 22 | Chain-of-Thought (CoT) | 思维链 | CoT | 包含中间推理步骤的文本或内部表示序列。 |
| 23 | Verifier | 验证器 |  | 检查候选答案、代码或推理步骤是否满足约束的组件。 |
| 24 | Self-Refinement | 自我改进／自我修订 |  | 模型根据反馈对初稿进行检查与修改的迭代过程。 |
| 25 | Speculative Decoding | 推测解码 |  | 先由草稿模型提议词元，再由目标模型验证以提速。 |
| 26 | Draft Model | 草稿模型 |  | 推测解码中低成本提出候选词元的模型。 |

## 10. 模型推理加速与服务

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Model Serving | 模型服务 |  | 将模型部署为可接收请求并返回结果的线上系统。 |
| 2 | Inference Engine | 推理引擎 |  | 负责模型加载、调度、执行和生成的运行时系统。 |
| 3 | Prefill | 预填充阶段 |  | 一次性处理输入提示，建立注意力缓存的推理阶段。 |
| 4 | Decode Phase | 逐词元解码阶段 |  | 基于既有缓存逐步生成输出词元的推理阶段。 |
| 5 | Key-Value Cache (KV Cache) | 键值缓存 |  | 保存历史位置注意力 K/V 状态以避免重复计算。 |
| 6 | Prefix Caching | 前缀缓存 |  | 复用共享提示前缀的已计算状态以降低重复预填充。 |
| 7 | PagedAttention | 分页注意力 |  | 以分页式存储管理 KV 缓存，减少内存浪费的机制。 |
| 8 | FlashAttention | 闪存注意力 |  | 通过 I/O 感知的分块计算提高精确注意力效率。 |
| 9 | Dynamic Batching | 动态批处理 |  | 将不同时刻到达的请求动态组合成批次。 |
| 10 | Chunked Prefill | 分块预填充 |  | 将长提示的预填充拆成较小任务以便调度。 |
| 11 | Disaggregated Prefill / Decode | 预填充—解码分离 |  | 将两个推理阶段分配到不同资源或服务。 |
| 12 | Quantization | 量化 |  | 以较低位宽表示权重或激活等数值以减少资源需求。 |
| 13 | Post-training Quantization (PTQ) | 训练后量化 | PTQ | 在训练完成后对模型数值进行量化。 |
| 14 | Quantization-aware Training (QAT) | 量化感知训练 | QAT | 在训练中模拟或考虑量化误差以保持性能。 |
| 15 | Weight-only Quantization | 仅权重量化 |  | 仅降低权重精度，激活保持其他数值格式。 |
| 16 | Activation Quantization | 激活量化 |  | 降低中间激活值所用位宽的量化方式。 |
| 17 | FP32 / FP16 / BF16 | 单精度／半精度／脑浮点 |  | 常见数值格式；BF16 指 bfloat16，动态范围与 FP16 不同。 |
| 18 | FP8 | 8 位浮点 |  | 为训练或推理加速使用的一类低精度浮点表示。 |
| 19 | INT8 / INT4 | 8 位／4 位整数 |  | 权重或激活量化中使用的低位宽整数格式。 |
| 20 | GGUF | GGUF 模型文件格式 |  | 常用于 llama.cpp 生态的模型权重与元数据容器格式。 |
| 21 | GPTQ | GPTQ 量化 |  | 通过训练后权重误差补偿进行低比特量化的方法。 |
| 22 | AWQ (Activation-aware Weight Quantization) | 激活感知权重量化 |  | 基于激活重要性保护关键权重的量化方法。 |
| 23 | Throughput | 吞吐量 |  | 单位时间系统处理的请求或生成的词元数量。 |
| 24 | Tokens per Second (TPS) | 每秒词元数 | TPS | 常见生成速度指标，须注明单请求还是系统总计。 |
| 25 | Time to First Token (TTFT) | 首词元延迟 | TTFT | 从请求发出到收到首个输出词元的时间。 |
| 26 | Time per Output Token (TPOT) | 单输出词元耗时 | TPOT | 输出生成阶段平均每个词元的耗时。 |
| 27 | Inter-token Latency (ITL) | 词元间延迟 | ITL | 相邻输出词元之间的时间间隔。 |
| 28 | End-to-End Latency | 端到端延迟 |  | 从请求开始到完整结果返回的总耗时。 |
| 29 | Requests per Second (RPS) | 每秒请求数 | RPS | 单位时间完成或处理的请求数量。 |
| 30 | Peak GPU Memory | GPU 显存峰值 |  | 执行期间设备所需的最大显存容量。 |
| 31 | Out of Memory (OOM) | 内存／显存不足 | OOM | 运行所需内存超过可用容量导致的错误。 |
| 32 | Kernel Fusion | 算子融合 |  | 合并多个 GPU 算子以降低访存及调度开销。 |
| 33 | CUDA Graph | CUDA 图 |  | 将 GPU 执行操作捕获为可重复启动的图以降低开销。 |

## 11. 检索增强生成与知识库

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Retrieval-Augmented Generation (RAG) | 检索增强生成 | RAG | 检索外部知识作为上下文，辅助模型生成回答的方法。 |
| 2 | Knowledge Base | 知识库 |  | 存储可供查询、检索和引用的业务或领域知识。 |
| 3 | Document Parsing | 文档解析 |  | 从 PDF、HTML 等文件提取结构化文本与元信息。 |
| 4 | Document Chunking | 文档切块 |  | 将长文档拆为便于嵌入、检索和组合的片段。 |
| 5 | Chunk Size | 块大小 |  | 单个检索片段包含的词元、字符或其他长度规模。 |
| 6 | Chunk Overlap | 块重叠 |  | 相邻片段之间保留的共享内容范围。 |
| 7 | Metadata | 元数据 |  | 描述文档来源、标题、时间、权限等附加字段。 |
| 8 | Embedding Model | 嵌入模型 |  | 将文本或其他对象编码为可检索向量的模型。 |
| 9 | Dense Retrieval | 稠密检索 |  | 利用连续向量表示计算查询与文档的相似性。 |
| 10 | Sparse Retrieval | 稀疏检索 |  | 使用稀疏特征，如词项权重进行匹配的检索方法。 |
| 11 | BM25 | BM25 排序算法 |  | 基于词频、逆文档频率与长度归一化的经典检索方法。 |
| 12 | TF-IDF | 词频—逆文档频率 |  | 用词在文档与语料中的分布衡量词项重要性。 |
| 13 | Vector Database | 向量数据库 |  | 支持向量索引、近邻查询和元数据过滤的数据系统。 |
| 14 | Vector Index | 向量索引 |  | 用于加速相似向量查询的数据结构。 |
| 15 | Approximate Nearest Neighbor (ANN) | 近似最近邻 | ANN | 以一定近似换取高效向量检索的技术。 |
| 16 | Hierarchical Navigable Small World (HNSW) | 分层可导航小世界图 | HNSW | 用于近似近邻搜索的多层图索引结构。 |
| 17 | Inverted File Index (IVF) | 倒排文件索引 | IVF | 通过向量聚类分桶减少检索扫描范围的索引策略。 |
| 18 | Cosine Similarity | 余弦相似度 |  | 计算两个向量方向相近程度的指标。 |
| 19 | Dot Product | 点积 |  | 向量对应元素乘积之和，常用于相似性评分。 |
| 20 | L2 Distance | 欧氏距离 |  | 衡量向量空间中两点直线距离的指标。 |
| 21 | Hybrid Search | 混合检索 |  | 结合词项匹配与向量语义相似性的检索方式。 |
| 22 | Query Rewriting | 查询改写 |  | 将用户问题改写为更适合检索的查询。 |
| 23 | Query Expansion | 查询扩展 |  | 加入近义词、相关术语等提高检索覆盖率。 |
| 24 | Reranker | 重排序模型 |  | 对初步召回的候选重新评分并调整排序的模型。 |
| 25 | Cross-Encoder Reranking | 交叉编码器重排序 |  | 将查询与候选联合编码以评估相关性的重排方法。 |
| 26 | Top-k Retrieval | Top-k 检索 |  | 返回按相关度排序的前 k 个候选文档或片段。 |
| 27 | Recall@k | 前 k 召回率 |  | 衡量前 k 个检索结果覆盖相关文档的比例。 |
| 28 | Precision@k | 前 k 精确率 |  | 衡量前 k 个检索结果中相关文档的占比。 |
| 29 | Grounding | 证据锚定／事实依据 |  | 让模型输出以可核查外部信息为依据。 |
| 30 | Citation | 引用／引文标注 |  | 指向支持某个回答论断的文档或具体证据位置。 |
| 31 | Contextual Retrieval | 上下文化检索 |  | 将片段所属上下文信息加入索引或查询流程。 |
| 32 | Knowledge Graph (KG) | 知识图谱 | KG | 以实体和关系表示知识、支持关系查询与推断。 |
| 33 | Graph RAG | 图结构增强检索生成 |  | 利用实体关系图、社区或图查询为生成提供依据。 |
| 34 | Retrieval Failure | 检索失败 |  | 未找到真正相关证据或召回内容不足的情况。 |

## 12. Agent 与工具使用

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | AI Agent | 人工智能智能体 |  | 能感知上下文、选择行动并推进目标的系统。 |
| 2 | Agentic Workflow | 智能体式工作流 |  | 在多步任务中使用模型决策与工具反馈的流程。 |
| 3 | Tool Calling | 工具调用 |  | 模型生成结构化请求，让应用执行外部工具。 |
| 4 | Function Calling | 函数调用 |  | 调用特定函数或接口的一种结构化工具交互形式。 |
| 5 | Tool Schema | 工具模式定义 |  | 描述工具名称、输入参数和约束的数据结构。 |
| 6 | Tool Result | 工具返回结果 |  | 外部工具执行后反馈给模型的信息。 |
| 7 | Observation | 观察结果 |  | 智能体执行动作后从环境或工具获得的反馈。 |
| 8 | Planner | 规划器 |  | 把目标拆成步骤、子目标或操作序列的组件。 |
| 9 | Executor | 执行器 |  | 根据计划调用工具或完成具体操作的组件。 |
| 10 | Reflection | 反思／复核 |  | 对先前动作、答案或证据进行自评与修正。 |
| 11 | State Machine | 状态机 |  | 用有限状态及转移条件控制工作流的机制。 |
| 12 | Model Context Protocol (MCP) | 模型上下文协议 | MCP | 为 AI 应用连接工具和上下文来源定义的标准化协议。 |
| 13 | MCP Server | MCP 服务器 |  | 向客户端暴露工具、资源等能力的协议端。 |
| 14 | MCP Client | MCP 客户端 |  | 与 MCP 服务器建立连接并调用其能力的组件。 |
| 15 | MCP Tool | MCP 工具 |  | 可由模型相关应用调用、带有参数模式的操作。 |
| 16 | MCP Resource | MCP 资源 |  | 通过协议访问的数据或上下文内容。 |
| 17 | MCP Prompt | MCP 提示模板 |  | 由服务器提供、供客户端使用的可复用提示模板。 |
| 18 | Human-in-the-Loop (HITL) | 人在回路 | HITL | 将人工审核、决策或授权引入自动化流程。 |
| 19 | Approval Gate | 审批关口 |  | 执行高风险或不可逆操作前要求授权的节点。 |
| 20 | Multi-agent System | 多智能体系统 |  | 多个专用智能体通过协作或协调完成任务。 |
| 21 | Handoff | 任务移交 |  | 把控制权或任务上下文转给另一智能体或模块。 |
| 22 | Agent Memory | 智能体记忆 |  | 为跨步骤或跨会话保留可复用信息的机制。 |
| 23 | Short-term Memory | 短期记忆 |  | 当前任务或会话中的临时上下文状态。 |
| 24 | Long-term Memory | 长期记忆 |  | 在后续任务中可再次使用的持久信息。 |
| 25 | Sandbox | 沙箱环境 |  | 隔离工具执行、限制资源与权限的运行环境。 |

## 13. 多模态大模型

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Modality | 模态 |  | 信息的表现形式，例如文本、图像、音频或视频。 |
| 2 | Multimodal Model | 多模态模型 |  | 能够联合处理不止一种输入或输出模态的模型。 |
| 3 | Vision-Language Model (VLM) | 视觉语言模型 | VLM | 联合处理视觉与语言内容的模型。 |
| 4 | Vision Encoder | 视觉编码器 |  | 把图像或视频转换为模型特征表示的组件。 |
| 5 | Vision Transformer (ViT) | 视觉 Transformer | ViT | 以 Transformer 为骨干处理图像的架构。 |
| 6 | Patch Embedding | 图像块嵌入 |  | 将图像分块映射为可供 Transformer 处理的向量。 |
| 7 | Cross-modal Alignment | 跨模态对齐 |  | 把不同模态内容映射到可关联的表示或任务空间。 |
| 8 | Contrastive Learning | 对比学习 |  | 拉近正样本、推远负样本表示的训练方法。 |
| 9 | Contrastive Language–Image Pretraining (CLIP) | 对比语言—图像预训练 | CLIP | 利用图像文本配对进行跨模态对比学习的模型范式。 |
| 10 | Optical Character Recognition (OCR) | 光学字符识别 | OCR | 从图片、扫描件中识别字符和文本。 |
| 11 | Visual Question Answering (VQA) | 视觉问答 | VQA | 根据图像信息回答自然语言问题。 |
| 12 | Image Captioning | 图像描述生成 |  | 为图像自动生成文本描述的任务。 |
| 13 | Automatic Speech Recognition (ASR) | 自动语音识别 | ASR | 将语音信号转写为文字的技术。 |
| 14 | Text-to-Speech (TTS) | 文本转语音 | TTS | 根据文本合成语音音频的技术。 |
| 15 | Speech-to-Text (STT) | 语音转文本 | STT | 与语音识别高度相关的通用任务名称。 |
| 16 | Speech Synthesis | 语音合成 |  | 生成人工语音波形或声学表示的过程。 |
| 17 | Audio Token | 音频词元 |  | 音频被离散或连续编码后供模型处理的表示单位。 |
| 18 | Speech Tokenizer | 语音分词器／编码器 |  | 将语音信号转化为模型可处理表示的模块。 |
| 19 | Video Understanding | 视频理解 |  | 对视频中的视觉内容、时序和事件进行建模。 |
| 20 | Frame Sampling | 视频帧采样 |  | 从视频中按规则抽取帧进行编码或分析。 |
| 21 | Temporal Modeling | 时序建模 |  | 利用时间顺序与动态变化理解序列信息。 |
| 22 | Unified Multimodal Model | 统一多模态模型 |  | 在共享框架中联合完成多种模态任务的模型。 |

## 14. 评测与基准

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Benchmark | 评测基准 |  | 包含数据、任务、规则和指标的标准化测试集合。 |
| 2 | Evaluation (Eval) | 模型评测 | Eval | 系统测量模型质量、能力、可靠性或成本的过程。 |
| 3 | Evaluation Harness | 评测框架 |  | 批量执行题目、评分与汇总结果的软件系统。 |
| 4 | Leaderboard | 排行榜 |  | 根据规定评测指标展示模型相对表现的列表。 |
| 5 | Out-of-distribution (OOD) | 分布外数据 | OOD | 偏离训练分布的数据或使用情形。 |
| 6 | Generalization | 泛化能力 |  | 模型在未见过的新样本或任务上表现的能力。 |
| 7 | Overfitting | 过拟合 |  | 模型过度适应训练样本而损害新数据表现。 |
| 8 | Underfitting | 欠拟合 |  | 模型复杂度或训练不足，无法充分拟合数据规律。 |
| 9 | Accuracy | 准确率 |  | 预测正确样本占总样本的比例，需明确题型与评分方式。 |
| 10 | Precision | 查准率／精确率 |  | 预测为正的样本中真正为正的比例。 |
| 11 | Recall | 查全率／召回率 |  | 所有真实正例中被正确识别的比例。 |
| 12 | F1 Score | F1 分数 |  | 精确率与召回率的调和平均数。 |
| 13 | Exact Match (EM) | 完全匹配率 | EM | 预测输出与标准答案按规则完全一致的比例。 |
| 14 | Bilingual Evaluation Understudy (BLEU) | BLEU 机器翻译指标 | BLEU | 根据 n 元片段重合度等评价候选译文的指标。 |
| 15 | Recall-Oriented Understudy for Gisting Evaluation (ROUGE) | ROUGE 文本重合指标 | ROUGE | 常用于文本摘要等任务的 n 元片段重合评价。 |
| 16 | BERTScore | BERTScore 语义相似评 |  | 使用上下文表示计算生成文本与参考文本的相似性。 |
| 17 | Pass@k | 前 k 次通过率 |  | 在 k 次采样中至少一个程序通过测试的估计指标。 |
| 18 | Win Rate | 胜率 |  | 在两两比较中某模型或方案获得偏好胜出的比例。 |
| 19 | Pairwise Evaluation | 成对比较评测 |  | 让评审比较两个候选输出质量的评估方式。 |
| 20 | LLM-as-a-Judge | 大模型裁判 |  | 使用另一个语言模型对输出进行自动评判的方法。 |
| 21 | Human Evaluation | 人工评测 |  | 由人类标注者或专家对结果质量进行评判。 |
| 22 | Inter-annotator Agreement | 标注者一致性 |  | 不同人工评估者对同一对象判断相符的程度。 |
| 23 | Calibration | 置信校准 |  | 模型声明的置信水平与真实正确率之间的一致程度。 |
| 24 | Groundedness | 依据性／证据一致性 |  | 答案是否受到给定证据支持的评价维度。 |
| 25 | Faithfulness | 忠实性 |  | 生成内容是否忠于给定来源或推理依据的性质。 |
| 26 | Factuality | 事实正确性 |  | 回答陈述是否符合可验证外部事实的程度。 |
| 27 | Robustness | 鲁棒性 |  | 模型在扰动、变体或异常条件下保持性能的能力。 |
| 28 | Massive Multitask Language Understanding (MMLU) | 大规模多任务语言理解 | MMLU | 覆盖多个学科知识问答的综合评测数据集。 |
| 29 | Grade School Math 8K (GSM8K) | 小学数学应用题基准 | GSM8K | 由多步骤小学数学文字题组成的测试集。 |
| 30 | MATH Benchmark | 数学问题基准 |  | 覆盖多类数学竞赛或分级难题的评测集。 |
| 31 | HumanEval | 代码生成评测集 |  | 使用函数级编程题与单元测试评估代码生成。 |
| 32 | SWE-bench | 软件工程任务基准 |  | 基于真实代码仓库问题的补丁修复能力评测。 |

## 15. 安全、对齐与可信性

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Hallucination | 幻觉 |  | 模型生成缺乏依据、虚构或错误的信息。 |
| 2 | Factual Error | 事实性错误 |  | 输出与可验证事实不一致的错误。 |
| 3 | Confabulation | 编造式回答 |  | 在缺乏可靠依据时生成看似合理的虚构叙述。 |
| 4 | Uncertainty Estimation | 不确定性估计 |  | 评估模型预测或回答可信程度的方法。 |
| 5 | Abstention | 拒答／弃答 |  | 在证据不足或风险较高时选择不作实质回答。 |
| 6 | Refusal | 拒绝响应 |  | 因安全规则或其他约束不执行特定请求。 |
| 7 | Safety Alignment | 安全对齐 |  | 使模型输出符合既定安全规范和风险限制。 |
| 8 | Guardrail | 安全护栏 |  | 对输入、工具行为或输出施加约束的保护措施。 |
| 9 | Content Moderation | 内容审核 |  | 识别并处理违规或高风险文本与多媒体内容。 |
| 10 | Prompt Injection | 提示注入攻击 |  | 通过恶意输入诱导模型偏离应遵循的指令。 |
| 11 | Indirect Prompt Injection | 间接提示注入 |  | 将恶意指令藏在网页、文档或工具结果等外部内容中。 |
| 12 | Jailbreak | 越狱提示 |  | 试图绕开模型既有限制或安全控制的输入策略。 |
| 13 | Data Poisoning | 数据投毒 |  | 通过篡改训练、微调或检索数据影响模型行为。 |
| 14 | Backdoor Attack | 后门攻击 |  | 植入特定触发条件下才显现的恶意行为。 |
| 15 | Model Extraction | 模型提取 |  | 通过查询或访问复制模型行为或参数的攻击。 |
| 16 | Model Inversion | 模型反演 |  | 从模型输出或参数推断训练数据特征的攻击。 |
| 17 | Membership Inference | 成员推断攻击 |  | 推断某条数据是否参与过模型训练的攻击。 |
| 18 | Sensitive Information Disclosure | 敏感信息泄露 |  | 无授权披露私人、机密或受保护数据的风险。 |
| 19 | Least Privilege | 最小权限原则 |  | 只向系统或工具授予完成任务所必需的权限。 |
| 20 | Privilege Escalation | 权限提升 |  | 越过原有授权边界获取更高权限的行为。 |
| 21 | Excessive Agency | 过度代理权限 |  | 模型工具权限、自治程度或操作范围过大带来的风险。 |
| 22 | Output Validation | 输出验证 |  | 在使用模型结果前检查格式、内容及安全约束。 |
| 23 | Red Teaming | 红队测试 |  | 主动模拟攻击与边界情形发现系统弱点的评测方法。 |
| 24 | Adversarial Example | 对抗样本 |  | 经精心构造、旨在诱发模型错误或异常行为的输入。 |
| 25 | Adversarial Robustness | 对抗鲁棒性 |  | 系统面对恶意或故意扰动时维持正确行为的能力。 |
| 26 | Algorithmic Bias | 算法偏差／偏见 |  | 数据或模型在结果上体现的不合理系统性倾向。 |
| 27 | Fairness | 公平性 |  | 模型对不同人群或情形产生结果时的公正性要求。 |
| 28 | Explainability | 可解释性 |  | 使人能理解模型输出依据或行为因素的程度。 |
| 29 | Audit Trail | 审计轨迹 |  | 可追溯记录数据、模型、操作和决策过程的证据链。 |

## 16. LLMOps 与部署工程

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | LLMOps | 大模型运维工程 |  | 围绕大模型开发、部署、监测、评测与治理的工程实践。 |
| 2 | Model Registry | 模型注册表 |  | 记录模型版本、元数据、状态和发布信息的系统。 |
| 3 | Model Versioning | 模型版本管理 |  | 对模型权重、配置及发布状态进行可追溯管理。 |
| 4 | API (Application Programming Interface) | 应用程序编程接口 |  | 不同软件组件交互的程序化调用边界。 |
| 5 | Endpoint | 服务端点 |  | 客户端发起模型请求的具体接口地址或入口。 |
| 6 | Streaming Response | 流式响应 |  | 生成过程中分批发送增量内容而非一次性返回。 |
| 7 | Server-Sent Events (SSE) | 服务器发送事件 | SSE | 服务器通过 HTTP 单向推送事件的常见流式机制。 |
| 8 | Rate Limit | 速率限制 |  | 控制单位时间请求数、词元数等资源消耗的规则。 |
| 9 | Timeout | 超时 |  | 等待操作完成所允许的最大持续时间。 |
| 10 | Retry with Backoff | 退避重试 |  | 请求失败后逐步增加等待间隔再次尝试的策略。 |
| 11 | Idempotency | 幂等性 |  | 重复执行同一操作不改变其额外业务效果的性质。 |
| 12 | Observability | 可观测性 |  | 通过日志、指标、追踪理解系统内部运行状态。 |
| 13 | Tracing | 调用链追踪 |  | 记录跨模型、检索和工具步骤的执行链路。 |
| 14 | Telemetry | 遥测数据 |  | 运行时自动收集的性能、错误与使用统计信息。 |
| 15 | Service Level Objective (SLO) | 服务等级目标 | SLO | 对可用性、时延等服务质量设定的可测目标。 |
| 16 | A/B Testing | A/B 测试 |  | 并行比较不同模型、提示或流程效果的实验方法。 |
| 17 | Canary Deployment | 金丝雀发布 |  | 先向少量流量发布新版本并观察风险的策略。 |
| 18 | Regression Testing | 回归测试 |  | 修改后复测既有能力，检查是否出现质量退化。 |
| 19 | Cost per Token | 每词元成本 |  | 按输入或输出词元计算的计费或内部资源成本。 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/large-language-models.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
