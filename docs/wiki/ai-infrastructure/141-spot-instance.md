# Spot Instance（竞价实例）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 云供给、折扣与中断政策依地区、版本和具体购买协议而变

## 1. 核心定义

竞价实例（Spot Instance）是在云服务商剩余可用计算容量基础上提供通常低于按需价的可中断实例。AWS EC2 Spot 的价格取决于长期供需趋势，若容量回收可由服务商中断实例；AWS 官方提供通常提前 **2 分钟** 的 interruption notice，并可能更早发出 rebalance recommendation。它不等于“低价永远可用”或“抢先占用其它用户预留实例”。

## 2. 形象理解

像航空公司廉价候补座位：价格便宜但航班满员或运营需要时可能失去座位。适合行程可中断且能另行安排的旅客，不适合每次迟到都会造成严重损失的核心任务。

## 3. 技术原理与核心内容

云 Spot 池按 region/AZ、实例类型和可用容量管理，中断可导致终止、停止或休眠（取决于服务商/实例设置）。AWS EC2 中 interruption notice 通常仅提前 2 分钟，并不保证足够完成大型 AI checkpoint；需要从持续 rebalance signals、Job 进度和 checkpoint 策略中提前降低损失。与 On-Demand/Reserved 组合可以使用多实例族、AZ、多池供给与迁移来降低不可用风险。价格折扣与实际可用率应在同一时间窗统计，训练可恢复、批处理任务幂等及数据 checkpoint 是关键前提。

## 4. 工程实践与设计权衡

AI 大模型离线训练可把 Spot 用于能断点续训的部分 worker、预处理 Job、短评测/蒸馏；同步 DDP 一张 worker 被中断时可能影响整个 job，必须支持 elastic orchestration、检查点和快速重调度。在线推理的常驻 SLO 底座宜考虑稳定容量，Spot 只承担可丢弃或可快速迁移的溢出流量；监控 interruption frequency、通知到实际终止间隔、checkpoint 保存耗时、重新下载模型与实例拿不到容量的情况。不能以某次 70% 折扣估算长期 guaranteed TCO。

## 5. 易混概念与边界

Spot 是可中断、折扣型供给模式，不是 Kubernetes Pod priority 的抢占，也不是 On-Demand Capacity Reservation。实例本身被云商回收与集群调度器主动驱逐 Pod 是不同事件，虽然都可能触发 checkpoint 恢复。

## 6. 中等难度面试题（含参考答案）

1. **问：AWS Spot 的 2 分钟中断通知可以保证完成 20 分钟 checkpoint 吗？** 答：不能。2 分钟窗口不足以完成 20 分钟保存；应使用更频繁的增量 checkpoint、复制、rebalance recommendation 或弹性训练，而非依赖最后时刻。

2. **问：为什么多个 AZ/实例类型可改善 Spot 可用性？** 答：不同容量池供需不完全相同，调度器可在部分池容量不足时选择其它池；但区域级故障或统一中断风险仍存在，不能当作绝对独立。

## 7. 中等难度考试题（含解析）

1. **题：按需实例 10 元/GPU-h，Spot 假设在某月平均 3 元/GPU-h，两者价差比例？** 解：`(10−3)/10=**70%**`，仅针对题设期间且不含中断/重算成本。

2. **题：某 Spot 作业每次中断需重算 2GPU-h，每月中断 12 次，单价 3 元/GPU-h，重算直接计算成本？** 解：`2×12×3=**72 元**`，不含额外恢复和等待损失。

## 8. 权威来源与延伸阅读

- [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)：用于核对供应商容量、计费与中断语义的官方文档。
- [How Spot Instances Work](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-spot-instances-work.html)：用于核对供应商容量、计费与中断语义的官方文档。
- [Spot Best Practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html)：用于核对供应商容量、计费与中断语义的官方文档。

> 所有价格与小时例题为教学假设，非实时云服务报价或财务建议。
