# 强化学习 · Reinforcement Learning

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：305 条 · 专题：14 类**

MDPs, value learning, policy optimization and reward models

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 基础概念与交互机制（27 条）
- 02. 马尔可夫决策过程与建模（23 条）
- 03. 价值函数与贝尔曼方程（22 条）
- 04. 蒙特卡洛、时序差分与资格迹（23 条）
- 05. 策略类别与经典表格算法（22 条）
- 06. 策略梯度、信赖域与行动者—评论家（25 条）
- 07. 深度强化学习与训练工程（25 条）
- 08. 分布式价值、风险与不确定性（15 条）
- 09. 探索、规划与模型学习（19 条）
- 10. 模仿学习与离线强化学习（19 条）
- 11. 多智能体与层级强化学习（19 条）
- 12. 奖励模型、RLHF 与偏好优化（16 条）
- 13. 评测、基准与常见环境（29 条）
- 14. 高级主题与应用（21 条）

---

## 01. 基础概念与交互机制

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Reinforcement Learning | 强化学习 | RL | 通过环境交互和奖励反馈学习决策策略的范式。 |
| 2 | Agent | 智能体 |  | 执行动作并据反馈更新策略的决策主体。 |
| 3 | Environment | 环境 |  | 接收动作并产生新观测、奖励等反馈的系统。 |
| 4 | State | 状态 |  | 充分描述环境当前情况、用于预测后续转移的信息。 |
| 5 | Observation | 观测 |  | 智能体可获得的环境信息，不一定等于完整状态。 |
| 6 | Action | 动作 |  | 智能体在某个时刻做出的决策或控制输入。 |
| 7 | Action Space | 动作空间 |  | 智能体可选动作构成的集合。 |
| 8 | State Space | 状态空间 |  | 所有可能环境状态构成的集合。 |
| 9 | Reward | 奖励 |  | 单步标量反馈，通常记作 r_t 或 R_{t+1}。 |
| 10 | Return | 回报 |  | 从某时刻开始的累计未来奖励，常含折扣。 |
| 11 | Policy | 策略 |  | 给定状态或观测时选择动作的规则。 |
| 12 | Deterministic Policy | 确定性策略 |  | 给定状态输出单个动作的策略。 |
| 13 | Stochastic Policy | 随机策略 |  | 给定状态输出动作概率分布的策略。 |
| 14 | Trajectory | 轨迹 |  | 一串状态、动作、奖励等交互记录。 |
| 15 | Episode | 回合 |  | 从初始状态到结束的一段交互过程。 |
| 16 | Rollout | 采样轨迹 |  | 按某策略运行环境得到的交互序列。 |
| 17 | Time Step | 时间步 |  | 一次动作选择及其相应环境反馈的时间单位。 |
| 18 | Horizon | 时域长度 |  | 评估或交互覆盖的时间步数。 |
| 19 | Finite Horizon | 有限时域 |  | 决策过程在有限步后结束。 |
| 20 | Infinite Horizon | 无限时域 |  | 理论上持续运行的决策过程。 |
| 21 | Episodic Task | 回合式任务 |  | 交互分成若干有终点的回合。 |
| 22 | Continuing Task | 持续式任务 |  | 不以自然终点分回合的任务。 |
| 23 | Discrete Action | 离散动作 |  | 动作由有限或可数集合中选取。 |
| 24 | Continuous Action | 连续动作 |  | 动作由连续数值向量表示。 |
| 25 | Sparse Reward | 稀疏奖励 |  | 只有少数时刻提供非零或有信息量的奖励。 |
| 26 | Dense Reward | 密集奖励 |  | 较频繁地给出奖励信号。 |
| 27 | Exploration–Exploitation Trade-off | 探索—利用权衡 |  | 在尝试新动作与利用已知高收益动作间取舍。 |

