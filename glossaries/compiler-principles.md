# 编译原理 · Compiler Principles

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：268 条 · 专题：12 类**

Lexing, grammars, parsing, semantics, SSA, optimization, code generation and runtime

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 编译器架构与工具链（20 条）
- 02. 形式语言与文法（24 条）
- 03. 词法分析（22 条）
- 04. 语法分析（27 条）
- 05. 语法树与属性文法（15 条）
- 06. 语义分析与类型系统（24 条）
- 07. 中间表示与控制流（24 条）
- 08. 数据流与程序分析（24 条）
- 09. 编译优化（24 条）
- 10. 代码生成与寄存器分配（22 条）
- 11. 运行时、链接与加载（22 条）
- 12. 现代编译器与工具（20 条）

---

## 01. 编译器架构与工具链

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Compiler | 编译器 |  | 将源程序转换为目标表示的程序，通常包含分析、优化和代码生成阶段。 |
| 2 | Compilation | 编译 |  | 把源代码转换为另一种程序表示或可执行形式的过程。 |
| 3 | Source Language | 源语言 |  | 编译器接受的输入编程语言。 |
| 4 | Target Language | 目标语言 |  | 编译器输出所采用的语言或机器表示。 |
| 5 | Compiler Front End | 编译器前端 |  | 负责词法、语法、语义分析并生成中间表示的部分。 |
| 6 | Compiler Middle End | 编译器中端 |  | 主要针对中间表示执行与目标机器相对独立的优化。 |
| 7 | Compiler Back End | 编译器后端 |  | 将中间表示映射到目标指令集并生成机器代码。 |
| 8 | Compilation Pipeline | 编译流水线 |  | 按顺序或按阶段组织编译任务的数据处理过程。 |
| 9 | Compiler Pass | 编译遍次 |  | 一次针对程序表示执行的分析或变换步骤。 |
| 10 | Pass Manager | 遍次管理器 |  | 安排、执行和管理编译分析与变换遍次的组件。 |
| 11 | Cross Compiler | 交叉编译器 |  | 在一种宿主平台上生成另一目标平台程序的编译器。 |
| 12 | Host Platform | 宿主平台 |  | 运行编译器或构建工具的计算平台。 |
| 13 | Target Architecture | 目标架构 |  | 生成代码需要符合的处理器架构或指令集约束。 |
| 14 | Toolchain | 工具链 |  | 编译器、汇编器、链接器及其他构建工具的集合。 |
| 15 | Assembler | 汇编器 |  | 将汇编语言转换为目标文件或机器指令的工具。 |
| 16 | Linker | 链接器 |  | 解析外部符号并组合目标文件与库以形成输出程序的工具。 |
| 17 | Interpreter | 解释器 |  | 按语言语义直接执行程序表示的运行系统。 |
| 18 | Transpiler | 源到源编译器 |  | 将一种高级语言或方言转换为另一种源码形式的编译器。 |
| 19 | Ahead-of-Time Compilation | 提前编译 | AOT | 在程序运行之前完成代码生成的编译方式。 |
| 20 | Just-in-Time Compilation | 即时编译 | JIT | 在程序执行期间根据需要生成或优化机器代码的方式。 |

