# SQL 数据库 · SQL Database

> 中英双语专业术语手册 | Chinese–English SQL Database Glossary

**术语总量：394 条 · 专题：13 类 · 2026 版**

本术语表涵盖 SQL 语法、关系模型、数据类型、查询与连接、聚合与窗口函数、建表约束、索引、优化器、事务并发、日志恢复、数据库运维与数据仓库。

## 专题目录

- 01. 关系数据库与基本概念（28 条）
- 02. SQL 语句与语言分类（28 条）
- 03. 数据类型、NULL 与表达式（35 条）
- 04. 查询子句与条件过滤（33 条）
- 05. 表连接、子查询与集合运算（29 条）
- 06. 聚合分析与窗口函数（28 条）
- 07. 建表、键与完整性约束（27 条）
- 08. 索引与存储结构（29 条）
- 09. 查询优化器与执行计划（30 条）
- 10. 事务、隔离级别与并发控制（35 条）
- 11. 日志、恢复、复制与分布式数据库（33 条）
- 12. 性能、运维、安全与生态（34 条）
- 13. 数据建模、范式与数据仓库（25 条）

---

## 01. 关系数据库与基本概念

*Relational database fundamentals*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Database | 数据库 |  | 按一定结构组织和持久化管理的数据集合。 |
| 2 | Database Management System (DBMS) | 数据库管理系统 | DBMS | 负责存储、查询、事务、权限和恢复的软件。 |
| 3 | Relational Database Management System (RDBMS) | 关系数据库管理系统 | RDBMS | 以关系模型为基础的数据库管理系统。 |
| 4 | Structured Query Language (SQL) | 结构化查询语言 | SQL | 关系数据库中定义、查询和修改数据的语言。 |
| 5 | Relational Model | 关系模型 |  | 以关系及其运算描述数据的理论模型。 |
| 6 | Relation | 关系 |  | 关系模型中的元组集合；实现中通常对应表。 |
| 7 | Table | 表 |  | 由行与列组成的数据对象。 |
| 8 | Row / Record | 行／记录 |  | 表中表示一个实体或事实的一条数据。 |
| 9 | Tuple | 元组 |  | 关系模型中一组属性值组成的元素。 |
| 10 | Column / Field | 列／字段 |  | 表中的命名属性；字段有时也指单个值。 |
| 11 | Attribute | 属性 |  | 关系模型中的列及其含义。 |
| 12 | Domain | 域 |  | 属性允许取值的集合或范围。 |
| 13 | Schema | 模式 |  | 数据库对象及其结构的命名空间或定义。 |
| 14 | Catalog | 目录／系统目录 |  | 保存数据库对象、权限、统计等元数据。 |
| 15 | Metadata | 元数据 |  | 描述表、列、约束及其属性的数据。 |
| 16 | Data Dictionary | 数据字典 |  | 用于管理和查询数据库元数据的集合。 |
| 17 | Instance | 实例 |  | 正在运行的数据库服务及其内存、进程等环境。 |
| 18 | Database Server | 数据库服务器 |  | 提供数据库请求处理的服务端程序或主机。 |
| 19 | Client | 客户端 |  | 向数据库服务发起请求的程序。 |
| 20 | Connection | 连接 |  | 客户端和数据库会话的通信通道。 |
| 21 | Session | 会话 |  | 连接关联的服务器端交互状态。 |
| 22 | Query | 查询 |  | 用于获取或处理数据的请求，常指 SELECT。 |
| 23 | Result Set | 结果集 |  | 查询返回的行与列的集合。 |
| 24 | View | 视图 |  | 由查询定义的逻辑表，通常不单独存储行。 |
| 25 | Materialized View | 物化视图 |  | 持久化存储查询结果、需要按机制刷新的对象。 |
| 26 | Temporary Table | 临时表 |  | 在限定作用域或生命周期内存在的表。 |
| 27 | System Table | 系统表 |  | 数据库内部维护的系统信息表。 |
| 28 | Information Schema | 信息模式 |  | 标准化暴露数据库元数据的一组视图。 |

## 02. SQL 语句与语言分类

*SQL statement families*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Data Definition Language (DDL) | 数据定义语言 | DDL | 用于创建、改变与删除数据库对象的语句类别。 |
| 2 | Data Manipulation Language (DML) | 数据操作语言 | DML | 用于读取或修改表内数据的语句类别；口径可能不同。 |
| 3 | Data Query Language (DQL) | 数据查询语言 | DQL | 教学中常用的 SELECT 分类，非严格独立标准子语言。 |
| 4 | Data Control Language (DCL) | 数据控制语言 | DCL | 用于授予或收回权限的命令类别。 |
| 5 | Transaction Control Language (TCL) | 事务控制语言 | TCL | 用于管理事务边界和保存点的语句类别。 |
| 6 | CREATE | 创建 |  | 创建表、视图、索引或其他数据库对象。 |
| 7 | ALTER | 修改定义 |  | 修改现有对象的结构或属性。 |
| 8 | DROP | 删除对象 |  | 删除数据库对象及其定义。 |
| 9 | TRUNCATE | 截断表 |  | 快速清空表记录；事务与触发器行为依产品而异。 |
| 10 | SELECT | 查询 |  | 从一个或多个数据源获取行与表达式结果。 |
| 11 | INSERT | 插入 |  | 向表写入新行。 |
| 12 | UPDATE | 更新 |  | 修改满足条件的已有行。 |
| 13 | DELETE | 删除行 |  | 移除满足条件的行。 |
| 14 | MERGE | 合并 |  | 基于匹配条件执行插入、更新或删除等动作。 |
| 15 | UPSERT | 存在则更新否则插入 |  | 插入与冲突更新组合的常用统称，语法因产品而异。 |
| 16 | RETURNING | 返回变更行 |  | 部分数据库在数据修改后返回受影响的行或字段。 |
| 17 | GRANT | 授权 |  | 将对象权限或角色授予主体。 |
| 18 | REVOKE | 撤销授权 |  | 撤回先前赋予的权限。 |
| 19 | BEGIN / START TRANSACTION | 开始事务 |  | 显式启动事务边界。 |
| 20 | COMMIT | 提交 |  | 结束事务并使写入按持久性规则生效。 |
| 21 | ROLLBACK | 回滚 |  | 撤销尚未提交的事务更改。 |
| 22 | SAVEPOINT | 保存点 |  | 在事务内部建立可回退的位置。 |
| 23 | EXPLAIN | 解释执行计划 |  | 显示优化器规划的执行步骤。 |
| 24 | ANALYZE / UPDATE STATISTICS | 更新统计信息 |  | 收集优化器用于估算成本和基数的统计数据；语法不同。 |
| 25 | Prepared Statement | 预处理语句 |  | 预先解析／规划并使用参数执行的 SQL。 |
| 26 | Bind Parameter | 绑定参数 |  | 由应用通过驱动传入 SQL 的参数值。 |
| 27 | Stored Procedure | 存储过程 |  | 保存在数据库端供调用的程序化逻辑。 |
| 28 | User-Defined Function (UDF) | 用户自定义函数 | UDF | 扩展数据库表达式或过程能力的函数。 |

