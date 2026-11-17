# Reserved Instance（预留实例）

> 学科：AI Infrastructure · 专题：成本、能效与资源治理 · 云供给、折扣与中断政策依地区、版本和具体购买协议而变

## 1. 核心定义

预留实例（Reserved Instance，RI）是云服务商面向约定期限、实例属性与覆盖范围提供的实例使用计费优惠机制，常见 AWS EC2 RI 有 1 年或 3 年等承诺选择。必须区分折扣权益和实际容量预留：**AWS Regional RI 提供账单折扣而不保留 AZ 物理容量；Zonal RI 可以在指定 Availability Zone 对匹配实例提供容量预留。** 具体产品/合同和折扣匹配规则因供应商而异。

## 2. 形象理解

像长期购买健身房优惠会员与预定某个固定时段的专属训练房：会员折扣不自动保证随时有空房，指定时段的房间预约才能额外提供容量保障。

## 3. 技术原理与核心内容

AWS RI 购买时选择 region/zonal scope、实例系列/规格、平台、tenancy、期限与付款选项。Regional RI 允许某些 size flexibility 与跨 AZ 折扣覆盖，但不提供容量保证；Zonal RI 在选定 AZ 保留匹配容量但匹配/灵活性更受限。RI 是计费折扣与可选容量保障，不等同资源自动扩缩容、AWS Savings Plans（另有消费承诺匹配模型）或 On-Demand Capacity Reservation（单独容量产品）。长期成本收益与基线利用率、购买数量、提前终止/出售条款及云定价变化有关。

## 4. 工程实践与设计权衡

为稳定在线推理底座、长期训练占用和固定 GPU 节点池规划 RI 时，先将过去 90 天稳态 GPU/CPU 实例用量按 family/region/AZ 统计，避免购买超过长期基线；若确需指定 AZ 的硬容量，则评估 Zonal RI 或独立 Capacity Reservation 能否覆盖所用 GPU instance family。将季节峰值和突发需求留给 On-Demand/Spot/Flex Capacity，结合云账号折扣归属与 chargeback 追踪覆盖率、实际使用率、承诺浪费与迁移风险。不同 GPU 类型在不同云/区域可能不适用于同一种 RI，必须核对可购买性。

## 5. 易混概念与边界

Reserved Instance 不是“买下一台云服务器”或“所有 RI 都保证机器留给你”。Regional RI 仅账单折扣，Zonal RI 才有特定 AZ 容量保留；Savings Plans、Capacity Reservations 与 RI 应按不同契约和技术语义分别讨论。

## 6. 中等难度面试题（含参考答案）

1. **问：购买 AWS Regional RI 是否就能在峰值时保证启动所需 GPU 实例？** 答：不能。Regional RI 不保留容量，只在匹配使用时提供账单折扣；需核对实际 GPU 类别、区域库存及 Zonal RI/Capacity Reservation 方案。

2. **问：为什么不能把全部历史峰值容量都购买成 RI？** 答：峰值可能短暂而基线低，超额承诺造成折扣未使用、规格迁移受限与财务浪费；应按长期稳定用量覆盖，弹性部分另选供给。

## 7. 中等难度考试题（含解析）

1. **题：一个实例按需 12 元/h，某 RI 对匹配使用折后等效 8 元/h，假设 720h 全部匹配且无其它费，单月节省？** 解：`(12−8)×720=**2880 元**`，仅按题设等效价格与匹配小时计算。

2. **题：按订购承诺覆盖 1000 实例小时，但只有 700 小时匹配使用，承诺使用率是多少？** 解：`700/1000=**70%**`，未用的 300 小时不能直接视作可退现金，依合同规则处理。

## 8. 权威来源与延伸阅读

- [AWS Regional and Zonal Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-scope.html)：用于核对供应商容量、计费与中断语义的官方文档。
- [AWS Reserved Instances Overview](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)：用于核对供应商容量、计费与中断语义的官方文档。
- [EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html)：用于核对供应商容量、计费与中断语义的官方文档。

> 所有价格与小时例题为教学假设，非实时云服务报价或财务建议。
