# 数据结构专有名词中英文对照表

> **Bilingual Glossary of Data Structures**  
> 版本：2026-11-16 ｜ 共 **352** 条术语，**14** 个主题。

本表面向数据结构学习、算法题阅读、技术面试与工程实现，采用常见中文译法；不同教材和语境中的译名可能有所不同。

## 目录

- [01 基础概念与抽象](#section-01)（28 条）
- [02 复杂度与存储布局](#section-02)（27 条）
- [03 数组、序列与矩阵](#section-03)（28 条）
- [04 链表与指针结构](#section-04)（19 条）
- [05 栈、队列与双端队列](#section-05)（23 条）
- [06 哈希表与映射](#section-06)（27 条）
- [07 树与遍历](#section-07)（30 条）
- [08 搜索树与平衡树](#section-08)（26 条）
- [09 堆与优先队列](#section-09)（19 条）
- [10 图的表示与属性](#section-10)（30 条）
- [11 图结构算法与连通性](#section-11)（25 条）
- [12 并查集与区间查询](#section-12)（22 条）
- [13 字符串、字典树与索引](#section-13)（23 条）
- [14 概率型、外存与并发结构](#section-14)（25 条）
- [易混淆概念对照](#confusions)

<a id="section-01"></a>
## 01 · 基础概念与抽象 / Core Concepts & Abstractions

从抽象数据类型、逻辑结构到基本操作，建立统一术语体系。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Data Structure | 数据结构 | 组织、存储和访问数据的方式及相应操作。 |
| Abstract Data Type (ADT) | 抽象数据类型 | 只规定数据与操作的语义，不限定实现细节。 |
| Data Type | 数据类型 | 值的集合及可执行操作的约束。 |
| Primitive Type | 基本类型 | 语言直接提供的基本数据类型，如整数与布尔值。 |
| Composite Type | 复合类型 | 由多个值或类型组合形成的类型。 |
| Container | 容器 | 保存与组织一组元素的对象或结构。 |
| Collection | 集合容器 | 一组元素及其访问、修改操作的统称。 |
| Element | 元素 | 数据结构中存储的一个数据项。 |
| Node | 节点 | 具有数据字段和可能的链接字段的基本单元。 |
| Key | 键 | 用于标识、检索或比较记录的字段。 |
| Value | 值 | 与键关联或作为容器成员的数据。 |
| Record | 记录 | 由若干字段构成的一条结构化数据。 |
| Entry | 条目 | 容器中的键值对或单个存储项。 |
| Index | 索引 | 指向元素位置或支持快速检索的辅助结构。 |
| Reference | 引用 | 用于间接访问对象的标识或关联。 |
| Pointer | 指针 | 保存内存地址或等价位置标识的值。 |
| Null Pointer | 空指针 | 表示不指向有效对象或节点的指针。 |
| Sentinel | 哨兵 | 简化边界判断的特殊标记或节点。 |
| Invariant | 不变量 | 在结构操作前后必须持续成立的性质。 |
| Mutable Structure | 可变数据结构 | 创建后可原地修改元素或链接的结构。 |
| Immutable Structure | 不可变数据结构 | 构建后不改变既有实例状态的结构。 |
| Persistent Data Structure | 持久化数据结构 | 更新时保留旧版本，并生成可访问的新版本。 |
| Ephemeral Data Structure | 非持久化数据结构 | 更新通常覆盖当前版本，不保留历史版本。 |
| Interface | 接口 | 向外提供的一组操作与使用约定。 |
| Implementation | 实现 | 将抽象操作映射到具体存储布局和算法。 |
| Traversal | 遍历 | 依照特定次序访问结构中的各元素。 |
| Iteration | 迭代 | 按序逐次取得元素或执行重复操作。 |
| Iterator | 迭代器 | 用于逐项访问容器元素的对象或协议。 |

<a id="section-02"></a>
## 02 · 复杂度与存储布局 / Complexity & Memory Layout

理解术语在性能分析、内存组织和实现取舍中的作用。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Time Complexity | 时间复杂度 | 描述输入规模增长时操作时间的渐近变化。 |
| Space Complexity | 空间复杂度 | 描述输入规模增长时所需空间的渐近变化。 |
| Big O Notation | 大 O 记号 | 表示函数增长率的渐近上界。 |
| Big Omega Notation | 大 Ω 记号 | 表示函数增长率的渐近下界。 |
| Big Theta Notation | 大 Θ 记号 | 表示函数增长率的渐近紧确界。 |
| Worst-case Complexity | 最坏情况复杂度 | 在最不利输入下的资源消耗上界。 |
| Average-case Complexity | 平均情况复杂度 | 给定输入分布下的期望资源消耗。 |
| Amortized Analysis | 均摊分析 | 将一系列操作的总成本分摊到单次操作。 |
| Amortized Complexity | 均摊复杂度 | 序列操作中平均分摊到每次的代价上界。 |
| Auxiliary Space | 辅助空间 | 除输入与输出数据本身以外的额外空间。 |
| Memory Footprint | 内存占用 | 数据结构及相关元数据消耗的存储空间。 |
| Contiguous Memory | 连续内存 | 数据元素占据相邻的内存地址区间。 |
| Non-contiguous Memory | 非连续内存 | 元素可散布在不同地址并通过链接关联。 |
| Random Access | 随机访问 | 能够直接通过位置标识访问任意元素。 |
| Sequential Access | 顺序访问 | 通常沿既定顺序逐个访问元素。 |
| Cache Locality | 缓存局部性 | 访问数据时倾向重复访问附近或近期的位置。 |
| Spatial Locality | 空间局部性 | 程序倾向访问地址相邻的存储位置。 |
| Temporal Locality | 时间局部性 | 程序倾向短期内重复访问同一数据。 |
| Memory Allocation | 内存分配 | 为元素或节点申请可用内存空间。 |
| Dynamic Allocation | 动态分配 | 运行期间按需申请与释放内存。 |
| Fragmentation | 内存碎片 | 空闲空间被分割，降低有效利用或分配效率。 |
| Capacity | 容量 | 容器当前无需扩容即可容纳的元素上限。 |
| Size | 大小 | 容器当前实际包含的元素个数。 |
| Load Factor | 负载因子 | 已存储元素数与桶数等容量指标的比值。 |
| Resize | 调整容量 | 改变底层可容纳元素数量的操作。 |
| Reallocation | 重新分配 | 申请新的存储区域并可能搬移既有元素。 |
| Memory Alignment | 内存对齐 | 按特定地址边界布置对象以满足平台要求。 |

<a id="section-03"></a>
## 03 · 数组、序列与矩阵 / Arrays, Sequences & Matrices

掌握连续存储、索引、动态扩容及多维表示的核心词汇。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Array | 数组 | 按索引访问、通常在连续存储区排列的同类型元素序列。 |
| Static Array | 静态数组 | 长度在创建后固定的数组。 |
| Dynamic Array | 动态数组 | 容量可通过重新分配等方式增长的数组。 |
| Resizable Array | 可调整大小数组 | 支持运行时扩容或缩容的数组实现。 |
| Array List | 数组列表 | 基于动态数组实现的列表容器名称。 |
| Sequence | 序列 | 元素按明确次序组织的抽象集合。 |
| List | 列表 | 支持按位置访问或插入删除的有序集合抽象。 |
| Indexing | 索引访问 | 使用位置编号定位元素。 |
| Zero-based Indexing | 从零开始的索引 | 首元素下标为零的索引约定。 |
| Subarray | 子数组 | 原数组中一段连续的元素区间。 |
| Slice | 切片 | 从序列中选择连续区间或按步长抽取元素。 |
| View | 视图 | 共享底层数据、提供不同访问方式的表示。 |
| Array Copy | 数组复制 | 将数组内容复制到另一存储区域。 |
| In-place Operation | 原地操作 | 主要在原有数据区域中完成修改。 |
| Append | 尾部追加 | 在序列末端加入一个元素。 |
| Insert | 插入 | 在指定位置加入元素并维护次序。 |
| Delete | 删除 | 移除指定位置或满足条件的元素。 |
| Shift | 移位 | 为插入、删除或重排移动元素位置。 |
| Circular Array | 循环数组 | 将固定数组下标按模运算首尾衔接使用。 |
| Multidimensional Array | 多维数组 | 使用多个下标表示元素位置的数组。 |
| Matrix | 矩阵 | 按行和列组织元素的二维数据结构。 |
| Row-major Order | 行主序 | 同一行的元素在内存中相邻排列的存储次序。 |
| Column-major Order | 列主序 | 同一列的元素在内存中相邻排列的存储次序。 |
| Stride | 步长 | 跨越某个数组维度一个索引单位时的内存偏移量。 |
| Sparse Matrix | 稀疏矩阵 | 绝大多数元素为零或缺省值的矩阵。 |
| Dense Matrix | 稠密矩阵 | 通常显式存储大部分位置元素的矩阵。 |
| Compressed Sparse Row (CSR) | 压缩稀疏行格式 | 以行指针、列索引和值表示稀疏矩阵。 |
| Compressed Sparse Column (CSC) | 压缩稀疏列格式 | 以列指针、行索引和值表示稀疏矩阵。 |

<a id="section-04"></a>
## 04 · 链表与指针结构 / Linked Lists & Pointer Structures

区分单链、双链、循环链表及常见节点操作。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Linked List | 链表 | 通过节点间链接组织的线性数据结构。 |
| Singly Linked List | 单向链表 | 每个节点通常仅保存后继节点链接的链表。 |
| Doubly Linked List | 双向链表 | 节点同时保存前驱与后继链接的链表。 |
| Circular Linked List | 循环链表 | 尾节点链接回某个起始节点的链表。 |
| Circular Doubly Linked List | 循环双向链表 | 前驱和后继关系均首尾闭合的双向链表。 |
| Head Node | 头节点 | 链表起始位置的节点；有时专指虚拟头节点。 |
| Tail Node | 尾节点 | 链表末端的节点。 |
| Dummy Head | 虚拟头节点 | 不承载普通业务元素、用于简化边界操作的节点。 |
| Next Pointer | 后继指针 | 指向下一个节点的链接。 |
| Previous Pointer | 前驱指针 | 指向上一个节点的链接。 |
| Predecessor | 前驱 | 在指定顺序中位于目标元素之前的元素。 |
| Successor | 后继 | 在指定顺序中位于目标元素之后的元素。 |
| List Reversal | 链表反转 | 将链表节点的链接方向或次序反转。 |
| List Splicing | 链表拼接 | 通过调整链接合并或移动一段链表。 |
| Cycle Detection | 环检测 | 判断链表中是否存在可重复到达的节点。 |
| Fast and Slow Pointers | 快慢指针 | 使用不同移动速度的指针完成检测或定位。 |
| Skip List | 跳表 | 通过多层有序链接实现期望对数级查找的结构。 |
| Unrolled Linked List | 分块链表 | 每个节点存储多个连续元素的链表变体。 |
| Intrusive Linked List | 侵入式链表 | 将链接字段直接放入被管理对象的链表。 |

<a id="section-05"></a>
## 05 · 栈、队列与双端队列 / Stacks, Queues & Deques

理解 LIFO、FIFO、双端操作以及实际工程中的队列变体。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Stack | 栈 | 遵循后进先出次序的线性容器。 |
| Last In, First Out (LIFO) | 后进先出 | 最后加入的元素最先被取出。 |
| Push | 入栈 | 向栈顶加入元素。 |
| Pop | 出栈 | 从栈顶移除并通常返回元素。 |
| Peek / Top | 查看栈顶 | 读取栈顶元素但不移除。 |
| Stack Overflow | 栈溢出 | 栈空间超出允许容量或调用栈限制。 |
| Stack Underflow | 栈下溢 | 在空栈上执行非法弹出等操作。 |
| Monotonic Stack | 单调栈 | 保持元素按单调关系排列的栈。 |
| Call Stack | 调用栈 | 保存函数调用帧和返回信息的运行时栈。 |
| Queue | 队列 | 通常遵循先进先出次序的线性容器。 |
| First In, First Out (FIFO) | 先进先出 | 最先加入的元素最先被取出。 |
| Enqueue | 入队 | 向队列尾端加入元素。 |
| Dequeue | 出队 | 从队列头端移除并通常返回元素。 |
| Front | 队首 | 队列中下一次通常被取出的元素位置。 |
| Rear / Back | 队尾 | 队列中通常执行追加的位置。 |
| Circular Queue | 循环队列 | 用环形下标复用固定缓冲区的队列。 |
| Deque (Double-ended Queue) | 双端队列 | 支持在首尾两端插入和删除的容器。 |
| Monotonic Queue | 单调队列 | 保持候选值单调，用于窗口极值等查询。 |
| Blocking Queue | 阻塞队列 | 在空或满等条件下可使操作等待的并发队列。 |
| Bounded Queue | 有界队列 | 最多容纳预设数量元素的队列。 |
| Unbounded Queue | 无界队列 | 不规定固定元素上限的队列抽象。 |
| Ring Buffer | 环形缓冲区 | 在固定空间内循环复用读写位置的缓冲结构。 |
| Producer–Consumer Queue | 生产者—消费者队列 | 在生产任务和消费任务间传递元素的队列。 |

<a id="section-06"></a>
## 06 · 哈希表与映射 / Hash Tables & Maps

覆盖哈希函数、冲突处理、哈希容器和探测策略。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Hash Table | 哈希表 | 通过哈希函数把键映射到桶或槽位的结构。 |
| Hash Map | 哈希映射 | 使用哈希表实现键到值映射的容器。 |
| Hash Set | 哈希集合 | 基于哈希表实现的去重元素集合。 |
| Map / Dictionary | 映射／字典 | 保存键值关联并支持按键查找的抽象类型。 |
| Set | 集合 | 不包含重复元素的抽象容器。 |
| Multiset | 多重集合 | 允许同一元素出现多次的集合抽象。 |
| Multimap | 多重映射 | 允许一个键对应多个值的映射抽象。 |
| Hash Function | 哈希函数 | 将输入键转换为固定范围摘要或索引的函数。 |
| Hash Value | 哈希值 | 哈希函数计算得到的摘要或数值。 |
| Hash Code | 哈希码 | 对象或键用于哈希分桶的整数等表示。 |
| Bucket | 桶 | 哈希表中负责容纳一个或多个条目的位置或分组。 |
| Slot | 槽位 | 底层表中可放置条目的单个位置。 |
| Hash Collision | 哈希冲突 | 不同键映射到同一桶或槽位的情形。 |
| Collision Resolution | 冲突解决 | 在碰撞发生时仍能正确存储和查找键的方法。 |
| Separate Chaining | 链地址法 | 将同桶碰撞项放入链表或其他次级容器。 |
| Open Addressing | 开放寻址法 | 通过探测表中其他槽位解决碰撞。 |
| Linear Probing | 线性探测 | 碰撞后依次检查相邻候选槽位。 |
| Quadratic Probing | 二次探测 | 以二次函数决定探测位移的策略。 |
| Double Hashing | 双重哈希 | 使用第二个哈希函数确定探测步长。 |
| Robin Hood Hashing | 罗宾汉哈希 | 通过平衡探测距离减少较长探测链的策略。 |
| Cuckoo Hashing | 布谷鸟哈希 | 在多个候选位置之间搬移键以处理冲突。 |
| Tombstone | 删除标记 | 开放寻址表中用于标识已删除槽位的标记。 |
| Rehashing | 重新哈希 | 改变容量或布局时重新安排各键的位置。 |
| Hash Flooding | 哈希洪泛 | 大量冲突导致哈希结构性能下降的情形。 |
| Perfect Hashing | 完美哈希 | 针对给定静态键集实现无碰撞映射的方法。 |
| Minimal Perfect Hash | 最小完美哈希 | 将 n 个固定键无碰撞映射到 n 个槽位。 |
| Ordered Map | 有序映射 | 按键顺序或插入顺序维持确定迭代次序的映射。 |

<a id="section-07"></a>
## 07 · 树与遍历 / Trees & Traversals

从节点关系、树的形态到深度优先与层序遍历。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Tree | 树 | 由节点和无环的层次连接关系组成的结构。 |
| Rooted Tree | 有根树 | 指定一个根节点以定义父子关系的树。 |
| Root | 根节点 | 有根树中没有父节点的起始节点。 |
| Parent Node | 父节点 | 树中直接连接到某个子节点上方的节点。 |
| Child Node | 子节点 | 由某个父节点直接连接的下层节点。 |
| Sibling Nodes | 兄弟节点 | 拥有相同父节点的节点。 |
| Leaf Node | 叶子节点 | 没有子节点的节点。 |
| Internal Node | 内部节点 | 至少拥有一个子节点的节点。 |
| Ancestor | 祖先节点 | 沿父指针不断向上可以到达的节点。 |
| Descendant | 后代节点 | 沿子指针向下可以到达的节点。 |
| Subtree | 子树 | 由某节点及其所有后代构成的树。 |
| Forest | 森林 | 若干互不相交的树的集合。 |
| Degree of a Node | 节点的度 | 节点直接拥有的子节点数（有根树语境）。 |
| Depth of a Node | 节点深度 | 从根到该节点的边数。 |
| Height of a Node | 节点高度 | 从该节点到最深叶节点的最长边数。 |
| Height of a Tree | 树高 | 根节点的高度；空树约定因实现而异。 |
| Level | 层 | 依据根到节点距离划分的层级；起始层编号依约定。 |
| Binary Tree | 二叉树 | 每个节点最多有左右两个子节点的树。 |
| Full Binary Tree | 严格二叉树／真二叉树 | 每个节点的子节点数只能是零或二的二叉树。 |
| Perfect Binary Tree | 满二叉树／完美二叉树 | 全部内部节点有两个子节点且叶子在同一层。 |
| Complete Binary Tree | 完全二叉树 | 除末层外各层已满，末层节点从左向右排列。 |
| Skewed Tree | 斜树 | 绝大多数节点只有单侧子节点的退化树。 |
| Tree Traversal | 树遍历 | 按指定顺序访问树中全部节点。 |
| Preorder Traversal | 前序遍历 | 按根、左子树、右子树的顺序访问二叉树。 |
| Inorder Traversal | 中序遍历 | 按左子树、根、右子树的顺序访问二叉树。 |
| Postorder Traversal | 后序遍历 | 按左子树、右子树、根的顺序访问二叉树。 |
| Level-order Traversal | 层序遍历 | 从上到下逐层访问节点，通常借助队列。 |
| Depth-first Search (DFS) | 深度优先搜索 | 优先深入尚未访问的分支，之后回溯。 |
| Breadth-first Search (BFS) | 广度优先搜索 | 按与起点距离的层次依次扩展节点。 |
| Lowest Common Ancestor (LCA) | 最近公共祖先 | 两个节点共同祖先中深度最大的节点。 |

<a id="section-08"></a>
## 08 · 搜索树与平衡树 / Search Trees & Balanced Trees

理解查找不变量、旋转、平衡约束和常见平衡树变体。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Binary Search Tree (BST) | 二叉搜索树 | 左子树键小于节点键、右子树键大于节点键（重复键规则另定）。 |
| Search Tree | 搜索树 | 利用键顺序或分区规则支持高效检索的树。 |
| Balanced Tree | 平衡树 | 通过结构约束控制高度以保证操作效率的树。 |
| Self-balancing Tree | 自平衡树 | 在更新时自动维持指定平衡条件的树。 |
| AVL Tree | AVL 树 | 通过左右子树高度差约束保持平衡的搜索树。 |
| Red–Black Tree | 红黑树 | 以节点颜色与路径约束限制高度的平衡搜索树。 |
| Splay Tree | 伸展树 | 通过访问后的旋转将操作节点移至根部的搜索树。 |
| Treap | 树堆 | 同时满足搜索树的键顺序和堆的优先级约束。 |
| Scapegoat Tree | 替罪羊树 | 在失衡时重建子树的平衡搜索树。 |
| Weight-balanced Tree | 权重平衡树 | 依据子树大小或权重维持平衡的搜索树。 |
| AA Tree | AA 树 | 使用简化层级约束实现平衡的搜索树。 |
| Tree Rotation | 树旋转 | 局部调整父子链接且维持中序顺序的操作。 |
| Left Rotation | 左旋 | 围绕节点与其右子节点进行的局部旋转。 |
| Right Rotation | 右旋 | 围绕节点与其左子节点进行的局部旋转。 |
| Balance Factor | 平衡因子 | 常指左右子树高度的差值。 |
| Rebalancing | 重新平衡 | 插入或删除后恢复树的平衡约束。 |
| Order Statistic Tree | 顺序统计树 | 支持按排名选取元素等操作的增强搜索树。 |
| Rank Query | 排名查询 | 求小于指定键的元素数量或对应位置。 |
| Select Query | 按秩选择 | 按排序位置查找第 k 个元素。 |
| Successor Query | 后继查询 | 查找比给定键大的最小键。 |
| Predecessor Query | 前驱查询 | 查找比给定键小的最大键。 |
| B-Tree | B 树 | 允许多键、多子节点、适合块存储的平衡搜索树。 |
| B+ Tree | B+ 树 | 通常把记录或索引条目集中于叶层的多路搜索树。 |
| B* Tree | B* 树 | 通过更高节点利用率约束改进的 B 树变体。 |
| 2–3 Tree | 2-3 树 | 内部节点可有两个或三个孩子的平衡搜索树。 |
| 2–3–4 Tree | 2-3-4 树 | 内部节点可有两个、三个或四个孩子的平衡搜索树。 |

<a id="section-09"></a>
## 09 · 堆与优先队列 / Heaps & Priority Queues

辨析堆序性质、堆构建以及优先队列的不同实现。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Heap (Data Structure) | 堆（数据结构） | 满足特定堆序性质的树形结构，不等同于堆内存。 |
| Binary Heap | 二叉堆 | 满足完全二叉树形态及堆序性质的堆。 |
| Min-heap | 最小堆 | 父节点键不大于子节点键的堆。 |
| Max-heap | 最大堆 | 父节点键不小于子节点键的堆。 |
| Heap Property | 堆序性质 | 父子节点键之间满足规定大小关系的性质。 |
| Priority Queue | 优先队列 | 按优先级而非严格入队时间取出元素的抽象容器。 |
| Heapify | 堆化 | 对数组或局部节点调整以恢复堆序性质。 |
| Build Heap | 建堆 | 将无序元素集合组织为合法堆的过程。 |
| Sift Up | 上滤／上浮 | 将节点向父节点方向调整以恢复堆序。 |
| Sift Down | 下滤／下沉 | 将节点向子节点方向调整以恢复堆序。 |
| Extract Min | 取出最小值 | 移除并返回最小堆的堆顶元素。 |
| Extract Max | 取出最大值 | 移除并返回最大堆的堆顶元素。 |
| Decrease Key | 减小键值 | 降低元素优先级键值并调整结构。 |
| Increase Key | 增大键值 | 提高元素键值并调整结构。 |
| D-ary Heap | d 叉堆 | 每个节点最多拥有 d 个孩子的堆。 |
| Binomial Heap | 二项堆 | 由满足约束的二项树集合组成的可合并堆。 |
| Fibonacci Heap | 斐波那契堆 | 支持多种高效均摊操作的可合并堆。 |
| Pairing Heap | 配对堆 | 通过树链接与成对合并实现的堆结构。 |
| Meldable Heap | 可合并堆 | 支持高效合并两堆元素的堆抽象或实现。 |

<a id="section-10"></a>
## 10 · 图的表示与属性 / Graphs: Representation & Properties

用统一术语描述顶点、边、方向、连通性和图的存储。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Graph | 图 | 由顶点集合与连接顶点的边集合构成的结构。 |
| Vertex | 顶点 | 图中表示对象、状态或位置的基本元素。 |
| Edge | 边 | 图中连接一对顶点的关系。 |
| Directed Graph (Digraph) | 有向图 | 边具有方向的图。 |
| Undirected Graph | 无向图 | 边不区分方向的图。 |
| Weighted Graph | 带权图 | 边或顶点带有成本、距离等数值权重的图。 |
| Unweighted Graph | 无权图 | 边不附加显式权重的图。 |
| Simple Graph | 简单图 | 通常不含自环和重边的图。 |
| Multigraph | 多重图 | 允许同一对顶点之间存在多条边的图。 |
| Self-loop | 自环 | 起点与终点为同一顶点的边。 |
| Parallel Edges | 平行边／重边 | 连接同一对顶点的多条边。 |
| Adjacent Vertices | 相邻顶点 | 通过一条边直接连接的两个顶点。 |
| Incident Edge | 关联边 | 以指定顶点为端点的边。 |
| Degree | 度 | 无向图中与顶点相接的边数，自环按两次计。 |
| In-degree | 入度 | 有向图中指向某顶点的边数。 |
| Out-degree | 出度 | 有向图中从某顶点出发的边数。 |
| Path | 路径 | 由相邻顶点与边依次组成的行进序列。 |
| Simple Path | 简单路径 | 顶点不重复出现的路径。 |
| Walk | 游走 | 允许重复顶点和边的图上行进序列。 |
| Cycle | 环／回路 | 起点与终点相同的闭合路径或游走，具体约定依语境。 |
| Connected Graph | 连通图 | 任意两顶点之间均存在路径的无向图。 |
| Connected Component | 连通分量 | 无向图中极大的连通子图。 |
| Strongly Connected Component (SCC) | 强连通分量 | 有向图中互相可达的极大顶点集合。 |
| Directed Acyclic Graph (DAG) | 有向无环图 | 不存在有向环的有向图。 |
| Bipartite Graph | 二分图 | 顶点可分为两组且边仅跨两组连接的图。 |
| Adjacency List | 邻接表 | 按顶点记录其相邻顶点或关联边的存储方式。 |
| Adjacency Matrix | 邻接矩阵 | 用二维矩阵标记顶点对之间是否存在边。 |
| Edge List | 边列表 | 逐条保存边及端点、权重等信息的表示。 |
| Incidence Matrix | 关联矩阵 | 通过顶点与边之间的关系构造的矩阵。 |
| Compressed Sparse Row (Graph CSR) | 图的压缩稀疏行表示 | 以偏移数组和邻接顶点数组紧凑存储图。 |

<a id="section-11"></a>
## 11 · 图结构算法与连通性 / Graph Algorithms & Connectivity

纳入与图结构直接相关的经典算法、生成树和拓扑关系。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Graph Traversal | 图遍历 | 按规则访问可达顶点与边的过程。 |
| Topological Sort | 拓扑排序 | 对 DAG 顶点排列，使每条有向边均从前指向后。 |
| Topological Order | 拓扑序 | 符合图中依赖方向约束的顶点排列。 |
| Reachability | 可达性 | 是否存在从一个顶点到另一个顶点的路径。 |
| Transitive Closure | 传递闭包 | 描述各顶点对之间可达性的关系。 |
| Spanning Tree | 生成树 | 包含连通无向图全部顶点的无环连通子图。 |
| Minimum Spanning Tree (MST) | 最小生成树 | 总边权最小的生成树。 |
| Kruskal's Algorithm | 克鲁斯卡尔算法 | 按边权排序并逐步选择不成环的边构建 MST。 |
| Prim's Algorithm | 普里姆算法 | 从一个顶点出发逐步扩张生成树以构建 MST。 |
| Shortest Path | 最短路径 | 两顶点间总权重最小的路径。 |
| Single-source Shortest Path (SSSP) | 单源最短路径 | 求一个源点到其他顶点的最短距离或路径。 |
| All-pairs Shortest Paths (APSP) | 全源最短路径 | 求图中所有顶点对的最短距离。 |
| Dijkstra's Algorithm | 迪杰斯特拉算法 | 求非负边权图单源最短路径的经典算法。 |
| Bellman–Ford Algorithm | 贝尔曼—福特算法 | 可处理负边权并检测可达负环的最短路算法。 |
| Floyd–Warshall Algorithm | 弗洛伊德—沃歇尔算法 | 使用动态规划求全源最短路径。 |
| A* Search | A* 搜索 | 借助启发函数指导的路径搜索算法。 |
| Negative Cycle | 负权环 | 边权之和为负的有向环。 |
| Cut | 割 | 将图的顶点分为两部分所形成的跨分区边集合。 |
| Bridge | 桥 | 移除后会增加无向图连通分量数量的边。 |
| Articulation Point | 割点 | 移除后会增加无向图连通分量数量的顶点。 |
| Biconnected Component | 双连通分量 | 按双连通关系划分的极大子图，需区分点／边双连通。 |
| Tarjan's Algorithm | Tarjan 算法 | 利用 DFS 与低链接值求强连通分量等的算法族。 |
| Low-link Value | 低链接值 | DFS 中表示可经特定边型到达的最早祖先编号。 |
| Eulerian Path | 欧拉路径 | 恰好经过每条边一次的路径或迹。 |
| Hamiltonian Path | 哈密顿路径 | 恰好访问每个顶点一次的路径。 |

<a id="section-12"></a>
## 12 · 并查集与区间查询 / Disjoint Sets & Range Queries

学习高效合并集合、区间聚合、树状数组与线段树。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Disjoint Set Union (DSU) | 并查集 | 维护互不相交集合并支持合并与代表元查询的结构。 |
| Union–Find | 并查集／合并查找 | 并查集数据结构及其核心操作的另一常用名称。 |
| Find | 查找代表元 | 返回元素所在集合的代表节点。 |
| Union | 合并集合 | 把两个不相交集合合为一个集合。 |
| Path Compression | 路径压缩 | 在查找代表元时缩短节点至根的路径。 |
| Union by Rank | 按秩合并 | 依据树的秩选择连接方向以限制高度。 |
| Union by Size | 按大小合并 | 将较小集合对应的树挂到较大集合的根下。 |
| Inverse Ackermann Function | 反阿克曼函数 | 用于描述优化并查集近乎常数均摊复杂度的函数。 |
| Range Query | 区间查询 | 查询连续下标区间上的汇总结果。 |
| Point Update | 单点更新 | 修改序列中某一个位置的值。 |
| Range Update | 区间更新 | 修改连续一段位置中的全部或部分值。 |
| Prefix Sum | 前缀和 | 从序列起始位置到指定下标的累计和。 |
| Prefix Sum Array | 前缀和数组 | 预先存储各位置前缀和的数组。 |
| Difference Array | 差分数组 | 通过相邻元素差表示序列，便于区间加法更新。 |
| Fenwick Tree (Binary Indexed Tree) | 树状数组 | 支持前缀聚合与单点更新的紧凑索引结构。 |
| Segment Tree | 线段树 | 通过树节点存储区间信息并支持聚合查询与更新。 |
| Lazy Propagation | 懒惰传播 | 延迟将区间更新下推至子节点的技术。 |
| Sparse Table | 稀疏表 | 预处理幂长区间以高效回答静态幂等区间查询的结构。 |
| Range Minimum Query (RMQ) | 区间最小值查询 | 求指定区间内的最小元素或最小值。 |
| Range Maximum Query | 区间最大值查询 | 求指定区间内的最大元素或最大值。 |
| Interval Tree | 区间树 | 保存区间并支持区间相交检索的结构。 |
| Binary Indexed Tree | 二叉索引树 | Fenwick Tree 的另一常见英文名称。 |

<a id="section-13"></a>
## 13 · 字符串、字典树与索引 / Strings, Tries & Indexes

覆盖前缀匹配、后缀索引与多模式字符串查询。

| English | 中文术语 | 简明释义 |
|---|---|---|
| String | 字符串 | 按次序排列的字符或符号序列。 |
| Character | 字符 | 字符串中的基本符号单位，具体编码粒度依语境。 |
| Substring | 子串 | 字符串中连续的一段字符序列。 |
| Subsequence | 子序列 | 保持相对次序但不要求连续的字符序列。 |
| Prefix | 前缀 | 从字符串起始位置开始的连续片段。 |
| Suffix | 后缀 | 直到字符串末尾的连续片段。 |
| Trie (Prefix Tree) | 字典树／前缀树 | 按字符或符号边组织键前缀的树形索引。 |
| Trie Node | 字典树节点 | 表示某个前缀状态并保存后继分支的节点。 |
| Terminal Node | 终止节点 | 表示某个完整键在 Trie 中结束的节点。 |
| Radix Tree | 基数树 | 将单分支路径压缩成多符号边的前缀树。 |
| Patricia Trie | Patricia 树 | 对 Trie 的单路径进行压缩的检索树变体。 |
| Ternary Search Tree | 三叉搜索树 | 每个节点按小于、等于、大于分支组织字符的树。 |
| Suffix Array | 后缀数组 | 按字典序排列所有后缀起始位置的数组。 |
| Suffix Tree | 后缀树 | 紧凑表示字符串所有后缀的树形索引。 |
| Suffix Automaton | 后缀自动机 | 紧凑表示一个字符串全部子串的有限状态自动机。 |
| Longest Common Prefix (LCP) | 最长公共前缀 | 两个字符串或后缀开头连续相同的最长部分。 |
| LCP Array | 最长公共前缀数组 | 保存排序后相邻后缀 LCP 长度的数组。 |
| Prefix Function | 前缀函数 | 记录每个前缀的最长相等真前后缀长度的数组。 |
| Failure Link | 失配链接 | 自动机或字典树匹配失败时的跳转链接。 |
| Aho–Corasick Automaton | AC 自动机 | 结合 Trie 与失配链接进行多模式匹配的结构。 |
| Rolling Hash | 滚动哈希 | 可通过递推快速更新窗口或子串哈希的技术。 |
| String Interner | 字符串驻留表 | 把相同内容字符串映射到共享表示的结构。 |
| Inverted Index | 倒排索引 | 按词项记录包含它的文档或位置列表的索引。 |

<a id="section-14"></a>
## 14 · 概率型、外存与并发结构 / Probabilistic, External & Concurrent Structures

延伸到数据库存储引擎、近似成员查询和多线程场景。

| English | 中文术语 | 简明释义 |
|---|---|---|
| Bloom Filter | 布隆过滤器 | 紧凑的概率型成员结构；可有假阳性，通常无假阴性。 |
| Counting Bloom Filter | 计数布隆过滤器 | 将位替换成计数器以支持一定条件下的删除。 |
| Cuckoo Filter | 布谷鸟过滤器 | 使用短指纹和可替换桶实现近似成员查询。 |
| Count–Min Sketch | Count–Min 草图 | 以概率误差上界估计元素出现频次的结构。 |
| HyperLogLog | HyperLogLog 基数估计 | 用少量空间近似统计不同元素数量的算法与结构。 |
| Probabilistic Data Structure | 概率型数据结构 | 用随机化或近似表示换取时间、空间收益的结构。 |
| Bitset / Bitmap | 位集合／位图 | 以比特位表示布尔状态或整数成员的结构。 |
| Roaring Bitmap | Roaring 位图 | 按块选择压缩形式的高效整数集合位图。 |
| External-memory Data Structure | 外存数据结构 | 针对磁盘或块设备访问成本设计的数据结构。 |
| B-Tree Index | B 树索引 | 使用多路平衡搜索树组织磁盘友好索引的方式。 |
| LSM Tree | 日志结构合并树 | 以可排序的内存表与磁盘层级文件组织写密集型存储。 |
| Memtable | 内存表 | LSM 系统中接收近期写入的有序内存结构。 |
| SSTable | 排序字符串表 | 将有序键值记录写入不可变文件的存储格式。 |
| Write-ahead Log (WAL) | 预写日志 | 先持久化操作记录，以支持崩溃恢复的日志结构。 |
| Log-structured Storage | 日志结构化存储 | 以追加写和后台整理为核心的存储组织方式。 |
| Concurrent Data Structure | 并发数据结构 | 允许多个执行线程协同访问的结构。 |
| Thread-safe Data Structure | 线程安全数据结构 | 并发使用时能满足规定正确性约束的结构。 |
| Lock-free Data Structure | 无锁数据结构 | 系统整体操作可在有限步骤中持续取得进展的结构。 |
| Wait-free Data Structure | 无等待数据结构 | 每个线程操作均能在有限自身步骤内完成的结构。 |
| Linearizability | 线性一致性 | 并发操作可视为在调用与返回之间某瞬间原子发生的正确性条件。 |
| Compare-and-swap (CAS) | 比较并交换 | 比较目标值并在匹配时原子更新的同步原语。 |
| ABA Problem | ABA 问题 | 值由 A 变 B 再变 A 导致 CAS 难察觉中间变化的问题。 |
| Lock-free Queue | 无锁队列 | 不依赖互斥锁并满足无锁进展保证的并发队列。 |
| Copy-on-write (COW) | 写时复制 | 在写入发生时才复制共享数据的策略。 |
| Structural Sharing | 结构共享 | 不同版本复用未改变的内部节点或子结构。 |

<a id="confusions"></a>
## 易混淆概念对照

| English | 中文辨析 | 说明 |
|---|---|---|
| Heap vs. Heap Memory | 堆（数据结构）≠ 堆内存 | 前者通常是满足堆序性质的树；后者指动态内存分配区域。 |
| Array vs. List | 数组 ≠ 列表抽象 | 数组强调索引与布局；List 是抽象序列，可用数组或链表实现。 |
| Stack vs. Call Stack | 栈 ≠ 调用栈 | 栈是 LIFO 容器抽象；调用栈是运行时保存调用帧的实现机制。 |
| Priority Queue vs. Heap | 优先队列 ≠ 堆 | 优先队列是抽象类型；二叉堆、平衡树等都可实现它。 |
| Map vs. Hash Map | 映射 ≠ 哈希映射 | Map 描述键值关联；Hash Map 只是其中一种实现。 |
| BST vs. Binary Tree | 二叉搜索树 ≠ 二叉树 | 二叉搜索树额外规定键顺序；普通二叉树没有此要求。 |
| Full vs. Perfect vs. Complete | 严格／满／完全二叉树 | 严格：节点有 0 或 2 个孩子；满：叶同层且内部节点各有 2 个孩子；完全：按层从左填充。 |
| Trie vs. Prefix Tree | Trie 与前缀树 | 通常是同一类数据结构的两种名称；不同实现可能压缩路径。 |
| Set vs. Multiset | 集合 ≠ 多重集合 | Set 不允许重复元素；Multiset 允许并记录重复次数。 |
| B-Tree vs. B+ Tree | B 树 ≠ B+ 树 | B+ 树常把数据条目放在叶层，并通过叶间链接支持范围扫描。 |
| DFS vs. BFS | 深度优先 ≠ 广度优先 | DFS 优先深入分支；BFS 按距离层次扩展。 |
| Bloom Filter vs. Hash Set | 布隆过滤器 ≠ 哈希集合 | Bloom Filter 节省空间但可能误判存在；Hash Set 通常给出精确成员答案。 |

## 使用说明

- 中英文术语按主题组织，而非严格按字母排序；便于建立数据结构知识体系。
- 释义为快速检索而压缩，具体边界条件以课程、论文、语言标准或库文档为准。
- 部分术语同时属于算法、数据库与并发编程，纳入是为了便于关联学习。
- 欢迎在 GitHub 仓库中通过 Issue 或 Pull Request 提议修订译名及补充术语。