## 03. 数据类型、NULL 与表达式

*Types, nulls and expressions*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Data Type | 数据类型 |  | 列或表达式的取值类型及可用运算。 |
| 2 | INTEGER / INT | 整数类型 |  | 存储有符号整数，范围因具体类型和数据库而异。 |
| 3 | BIGINT | 大整数 |  | 通常为 64 位有符号整数类型。 |
| 4 | SMALLINT | 小整数 |  | 通常存储较小范围的有符号整数。 |
| 5 | DECIMAL / NUMERIC | 定点数／精确数值 |  | 以精度和标度定义十进制定点数。 |
| 6 | Precision | 精度 |  | 数值允许的有效数字总位数。 |
| 7 | Scale | 标度 |  | 十进制小数点右侧的位数。 |
| 8 | FLOAT / REAL / DOUBLE PRECISION | 浮点数 |  | 近似数值类型，存在二进制舍入误差。 |
| 9 | CHAR | 定长字符 |  | 长度固定或按定长语义处理的字符类型。 |
| 10 | VARCHAR | 变长字符 |  | 长度可变的字符字符串类型。 |
| 11 | TEXT / CLOB | 大文本 |  | 用于较长文本，具体命名和限制因产品而异。 |
| 12 | BINARY / VARBINARY | 二进制类型 |  | 用于存储字节序列。 |
| 13 | BLOB | 二进制大对象 |  | 用于保存较大的二进制内容。 |
| 14 | BOOLEAN | 布尔类型 |  | 表示真／假；具体存储和支持程度不同。 |
| 15 | DATE | 日期 |  | 仅表示日历日期的类型。 |
| 16 | TIME | 时间 |  | 表示一天中的时间值。 |
| 17 | TIMESTAMP / DATETIME | 时间戳／日期时间 |  | 表示日期和时间，时区语义因类型与产品而异。 |
| 18 | TIMESTAMP WITH TIME ZONE | 带时区时间戳 |  | 表示时间点的类型，具体输出方式因产品而异。 |
| 19 | INTERVAL | 时间间隔 |  | 表示时长或年月日时分秒区间。 |
| 20 | UUID | 通用唯一标识符 |  | 常见的 128 位标识符；是否原生类型因产品而异。 |
| 21 | JSON JSON | 数据类型 |  | 保存 JSON 文档，校验和存储方式不同。 |
| 22 | JSONB | 二进制 |  | JSON PostgreSQL 中用于高效处理的二进制 JSON 表示。 |
| 23 | ARRAY | 数组类型 |  | 允许在单个值中保存同类型元素；并非普遍支持。 |
| 24 | ENUM | 枚举类型 |  | 值限定在预先定义的符号集合内。 |
| 25 | NULL | 空值／未知值标记 |  | 表示缺失或未知，不等于 0 或空字符串。 |
| 26 | Three-Valued Logic (3VL) | 三值逻辑 |  | SQL 谓词结果可以为 TRUE、FALSE、UNKNOWN。 |
| 27 | UNKNOWN | 未知逻辑值 |  | 与 NULL 参与比较等运算时常产生的结果。 |
| 28 | IS NULL / IS NOT NULL | 空值判定 |  | 用于检查值是否为 NULL，不能用 = NULL 替代。 |
| 29 | COALESCE | 取首个非空值 |  | 返回参数中第一个非 NULL 的值。 |
| 30 | NULLIF | 相等则返回空值 |  | 两个参数相等时返回 NULL，否则返回首参。 |
| 31 | CAST | 显式类型转换 |  | 按指定数据类型转换表达式。 |
| 32 | Implicit Cast | 隐式转换 |  | 数据库自动在兼容的数据类型之间转换。 |
| 33 | Collation | 排序规则 |  | 定义字符比较、排序与大小写等语义。 |
| 34 | Character Set | 字符集 |  | 字符与编码之间的映射集合。 |
| 35 | Unicode | 统一码 |  | 跨语言字符编码标准。 |

## 04. 查询子句与条件过滤