## 02. 马尔可夫决策过程与建模

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Markov Decision Process | 马尔可夫决策过程 | MDP | 用状态、动作、转移和奖励刻画序贯决策问题。 |
| 2 | Markov Property | 马尔可夫性质 |  | 给定当前状态，未来与更早历史条件独立。 |
| 3 | Transition Probability | 状态转移概率 |  | 给定状态和动作时进入下一状态的概率。 |
| 4 | Transition Kernel | 转移核 |  | 从状态—动作对到下一状态概率分布的映射。 |
| 5 | Reward Function | 奖励函数 |  | 刻画状态、动作或转移产生的奖励的函数。 |
| 6 | Discount Factor | 折扣因子 |  | 控制未来奖励相对当前奖励的权重，常取 0≤γ≤1。 |
| 7 | Initial-State Distribution | 初始状态分布 | ρ₀ | 每回合起点状态的概率分布。 |
| 8 | Terminal State | 终止状态 |  | 按任务定义结束回合的状态。 |
| 9 | Absorbing State | 吸收状态 |  | 进入后通常始终留在其中的状态。 |
| 10 | Partial Observability | 部分可观测性 |  | 智能体无法直接获得完整环境状态。 |
| 11 | Partially Observable MDP | 部分可观测马尔可夫决策过程 | POMDP | 在 MDP 基础上引入隐藏状态和观测模型。 |
| 12 | Belief State | 信念状态 |  | 关于隐藏状态的概率分布或其摘要。 |
| 13 | Observation Function | 观测函数 |  | 描述环境状态如何生成观测的映射。 |
| 14 | History | 交互历史 |  | 截至当前所经历的观测、动作和奖励序列。 |
| 15 | Stationary Policy | 平稳策略 |  | 不随绝对时间步改变决策规则的策略。 |
| 16 | Nonstationarity | 非平稳性 |  | 环境动态、奖励或参与者策略随时间变化。 |
| 17 | Stochastic Dynamics | 随机动力学 |  | 相同状态与动作可能产生不同后继状态。 |
| 18 | Deterministic Dynamics | 确定性动力学 |  | 给定状态与动作唯一决定后继状态。 |
| 19 | Constraint | 约束 |  | 对资源、风险或动作的额外限制条件。 |
| 20 | Constrained MDP | 约束马尔可夫决策过程 |  | 在最大化回报时加入成本等约束的 MDP。 |
| 21 | Semi-Markov Decision Process | 半马尔可夫决策过程 |  | 允许动作或决策间隔具有不同持续时间。 |
| 22 | Reward Shaping | 奖励塑形 |  | 对奖励进行设计以改善学习信号。 |
| 23 | Potential-Based Reward Shaping | 基于势函数的奖励塑形 |  | 用势差修改奖励；在适当条件下保持最优策略。 |

## 03. 价值函数与贝尔曼方程

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | State-Value Function | 状态价值函数 |  | 在给定策略下，从状态出发的期望回报。 |
| 2 | Action-Value Function | 动作价值函数 | Q(s,a) | 先选定动作、随后按策略行动时的期望回报。 |
| 3 | Advantage Function | 优势函数 |  | 动作价值相对状态价值的增益，A=Q−V。 |
| 4 | Optimal Value Function | 最优状态价值函数 | V* | 所有可行策略中状态的最大期望回报。 |
| 5 | Optimal Action-Value Function | 最优动作价值函数 |  | 固定初始动作后可获得的最优期望回报。 |
| 6 | Bellman Equation | 贝尔曼方程 |  | 价值等于当前奖励与下一步价值的期望之和。 |
| 7 | Bellman Expectation Equation | 贝尔曼期望方程 |  | 描述某固定策略对应价值函数的递推关系。 |
| 8 | Bellman Optimality Equation | 贝尔曼最优方程 |  | 对动作取最优选择时的价值递推关系。 |
| 9 | Bellman Backup | 贝尔曼回溯更新 |  | 用一步奖励加后续价值更新当前估计。 |
| 10 | Bellman Operator | 贝尔曼算子 |  | 将价值函数映射到其贝尔曼更新结果的算子。 |
| 11 | Policy Evaluation | 策略评估 |  | 估计当前策略的价值函数。 |
| 12 | Policy Improvement | 策略改进 |  | 根据当前价值估计构造更优策略。 |
| 13 | Policy Iteration | 策略迭代 |  | 交替执行策略评估与策略改进。 |
| 14 | Value Iteration | 价值迭代 |  | 反复执行贝尔曼最优更新。 |
| 15 | Dynamic Programming | 动态规划 | DP | 利用已知环境模型进行递推规划的方法族。 |
| 16 | Generalized Policy Iteration | 广义策略迭代 | GPI | 价值评估与策略改进相互交织的框架。 |
| 17 | Greedy Policy | 贪心策略 |  | 每一步选择当前估计价值最高的动作。 |
| 18 | Bootstrapping | 自举 |  | 用其他时刻的估计值更新当前估计。 |
| 19 | Prediction Problem | 预测问题 |  | 在固定策略下估计价值函数。 |
| 20 | Control Problem | 控制问题 |  | 寻找能最大化预期回报的策略。 |
| 21 | Contraction Mapping | 压缩映射 |  | 使迭代值函数朝唯一不动点收敛的性质。 |
| 22 | Fixed Point | 不动点 |  | 经相应算子更新后不再变化的函数。 |

