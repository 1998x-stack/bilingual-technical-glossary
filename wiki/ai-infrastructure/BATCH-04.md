# 推理服务：性能指标、调度、量化与运行时

> 仅供仓库作者梳理内容依赖。正式读者入口是 TERM/ATLAS Explorer 的术语详情页，不能新增公开批次菜单或独立 Wiki 页面。

## 指标：先说清测量边界

从 [TTFT](061-time-to-first-token.md)、[TPOT](062-time-per-output-token.md)、[ITL](063-inter-token-latency.md)、[TPS](064-tokens-per-second.md)、[RPS](065-requests-per-second.md) 开始，必须区分客户端时间戳、请求级平均与输出事件样本，且明确输入/输出 token 口径。

## 生成机制：调度与内存共同制约吞吐

[Prefill](066-prefill.md) 建立上下文，随后 [Decode](067-decode.md) 逐 token 生成并维护 [KV Cache](068-key-value-cache.md)。[Paged Attention](069-paged-attention.md) 管理物理 KV block，配合 [Continuous Batching](070-continuous-batching.md) 调度不同长度请求。[Dynamic Batching](071-dynamic-batching.md) 面向可合批模型，不等同于迭代级调度。[Speculative Decoding](072-speculative-decoding.md) 以 draft 提议和 target 验证减少串行调用；[PD Disaggregation](073-disaggregated-prefill-and-decode.md) 则把 prefill/decode 分池以降低干扰，需计算 KV 传输成本。

## 表示与交付：不要把“低位宽”误当“低延迟”

先读 [Quantization](074-quantization.md) 和 [Weight-only](075-weight-only-quantization.md)；再对比 [PTQ](076-post-training-quantization.md) 与 [QAT](077-quantization-aware-training.md) 的训练介入与质量风险。部署时通过 [Model Sharding](078-model-sharding.md) 分担权重/计算，使用 [Hot Reload](079-hot-reload.md) 进行版本切流，最后理解 [Container](080-container.md) 的 namespace/cgroup 与宿主 GPU 驱动依赖。

## 研究时必须回答

1. 为什么 TPS 上升时 ITL P99 可能反而恶化？
2. 同一个请求输出 chunk 含多个 token 时，TPOT 与 ITL 如何区别统计？
3. PagedAttention、FlashAttention、prefix caching 的关系是什么？
4. PTQ、QAT、weight-only 和 W8A8 的边界在哪里？
5. 热重载要如何避免新旧模型混合状态，容器化后如何处理 GPU 驱动与显存 OOM？

## 一手资料

- [vLLM 性能指标](https://docs.vllm.ai/en/latest/design/metrics/)
- [vLLM Benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)
- [PagedAttention 原论文](https://arxiv.org/abs/2309.06180)
- [Orca 迭代级调度论文](https://www.usenix.org/conference/osdi22/presentation/yu)
- [Speculative Decoding 原论文](https://arxiv.org/abs/2211.17192)
- [torchao 量化推理](https://docs.pytorch.org/ao/stable/workflows/inference.html)
- [Triton 模型控制](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_management.html)
