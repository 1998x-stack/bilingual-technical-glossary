# Pipeline（流水线）

> 领域：机器学习 · 专题：数据预处理与特征工程 · 定义、原理、数学与真实工程边界

## 1. 核心定义

机器学习流水线（Pipeline）把缺失填补、缩放、特征选择、编码与最终估计器按顺序组合为可复现对象，保证训练、验证和推理使用同一套变换规则。它解决流程一致性和大量常见泄漏风险，但不能自动阻止特征本身包含未来信息。

## 2. 形象理解

像工厂生产线：原材料依次清洗、分拣、加工、质检，各工序参数与顺序被固定并可追踪。

**类比的局限：**工厂流程正确仍可能原料来源错误；Pipeline 不替代时点约束、患者/用户分组和测试集纪律。

## 3. 技术原理与核心内容

对于 transformer T₁,…,T_m 与估计器 f，fit 按顺序 T₁.fit_transform(X_train)→…→f.fit；predict 则复用保存的 T_j.transform 而不是重新拟合。scikit-learn Pipeline 与 ColumnTransformer 可组合列级分支，GridSearchCV 在各折自动重新 fit 整个 Pipeline。包含 SMOTE 的重采样步骤需使用 imbalanced-learn Pipeline，其 fit_resample 仅用于训练过程。

## 4. 工程实践与设计权衡

信用评分服务把 SimpleImputer、StandardScaler、OneHotEncoder 和逻辑回归封装为版本化 Pipeline，记录 schema、参数和阈值；监控未知类别/单位变化，线上只调用 predict_proba 而不是单独手写预处理。

## 5. 关联知识与易混辨析

Pipeline 是端到端变换契约；Data Preprocessing 是其中的数据操作；Workflow Orchestration 是任务调度层。Pipeline 防止 fit 范围误用，却不能让未来产生的字段变得合法。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么交叉验证时只把模型放入 GridSearchCV 而预先全量拟合选择器不安全？** 答：选择器已利用验证折数据甚至标签，应将其与估计器共同置于 Pipeline 使每折独立 fit。

2. **问：为什么重采样不能像普通 transformer 在推理时对新输入继续执行？** 答：采样是改变训练样本分布的 fit 阶段操作，不应在 predict 时构造新测试样本；使用专用的 imbalanced-learn Pipeline 处理。

## 7. 中等难度考试题（含解析）

1. **题：一个 Pipeline 包含 3 个 transformer 和 1 个 estimator，固定超参做 5 折 CV 通常需要拟合几套完整流水线？** 解：5 套；每折都重新拟合各 transformer 和 estimator，不共享折外数据统计。

2. **题：训练特征均值为 20，测试样本为 30；若 Pipeline 仅做中心化，测试值转为多少？** 解：30−20=10，不能把测试点参与重新计算训练均值。

## 8. 权威来源与延伸阅读

- [scikit-learn Pipeline 官方文档](https://scikit-learn.org/stable/modules/compose.html#pipeline)：供核对正式定义、公式、实现与适用条件。
- [imbalanced-learn Pipeline 官方 API](https://imbalanced-learn.org/stable/references/generated/imblearn.pipeline.Pipeline.html)：供核对正式定义、公式、实现与适用条件。

> 上述数值均为教学题设，并非实际业务基准；专家内容审稿仍为 pending。
