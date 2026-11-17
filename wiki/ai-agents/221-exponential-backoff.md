# Exponential Backoff（指数退避）

> AI Agents · 专题：执行状态、持久化与恢复 · 时延、恢复和外部事务的真实边界

## 1. 核心定义

**Exponential Backoff（指数退避）**：Exponential Backoff（指数退避）是对可重试错误按照指数增长的间隔等待后再次尝试，减少 Agent 或工具服务在短暂故障期间的集体拥塞。通常搭配随机抖动、最大等待时间、重试次数和总体截止时间。

**适用边界：**指数退避不是通用错误修复器：401/403、参数校验失败通常不应按原样重试。即便响应超时，对具有副作用的支付/建单也要先查 transaction_id，不能无条件重复调用。

## 2. 形象理解

像一条拥堵道路，车辆错峰改道而不是所有车每隔一秒一起冲入瓶颈。

**类比的局限：**退避只帮助缓解拥堵，若道路永久封闭或驾驶许可无效，等再久也不会解决问题。

## 3. 技术原理与核心内容

设 base=0.5 秒、factor=2、cap=8 秒，第 k 次失败后的等待 `d_k=min(cap,base*factor^(k−1))`。实际 sleep 可用 full-jitter `U(0,d_k)` 分散蜂群。注意重试次数和等待次数定义：初次调用在 k=0 不等待；遇到 Retry-After 时遵守服务端建议并限制全链路 deadline。对不同层叠加重试设置全局 budget，防止 N 层每层三次最终 3^N 次请求。

## 4. 工程实践与设计权衡

**工程案例：**多租户代码分析 Agent 扫描 API 返回 429，第一次重试等随机 0–0.5 秒，第二次等 0–1 秒，后续上限 8 秒；超过业务 deadline 时返回未完成，而不是在后台无限调用。

**失败模式与验证：**没有 jitter 导致同步惊群、重试覆盖外部副作用、无上界延迟、重试 403 泄漏或浪费资源。测试 429、503、限流头、无界队列、权限拒绝和幂等回执。

## 5. 关联知识与易混辨析

Exponential Backoff 是延时规则；Retry Policy 还决定错误分类/次数/截止时间；Timeout 是单次耗时上限；Circuit Breaker 用于持续故障隔离。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么指数退避推荐附加 jitter？** 答：很多客户端同时失败会同步重试，随机化等待可分散流量峰值并降低下游继续过载的风险。
2. **问：已经提交的转账超时可以直接按指数退避再转一次吗？** 答：不行，必须先用 operation_id 或服务端幂等机制查询原事务。

## 7. 中等难度考试题（含解析）

1. **题：base=1 秒、factor=2、cap=10 秒，第 1、2、3、4 次重试上限等待分别多少？** 解：依次为 1、2、4、8 秒。
2. **题：相同参数第 5 次退避上限为多少？** 解：min(10,1×2^4)=10 秒。

## 8. 权威来源与延伸阅读

- [AWS · Retry with Backoff](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html)：指数延时、暂时错误和幂等边界。
- [Amazon Builders' Library · Timeouts, retries, and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)：deadline 传递、随机抖动和重试放大。
