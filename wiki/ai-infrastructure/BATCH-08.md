# AI Infrastructure：弹性采购的最后两项决策

> **内部编辑研究路线**。网站仅通过统一 Explorer 的术语详情阅读正文。

## Spot Instance（可中断折扣容量）

阅读 [Spot Instance](141-spot-instance.md)。AWS EC2 Spot 可能因容量回收而中断，通常有约 **2 分钟的 interruption notice**；还可能更早发出 rebalance recommendation。对离线训练需考虑 checkpoint 时长、分布式 rank 一致性、故障重新部署和 Spot 池的多 AZ/机型扩展。**折扣只是价格数据，不能替代可用性保证。**

## Reserved Instance（长期承诺折扣）

阅读 [Reserved Instance](142-reserved-instance.md)。AWS **Regional RI** 通常提供符合条件用量的折扣、**不**保留实际实例容量；**Zonal RI** 在指定可用区保留匹配容量。它们与 Savings Plans、单独的 On-Demand Capacity Reservation 都不是同一产品。

## 对比决策

- 基线常驻推理：先确认 SLO、服务冗余、最低运行规模，再比较 On-Demand、RI 和容量预留；
- 可恢复的离线训练：核算 Spot 中断重算、checkpoint 频率、等待容量、实际单位有效训练产出成本；
- 短期弹性容量：联合 [Autoscaling](140-autoscaling.md)、[Capacity Planning](139-capacity-planning.md) 和承诺覆盖率；
- 所有方案采用相同模型、地区/实例族、有效 token/GPU-hour 与 SLO 边界比较，禁止将一次报价当成未来价格保证。

## 权威资料

- [Amazon EC2 Spot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- [AWS Regional and Zonal RI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-scope.html)
- [AWS Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html)
