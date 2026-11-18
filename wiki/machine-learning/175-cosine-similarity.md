# Cosine Similarity（余弦相似度）

> 领域：机器学习 · 专题：支持向量机、核方法与近邻 · 数学、工程实践及邻域检索

## 1. 核心定义

余弦相似度（Cosine Similarity）衡量非零向量之间的夹角余弦，定义 cos(x,z)=xᵀz/(||x||₂||z||₂)，取值在 [−1,1]。它忽略正比例缩放后的向量长度，因此常用于文本向量、Embedding 检索与内容推荐，但不衡量概率和绝对距离。

## 2. 形象理解

像比较两个人都朝向哪个方向行走：即使一个人走得快、另一个走得慢，只要方向相同，余弦相似度仍为 1。

**类比的局限：**若任一向量是零向量，数学定义分母为零；某些软件会以特殊实现返回 0，这只是约定而非原公式的合法计算。

## 3. 技术原理与核心内容

对非零向量 x,z，cos=Σ_jx_jz_j/[sqrt(Σ_jx_j²)sqrt(Σ_jz_j²)]。同向正比例向量 cos=1，正交 cos=0，反向 cos=−1。对单位范数向量，cos(x,z)=xᵀz，且 ||x−z||²=2−2cos，因此最大化 cosine 与最小化单位向量欧氏距离有相同排序。工程常用 d_cos=1−cos 作为差异度，但它一般违反三角不等式，不能无条件称为严格 metric；角距离 arccos(cos) 在单位方向空间具备不同的几何性质。

## 4. 工程实践与设计权衡

文档 RAG 检索需固定 embedding 模型版本、是否 L2 归一化、相似度阈值及近似索引设置；对全零向量、NaN 和异常长度做质量验证。余弦高不保证事实相关或避免隐私/版权风险，仍需用业务标注评估 Recall@k。

## 5. 关联知识与易混辨析

Cosine Similarity 为方向分数而非严格距离；Euclidean/Manhattan 是 metric；Linear Kernel 是未归一化内积；L2 归一化后 sklearn cosine 等于 linear kernel，但原始向量长度信息被舍弃。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么向量 x 和 100x（x 非零、比例为正）的余弦相似度是 1？** 答：两向量方向相同，归一化后相同，长度因子相消；但 100 倍幅值可能代表不同业务含义。

2. **问：为什么 1−cosine 不一定满足 metric 的三角不等式？** 答：非线性角度映射会使两个小的方向差所对应的 1−cos 数值加和小于直接跨越大角度的差，需将其视为相异度而非标准距离。

## 7. 中等难度考试题（含解析）

1. **题：x=(3,4)、z=(6,8)，余弦相似度是多少？** 解：点积 18+32=50，两者范数为 5 与 10，因此 cos=50/(5×10)=1。

2. **题：单位向量 x=(1,0)、z=(0,1)，cosine 及平方欧氏距离各是多少？** 解：cos=0；||x−z||²=(1−0)²+(0−1)²=2，与 2−2cos=2 一致。

## 8. 权威来源与延伸阅读

- [scikit-learn cosine_similarity 官方接口](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)：为技术公式与参数行为提供可追溯一手文档。
- [SciPy cosine distance 官方 API](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html)：为技术公式与参数行为提供可追溯一手文档。

> 文中数值为清晰条件下的演算，非生产基准；独立专业审核仍为 pending。
