# Expert Parallelism（专家并行 · EP）

> 学科：AI Infrastructure · 专题：分布式训练 · 内容范围：训练系统与工程实现（以所引官方资料的版本为准）

## 1. 核心定义

专家并行（EP）将混合专家模型（MoE）的多个专家网络分配到不同设备或 rank，由路由器为 token 选择专家，再把 token 在专家所有者间分发并汇总输出。它分摊专家参数存储与专家计算，而非把每个 token 都送入所有专家。

## 2. 形象理解

一座医院有不同科室，分诊台按病情把患者送到合适专家；专家分散在不同楼层，运输和排队可能抵消同时看诊的优势。类比的边界：MoE 路由可为一个 token 选择多个专家，通常需加权组合专家结果。

## 3. 技术原理与核心内容

一个 top-k MoE 层通常经历：router 产生 logits → 选 k 个专家 → 将 token 按目标 expert 分桶并执行 all-to-all/等价通信 → 专家执行局部 FFN → 结果返还原 token 位置并按门控权重组合。容量因子、负载均衡损失、丢弃或重路由策略会影响准确率与尾延迟。不同实现的 dispatch/combine 通信算法不同；不能把 EP 度误写成模型中专家总数。

## 4. 工程实践与设计权衡

部署 16 个专家到 8 个 rank，可先以每 rank 2 专家为起点；观察各专家接收 token 数、路由熵、发送字节、all-to-all P99 与 GPU kernel idle。若少数热专家成为瓶颈，可以调优路由负载均衡、专家副本、token grouping 或 EP 拓扑。注意网络切分和输入长度分布造成的长尾，不只看平均 token 数。

## 5. 易混概念与边界

**EP** 按 expert 划分，**TP** 把单个专家的矩阵再切片；**DP** 复制一个或一组专家处理不同样本。**SP** 处理序列维激活，不改变 expert 所属关系。EP 与 TP 组合的具体 SP 要求依框架版本而定。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 MoE 参数量很大但每 token FLOPs 不一定同比增加？** 答：稀疏路由仅选择 top-k 专家；每 token 只调用被选中的专家 FFN，未被激活的专家权重不参与该 token 的计算。但 router、token exchange 和专家负载不均可能仍决定实际时延。

2. **问：训练 MoE 时 all-to-all 占主导，排查顺序是什么？** 答：先看每个专家 token 数与容量溢出，再查 EP rank 拓扑是否跨机、网络带宽/拥塞、token 打包粒度与通信重叠。还应检查混合精度与调度是否造成大量小消息，而非盲目增加 EP 度。

## 7. 中等难度考试题（含解析）

1. **题：一个 MoE 层收到 1024 个 token、16 个专家、top-2 选择；假设完全均匀，平均每专家处理多少次 token 指派？** 解：总指派数 `1024×2=2048`；平均 `2048/16=**128**` 次。这是 token–expert 指派数，不等于不重复 token 总数，实际路由通常非均匀。

2. **题：16 个专家均匀部署到 8 个 EP rank；平均每 rank 存几个专家？若平均每专家获得 128 次指派，每 rank 执行多少次？** 解：每 rank `16/8=**2**` 个专家；平均 `2×128=**256**` 次指派计算。不包括 shared experts 或专家复制，网络通信成本不能由此确定。

## 8. 权威来源与延伸阅读

- [Megatron Core MoE Features](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/moe.html)：专家路由、token 分发、负载均衡与 EP/TP 组合。
- [Switch Transformers (Fedus et al.)](https://arxiv.org/abs/2101.03961)：稀疏专家选择与模型容量研究。

> 数值题均为明确的教学假设，不代表设备实际基准性能；版本敏感的接口与优化建议以对应官方文档为准。
