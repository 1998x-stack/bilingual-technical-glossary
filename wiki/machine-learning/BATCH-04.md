# Machine Learning · Batch 04 学习路径（076–100）

> 唯一权威词序是 [机器学习术语表](../../glossaries/machine-learning.md)。此为仓库内部编辑与同行复核资料；公开页面仍只通过统一 Explorer → term.html 查看，不新增独立 /wiki 首页。

## 第一模块（076–082）：模型输入、数据增强与复现流水线

**Embedding** 是在目标函数下学习的向量表征，不等于词袋；**Sparse Feature**、**Dense Feature** 描述非零密度和存储形态，不天然是语义质量的区别；**Data Augmentation** 必须在按实体拆分后仅用于训练；**Resampling** 包含 Bootstrap、过/欠采样，不产生新的独立统计单位；**SMOTE** 采用邻近少数类插值，只能在训练折内执行并检查混合类别和可行性约束；**Pipeline** 保存可复现的 train/transform/predict 契约，但不能解决原始事件时间的后验泄漏。

## 第二模块（083–091）：泛化目标与失败模式

- **Empirical Risk**：训练损失平均 Rhat；**Expected Risk**：目标分布上期望 R；二者不同。
- **ERM** 在固定 H 内最小化训练损失；**SRM** 在多个复杂度模型类之间考虑泛化惩罚，理论上依赖分布及界的假设。
- **Generalization** 指目标未见数据上有效，**Generalization Gap** 需明确是 loss 还是 accuracy 口径。
- **Overfitting** 训练好、未知数据差；**Underfitting** 训练也差；避免混同数据泄漏、分布漂移、优化失败。
- **Bias–Variance** 对平方损失有具体恒等式：Bias²+Variance+Noise；其他损失或复杂模型不照搬。

## 第三模块（092–100）：从正则化到理论可学性

- **Inductive Bias** 是从有限样本向未见点推广所采用的结构偏好，不等于统计 Bias 数值。
- **Regularization / L1 / L2 / Elastic Net**：比较优化目标中对样本量、1/2 因子、截距和标准化方式的定义。L1 用 soft-threshold 可达精确零；L2 常连续收缩；Elastic Net 采用比例权重组合。
- **Model Complexity** 与 **Capacity** 是相关但不相同的概念，单凭参数数目无法推断部署风险。
- **VC Dimension** 是可打散点数的最大值。实数定向阈值 VC=1、区间 VC=2、仿射 R^d 半空间在通常条件下 VC=d+1。明确存在一组点的逻辑量词。
- **PAC Learning** 的概率是在随机训练集上，而不是说每条预测以 (1−δ) 的概率正确。有限类可实现情形下，联合界可导出 n≥(ln|H|+ln(1/δ))/ε 的**充分**样本量；不可随意用于非 IID 部署或不可实现模型。

## 跨术语复核案例：新设备故障检测

制造商使用设备嵌入表示、高基数故障码与连续传感器记录。首先按设备和时间切分，训练折内以 imbalanced-learn Pipeline 做缺失值处理、特征缩放及 SMOTE；未知设备应有 OOV 或内容编码。比较正则化线性基线和深模型的训练/验证风险，评估未来机器群的 PR-AUC、成本以及置信区间；L1/Elastic Net 选特征但不承诺因果解释；理论 VC/PAC 仅解释在受限函数类、样本独立与损失边界条件下的可学性，不代替真实世界外部验证。

## 审校重点与证据

1. 逐条查证每篇的原始论文或维护者官方文档，特别是 SMOTE、Mikolov word embedding、Valiant PAC、Vapnik–Chervonenkis 一致收敛和 Elastic Net 原文。
2. 独立重算新增 **50 道中等考试题**与 **50 道中等面试问答**，检查 log/ceil 四舍五入、Ridge/Lasso 目标归一化差别、VC 打散的存在量词。
3. 机读自动验收仅证明目录、编号、镜像、结构及部分数学算例符合预期；机器学习领域 **100 篇**仍待真实专家复核，台账全部 pending，不伪造签名。
