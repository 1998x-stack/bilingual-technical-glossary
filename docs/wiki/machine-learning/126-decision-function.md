# Decision Function（决策函数）

> 领域：机器学习 · 专题：回归、分类与线性模型 · 数学原理、技术约束与工程实践

## 1. 核心定义

决策函数（Decision Function）是分类器将输入映射成可比较的实数得分或多类得分向量的函数，通常在阈值或 argmax 规则后才变成类别预测。得分并非天然概率：不同估计器对得分的定义、符号方向、形状及可比性并不相同。

## 2. 形象理解

像机场安检仪先为每件行李给出风险分数，再依据阈值决定是否进入人工复检；分数和最终决定是两个不同步骤。

**类比的局限：**一台仪器的 2 分和另一台的 2 分不一定代表相同风险；分数绝对值是否能解释成几何距离还取决于模型归一化。

## 3. 技术原理与核心内容

在二分类线性分类器中 s(x)=wᵀx+b，常以 sign(s) 决策；若使用逻辑回归，则 p(y=1|x)=σ(s)，s 是 log-odds。SVM 的 `decision_function` 通常给出有符号间隔分数，但除非按范数归一化，否则不是欧氏距离。多类情形返回各类得分或 OVO 转换得分，其形状依 estimator 的 `decision_function_shape` 而变。要观察 `classes_` 顺序，并用单独的概率校准对照评估。

## 4. 工程实践与设计权衡

欺诈审核服务保留 raw decision score、版本化阈值和最终 action 三个字段，方便业务成本变化时调整阈值而不重训模型。校准应在与训练隔离的数据上完成，监控负类分数分布与未知样本。

## 5. 关联知识与易混辨析

Decision Function 输出决策依据，Decision Boundary 是分类切换的点集；`predict_proba` 输出概率但校准水平因模型不同；Margin 指间隔，不能与任意 score 混同。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 SVM 的 decision_function=2 不能直接称为 88% 的风险概率？** 答：SVM 得分是间隔相关的数值而非后验概率，需要独立校准；即使模型提供 predict_proba，也要检验校准和类别映射。

2. **问：两次训练得到的决策函数分数可直接比较吗？** 答：参数缩放、特征预处理与类别定义可能不同，甚至相同决策边界可对应不同得分；比较前需要固定模型版本和评分尺度。

## 7. 中等难度考试题（含解析）

1. **题：s(x)=2x₁−x₂+1，x=(1,4)，零阈值下得分及类别符号？** 解：得分 2−4+1=−1，以 s≥0 判正的规则下输出负类。

2. **题：两类模型 s(x)=0.8、决策阈值 0.5，预测结果？该分数一定是概率吗？** 解：按给定得分阈值判正；但 0.8 本身不一定是概率，须看 score 定义。

## 8. 权威来源与延伸阅读

- [scikit-learn LinearSVC decision_function](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)：用于核对定义、数理行为、参数或实现限制。
- [scikit-learn LogisticRegression 接口](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)：用于核对定义、数理行为、参数或实现限制。

> 文中定量例题均为教学假设而非生产实测数据；独立技术专家审稿记录仍为 pending。
