# Cache Hit Rate（缓存命中率）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 数据读写、缓存和负载口径需明确环境及版本

## 1. 核心定义

缓存命中率（Cache Hit Rate）是一定窗口内可由缓存直接满足的访问次数占符合统计边界的总访问次数之比。常见口径为 request hit ratio=`hits/(hits+misses)`；还可按字节计 weighted hit ratio。必须说明是本机 RAM、GPU KV Cache、CDN edge 还是对象存储缓存，以及 stale/revalidation、partial hits 的计数规则。

## 2. 形象理解

像图书馆前台常备借阅书：100 次请求里 85 次可以直接从前台拿到，就是 85% 的请求命中；但如果未命中的是几本特别厚的书，实际从仓库搬来的总字节仍可能非常多。

## 3. 技术原理与核心内容

在同一时间窗内记录 `hits` 和 `misses`，请求命中率 `H=hits/(hits+misses)`，miss ratio=`1−H`。字节命中率 `H_bytes=cache-served_bytes/eligible_requested_bytes` 可能与请求命中率显著不同。真实系统有 TTL、LRU/LFU、capacity、write invalidation、negative caching、range requests 与 revalidate；CDN 的 304 回源与 partial content 是否算命中依供应商统计。高命中率不保证低 P99：miss 可能触发对象下载、远程解压或原始模型 prefill。

## 4. 工程实践与设计权衡

训练节点测 shard cache、page cache 与 GPU prefix KV 命中，不把不同层相加；根据工作集大小、对象尺寸与热点 skew 分层报告 hit rate 和 eviction，防止缓存被一次数据集全量扫描污染。CDN 诊断需记录 cache key、TTL、Vary、Authorization、query parameters 与 purge 策略，避免跨租户缓存内容泄漏。

## 5. 易混概念与边界

Cache hit rate 是缓存被使用的比例，不是命中后节省的绝对时间。`Hit request ratio` 与 `Byte hit ratio` 不相同；缓存命中率也不直接等于缓存命中**价值**，还要看 miss penalty、后端负载、延迟尾部。

## 6. 中等难度面试题（含参考答案）

1. **问：请求命中率 95%，为什么源站仍承担大量带宽？** 答：剩余 5% miss 可能对应最大对象，byte miss ratio 很高；还可能有 revalidation、range miss 或长尾流量未纳入相同统计边界。

2. **问：缓存命中率突然降低，如何定位是工作集变化还是 cache key 配置错误？** 答：对比访问 key 分布、hash/cardinality、TTL/evictions、cache purge、请求 header/query、部署前后缓存容量与新老版本的命中统计。

## 7. 中等难度考试题（含解析）

1. **题：24,000 次请求中有 18,600 次命中、5400 次未命中，request hit ratio？** 解：`18600/24000=**77.5%**`。

2. **题：缓存处理 80GiB，eligible 总请求 100GiB，byte hit ratio？** 解：`80/100=**80%**`，但不能据此推出 request hit ratio 也是 80%。

## 8. 权威来源与延伸阅读

- [Cloudflare Cache Performance](https://developers.cloudflare.com/cache/performance-review/cache-performance/)：用于核对资料机制、测量定义与实现约束的资料。
- [Cloudflare cache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/)：用于核对资料机制、测量定义与实现约束的资料。
- [vLLM Prefix Caching](https://docs.vllm.ai/en/latest/design/prefix_caching/)：用于核对资料机制、测量定义与实现约束的资料。

> 示例计算使用明确的理想条件，不等于某个生产系统的实测结果。