## 04. 蒙特卡洛、时序差分与资格迹

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Monte Carlo Method | 蒙特卡洛方法 |  | 通过完整回合的样本回报估计价值。 |
| 2 | First-Visit Monte Carlo | 首次访问蒙特卡洛 |  | 每回合仅使用某状态第一次出现后的回报。 |
| 3 | Every-Visit Monte Carlo | 每次访问蒙特卡洛 |  | 使用某状态在回合中的全部访问回报。 |
| 4 | Temporal-Difference Learning | 时序差分学习 |  | 利用奖励与下一时刻估值进行增量更新。 |
| 5 | TD Error | 时序差分误差 |  | 一步目标与当前价值估计之间的差。 |
| 6 | TD(0) | 一步时序差分 |  | 使用一步自举目标更新价值。 |
| 7 | n-Step Return | n 步回报 |  | 先累计 n 步奖励再对剩余部分自举。 |
| 8 | n-Step TD | n 步时序差分 |  | 用 n 步回报更新价值估计。 |
| 9 | TD(λ) | TD(λ) 方法 |  | 结合多个 n 步目标或资格迹进行学习。 |
| 10 | Eligibility Trace | 资格迹 |  | 记录最近访问状态或参数的更新资格。 |
| 11 | Trace Decay Parameter | 迹衰减参数 | λ | 控制较早状态或动作的更新影响。 |
| 12 | Forward View | 前向视角 |  | 用加权多步回报描述 TD(λ)。 |
| 13 | Backward View | 后向视角 |  | 用资格迹在线分配 TD 更新。 |
| 14 | Lambda Return | λ 回报 |  | 对不同 n 步回报做 λ 加权组合。 |
| 15 | SARSA | SARSA 算法 |  | 以实际后续动作的 Q 值作目标的 on-policy TD 控制。 |
| 16 | Expected SARSA | 期望 SARSA |  | 以下一状态按目标策略的期望 Q 值作目标。 |
| 17 | Q-Learning | Q 学习 |  | 以最大下一状态动作价值作目标的 off-policy TD 控制。 |
| 18 | Double Q-Learning | 双 Q 学习 |  | 通过两个价值估计减轻最大化偏差。 |
| 19 | Maximization Bias | 最大化偏差 |  | 选取噪声估计最大值导致的系统性高估。 |
| 20 | Importance Sampling | 重要性采样 |  | 用概率比校正不同采样分布的期望估计。 |
| 21 | Per-Decision Importance Sampling | 逐决策重要性采样 |  | 在时间步级别使用重要性权重。 |
| 22 | Weighted Importance Sampling | 加权重要性采样 |  | 用归一化权重改善估计稳定性。 |
| 23 | Off-Policy Correction | 离策略校正 |  | 纠正行为策略与目标策略分布差异。 |

## 05. 策略类别与经典表格算法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | On-Policy Learning | 同策略学习 |  | 主要用当前目标策略生成的数据学习或评估该策略。 |
| 2 | Off-Policy Learning | 异策略学习 |  | 从一种行为策略的数据学习另一目标策略。 |
| 3 | Behavior Policy | 行为策略 |  | 实际产生训练数据的策略。 |
| 4 | Target Policy | 目标策略 |  | 正在评估或优化的策略。 |
| 5 | Tabular RL | 表格型强化学习 |  | 通过查找表直接存储状态或动作价值。 |
| 6 | Model-Free RL | 无模型强化学习 |  | 不依赖已知状态转移模型直接学习决策。 |
| 7 | Model-Based RL | 基于模型的强化学习 |  | 利用已知或学得环境模型规划或学习。 |
| 8 | Policy-Based Method | 基于策略的方法 |  | 直接参数化并改进策略。 |
| 9 | Value-Based Method | 基于价值的方法 |  | 重点学习价值并据此选择动作。 |
| 10 | Actor–Critic Method | 行动者—评论家方法 |  | 联合学习策略（actor）与价值估计器（critic）。 |
| 11 | Asynchronous Update | 异步更新 |  | 各节点或状态的更新并非完全同步。 |
| 12 | Synchronous Update | 同步更新 |  | 按统一阶段更新或聚合参数。 |
| 13 | Generalized Advantage Estimation | 广义优势估计 |  | 使用 λ 加权的多步 TD 误差估计优势。 |
| 14 | Exploring Starts | 探索性起始 |  | 假设起始状态—动作对均有被访问机会。 |
| 15 | ε-Greedy Policy | ε-贪心策略 |  | 以概率 ε 随机探索，否则选择当前最优动作。 |
| 16 | ε-Soft Policy | ε-软策略 |  | 为每个动作保留一定的正概率。 |
| 17 | Softmax Action Selection | Softmax 动作选择 |  | 将动作偏好通过指数归一化为选择概率。 |
| 18 | Boltzmann Exploration | 玻尔兹曼探索 |  | 按带温度参数的 Softmax 概率探索。 |
| 19 | Upper Confidence Bound | 置信上界策略 | UCB | 利用估计收益和不确定性奖励共同选动作。 |
| 20 | Multi-Armed Bandit | 多臂老虎机问题 |  | 没有状态转移的序贯动作选择问题。 |
| 21 | Contextual Bandit | 上下文老虎机 |  | 依据当下上下文选动作、通常无长期状态转移。 |
| 22 | Regret | 遗憾值 |  | 相对某最优基准方案损失的累计收益。 |