## 02. 形式语言与文法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Formal Language | 形式语言 |  | 由给定字母表上满足规则的字符串构成的集合。 |
| 2 | Alphabet | 字母表 |  | 形式语言中允许出现的基本符号的有限集合。 |
| 3 | String | 符号串 |  | 由字母表中的符号按顺序组成的有限序列。 |
| 4 | Language Recognition | 语言识别 |  | 判断输入符号串是否属于某种形式语言。 |
| 5 | Grammar | 文法 |  | 通过产生式描述语言句子结构的形式系统。 |
| 6 | Context-Free Grammar | 上下文无关文法 | CFG | 每条产生式左部恰有一个非终结符的文法。 |
| 7 | Terminal Symbol | 终结符 |  | 文法推导中不再被替换的基本语法符号。 |
| 8 | Nonterminal Symbol | 非终结符 |  | 表示语法类别并可按产生式继续展开的符号。 |
| 9 | Start Symbol | 开始符号 |  | 文法推导的指定初始非终结符。 |
| 10 | Production Rule | 产生式 |  | 描述一个非终结符如何替换为符号序列的规则。 |
| 11 | Derivation | 推导 |  | 从开始符号应用产生式得到句子的过程。 |
| 12 | Leftmost Derivation | 最左推导 |  | 每一步均替换当前最左非终结符的推导。 |
| 13 | Rightmost Derivation | 最右推导 |  | 每一步均替换当前最右非终结符的推导。 |
| 14 | Sentential Form | 句型 |  | 从开始符号经过零次或多次推导得到的符号串。 |
| 15 | Parse Tree | 分析树 |  | 表示某个句子按照文法产生式推导的层次结构。 |
| 16 | Ambiguous Grammar | 二义性文法 |  | 存在至少一个句子可以对应两棵不同分析树的文法。 |
| 17 | Left Recursion | 左递归 |  | 非终结符可以推导出以自身为首符号的句型。 |
| 18 | Left Factoring | 提取左公因子 |  | 合并候选式公共前缀以便进行预测分析的文法变换。 |
| 19 | Nullable Nonterminal | 可空非终结符 |  | 可以推导出空串的非终结符。 |
| 20 | FIRST Set | FIRST 集 |  | 某个符号串可推导出的句子的首个终结符集合，并可能包含空串。 |
| 21 | FOLLOW Set | FOLLOW 集 |  | 在句型中可能紧跟某个非终结符出现的终结符集合，可含输入结束标记。 |
| 22 | Chomsky Normal Form | 乔姆斯基范式 | CNF | 上下文无关文法的一类标准形式，典型产生式为 A→BC 或 A→a。 |
| 23 | Backus–Naur Form | 巴科斯-诺尔范式 | BNF | 采用产生式符号表达编程语言语法的记法。 |
| 24 | Extended Backus–Naur Form | 扩展巴科斯-诺尔范式 | EBNF | 为 BNF 引入重复、可选等表达手段的语法记法。 |

## 03. 词法分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Lexical Analysis | 词法分析 |  | 把字符流划分为词法单元并识别其类别的过程。 |
| 2 | Lexer | 词法分析器 |  | 根据词法规则从输入字符序列生成词法单元的程序。 |
| 3 | Token | 词法单元 |  | 供语法分析器消费的词法类别及相关属性。 |
| 4 | Lexeme | 词素 |  | 源程序中与某个词法单元实例相匹配的实际字符序列。 |
| 5 | Token Kind | 词法单元类别 |  | 标识标识符、关键字、运算符等词法单元种类。 |
| 6 | Identifier | 标识符 |  | 用于命名变量、函数、类型或其他程序实体的记号。 |
| 7 | Keyword | 关键字 |  | 语言定义为具有特殊语法用途的保留或上下文词语。 |
| 8 | Literal | 字面量 |  | 在源程序中直接表示某个值的记法。 |
| 9 | Regular Expression | 正则表达式 |  | 用于描述正则语言的一类模式表达式。 |
| 10 | Regular Language | 正则语言 |  | 可由有限自动机识别的形式语言。 |
| 11 | Finite Automaton | 有限自动机 | FA | 通过有限个状态和状态转移识别符号串的计算模型。 |
| 12 | Deterministic Finite Automaton | 确定有限自动机 | DFA | 每个状态对每个输入符号最多只有一条适用转移的自动机。 |
| 13 | Nondeterministic Finite Automaton | 非确定有限自动机 | NFA | 可存在多条选择或空转移的有限自动机。 |
| 14 | Epsilon Transition | 空串转移 | ε-transition | 不消耗输入符号的自动机状态转移。 |
| 15 | Subset Construction | 子集构造法 |  | 将 NFA 状态集合映射为 DFA 状态的确定化算法。 |
| 16 | DFA Minimization | DFA 最小化 |  | 合并等价状态以减少确定有限自动机状态数量的过程。 |
| 17 | Maximal Munch | 最长匹配原则 |  | 词法扫描优先选择当前位置能够识别的最长词素。 |
| 18 | Lookahead | 向前看 |  | 为决定当前词法或语法动作而查看后续输入符号。 |
| 19 | Lexical State | 词法状态 |  | 用于区分不同扫描上下文和词法规则的状态。 |
| 20 | Whitespace | 空白符 |  | 如空格、制表符和换行等通常用于分隔词法单元的字符。 |
| 21 | Escape Sequence | 转义序列 |  | 以特殊写法表示控制字符或其他字符的符号序列。 |
| 22 | Source Span | 源码区间 |  | 记录词法单元或语法节点在源文件中的起止位置。 |

