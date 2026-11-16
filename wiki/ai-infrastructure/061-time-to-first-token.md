# Time to First Token（首词元延迟 · TTFT）

> 学科：AI Infrastructure · 专题：推理与服务 · 所有性能指标必须注明计量口径与软件版本

## 1. 核心定义

首词元延迟（TTFT）是发送生成请求至客户端收到第一个流式输出 token 或首个流式事件所经历的时间。必须报告**起点**（客户端发送、网关入站或引擎调度）及**终点**（首个 token 生成或网络送达），否则不同系统的数字不能直接比较。vLLM benchmark 的客户端口径与引擎内部分阶段指标的计时起点可能不同。

## 2. 形象理解

像餐厅下单到第一道菜端上桌，包含排队、备料、做菜和送菜；后续上菜的间隔是另一种体验。这个类比不能证明每个 LLM 的首 token 都来自独立的一次 decode：引擎可能在 prefill 附近处理首次输出。

## 3. 技术原理与核心内容

可将请求的首包路径拆成 `接入/鉴权 → 等待队列 → prefill → 首次生成 → 流式返回`。非缓存长 prompt 的 prefill 工作量通常较大，prefix cache 命中又会改变路径。记录同一请求 ID 的 queue_time、prefill_time、time_to_first_token 和 network timestamp；注意 SSE 代理可能缓冲输出。任何分解式相加都须声明阶段是否重叠以及首 token 的归属。

## 4. 工程实践与设计权衡

对 128、2048、16384 输入 token 分桶，固定输出长度和并发，画出 TTFT P50/P95/P99 随队列长度的变化。长尾上升先检查长 prompt、chunked prefill、等待调度与 HTTP flush，再考虑 PD disaggregation；后者还可能引入 KV 传输和路由开销。

## 5. 易混概念与边界

TTFT 描述**第一响应**，TPOT 是首响应后的每 token 平均耗时，ITL 按实际相邻流式事件抽样。不能用吞吐 TPS 或仅 GPU prefill kernel 时间替代客户端 TTFT。

## 6. 中等难度面试题（含参考答案）

1. **问：为何 GPU prefill 只耗 40 ms，客户端 TTFT 却超过 200 ms？** 答：测量请求入站到调度的等待、鉴权/tokenize、首步 decode、网关缓冲和网络传输。应把客户端与服务端时间戳对齐，并核实缓存命中和请求归属。

2. **问：PD 分离必然降低 TTFT 吗？** 答：不必然。分离可独立配置 prefill 并隔离 decode 干扰，但 KV 传输、跨池网络及异步调度也有成本。以相同输入分布、同一 SLO 对照实验判断。

## 7. 中等难度考试题（含解析）

1. **题：请求排队 25 ms、prefill 70 ms、首次生成 15 ms、网络返回 10 ms，阶段不重叠，TTFT？** 解：`25+70+15+10=**120 ms**`。若使用客户端发出时间起点，还应计入本题未列的上传等时延。

2. **题：95 次请求 TTFT 为 180 ms、5 次为 600 ms，按最近秩顺序统计的 P95 与 P99？** 解：100 个按升序，位置 95 为 **180 ms**，位置 99 为 **600 ms**。不同监控库采用插值算法时数值口径可能不同。

## 8. 权威来源与延伸阅读

- [vLLM Benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)：所述指标定义、测量或工程实现的维护者说明。
- [vLLM Metrics](https://docs.vllm.ai/en/latest/design/metrics/)：所述指标定义、测量或工程实现的维护者说明。

> 示例中的具体数字是有声明前提的教学计算，不是硬件或线上集群的实测基准。