*Query clauses and predicates*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Projection | 投影 |  | 选择返回哪些列或表达式。 |
| 2 | Selection | 选择／筛选 |  | 按条件保留符合要求的行。 |
| 3 | FROM | 数据来源子句 |  | 声明查询所读取的表、视图或派生数据源。 |
| 4 | WHERE | 行过滤子句 |  | 对分组之前的数据行执行条件过滤。 |
| 5 | ORDER BY | 排序子句 |  | 指定输出行的排序键与方向。 |
| 6 | GROUP BY | 分组子句 |  | 按指定字段或表达式形成分组。 |
| 7 | HAVING | 分组过滤子句 |  | 对聚合之后的分组应用筛选条件。 |
| 8 | DISTINCT | 去重关键字 |  | 去除投影结果中的重复行。 |
| 9 | ALL | 保留全部 |  | 在特定语法中表示不去重。 |
| 10 | LIMIT | 返回条数上限 |  | 限制输出行数；并非所有数据库使用同一语法。 |
| 11 | OFFSET | 跳过行数 |  | 跳过指定数量的结果行；分页需关注稳定排序。 |
| 12 | FETCH FIRST / NEXT | 提取前若干行 |  | 标准风格的结果行数限制语法。 |
| 13 | TOP | 取前若干行 |  | SQL Server 常用行数限制关键字。 |
| 14 | Alias (AS) | 别名 | AS | 为表或输出表达式指定临时名称。 |
| 15 | Expression | 表达式 |  | 由字面量、列、运算符与函数组合成的值。 |
| 16 | Predicate | 谓词 |  | 计算 TRUE、FALSE 或 UNKNOWN 的判断式。 |
| 17 | Comparison Operator | 比较运算符 |  | 如 =、<>、<、<=、>、>=。 |
| 18 | Logical Operator | 逻辑运算符 |  | AND、OR、NOT 等逻辑组合运算符。 |
| 19 | BETWEEN | 区间判断 |  | 通常包含上下边界，等价于闭区间比较。 |
| 20 | IN | 集合成员判断 |  | 检查是否匹配给定列表或子查询结果。 |
| 21 | LIKE | 模糊匹配 |  | 通过 % 和 _ 通配符匹配字符模式。 |
| 22 | ESCAPE | 转义声明 |  | 指定 LIKE 模式中特殊字符的转义方式。 |
| 23 | REGEXP / SIMILAR TO | 正则／模式匹配 |  | 可选的高级模式匹配方式，语法不同。 |
| 24 | CASE | 条件表达式 |  | 按条件分支计算并返回一个值。 |
| 25 | EXISTS | 存在性判断 |  | 检查子查询是否至少返回一行。 |
| 26 | ANY / SOME | 任一满足 |  | 将比较条件应用于子查询或数组中的任意值。 |
| 27 | ALL (quantifier) | 全部满足 |  | 要求比较条件对集合中的所有值成立。 |
| 28 | Scalar Function | 标量函数 |  | 对输入返回单个值的函数。 |
| 29 | String Function | 字符串函数 |  | 如 LOWER、SUBSTRING、TRIM 等。 |
| 30 | Date/Time Function | 日期时间函数 |  | 用于日期计算、提取和格式化。 |
| 31 | Aggregate Function | 聚合函数 |  | 对一组输入行计算汇总结果。 |
| 32 | Deterministic Function | 确定性函数 |  | 对相同输入总返回相同结果的函数性质。 |
| 33 | Short-Circuit Evaluation | 短路求值 |  | 部分表达式可能跳过求值；不要依赖未保证的执行顺序。 |

## 05. 表连接、子查询与集合运算

*Joins, subqueries and sets*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | JOIN | 连接 |  | 按照指定关系组合多个数据源的行。 |
| 2 | INNER JOIN | 内连接 |  | 只返回符合连接条件的匹配行。 |
| 3 | LEFT OUTER JOIN | 左外连接 |  | 保留左表全部行，未匹配右侧以 NULL 补充。 |
| 4 | RIGHT OUTER JOIN | 右外连接 |  | 保留右表全部行，未匹配左侧以 NULL 补充。 |
| 5 | FULL OUTER JOIN | 全外连接 |  | 保留左右两侧行，未匹配端以 NULL 补充。 |
| 6 | CROSS JOIN | 交叉连接 |  | 生成两个数据源的笛卡儿积。 |
| 7 | SELF JOIN | 自连接 |  | 同一张表通过不同别名与自身连接。 |
| 8 | NATURAL JOIN | 自然连接 |  | 自动用同名列等值连接，模式变化可能改变语义。 |
| 9 | Equi-Join | 等值连接 |  | 连接谓词主要使用相等比较。 |
| 10 | Non-Equi Join | 非等值连接 |  | 使用范围、不等式等条件关联数据。 |
| 11 | Join Condition (ON) | 连接条件 | ON | 定义哪些来自不同输入的行能够匹配。 |
| 12 | USING Clause | 同名列连接子句 |  | 按指定同名列连接，并按规则合并输出列。 |
| 13 | Cartesian Product | 笛卡儿积 |  | 两组行所有可能的配对集合。 |
| 14 | Subquery | 子查询 |  | 嵌套在另一条 SQL 语句内部的查询。 |
| 15 | Scalar Subquery | 标量子查询 |  | 期望返回单行单列的子查询。 |
| 16 | Correlated Subquery | 相关子查询 |  | 引用外层查询列的子查询。 |
| 17 | Derived Table | 派生表 |  | FROM 子句中由子查询产生的临时结果。 |
| 18 | Common Table Expression (CTE) | 公用表表达式 | CTE | WITH 定义的可在单条语句中引用的命名结果。 |
| 19 | WITH RECURSIVE | 递归公用表表达式 |  | 允许递归引用以处理层级或图结构。 |
| 20 | LATERAL | 横向关联子查询 |  | 允许 FROM 子项引用其左侧数据源的列。 |
| 21 | UNION | 并集去重 |  | 组合两个结果并去除重复行。 |
| 22 | UNION ALL | 并集保留重复 |  | 组合结果并保留重复行。 |
| 23 | INTERSECT | 交集 |  | 返回两个结果中共同的行。 |
| 24 | EXCEPT / MINUS | 差集 |  | 返回左侧结果中不属于右侧的行，命名因产品而异。 |
| 25 | Set Operation | 集合运算 |  | UNION、INTERSECT、EXCEPT 等关系组合。 |
| 26 | Semi Join | 半连接 |  | 只保留左侧存在匹配的行，常用于 EXISTS 优化。 |
| 27 | Anti Join | 反连接 |  | 只保留左侧不存在匹配的行，常用于 NOT EXISTS。 |
| 28 | Join Cardinality | 连接结果基数 |  | 连接运算输出的行数。 |
| 29 | Duplicate Row | 重复行 |  | 所考虑列组合完全一致的多条结果记录。 |