## 04. 语法分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Parsing | 语法分析 |  | 依据文法确定词法单元序列的语法结构。 |
| 2 | Parser | 语法分析器 |  | 读取词法单元并构造或验证语法结构的程序。 |
| 3 | Top-Down Parsing | 自顶向下分析 |  | 从开始符号或起始规则逐步预测并匹配输入的分析方法。 |
| 4 | Bottom-Up Parsing | 自底向上分析 |  | 从输入符号归约形成较高层语法结构的分析方法。 |
| 5 | Recursive Descent Parser | 递归下降分析器 |  | 以相互调用的过程实现语法规则的自顶向下分析器。 |
| 6 | Predictive Parsing | 预测分析 |  | 利用有限向前看符号选择产生式的分析方法。 |
| 7 | LL(1) Grammar | LL(1) 文法 |  | 可从左到右读取并构造最左推导且只需一个向前看符号的文法类。 |
| 8 | LR Parsing | LR 分析 |  | 从左到右读取输入并按最右推导的逆过程进行归约的分析。 |
| 9 | LR(0) Item | LR(0) 项 |  | 在产生式右部用点标记识别进度的分析状态元素。 |
| 10 | LR(1) Item | LR(1) 项 |  | 包含产生式、点位置和一个向前看终结符的分析项。 |
| 11 | Canonical LR(1) | 规范 LR(1) |  | 使用完整 LR(1) 项集构造分析自动机与分析表的方法。 |
| 12 | SLR Parsing | 简单 LR 分析 | SLR | 使用 LR(0) 项集和 FOLLOW 集决定部分归约动作的分析方法。 |
| 13 | LALR Parsing | 向前看 LR 分析 | LALR | 合并相同 LR(0) 核心的 LR(1) 状态以压缩分析表的方法。 |
| 14 | GLR Parsing | 广义 LR 分析 | GLR | 通过保留多个分析分支处理冲突或二义性文法的分析技术。 |
| 15 | Shift Action | 移进动作 |  | 把当前输入词法单元移入分析栈并推进状态。 |
| 16 | Reduce Action | 归约动作 |  | 按某条产生式把栈上的右部符号归并为左部非终结符。 |
| 17 | Shift/Reduce Conflict | 移进-归约冲突 |  | 同一状态和向前看符号同时允许移进与归约的情况。 |
| 18 | Reduce/Reduce Conflict | 归约-归约冲突 |  | 同一状态与向前看符号存在多个可能归约的情况。 |
| 19 | Parsing Table | 分析表 |  | 根据状态和输入符号选择语法分析动作的数据结构。 |
| 20 | ACTION Table | ACTION 表 |  | LR 分析器用于决定移进、归约、接受或报错的表。 |
| 21 | GOTO Table | GOTO 表 |  | LR 分析器按归约后非终结符转移到新状态的表。 |
| 22 | Operator Precedence | 运算符优先级 |  | 定义运算符组合绑定次序的语法规则。 |
| 23 | Associativity | 结合性 |  | 控制相同优先级运算符组合方向的规则。 |
| 24 | Dangling Else | 悬空 else 问题 |  | 嵌套条件语句中 else 归属可能不明确的典型语法歧义。 |
| 25 | Error Recovery | 错误恢复 |  | 语法分析在发现错误后尝试定位问题并继续处理后续输入的机制。 |
| 26 | Panic-Mode Recovery | 恐慌模式恢复 |  | 跳过输入直到同步符号出现的语法错误恢复策略。 |
| 27 | Parser Generator | 语法分析器生成器 |  | 根据文法描述自动生成解析器的工具。 |

