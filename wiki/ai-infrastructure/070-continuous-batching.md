# Continuous Batching（连续批处理）

> 学科：AI Infrastructure · 专题：推理与服务 · 推理服务实现需核对引擎版本、请求与测量边界

## 1. 核心定义

连续批处理（Continuous Batching）也称迭代级调度，是生成式模型推理中**每次解码迭代或调度步**重新选择在运行的请求集合：已结束的请求可离开，等待中的请求可加入，而不必等待一个固定批的全部请求完成。它提高共享执行资源利用率，但增加 KV/调度复杂度。

## 2. 形象理解

电梯不是让整层楼的所有乘客同一时间进出，而是每停一站有人下车、有人上车；但电梯容量有限，频繁上下人也有开销。这里的“站”对应一次迭代，不意味着真实系统每个 token 必定仅做一次统一 GPU kernel。

## 3. 技术原理与核心内容

Orca 论文提出 iteration-level scheduling；服务 runtime 依据 running/waiting 队列、每序列 token budget、KV block 预算和优先级决定活跃 request 集。不同序列长度/停止条件造成每步 batch 大小变化，调度器还需处理 prefill、decode 共存、KV allocation、流式输出与抢占。相对固定批，连续批处理可减少因一条长请求拖住整个批的空闲窗口；并非消除所有 head-of-line 阻塞。

## 4. 工程实践与设计权衡

对在线对话服务测混合短答和长答负载，比较固定 batch vs continuous scheduling 的 output TPS、TTFT P95、ITL P99、KV occupancy 与等待队列。过度追求大并发可能导致 preempt/recompute 和高尾延迟，需设置 token 与请求级限额。对于长 prompt 可选 chunked prefill 提高共存公平性。

## 5. 易混概念与边界

连续批处理强调**迭代间动态入退**，普通 Dynamic Batching 是按请求到达合批，在某些 Triton stateless 后端中一次 batch 执行完才归还。两者可在不同子系统共存，但术语不能互换。

## 6. 中等难度面试题（含参考答案）

1. **问：为何 continuous batching 更适合不同输出长度的生成请求？** 答：完成短请求后可以在后续迭代释放其 KV slot 并加入新请求，不必等同一固定批最长请求结束。实际性能仍受 KV 容量与调度开销限制。

2. **问：连续批处理提升 TPS 却使 P99 ITL 变差，可能由什么造成？** 答：活跃集合过大、长 prefill 插队、KV preemption 或不公平调度使部分请求等待更久。按请求 trace 联合 running/waiting、KV 使用率分析。

## 7. 中等难度考试题（含解析）

1. **题：运行 8 个请求，其中 3 个完成、随后又接入 5 个，假设容量足够且无其它退出，下轮活跃数？** 解：`8−3+5=**10**` 个；此模型忽略资源预算与请求优先级。

2. **题：固定 batch 必须等最长 5s 任务结束，而另一条 2s 任务已经结束，固定批空置等待时间？** 解：该已完成短请求的 slot 在本批结束前额外空闲 **3 s**。连续批处理原则上能更早重用该位置，但不能保证立即分配成功。

## 8. 权威来源与延伸阅读

- [Orca OSDI 2022](https://www.usenix.org/conference/osdi22/presentation/yu)：可用于核对上述机制的维护者文档或原始研究。
- [vLLM Architecture/Features](https://docs.vllm.ai/en/latest/)：可用于核对上述机制的维护者文档或原始研究。

> 所有数字示例均为题设下计算，不是生产集群性能承诺。