## 06. 聚合分析与窗口函数

*Aggregation and window analytics*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | COUNT(*) | 统计行数 |  | 统计输入行数，包含含 NULL 字段的行。 |
| 2 | COUNT(column) | 统计非空值数 |  | 统计指定表达式不为 NULL 的行数。 |
| 3 | COUNT(DISTINCT) | 去重计数 | DISTINCT | 统计不同的非 NULL 值数量。 |
| 4 | SUM | 求和 |  | 计算数值表达式的合计。 |
| 5 | AVG | 平均值 |  | 计算非 NULL 数值的算术平均。 |
| 6 | MIN / MAX | 最小值／最大值 |  | 返回一组值中的最小或最大值。 |
| 7 | STDDEV | 标准差 |  | 常见统计聚合函数；具体变体名称不同。 |
| 8 | GROUPING SETS | 分组集 |  | 在一次查询中表达多种分组组合。 |
| 9 | ROLLUP | 层级汇总 |  | 按分组列层级产生小计与总计。 |
| 10 | CUBE | 立方体汇总 |  | 产生分组列组合的多维汇总。 |
| 11 | GROUPING | 汇总层级标记 |  | 用于区分汇总生成的 NULL 与源数据 NULL。 |
| 12 | Window Function | 窗口函数 |  | 对行的相关窗口计算值，通常保留原行。 |
| 13 | OVER | 窗口子句 |  | 声明窗口函数的分区、排序和帧定义。 |
| 14 | PARTITION BY | 窗口分区 |  | 将结果行划入互不相交的计算分区。 |
| 15 | Window Frame | 窗口帧 |  | 在分区内围绕当前行选取参与计算的行范围。 |
| 16 | ROWS | 按物理行定义帧 |  | 按行偏移描述窗口帧边界。 |
| 17 | RANGE | 按排序值定义帧 |  | 按排序键值或同值组定义窗口帧。 |
| 18 | GROUPS | 按同值组定义帧 |  | 按排序键相同的行组定义窗口帧。 |
| 19 | ROW_NUMBER | 行序号 |  | 按窗口排序给每行分配连续唯一编号。 |
| 20 | RANK | 竞赛排名 |  | 并列值同名次，下一名次存在跳号。 |
| 21 | DENSE_RANK | 密集排名 |  | 并列值同名次，后续名次不跳号。 |
| 22 | NTILE | 分桶编号 |  | 将排序结果分为近似等量的若干桶。 |
| 23 | LAG | 取前序行值 |  | 读取窗口中较前位置的行值。 |
| 24 | LEAD | 取后序行值 |  | 读取窗口中较后位置的行值。 |
| 25 | FIRST_VALUE | 取窗口首值 |  | 返回窗口帧中的第一个值。 |
| 26 | LAST_VALUE | 取窗口末值 |  | 受窗口帧边界影响，未必是分区最后一行。 |
| 27 | Running Total | 累计和 |  | 随排序位置递增累积的汇总值。 |
| 28 | Moving Average | 移动平均 |  | 在滑动窗口内计算平均值。 |

## 07. 建表、键与完整性约束

*Schema design and constraints*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Primary Key (PK) | 主键 | PK | 唯一标识表内一行的一个或多个列。 |
| 2 | Foreign Key (FK) | 外键 | FK | 引用另一表或本表候选键的完整性约束。 |
| 3 | Candidate Key | 候选键 |  | 能够唯一标识行的最小属性集合。 |
| 4 | Composite Key | 复合键 |  | 由多个列共同构成的键。 |
| 5 | Surrogate Key | 代理键 |  | 与业务属性解耦的人造标识符。 |
| 6 | Natural Key | 自然键 |  | 来自业务数据、具有业务含义的键。 |
| 7 | Unique Constraint | 唯一约束 |  | 限制列或列组合不能出现不允许的重复值。 |
| 8 | NOT NULL Constraint | 非空约束 |  | 禁止指定列存储 NULL。 |
| 9 | CHECK Constraint | 检查约束 |  | 要求行满足给定布尔判断条件。 |
| 10 | DEFAULT | 默认值 |  | 插入时未提供列值所使用的预设表达式。 |
| 11 | REFERENCES | 引用声明 |  | 在外键定义中指定被引用目标。 |
| 12 | Referential Integrity | 参照完整性 |  | 保证外键关系满足引用规则。 |
| 13 | ON DELETE CASCADE | 级联删除 |  | 被引用行删除时联动删除相关行。 |
| 14 | ON UPDATE CASCADE | 级联更新 |  | 被引用键更新时联动更新外键。 |
| 15 | RESTRICT / NO ACTION | 限制／延迟拒绝 |  | 约束不满足时拒绝操作；判定时机因产品而异。 |
| 16 | SET NULL / SET DEFAULT | 设空／设默认 |  | 参照操作触发时对外键赋值的策略。 |
| 17 | Generated Column | 生成列 |  | 按表达式从其他数据派生的列。 |
| 18 | Identity Column | 标识列 |  | 由数据库自动生成递增或指定规则的标识值。 |
| 19 | Sequence | 序列 |  | 独立产生数值序列的数据库对象。 |
| 20 | AUTO_INCREMENT | 自增属性 |  | MySQL 常用的自动生成整数标识机制。 |
| 21 | Constraint | 约束 |  | 由数据库执行的数据合法性规则。 |
| 22 | Deferrable Constraint | 可延迟约束 |  | 部分数据库支持在事务结束前再检查约束。 |
| 23 | Trigger | 触发器 |  | 在指定数据事件发生时自动运行的逻辑。 |
| 24 | BEFORE / AFTER Trigger | 前置／后置触发器 |  | 在事件动作之前或之后触发。 |
| 25 | INSTEAD OF Trigger | 替代触发器 |  | 以触发器逻辑替代对视图等对象的直接操作。 |
| 26 | Schema Migration | 模式迁移 |  | 对数据库结构进行版本化变更。 |
| 27 | Backward Compatibility | 向后兼容 |  | 新结构对旧应用或旧查询仍然可用的能力。 |