## 05. 语法树与属性文法

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Concrete Syntax Tree | 具体语法树 | CST | 保留接近原始文法结构与语法符号的树形表示。 |
| 2 | Abstract Syntax Tree | 抽象语法树 | AST | 省略部分具体语法细节并表达程序结构的树。 |
| 3 | Syntax Node | 语法节点 |  | 表示表达式、语句、声明等语法构造的树节点。 |
| 4 | Node Visitor | 节点访问者 |  | 沿语法树遍历并对各类节点执行操作的设计模式。 |
| 5 | Tree Traversal | 树遍历 |  | 按预定顺序访问语法树节点的过程。 |
| 6 | Preorder Traversal | 先序遍历 |  | 先处理当前节点再处理其子节点的遍历方式。 |
| 7 | Postorder Traversal | 后序遍历 |  | 先处理子节点再处理当前节点的遍历方式。 |
| 8 | Attribute Grammar | 属性文法 |  | 为文法符号关联属性及计算规则的语义描述方法。 |
| 9 | Synthesized Attribute | 综合属性 |  | 通常从子节点属性推导并向父节点传递的属性。 |
| 10 | Inherited Attribute | 继承属性 |  | 通常由父节点或兄弟节点上下文提供的属性。 |
| 11 | Syntax-Directed Definition | 语法制导定义 | SDD | 将属性及语义规则与文法产生式关联的形式化定义。 |
| 12 | Syntax-Directed Translation | 语法制导翻译 | SDT | 在语法分析过程中执行语义动作以生成结果的技术。 |
| 13 | Semantic Action | 语义动作 |  | 附在文法规则上的属性计算或代码生成操作。 |
| 14 | Desugaring | 语法糖消除 |  | 把高级语法便捷写法改写为较基础表示的变换。 |
| 15 | AST Lowering | 抽象语法树降低 |  | 将高层 AST 转换为更低层程序表示的过程。 |

## 06. 语义分析与类型系统

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Semantic Analysis | 语义分析 |  | 检查程序是否满足名称、类型及语言其他静态语义规则的过程。 |
| 2 | Name Resolution | 名称解析 |  | 把名称出现位置关联到其所引用的声明或实体。 |
| 3 | Scope | 作用域 |  | 程序中一个声明名称可见或可绑定的区域。 |
| 4 | Lexical Scope | 词法作用域 |  | 由程序静态嵌套结构决定名称绑定的作用域规则。 |
| 5 | Symbol Table | 符号表 |  | 存储标识符及其声明、类型、位置等属性的数据结构。 |
| 6 | Binding | 绑定 |  | 将名称与程序实体或值建立关联。 |
| 7 | Shadowing | 名称遮蔽 |  | 内层作用域中的同名声明隐藏外层声明的现象。 |
| 8 | Type Checking | 类型检查 |  | 判断表达式与操作是否符合语言类型规则。 |
| 9 | Static Typing | 静态类型 |  | 在编译期按静态规则确定或检查表达式类型的类型机制。 |
| 10 | Dynamic Typing | 动态类型 |  | 在运行期通过值或运行时检查约束类型相关行为的机制。 |
| 11 | Type Inference | 类型推断 |  | 根据约束和上下文自动推导表达式类型。 |
| 12 | Type Unification | 类型合一 |  | 求解使多个类型表达式一致的类型替换关系。 |
| 13 | Subtyping | 子类型关系 |  | 允许某类值在一定规则下替代另一类型值的关系。 |
| 14 | Parametric Polymorphism | 参数多态 |  | 代码用类型参数抽象多种具体类型的能力。 |
| 15 | Ad Hoc Polymorphism | 特设多态 |  | 通过重载或类型类等机制为不同类型选取不同操作实现。 |
| 16 | Generic Instantiation | 泛型实例化 |  | 将泛型声明与具体类型参数结合形成使用实例。 |
| 17 | Monomorphization | 单态化 |  | 为泛型类型参数组合生成具体专用实现的编译策略。 |
| 18 | Overload Resolution | 重载决议 |  | 从同名候选函数或运算符中选择匹配调用的实现。 |
| 19 | Implicit Conversion | 隐式类型转换 |  | 编译器按语言规则自动插入或允许的类型转换。 |
| 20 | Lvalue | 左值 |  | 具有可寻址存储位置或其他语言规定身份属性的表达式类别。 |
| 21 | Rvalue | 右值 |  | 通常表示可读取的计算值的表达式类别，其精确定义依语言而异。 |
| 22 | Constant Expression | 常量表达式 |  | 按语言规则可在编译期求值的表达式。 |
| 23 | Definite Assignment | 确定赋值分析 |  | 验证变量在使用之前已沿所有相关路径完成赋值的检查。 |
| 24 | Escape Analysis | 逃逸分析 |  | 判断对象或引用是否可能超出其创建位置或局部作用域的分析。 |