## 06. 策略梯度、信赖域与行动者—评论家

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Policy Gradient | 策略梯度 |  | 沿目标函数对策略参数的梯度优化策略。 |
| 2 | Policy Gradient Theorem | 策略梯度定理 |  | 将策略性能梯度表达为动作对数概率的期望。 |
| 3 | REINFORCE | REINFORCE 算法 |  | 使用蒙特卡洛回报估计策略梯度的经典方法。 |
| 4 | Vanilla Policy Gradient | 基础策略梯度 | VPG | 常指简单的基于策略梯度的更新方法。 |
| 5 | Score Function Estimator | 得分函数估计器 |  | 利用 ∇logπ 构造随机变量期望的梯度估计。 |
| 6 | Log-Probability Trick | 对数概率技巧 |  | 通过 ∇p=p∇log p 重写梯度。 |
| 7 | Baseline | 基线 |  | 减去不依赖所选动作的量以降低梯度方差。 |
| 8 | Variance Reduction | 方差缩减 |  | 降低梯度或回报估计噪声的方法。 |
| 9 | Surrogate Objective | 代理目标 |  | 为便于更新而构造的近似优化目标。 |
| 10 | Likelihood Ratio | 似然比 |  | 新旧策略对同一动作的概率之比。 |
| 11 | Trust Region | 信赖域 |  | 限制每次策略更新变化幅度的区域。 |
| 12 | Trust Region Policy Optimization | 信赖域策略优化 |  | 在策略变化约束下优化策略目标。 |
| 13 | Proximal Policy Optimization | 近端策略优化 | PPO | 通过裁剪或惩罚代理目标限制策略更新。 |
| 14 | Clipped Surrogate Objective | 裁剪代理目标 |  | 对概率比进行裁剪以抑制过大策略更新。 |
| 15 | KL Divergence | KL 散度 |  | 比较两个概率分布差异的非对称度量。 |
| 16 | Entropy Bonus | 熵奖励项 |  | 在目标中鼓励随机策略保持一定探索性。 |
| 17 | Entropy Regularization | 熵正则化 |  | 将策略熵纳入优化目标。 |
| 18 | Deterministic Policy Gradient | 确定性策略梯度 | DPG | 直接对确定性动作输出求策略梯度。 |
| 19 | Deep Deterministic Policy Gradient | 深度确定性策略梯度 |  | 连续动作空间的离策略 actor–critic 方法。 |
| 20 | Twin Delayed DDPG | 双延迟深度确定性策略梯度 |  | 使用双 Q、延迟策略更新等改进 DDPG。 |
| 21 | Soft Actor-Critic | 软行动者—评论家 |  | 面向最大熵目标的离策略随机 actor–critic。 |
| 22 | Asynchronous Advantage Actor-Critic | 异步优势行动者—评论家 |  | 多工作进程异步更新共享模型的算法。 |
| 23 | Advantage Actor-Critic | 优势行动者—评论家 | A2C | 常指 A3C 风格的同步 actor–critic 变体。 |
| 24 | Critic | 评论家网络 |  | 估计价值或优势以辅助策略学习。 |
| 25 | Actor | 行动者网络 |  | 输出动作或动作分布的策略网络。 |

