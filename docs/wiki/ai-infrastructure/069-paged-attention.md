# Paged Attention（分页注意力）

> 学科：AI Infrastructure · 专题：推理与服务 · 推理服务实现需核对引擎版本、请求与测量边界

## 1. 核心定义

分页注意力（PagedAttention）是以类似操作系统虚拟内存分页的**块式 KV Cache 管理**支持注意力读取的技术。逻辑上连续的 token 历史可通过块表映射到不连续的物理 KV block，降低扩容和碎片化的限制；论文提出了专用 attention kernel 处理这种块表。

## 2. 形象理解

把连续书页的逻辑页码映射到分散的书架格子，读者仍按顺序阅读。书架格子不必物理相邻，借阅和复制可复用页块；但每个格子仍有容量，最后一格往往留有空位。

## 3. 技术原理与核心内容

在 vLLM 的早期设计中，每请求维护逻辑 token block 到物理 KV block 的映射，按需分配物理块，attention kernel 根据 block table 获取历史 K/V；对可共享前缀可按引用计数和写时复制策略共享块。若 block_size=B，长度 L 的序列需 `ceil(L/B)` 个逻辑块，单请求最后一个 block 内部浪费不足 B 个 token 槽位，但实际系统还会有元数据、策略和调度约束。PagedAttention 不等于 OS swap 到磁盘，也不应把全部内存浪费都说成零。

## 4. 工程实践与设计权衡

配置 block_size、GPU KV 容量、max_model_len 与并发时，测空闲槽位、block_alloc_fail、preemption、prefix cache hit 和 TTFT/ITL。block 太小可能增加块表/管理开销，过大则增加尾部内部碎片。对于 hybrid attention/Mamba 的模型，KV manager 的分组规则更加复杂，应检查引擎版本。

## 5. 易混概念与边界

PagedAttention 是**分页式管理和访问 KV**的机制；FlashAttention 主要改变 attention kernel 的计算/访存策略，二者可以组合。Prefix caching 是内容复用策略，不等同仅靠分页就能获得命中。

## 6. 中等难度面试题（含参考答案）

1. **问：PagedAttention 为何可能增加可同时容纳的请求数？** 答：按需分配非连续块，减少预留过量连续 KV 和碎片；在固定显存预算下可能支持更多有效缓存 token。但请求变长时总 KV 仍会增长，物理带宽也会形成限制。

2. **问：为什么不能说 PagedAttention 把长上下文模型 KV 需求消除了？** 答：它降低分配碎片和重复，KV 本身仍需存储并被 attention 读取。长上下文 KV 容量与带宽约束仍在，最终取决于模型和请求长度。

## 7. 中等难度考试题（含解析）

1. **题：每块容纳 16 tokens，序列长 1000 tokens，需多少块，最后一块未使用槽位数？** 解：`ceil(1000/16)=**63**` 块，容量 1008，内部空槽位 **8** 个。

2. **题：同样 block_size=16，有三条长度 17、31、32 的互不共享请求，总需多少物理块？** 解：分别 `ceil(17/16)=2`、`ceil(31/16)=2`、`ceil(32/16)=2`，合计 **6 块**；未用槽位 15+1+0=**16**。

## 8. 权威来源与延伸阅读

- [PagedAttention paper](https://arxiv.org/abs/2309.06180)：可用于核对上述机制的维护者文档或原始研究。
- [vLLM Paged Attention design](https://docs.vllm.ai/en/latest/design/paged_attention/)：可用于核对上述机制的维护者文档或原始研究。

> 所有数字示例均为题设下计算，不是生产集群性能承诺。