## 07. 中间表示与控制流

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Intermediate Representation | 中间表示 | IR | 连接前端与后端、便于分析和变换的程序表示。 |
| 2 | High-Level IR | 高级中间表示 | HIR | 较多保留语言抽象与结构信息的中间表示。 |
| 3 | Low-Level IR | 低级中间表示 | LIR | 更接近机器操作或目标指令形式的中间表示。 |
| 4 | Three-Address Code | 三地址码 | TAC | 以有限个操作数和结果位置表达指令的经典中间代码。 |
| 5 | Basic Block | 基本块 |  | 具有单一入口、内部无分支的最长连续指令序列。 |
| 6 | Control-Flow Graph | 控制流图 | CFG | 以基本块为节点、可能控制转移为边的有向图。 |
| 7 | Directed Edge | 有向边 |  | 表示一个基本块可能转移到另一基本块的控制关系。 |
| 8 | Entry Block | 入口块 |  | 控制流图中函数执行开始位置对应的基本块。 |
| 9 | Exit Block | 出口块 |  | 控制流图中控制离开函数的一类终止位置或人工汇总节点。 |
| 10 | Predecessor Block | 前驱基本块 |  | 控制流图中具有指向当前块边的基本块。 |
| 11 | Successor Block | 后继基本块 |  | 控制流图中可从当前块直接到达的基本块。 |
| 12 | Terminator Instruction | 终结指令 |  | 决定基本块结束时控制如何转移的指令。 |
| 13 | Static Single Assignment | 静态单赋值形式 | SSA | 每个变量版本只被定义一次的中间表示约束。 |
| 14 | Phi Function | φ 函数 | φ | 在 SSA 的控制流汇合处依据前驱路径选择输入值的概念操作。 |
| 15 | Dominance | 支配关系 |  | 若到某节点的每条入口路径都经过另一节点，则后者支配前者。 |
| 16 | Dominator Tree | 支配树 |  | 以树形结构刻画控制流图中直接支配关系。 |
| 17 | Immediate Dominator | 直接支配节点 | idom | 严格支配一个节点且在其所有严格支配者中最接近该节点的节点。 |
| 18 | Dominance Frontier | 支配边界 |  | 用于定位 SSA φ 函数插入点的一种控制流边界集合。 |
| 19 | Loop Header | 循环头 |  | 自然循环中支配循环内节点并接收回边的入口基本块。 |
| 20 | Back Edge | 回边 |  | 控制流图中从某节点指向其支配节点的边。 |
| 21 | Natural Loop | 自然循环 |  | 由回边及其关联控制流结构确定的循环区域。 |
| 22 | Critical Edge | 关键边 |  | 从多后继块指向多前驱块的控制流边，拆分后便于局部变换。 |
| 23 | Continuation-Passing Style | 续延传递风格 | CPS | 将后续计算显式表示为续延参数的程序表示方式。 |
| 24 | Memory SSA | 内存 SSA | MemorySSA | 将内存读写关系组织为 SSA 风格依赖结构的程序分析表示。 |

## 08. 数据流与程序分析

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Data-Flow Analysis | 数据流分析 |  | 沿控制流传播抽象信息以计算程序性质的分析框架。 |
| 2 | Forward Analysis | 前向分析 |  | 沿程序执行方向传播信息的数据流分析。 |
| 3 | Backward Analysis | 后向分析 |  | 沿控制流反向传播信息的数据流分析。 |
| 4 | Transfer Function | 传递函数 |  | 描述基本块或指令如何改变抽象分析状态的函数。 |
| 5 | Meet Operator | 汇合运算符 |  | 将来自多个控制流路径的分析信息合并的运算。 |
| 6 | Fixed Point | 不动点 |  | 反复求解后分析状态不再发生变化的结果。 |
| 7 | Worklist Algorithm | 工作表算法 |  | 反复处理待更新节点直至满足收敛条件的求解方法。 |
| 8 | Lattice | 格 |  | 具有偏序与合并等运算、常用于抽象分析状态的数学结构。 |
| 9 | Monotone Framework | 单调数据流框架 |  | 使用单调传递函数和适当格结构描述的数据流分析体系。 |
| 10 | Reaching Definitions | 到达定义分析 |  | 求解哪些赋值定义可能在未被覆盖前到达某程序点。 |
| 11 | Live Variable Analysis | 活跃变量分析 |  | 求解当前变量值是否可能在后续路径被读取。 |
| 12 | Available Expressions | 可用表达式分析 |  | 找出在到达程序点的所有路径上已计算且操作数未被修改的表达式。 |
| 13 | Very Busy Expressions | 预期表达式分析 |  | 寻找在所有后续路径上会先被计算而其操作数不被修改的表达式。 |
| 14 | Constant Propagation | 常量传播 |  | 通过追踪已知常量值替换或简化程序表达式。 |
| 15 | Alias Analysis | 别名分析 | AA | 判断不同指针或引用是否可能指向同一存储位置。 |
| 16 | Points-To Analysis | 指向分析 |  | 估计指针可能指向的内存对象集合。 |
| 17 | Interprocedural Analysis | 过程间分析 |  | 跨越函数调用边界推导程序性质的分析。 |
| 18 | Intraprocedural Analysis | 过程内分析 |  | 仅在单个函数或过程范围内开展的分析。 |
| 19 | Call Graph | 调用图 |  | 以函数为节点、调用关系为边表示程序调用结构的图。 |
| 20 | Use-Def Chain | 使用-定义链 |  | 从变量使用位置关联到可能产生该值的定义位置。 |
| 21 | Def-Use Chain | 定义-使用链 |  | 从变量定义位置关联到可能读取该定义值的使用位置。 |
| 22 | Abstract Interpretation | 抽象解释 |  | 以抽象语义近似程序运行行为并推导性质的方法。 |
| 23 | Path Sensitivity | 路径敏感性 |  | 分析是否区分不同控制流路径条件的特性。 |
| 24 | Context Sensitivity | 上下文敏感性 |  | 过程间分析是否区分不同调用上下文的特性。 |