## 07. 深度强化学习与训练工程

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Deep Reinforcement Learning | 深度强化学习 |  | 用深度神经网络表示策略、价值函数或环境模型。 |
| 2 | Deep Q-Network | 深度 Q 网络 |  | 使用神经网络逼近 Q 值的经典方法。 |
| 3 | Double DQN | 双重深度 Q 网络 |  | 用动作选择与动作评价分离减轻 Q 值高估。 |
| 4 | Dueling DQN | 决斗结构深度 Q 网络 |  | 分别估计状态价值与动作优势并进行组合。 |
| 5 | Rainbow DQN | 彩虹 DQN |  | 整合多项 DQN 改进技巧的算法。 |
| 6 | Experience Replay | 经验回放 |  | 将历史交互样本存入缓冲区以重复训练。 |
| 7 | Replay Buffer | 经验回放缓冲区 |  | 保存状态转移等训练样本的数据结构。 |
| 8 | Prioritized Experience Replay | 优先经验回放 |  | 按 TD 误差等重要程度优先抽样。 |
| 9 | Target Network | 目标网络 |  | 较慢更新的网络，用于生成较稳定的学习目标。 |
| 10 | Online Network | 在线网络 |  | 被梯度更新、用于价值或策略估计的当前网络。 |
| 11 | Polyak Averaging | Polyak 平均 |  | 对参数执行指数滑动平均以更新目标网络。 |
| 12 | Hard Target Update | 硬目标更新 |  | 周期性直接复制在线网络参数到目标网络。 |
| 13 | Soft Target Update | 软目标更新 |  | 以较小插值系数平滑更新目标网络。 |
| 14 | Function Approximation | 函数逼近 |  | 用参数化函数估计价值、策略或模型。 |
| 15 | Deadly Triad | 致命三要素 |  | 自举、离策略和函数逼近组合可能导致发散。 |
| 16 | Overestimation Bias | 高估偏差 |  | 估计 Q 值相对真实目标偏高的倾向。 |
| 17 | Gradient Clipping | 梯度裁剪 |  | 限制梯度范数或数值范围以稳定训练。 |
| 18 | Reward Clipping | 奖励裁剪 |  | 将奖励限制在指定范围的预处理方法。 |
| 19 | Observation Normalization | 观测归一化 |  | 缩放观测特征以改善数值稳定性。 |
| 20 | Reward Normalization | 奖励归一化 |  | 按统计量缩放奖励或回报。 |
| 21 | Vectorized Environment | 向量化环境 |  | 并行运行多个环境实例以提高吞吐量。 |
| 22 | Sample Efficiency | 样本效率 |  | 达到某性能所需环境交互样本的多少。 |
| 23 | Wall-Clock Time | 实际耗时 |  | 算法执行的真实时间开销。 |
| 24 | Hyperparameter | 超参数 |  | 学习率、折扣因子等训练前设定的控制量。 |
| 25 | Random Seed | 随机种子 |  | 控制可复现随机过程的初始化值。 |

## 08. 分布式价值、风险与不确定性

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Distributional RL | 分布强化学习 |  | 学习回报的概率分布，而非仅估计其期望。 |
| 2 | Return Distribution | 回报分布 |  | 未来累计回报的完整随机分布。 |
| 3 | Categorical DQN | 分类分布式 DQN |  | 用固定支持点上的分类分布近似回报分布。 |
| 4 | Quantile Regression DQN | 分位数回归 DQN | QR-DQN | 使用分位数回归学习回报分布。 |
| 5 | Implicit Quantile Network | 隐式分位数网络 | IQN | 以分位数参数化方式生成回报估计。 |
| 6 | Risk-Sensitive RL | 风险敏感强化学习 |  | 在目标中考虑回报波动与尾部风险。 |
| 7 | Conditional Value at Risk | 条件风险价值 | CVaR | 衡量分布尾部极端不利结果的风险指标。 |
| 8 | Value at Risk | 风险价值 |  | 给定分位水平下的损失阈值指标。 |
| 9 | Epistemic Uncertainty | 认知不确定性 |  | 由知识不足导致、可随数据增加减少的不确定性。 |
| 10 | Aleatoric Uncertainty | 偶然不确定性 |  | 由环境固有随机性导致的不确定性。 |
| 11 | Ensemble | 模型集成 |  | 结合多个模型估计以改善稳定性或不确定性评估。 |
| 12 | Calibration | 校准 |  | 预测置信度与真实频率的一致程度。 |
| 13 | Distribution Shift | 分布偏移 |  | 训练与部署数据分布存在差别。 |
| 14 | Out-of-Distribution | 分布外 |  | 超出训练数据典型覆盖范围的样本或状态。 |
| 15 | Conservative Estimate | 保守估计 |  | 倾向避免过高估计价值或收益的估计方式。 |

