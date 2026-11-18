# Machine Learning · Batch 05 学习路径（101–125）

> 内部编辑与技术复核资料。术语顺序严格遵循 [机器学习中英词表](../../glossaries/machine-learning.md)，网站继续沿用统一 Explorer 和 `term.html`，不新增 /wiki 首页。

## 学习主线 A：可靠泛化与部署分布（101–107）

- **Sample Complexity**：PAC 理论中的 n 对误差 ε、置信 δ、假设类 H 的依赖；有限类、可实现性、iid 等都是明确的定理前提。不能把传感器重复行直接当独立样本。
- **Learning Curve vs Validation Curve**：前者横轴为训练样本量，后者横轴为一个模型超参数；可诊断欠拟合/过拟合，但反复调参会消耗验证集独立性。
- **Distribution Shift** 是总称，**Covariate Shift** 指 P(X) 变而 P(Y|X) 不变，**Label Shift** 指 P(Y) 变而 P(X|Y) 不变，**Concept Drift** 通常指预测条件 P(Y|X) 随时间发生变化。
- 针对 Covariate Shift，权重 w(x)=p_t(x)/p_s(x) 要求支持集覆盖；Label Shift 的贝叶斯校正也要重新归一化，且类条件不变需额外核验。

## 学习主线 B：先定义输出任务（108–113）

- Regression 估计连续数值、条件均值或分位数；Classification 输出离散类别或类别概率。
- Binary Classification 需要明确正类、概率校准和成本阈值。
- Multiclass 是互斥 K 类，Softmax 保证各类概率总和为 1。
- Multilabel 每个样本可同时拥有多个标签（K 个标签位），Subset Accuracy 比逐标签准确率更严格。
- Multioutput 可包括多个连续目标或者多个独立分类目标，需要处理单位差异和加权损失。

## 学习主线 C：线性模型与不同的优化原则（114–125）

- **Linear Regression** 对参数线性，**OLS** 是最小化平方残差和的估计法。QR/SVD 通常比直接求逆 XᵀX 更稳健。
- **Ridge** 添加 L2 惩罚，**Lasso** 添加 L1 惩罚并可给出精确零，**Elastic Net** 合并两者。各官方 API 的损失归一化和 α 定义不能混用。
- **Logistic Regression** 是 log-odds 线性化的二分类模型；**Softmax Regression** 是互斥多类推广。
- **GLM** 用指数族、线性预测器和链接函数统一多个响应类型；**Poisson Regression** 处理计数与暴露量；**Quantile Regression** 使用 pinball loss 估计条件分位数；**Robust Regression** 使用 Huber/RANSAC 等减少异常点主导。
- **Decision Boundary** 由阈值及得分决定：二分类 Logistic 阈值 τ 的 logit 边界为 ln(τ/(1−τ))，只有 τ=0.5 时为 0。

## 综合工程案例：跨区域订单量与欺诈审核

1. 同一电商系统需要同时预测日订单数（计数）、未来交付时间的 90% 分位数（连续目标）和是否欺诈（二分类），必须按目标成熟时间定义独立的 y、损失及评价指标。
2. 先按客户、商户和时间窗划分训练、验证与最终测试；保留订单重试关联，避免用户或订单跨集泄漏。
3. 订单量可从 Poisson+暴露量 offset 开始（注意过度离散）；送达时间比较 Linear/Huber/Quantile；欺诈评分用 Logistic，选阈值时明确误报/漏报成本。
4. 当新地区客户组成变化时先判断协变量偏移、标签偏移还是条件概念漂移；有延迟标签时避免仅凭 PSI 判断关系变化。
5. 所有标准化、编码、正则选择都在训练折内执行；按地区和月份追踪 MAE、pinball loss、Precision/Recall、校准和运营成本。

## 专项复核要求

- 每篇 2 道中等面试题与 2 道中等考试题，重点复核 PAC 样本量上整、密度比与后验重权重、Softmax 交叉熵、岭回归正规方程、Huber 损失、分位数 pinball loss 等数理条件。
- 查验每篇来源确实支持所用公式和假设；现有结构/镜像/数学 CI 不能替代领域专家独立签核。
- 第五批 25 条与前四批 100 条共 125 条审稿台账均保持 pending；除非真实领域审稿人以正文哈希和证据记录复核，不得把技术审核表述为完成。
