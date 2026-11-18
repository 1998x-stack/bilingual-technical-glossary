# Machine Learning · Batch 07 学习路径（151–175）

> 本文属于内部知识路径与人工审稿文档，正式网站依然通过 [统一 Explorer](https://1998x-stack.github.io/bilingual-technical-glossary/?category=machine-learning#explorer) → term.html，不添加 /wiki 专用网页。术语序号、中文译名依赖 [权威术语词表](../../glossaries/machine-learning.md)。

## 主线一：GBDT 产业实现、组合与重要性（151–157）

- **XGBoost** 的增益与叶权重来自正则化目标的二阶泰勒展开。固定树结构时，w* = −G/(H+λ)，γ 惩罚叶数；不能将 gain 排名误当因果效应。
- **LightGBM** 用直方图候选分裂与 leaf-wise 生长，需控制 num_leaves、min_data_in_leaf、max_depth；GOSS、EFB 是其重要研究技术，但**不保证每次训练配置都启用**。
- **CatBoost** 使用 ordered categorical statistics 与 ordered boosting 的理论机制抑制目标泄漏；参数 boosting_type 实际可为 Ordered 或 Plain，默认受硬件、样本数和任务影响，不可笼统说所有 CatBoost 都使用 Ordered。
- **Stacking** 的元学习器必须使用恰当的 out-of-fold 基模型预测；直接用基模型自身训练集预测训练元模型会造成信息泄漏。**Voting Ensemble** 使用固定 hard / soft 投票而不训练新的融合模型，soft voting 需要对齐类别及校准。
- **OOB** 以每棵 Bootstrap 未抽中的样本做内部评估，固定行 OOB 概率约 36.8%，但与新设备、新用户和未来时间外部测试不同。
- **Feature Importance** 需说明 MDI、Permutation、SHAP 各自的测量定义及相关特征和高基数偏差，不能被视为因果特征排名。

## 主线二：SVM、margin 与核空间（158–169）

- **SVM** 硬/软间隔形式化为 min 0.5||w||²+CΣξ；强制 y_if(x_i)≥1−ξ_i 且 ξ_i≥0。**Support Vector** 是 α_i>0 的样本，可能落在间隔内或被误分类，非仅在边界。
- **Margin** 要区分功能间隔 y_i f_i 与几何间隔 y_i f_i / ||w||；hard-margin 规范间隔超平面宽度为 2/||w||。**Hinge Loss** 为 max(0,1−yf)，正确但落在间隔内的样本仍有损失。C 增大对违反间隔的惩罚更强，并不保证泛化更好。
- **Kernel Trick** 以 K(x,z)=⟨φ(x),φ(z)⟩替代显式高维内积；需要理解 kernel Gram 对称半正定。n 条数据的完整 float64 Gram 基础存储为 8n² 字节，核并不是无成本的高维计算捷径。
- **Linear Kernel** K=xᵀz；**Polynomial Kernel** K=(γxᵀz+r)^d；**RBF** K=exp(−γ||x−z||²)，γ=1/(2σ²)。在同一训练折内标准化，比较 C、gamma、degree、coef0 与真实外部测试。
- **SVR** 用 ε-insensitive loss max(0,|y−f|−ε) 和相应 ε 管；ε 不是概率区间覆盖的保证。

## 主线三：KNN、搜索与度量（170–175）

- **KNN** 是按邻居投票/回归的学习规则；**Nearest Neighbor Search** 是返回索引和距离的检索运算，可用 brute、KDTree、BallTree 或 ANN；大维度下 KDTree 未必有优势。
- **Distance Metric** 需满足非负、同一性、对称与三角不等式；**Euclidean** 为 L2、**Manhattan** 为 L1，输入量纲会影响邻居排序。
- **Cosine Similarity** 为向量方向归一化内积，零向量数学上无定义，软件实现可能有特殊约定；**1−cosine 一般不是严格 metric**。对单位 L2 向量，||x−z||²=2−2cos(x,z)，因此 cosine 排序与欧氏距离排序一致。

## 复合工程案例：跨医院病例检索与风险评分

1. 在按病人、医院和时间切分的数据上建立 Logistic、XGBoost、LightGBM、CatBoost 与线性/RBF SVM 基线。类别目标统计、标准化以及任何特征筛选必须在训练折内部拟合。
2. 比较单模型预测校准、PR-AUC 与误报/漏报成本，再用合法 OOF 的 Stacking 与投票集成对照，不以训练集分数评价融合收益。
3. 通过 Permutation Importance、背景分布明确的 SHAP 等解释模型，但不得直接得出医疗因果结论或用结果替代公平/合规审查。
4. 对病历相似病例检索分别实验归一化 Cosine、Euclidean、Manhattan，建立精确 top-k 基准，再测 ANN Recall@k、P95 延迟、索引新鲜度和访问权限正确性。
5. 生产上同时版本化模型、向量、特征尺度、类别字典、核参数、概率校准与阈值；随病例变化监控漂移和 OOD 样本。

## 专项审校与证据台账

本批 25 篇每篇含两道中等难度面试问答、两道中等难度考试题及完整解析，新增各 50 题。重点重算 XGBoost w*=−G/(H+λ)、ordered CTR、投票加权概率、核函数与 Gram PSD 反例、软间隔/hinge、SVR ε 管、Cosine/Euclidean 排序关系和近邻 Recall@k。自动化验证仅检查结构、镜像和部分可复算题，175 篇专业人工审稿仍保持 pending，不伪造人工签核。
