# 机器学习 · 深度 Wiki 内部批次路线图

> 唯一权威词序：[机器学习术语原稿](../../glossaries/machine-learning.md) · **447 条 / 19 专题 / 18 批**。本目录供内部编辑与复核，不作为公众独立 Wiki 入口。

每批连续 **25** 条（末批 **22**），保持原始章节、英文名称与中文译名，不按章节重置全局编号。每篇含精准定义与适用边界、形象类比及局限、算法机制、工程实践及失败模式、相邻术语辨析、**2 道中等面试问答 + 2 道中等考试题及推导**、至少两项可追溯一手来源。每批独立 PR；专家审核记为 pending 直至真实审核人签署。

| 批次 | 全局编号 | 覆盖主题 | 术语数 | 生产状态 |
|---|---|---|---:|---|
| 01 | 001–025 | 基础概念与学习范式 / 数据、样本与数据集划分 | 25 | planned |
| 02 | 026–050 | 数据、样本与数据集划分 | 25 | planned |
| 03 | 051–075 | 数据、样本与数据集划分 / 数据预处理与特征工程 | 25 | planned |
| 04 | 076–100 | 数据预处理与特征工程 / 统计学习与泛化理论 | 25 | planned |
| 05 | 101–125 | 统计学习与泛化理论 / 回归、分类与线性模型 | 25 | planned |
| 06 | 126–150 | 回归、分类与线性模型 / 树模型与集成学习 | 25 | planned |
| 07 | 151–175 | 树模型与集成学习 / 支持向量机、核方法与近邻 | 25 | planned |
| 08 | 176–200 | 支持向量机、核方法与近邻 / 概率模型与统计推断 | 25 | planned |
| 09 | 201–225 | 概率模型与统计推断 / 无监督学习与聚类 | 25 | planned |
| 10 | 226–250 | 降维、分解与流形学习 / 优化算法与模型训练 | 25 | planned |
| 11 | 251–275 | 优化算法与模型训练 | 25 | planned |
| 12 | 276–300 | 损失函数与回归评估 / 分类指标与概率校准 | 25 | planned |
| 13 | 301–325 | 分类指标与概率校准 / 调参与模型选择 | 25 | planned |
| 14 | 326–350 | 调参与模型选择 / 时间序列与预测 / 推荐系统与排序学习 | 25 | planned |
| 15 | 351–375 | 推荐系统与排序学习 / 深度学习相关核心术语 | 25 | planned |
| 16 | 376–400 | 深度学习相关核心术语 / 机器学习工程与生产部署 | 25 | planned |
| 17 | 401–425 | 机器学习工程与生产部署 / 可解释性、公平性与安全 | 25 | planned |
| 18 | 426–447 | 可解释性、公平性与安全 | 22 | planned |

## 来源、发布与验证

- 源稿：`wiki/machine-learning/<NNN>-<slug>.md`；Pages 镜像：`docs/wiki/machine-learning/`（逐字节相同）。
- 元数据：本目录 `batches.json`、`docs/wiki/machine-learning/manifest.json`、`wiki/reviews/machine-learning.json`；网站统一 `docs/data/wiki-index.json`。
- 公共入口仍为 [Explorer](https://1998x-stack.github.io/bilingual-technical-glossary/?category=machine-learning#explorer) → 术语详情，不暴露批次计划。
- `python3 scripts/build_wiki_index.py --check`、`python3 scripts/verify_wiki_reviews.py --check`、整库测试、Chromium E2E；审稿和 CI 分开记录。

## 第一批 001–025

覆盖“基础概念与学习范式”24 条，以及第二个专题“数据、样本与数据集划分”第 1 条 **Dataset**。不要误将第二章局部编号 1 当作全局编号 1。

1. Machine Learning (ML)（机器学习）
2. Artificial Intelligence (AI)（人工智能）
3. Statistical Learning（统计学习）
4. Supervised Learning（监督学习）
5. Unsupervised Learning（无监督学习）
6. Semi-supervised Learning（半监督学习）
7. Self-supervised Learning（自监督学习）
8. Reinforcement Learning (RL)（强化学习）
9. Online Learning（在线学习）
10. Offline Learning / Batch Learning（离线学习／批量学习）
11. Active Learning（主动学习）
12. Transfer Learning（迁移学习）
13. Multi-task Learning（多任务学习）
14. Meta-learning（元学习）
15. Few-shot Learning（少样本学习）
16. Zero-shot Learning（零样本学习）
17. Domain Adaptation（领域自适应）
18. Inductive Learning（归纳学习）
19. Transductive Learning（直推学习）
20. Generative Model（生成模型）
21. Discriminative Model（判别模型）
22. Predictive Modeling（预测建模）
23. Representation Learning（表征学习）
24. Foundation Model（基础模型）
25. Dataset（数据集）