## 08. 索引与存储结构

*Indexing and physical storage*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Index | 索引 |  | 支持高效定位、排序或过滤数据的辅助结构。 |
| 2 | B-Tree Index B | 树索引 |  | 基于平衡树的通用有序检索索引。 |
| 3 | B+ Tree B+ | 树 |  | 常见数据库索引实现，数据引用主要位于叶节点。 |
| 4 | Hash Index | 哈希索引 |  | 基于哈希的等值查找结构，通常不支持范围排序。 |
| 5 | Clustered Index | 聚簇索引 |  | 决定数据行与索引组织关系的索引机制。 |
| 6 | Secondary Index | 二级索引 |  | 除主要组织索引之外的其他索引。 |
| 7 | Unique Index | 唯一索引 |  | 限制索引键重复的索引，NULL 规则依数据库而异。 |
| 8 | Composite Index | 联合／复合索引 |  | 对多个列共同建立的索引。 |
| 9 | Covering Index | 覆盖索引 |  | 包含查询所需字段，从而减少回表需求。 |
| 10 | Partial Index | 部分索引 |  | 仅为满足谓词的行构建索引。 |
| 11 | Expression Index | 表达式索引 |  | 为函数或表达式计算结果创建索引。 |
| 12 | Functional Index | 函数索引 |  | 以表达式为键的索引，一些系统的命名。 |
| 13 | Descending Index | 降序索引 |  | 以特定降序方式组织索引键。 |
| 14 | Bitmap Index | 位图索引 |  | 利用位集合表示键值与行的关系。 |
| 15 | GIN Index | 广义倒排索引 |  | PostgreSQL 常用于数组、全文与 JSONB 等类型。 |
| 16 | GiST Index | 通用搜索树索引 |  | PostgreSQL 可扩展索引框架。 |
| 17 | BRIN Index | 块范围索引 |  | PostgreSQL 为物理块范围保存摘要信息的索引。 |
| 18 | Full-Text Index | 全文索引 |  | 支持词项检索、相关性搜索的索引。 |
| 19 | Spatial Index | 空间索引 |  | 为几何或地理空间关系加速的索引。 |
| 20 | Heap Table | 堆表 |  | 行存放位置不按某个主索引键的逻辑顺序组织。 |
| 21 | Page / Block | 页／块 |  | 数据库读写及缓存管理的常见基本单位。 |
| 22 | Extent | 区／连续页组 |  | 分配给对象的一组存储页。 |
| 23 | Tablespace | 表空间 |  | 映射逻辑数据库对象与物理存储资源的管理单元。 |
| 24 | Buffer Pool | 缓冲池 |  | 缓存数据页和索引页的内存区域。 |
| 25 | Dirty Page | 脏页 |  | 内存中已修改但尚未写回持久介质的页。 |
| 26 | Page Split | 页分裂 |  | 有序索引页满时为插入腾出空间的结构调整。 |
| 27 | Fill Factor | 填充因子 |  | 控制页目标使用率，预留空间可减少后续页分裂。 |
| 28 | Index Bloat | 索引膨胀 |  | 索引占用空间高于有效数据所需空间的现象。 |
| 29 | Vacuum | 清理／空间回收 |  | PostgreSQL 等数据库用于清理无效行版本的过程。 |

## 09. 查询优化器与执行计划