## 09. 编译优化

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Optimization Pass | 优化遍次 |  | 尝试改善代码性能、大小或其他目标的程序变换阶段。 |
| 2 | Correctness-Preserving Transformation | 保持语义变换 |  | 在规定可观察行为下不改变程序语义的优化变换。 |
| 3 | Dead Code Elimination | 死代码消除 | DCE | 删除其结果不被使用且无需要保留副作用的计算。 |
| 4 | Dead Store Elimination | 死存储消除 | DSE | 删除在被任何相关读取观察前已被覆盖的写入。 |
| 5 | Common Subexpression Elimination | 公共子表达式消除 | CSE | 复用等价表达式已有结果以避免重复计算。 |
| 6 | Global Value Numbering | 全局值编号 | GVN | 通过识别跨基本块的值等价关系消除冗余计算。 |
| 7 | Constant Folding | 常量折叠 |  | 在编译期计算具有已知常量操作数的表达式。 |
| 8 | Copy Propagation | 复制传播 |  | 将复制语句的源值替代后续对目标变量的使用。 |
| 9 | Sparse Conditional Constant Propagation | 稀疏条件常量传播 | SCCP | 结合可达性和 SSA 稀疏表示执行常量推导的优化。 |
| 10 | Loop Invariant Code Motion | 循环不变代码外提 | LICM | 在安全条件下将循环中不变计算移至循环外。 |
| 11 | Loop Unrolling | 循环展开 |  | 复制循环体以减少循环控制开销或暴露优化机会。 |
| 12 | Loop Fusion | 循环融合 |  | 将可兼容的相邻循环合并以降低开销或提高局部性。 |
| 13 | Loop Fission | 循环分裂 |  | 将一个循环拆成多个循环以调整数据访问与并行机会。 |
| 14 | Loop Tiling | 循环分块 |  | 把迭代空间划分为小块以改善缓存局部性。 |
| 15 | Strength Reduction | 强度削弱 |  | 将高成本运算替换为语义等价的较低成本运算。 |
| 16 | Inlining | 函数内联 |  | 以被调函数体替换调用点以减少调用开销并暴露优化。 |
| 17 | Tail Call Optimization | 尾调用优化 | TCO | 优化位于尾位置的函数调用以减少额外调用开销。 |
| 18 | Vectorization | 向量化 |  | 将多个标量操作重写为可由向量指令执行的操作。 |
| 19 | Auto-Vectorization | 自动向量化 |  | 编译器自动识别并生成 SIMD 等向量计算代码。 |
| 20 | Instruction Scheduling | 指令调度 |  | 重排满足依赖约束的指令以改善执行效率。 |
| 21 | Profile-Guided Optimization | 基于性能剖析的优化 | PGO | 利用运行采样或插桩得到的执行信息指导优化。 |
| 22 | Link-Time Optimization | 链接时优化 | LTO | 在链接阶段跨目标文件进行程序分析与优化。 |
| 23 | Devirtualization | 去虚调用化 |  | 在能确定目标时将间接虚调用转换为直接调用或更专用形式。 |
| 24 | Undefined Behavior | 未定义行为 | UB | 语言规范不对某种程序行为施加要求的情形，会影响合法优化前提。 |

