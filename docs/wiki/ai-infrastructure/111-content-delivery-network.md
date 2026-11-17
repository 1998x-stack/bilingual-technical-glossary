# Content Delivery Network（内容分发网络 · CDN）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 服务边界、窗口和用户可见性必须明确

## 1. 核心定义

内容分发网络（Content Delivery Network，CDN）通过地理或网络拓扑上分布的边缘节点缓存/转发内容，让请求尽量靠近用户完成，从而降低回源流量与部分请求延迟。CDN 可以处理静态资源、分片视频、下载包，也可代理动态 HTTPS 请求；是否缓存取决于 cache policy、method、response headers、权限与 cache key。

## 2. 形象理解

像在各城市建本地配送站：常用商品在近处就能取到，减少跨城运输；但售罄或库存失效时仍需向中心仓补货。站点多并不保证每个请求都命中或响应快。

## 3. 技术原理与核心内容

DNS/Anycast 等路由让客户端接入边缘 PoP，edge 根据 scheme/host/path/query、header 等因素构造 cache key。命中直接返回，未命中/过期则向 origin 或上层 shield 请求并按 Cache-Control、ETag/Last-Modified 处理缓存、revalidation 和更新。不同 CDN 的 tiered cache、purge、stale-while-revalidate、range requests 和 TLS 终止策略存在差异。请求缓存命中率与字节命中率不同；个性化/授权数据必须配置正确的私有缓存策略，不能因为“加速”就共享敏感 token 或生成内容。

## 4. 工程实践与设计权衡

TERM/ATLAS、模型权重分发与客户端下载可以对 versioned immutable assets 配长 TTL，并在变更时发布新 digest；HTML/API 需合理使用 short TTL、revalidation 或 no-store。验证边缘与源站的 cache status、P50/P99、HTTP 3xx/4xx/5xx、跨区域 RTT、回源带宽、cache key cardinality 和 purge 传播。发布大型训练 shard 可先规划跨地域镜像/分发；CDN 并不自动解决训练集许可与权限隔离。

## 5. 易混概念与边界

CDN 是网络边缘分发层，不等同对象存储源站；`Cache-Control: private` 的响应不应被共享边缘缓存当作公共资源。CDN hit ratio 既非可靠性 SLO，也非源站可用性指标；动态反向代理与缓存加速是两个可能同时存在的功能。

## 6. 中等难度面试题（含参考答案）

1. **问：为何 URL 带随机查询参数时 CDN 命中率会下降？** 答：默认 cache key 往往包含 query string，不同参数会导致逻辑上相同内容变成不同缓存对象。可在保证语义正确与安全前提下规范化可忽略参数。

2. **问：API 返回用户隐私数据时如何避免 CDN 跨用户泄漏？** 答：使用 Cache-Control private/no-store、正确的认证/授权流程、区分用户身份的 cache key 或直接 bypass cache；不能将带个人数据的响应错误标为 public。

## 7. 中等难度考试题（含解析）

1. **题：某 CDN 节点一个小时收到 100万次 eligible 请求，命中 87万，request hit ratio？** 解：`870000/1000000=**87%**`，回源请求数量不一定精确等于未命中数，因为 shield、合并回源和 revalidation 会影响。

2. **题：总客户端下载 2TiB，edge 直接从缓存发送 1.5TiB，忽略协议开销，byte hit ratio？** 解：`1.5/2=**75%**`；不能由此推断 request hit ratio 也是 75%。

## 8. 权威来源与延伸阅读

- [Cloudflare Cache Keys](https://developers.cloudflare.com/cache/how-to/cache-keys/)：用于核对服务目标、指标与统计约定的原始资料。
- [Cloudflare cache performance](https://developers.cloudflare.com/cache/performance-review/cache-performance/)：用于核对服务目标、指标与统计约定的原始资料。
- [HTTP Caching RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html)：用于核对服务目标、指标与统计约定的原始资料。

> 计算题中的数值为条件明确的教学示例；不代表具体运营合同或实际 SLO。