*Optimizer and execution plans*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Query Parser | 查询解析器 |  | 将 SQL 文本解析为语法结构。 |
| 2 | Abstract Syntax Tree (AST) | 抽象语法树 | AST | 表达 SQL 语法层次关系的树结构。 |
| 3 | Binder / Name Resolver | 绑定器／名称解析器 |  | 将列、表和函数名关联至具体数据库对象。 |
| 4 | Query Planner | 查询规划器 |  | 枚举或生成可行的执行方案。 |
| 5 | Query Optimizer | 查询优化器 |  | 选择预计代价较低的执行计划。 |
| 6 | Cost-Based Optimizer (CBO) | 基于成本的优化器 | CBO | 依赖统计信息和成本模型选择计划。 |
| 7 | Rule-Based Optimization | 基于规则的优化 |  | 依据固定变换与启发式规则改写查询。 |
| 8 | Execution Plan | 执行计划 |  | 查询算子及其运行顺序的表示。 |
| 9 | Plan Node | 计划节点 |  | 执行计划中的单个物理算子。 |
| 10 | Sequential Scan / Table Scan | 顺序扫描／全表扫描 |  | 顺序读取表中数据来检查条件。 |
| 11 | Index Scan | 索引扫描 |  | 利用索引检索满足条件的条目及相关行。 |
| 12 | Index-Only Scan | 仅索引扫描 |  | 尽可能从索引完成查询，具体还可能受可见性检查影响。 |
| 13 | Bitmap Heap Scan | 位图堆扫描 |  | 先用位图记录候选页再读取表页的扫描策略。 |
| 14 | Filter | 过滤算子 |  | 在执行阶段排除不符合条件的行。 |
| 15 | Sort | 排序算子 |  | 按指定键对行排序。 |
| 16 | Hash Aggregate | 哈希聚合 |  | 利用哈希表维护各分组的聚合状态。 |
| 17 | Sort Aggregate | 排序聚合 |  | 利用已排序分组输入完成聚合。 |
| 18 | Nested Loop Join | 嵌套循环连接 |  | 对外侧行重复寻找内侧匹配行。 |
| 19 | Hash Join | 哈希连接 |  | 建立哈希表并探测匹配行的连接算法。 |
| 20 | Merge Join | 归并连接 |  | 利用按连接键排序的输入进行匹配。 |
| 21 | Predicate Pushdown | 谓词下推 |  | 将过滤条件尽量移到靠近数据源的位置。 |
| 22 | Projection Pushdown | 投影下推 |  | 尽早只保留后续需要的列。 |
| 23 | Join Reordering | 连接重排 |  | 改变多表连接顺序以降低预计成本。 |
| 24 | Cardinality Estimation | 基数估计 |  | 预测算子将输出多少行。 |
| 25 | Selectivity | 选择率 |  | 谓词匹配行数占输入行数的比例。 |
| 26 | Histogram | 直方图 |  | 描述列值分布的统计摘要。 |
| 27 | Statistics | 统计信息 |  | 帮助估算行数、分布与成本的数据。 |
| 28 | Plan Cache | 计划缓存 |  | 复用已生成执行计划的缓存机制。 |
| 29 | Parameter Sniffing | 参数嗅探 |  | 基于首轮绑定参数生成计划而影响后续执行的现象。 |
| 30 | EXPLAIN ANALYZE | 实际执行分析 |  | 执行 SQL 并展示实际耗时与行数；注意可能产生副作用。 |

## 10. 事务、隔离级别与并发控制

*Transactions, isolation and concurrency*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Transaction | 事务 |  | 作为一个逻辑单元执行的一组数据库操作。 |
| 2 | Atomicity | 原子性 |  | 事务中的操作要么整体生效，要么整体撤销。 |
| 3 | Consistency | 一致性 |  | 事务将数据库从满足约束的状态转到另一合法状态。 |
| 4 | Isolation | 隔离性 |  | 并发事务之间的可见性与相互影响受到控制。 |
| 5 | Durability | 持久性 |  | 事务成功提交后，其效果按保证持久保存。 |
| 6 | ACID | 事务四特性 |  | Atomicity、Consistency、Isolation、Durability 的缩写。 |
| 7 | Autocommit | 自动提交 |  | 通常在单条语句成功完成后自动提交事务。 |
| 8 | Isolation Level | 隔离级别 |  | 定义并发事务可见性与异常的规则。 |
| 9 | READ UNCOMMITTED | 读未提交 |  | 最低隔离级别，标准允许脏读；具体实现可能更强。 |
| 10 | READ COMMITTED | 读已提交 |  | 不读取未提交修改；同事务多次读取仍可能不同。 |
| 11 | REPEATABLE READ | 可重复读 |  | 同事务重复读取的保证，具体实现差异明显。 |
| 12 | SERIALIZABLE | 可串行化 |  | 并发结果等价于某种串行执行顺序。 |
| 13 | Dirty Read | 脏读 |  | 读取另一事务尚未提交的数据。 |
| 14 | Non-Repeatable Read | 不可重复读 |  | 同事务重复读取同一行得到不同值。 |
| 15 | Phantom Read | 幻读 |  | 同事务相同条件查询出现不同的行集合。 |
| 16 | Lost Update | 丢失更新 |  | 并发写入覆盖而丢失另一事务修改。 |
| 17 | Write Skew | 写偏斜 |  | 并发事务基于相同快照写不同数据而破坏业务约束。 |
| 18 | Serialization Anomaly | 序列化异常 |  | 并发执行结果无法等价于某串行顺序。 |
| 19 | Multi-Version Concurrency Control (MVCC) | 多版本并发控制 | MVCC | 使用行版本与可见性规则支持并发读写。 |
| 20 | Snapshot | 快照 |  | 用于决定某一读取可见哪些数据版本的视图。 |
| 21 | Snapshot Isolation (SI) | 快照隔离 | SI | 事务在一致快照下读取，仍可能发生写偏斜。 |
| 22 | Lock | 锁 |  | 协调多个事务访问共享资源的同步机制。 |
| 23 | Shared Lock (S Lock) | 共享锁 |  | 通常允许并行读取、限制冲突性写入。 |
| 24 | Exclusive Lock (X Lock) | 排他锁 |  | 对资源施加互斥性的更新访问限制。 |
| 25 | Row-Level Lock | 行级锁 |  | 锁定特定数据行的粒度。 |
| 26 | Table-Level Lock | 表级锁 |  | 锁定表级资源的粒度。 |
| 27 | Gap Lock | 间隙锁 |  | 部分数据库锁定索引键之间的间隙以限制插入。 |
| 28 | Next-Key Lock | 临键锁 |  | 在 InnoDB 中结合记录和相邻间隙的锁。 |
| 29 | Optimistic Concurrency Control (OCC) | 乐观并发控制 | OCC | 以冲突检测或版本比对为主的并发策略。 |
| 30 | Pessimistic Locking | 悲观锁策略 |  | 先获取锁再访问或更新冲突数据。 |
| 31 | Deadlock | 死锁 |  | 多个事务相互等待所持资源而无法前进。 |
| 32 | Lock Wait Timeout | 锁等待超时 |  | 等待锁超过设置期限后的终止机制。 |
| 33 | Two-Phase Locking (2PL) | 两阶段锁协议 |  | 锁获取阶段与释放阶段分离的并发控制协议。 |
| 34 | SELECT FOR UPDATE | 选择并加更新锁 |  | 读取目标行并按数据库规则获取更新相关锁。 |
| 35 | Transaction Retry | 事务重试 |  | 遇到冲突或序列化失败后重新执行完整事务。 |