## 10. 代码生成与寄存器分配

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Code Generation | 代码生成 |  | 把中间表示映射为目标机器指令或目标语言代码的过程。 |
| 2 | Instruction Selection | 指令选择 |  | 为程序操作选择符合目标指令集的机器指令序列。 |
| 3 | Instruction Set Architecture | 指令集架构 | ISA | 定义机器指令、寄存器及其程序可见语义的接口。 |
| 4 | Target Machine | 目标机器 |  | 代码生成器面向的处理器与 ABI 等平台环境。 |
| 5 | Machine Instruction | 机器指令 |  | 目标处理器可以执行的编码操作。 |
| 6 | Machine IR | 机器中间表示 | MIR | 接近机器指令层次、便于后端处理的中间表示。 |
| 7 | Pattern Matching | 模式匹配 |  | 识别 IR 结构并选择相应指令模板的技术。 |
| 8 | Instruction Legalization | 指令合法化 |  | 将目标架构不支持的操作拆解或转换成支持的操作。 |
| 9 | Register Allocation | 寄存器分配 |  | 决定程序中的值在何处使用物理寄存器或栈槽的过程。 |
| 10 | Virtual Register | 虚拟寄存器 |  | 寄存器分配前表示临时值的抽象寄存器。 |
| 11 | Physical Register | 物理寄存器 |  | 目标处理器实际提供的架构寄存器。 |
| 12 | Register Interference Graph | 寄存器冲突图 |  | 用边表示不能共享同一寄存器的活跃值关系图。 |
| 13 | Graph Coloring Allocation | 图着色寄存器分配 |  | 将寄存器分配建模为冲突图着色问题的方法。 |
| 14 | Linear Scan Allocation | 线性扫描寄存器分配 |  | 按活跃区间顺序快速安排寄存器的分配算法。 |
| 15 | Live Interval | 活跃区间 |  | 描述变量或虚拟寄存器值在程序序列上存活范围的表示。 |
| 16 | Register Spilling | 寄存器溢出 |  | 寄存器不足时将值暂存到内存并在需要时加载的处理。 |
| 17 | Spill Slot | 溢出栈槽 |  | 为寄存器溢出值保留的栈帧存储位置。 |
| 18 | Calling Convention | 调用约定 |  | 规定参数传递、返回值、寄存器保存等函数调用规则。 |
| 19 | Application Binary Interface | 应用二进制接口 | ABI | 规定函数调用、对象格式和数据布局等二进制兼容约定。 |
| 20 | Stack Frame | 栈帧 |  | 函数调用期间用于保存局部变量、返回信息等内容的栈空间布局。 |
| 21 | Prologue | 函数序言 |  | 函数入口处建立运行环境的指令序列。 |
| 22 | Epilogue | 函数尾声 |  | 函数返回前恢复调用约定状态的指令序列。 |

