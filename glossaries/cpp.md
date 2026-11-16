# C++ 专有名词中英文对照表

> C++ Technical Terminology: English–Chinese Glossary · **357 条术语 / 16 章** · 2026-11-16

本手册围绕 **C++ 语言核心、对象模型、泛型模板、STL、内存模型与现代工程实践** 编排。术语中译采用教材与工程领域常见用法，少数词汇可能因语境有不同译名。

**适用范围：** 以 C++11 / C++14 / C++17 / C++20 / C++23 的稳定概念为主体；所列库类型对应其首次引入时的标准版本。对 C++26 等持续演进的工作草案，不默认认定其特性已获所有主流编译器实现。

**阅读提示：** 本表的定义均为原创简释，便于查阅而非替代标准中的精确定义；标准支持情况应查看对应版本的标准文本与实现文档。

## 目录

- [01 语言基础与翻译构建 / Language Fundamentals and Toolchain](#chapter-01)（25 条）
- [02 类型、对象与存储期 / Types, Objects and Storage](#chapter-02)（26 条）
- [03 声明、引用和值类别 / Declarations, References and Value Categories](#chapter-03)（26 条）
- [04 表达式、转换与求值 / Expressions, Conversions and Evaluation](#chapter-04)（20 条）
- [05 函数、重载与参数 / Functions, Overloading and Parameters](#chapter-05)（19 条）
- [06 类、继承与对象模型 / Classes, Inheritance and Object Model](#chapter-06)（22 条）
- [07 资源管理与内存安全 / Resource Management and Memory Safety](#chapter-07)（22 条）
- [08 模板、泛型与 Concepts / Templates, Generic Programming and Concepts](#chapter-08)（29 条）
- [09 标准库容器、迭代器与视图 / Containers, Iterators and Views](#chapter-09)（23 条）
- [10 算法、Ranges 与函数式组件 / Algorithms, Ranges and Functional Tools](#chapter-10)（21 条）
- [11 异常、安全保证与错误处理 / Exceptions and Error Handling](#chapter-11)（16 条）
- [12 并发、线程与内存模型 / Concurrency, Threads and Memory Model](#chapter-12)（25 条）
- [13 常量求值与元编程 / Constant Evaluation and Metaprogramming](#chapter-13)（17 条）
- [14 现代 C++ 语言特性 / Modern C++ Language Features](#chapter-14)（24 条）
- [15 输入输出、文本与文件系统 / I/O, Text and Filesystem](#chapter-15)（18 条）
- [16 性能、诊断与工程实践 / Performance, Diagnostics and Engineering](#chapter-16)（24 条）
- [附录 A：易混淆概念速查](#appendix-a)
- [附录 B：参考资料与编辑原则](#appendix-b)

---

<a id="chapter-01"></a>

## 01 语言基础与翻译构建 / Language Fundamentals and Toolchain

从源文件、预处理、链接到标准符合性，理解 C++ 程序如何成为可执行文件。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| C++ programming language | C++ 编程语言 | 兼顾系统编程、抽象与性能的通用编译型编程语言。 |
| ISO C++ standard | ISO C++ 标准 | 规定语言及标准库要求的国际标准。 |
| C++ implementation | C++ 实现 | 编译器、标准库与运行环境共同实现标准的具体系统。 |
| hosted implementation | 宿主实现 | 提供完整标准库和程序启动环境的实现形式。 |
| freestanding implementation | 独立式实现 | 面向内核或嵌入式等环境，标准库要求较少的实现形式。 |
| translation unit | 翻译单元 | 源文件经预处理并展开头文件后的编译输入单位。 |
| source file | 源文件 | 包含 C++ 代码的程序文本文件。 |
| header file | 头文件 | 通常通过包含指令共享声明的文件。 |
| preprocessing | 预处理 | 编译早期处理宏、条件编译与文件包含的阶段。 |
| preprocessor directive | 预处理指令 | 以井号开头的预处理控制语句。 |
| macro expansion | 宏展开 | 将宏调用按预处理规则替换为相应记号序列。 |
| include guard | 头文件包含保护 | 防止同一头文件在单个翻译单元内重复展开的机制。 |
| compilation | 编译 | 将源程序翻译为目标代码的过程。 |
| compiler | 编译器 | 检查并翻译 C++ 源程序的工具。 |
| linker | 链接器 | 解析符号与重定位，组合目标文件和库的工具。 |
| object file | 目标文件 | 保存机器代码、符号及重定位信息的编译产物。 |
| executable | 可执行文件 | 可由运行环境加载并执行的程序文件。 |
| static library | 静态库 | 通常在链接时将所需目标代码纳入最终产物的库。 |
| shared library | 共享库 | 通常在加载或运行时参与符号解析的动态库。 |
| name mangling | 名字修饰 | 实现将函数签名等信息编码进链接符号的惯用方式。 |
| application binary interface (ABI) | 应用二进制接口 | 规定调用约定、对象布局、符号等二进制兼容规则。 |
| one-definition rule (ODR) | 单一定义规则 | 约束实体定义数量及跨翻译单元定义一致性的规则。 |
| undefined behavior (UB) | 未定义行为 | 标准不对该程序行为施加要求的情况。 |
| implementation-defined behavior | 实现定义行为 | 标准允许实现选择并要求记录的行为。 |
| unspecified behavior | 未指定行为 | 标准允许多个结果但无需规定选择哪一个的行为。 |

<a id="chapter-02"></a>

## 02 类型、对象与存储期 / Types, Objects and Storage

区分类型、对象、存储与生存期，避免把“内存存在”误作“对象有效”。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| fundamental type | 基本类型 | 语言内建的算术、void 与 nullptr_t 等基础类型类别。 |
| integral type | 整数类型 | 可表示整数或字符等离散值的内建类型。 |
| floating-point type | 浮点类型 | 表示浮点数值的类型，如 float 和 double。 |
| enumeration | 枚举类型 | 由命名枚举值组成的用户定义类型。 |
| scoped enumeration | 有作用域枚举 | 使用 enum class 或 enum struct 声明的枚举。 |
| class type | 类类型 | 通过 class、struct 或 union 定义的用户类型。 |
| compound type | 复合类型 | 在基础类型上构成的引用、指针、数组、类等类型。 |
| complete type | 完整类型 | 在需要其大小或成员信息处已完整定义的类型。 |
| incomplete type | 不完整类型 | 声明已知但定义尚不可用的类型。 |
| type alias | 类型别名 | 通过 using 或 typedef 为已有类型引入新名称。 |
| type deduction | 类型推导 | 编译器依据表达式或初始化信息推断类型。 |
| auto specifier | auto 类型说明符 | 要求编译器按上下文规则推导声明类型。 |
| decltype specifier | decltype 类型说明符 | 依据表达式的类型与值类别推导类型。 |
| object | 对象 | 具有存储、类型与生存期的存储区域或其关联实体。 |
| object representation | 对象表示 | 对象占用的字节序列。 |
| value representation | 值表示 | 对象表示中用于表示值的位。 |
| object lifetime | 对象生存期 | 对象存在且可按相应规则使用的时间区间。 |
| storage duration | 存储期 | 对象所用存储得以保持的时间属性。 |
| automatic storage duration | 自动存储期 | 典型局部变量在所属作用域执行期间管理的存储期。 |
| static storage duration | 静态存储期 | 程序执行期间持续存在的存储期。 |
| thread storage duration | 线程存储期 | 每个线程分别拥有并在线程期间持续存在的存储期。 |
| dynamic storage duration | 动态存储期 | 由分配与释放操作控制的存储期。 |
| alignment | 对齐 | 对象地址须满足的字节边界约束。 |
| padding byte | 填充字节 | 对象布局中不承载指定成员值的字节。 |
| trivially copyable type | 可平凡复制类型 | 满足标准规定的、可按对象表示复制的类型类别。 |
| standard-layout type | 标准布局类型 | 满足一组用于对象布局兼容性约束的类类型。 |

<a id="chapter-03"></a>

## 03 声明、引用和值类别 / Declarations, References and Value Categories

lvalue、prvalue、xvalue 是表达式类别，不等同于 const 或内存位置。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| declaration | 声明 | 向程序引入实体或给出其属性的语法构造。 |
| definition | 定义 | 提供实体完整定义所需信息的声明。 |
| initialization | 初始化 | 在对象创建或引用绑定时赋予初始状态的过程。 |
| copy initialization | 复制初始化 | 使用等号等形式触发的初始化规则。 |
| direct initialization | 直接初始化 | 使用圆括号或直接构造形式执行初始化。 |
| list initialization | 列表初始化 | 使用花括号初始化并遵守窄化限制等规则。 |
| aggregate initialization | 聚合初始化 | 按聚合成员或元素顺序进行的初始化。 |
| zero initialization | 零初始化 | 将标量设零等按标准规则执行的初始化。 |
| value initialization | 值初始化 | 按类型采用零初始化和默认初始化等组合规则。 |
| default initialization | 默认初始化 | 不提供显式初始化器时执行的初始化形式。 |
| reference | 引用 | 某个实体的别名，不是可重新绑定的独立指针。 |
| lvalue reference | 左值引用 | 使用 T& 声明并按引用绑定规则绑定表达式的引用。 |
| rvalue reference | 右值引用 | 使用 T&& 声明并可绑定特定右值表达式的引用。 |
| forwarding reference | 转发引用 | 特定推导上下文中的 T&&，可依据实参推导左右值。 |
| const qualifier | const 限定符 | 约束通过相应类型访问对象的修改操作。 |
| volatile qualifier | volatile 限定符 | 对特定对象访问施加语义限制，不等于线程同步。 |
| cv-qualification | cv 限定 | const 和 volatile 对类型的联合限定。 |
| value category | 值类别 | 表达式按对象身份与临时值语义划分的类别。 |
| lvalue | 左值 | 具有身份、可用于定位某实体等语义的表达式类别。 |
| rvalue | 右值 | prvalue 与 xvalue 的统称。 |
| prvalue | 纯右值 | 主要用于计算值或初始化对象的表达式类别。 |
| xvalue | 将亡值 | 具有对象身份且资源可被重用的表达式类别。 |
| glvalue | 泛左值 | lvalue 与 xvalue 的统称。 |
| temporary object | 临时对象 | 按表达式与初始化规则创建并通常在限定时机销毁的对象。 |
| temporary materialization | 临时量实质化 | 在需要对象身份时把纯右值转为临时对象的转换。 |
| lifetime extension | 生存期延长 | 某些引用绑定或初始化场景延长临时对象生存期的规则。 |

<a id="chapter-04"></a>

## 04 表达式、转换与求值 / Expressions, Conversions and Evaluation

关注求值顺序、隐式转换与 UB，避免将编译器观察当作语言保证。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| expression | 表达式 | 能产生值、对象指定或副作用的语法结构。 |
| statement | 语句 | 执行控制、声明或表达式操作的语法单位。 |
| full-expression | 完整表达式 | 影响临时量销毁和顺序规则的完整表达式边界。 |
| side effect | 副作用 | 对可观察状态的修改等求值效果。 |
| sequenced-before | 先序于 | 标准定义的同一线程内求值顺序关系。 |
| unsequenced evaluation | 无先后顺序求值 | 两个求值之间没有规定先序关系的情况。 |
| implicit conversion | 隐式转换 | 语言规则自动执行的类型或值转换。 |
| explicit conversion | 显式转换 | 程序员通过类型转换语法请求的转换。 |
| usual arithmetic conversions | 通常算术转换 | 二元算术表达式中为操作数选择共同类型的规则。 |
| integral promotion | 整数提升 | 将小整数类型提升为 int 等类型的转换。 |
| narrowing conversion | 窄化转换 | 可能丢失值域或精度、在部分列表初始化中受禁止的转换。 |
| static_cast | static_cast 转换 | 执行标准允许的显式类型转换。 |
| dynamic_cast | dynamic_cast 转换 | 针对多态类层次的运行时检查转换。 |
| const_cast | const_cast 转换 | 改变指针或引用表达式的 cv 限定形式。 |
| reinterpret_cast | reinterpret_cast 转换 | 执行特定底层指针、整数等重新解释转换。 |
| operator precedence | 运算符优先级 | 决定表达式如何组合的语法约定，不决定求值先后。 |
| short-circuit evaluation | 短路求值 | 逻辑与或按规则跳过不必计算的右操作数。 |
| conditional operator | 条件运算符 | 依据条件选择两个操作数结果的 ?: 运算符。 |
| comma operator | 逗号运算符 | 先计算左操作数，再计算右操作数的运算符。 |
| as-if rule | 假定规则 | 允许实现优化，只要保持标准要求的可观察行为。 |

<a id="chapter-05"></a>

## 05 函数、重载与参数 / Functions, Overloading and Parameters

把声明、实参匹配、重载决议与泛型参数传递分开理解。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| function declaration | 函数声明 | 说明函数名称、返回类型与形参列表的声明。 |
| function definition | 函数定义 | 提供函数体的声明。 |
| function signature | 函数签名 | 由语言规则用于区分特定函数的相关信息组合。 |
| function overload | 函数重载 | 在允许范围内共用名称而参数列表等不同的函数集合。 |
| overload resolution | 重载决议 | 为调用选择最佳可行函数的规则。 |
| argument-dependent lookup (ADL) | 实参依赖查找 | 依据实参关联的命名空间或类补充函数查找。 |
| parameter | 形参 | 在函数声明或定义中出现的参数变量或声明。 |
| argument | 实参 | 函数调用时提供的表达式或初始值。 |
| pass by value | 按值传递 | 在被调用方构造独立形参对象的传参方式。 |
| pass by reference | 按引用传递 | 形参引用绑定到调用方所指定实体的传参方式。 |
| default argument | 默认实参 | 调用时省略对应实参所使用的默认表达式。 |
| variadic function | 可变参数函数 | 能够接受可变数量实参的函数形式。 |
| variadic template | 可变参数模板 | 接收类型或非类型参数包的模板。 |
| function pointer | 函数指针 | 保存可调用函数地址的指针类型。 |
| member function | 成员函数 | 在类中声明且与成员访问相关的函数。 |
| inline function | 内联函数 | 受 ODR 多定义规则支持的函数；不保证机器码内联。 |
| noexcept specification | noexcept 异常规范 | 表达函数是否允许异常传播的规范。 |
| lambda expression | Lambda 表达式 | 生成匿名闭包对象的表达式。 |
| closure type | 闭包类型 | 编译器为 Lambda 表达式生成的独特类类型。 |

<a id="chapter-06"></a>

## 06 类、继承与对象模型 / Classes, Inheritance and Object Model

聚焦类的接口、对象构造和析构语义，而非某一 ABI 的固定布局。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| class | 类 | 将数据成员和函数等关联为自定义类型的构造。 |
| struct | 结构体 | 默认成员与基类访问权限为 public 的类声明形式。 |
| union | 联合体 | 成员共享同一存储的特殊类类型。 |
| access specifier | 访问说明符 | public、protected、private 等成员可访问性标记。 |
| encapsulation | 封装 | 通过类型接口与访问控制管理内部状态的设计思想。 |
| data member | 数据成员 | 类中声明的成员对象或其相关声明。 |
| static data member | 静态数据成员 | 属于类而非单个对象的静态成员。 |
| constructor | 构造函数 | 负责类对象初始化过程的特殊成员函数。 |
| default constructor | 默认构造函数 | 可以在无显式实参时调用的构造函数。 |
| copy constructor | 复制构造函数 | 从同类型对象初始化新对象的特殊构造函数。 |
| move constructor | 移动构造函数 | 通常从同类型右值对象转移状态的特殊构造函数。 |
| copy assignment operator | 复制赋值运算符 | 将一个现有对象的状态按复制语义赋给另一对象。 |
| move assignment operator | 移动赋值运算符 | 将右值来源状态按移动语义赋给现有对象。 |
| destructor | 析构函数 | 对象生存期结束时执行清理的特殊成员函数。 |
| rule of three | 三法则 | 需要自定义析构、复制构造或复制赋值时应审视三者的一致性。 |
| rule of five | 五法则 | 在三法则上同时考虑移动构造与移动赋值。 |
| rule of zero | 零法则 | 优先使用正确管理资源的成员，避免自定义五类特殊成员。 |
| inheritance | 继承 | 派生类基于基类形成类层次关系的机制。 |
| virtual function | 虚函数 | 支持通过基类接口动态分派的成员函数。 |
| abstract class | 抽象类 | 含有或继承未实现纯虚函数、不能直接实例化的类。 |
| virtual destructor | 虚析构函数 | 允许通过适当基类指针安全销毁派生对象的重要接口设计。 |
| object slicing | 对象切片 | 将派生对象按值复制成基类对象时丢失派生部分的现象。 |

<a id="chapter-07"></a>

## 07 资源管理与内存安全 / Resource Management and Memory Safety

强调 RAII、所有权与失效规则，区分语言工具和工程约定。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| resource acquisition is initialization (RAII) | 资源获取即初始化 | 将资源获得与对象初始化绑定，并在析构时自动释放资源的惯用法。 |
| resource ownership | 资源所有权 | 规定谁负责管理资源释放的设计关系。 |
| owning pointer | 拥有型指针 | 表达负责释放所指资源的指针或包装类型。 |
| non-owning pointer | 非拥有型指针 | 不负责释放目标对象的指针使用语义。 |
| raw pointer | 原始指针 | 语言内建指针类型，单独并不表达所有权。 |
| smart pointer | 智能指针 | 以类封装指针与所有权管理规则的工具。 |
| std::unique_ptr | 独占所有权智能指针 | 通过不可复制的所有权语义在析构时管理对象。 |
| std::shared_ptr | 共享所有权智能指针 | 以共享控制块的引用计数管理所拥有对象。 |
| std::weak_ptr | 弱引用智能指针 | 观察 shared_ptr 所管理对象且不增加强所有权计数。 |
| reference counting | 引用计数 | 通过计数追踪资源拥有者数量的管理方法。 |
| cyclic ownership | 循环所有权 | 共享所有权对象成环而导致资源无法自动释放的情况。 |
| custom deleter | 自定义删除器 | 指定智能指针释放资源方式的可调用对象。 |
| std::make_unique | make_unique 工厂函数 | 创建对象并返回管理其独占所有权的 unique_ptr。 |
| std::make_shared | make_shared 工厂函数 | 创建共享所有权对象并通常合并资源与控制块分配。 |
| allocator | 分配器 | 负责容器等组件存储分配与释放的抽象。 |
| std::pmr | 多态内存资源设施 | 标准库提供的运行时可配置内存资源接口集合。 |
| placement new | 定位 new | 在指定存储位置构造对象的 new 表达式形式。 |
| manual lifetime management | 手动生存期管理 | 显式控制对象构造与销毁时机的技术。 |
| dangling pointer | 悬空指针 | 所指对象已失效而仍保留其地址的指针。 |
| use-after-free | 释放后使用 | 访问已被释放或结束生存期资源的错误。 |
| double deletion | 重复释放 | 对同一资源错误地执行多次释放的行为。 |
| memory leak | 内存泄漏 | 不再能正确回收已分配资源的情况。 |

<a id="chapter-08"></a>

## 08 模板、泛型与 Concepts / Templates, Generic Programming and Concepts

将“泛型实例化规则”和“运行时多态”明确区分。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| template | 模板 | 参数化生成类、函数或变量等实体的语言机制。 |
| function template | 函数模板 | 以模板参数描述一族函数的声明。 |
| class template | 类模板 | 以模板参数描述一族类的声明。 |
| variable template | 变量模板 | 以模板参数描述一族变量的声明。 |
| alias template | 别名模板 | 以模板参数描述一族类型别名的声明。 |
| template parameter | 模板形参 | 在模板声明中引入的类型、常量或模板参数。 |
| template argument | 模板实参 | 为模板形参提供的具体参数。 |
| non-type template parameter | 非类型模板形参 | 以值而非类型作为模板参数的机制。 |
| template instantiation | 模板实例化 | 按模板与实参形成具体实体的过程。 |
| implicit instantiation | 隐式实例化 | 编译器因使用需求触发的模板实例化。 |
| explicit instantiation | 显式实例化 | 使用显式语法要求实例化模板特化。 |
| template specialization | 模板特化 | 针对给定模板实参形成的模板实体。 |
| full specialization | 全特化 | 为模板的特定实参集合提供专门定义。 |
| partial specialization | 偏特化 | 类或变量模板针对一部分实参模式提供专门定义。 |
| template argument deduction | 模板实参推导 | 编译器根据调用或其他上下文推导模板实参。 |
| substitution failure is not an error (SFINAE) | 替换失败并非错误 | 模板候选替换失败时可从重载集合移除候选的规则。 |
| constraint | 约束 | 限制模板实参或函数可用性的编译期条件。 |
| concept | 概念 | C++20 中可命名并复用的编译期约束集合。 |
| requires-expression | requires 表达式 | 检验表达式、类型或嵌套条件是否满足要求。 |
| requires-clause | requires 子句 | 为模板或函数声明附加约束的语法。 |
| constrained template | 受约束模板 | 以 concepts 或其他约束限制可用实参的模板。 |
| std::enable_if | enable_if 类型条件工具 | 按编译期条件启用特定类型或候选的类型特征工具。 |
| std::void_t | void_t 类型工具 | 将一组有效类型映射为 void 的元编程工具。 |
| type trait | 类型特征 | 编译期查询或变换类型属性的工具。 |
| std::is_same | 类型相同判断特征 | 检查两个模板类型实参是否为相同类型。 |
| perfect forwarding | 完美转发 | 保留实参值类别等性质向下游传递的泛型技术。 |
| std::forward | 条件式转发工具 | 依据模板参数选择适当值类别的强制转换工具。 |
| std::move | 转右值转换工具 | 将表达式转换为可移动的右值引用形式；本身不移动资源。 |
| fold expression | 折叠表达式 | C++17 对参数包应用二元运算符的表达式形式。 |

<a id="chapter-09"></a>

## 09 标准库容器、迭代器与视图 / Containers, Iterators and Views

容器复杂度、迭代器失效与范围适配是工程判断重点。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| standard template library (STL) | 标准模板库 | 惯常指标准库的容器、迭代器、算法等泛型组件群。 |
| sequence container | 序列容器 | 按线性序列组织元素的标准库容器类别。 |
| associative container | 关联容器 | 按键排序并组织元素的容器类别。 |
| unordered associative container | 无序关联容器 | 通常以哈希组织元素的关联容器类别。 |
| std::vector | 动态数组容器 | 提供连续存储及尾部高效插入的序列容器。 |
| std::array | 定长数组容器 | 以编译期固定长度封装内建数组的容器。 |
| std::deque | 双端队列容器 | 支持两端高效插入删除的分段序列容器。 |
| std::list | 双向链表容器 | 节点式双向链表容器。 |
| std::forward_list | 单向链表容器 | 节点式单向链表容器。 |
| std::map | 有序映射容器 | 按键排序、键唯一的关联容器。 |
| std::set | 有序集合容器 | 按键排序、元素唯一的关联容器。 |
| std::unordered_map | 无序映射容器 | 基于哈希的键唯一关联容器。 |
| std::unordered_set | 无序集合容器 | 基于哈希的元素唯一关联容器。 |
| std::span | 连续序列非拥有视图 | C++20 中对一段连续对象序列的轻量非拥有视图。 |
| std::string_view | 字符串非拥有视图 | 对连续字符序列的轻量只读视图；不拥有字符存储。 |
| iterator | 迭代器 | 抽象表示容器或序列中位置与访问操作的对象。 |
| input iterator | 输入迭代器 | 支持按输入语义读取序列元素的迭代器类别。 |
| forward iterator | 前向迭代器 | 支持多遍遍历的迭代器类别。 |
| bidirectional iterator | 双向迭代器 | 支持递增与递减遍历的迭代器类别。 |
| random-access iterator | 随机访问迭代器 | 支持常数时间位置跳转等操作的迭代器类别。 |
| contiguous iterator | 连续迭代器 | 保证元素物理连续存储语义的迭代器概念。 |
| iterator invalidation | 迭代器失效 | 容器操作使原有迭代器、指针或引用不再可用的现象。 |
| container adaptor | 容器适配器 | 在底层容器之上提供受限接口的组件，如 stack。 |

<a id="chapter-10"></a>

## 10 算法、Ranges 与函数式组件 / Algorithms, Ranges and Functional Tools

理解算法复杂度与惰性视图，不把 ranges 误当作独立容器。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| std::sort | 排序算法 | 对随机访问范围进行比较排序的标准算法。 |
| std::stable_sort | 稳定排序算法 | 排序时保留等价元素相对顺序的标准算法。 |
| std::find | 顺序查找算法 | 在范围中定位第一个等于指定值的元素。 |
| std::lower_bound | 下界查找算法 | 在已分区范围中定位首个不小于指定值的位置。 |
| std::binary_search | 二分存在性查找 | 检查已分区范围是否存在等价值。 |
| std::transform | 变换算法 | 对输入序列应用操作并向输出序列写结果。 |
| std::accumulate | 累积算法 | 按给定运算从初值顺序累加范围元素。 |
| std::reduce | 归约算法 | 可在不同求值分组下合并元素，不承诺与 accumulate 相同顺序。 |
| std::for_each | 逐元素操作算法 | 对范围中每个元素调用函数对象。 |
| comparator | 比较器 | 决定元素相对顺序或等价关系的可调用对象。 |
| strict weak ordering | 严格弱序 | 许多排序算法要求比较关系满足的数学性质。 |
| predicate | 谓词 | 返回可解释为布尔值结果的可调用对象。 |
| function object | 函数对象 | 定义了调用运算符的对象。 |
| std::function | 类型擦除可调用包装器 | 用统一接口保存满足签名要求的可调用目标。 |
| std::invoke | 通用调用工具 | 统一调用函数、成员指针及其他可调用对象。 |
| range | 范围 | 由起止位置或范围对象描述的可遍历元素序列。 |
| std::ranges | 范围库 | C++20 引入的范围概念、算法和视图工具集合。 |
| view | 视图 | 通常轻量且可组合的范围抽象，不等于拥有容器。 |
| range adaptor | 范围适配器 | 将范围变换为新视图的可组合操作。 |
| std::views::filter | 筛选视图适配器 | 按谓词从输入范围惰性筛选元素。 |
| std::views::transform | 映射视图适配器 | 按可调用操作惰性映射范围元素。 |

<a id="chapter-11"></a>

## 11 异常、安全保证与错误处理 / Exceptions and Error Handling

区分不抛异常的接口承诺、异常安全级别与可恢复错误表达。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| exception | 异常 | 用于非局部传播错误或异常条件的语言机制实体。 |
| throw expression | 抛出表达式 | 创建或重新抛出异常并启动异常传播的表达式。 |
| try block | try 语句块 | 包含受异常处理器监控的代码块。 |
| catch handler | catch 处理器 | 按类型等规则处理所捕获异常的代码。 |
| stack unwinding | 栈展开 | 异常传播时按规则销毁已构造的自动对象的过程。 |
| exception safety | 异常安全 | 代码在异常发生后保持资源与状态约束的能力。 |
| no-throw guarantee | 不抛异常保证 | 某操作承诺不会让异常向调用方传播。 |
| strong exception guarantee | 强异常保证 | 操作失败时对外可观察状态不变的保证。 |
| basic exception guarantee | 基本异常保证 | 操作失败仍维持有效状态且不泄漏资源的保证。 |
| std::exception | 标准异常基类 | 标准库常见异常类型的基类。 |
| std::runtime_error | 运行时错误异常 | 表达仅在运行时可检测错误的标准异常类型。 |
| std::error_code | 错误码对象 | 封装错误值与错误类别的标准库类型。 |
| std::optional | 可选值容器 | 显式表示存在值或不存在值的对象包装器。 |
| std::variant | 类型安全的可辨识联合 | 可在多个备选类型中保存一个当前有效值的对象。 |
| std::expected | 期望值或错误容器 | C++23 中表示成功值或错误值的类型。 |
| assertion | 断言 | 程序运行时验证开发假设的检查机制。 |

<a id="chapter-12"></a>

## 12 并发、线程与内存模型 / Concurrency, Threads and Memory Model

同步原语不能替代数据竞争定义；内存序必须结合 happens-before 理解。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| concurrency | 并发 | 多个任务的执行时间在逻辑上重叠的系统性质。 |
| parallelism | 并行 | 多个工作单元在物理计算资源上同时执行。 |
| thread | 线程 | 程序内可独立调度的执行流。 |
| std::thread | 标准线程类 | C++11 对执行线程的标准封装。 |
| std::jthread | 自动请求停止的线程类 | C++20 在线程析构时可请求停止并合并的封装。 |
| mutex | 互斥量 | 用于控制多个线程对共享资源互斥访问的同步原语。 |
| std::lock_guard | 作用域互斥锁保护器 | 用 RAII 在作用域开始与结束锁定及解锁互斥量。 |
| std::unique_lock | 可移动灵活锁管理器 | 支持延迟、条件等多种锁管理策略的包装器。 |
| std::scoped_lock | 多互斥量作用域锁 | 可同时管理一个或多个互斥量的 RAII 包装器。 |
| condition variable | 条件变量 | 线程等待条件并接受通知的同步设施。 |
| std::future | 异步结果对象 | 表示尚未就绪或可能包含异常的异步计算结果。 |
| std::promise | 异步结果承诺对象 | 向共享状态设置值或异常的生产端对象。 |
| std::async | 异步任务启动接口 | 按启动策略运行函数并返回 future 的标准接口。 |
| atomic operation | 原子操作 | 在标准内存模型中不可被其他线程观察到中间状态的操作。 |
| std::atomic | 原子类型模板 | 提供满足内存模型要求的原子读写与读改写操作。 |
| memory ordering | 内存序 | 规定原子操作之间可见性与重排约束的规则。 |
| relaxed ordering | 宽松内存序 | 仅提供原子性、不额外建立同步关系的内存序。 |
| acquire operation | 获取操作 | 可与适当释放操作建立同步关系的读侧原子操作。 |
| release operation | 释放操作 | 可将之前的效果发布给相应获取操作的写侧原子操作。 |
| sequential consistency | 顺序一致性 | 对相关原子操作施加全局单一顺序约束的模型。 |
| happens-before | 先行发生关系 | 决定线程间可见性与竞争关系的标准偏序关系。 |
| data race | 数据竞争 | 不同线程中冲突访问同一内存位置且不满足同步等条件的情况。 |
| race condition | 竞态条件 | 结果依赖并发执行时序的广义逻辑问题。 |
| deadlock | 死锁 | 线程互相等待资源或条件而无法继续执行的状态。 |
| false sharing | 伪共享 | 独立数据共享缓存行导致缓存一致性开销的性能现象。 |

<a id="chapter-13"></a>

## 13 常量求值与元编程 / Constant Evaluation and Metaprogramming

区分编译期可求值与强制编译期求值的语言要求。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| constant expression | 常量表达式 | 满足标准约束、可用于特定编译期语境的表达式。 |
| constexpr variable | constexpr 变量 | 要求按相应规则进行常量初始化的变量。 |
| constexpr function | constexpr 函数 | 可在符合要求的调用中参与常量求值的函数。 |
| consteval function | 立即函数 | C++20 要求按规则在编译期求值的函数。 |
| constinit specifier | constinit 说明符 | C++20 要求变量具备静态初始化的声明说明符。 |
| if constexpr | 编译期条件语句 | C++17 在实例化时可舍弃不满足条件的分支。 |
| static_assert | 静态断言 | 编译时验证常量条件并在失败时诊断的语句。 |
| template metaprogramming (TMP) | 模板元编程 | 利用模板实例化与类型计算完成编译期逻辑的技术。 |
| compile-time computation | 编译期计算 | 在程序翻译期间完成的值或类型计算。 |
| constant initialization | 常量初始化 | 静态或线程存储期变量按标准规则在静态阶段初始化。 |
| static initialization | 静态初始化 | 含常量初始化与零初始化的初始化类别。 |
| dynamic initialization | 动态初始化 | 不属于静态初始化的变量初始化阶段。 |
| non-type template argument | 非类型模板实参 | 作为模板参数传入的值或结构化对象等实参。 |
| parameter pack | 参数包 | 代表零个或多个模板或函数参数的集合。 |
| pack expansion | 参数包展开 | 把模式按参数包元素逐项展开的语法。 |
| integer_sequence | 整数序列模板 | 在类型层面表示编译期整数序列的库工具。 |
| feature-test macro | 特性测试宏 | 用于检测语言或标准库特性可用性的预定义或标准宏。 |

<a id="chapter-14"></a>

## 14 现代 C++ 语言特性 / Modern C++ Language Features

按照语言版本分层，并提醒编译器支持与标准文本并不相同。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| uniform initialization | 统一初始化 | 广泛采用花括号语法进行对象初始化的设计方向。 |
| range-based for loop | 范围 for 循环 | C++11 按元素或引用遍历范围的循环语法。 |
| structured binding | 结构化绑定 | C++17 将数组、元组状对象或成员分解为多个名称的声明。 |
| initialization statement | 初始化语句 | 可在 if 或 switch 条件前引入局部初始化的语法。 |
| if with initializer | 带初始化语句的 if | C++17 在 if 判断前执行局部初始化的结构。 |
| class template argument deduction (CTAD) | 类模板实参推导 | C++17 由初始化器推导类模板参数的机制。 |
| deduction guide | 推导指引 | 影响类模板实参推导的声明。 |
| inline variable | 内联变量 | C++17 支持跨翻译单元一致定义的变量形式。 |
| three-way comparison | 三路比较 | C++20 使用 <=> 建立排序关系的表达式机制。 |
| spaceship operator | 飞船运算符 | 三路比较运算符 <=> 的俗称。 |
| std::strong_ordering | 强序比较类别 | 表达强等价与有序比较结果的标准类型。 |
| module | 模块 | C++20 组织声明与依赖的语言级编译单元机制。 |
| module interface unit | 模块接口单元 | 含有导出模块声明的翻译单元。 |
| module implementation unit | 模块实现单元 | 定义模块内部实现的模块单元。 |
| export declaration | 导出声明 | 将声明纳入模块对外接口的语法。 |
| header unit | 头文件单元 | 可作为可导入单元使用的头文件形式。 |
| coroutine | 协程 | 能够挂起并恢复其执行的 C++20 函数形式。 |
| co_await expression | co_await 表达式 | 执行可等待对象协议并可能挂起协程的表达式。 |
| co_yield expression | co_yield 表达式 | 向协程消费者产生值并可能挂起的表达式。 |
| co_return statement | co_return 语句 | 按协程协议完成协程返回的语句。 |
| coroutine promise type | 协程承诺类型 | 定义协程状态与返回行为协议的类型。 |
| std::generator | 生成器 | C++23 提供的基于协程的同步序列生成设施。 |
| explicit object parameter | 显式对象形参 | C++23 允许成员函数显式声明对象形参的机制。 |
| multidimensional subscript operator | 多维下标运算符 | C++23 允许重载 operator[] 接受多个下标实参。 |

<a id="chapter-15"></a>

## 15 输入输出、文本与文件系统 / I/O, Text and Filesystem

明确文本编码问题与格式化、流状态和文件路径之间的边界。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| input/output stream (iostream) | 输入输出流 | 以统一接口处理输入与输出的标准库抽象。 |
| std::cin | 标准输入流 | 通常连接进程标准输入的字符输入流对象。 |
| std::cout | 标准输出流 | 通常连接进程标准输出的字符输出流对象。 |
| std::cerr | 标准错误流 | 通常连接进程标准错误输出的字符流对象。 |
| stream buffer | 流缓冲区 | 管理字符传输与缓冲的标准流组件。 |
| stream state flags | 流状态标志 | 记录 eof、fail、bad 等 I/O 状态的标志集合。 |
| std::ifstream | 输入文件流 | 用于从文件读取字符的流类型。 |
| std::ofstream | 输出文件流 | 用于向文件写入字符的流类型。 |
| std::stringstream | 字符串流 | 对字符串执行流式读写与格式转换的流类型。 |
| std::filesystem | 文件系统库 | C++17 提供路径、目录和文件操作的标准设施。 |
| std::filesystem::path | 文件系统路径 | 表示可按平台规则操作的路径对象。 |
| std::format | 格式化函数 | C++20 类型安全的格式化字符串接口。 |
| std::print | 格式化打印函数 | C++23 直接格式化并输出文本的标准函数。 |
| std::string | 字符串类 | 通常保存连续 char 元素序列的可拥有字符串类型。 |
| std::u8string | UTF-8 代码单元字符串 | 以 char8_t 保存 UTF-8 代码单元序列的字符串类型。 |
| character encoding | 字符编码 | 字符或代码点到代码单元序列的表示规则。 |
| locale | 区域设置 | 控制字符分类、数字格式等本地化行为的环境与库概念。 |
| serialization | 序列化 | 将对象状态转换为可存储或传输表示的过程；非统一标准库设施。 |

<a id="chapter-16"></a>

## 16 性能、诊断与工程实践 / Performance, Diagnostics and Engineering

区别语言保证、实现细节与性能工程术语。

| English term | 中文术语 | 简明释义 |
| --- | --- | --- |
| compile-time error | 编译期错误 | 编译器在翻译阶段诊断的程序错误。 |
| linker error | 链接错误 | 链接阶段出现的符号解析或目标文件组合失败。 |
| runtime error | 运行时错误 | 程序执行期间出现的错误情况。 |
| compiler warning | 编译器警告 | 编译器报告的潜在问题，并不一定表示程序不合法。 |
| optimization level | 优化级别 | 编译器控制优化策略集合的配置。 |
| inlining | 函数内联展开 | 编译器将调用替换为函数体或等效操作的优化。 |
| copy elision | 复制消除 | 按语言规则省去对象复制或移动构造的机制。 |
| return value optimization (RVO) | 返回值优化 | 在允许场景避免创建独立返回临时对象的优化。 |
| named return value optimization (NRVO) | 具名返回值优化 | 对具名局部对象返回时可能执行的复制消除。 |
| small string optimization (SSO) | 小字符串优化 | 标准库实现把短字符串存储在对象内部的常见优化。 |
| small buffer optimization (SBO) | 小缓冲区优化 | 将小对象以内嵌缓冲减少动态分配的实现技巧。 |
| move semantics | 移动语义 | 借助右值引用及特殊成员函数转移资源的语言与库惯用语义。 |
| zero-cost abstraction | 零开销抽象 | 目标是在不使用某抽象时无额外成本、使用时可高效实现的设计原则。 |
| cache locality | 缓存局部性 | 数据访问集中有利于缓存命中的性能性质。 |
| false sharing detection | 伪共享检测 | 识别线程访问同一缓存行不同数据引起争用的诊断活动。 |
| profiling | 性能剖析 | 测量运行时热点、调用或资源开销的过程。 |
| benchmark | 基准测试 | 在明确条件下比较性能指标的测试。 |
| unit testing | 单元测试 | 对较小的程序单元独立验证其行为的测试。 |
| address sanitizer (ASan) | 地址检查器 | 检测多类越界与释放后使用错误的运行时检测工具。 |
| undefined behavior sanitizer (UBSan) | 未定义行为检查器 | 通过编译插桩检测部分未定义行为的工具。 |
| thread sanitizer (TSan) | 线程检查器 | 检测部分并发数据竞争问题的动态分析工具。 |
| CMake | CMake 构建系统工具 | 广泛使用的跨平台项目配置与构建生成工具，非 C++ 标准组件。 |
| package manager | 包管理器 | 用于获取、解析与维护第三方库依赖的工具。 |
| continuous integration (CI) | 持续集成 | 在代码变更时自动执行构建和测试等检查的工程流程。 |

---

<a id="appendix-a"></a>

## 附录 A：易混淆概念速查

| 术语对照 | 核心区别 |
| --- | --- |
| 声明 vs 定义 | 声明说明实体存在及属性；定义进一步提供标准所需完整信息。并非每个声明都是定义。 |
| 类型 vs 对象 | 类型给出值与操作的规则；对象具备自己的存储和生存期。同一类型可以有多个对象。 |
| 存储期 vs 生存期 | 存储期谈底层存储何时可用；生存期谈对象何时已构造、可使用并最终销毁。 |
| 左值 vs 纯右值 vs 将亡值 | lvalue 具有身份；prvalue 主要用于计算值和初始化；xvalue 具有身份且资源可能被重用。 |
| 引用 vs 指针 | 引用以绑定对象的别名方式使用；指针有自身值、可空且通常可重新赋值。 |
| std::move vs 移动操作 | std::move 本身通常仅转换值类别；真正资源转移取决于后续构造或赋值等操作。 |
| 复制消除 vs 移动语义 | 复制消除可使预期复制或移动根本不发生；移动语义仍对应具体构造或赋值。 |
| const vs constexpr vs consteval vs constinit | const 限制修改，constexpr 可参与常量求值，consteval 要求立即函数的规定调用常量求值，constinit 保证静态初始化。 |
| 未定义 vs 未指定 vs 实现定义行为 | UB 没有行为要求；unspecified 允许多种行为但不必文档说明；implementation-defined 需要实现记录选择。 |
| volatile vs std::atomic | volatile 不是线程间同步手段；atomic 通过原子操作和内存序参加标准并发模型。 |
| 数据竞争 vs 竞态条件 | 数据竞争有严格的标准内存模型条件且导致 UB；竞态条件是更宽泛的时序依赖逻辑问题。 |
| 重载 vs 覆盖 vs 隐藏 | overload 是同名不同参数候选；override 是派生类覆写虚函数；name hiding 则是名称查找屏蔽。 |
| 全特化 vs 偏特化 | 全特化针对确切模板参数；偏特化为类或变量模板指定更窄参数模式，函数模板不允许偏特化。 |
| 容器 vs 视图 | 容器通常拥有元素；view 主要描述可遍历范围，可惰性计算且通常不拥有元素。 |
| unique_ptr vs shared_ptr vs weak_ptr | unique_ptr 独占所有权；shared_ptr 共享所有权；weak_ptr 只观察共享对象且不保持其存活。 |
| 模块 vs 头文件 | 模块具有语言级导入和可见性规则；传统头文件使用预处理文本包含，两者并不等价。 |

<a id="appendix-b"></a>

## 附录 B：参考资料与编辑原则

参考资料（用于术语核对与进一步阅读）：

- [ISO C++ 标准委员会（WG21）](https://www9.open-std.org/JTC1/SC22/WG21/)
- [cppreference：C++ language](https://en.cppreference.com/cpp/language)
- [cppreference：C++ library](https://en.cppreference.com/cpp)
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
- [C++ working draft（非正式发布标准）](https://eel.is/c++draft/)

**编辑原则：**

1. 优先使用标准规范中的英文原词与主流中文译名，必要时给出英文缩写。
2. 区分语言保证、标准库保证、常见实现策略与工程习惯。
3. 不将某一编译器、STL 实现或平台 ABI 的细节当作通用 C++ 规则。
4. 对每个术语保持唯一英文主键；新条目须包含简明定义和明确章节。
5. 编辑 `data/cpp-glossary.tsv` 后运行生成脚本，使 Markdown 与 PDF 保持一致。

欢迎通过 [GitHub Pull Request](https://github.com/1998x-stack/bilingual-technical-glossary/pulls) 修正术语或补充权威来源。