## 09. 探索、规划与模型学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | World Model | 世界模型 |  | 预测环境动态、观测或奖励的学习模型。 |
| 2 | Dynamics Model | 动力学模型 |  | 根据状态与动作预测下一状态或分布。 |
| 3 | Learned Model | 学习得到的模型 |  | 从交互数据拟合而不是先验给定的模型。 |
| 4 | Planning | 规划 |  | 利用模型搜索未来动作序列或决策方案。 |
| 5 | Model Predictive Control | 模型预测控制 | MPC | 反复优化短期动作序列并仅执行当前动作。 |
| 6 | Dyna | Dyna 框架 |  | 将真实经验、模型学习和模拟规划结合的框架。 |
| 7 | Imagination Rollout | 想象采样轨迹 |  | 在学得模型中模拟未来交互轨迹。 |
| 8 | Monte Carlo Tree Search | 蒙特卡洛树搜索 | MCTS | 通过采样与树搜索选择动作的方法。 |
| 9 | Upper Confidence Bounds for Trees | 树搜索置信上界 |  | 将 UCB 用于树节点选择的规则。 |
| 10 | Search Tree | 搜索树 |  | 表达候选动作及后续状态分支的数据结构。 |
| 11 | Leaf Evaluation | 叶节点评估 |  | 估计搜索树末端节点的价值。 |
| 12 | Planning Horizon | 规划时域 |  | 模型规划向前展开的步数。 |
| 13 | Open-Loop Planning | 开环规划 |  | 先规划一段动作序列，执行期间不使用新反馈改动计划。 |
| 14 | Closed-Loop Control | 闭环控制 |  | 根据新观测持续调整当前控制动作。 |
| 15 | Model Bias | 模型偏差 |  | 学得模型误差引入的价值或决策偏差。 |
| 16 | Simulation-to-Real Transfer | 仿真到现实迁移 | Sim2Real | 将仿真环境学到的策略部署到现实系统。 |
| 17 | Domain Randomization | 域随机化 |  | 随机改变仿真条件以提升跨环境泛化。 |
| 18 | System Identification | 系统辨识 |  | 根据输入输出数据推断环境动力学参数。 |
| 19 | Latent Dynamics | 潜在空间动力学 |  | 在压缩表征空间中学习状态转移。 |

## 10. 模仿学习与离线强化学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Intrinsic Reward | 内在奖励 |  | 由好奇心、新颖性等内部指标构造的奖励。 |
| 2 | Extrinsic Reward | 外在奖励 |  | 由环境任务目标直接给出的奖励。 |
| 3 | Curiosity-Driven Exploration | 好奇心驱动探索 |  | 借助预测误差或新颖性鼓励未知状态探索。 |
| 4 | Count-Based Exploration | 计数式探索 |  | 利用状态访问次数调整探索奖励。 |
| 5 | Pseudo-Count | 伪计数 |  | 在复杂状态空间中近似估计访问次数。 |
| 6 | Random Network Distillation | 随机网络蒸馏 | RND | 用固定随机网络的预测误差提供新颖性信号。 |
| 7 | Information Gain | 信息增益 |  | 新观测减少模型不确定性的程度。 |
| 8 | Empowerment | 赋能度 |  | 状态下智能体对未来可达结果的控制能力指标。 |
| 9 | Hierarchical RL | 层次强化学习 |  | 用多级决策或子技能处理长时序任务。 |
| 10 | Option | 选项 |  | 具有启动条件、内部策略和终止条件的时序扩展动作。 |
| 11 | Option-Critic | 选项评论家方法 |  | 联合学习选项内部策略与终止条件的框架。 |
| 12 | Skill | 技能 |  | 可复用的行为策略或子任务能力。 |
| 13 | Subgoal | 子目标 |  | 服务于长期任务的中间目标。 |
| 14 | Goal-Conditioned Policy | 目标条件策略 |  | 根据当前状态及目标共同选择动作的策略。 |
| 15 | Hindsight Experience Replay | 事后经验回放 | HER | 将实际达到的结果重新当作目标利用经验。 |
| 16 | Successor Representation | 后继表征 | SR | 表示未来状态访问折扣频率的特征形式。 |
| 17 | Temporal Abstraction | 时间抽象 |  | 以持续多个时间步的行为作为决策单元。 |
| 18 | Curriculum Learning | 课程学习 |  | 按照任务难度或结构逐步组织训练。 |
| 19 | Self-Play | 自我对弈 |  | 智能体与自身或历史策略交互以改进策略。 |

## 11. 多智能体与层级强化学习

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Offline Reinforcement Learning | 离线强化学习 |  | 仅依赖固定历史数据集学习策略，不在线采样更新数据。 |
| 2 | Batch RL | 批量强化学习 |  | 通常与离线 RL 近义，强调从给定批量数据学习。 |
| 3 | Online Reinforcement Learning | 在线强化学习 |  | 学习过程中持续与环境交互并获取新数据。 |
| 4 | Behavior Cloning | 行为克隆 |  | 将专家状态—动作对当作监督数据拟合策略。 |
| 5 | Imitation Learning | 模仿学习 |  | 通过模仿示范行为学习决策的方法族。 |
| 6 | Inverse Reinforcement Learning | 逆强化学习 |  | 从示范行为推断可能的奖励函数。 |
| 7 | Apprenticeship Learning | 学徒学习 |  | 通过专家示范使学习策略达到相近表现。 |
| 8 | Generative Adversarial Imitation Learning | 生成对抗模仿学习 |  | 用对抗训练匹配专家与学习者的行为分布。 |
| 9 | Dataset Coverage | 数据集覆盖度 |  | 离线数据对状态—动作空间的覆盖程度。 |
| 10 | Extrapolation Error | 外推误差 |  | 对训练数据未覆盖动作作价值估计时出现的误差。 |
| 11 | Conservative Q-Learning | 保守 Q 学习 | CQL | 通过对 Q 值施加保守约束降低分布外动作高估。 |
| 12 | Implicit Q-Learning | 隐式 Q 学习 |  | 避免显式评估数据外动作的离线 RL 方法。 |
| 13 | Behavior Regularization | 行为正则化 |  | 限制学习策略不要过度偏离数据行为策略。 |
| 14 | Behavior Support | 行为支持集 |  | 数据行为策略具有非零概率的动作区域。 |
| 15 | Offline Policy Evaluation | 离线策略评估 | OPE | 在不执行目标策略时估计其性能。 |
| 16 | Direct Method | 直接法 |  | 用估计奖励或价值模型评估策略。 |
| 17 | Doubly Robust Estimator | 双重稳健估计器 | DR | 结合模型估计与重要性加权进行策略评估。 |
| 18 | Fitted Q Evaluation | 拟合 Q 评估 |  | 利用固定数据拟合目标策略的 Q 函数。 |
| 19 | Fitted Q Iteration | 拟合 Q 迭代 |  | 用监督回归反复逼近贝尔曼最优目标。 |