## 11. 运行时、链接与加载

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Runtime System | 运行时系统 |  | 为程序执行提供内存管理、异常处理等支持的组件。 |
| 2 | Runtime Library | 运行时库 |  | 实现语言运行时操作和基础辅助服务的库。 |
| 3 | Object File | 目标文件 |  | 包含机器码、符号表及重定位信息的编译输出文件。 |
| 4 | Executable File | 可执行文件 |  | 经链接后满足目标平台装载执行要求的程序文件。 |
| 5 | Static Linking | 静态链接 |  | 在链接时将所需库代码或对象内容纳入输出文件的方式。 |
| 6 | Dynamic Linking | 动态链接 |  | 在装载或运行期间解析共享库引用的链接方式。 |
| 7 | Shared Library | 共享库 |  | 供多个程序或模块加载并使用的库文件。 |
| 8 | Symbol Resolution | 符号解析 |  | 为未定义或外部符号引用寻找对应定义的过程。 |
| 9 | Symbol Mangling | 符号修饰 |  | 将名称空间、参数类型等信息编码进符号名的过程。 |
| 10 | Relocation | 重定位 |  | 根据符号地址或布局调整目标代码与数据中的地址引用。 |
| 11 | Position-Independent Code | 位置无关代码 | PIC | 设计为可在不同加载地址运行而无需对代码作大量重写的机器代码。 |
| 12 | Global Offset Table | 全局偏移表 | GOT | 在某些目标平台上辅助访问可重定位地址的表。 |
| 13 | Procedure Linkage Table | 过程链接表 | PLT | 在某些目标平台上支持动态函数调用解析的跳转表。 |
| 14 | Loader | 装载器 |  | 把可执行文件及依赖模块映射到内存并准备执行的系统组件。 |
| 15 | Garbage Collection | 垃圾回收 | GC | 自动识别并回收不再可达或使用的内存对象的机制。 |
| 16 | Reference Counting | 引用计数 |  | 通过维护引用数量来管理对象生命周期的一种技术。 |
| 17 | Exception Handling | 异常处理 |  | 表示、传播并处理运行期间异常情况的语言机制。 |
| 18 | Stack Unwinding | 栈展开 |  | 异常传播或其他控制转移时逐层退出调用帧的过程。 |
| 19 | Safepoint | 安全点 |  | 运行系统可安全执行某些全局协调操作的程序位置。 |
| 20 | Thread-Local Storage | 线程局部存储 | TLS | 每个线程独享一份同名变量存储的机制。 |
| 21 | Debug Information | 调试信息 |  | 将机器代码地址映射到源代码、类型和变量等信息的元数据。 |
| 22 | DWARF | DWARF 调试信息格式 |  | 常用于目标文件的标准化调试信息格式。 |

## 12. 现代编译器与工具

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | LLVM | LLVM 编译器基础设施 |  | 提供中间表示、优化器和多种目标后端的编译器项目。 |
| 2 | LLVM IR | LLVM 中间表示 |  | LLVM 使用的基于 SSA 的类型化中间表示。 |
| 3 | Clang | Clang 编译器前端 |  | 支持 C、C++ 等语言并与 LLVM 工具链集成的编译器前端。 |
| 4 | GCC | GNU 编译器套件 |  | 支持多种源语言与目标平台的编译器集合。 |
| 5 | MLIR | 多级中间表示 |  | LLVM 生态中用于表示多个抽象层次与可扩展方言的编译器基础设施。 |
| 6 | Dialect | 方言 |  | MLIR 中由一组操作、类型与属性组成的可扩展语义命名空间。 |
| 7 | Operation | 操作 |  | MLIR 等中间表示中可包含操作数、结果、属性与区域的结构单元。 |
| 8 | Region | 区域 |  | MLIR 中可包含一个或多个块的操作内部控制范围。 |
| 9 | Rewrite Pattern | 重写模式 |  | 识别特定程序结构并以替代表示改写它的规则。 |
| 10 | Canonicalization | 规范化 |  | 将等价表示重写为相对统一形式以简化后续分析。 |
| 11 | Lowering | 降低 |  | 将较高级表示逐步转换为较低级操作或目标表示的过程。 |
| 12 | JIT Compiler | 即时编译器 |  | 在运行阶段把程序表示编译为可执行机器代码的组件。 |
| 13 | Tiered Compilation | 分层编译 |  | 根据执行热度等信息在不同编译优化层级间切换的策略。 |
| 14 | Hot Path | 热点路径 |  | 程序执行中被频繁经过的控制流路径。 |
| 15 | On-Stack Replacement | 栈上替换 | OSR | 在函数运行过程中切换到另一版本已编译代码的技术。 |
| 16 | Deoptimization | 去优化 |  | 从优化代码回退到较通用执行状态的机制。 |
| 17 | Speculative Optimization | 推测性优化 |  | 基于可在运行期校验的假设执行的优化。 |
| 18 | Incremental Compilation | 增量编译 |  | 仅重新处理受输入变化影响的编译单元或阶段。 |
| 19 | Reproducible Build | 可复现构建 |  | 在相同规定输入条件下产生可验证一致输出的构建过程。 |
| 20 | Source Map | 源码映射 |  | 把生成代码位置映射回原始源码位置的元数据。 |

> 术语辨析：CFG 在形式语言中指上下文无关文法，在程序分析中指控制流图。

参考资料：[LLVM Language Reference](https://llvm.org/docs/LangRef.html) · [GNU Bison Manual](https://www.gnu.org/software/bison/manual/) · [GCC Internals](https://gcc.gnu.org/onlinedocs/gccint/)

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/compiler-principles.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
