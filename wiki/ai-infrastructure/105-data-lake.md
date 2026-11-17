# Data Lake（数据湖）

> 学科：AI Infrastructure · 专题：存储与数据管道 · 协议与性能口径以官方版本及实测边界为准

## 1. 核心定义

数据湖（Data Lake）是一种集中保留结构化、半结构化与非结构化数据的架构，通常使用可扩展对象存储为主要数据层，结合元数据 catalog、权限治理、数据质量、格式/表管理和计算引擎。原始数据可以先落地再解释 schema，但“任何文件丢进 bucket”并不足以构成可治理的数据湖。

## 2. 形象理解

像城市公共资料档案馆：有原始档案区、清洗修订区、可供分析的标准资料区，还有目录、权限和出处记录。若只堆放文件而没有索引、版本和所有权，档案馆会退化成难以使用的数据沼泽。

## 3. 技术原理与核心内容

典型架构把 raw/landing、processed、curated 分层，使用对象 key+manifest/table metadata 映射物理文件与逻辑数据集。Parquet/ORC 通过列存压缩和 predicate pushdown 提高查询效率；Iceberg/Delta Lake/Hudi 等表格式在对象存储之上提供事务元数据和 snapshot 管理，但其具体一致性由 catalog、commit 协议与实现决定。数据发现通过 catalog、lineage、classification 与 schema registry；敏感数据必须按租户和用途控制访问。

## 4. 工程实践与设计权衡

AI 训练语料入湖需保留来源、许可证、PII 处理、去重、质量分数与数据集版本，固定 train/validation/test split 的 manifest，避免数据泄漏。对数百 TB 数据采用 partition pruning、列式格式、压缩和合适的对象 shard 尺寸，分析小文件合并成本、list/request 费用与跨区搬运。模型训练应从一个已签名/可复现的快照读取，不跟随不断变化的 raw bucket。

## 5. 易混概念与边界

Data Lake 是数据架构而非具体产品，S3 是存储服务，Spark/Trino 是计算引擎，Iceberg 是表格式。与传统 warehouse 相比，数据湖通常保留更丰富的原始格式；lakehouse 通过表层补齐治理与事务能力，两者边界取决于实施。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么只建立一个 S3 bucket 不能称为成熟数据湖？** 答：缺少 catalog、schema/版本、权限、来源、质量和生命周期管理时无法稳定发现、审计或重复计算；原始存储只是基础层。

2. **问：训练集为何要绑定不可变 manifest 或 table snapshot？** 答：防止多机在不同时间读到变化的对象列表、样本重复/缺失与训练数据难以复现；需要固定输入、分片、顺序/种子和数据质量版本。

## 7. 中等难度考试题（含解析）

1. **题：原始数据 100TiB，经清洗剔除 30%，curated 层剩余多少 TiB？** 解：`100×(1−0.30)=**70TiB**`，不包含压缩/格式转换造成的额外变化。

2. **题：有 2400 个等大小对象，按日期分区后查询只命中 10%，并假设完美 partition pruning，理论读取对象数？** 解：`2400×0.10=**240 个**`，实际还受文件统计和分区布局影响。

## 8. 权威来源与延伸阅读

- [AWS S3 Data Lakes architecture](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/s3-data-lakes.html)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/)：用于核对上述协议、性能口径或数据管理机制的一手资料。
- [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)：用于核对上述协议、性能口径或数据管理机制的一手资料。

> 数值示例均为题设下的简化计算，不是生产集群的真实性能指标。
