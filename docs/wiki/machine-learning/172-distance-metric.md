# Distance Metric（距离度量）

> 领域：机器学习 · 专题：支持向量机、核方法与近邻 · 数学、工程实践及邻域检索

## 1. 核心定义

距离度量（Distance Metric）是对对象 x,z 赋予非负距离 d(x,z) 的规则；严格数学意义的 metric 应满足非负性、同一性（d=0 当且仅当相同）、对称性和三角不等式。机器学习工程中很多称为 distance 的分数只是相异度，并不都满足 metric 公理。

## 2. 形象理解

像给地图规划移动成本：直线距离、沿街道走的距离以及只看方向的相似性，回答的是不同‘接近’概念。

**类比的局限：**不同距离会决定哪些样本被称为近邻；若混合了米、秒、货币等量纲且不做合理缩放，几何邻近可能毫无业务意义。

## 3. 技术原理与核心内容

常见 Minkowski 距离 d_p(x,z)=(Σ_j|x_j−z_j|^p)^(1/p)，p≥1 是度量，其中 p=1 为 Manhattan，p=2 为 Euclidean。任意正权重的 Lp 组合在适当定义下也可构成度量；p<1 的这种表达通常不满足三角不等式。Cosine Similarity=内积/范数乘积，1−cos 一般不满足三角不等式，因此不能无条件称标准 metric。Mahalanobis 等需选择正定协方差逆/矩阵并处理数值条件。

## 4. 工程实践与设计权衡

表格近邻检索需对连续数值按训练统计做缩放，对类别字段选择合适编码/混合距离；发布前记录度量名称、参数、归一化与缺失值规则，并在相同度量下比较精确近邻与近似索引。

## 5. 关联知识与易混辨析

Distance Metric 是公理化的距离概念；Euclidean 和 Manhattan 为具体 Minkowski 度量；Cosine 是方向相似分数；RBF Kernel 由平方 L2 距离变换获得核相似度，但不是距离。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么不能把所有“1−相似度”都称为 metric？** 答：减去相似度只能产生一个形式上的差异分数，未必满足非负、同一性和三角不等式，应逐项验证。

2. **问：为什么许多 KNN 应用要在训练集上拟合 StandardScaler？** 答：不同量纲将改变近邻排序，标准化减少无关单位放缩；不能让验证/测试样本影响训练的尺度统计。

## 7. 中等难度考试题（含解析）

1. **题：x=(0,0)、z=(3,4)，Minkowski p=2 的距离？** 解：sqrt(3²+4²)=5。

2. **题：相同两点 Minkowski p=1 的距离？** 解：|3|+|4|=7；两者都是合法度量，但几何邻域不同。

## 8. 权威来源与延伸阅读

- [scikit-learn Distance Metrics 使用参考](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html)：为技术公式与参数行为提供可追溯一手文档。
- [scikit-learn Nearest Neighbors 用户指南](https://scikit-learn.org/stable/modules/neighbors.html)：为技术公式与参数行为提供可追溯一手文档。

> 文中数值为清晰条件下的演算，非生产基准；独立专业审核仍为 pending。
