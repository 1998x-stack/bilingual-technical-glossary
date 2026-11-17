# Data Pipeline（数据管道）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 数据读写、缓存和负载口径需明确环境及版本

## 1. 核心定义

数据管道（Data Pipeline）是从源系统采集、验证、转换、传输、存储到下游消费的数据处理流程及其依赖关系。它既可以按 batch 调度，也可以按事件或流式持续运行；关键不只是组件连接，而是明确输入/输出数据契约、幂等性、错误恢复、质量与可重放性。

## 2. 形象理解

像一条质量受控的流水线：材料进入后经过清洗、分类、验收和打包，任一道工序失败需要知道从哪里安全重做。单纯把材料从甲地运到乙地不保证输出产品正确。

## 3. 技术原理与核心内容

把处理过程建成任务 DAG：采集 → schema/PII 校验 → 规范化 → 去重 → 分片 → 写出 manifest → 通知训练器。批式编排可用 Airflow DAG task 与依赖触发；流式语义需要考虑 event time、watermark、late events、checkpoint 和 sink commit。At-least-once delivery 可产生重复，exactly-once 结果通常由事务性 sink、幂等写入和端到端重放协议共同实现，不可仅根据消息中间件宣传语断言。数据 lineage 记录输入来源、处理版本、输出快照和质量检验。

## 4. 工程实践与设计权衡

训练流水线先固定数据版本、转换代码 SHA、schema、去重策略和样本排序种子；中间过程输出到带临时 key 的新分区，验证后原子发布 manifest。统计每步吞吐、失败重试、积压年龄、坏记录率、重复样本数、上游到下游延迟及成本。大规模样本生成需支持断点续跑、坏分片隔离、限速与访问权限，避免局部成功导致下游读取半成品。

## 5. 易混概念与边界

Data Pipeline 是端到端过程，Data Loader 是训练进程把已准备数据送入模型的组件。ETL 先变换再加载，ELT 先落原始数据后变换；编排器决定执行顺序，不自动提供跨系统 exactly-once。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 at-least-once 重试时必须让 sink 幂等？** 答：网络重试或 worker 崩溃可能重复发送同一记录，若 sink 每次追加没有去重/事务键就会重复样本；应采用稳定 event ID、upsert 或事务提交并记录 checkpoint。

2. **问：如何保证多机训练只读取同一版清洗数据？** 答：在所有转换和质量检查完成后发布不可变 dataset manifest 或 table snapshot，并将版本 ID 写入训练作业配置；避免运行期间直接 list 可变原始目录。

## 7. 中等难度考试题（含解析）

1. **题：管道每天输入 12TiB，质量过滤剔除 15%，输出多少 TiB？** 解：`12×0.85=**10.2TiB**`，忽略压缩改变数据字节数。

2. **题：有 8 个阶段每阶段独立成功率 99.5%，假定一次执行不重试且相互独立，整条流水线成功率约多少？** 解：`0.995^8≈**96.07%**`；这是独立性教学假设，生产失败往往有关联。

## 8. 权威来源与延伸阅读

- [Apache Airflow DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html)：用于核对资料机制、测量定义与实现约束的资料。
- [Apache Flink Checkpoints](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/fault-tolerance/checkpointing/)：用于核对资料机制、测量定义与实现约束的资料。
- [Apache Iceberg table snapshots](https://iceberg.apache.org/docs/latest/)：用于核对资料机制、测量定义与实现约束的资料。

> 示例计算使用明确的理想条件，不等于某个生产系统的实测结果。