## 12. 奖励模型、RLHF 与偏好优化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Multi-Agent Reinforcement Learning | 多智能体强化学习 |  | 多个相互作用的智能体同时学习或决策。 |
| 2 | Markov Game | 马尔可夫博弈 |  | 将 MDP 扩展为多智能体交互的形式化模型。 |
| 3 | Stochastic Game | 随机博弈 |  | 又称马尔可夫博弈，包含状态转移与多参与者收益。 |
| 4 | Cooperative MARL | 合作式多智能体强化学习 |  | 各智能体追求共享或一致的任务目标。 |
| 5 | Competitive MARL | 竞争式多智能体强化学习 |  | 智能体目标冲突，需考虑相互对抗。 |
| 6 | Mixed-Motive Game | 混合动机博弈 |  | 同时存在合作与竞争的多智能体情境。 |
| 7 | Centralized Training, Decentralized Execution | 集中训练、分散执行 |  | 训练时使用全局信息，执行时各体独立决策。 |
| 8 | Independent Q-Learning | 独立 Q 学习 | IQL (MARL) | 各智能体将其他智能体当作环境的一部分分别学习。 |
| 9 | Value Decomposition Networks | 价值分解网络 |  | 把团队价值表示为各智能体局部价值之和。 |
| 10 | QMIX | QMIX 算法 |  | 用单调混合网络结合个体 Q 值得到团队 Q 值。 |
| 11 | Multi-Agent DDPG | 多智能体深度确定性策略梯度 |  | 集中 critic 与分散 actor 的多智能体方法。 |
| 12 | Credit Assignment | 信用分配 |  | 判断团队结果应归因于哪些智能体或动作。 |
| 13 | Joint Action | 联合动作 |  | 所有智能体在同一时刻的动作组合。 |
| 14 | Nash Equilibrium | 纳什均衡 |  | 任一参与者单独改策略都无法提高自身收益的状态。 |
| 15 | Opponent Modeling | 对手建模 |  | 估计其他智能体的策略、目标或行为规律。 |
| 16 | Population-Based Training | 基于种群的训练 | PBT | 并行维护多个策略并通过选择与变异更新。 |

