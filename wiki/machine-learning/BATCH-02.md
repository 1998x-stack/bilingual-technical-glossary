# Machine Learning · 第二批学习路径（026–050）

> 内部编辑资料，不在公共 Explorer 暴露批次信息。词表顺序参见 [原始中英术语表](../../glossaries/machine-learning.md)。

## 学习地图

1. **026–032 观测、学习单位与特征契约：** Sample、Observation、Feature、Target/Label、Ground Truth、X 和 y。需要把“模型预测单位”与“数据统计独立单位”分开理解；同时掌握数据采集、标签成熟时点以及矩阵行列对齐。
2. **033–037 训练、开发与保留测试：** Training、Validation、Test、Holdout 与 Train–Test Split。超参不能用测试集选择，预处理不得在任何验证数据上预先拟合。
3. **038–040 分层、分组与时间：** 分层维护标签比例；分组避免同一实体跨集合；时间划分防止未来数据进入过去模型。两种以上条件需要组合评估。
4. **041–045 CV、KFold、Stratified K-fold、LOOCV 与 OOF：** 弄清折内重新训练、计算开销、估计相关性及 Stacking 的 OOF 训练逻辑。
5. **046–050 Data/Label Leakage、Sampling Bias、Class Imbalance 与 Missing Value：** 高分并非足够，目标分布、泄漏审计和缺失机制需要同时核查。

## 工程案例：跨医院 30 天再入院预测

在出院当时判断未来 30 天是否再次入院。每条样本是符合条件的一次出院事件，但多次出院来自同一患者；建模需明确患者 ID、医院 ID、预测时点与 30 天标签成熟期。不能使用患者再次入院之后产生的诊断、报销或随访数据。跨医院泛化要在医院级保留测试，跨时间泛化则需要后续时间窗测试；各折只在训练部分拟合插补、标准化和特征选择器。处理低再入院率时可考虑类权重，评价用 Recall、Precision、PR-AUC、校准度及组别审计，不能只报告准确率。

## 审稿注意事项

- 核验 K 折分配、分层稀有类、LOOCV、OOF、Cohen κ、逆抽样权重、缺失率等数学题的题设与逐步推导。
- 需要明确 OOF 不等于独立外部测试，TimeSeriesSplit gap 是样本间隔，StratifiedKFold 不保证患者独立。
- 新增 25 篇保持独立审稿 pending；CI 仅对文件结构、编号、链接和习题存在性作自动检验，不冒充专家认可。