## 11. 日志、恢复、复制与分布式数据库

*Logging, recovery and distribution*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Write-Ahead Logging (WAL) | 预写式日志 | WAL | 先持久记录变更日志再落实相应数据页修改的技术。 |
| 2 | Redo Log | 重做日志 |  | 用于恢复已提交但尚未写入数据页的修改。 |
| 3 | Undo Log | 撤销日志 |  | 用于回滚或支持旧版本读取的变更记录。 |
| 4 | Transaction Log | 事务日志 |  | 记录事务相关操作与状态的日志体系。 |
| 5 | Checkpoint | 检查点 |  | 推进持久化进度、限制恢复需重放日志的范围。 |
| 6 | Crash Recovery | 崩溃恢复 |  | 进程或主机异常终止后恢复一致状态。 |
| 7 | Point-in-Time Recovery (PITR) | 时间点恢复 | PITR | 从备份和日志将数据库恢复到指定时刻。 |
| 8 | Replication | 复制 |  | 将数据库变更从一个节点传播到其他节点。 |
| 9 | Primary / Replica | 主节点／副本节点 |  | 写入源与接收复制结果的节点角色。 |
| 10 | Leader / Follower | 领导者／跟随者 |  | 按复制或共识协议划分的节点角色。 |
| 11 | Synchronous Replication | 同步复制 |  | 提交路径等待约定的副本确认。 |
| 12 | Asynchronous Replication | 异步复制 |  | 主节点提交不必等待全部副本确认。 |
| 13 | Replication Lag | 复制延迟 |  | 副本相对于源节点尚未追赶的进度或时间差。 |
| 14 | Log Shipping | 日志传送 |  | 把日志流持续传递至备用节点。 |
| 15 | Logical Replication | 逻辑复制 |  | 按表、行或逻辑变更事件进行复制。 |
| 16 | Physical Replication | 物理复制 |  | 基于页、块或底层日志记录复制数据库状态。 |
| 17 | Change Data Capture (CDC) | 变更数据捕获 | CDC | 将数据变更持续提取为可消费事件。 |
| 18 | High Availability (HA) | 高可用 | HA | 通过冗余和故障切换提高服务连续性。 |
| 19 | Failover | 故障切换 |  | 在节点故障后将服务职责转移到备用节点。 |
| 20 | Switchover | 计划切换 |  | 在受控条件下主动切换主从角色。 |
| 21 | Read Replica | 只读副本 |  | 主要用于承载读取流量的数据库副本。 |
| 22 | Read-Write Splitting | 读写分离 |  | 将读请求与写请求分配至不同实例。 |
| 23 | Partitioning | 分区 |  | 将一张逻辑表按规则划分为多个物理分区。 |
| 24 | Range Partitioning | 范围分区 |  | 按值域范围将数据分配至分区。 |
| 25 | Hash Partitioning | 哈希分区 |  | 按键的哈希值将数据分布至分区。 |
| 26 | Sharding | 分片 |  | 把数据拆分到多个独立存储或服务节点。 |
| 27 | Distributed Transaction | 分布式事务 |  | 跨多个资源管理器或节点的协同事务。 |
| 28 | Two-Phase Commit (2PC) | 两阶段提交 |  | 协调参与者先准备、后统一提交或回滚的协议。 |
| 29 | Consensus | 共识 |  | 分布式节点对某项状态或决议达成一致。 |
| 30 | Quorum | 法定多数 |  | 足以形成有效读写决议的节点集合阈值。 |
| 31 | CAP Theorem CAP | 定理 |  | 分区发生时无法同时无条件保证强一致与可用性的权衡。 |
| 32 | Eventual Consistency | 最终一致性 |  | 无新变更且通信恢复后，副本最终趋于一致。 |
| 33 | Split-Brain | 脑裂 |  | 多个节点同时认为自己具备主控权的异常状态。 |

## 12. 性能、运维、安全与生态

