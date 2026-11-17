# Retry Policy（重试策略）

> AI Agents · 专题：执行状态、持久化与恢复 · 工程事故防护与可恢复性以业务事实为准

## 1. 核心定义

**Retry Policy（重试策略）**：Retry Policy（重试策略）是对某类调用失败之后是否重试、等待多久、最多重试多少次、何时停止以及如何保护副作用作出的系统性规则。它在 Agent 工具调用和远程多智能体交互中直接影响延迟、成本、服务负载与业务一致性。

**适用边界：**Retry 不等于重新发起全新业务事务。对支付、建单、删除等动作，网络失败时须先依据 stable idempotency_key/operation_id 查证后端状态。不同错误码要有明确分类，别把 401/403 等权限拒绝用重试绕过。

## 2. 形象理解

像拨打繁忙的电话，过一会儿重拨几次有意义；但如果对方已经接通并办好了事情，就不该不断发新的申请。

**类比的局限：**如果号码写错，重拨次数再多也无济于事；拨号成功也不代表业务办理完毕。

## 3. 技术原理与核心内容

配置 Retry={retryable_codes,maxAttempts,baseDelay,multiplier,maxDelay,jitter,maxElapsed,deadline}；例如仅对 429/503 或可确定的临时网络错误延时重试，用指数退避与随机抖动避免所有 Agent 同步冲击服务。每次请求记 attempt_id，跨重试保持同一业务幂等键，对结果 unknown 先查询事务状态。上游/下游重复叠加可能令尝试数乘法爆炸，需全链路 retry budget 与 circuit breaker。

## 4. 工程实践与设计权衡

**工程案例：**代码检测 Agent 调用限速的扫描 API，遇到 429 按 Retry-After 和 retry budget 排队，最多尝试 4 次；如被拒绝访问某私有库，直接报告权限缺失。扫描结果应与 commit SHA 对齐，不复用之前版本的成功记录。

**失败模式与验证：**多层重试放大流量、按固定间隔形成惊群、误以为 HTTP 200 就代表业务成功、错误分类导致无限调用。统计 retry amplification、p95 latency、重复副作用与错误终止率。

## 5. 关联知识与易混辨析

Retry Policy 是完整决策规则；Exponential Backoff 只是延时算法；Timeout 是单次调用的时长约束；Deadline 是整个任务剩余的时间预算；Recoverable Error 判断是否适合重试。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么全链路要有 retry budget？** 答：多个组件各自重试会乘法放大请求量，诱发下游过载、增加成本和更严重的失败。
2. **问：为什么 jitter 比全体固定 2 秒再试更稳健？** 答：随机分散重试峰值，缓解大量客户端同一时间再次请求造成的惊群。

## 7. 中等难度考试题（含解析）

1. **题：四层服务每层最多重试 2 次（原尝试加 2 次），最坏可能放大多少次底层调用？** 解：3^4=81 次，题设为每一层对下游整个调用都重复。
2. **题：第一次加两次重试，单次成本 0.02 元，最大直接工具成本？** 解：3×0.02=0.06 元，忽略延时与额外操作。

## 8. 权威来源与延伸阅读

- [AWS · Retry with Backoff](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html)：可重试错误、退避与幂等。
- [Azure · Retry Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)：瞬态故障、重试次数和快速失败。
