# Machine Learning · 第三批学习路径（051–075）

> 内部教学与编辑资料；不在公开网站中创建独立 Wiki 首页或批次入口。权威词序为 [机器学习词表](../../glossaries/machine-learning.md)。

## 主线 1：数据可信度（051–054）

- **Outlier vs Missing Value：**离群是偏离所定义的参考分布；缺失是没有观测。极端欺诈交易不可一律删除。
- **Data Annotation：**写清类别定义、标注指南、审核者分歧和真值来源。Cohen κ 衡量一致性，不是直接的真实性证明。
- **Data Cleaning / Data Preprocessing：**前者处理错误与不一致，后者还包含编码、数值变换等模型输入准备。清洗必须记录变更与可逆的来源依据。

## 主线 2：构造可靠特征（055–058）

Feature Engineering 是总设计活动；Feature Extraction 是从原始输入计算表示，Feature Selection 只选择已有特征；Imputation 填补缺失。所有需要学习数据统计量的步骤必须 **在交叉验证每个训练折内部拟合**，不让测试数据参与参数估计。

## 主线 3：数值尺度（059–063）

- Mean Imputation：均值仅来自训练中非缺失值；不能恢复真实误差分布。
- Standardization：训练列均值与标准差的 z-score。与样本行 L2 归一化不同。
- Normalization：明确是否表示 L1/L2 样本级归一化；遇零向量需处理。
- Min–Max Scaling：使用训练极值；上线新值**可能超过 1 或小于 0**。
- Robust Scaling：训练中位数与 IQR，抵抗极值对参数的影响但**不裁剪异常观测**。

## 主线 4：类别编码及泄漏（064–068）

One-hot 保留无序类别的独立指示位；Ordinal Encoding 可能引入人为大小/距离；Target Encoding 使用训练目标统计量，必须做 OOF cross-fitting 或正确的历史截断与平滑，防止 label leakage；Label Encoding 通常用于监督目标 y；Binning 将连续输入变为离散区间，需量化边界处的信息损失。

## 主线 5：非线性与文本特征（069–075）

多项式展开增加模型函数容量，交互项表达条件联合作用；LogTransformation 和 Box–Cox 的定义域不同（后者要求 x>0）；Feature Hashing 固定维但可能桶碰撞；Bag of Words 仅记录计数而不保词序；TF–IDF 通过训练语料的 IDF 加权，**公式约定需要与 scikit-learn 的平滑 IDF 区分**。

## 综合工程案例：电商欺诈的可复现特征 Pipeline

1. 定义预测时点为用户下单当刻，保存交易 ID、客户 ID、业务时间、币种、交易类型；标注审核事件只能来自合法的成熟标签。
2. 按客户及后续时间窗口建立独立验证与最终测试；检测重复订单、币种异常、未来退款字段和跨用户关联。
3. 数值列分别测试训练折内填补/标准化/稳健缩放；类别列对低基数做 OneHot，对高基数可用严格 OOF TargetEncoder 或固定桶数 Hashing。
4. 原始订单说明可用 Bag of Words/TF–IDF 做低成本语义基线，词表与 IDF 均在训练折拟合，未知词按部署策略处理。
5. 对组合特征（商户×时段、近 24h 交易次数）进行时间回放，要求所有输入在实际预测时刻可获得；以 PR-AUC、漏报/误报成本和分层指标验收。
6. 上线监测缺失率、未见类别、哈希碰撞诊断、数值越界和评分漂移，保存特征转换参数版本及回滚方案。

## 独立专业审稿的关键边界

- 检查 Box–Cox 的 x>0 与 λ=0 极限、TF–IDF 默认平滑公式、StandardScaler 的方差口径、TargetEncoder cross-fitting、KFold 预处理隔离等机制。
- 逐题复算 25 篇共 50 道考试题及 50 道中等面试题答案；查证每个相关的维护者文档及原始论文确实支持所述结论。
- 本阶段不伪造 expert reviewer：新增 25 条 review ledger 为 pending。自动化验收不等于技术事实被人类专家复核。