## 13. 评测、基准与常见环境

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Reinforcement Learning from Human Feedback | 基于人类反馈的强化学习 |  | 利用人类反馈形成训练信号以改进模型行为。 |
| 2 | Reinforcement Learning from AI Feedback | 基于 AI 反馈的强化学习 |  | 用模型提供的反馈或偏好代替或补充人工反馈。 |
| 3 | Reinforcement Learning with Verifiable Rewards | 基于可验证奖励的强化学习 |  | 依据可自动判定正确性的反馈优化模型输出。 |
| 4 | Supervised Fine-Tuning | 监督微调 | SFT | 用示范数据做监督学习；本身不是强化学习。 |
| 5 | Preference Dataset | 偏好数据集 |  | 包含候选响应及其偏好比较的训练数据。 |
| 6 | Pairwise Preference | 成对偏好 |  | 比较两份响应并标注哪一个更受偏好。 |
| 7 | Chosen Response | 优选响应 |  | 偏好对中被选择的较优回答。 |
| 8 | Rejected Response | 未选响应 |  | 偏好对中未被选择的回答。 |
| 9 | Reward Model | 奖励模型 |  | 将候选输出映射为奖励分数的学习模型。 |
| 10 | Outcome Reward Model | 结果奖励模型 | ORM | 主要评价完整答案或最终结果的奖励模型。 |
| 11 | Process Reward Model | 过程奖励模型 | PRM | 对推理步骤或中间过程提供评价的模型。 |
| 12 | Preference Model | 偏好模型 |  | 预测候选输出之间相对偏好的模型。 |
| 13 | Bradley–Terry Model | 布拉德利—特里模型 |  | 以潜在分数描述两两比较胜出概率的模型。 |
| 14 | Reference Policy | 参考策略 |  | 用作概率比或 KL 约束基准的固定策略。 |
| 15 | Policy Model | 策略模型 |  | 被训练以生成输出的模型。 |
| 16 | Direct Preference Optimization | 直接偏好优化 |  | 直接用偏好对训练策略，通常不显式训练奖励模型或在线 RL。 |
| 17 | Group Relative Policy Optimization | 组相对策略优化 |  | 通过同一提示下多条回答的组内奖励比较估计优势。 |
| 18 | REINFORCE Leave-One-Out | 留一法 REINFORCE | RLOO | 用同组其他样本回报构造基线的策略梯度方法。 |
| 19 | KL Penalty | KL 惩罚项 |  | 抑制优化后策略偏离参考策略过远的惩罚。 |
| 20 | KL Coefficient | KL 系数 |  | 控制相对参考策略约束强弱的权重。 |
| 21 | Reward Hacking | 奖励投机 |  | 模型利用奖励函数缺陷得高分却未实现真实目标。 |
| 22 | Reward Overoptimization | 奖励过度优化 |  | 过度针对代理奖励优化导致真实质量下降。 |
| 23 | Alignment Tax | 对齐代价 |  | 对齐训练可能带来的其他能力或性能损失。 |
| 24 | Best-of-N Sampling | N 选一采样 |  | 生成 N 个候选并按评分选取一个。 |
| 25 | Rejection Sampling | 拒绝采样 |  | 通过评分或规则筛选生成样本的过程。 |
| 26 | Completion | 生成续写 |  | 给定提示后模型生成的输出文本。 |
| 27 | Token-Level Reward | 词元级奖励 |  | 对单个词元或位置提供的奖励信号。 |
| 28 | Sequence-Level Reward | 序列级奖励 |  | 对完整生成序列进行的整体评分。 |
| 29 | Advantage Normalization | 优势归一化 |  | 将优势按均值和方差缩放以稳定更新。 |

## 14. 高级主题与应用

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Evaluation Episode | 评估回合 |  | 不用于策略参数更新、专门测量性能的交互回合。 |
| 2 | Average Episodic Return | 平均回合回报 |  | 多个评估回合的累计奖励均值。 |
| 3 | Success Rate | 成功率 |  | 达到任务成功条件的回合比例。 |
| 4 | Learning Curve | 学习曲线 |  | 训练进度与性能指标之间的关系图。 |
| 5 | Sample Complexity | 样本复杂度 |  | 达到目标误差或性能所需样本数量级。 |
| 6 | Generalization | 泛化 |  | 策略在未见情境下维持表现的能力。 |
| 7 | Robustness | 鲁棒性 |  | 面对扰动、噪声和分布变化仍保持性能的能力。 |
| 8 | Safety Constraint | 安全约束 |  | 限制危险动作、风险或累计成本的条件。 |
| 9 | Safe RL | 安全强化学习 |  | 在学习或执行过程中考虑风险与安全要求的 RL。 |
| 10 | Cost Function | 成本函数 |  | 量化约束违规或不良后果的数值函数。 |
| 11 | Lagrangian Method | 拉格朗日方法 |  | 通过乘子将约束转化为优化目标的一种方法。 |
| 12 | Reward Scale | 奖励尺度 |  | 奖励取值大小影响价值尺度和优化动态。 |
| 13 | Training Instability | 训练不稳定性 |  | 学习过程大幅震荡、性能退化或发散。 |
| 14 | Seed Variance | 随机种子方差 |  | 不同随机种子导致训练结果的差异。 |
| 15 | Confidence Interval | 置信区间 |  | 对统计估计不确定性的区间描述。 |
| 16 | Termination | 任务终止 |  | 根据环境任务定义进入终止状态。 |
| 17 | Truncation | 外部截断 |  | 因时间限制等外部条件中止回合，未必到终止状态。 |
| 18 | Bootstrapping Mask | 自举掩码 |  | 控制在某类结束信号后是否继续使用下一状态价值。 |
| 19 | Data Leakage | 数据泄漏 |  | 训练或调参意外利用评测专用信息。 |
| 20 | Benchmark | 基准测试 |  | 用于统一比较方法的任务和评估协议。 |
| 21 | Reproducibility | 可复现性 |  | 他人依据公开设置能得到一致趋势或结果的程度。 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/reinforcement-learning.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