*Operations, security and ecosystem*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Online Transaction Processing (OLTP) | 联机事务处理 | OLTP | 大量低延迟、短事务读写的工作负载。 |
| 2 | Online Analytical Processing (OLAP) | 联机分析处理 | OLAP | 偏向扫描、聚合与复杂分析的工作负载。 |
| 3 | Query Latency | 查询延迟 |  | 一次查询从发起到完成的耗时。 |
| 4 | Throughput | 吞吐量 |  | 系统单位时间内处理的请求或事务数量。 |
| 5 | Queries per Second (QPS) | 每秒查询数 | QPS | 单位时间内处理的查询请求数。 |
| 6 | Transactions per Second (TPS) | 每秒事务数 | TPS | 单位时间内完成的事务数量。 |
| 7 | Slow Query | 慢查询 |  | 耗时达到监控阈值的 SQL 请求。 |
| 8 | Slow Query Log | 慢查询日志 |  | 用于记录达到阈值的 SQL 语句或执行情况。 |
| 9 | Connection Pool | 连接池 |  | 复用数据库连接并限制并发连接数量的组件。 |
| 10 | Connection Timeout | 连接超时 |  | 建立连接超过等待阈值后的失败机制。 |
| 11 | Statement Timeout | 语句超时 |  | 单条语句执行超过期限后的终止机制。 |
| 12 | Query Cancellation | 查询取消 |  | 主动中止正在运行的查询。 |
| 13 | Backup | 备份 |  | 保存可用于恢复的数据库数据副本。 |
| 14 | Full Backup | 全量备份 |  | 保存完整受保护数据集的备份。 |
| 15 | Incremental Backup | 增量备份 |  | 只记录相对指定基线新发生的变更。 |
| 16 | Differential Backup | 差异备份 |  | 记录自最近全量备份以来发生的变更。 |
| 17 | Restore | 还原 |  | 使用备份材料重新构建数据库内容。 |
| 18 | Recovery Point Objective (RPO) | 恢复点目标 | RPO | 故障后业务可接受的最大数据丢失时间范围。 |
| 19 | Recovery Time Objective (RTO) | 恢复时间目标 | RTO | 业务可接受的最长恢复服务时间。 |
| 20 | Authentication | 身份认证 |  | 验证连接主体身份的过程。 |
| 21 | Authorization | 权限控制／授权 |  | 确定某主体允许执行哪些操作。 |
| 22 | Role | 角色 |  | 可被授予权限并分配给用户的权限集合或主体。 |
| 23 | Principle of Least Privilege | 最小权限原则 |  | 只赋予完成任务所必需的最小权限。 |
| 24 | SQL Injection SQL | 注入 |  | 将恶意输入拼进 SQL 而改变执行含义的漏洞。 |
| 25 | Parameterized Query | 参数化查询 |  | 将 SQL 结构与用户输入值分离以降低注入风险。 |
| 26 | TLS Encryption TLS | 传输加密 |  | 保护客户端与数据库之间的通信。 |
| 27 | Encryption at Rest | 静态数据加密 |  | 对存储介质上的数据库数据或备份进行加密。 |
| 28 | Audit Log | 审计日志 |  | 记录访问、权限及关键操作的追踪信息。 |
| 29 | Database Driver | 数据库驱动 |  | 应用访问数据库的连接与协议适配软件。 |
| 30 | Open Database Connectivity (ODBC) | 开放数据库互连 | ODBC | 通用的数据库访问接口规范。 |
| 31 | Java Database Connectivity (JDBC) Java | 数据库连接接口 |  | Java 平台常用数据库访问 API。 |
| 32 | Object-Relational Mapping (ORM) | 对象关系映射 | ORM | 把应用对象映射为关系表与查询的技术。 |
| 33 | SQL Dialect SQL | 方言 |  | 各数据库产品对 SQL 标准的扩展与差异。 |
| 34 | Portability | 可移植性 |  | SQL 或应用跨不同数据库产品迁移的难易程度。 |

## 13. 数据建模、范式与数据仓库

*Modeling and data warehousing*

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Entity | 实体 |  | 需要在数据库中表示的业务对象或概念。 |
| 2 | Entity-Relationship Model (ER Model) | 实体关系模型 |  | 用实体、属性和联系进行概念建模。 |
| 3 | Entity-Relationship Diagram (ERD) | 实体关系图 | ERD | 可视化表示实体及其关系的图。 |
| 4 | One-to-One (1:1) | 一对一关系 |  | 一个实体至多对应另一个实体的一条记录。 |
| 5 | One-to-Many (1:N) | 一对多关系 |  | 一个实体可关联另一实体的多条记录。 |
| 6 | Many-to-Many (M:N) | 多对多关系 |  | 两侧实体均可与对侧多条记录关联。 |
| 7 | Junction Table | 关联表／连接表 |  | 通过外键实现多对多关系的中间表。 |
| 8 | Normalization | 规范化 |  | 依据函数依赖等规则减少冗余和更新异常。 |
| 9 | Denormalization | 反规范化 |  | 为查询性能等目的有意识引入冗余数据。 |
| 10 | First Normal Form (1NF) | 第一范式 |  | 要求属性值满足所采用关系模型的原子性约定。 |
| 11 | Second Normal Form (2NF) | 第二范式 |  | 在 1NF 基础上排除非主属性对候选键的部分依赖。 |
| 12 | Third Normal Form (3NF) | 第三范式 |  | 控制非主属性通过非键属性产生的传递依赖。 |
| 13 | Boyce-Codd Normal Form (BCNF) BC | 范式 |  | 要求每个非平凡函数依赖的决定因素都是超键。 |
| 14 | Functional Dependency | 函数依赖 |  | 给定一组属性值可确定另一组属性值的关系。 |
| 15 | Update Anomaly | 更新异常 |  | 冗余导致更新时可能发生的不一致。 |
| 16 | Star Schema | 星型模式 |  | 事实表连接若干维度表的分析数据模型。 |
| 17 | Snowflake Schema | 雪花模式 |  | 维度进一步规范化为层级表的数据模型。 |
| 18 | Fact Table | 事实表 |  | 保存业务事件、度量值与维度键的表。 |
| 19 | Dimension Table | 维度表 |  | 描述事实的业务维度和属性的表。 |
| 20 | Slowly Changing Dimension (SCD) | 缓慢变化维 | SCD | 管理维度属性随时间变化的建模方法。 |
| 21 | ETL | 抽取－转换－加载 |  | 先变换再将数据加载到目标系统的数据流程。 |
| 22 | ELT | 抽取－加载－转换 |  | 先加载到目标系统再执行数据变换的流程。 |
| 23 | Data Warehouse | 数据仓库 |  | 服务分析与决策的集成型历史数据系统。 |
| 24 | Data Mart | 数据集市 |  | 面向某业务主题或团队的分析数据子集。 |
| 25 | Columnar Storage | 列式存储 |  | 按列组织数据，适合某些分析扫描与压缩场景。 |


## 使用注意

- SQL 标准和各产品方言在功能与语法上存在差异；以实际 PostgreSQL、MySQL、SQLite、SQL Server、Oracle 等版本的官方文档为准。
- 三值逻辑、NULL 处理、事务隔离和索引可用性等概念不可直接用单一数据库实现替代通用定义。
- 本术语表为学习与工程查阅资料，不是 SQL 标准官方术语规范。

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/sql-database.pdf)

