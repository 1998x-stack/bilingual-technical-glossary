# Recoverable Error（可恢复错误）

> AI Agents · 专题：执行状态、持久化与恢复 · 工程事故防护与可恢复性以业务事实为准

## 1. 核心定义

**Recoverable Error（可恢复错误）**：Recoverable Error（可恢复错误）是暂时性、可纠正或可重新协调的故障，系统可以经过限次重试、状态刷新、人工补充输入或替代路径继续安全完成目标。它与不可恢复的权限拒绝、无效参数和业务规则失败需要明确区分。

**适用边界：**网络 timeout 不自动证明写请求没有执行。若外部转账是否提交未知，系统应先对账；只有幂等操作或明确未执行的动作，才适合按重试策略重发。重复错误也可能从瞬态转为持续故障，应触发停止和告警。

## 2. 形象理解

像资料查询时网络偶尔断线，稍后重新连接可能恢复；但身份证已过期不能靠反复刷新网络解决。

**类比的局限：**所谓‘临时’只是根据证据的分类，若底层服务长期故障，盲重试只会让事故更严重。

## 3. 技术原理与核心内容

分类 error={kind,code,retryable,operation_id,last_attempt,scope}。如 429/503、短期连接失败可限次数指数退避；401/403 通常需重新认证/授权而不是原样重试；输入校验 400 应修正参数。对于异常中断，保持 unknown 并检查外部后置条件；使用最大次数、maxElapsed、deadline 和 circuit_breaker 防止雪崩。重新获得合法输入或凭证后可 resume。

## 4. 工程实践与设计权衡

**工程案例：**企业 Agent 查询库存 API 遇到 503，采用 jitter backoff 最多 3 次；若创建订单返回超时，先按 idempotency_key 查询订单号。权限被拒绝时向授权流程升级，绝不继续尝试绕过身份。

**失败模式与验证：**把任何失败都归类 recoverable、无上限重试、误将付款重复执行、隐瞒恢复期间的数据缺口。以故障注入覆盖限流、权限、参数错误、部分提交与环境切换。

## 5. 关联知识与易混辨析

Recoverable Error 描述能否通过纠正后继续；Retry Policy 定义如何再试；Failover 切换服务或资源；Compensating Action 处理已经产生的副作用。

## 6. 中等难度面试题（含参考答案）

1. **问：HTTP 403 应否自动指数退避重试？** 答：通常不应，以同样凭证会持续拒绝，应核查身份和权限并要求合法授权。
2. **问：订单创建 API timeout 时为什么不能直接当 Recoverable Error 盲重发？** 答：后端可能已创建成功，只是结果未知；需用业务幂等键或订单查询先确认状态。

## 7. 中等难度考试题（含解析）

1. **题：一个 503 请求最多重试 3 次，初始尝试另计，最多会调用多少次？** 解：1+3=4 次。
2. **题：三次 429 后触发错误预算停止，是否还可以无限次快速调用？** 解：不应，应遵守停止/退避和服务端限流策略。

## 8. 权威来源与延伸阅读

- [AWS · Retry with Backoff](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html)：可重试错误、退避与幂等。
- [Azure · Retry Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)：瞬态故障、重试次数和快速失败。
