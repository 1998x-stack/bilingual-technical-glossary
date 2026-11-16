# Python 专有名词中英文对照表

> Python Technical Terminology English–Chinese Glossary · 429 条术语 · 16 章 · 2026-11-16

说明：主要依据 Python 3.x 官方参考文档与 Python Packaging User Guide。中文译名是编辑性整理，遇到版本差异以官方原文为准。

## 目录

- [01 语言与运行环境](#chapter-01)（24 条）
- [02 词法、语法与源文件](#chapter-02)（25 条）
- [03 类型、对象与容器](#chapter-03)（33 条）
- [04 表达式、运算符与赋值](#chapter-04)（24 条）
- [05 控制流程与函数](#chapter-05)（28 条）
- [06 类、面向对象与数据模型](#chapter-06)（31 条）
- [07 迭代器、生成器与函数式工具](#chapter-07)（24 条）
- [08 异常处理与上下文管理](#chapter-08)（21 条）
- [09 模块、导入与项目结构](#chapter-09)（22 条）
- [10 类型注解与静态分析](#chapter-10)（28 条）
- [11 异步编程与并发模型](#chapter-11)（34 条）
- [12 文件、I/O 与系统接口](#chapter-12)（27 条）
- [13 常用标准库与数据工具](#chapter-13)（24 条）
- [14 依赖、包管理与构建发布](#chapter-14)（27 条）
- [15 测试、调试与工程质量](#chapter-15)（28 条）
- [16 性能、内存与解释器内部](#chapter-16)（29 条）
- [附录 A：易混淆概念速查](#appendix-a)
- [附录 B：英文 A-Z 索引](#appendix-b)
- [附录 C：参考文献](#appendix-c)

<a id="chapter-01"></a>

## 01 语言与运行环境 / Language & Runtime

先理解 Python 是如何解释、执行与组织代码的。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| Python | Python 编程语言 | 一种通用的高级编程语言，强调可读性与丰富的生态。 |
| CPython | CPython 解释器 | 最常见的 Python 实现，主要由 C 语言编写。 |
| Python implementation | Python 实现 | 实现 Python 语言规范的运行系统，如 CPython、PyPy。 |
| interpreter | 解释器 | 读取并执行 Python 程序的运行组件。 |
| interactive mode | 交互模式 | 在提示符中逐条输入并执行代码的工作模式。 |
| REPL | 读取-求值-输出循环 | Read–Eval–Print Loop；典型的交互式执行环境。 |
| script | 脚本 | 作为程序入口直接运行的 Python 源文件。 |
| source code | 源代码 | 开发者编写的可读程序文本。 |
| bytecode | 字节码 | Python 编译阶段产生的中间指令形式。 |
| code object | 代码对象 | 表示已编译可执行代码片段的内部对象。 |
| virtual machine | 虚拟机 | 在解释器内部执行字节码的抽象执行机制。 |
| runtime | 运行时 | 程序执行期间提供对象、异常与资源管理的环境。 |
| standard library | 标准库 | 随 Python 发行、涵盖大量常见功能的模块集合。 |
| built-in function | 内置函数 | 无须导入即可使用的函数，如 len()、print()。 |
| built-in type | 内置类型 | 无须额外导入的类型，如 int、list、dict。 |
| namespace | 命名空间 | 将名称映射到对象的结构。 |
| scope | 作用域 | 名称可被直接查找或引用的代码区域。 |
| name binding | 名称绑定 | 将变量名与某个对象建立关联。 |
| object | 对象 | Python 中具有身份、类型和值的运行实体。 |
| identity | 身份标识 | 标识对象本身；is 运算符比较对象身份。 |
| reference | 引用 | 指向对象的关联；变量保存的是对象引用语义。 |
| implementation detail | 实现细节 | 特定解释器的行为，不应一概视为语言保证。 |
| backward compatibility | 向后兼容 | 新版本尽量保持旧程序可运行的性质。 |
| Python Enhancement Proposal (PEP) | Python 增强提案 | 记录语言、库与开发流程重大设计决策的提案文档。 |

<a id="chapter-02"></a>

## 02 词法、语法与源文件 / Lexical & Syntax

区分代码文本的词法结构、语法规则和格式约定。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| token | 词法单元 | 词法分析器识别出的最小语法组成单位。 |
| keyword | 关键字 | 具有固定语法用途的保留词，如 if、return。 |
| soft keyword | 软关键字 | 仅在特定语法上下文中作关键字，如 match、case。 |
| identifier | 标识符 | 用于命名变量、函数、类和模块的合法名称。 |
| literal | 字面量 | 在代码中直接写出的常量表示，如 42、'hi'。 |
| expression | 表达式 | 可求值得到某个结果的语法结构。 |
| statement | 语句 | 执行动作或控制程序结构的语法单元。 |
| simple statement | 简单语句 | 通常占一个逻辑行的语句，如 pass、import。 |
| compound statement | 复合语句 | 引入代码块的语句，如 if、for、def。 |
| block | 代码块 | 按缩进组织的一组相关语句。 |
| indentation | 缩进 | Python 用来划定代码块层级的空白排版。 |
| logical line | 逻辑行 | 词法层面的完整语句行，可跨多个物理行。 |
| physical line | 物理行 | 源文件中由换行结束的一行字符。 |
| comment | 注释 | 以 # 开始、不会作为代码执行的说明文字。 |
| docstring | 文档字符串 | 模块、类或函数开头的字符串文档说明。 |
| encoding declaration | 编码声明 | 文件开头可指定源码编码的特殊注释。 |
| UTF-8 | UTF-8 编码 | Python 3 源码默认使用的 Unicode 编码形式。 |
| string prefix | 字符串前缀 | r、b、f 等前缀，用于指定字符串字面量种类。 |
| raw string | 原始字符串 | 带 r 前缀的字符串，减少对反斜杠转义的处理。 |
| f-string | 格式化字符串字面量 | 以 f 开头，允许在花括号中嵌入表达式。 |
| escape sequence | 转义序列 | 使用反斜杠表示特殊字符或编码，如 \n。 |
| syntax error | 语法错误 | 源代码违反语法规则，通常无法完成解析。 |
| semantic meaning | 语义 | 符合语法的代码在执行或求值时的含义。 |
| type annotation syntax | 类型注解语法 | 在函数参数、返回值及变量处声明类型信息的写法。 |
| PEP 8 | Python 代码风格指南 | 广泛使用的 Python 代码排版与命名建议。 |

<a id="chapter-03"></a>

## 03 类型、对象与容器 / Types & Containers

掌握内置类型、可变性、容器与视图的基本差别。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| type | 类型 | 决定对象支持哪些操作及其语义的类别。 |
| instance | 实例 | 某个类型或类创建出的具体对象。 |
| value | 值 | 对象所表示的数据内容。 |
| None | 空值对象 | 内置单例，通常表示缺失值或无返回结果。 |
| NoneType | 空值类型 | 单例 None 的类型。 |
| boolean | 布尔值 | 真或假；Python 内置 bool 类型的值。 |
| integer | 整数 | Python 的 int，支持任意精度整数运算。 |
| floating-point number | 浮点数 | Python 的 float，通常采用二进制浮点表示。 |
| complex number | 复数 | Python 的 complex，包含实部与虚部。 |
| string (str) | 字符串 | 不可变的 Unicode 文本序列。 |
| bytes | 字节串 | 不可变的字节序列，元素值为 0 到 255。 |
| bytearray | 可变字节数组 | 可就地修改的字节序列。 |
| list | 列表 | 有序、可变的对象序列。 |
| tuple | 元组 | 有序、不可变的对象序列。 |
| range | 范围对象 | 惰性表示整数等差序列的内置类型。 |
| dictionary (dict) | 字典 | 按键映射到值、保持插入顺序的可变映射。 |
| set | 集合 | 无序、不重复元素的可变集合类型。 |
| frozenset | 不可变集合 | 元素集合不支持增删操作的集合类型。 |
| sequence | 序列 | 支持按位置索引等操作的数据结构抽象。 |
| mapping | 映射 | 从键到值的关联结构抽象。 |
| container | 容器 | 用于包含其他对象的对象，如列表或字典。 |
| mutable | 可变的 | 对象创建后，其内部状态可以被修改。 |
| immutable | 不可变的 | 对象创建后，其值不可就地改变。 |
| hashable | 可哈希的 | 具有稳定哈希值并可用于字典键、集合元素的对象。 |
| hash value | 哈希值 | 由 hash() 返回、用于哈希表定位的整数。 |
| truth value testing | 真值测试 | 在 if、while、bool() 等场景判断对象真假。 |
| subscript | 下标访问 | 使用 obj[key] 访问元素或切片的语法。 |
| slice | 切片 | 用 start:stop:step 指定序列的某一范围。 |
| shallow copy | 浅拷贝 | 复制外层容器，内部嵌套对象通常仍被共享。 |
| deep copy | 深拷贝 | 递归复制嵌套对象，尽可能解除共享引用。 |
| dictionary view | 字典视图 | keys()、values()、items() 返回的动态视图。 |
| bytes-like object | 类字节对象 | 支持缓冲区协议的二进制数据对象。 |
| memoryview | 内存视图 | 无须复制底层数据即可访问缓冲区内容的对象。 |

<a id="chapter-04"></a>

## 04 表达式、运算符与赋值 / Expressions & Operators

理解求值、赋值、比较以及常见运算符行为。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| operator | 运算符 | 指定运算或比较操作的符号或关键字。 |
| operand | 操作数 | 运算符作用的值或表达式。 |
| operator precedence | 运算符优先级 | 决定表达式中不同运算符结合顺序的规则。 |
| associativity | 结合性 | 同优先级运算符的分组方式。 |
| arithmetic operator | 算术运算符 | 例如 +、-、*、/、//、%、**。 |
| floor division | 向下取整除法 | // 运算通常向负无穷方向取整。 |
| modulo | 取模运算 | % 返回余数，整数运算结果与除数符号相关。 |
| exponentiation | 幂运算 | ** 计算乘方。 |
| comparison operator | 比较运算符 | 如 ==、!=、<、>=，返回比较结果。 |
| equality | 相等性 | == 判断两个对象的值是否按规则相等。 |
| identity comparison | 身份比较 | is 与 is not 比较是否为同一对象。 |
| logical operator | 逻辑运算符 | and、or、not，支持短路求值。 |
| short-circuit evaluation | 短路求值 | 已足以确定结果时不再执行后续操作数。 |
| bitwise operator | 按位运算符 | 对整数位模式进行 &、\|、^、~、移位操作。 |
| membership test | 成员资格测试 | in / not in 判断元素是否在容器中。 |
| assignment | 赋值 | 用 = 将名称绑定到表达式的求值结果。 |
| augmented assignment | 增强赋值 | +=、*= 等，可能调用对象的就地运算方法。 |
| unpacking | 解包 | 将序列或可迭代对象的元素分配到多个目标。 |
| starred expression | 星号表达式 | 在解包或调用等位置使用 * 处理多个元素。 |
| walrus operator | 海象运算符 | := 是赋值表达式，在表达式中绑定名称。 |
| conditional expression | 条件表达式 | x if condition else y 的表达式形式。 |
| chained comparison | 链式比较 | 例如 0 < x < 10，避免重复求值中间操作数。 |
| operator overloading | 运算符重载 | 类通过特殊方法自定义运算符行为。 |
| bitwise OR type union | 类型联合写法 | 在类型表达式中用 X \| Y 表示联合类型。 |

<a id="chapter-05"></a>

## 05 控制流程与函数 / Control Flow & Functions

从分支、循环到函数调用，建立程序执行模型。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| conditional statement | 条件语句 | 使用 if、elif、else 选择执行分支。 |
| for loop | for 循环 | 依次取出可迭代对象中的元素执行代码块。 |
| while loop | while 循环 | 当条件保持为真时重复执行代码块。 |
| break | 跳出循环 | 提前结束最近一层循环。 |
| continue | 继续下一轮 | 跳过本轮剩余语句，开始下一次循环。 |
| pass | 空语句 | 语法上需要语句时使用的不执行操作的占位语句。 |
| loop else | 循环 else 子句 | 循环未通过 break 退出时执行的代码块。 |
| match statement | 模式匹配语句 | 使用 match/case 按结构模式选择分支。 |
| pattern matching | 模式匹配 | 按值、结构或绑定模式检查数据。 |
| function | 函数 | 可复用的可调用代码单元。 |
| function definition | 函数定义 | 用 def 创建函数对象并绑定名称。 |
| call | 调用 | 通过圆括号向可调用对象传入参数并执行。 |
| parameter | 形参 | 函数定义中声明的接收值的名称。 |
| argument | 实参 | 函数调用时实际传递的值或表达式。 |
| positional argument | 位置实参 | 依靠参数位置匹配形参的实参。 |
| keyword argument | 关键字实参 | 使用 name=value 显式指定目标形参。 |
| default argument value | 默认参数值 | 定义函数时计算、调用时可省略的形参默认值。 |
| mutable default pitfall | 可变默认参数陷阱 | 默认值对象在多次调用之间复用，可能意外共享状态。 |
| variadic positional parameters (*args) | 可变位置参数 | 接收多余位置实参并组成元组。 |
| variadic keyword parameters (**kwargs) | 可变关键字参数 | 接收多余关键字实参并组成字典。 |
| positional-only parameter | 仅限位置参数 | 定义中放在 / 之前，只能按位置传入。 |
| keyword-only parameter | 仅限关键字参数 | 定义中位于 * 之后，必须以关键字传入。 |
| return value | 返回值 | 函数执行 return 后交还调用者的结果。 |
| recursion | 递归 | 函数直接或间接调用自身。 |
| closure | 闭包 | 函数携带并访问其定义时外层作用域的绑定。 |
| LEGB rule | LEGB 名称查找规则 | Local、Enclosing、Global、Built-in 的常见查找顺序概括。 |
| global statement | global 声明 | 指定函数中某名称绑定到模块级命名空间。 |
| nonlocal statement | nonlocal 声明 | 指定名称绑定到最近的已有外层函数作用域。 |

<a id="chapter-06"></a>

## 06 类、面向对象与数据模型 / OOP & Data Model

理解对象协议、属性查找以及 Python 的“魔术方法”。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| class | 类 | 定义对象属性与行为的可调用构造模板。 |
| constructor call | 构造调用 | 调用类对象以创建并初始化实例。 |
| class attribute | 类属性 | 定义在类命名空间中的属性，可被实例读取。 |
| instance attribute | 实例属性 | 保存于某个实例自身的属性。 |
| method | 方法 | 通过对象属性访问、具有调用行为的函数或描述符。 |
| instance method | 实例方法 | 一般将实例作为第一个参数（惯例名 self）。 |
| class method | 类方法 | 经 @classmethod 装饰，将类作为第一个参数。 |
| static method | 静态方法 | 经 @staticmethod 装饰，不自动接收实例或类。 |
| inheritance | 继承 | 子类从基类获取可复用或可覆盖的行为。 |
| base class | 基类 | 被其他类继承的父类。 |
| subclass | 子类 | 从已有类派生出的类。 |
| multiple inheritance | 多重继承 | 一个类继承多个基类。 |
| method resolution order (MRO) | 方法解析顺序 | 多重继承下查找类属性的线性顺序。 |
| polymorphism | 多态 | 不同类型对象以共同接口参与相同操作。 |
| duck typing | 鸭子类型 | 更关注对象能做什么，而非其名义继承关系。 |
| encapsulation | 封装 | 通过接口组织对象的状态与行为；Python 主要依靠约定。 |
| property | 属性描述器 | property 允许通过属性访问调用 getter/setter。 |
| descriptor | 描述符 | 实现 __get__、__set__ 或 __delete__ 的属性协议对象。 |
| attribute lookup | 属性查找 | 解析 obj.attr 时依据数据模型执行的查找流程。 |
| special method | 特殊方法 | 如 __len__、__iter__，让对象参与语言协议。 |
| dunder method | 双下划线方法 | 对 __xxx__ 特殊方法的常用俗称。 |
| __init__() | 初始化方法 | 新实例创建后被调用，用于设置初始状态。 |
| __new__() | 实例创建方法 | 负责创建并返回实例，先于 __init__。 |
| __repr__() | 开发者表示方法 | 返回倾向于准确、可调试的对象字符串表示。 |
| __str__() | 字符串表示方法 | 定义 str(obj) 和 print(obj) 的友好文本形式。 |
| __eq__() | 相等比较方法 | 定义对象的 == 比较行为。 |
| __hash__() | 哈希方法 | 返回整数哈希值，需与相等性约束一致。 |
| __slots__ | 属性槽声明 | 可限制常规实例属性布局，常用于节省部分对象开销。 |
| metaclass | 元类 | 控制类对象创建与行为的类，常见默认元类为 type。 |
| abstract base class (ABC) | 抽象基类 | 通过 abc 提供抽象接口或虚拟子类机制。 |
| dataclass | 数据类 | 使用 @dataclass 自动生成常见数据承载类方法。 |

<a id="chapter-07"></a>

## 07 迭代器、生成器与函数式工具 / Iteration & Functional Tools

重点区分 iterable、iterator、generator 三类概念。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| iterable | 可迭代对象 | 能通过 iter() 取得迭代器的对象。 |
| iterator | 迭代器 | 实现 __next__() 并逐个提供元素的对象。 |
| iteration | 迭代 | 依次获取一系列元素的过程。 |
| iteration protocol | 迭代协议 | 由 __iter__() 与 __next__() 组成的常用接口。 |
| StopIteration | 迭代结束异常 | 迭代器耗尽时发出的终止信号。 |
| generator | 生成器 | 通常指由含 yield 的函数创建的迭代器。 |
| generator function | 生成器函数 | 函数体含 yield，调用后返回生成器对象。 |
| generator expression | 生成器表达式 | 如 (x*x for x in data) 的惰性迭代结构。 |
| yield | 产出并暂停 | 生成器发送一个值并保存执行现场。 |
| yield from | 委托产出 | 将产出与交互委托给子迭代器或生成器。 |
| next() | 获取下个元素 | 从迭代器中取一个元素，可设置耗尽默认值。 |
| iter() | 获取迭代器 | 对可迭代对象构造或取得迭代器。 |
| list comprehension | 列表推导式 | 由迭代表达式简洁构造列表。 |
| set comprehension | 集合推导式 | 由迭代表达式简洁构造集合。 |
| dictionary comprehension | 字典推导式 | 由键值表达式简洁构造字典。 |
| lazy evaluation | 惰性求值 | 仅在需要时计算后续数据或结果。 |
| eager evaluation | 立即求值 | 立即完成计算并产生完整结果。 |
| map() | 映射函数 | 对一个或多个可迭代对象逐项应用函数。 |
| filter() | 过滤函数 | 保留使谓词结果为真的输入元素。 |
| zip() | 并行打包函数 | 将多个可迭代对象按位置组合成元组。 |
| enumerate() | 带索引枚举 | 迭代时同时产生索引和值。 |
| functools | 函数式工具模块 | 提供 partial、reduce、缓存装饰器等。 |
| itertools | 迭代器工具模块 | 提供组合、排列、链式迭代等工具。 |
| partial function | 偏函数 | 固定某些实参以得到新的可调用对象。 |

<a id="chapter-08"></a>

## 08 异常处理与上下文管理 / Exceptions & Context Managers

理解异常链、资源释放及 with 所依赖的协议。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| exception | 异常 | 表示错误或特殊控制事件的对象。 |
| exception class | 异常类 | 用于表示某类异常的类型。 |
| raise statement | 抛出异常语句 | 使用 raise 发出异常。 |
| try statement | 尝试语句 | 捕获与清理异常的复合语句。 |
| except clause | 异常捕获子句 | 在异常匹配时执行恢复或处理逻辑。 |
| except* clause | 异常组捕获子句 | 按异常类型处理 ExceptionGroup 的子集。 |
| else clause | 无异常子句 | try 主体未抛出异常时执行的对应子句。 |
| finally clause | 最终清理子句 | 不论 try 如何退出通常都会执行的清理逻辑。 |
| exception chaining | 异常链 | 通过 __cause__、__context__ 记录异常间的关系。 |
| raise ... from ... | 显式异常原因 | 将一个异常明确设置为另一个异常的原因。 |
| traceback | 回溯信息 | 展示异常调用栈与代码位置的信息。 |
| stack frame | 栈帧 | 函数执行时携带局部变量等状态的运行记录。 |
| context manager | 上下文管理器 | 定义进入、退出受管理执行环境的对象。 |
| with statement | with 语句 | 通过上下文管理器管理资源范围。 |
| __enter__() | 进入上下文方法 | 进入 with 块前调用，返回绑定给 as 的对象。 |
| __exit__() | 退出上下文方法 | 离开 with 块时调用，可控制异常是否被抑制。 |
| contextlib | 上下文工具模块 | 提供 contextmanager、ExitStack 等工具。 |
| resource cleanup | 资源清理 | 关闭文件、释放锁等操作。 |
| custom exception | 自定义异常 | 应用代码定义的异常类，通常继承 Exception。 |
| BaseException | 异常基类 | 大多数可抛出异常的共同根类型。 |
| ExceptionGroup | 异常组 | 聚合多个异常以便统一传播与拆分处理。 |

<a id="chapter-09"></a>

## 09 模块、导入与项目结构 / Modules & Imports

区分 Python 可导入的模块与分发安装的包。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| module | 模块 | 可导入的 Python 代码组织单元。 |
| package | 包（导入包） | 组织子模块的可导入包；不同于发布分发包。 |
| submodule | 子模块 | 位于包之下的模块。 |
| import statement | 导入语句 | 使用 import 或 from ... import 绑定导入名称。 |
| absolute import | 绝对导入 | 从顶层包名称开始解析的导入方式。 |
| relative import | 相对导入 | 使用前导点号按包层级解析导入。 |
| import path | 模块搜索路径 | 导入系统查找模块所用的路径集合。 |
| sys.path | 模块搜索路径列表 | Python 导入器使用的重要路径序列。 |
| module cache | 模块缓存 | sys.modules 中已加载模块的映射。 |
| __name__ | 模块名称属性 | 模块作为脚本运行时通常为 '__main__'。 |
| __main__ | 主模块 | 解释器执行程序入口时使用的模块名。 |
| __init__.py | 包初始化文件 | 常规包中的初始化模块文件。 |
| namespace package | 命名空间包 | 可跨多个目录位置组成同一包的机制。 |
| importlib | 导入工具库 | 提供导入系统与模块加载的编程接口。 |
| module spec | 模块规格信息 | 描述模块加载器与来源等元数据的对象。 |
| relative path | 相对路径 | 相对于当前目录或基准目录的路径。 |
| absolute path | 绝对路径 | 从文件系统根或盘符基准定位的路径。 |
| project root | 项目根目录 | 项目配置与代码结构的顶层目录。 |
| source layout | 源码布局 | 例如 src/ 目录承载项目导入包的组织方式。 |
| circular import | 循环导入 | 模块互相依赖导入，可能在初始化中出现问题。 |
| entry point | 入口点 | 包元数据声明的可执行命令或插件入口。 |
| plugin | 插件 | 通过约定接口动态扩展宿主程序的组件。 |

<a id="chapter-10"></a>

## 10 类型注解与静态分析 / Typing & Static Analysis

类型注解主要服务静态工具；默认不强制运行时类型检查。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| type hint | 类型提示 | 用注解表达开发者预期的类型信息。 |
| type annotation | 类型注解 | 放在变量、形参或返回值上的类型表达式。 |
| static type checker | 静态类型检查器 | 不运行程序即可分析类型兼容性的工具。 |
| runtime type checking | 运行时类型检查 | 程序执行期间主动验证值的类型。 |
| typing module | typing 模块 | 提供 Python 类型系统相关构造与工具。 |
| Any | 任意类型 | 静态类型系统中的动态逃逸类型，削弱检查约束。 |
| object type | 顶层对象类型 | Python 类层次常见顶层类；静态意义不同于 Any。 |
| Union | 联合类型 | 表示值可能符合多个类型之一。 |
| Optional | 可选空值类型 | Optional[T] 等价于 T 与 None 的联合类型。 |
| Literal | 字面量类型 | 限定到某些具体字面值的静态类型。 |
| Annotated | 附加元数据类型 | 在基本类型上附加供工具使用的元数据。 |
| Callable | 可调用类型 | 描述参数与返回值形状的函数接口类型。 |
| Iterable | 可迭代协议类型 | 描述可通过迭代取元素的对象。 |
| Iterator | 迭代器协议类型 | 描述既可迭代又可提供下一元素的对象。 |
| Generator | 生成器类型 | 在类型层表示 yield、send、return 类型信息。 |
| Protocol | 协议类型 | 通过结构成员而非显式继承表达接口兼容性。 |
| structural subtyping | 结构化子类型 | 依据对象成员结构判断类型兼容性。 |
| nominal subtyping | 名义子类型 | 依据显式继承或注册关系判断子类型。 |
| TypeVar | 类型变量 | 在泛型定义中表达类型之间的关联。 |
| generic | 泛型 | 以类型参数描述可复用的类型或函数。 |
| ParamSpec | 参数规格变量 | 在高阶函数中保留被包装函数的参数形状。 |
| TypeAlias | 类型别名 | 为类型表达式赋予可复用名称。 |
| TypedDict | 带类型键的字典 | 为具有固定键结构的字典声明预期值类型。 |
| NewType | 新类型标记 | 为静态检查构造名义上不同的简单类型。 |
| Final | 不应重赋值标记 | 静态工具可检查被标记名称的重新赋值。 |
| overload | 重载声明 | 描述函数针对不同参数类型的多个静态签名。 |
| Self | 自身类型 | 在方法或类接口中引用当前类及其子类的类型。 |
| type narrowing | 类型缩窄 | 在条件判断后，将联合类型缩小到更具体类型。 |

<a id="chapter-11"></a>

## 11 异步编程与并发模型 / Async & Concurrency

区分并发与并行、协程与任务，以及线程和进程。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| concurrency | 并发 | 多项任务在时间上交错或协调推进。 |
| parallelism | 并行 | 多项计算在同一时刻实质上执行。 |
| asynchronous programming | 异步编程 | 使用非阻塞等待与任务调度组织工作。 |
| synchronous programming | 同步编程 | 按顺序执行并在调用完成后继续的常见模式。 |
| coroutine | 协程 | 可挂起并在之后恢复执行的计算对象。 |
| coroutine function | 协程函数 | 通过 async def 定义，调用后通常返回协程对象。 |
| awaitable | 可等待对象 | 可作为 await 表达式操作数的对象。 |
| await | 等待表达式 | 在协程中等待可等待对象，同时让出调度控制权。 |
| asyncio | 异步 I/O 标准库 | Python 提供事件循环、任务与异步同步原语的模块。 |
| event loop | 事件循环 | 负责调度异步回调、任务及 I/O 事件的核心组件。 |
| Task | 异步任务 | asyncio 中调度协程执行的可等待对象。 |
| Future | 未来结果对象 | 表示异步操作未来完成结果的可等待对象。 |
| async iterator | 异步迭代器 | 提供 __aiter__ 与异步 __anext__ 方法的对象。 |
| async for | 异步迭代语句 | 迭代异步迭代器的语法。 |
| async context manager | 异步上下文管理器 | 定义 __aenter__ 和 __aexit__ 的资源管理对象。 |
| async with | 异步 with 语句 | 以异步协议进入与退出上下文。 |
| asynchronous generator | 异步生成器 | 同时使用 async def 与 yield 定义的生成器机制。 |
| thread | 线程 | 进程内执行流，通常共享同一进程内存。 |
| process | 进程 | 操作系统管理的独立执行单元，通常有独立地址空间。 |
| threading | 线程模块 | 提供 Thread、Lock、Event 等线程同步接口。 |
| multiprocessing | 多进程模块 | 基于子进程提供并行计算与通信的工具。 |
| concurrent.futures | 并发任务接口 | 提供线程池、进程池与 Future 抽象。 |
| thread pool | 线程池 | 重用工作线程执行多个任务的机制。 |
| process pool | 进程池 | 重用工作进程执行多个任务的机制。 |
| lock | 互斥锁 | 限制共享资源被多个执行单元同时访问的同步原语。 |
| reentrant lock (RLock) | 可重入锁 | 同一线程可以多次获取的锁。 |
| semaphore | 信号量 | 限制同时进入某个资源区的执行单元数量。 |
| race condition | 竞态条件 | 程序结果依赖不受控执行时序的缺陷。 |
| deadlock | 死锁 | 多个执行单元相互等待导致无法继续推进。 |
| cancellation | 取消 | 请求异步任务停止，通常在可等待点传播取消异常。 |
| structured concurrency | 结构化并发 | 让子任务生命周期与明确的代码作用域绑定的设计思想。 |
| TaskGroup | 任务组 | asyncio 中用于成组管理子任务及异常传播的上下文管理器。 |
| Global Interpreter Lock (GIL) | 全局解释器锁 | 传统 CPython 构建中限制同一解释器内线程并行执行字节码的机制。 |
| free-threaded build | 自由线程构建 | 可禁用 GIL 的 CPython 构建模式，兼容性与行为需参照对应版本文档。 |

<a id="chapter-12"></a>

## 12 文件、I/O 与系统接口 / Files, I/O & OS

掌握文本、字节、路径、流和操作系统交互。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| I/O (input/output) | 输入/输出 | 程序与文件、终端或外部设备交换数据的活动。 |
| stream | 流 | 按顺序读写数据的抽象接口。 |
| text I/O | 文本输入输出 | 读写 str 并涉及字符编码/解码的 I/O。 |
| binary I/O | 二进制输入输出 | 读写 bytes 等二进制对象的 I/O。 |
| buffering | 缓冲 | 临时聚集数据以减少底层读写次数的机制。 |
| file object | 文件对象 | 提供 read、write、close 等接口的对象。 |
| file descriptor | 文件描述符 | 操作系统使用的打开文件资源整数标识。 |
| open() | 打开文件函数 | 返回适当类型的文件对象。 |
| encoding | 字符编码 | 在字符与字节之间进行映射的规则。 |
| decoding | 解码 | 将字节序列转换为字符文本的过程。 |
| newline translation | 换行符转换 | 文本 I/O 对不同平台换行形式的处理。 |
| pathlike object | 类路径对象 | 通过 __fspath__ 表示文件系统路径的对象。 |
| pathlib.Path | 路径对象 | 面向对象地处理文件与目录路径的类型。 |
| os module | 操作系统接口模块 | 提供环境变量、进程与文件系统相关操作。 |
| sys module | 解释器系统模块 | 提供 argv、path、stdout 等解释器级接口。 |
| stdin | 标准输入 | 程序默认接收输入的数据流。 |
| stdout | 标准输出 | 程序正常输出的默认流。 |
| stderr | 标准错误 | 程序诊断信息的默认输出流。 |
| environment variable | 环境变量 | 由进程环境提供的键值配置。 |
| subprocess | 子进程模块 | 启动、控制与通信外部程序的标准库模块。 |
| pipe | 管道 | 将一个进程的数据流连接到另一进程的通信机制。 |
| serialization | 序列化 | 将对象或数据结构编码成可保存/传输形式。 |
| deserialization | 反序列化 | 从编码格式恢复对应的数据结构。 |
| JSON | JSON 数据格式 | 通用文本数据交换格式，Python 常用 json 模块处理。 |
| pickle | Python 对象序列化 | pickle 能序列化大量 Python 对象，但不可加载不可信数据。 |
| CSV | 逗号分隔值格式 | 常用于表格型数据交换，分隔规则由方言决定。 |
| temporary file | 临时文件 | 为短期处理创建、通常需要及时清理的文件。 |

<a id="chapter-13"></a>

## 13 常用标准库与数据工具 / Standard Library Toolkit

常见标准库名称及其实际职责，便于查阅文档。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| collections | 集合工具模块 | 提供 deque、Counter、defaultdict 等容器。 |
| collections.abc | 容器抽象基类模块 | 定义 Iterable、Mapping、Sequence 等 ABC。 |
| dataclasses | 数据类模块 | 自动为数据类生成初始化和比较等方法。 |
| heapq | 堆队列模块 | 提供基于列表的小顶堆操作。 |
| bisect | 二分查找模块 | 在有序序列中查找插入位置。 |
| array | 同类型值数组模块 | 存储特定基本 C 类型数值的紧凑序列。 |
| math | 数学函数模块 | 提供实数数学函数与常量。 |
| statistics | 统计模块 | 提供均值、中位数、方差等基础统计工具。 |
| decimal | 十进制运算模块 | 提供可控制精度与舍入的十进制数。 |
| fractions | 有理数模块 | 通过 Fraction 表示分子、分母比值。 |
| random | 伪随机数模块 | 用于模拟等普通随机需求，不应用于密码安全。 |
| secrets | 安全随机工具 | 适于生成令牌等密码学用途的随机值。 |
| re | 正则表达式模块 | 提供文本模式匹配与替换功能。 |
| string | 字符串常量与模板 | 提供字符类别常量、Template 等。 |
| datetime | 日期时间模块 | 提供 date、time、datetime 和 timedelta。 |
| zoneinfo | 时区数据库接口 | 提供 IANA 时区数据库对应的时区对象。 |
| logging | 日志模块 | 支持等级、格式器、处理器的日志记录。 |
| argparse | 命令行参数模块 | 构建具有选项和帮助信息的命令行接口。 |
| configparser | INI 配置解析模块 | 读写传统 INI 风格配置文件。 |
| shutil | 高级文件操作模块 | 提供复制、移动、目录树操作等。 |
| functools.lru_cache | 最近最少使用缓存 | 按调用参数缓存函数结果的装饰器。 |
| weakref | 弱引用模块 | 引用对象而不阻止其被垃圾回收的工具。 |
| inspect | 内省工具模块 | 读取签名、源码及其他运行对象信息。 |
| importlib.metadata | 包元数据读取 | 查询已安装分发包的版本与元信息。 |

<a id="chapter-14"></a>

## 14 依赖、包管理与构建发布 / Packaging & Distribution

特别注意 import package 与 distribution package 并不总同名。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| package manager | 包管理器 | 安装、更新或管理可复用软件包的工具。 |
| pip | Python 包安装工具 | 常用的 Python 分发包安装前端。 |
| PyPI | Python 包索引 | Python 社区广泛使用的公开分发包索引服务。 |
| virtual environment | 虚拟环境 | 为项目隔离 Python 解释器环境与安装依赖的机制。 |
| venv | 虚拟环境模块 | 创建 Python 虚拟环境的标准库模块。 |
| site-packages | 第三方包安装目录 | 解释器环境中常见的已安装包位置。 |
| dependency | 依赖 | 项目正常运行或构建所依赖的其他包或组件。 |
| direct dependency | 直接依赖 | 项目显式声明依赖的软件包。 |
| transitive dependency | 传递依赖 | 因直接依赖的需求而间接引入的软件包。 |
| version specifier | 版本约束 | 指定可接受软件包版本范围的表达式。 |
| requirement | 安装需求 | 对需要安装的分发包及其约束的说明。 |
| requirements.txt | 依赖需求文件 | 常用于按行列出 pip 需要安装的需求。 |
| lock file | 锁定文件 | 记录经解析后的具体依赖版本/工件，格式因工具而异。 |
| reproducible build | 可复现构建 | 在规定条件下能重复产出相同工件的构建目标。 |
| pyproject.toml | Python 项目配置文件 | 声明构建系统、项目元数据及工具配置的 TOML 文件。 |
| [build-system] | 构建系统配置区 | pyproject.toml 中声明构建后端等设置的表。 |
| [project] | 项目元数据配置区 | pyproject.toml 中声明包名、版本、依赖等字段的表。 |
| build backend | 构建后端 | 按标准构建接口生成源码包或 wheel 的实现。 |
| build frontend | 构建前端 | 调用构建后端并管理构建流程的工具。 |
| source distribution (sdist) | 源码分发包 | 含构建所需源码和元数据的发布工件。 |
| wheel | Wheel 二进制分发包 | 可安装的构建分发格式，扩展模块可能含平台特定二进制文件。 |
| distribution package | 分发包 | 供包管理器发布与安装的项目版本工件。 |
| import package | 导入包 | import 语句访问的 Python 包结构。 |
| editable install | 可编辑安装 | 安装后可直接使用源码目录中改动的开发模式。 |
| semantic versioning | 语义化版本 | MAJOR.MINOR.PATCH 版本约定；并非全部 Python 项目都遵循。 |
| build artifact | 构建产物 | 构建系统生成的文件，如 wheel 或 sdist。 |
| package index | 包索引 | 托管并提供分发包发现/下载的仓库服务。 |

<a id="chapter-15"></a>

## 15 测试、调试与工程质量 / Testing & Engineering

从异常诊断到自动化质量保障的常用术语。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| test case | 测试用例 | 对某个预期行为进行输入与验证的独立检查。 |
| test suite | 测试套件 | 多个相关测试的集合。 |
| unit test | 单元测试 | 针对函数、类等较小代码单元的测试。 |
| integration test | 集成测试 | 验证多个组件一起工作的行为。 |
| end-to-end test | 端到端测试 | 模拟完整用户流程或系统路径的测试。 |
| regression test | 回归测试 | 确保代码变化未破坏既有行为的测试。 |
| assertion | 断言 | 对预期条件成立作出检查的表达式或工具。 |
| assert statement | assert 语句 | 在调试构建中检查条件；优化模式可能移除，不能用于安全校验。 |
| fixture | 测试夹具 | 为测试准备及清理环境、对象或数据的机制。 |
| mock | 模拟对象 | 用可控替身代替真实依赖以进行测试。 |
| monkeypatch | 动态替换 | 测试中临时替换模块属性、函数或环境配置的做法。 |
| code coverage | 代码覆盖率 | 衡量测试执行触及代码区域的程度。 |
| branch coverage | 分支覆盖率 | 衡量控制流各分支被测试执行的比例。 |
| property-based testing | 基于性质的测试 | 生成多种输入并验证通用不变量。 |
| parameterized test | 参数化测试 | 一份测试逻辑使用多组输入与期望结果。 |
| unittest | 单元测试标准库 | Python 自带的测试框架。 |
| pytest | pytest 测试框架 | 流行的第三方测试工具，支持 fixture 与参数化。 |
| debugger | 调试器 | 允许断点、单步执行与状态检查的工具。 |
| breakpoint | 断点 | 程序执行时主动暂停以便诊断的位置。 |
| pdb | Python 调试器 | 标准库提供的交互式调试工具。 |
| stack trace | 调用栈跟踪 | 展示函数调用链，常用于定位异常原因。 |
| linter | 静态规范检查器 | 检查潜在错误和编码风格问题的工具。 |
| formatter | 代码格式化器 | 自动统一缩进、换行等代码样式的工具。 |
| refactoring | 重构 | 在保持外部行为的条件下改进内部结构。 |
| continuous integration (CI) | 持续集成 | 自动构建、测试及验证代码变更的流程。 |
| pre-commit hook | 提交前钩子 | 在 Git 提交前运行检查或自动修复的机制。 |
| logging level | 日志级别 | DEBUG、INFO、WARNING、ERROR、CRITICAL 等等级。 |
| structured logging | 结构化日志 | 以 JSON 或字段形式输出便于机器分析的日志。 |

<a id="chapter-16"></a>

## 16 性能、内存与解释器内部 / Performance & Internals

这些概念常有实现差异，不宜把 CPython 细节泛化。

| English | 中文术语 | 简明释义 |
| --- | --- | --- |
| time complexity | 时间复杂度 | 分析算法运行开销随输入规模变化的量级。 |
| space complexity | 空间复杂度 | 分析额外内存开销随输入规模变化的量级。 |
| Big O notation | 大 O 记号 | 描述渐近上界或增长阶的常见记法。 |
| profiling | 性能剖析 | 测量程序各部分时间或资源使用的过程。 |
| profiler | 性能分析器 | 采集执行耗时、调用次数等指标的工具。 |
| cProfile | cProfile 分析器 | CPython 常见确定性函数级性能分析模块。 |
| timeit | 微基准测试模块 | 重复计时小段 Python 代码的工具。 |
| benchmark | 基准测试 | 在明确条件下比较性能的测试方法。 |
| latency | 延迟 | 单个请求或操作完成所花的时间。 |
| throughput | 吞吐量 | 单位时间可完成的任务或处理数据量。 |
| reference counting | 引用计数 | 以引用数量辅助管理对象生命周期的机制。 |
| cyclic garbage collector | 循环垃圾回收器 | 用来发现并回收某些引用环的机制。 |
| garbage collection (GC) | 垃圾回收 | 回收程序不再需要的对象占用资源的过程。 |
| memory leak | 内存泄漏 | 不再需要的数据仍被保留，导致内存占用增长。 |
| weak reference | 弱引用 | 不因自身存在而阻止对象回收的引用。 |
| object interning | 对象驻留 | 复用部分不可变对象实例的优化技术。 |
| small integer cache | 小整数缓存 | 某些 Python 实现对部分整数对象的复用优化。 |
| copy-on-write | 写时复制 | 共享数据直到有写入才进行复制的系统机制。 |
| stack | 栈 | 用于管理调用上下文等信息的数据结构概念。 |
| heap | 堆内存 | 动态分配对象通常使用的内存区域概念。 |
| heap allocation | 堆分配 | 从动态内存管理区域为对象分配空间。 |
| C extension | C 扩展模块 | 使用 C/C++ 等编写、以原生扩展形式加载的模块。 |
| Python C API | Python C 接口 | 供原生代码与 Python 运行时交互的接口集合。 |
| ABI | 应用二进制接口 | 二进制模块间调用约定、符号和数据布局等契约。 |
| stable ABI | 稳定 ABI | Python 为兼容多个 CPython 版本提供的受限二进制接口。 |
| bytecode cache | 字节码缓存 | 常以 __pycache__ 下的 .pyc 文件保存编译结果。 |
| __pycache__ | 字节码缓存目录 | 通常存放解释器生成的版本标记 .pyc 文件。 |
| JIT compilation | 即时编译 | 运行时将热点代码转成更低层指令的技术。 |
| vectorization | 向量化 | 用批量运算代替逐元素 Python 级循环的优化方法。 |

<a id="appendix-a"></a>
## 附录 A：易混淆概念速查

| 易混淆术语 | 核心区别 |
| --- | --- |
| iterable / iterator | 可迭代对象能产生迭代器；迭代器保存迭代状态，通常只能顺序消耗。 |
| is / == | is 比身份；== 比相等性。比较 None 通常使用 is None。 |
| list / tuple | 前者可变；后者不可变，但元组可以持有可变对象。 |
| shallow copy / deep copy | 浅拷贝通常共享嵌套对象；深拷贝尝试递归复制。 |
| argument / parameter | 调用处传入 argument；定义处声明 parameter。 |
| generator function / generator | 调用生成器函数才得到生成器对象；函数体不会立即完整运行。 |
| coroutine function / coroutine | async def 定义的是协程函数；调用通常创建协程对象，不代表自动调度。 |
| concurrency / parallelism | 并发是多个任务协调推进；并行强调实际同时执行。 |
| thread / process | 线程通常共享内存；进程通常拥有独立的地址空间。 |
| module / import package / distribution package | 可导入模块、导入包与安装分发包是不同层级概念，名称也不必相同。 |
| type hint / runtime check | 类型提示默认不会自动阻止不匹配的运行时值。 |
| staticmethod / classmethod | 前者不自动绑定类或实例；后者绑定类对象。 |
| encoding / decoding | 编码将文本映射成字节；解码将字节还原为文本。 |
| wheel / sdist | wheel 是可安装构建分发格式；sdist 提供源代码以供构建。 |
| GIL / free-threaded | GIL 取决于解释器与构建模式；不能简单说所有 Python 都始终有同一把锁。 |
| assert / validation | assert 可被优化关闭，不应替代输入验证或权限检查。 |

<a id="appendix-b"></a>
## 附录 B：英文 A-Z 索引

| English | 中文 | 章节 |
| --- | --- | --- |
| [build-system] | 构建系统配置区 | 14 依赖、包管理与构建发布 |
| [project] | 项目元数据配置区 | 14 依赖、包管理与构建发布 |
| __enter__() | 进入上下文方法 | 08 异常处理与上下文管理 |
| __eq__() | 相等比较方法 | 06 类、面向对象与数据模型 |
| __exit__() | 退出上下文方法 | 08 异常处理与上下文管理 |
| __hash__() | 哈希方法 | 06 类、面向对象与数据模型 |
| __init__() | 初始化方法 | 06 类、面向对象与数据模型 |
| __init__.py | 包初始化文件 | 09 模块、导入与项目结构 |
| __main__ | 主模块 | 09 模块、导入与项目结构 |
| __name__ | 模块名称属性 | 09 模块、导入与项目结构 |
| __new__() | 实例创建方法 | 06 类、面向对象与数据模型 |
| __pycache__ | 字节码缓存目录 | 16 性能、内存与解释器内部 |
| __repr__() | 开发者表示方法 | 06 类、面向对象与数据模型 |
| __slots__ | 属性槽声明 | 06 类、面向对象与数据模型 |
| __str__() | 字符串表示方法 | 06 类、面向对象与数据模型 |
| ABI | 应用二进制接口 | 16 性能、内存与解释器内部 |
| absolute import | 绝对导入 | 09 模块、导入与项目结构 |
| absolute path | 绝对路径 | 09 模块、导入与项目结构 |
| abstract base class (ABC) | 抽象基类 | 06 类、面向对象与数据模型 |
| Annotated | 附加元数据类型 | 10 类型注解与静态分析 |
| Any | 任意类型 | 10 类型注解与静态分析 |
| argparse | 命令行参数模块 | 13 常用标准库与数据工具 |
| argument | 实参 | 05 控制流程与函数 |
| arithmetic operator | 算术运算符 | 04 表达式、运算符与赋值 |
| array | 同类型值数组模块 | 13 常用标准库与数据工具 |
| assert statement | assert 语句 | 15 测试、调试与工程质量 |
| assertion | 断言 | 15 测试、调试与工程质量 |
| assignment | 赋值 | 04 表达式、运算符与赋值 |
| associativity | 结合性 | 04 表达式、运算符与赋值 |
| async context manager | 异步上下文管理器 | 11 异步编程与并发模型 |
| async for | 异步迭代语句 | 11 异步编程与并发模型 |
| async iterator | 异步迭代器 | 11 异步编程与并发模型 |
| async with | 异步 with 语句 | 11 异步编程与并发模型 |
| asynchronous generator | 异步生成器 | 11 异步编程与并发模型 |
| asynchronous programming | 异步编程 | 11 异步编程与并发模型 |
| asyncio | 异步 I/O 标准库 | 11 异步编程与并发模型 |
| attribute lookup | 属性查找 | 06 类、面向对象与数据模型 |
| augmented assignment | 增强赋值 | 04 表达式、运算符与赋值 |
| await | 等待表达式 | 11 异步编程与并发模型 |
| awaitable | 可等待对象 | 11 异步编程与并发模型 |
| backward compatibility | 向后兼容 | 01 语言与运行环境 |
| base class | 基类 | 06 类、面向对象与数据模型 |
| BaseException | 异常基类 | 08 异常处理与上下文管理 |
| benchmark | 基准测试 | 16 性能、内存与解释器内部 |
| Big O notation | 大 O 记号 | 16 性能、内存与解释器内部 |
| binary I/O | 二进制输入输出 | 12 文件、I/O 与系统接口 |
| bisect | 二分查找模块 | 13 常用标准库与数据工具 |
| bitwise operator | 按位运算符 | 04 表达式、运算符与赋值 |
| bitwise OR type union | 类型联合写法 | 04 表达式、运算符与赋值 |
| block | 代码块 | 02 词法、语法与源文件 |
| boolean | 布尔值 | 03 类型、对象与容器 |
| branch coverage | 分支覆盖率 | 15 测试、调试与工程质量 |
| break | 跳出循环 | 05 控制流程与函数 |
| breakpoint | 断点 | 15 测试、调试与工程质量 |
| buffering | 缓冲 | 12 文件、I/O 与系统接口 |
| build artifact | 构建产物 | 14 依赖、包管理与构建发布 |
| build backend | 构建后端 | 14 依赖、包管理与构建发布 |
| build frontend | 构建前端 | 14 依赖、包管理与构建发布 |
| built-in function | 内置函数 | 01 语言与运行环境 |
| built-in type | 内置类型 | 01 语言与运行环境 |
| bytearray | 可变字节数组 | 03 类型、对象与容器 |
| bytecode | 字节码 | 01 语言与运行环境 |
| bytecode cache | 字节码缓存 | 16 性能、内存与解释器内部 |
| bytes | 字节串 | 03 类型、对象与容器 |
| bytes-like object | 类字节对象 | 03 类型、对象与容器 |
| C extension | C 扩展模块 | 16 性能、内存与解释器内部 |
| call | 调用 | 05 控制流程与函数 |
| Callable | 可调用类型 | 10 类型注解与静态分析 |
| cancellation | 取消 | 11 异步编程与并发模型 |
| chained comparison | 链式比较 | 04 表达式、运算符与赋值 |
| circular import | 循环导入 | 09 模块、导入与项目结构 |
| class | 类 | 06 类、面向对象与数据模型 |
| class attribute | 类属性 | 06 类、面向对象与数据模型 |
| class method | 类方法 | 06 类、面向对象与数据模型 |
| closure | 闭包 | 05 控制流程与函数 |
| code coverage | 代码覆盖率 | 15 测试、调试与工程质量 |
| code object | 代码对象 | 01 语言与运行环境 |
| collections | 集合工具模块 | 13 常用标准库与数据工具 |
| collections.abc | 容器抽象基类模块 | 13 常用标准库与数据工具 |
| comment | 注释 | 02 词法、语法与源文件 |
| comparison operator | 比较运算符 | 04 表达式、运算符与赋值 |
| complex number | 复数 | 03 类型、对象与容器 |
| compound statement | 复合语句 | 02 词法、语法与源文件 |
| concurrency | 并发 | 11 异步编程与并发模型 |
| concurrent.futures | 并发任务接口 | 11 异步编程与并发模型 |
| conditional expression | 条件表达式 | 04 表达式、运算符与赋值 |
| conditional statement | 条件语句 | 05 控制流程与函数 |
| configparser | INI 配置解析模块 | 13 常用标准库与数据工具 |
| constructor call | 构造调用 | 06 类、面向对象与数据模型 |
| container | 容器 | 03 类型、对象与容器 |
| context manager | 上下文管理器 | 08 异常处理与上下文管理 |
| contextlib | 上下文工具模块 | 08 异常处理与上下文管理 |
| continue | 继续下一轮 | 05 控制流程与函数 |
| continuous integration (CI) | 持续集成 | 15 测试、调试与工程质量 |
| copy-on-write | 写时复制 | 16 性能、内存与解释器内部 |
| coroutine | 协程 | 11 异步编程与并发模型 |
| coroutine function | 协程函数 | 11 异步编程与并发模型 |
| cProfile | cProfile 分析器 | 16 性能、内存与解释器内部 |
| CPython | CPython 解释器 | 01 语言与运行环境 |
| CSV | 逗号分隔值格式 | 12 文件、I/O 与系统接口 |
| custom exception | 自定义异常 | 08 异常处理与上下文管理 |
| cyclic garbage collector | 循环垃圾回收器 | 16 性能、内存与解释器内部 |
| dataclass | 数据类 | 06 类、面向对象与数据模型 |
| dataclasses | 数据类模块 | 13 常用标准库与数据工具 |
| datetime | 日期时间模块 | 13 常用标准库与数据工具 |
| deadlock | 死锁 | 11 异步编程与并发模型 |
| debugger | 调试器 | 15 测试、调试与工程质量 |
| decimal | 十进制运算模块 | 13 常用标准库与数据工具 |
| decoding | 解码 | 12 文件、I/O 与系统接口 |
| deep copy | 深拷贝 | 03 类型、对象与容器 |
| default argument value | 默认参数值 | 05 控制流程与函数 |
| dependency | 依赖 | 14 依赖、包管理与构建发布 |
| descriptor | 描述符 | 06 类、面向对象与数据模型 |
| deserialization | 反序列化 | 12 文件、I/O 与系统接口 |
| dictionary (dict) | 字典 | 03 类型、对象与容器 |
| dictionary comprehension | 字典推导式 | 07 迭代器、生成器与函数式工具 |
| dictionary view | 字典视图 | 03 类型、对象与容器 |
| direct dependency | 直接依赖 | 14 依赖、包管理与构建发布 |
| distribution package | 分发包 | 14 依赖、包管理与构建发布 |
| docstring | 文档字符串 | 02 词法、语法与源文件 |
| duck typing | 鸭子类型 | 06 类、面向对象与数据模型 |
| dunder method | 双下划线方法 | 06 类、面向对象与数据模型 |
| eager evaluation | 立即求值 | 07 迭代器、生成器与函数式工具 |
| editable install | 可编辑安装 | 14 依赖、包管理与构建发布 |
| else clause | 无异常子句 | 08 异常处理与上下文管理 |
| encapsulation | 封装 | 06 类、面向对象与数据模型 |
| encoding | 字符编码 | 12 文件、I/O 与系统接口 |
| encoding declaration | 编码声明 | 02 词法、语法与源文件 |
| end-to-end test | 端到端测试 | 15 测试、调试与工程质量 |
| entry point | 入口点 | 09 模块、导入与项目结构 |
| enumerate() | 带索引枚举 | 07 迭代器、生成器与函数式工具 |
| environment variable | 环境变量 | 12 文件、I/O 与系统接口 |
| equality | 相等性 | 04 表达式、运算符与赋值 |
| escape sequence | 转义序列 | 02 词法、语法与源文件 |
| event loop | 事件循环 | 11 异步编程与并发模型 |
| except clause | 异常捕获子句 | 08 异常处理与上下文管理 |
| except* clause | 异常组捕获子句 | 08 异常处理与上下文管理 |
| exception | 异常 | 08 异常处理与上下文管理 |
| exception chaining | 异常链 | 08 异常处理与上下文管理 |
| exception class | 异常类 | 08 异常处理与上下文管理 |
| ExceptionGroup | 异常组 | 08 异常处理与上下文管理 |
| exponentiation | 幂运算 | 04 表达式、运算符与赋值 |
| expression | 表达式 | 02 词法、语法与源文件 |
| f-string | 格式化字符串字面量 | 02 词法、语法与源文件 |
| file descriptor | 文件描述符 | 12 文件、I/O 与系统接口 |
| file object | 文件对象 | 12 文件、I/O 与系统接口 |
| filter() | 过滤函数 | 07 迭代器、生成器与函数式工具 |
| Final | 不应重赋值标记 | 10 类型注解与静态分析 |
| finally clause | 最终清理子句 | 08 异常处理与上下文管理 |
| fixture | 测试夹具 | 15 测试、调试与工程质量 |
| floating-point number | 浮点数 | 03 类型、对象与容器 |
| floor division | 向下取整除法 | 04 表达式、运算符与赋值 |
| for loop | for 循环 | 05 控制流程与函数 |
| formatter | 代码格式化器 | 15 测试、调试与工程质量 |
| fractions | 有理数模块 | 13 常用标准库与数据工具 |
| free-threaded build | 自由线程构建 | 11 异步编程与并发模型 |
| frozenset | 不可变集合 | 03 类型、对象与容器 |
| function | 函数 | 05 控制流程与函数 |
| function definition | 函数定义 | 05 控制流程与函数 |
| functools | 函数式工具模块 | 07 迭代器、生成器与函数式工具 |
| functools.lru_cache | 最近最少使用缓存 | 13 常用标准库与数据工具 |
| Future | 未来结果对象 | 11 异步编程与并发模型 |
| garbage collection (GC) | 垃圾回收 | 16 性能、内存与解释器内部 |
| generator | 生成器 | 07 迭代器、生成器与函数式工具 |
| Generator | 生成器类型 | 10 类型注解与静态分析 |
| generator expression | 生成器表达式 | 07 迭代器、生成器与函数式工具 |
| generator function | 生成器函数 | 07 迭代器、生成器与函数式工具 |
| generic | 泛型 | 10 类型注解与静态分析 |
| Global Interpreter Lock (GIL) | 全局解释器锁 | 11 异步编程与并发模型 |
| global statement | global 声明 | 05 控制流程与函数 |
| hash value | 哈希值 | 03 类型、对象与容器 |
| hashable | 可哈希的 | 03 类型、对象与容器 |
| heap | 堆内存 | 16 性能、内存与解释器内部 |
| heap allocation | 堆分配 | 16 性能、内存与解释器内部 |
| heapq | 堆队列模块 | 13 常用标准库与数据工具 |
| I/O (input/output) | 输入/输出 | 12 文件、I/O 与系统接口 |
| identifier | 标识符 | 02 词法、语法与源文件 |
| identity | 身份标识 | 01 语言与运行环境 |
| identity comparison | 身份比较 | 04 表达式、运算符与赋值 |
| immutable | 不可变的 | 03 类型、对象与容器 |
| implementation detail | 实现细节 | 01 语言与运行环境 |
| import package | 导入包 | 14 依赖、包管理与构建发布 |
| import path | 模块搜索路径 | 09 模块、导入与项目结构 |
| import statement | 导入语句 | 09 模块、导入与项目结构 |
| importlib | 导入工具库 | 09 模块、导入与项目结构 |
| importlib.metadata | 包元数据读取 | 13 常用标准库与数据工具 |
| indentation | 缩进 | 02 词法、语法与源文件 |
| inheritance | 继承 | 06 类、面向对象与数据模型 |
| inspect | 内省工具模块 | 13 常用标准库与数据工具 |
| instance | 实例 | 03 类型、对象与容器 |
| instance attribute | 实例属性 | 06 类、面向对象与数据模型 |
| instance method | 实例方法 | 06 类、面向对象与数据模型 |
| integer | 整数 | 03 类型、对象与容器 |
| integration test | 集成测试 | 15 测试、调试与工程质量 |
| interactive mode | 交互模式 | 01 语言与运行环境 |
| interpreter | 解释器 | 01 语言与运行环境 |
| iter() | 获取迭代器 | 07 迭代器、生成器与函数式工具 |
| iterable | 可迭代对象 | 07 迭代器、生成器与函数式工具 |
| Iterable | 可迭代协议类型 | 10 类型注解与静态分析 |
| iteration | 迭代 | 07 迭代器、生成器与函数式工具 |
| iteration protocol | 迭代协议 | 07 迭代器、生成器与函数式工具 |
| iterator | 迭代器 | 07 迭代器、生成器与函数式工具 |
| Iterator | 迭代器协议类型 | 10 类型注解与静态分析 |
| itertools | 迭代器工具模块 | 07 迭代器、生成器与函数式工具 |
| JIT compilation | 即时编译 | 16 性能、内存与解释器内部 |
| JSON | JSON 数据格式 | 12 文件、I/O 与系统接口 |
| keyword | 关键字 | 02 词法、语法与源文件 |
| keyword argument | 关键字实参 | 05 控制流程与函数 |
| keyword-only parameter | 仅限关键字参数 | 05 控制流程与函数 |
| latency | 延迟 | 16 性能、内存与解释器内部 |
| lazy evaluation | 惰性求值 | 07 迭代器、生成器与函数式工具 |
| LEGB rule | LEGB 名称查找规则 | 05 控制流程与函数 |
| linter | 静态规范检查器 | 15 测试、调试与工程质量 |
| list | 列表 | 03 类型、对象与容器 |
| list comprehension | 列表推导式 | 07 迭代器、生成器与函数式工具 |
| literal | 字面量 | 02 词法、语法与源文件 |
| Literal | 字面量类型 | 10 类型注解与静态分析 |
| lock | 互斥锁 | 11 异步编程与并发模型 |
| lock file | 锁定文件 | 14 依赖、包管理与构建发布 |
| logging | 日志模块 | 13 常用标准库与数据工具 |
| logging level | 日志级别 | 15 测试、调试与工程质量 |
| logical line | 逻辑行 | 02 词法、语法与源文件 |
| logical operator | 逻辑运算符 | 04 表达式、运算符与赋值 |
| loop else | 循环 else 子句 | 05 控制流程与函数 |
| map() | 映射函数 | 07 迭代器、生成器与函数式工具 |
| mapping | 映射 | 03 类型、对象与容器 |
| match statement | 模式匹配语句 | 05 控制流程与函数 |
| math | 数学函数模块 | 13 常用标准库与数据工具 |
| membership test | 成员资格测试 | 04 表达式、运算符与赋值 |
| memory leak | 内存泄漏 | 16 性能、内存与解释器内部 |
| memoryview | 内存视图 | 03 类型、对象与容器 |
| metaclass | 元类 | 06 类、面向对象与数据模型 |
| method | 方法 | 06 类、面向对象与数据模型 |
| method resolution order (MRO) | 方法解析顺序 | 06 类、面向对象与数据模型 |
| mock | 模拟对象 | 15 测试、调试与工程质量 |
| module | 模块 | 09 模块、导入与项目结构 |
| module cache | 模块缓存 | 09 模块、导入与项目结构 |
| module spec | 模块规格信息 | 09 模块、导入与项目结构 |
| modulo | 取模运算 | 04 表达式、运算符与赋值 |
| monkeypatch | 动态替换 | 15 测试、调试与工程质量 |
| multiple inheritance | 多重继承 | 06 类、面向对象与数据模型 |
| multiprocessing | 多进程模块 | 11 异步编程与并发模型 |
| mutable | 可变的 | 03 类型、对象与容器 |
| mutable default pitfall | 可变默认参数陷阱 | 05 控制流程与函数 |
| name binding | 名称绑定 | 01 语言与运行环境 |
| namespace | 命名空间 | 01 语言与运行环境 |
| namespace package | 命名空间包 | 09 模块、导入与项目结构 |
| newline translation | 换行符转换 | 12 文件、I/O 与系统接口 |
| NewType | 新类型标记 | 10 类型注解与静态分析 |
| next() | 获取下个元素 | 07 迭代器、生成器与函数式工具 |
| nominal subtyping | 名义子类型 | 10 类型注解与静态分析 |
| None | 空值对象 | 03 类型、对象与容器 |
| NoneType | 空值类型 | 03 类型、对象与容器 |
| nonlocal statement | nonlocal 声明 | 05 控制流程与函数 |
| object | 对象 | 01 语言与运行环境 |
| object interning | 对象驻留 | 16 性能、内存与解释器内部 |
| object type | 顶层对象类型 | 10 类型注解与静态分析 |
| open() | 打开文件函数 | 12 文件、I/O 与系统接口 |
| operand | 操作数 | 04 表达式、运算符与赋值 |
| operator | 运算符 | 04 表达式、运算符与赋值 |
| operator overloading | 运算符重载 | 04 表达式、运算符与赋值 |
| operator precedence | 运算符优先级 | 04 表达式、运算符与赋值 |
| Optional | 可选空值类型 | 10 类型注解与静态分析 |
| os module | 操作系统接口模块 | 12 文件、I/O 与系统接口 |
| overload | 重载声明 | 10 类型注解与静态分析 |
| package | 包（导入包） | 09 模块、导入与项目结构 |
| package index | 包索引 | 14 依赖、包管理与构建发布 |
| package manager | 包管理器 | 14 依赖、包管理与构建发布 |
| parallelism | 并行 | 11 异步编程与并发模型 |
| parameter | 形参 | 05 控制流程与函数 |
| parameterized test | 参数化测试 | 15 测试、调试与工程质量 |
| ParamSpec | 参数规格变量 | 10 类型注解与静态分析 |
| partial function | 偏函数 | 07 迭代器、生成器与函数式工具 |
| pass | 空语句 | 05 控制流程与函数 |
| pathlib.Path | 路径对象 | 12 文件、I/O 与系统接口 |
| pathlike object | 类路径对象 | 12 文件、I/O 与系统接口 |
| pattern matching | 模式匹配 | 05 控制流程与函数 |
| pdb | Python 调试器 | 15 测试、调试与工程质量 |
| PEP 8 | Python 代码风格指南 | 02 词法、语法与源文件 |
| physical line | 物理行 | 02 词法、语法与源文件 |
| pickle | Python 对象序列化 | 12 文件、I/O 与系统接口 |
| pip | Python 包安装工具 | 14 依赖、包管理与构建发布 |
| pipe | 管道 | 12 文件、I/O 与系统接口 |
| plugin | 插件 | 09 模块、导入与项目结构 |
| polymorphism | 多态 | 06 类、面向对象与数据模型 |
| positional argument | 位置实参 | 05 控制流程与函数 |
| positional-only parameter | 仅限位置参数 | 05 控制流程与函数 |
| pre-commit hook | 提交前钩子 | 15 测试、调试与工程质量 |
| process | 进程 | 11 异步编程与并发模型 |
| process pool | 进程池 | 11 异步编程与并发模型 |
| profiler | 性能分析器 | 16 性能、内存与解释器内部 |
| profiling | 性能剖析 | 16 性能、内存与解释器内部 |
| project root | 项目根目录 | 09 模块、导入与项目结构 |
| property | 属性描述器 | 06 类、面向对象与数据模型 |
| property-based testing | 基于性质的测试 | 15 测试、调试与工程质量 |
| Protocol | 协议类型 | 10 类型注解与静态分析 |
| PyPI | Python 包索引 | 14 依赖、包管理与构建发布 |
| pyproject.toml | Python 项目配置文件 | 14 依赖、包管理与构建发布 |
| pytest | pytest 测试框架 | 15 测试、调试与工程质量 |
| Python | Python 编程语言 | 01 语言与运行环境 |
| Python C API | Python C 接口 | 16 性能、内存与解释器内部 |
| Python Enhancement Proposal (PEP) | Python 增强提案 | 01 语言与运行环境 |
| Python implementation | Python 实现 | 01 语言与运行环境 |
| race condition | 竞态条件 | 11 异步编程与并发模型 |
| raise ... from ... | 显式异常原因 | 08 异常处理与上下文管理 |
| raise statement | 抛出异常语句 | 08 异常处理与上下文管理 |
| random | 伪随机数模块 | 13 常用标准库与数据工具 |
| range | 范围对象 | 03 类型、对象与容器 |
| raw string | 原始字符串 | 02 词法、语法与源文件 |
| re | 正则表达式模块 | 13 常用标准库与数据工具 |
| recursion | 递归 | 05 控制流程与函数 |
| reentrant lock (RLock) | 可重入锁 | 11 异步编程与并发模型 |
| refactoring | 重构 | 15 测试、调试与工程质量 |
| reference | 引用 | 01 语言与运行环境 |
| reference counting | 引用计数 | 16 性能、内存与解释器内部 |
| regression test | 回归测试 | 15 测试、调试与工程质量 |
| relative import | 相对导入 | 09 模块、导入与项目结构 |
| relative path | 相对路径 | 09 模块、导入与项目结构 |
| REPL | 读取-求值-输出循环 | 01 语言与运行环境 |
| reproducible build | 可复现构建 | 14 依赖、包管理与构建发布 |
| requirement | 安装需求 | 14 依赖、包管理与构建发布 |
| requirements.txt | 依赖需求文件 | 14 依赖、包管理与构建发布 |
| resource cleanup | 资源清理 | 08 异常处理与上下文管理 |
| return value | 返回值 | 05 控制流程与函数 |
| runtime | 运行时 | 01 语言与运行环境 |
| runtime type checking | 运行时类型检查 | 10 类型注解与静态分析 |
| scope | 作用域 | 01 语言与运行环境 |
| script | 脚本 | 01 语言与运行环境 |
| secrets | 安全随机工具 | 13 常用标准库与数据工具 |
| Self | 自身类型 | 10 类型注解与静态分析 |
| semantic meaning | 语义 | 02 词法、语法与源文件 |
| semantic versioning | 语义化版本 | 14 依赖、包管理与构建发布 |
| semaphore | 信号量 | 11 异步编程与并发模型 |
| sequence | 序列 | 03 类型、对象与容器 |
| serialization | 序列化 | 12 文件、I/O 与系统接口 |
| set | 集合 | 03 类型、对象与容器 |
| set comprehension | 集合推导式 | 07 迭代器、生成器与函数式工具 |
| shallow copy | 浅拷贝 | 03 类型、对象与容器 |
| short-circuit evaluation | 短路求值 | 04 表达式、运算符与赋值 |
| shutil | 高级文件操作模块 | 13 常用标准库与数据工具 |
| simple statement | 简单语句 | 02 词法、语法与源文件 |
| site-packages | 第三方包安装目录 | 14 依赖、包管理与构建发布 |
| slice | 切片 | 03 类型、对象与容器 |
| small integer cache | 小整数缓存 | 16 性能、内存与解释器内部 |
| soft keyword | 软关键字 | 02 词法、语法与源文件 |
| source code | 源代码 | 01 语言与运行环境 |
| source distribution (sdist) | 源码分发包 | 14 依赖、包管理与构建发布 |
| source layout | 源码布局 | 09 模块、导入与项目结构 |
| space complexity | 空间复杂度 | 16 性能、内存与解释器内部 |
| special method | 特殊方法 | 06 类、面向对象与数据模型 |
| stable ABI | 稳定 ABI | 16 性能、内存与解释器内部 |
| stack | 栈 | 16 性能、内存与解释器内部 |
| stack frame | 栈帧 | 08 异常处理与上下文管理 |
| stack trace | 调用栈跟踪 | 15 测试、调试与工程质量 |
| standard library | 标准库 | 01 语言与运行环境 |
| starred expression | 星号表达式 | 04 表达式、运算符与赋值 |
| statement | 语句 | 02 词法、语法与源文件 |
| static method | 静态方法 | 06 类、面向对象与数据模型 |
| static type checker | 静态类型检查器 | 10 类型注解与静态分析 |
| statistics | 统计模块 | 13 常用标准库与数据工具 |
| stderr | 标准错误 | 12 文件、I/O 与系统接口 |
| stdin | 标准输入 | 12 文件、I/O 与系统接口 |
| stdout | 标准输出 | 12 文件、I/O 与系统接口 |
| StopIteration | 迭代结束异常 | 07 迭代器、生成器与函数式工具 |
| stream | 流 | 12 文件、I/O 与系统接口 |
| string | 字符串常量与模板 | 13 常用标准库与数据工具 |
| string (str) | 字符串 | 03 类型、对象与容器 |
| string prefix | 字符串前缀 | 02 词法、语法与源文件 |
| structural subtyping | 结构化子类型 | 10 类型注解与静态分析 |
| structured concurrency | 结构化并发 | 11 异步编程与并发模型 |
| structured logging | 结构化日志 | 15 测试、调试与工程质量 |
| subclass | 子类 | 06 类、面向对象与数据模型 |
| submodule | 子模块 | 09 模块、导入与项目结构 |
| subprocess | 子进程模块 | 12 文件、I/O 与系统接口 |
| subscript | 下标访问 | 03 类型、对象与容器 |
| synchronous programming | 同步编程 | 11 异步编程与并发模型 |
| syntax error | 语法错误 | 02 词法、语法与源文件 |
| sys module | 解释器系统模块 | 12 文件、I/O 与系统接口 |
| sys.path | 模块搜索路径列表 | 09 模块、导入与项目结构 |
| Task | 异步任务 | 11 异步编程与并发模型 |
| TaskGroup | 任务组 | 11 异步编程与并发模型 |
| temporary file | 临时文件 | 12 文件、I/O 与系统接口 |
| test case | 测试用例 | 15 测试、调试与工程质量 |
| test suite | 测试套件 | 15 测试、调试与工程质量 |
| text I/O | 文本输入输出 | 12 文件、I/O 与系统接口 |
| thread | 线程 | 11 异步编程与并发模型 |
| thread pool | 线程池 | 11 异步编程与并发模型 |
| threading | 线程模块 | 11 异步编程与并发模型 |
| throughput | 吞吐量 | 16 性能、内存与解释器内部 |
| time complexity | 时间复杂度 | 16 性能、内存与解释器内部 |
| timeit | 微基准测试模块 | 16 性能、内存与解释器内部 |
| token | 词法单元 | 02 词法、语法与源文件 |
| traceback | 回溯信息 | 08 异常处理与上下文管理 |
| transitive dependency | 传递依赖 | 14 依赖、包管理与构建发布 |
| truth value testing | 真值测试 | 03 类型、对象与容器 |
| try statement | 尝试语句 | 08 异常处理与上下文管理 |
| tuple | 元组 | 03 类型、对象与容器 |
| type | 类型 | 03 类型、对象与容器 |
| type annotation | 类型注解 | 10 类型注解与静态分析 |
| type annotation syntax | 类型注解语法 | 02 词法、语法与源文件 |
| type hint | 类型提示 | 10 类型注解与静态分析 |
| type narrowing | 类型缩窄 | 10 类型注解与静态分析 |
| TypeAlias | 类型别名 | 10 类型注解与静态分析 |
| TypedDict | 带类型键的字典 | 10 类型注解与静态分析 |
| TypeVar | 类型变量 | 10 类型注解与静态分析 |
| typing module | typing 模块 | 10 类型注解与静态分析 |
| Union | 联合类型 | 10 类型注解与静态分析 |
| unit test | 单元测试 | 15 测试、调试与工程质量 |
| unittest | 单元测试标准库 | 15 测试、调试与工程质量 |
| unpacking | 解包 | 04 表达式、运算符与赋值 |
| UTF-8 | UTF-8 编码 | 02 词法、语法与源文件 |
| value | 值 | 03 类型、对象与容器 |
| variadic keyword parameters (**kwargs) | 可变关键字参数 | 05 控制流程与函数 |
| variadic positional parameters (*args) | 可变位置参数 | 05 控制流程与函数 |
| vectorization | 向量化 | 16 性能、内存与解释器内部 |
| venv | 虚拟环境模块 | 14 依赖、包管理与构建发布 |
| version specifier | 版本约束 | 14 依赖、包管理与构建发布 |
| virtual environment | 虚拟环境 | 14 依赖、包管理与构建发布 |
| virtual machine | 虚拟机 | 01 语言与运行环境 |
| walrus operator | 海象运算符 | 04 表达式、运算符与赋值 |
| weak reference | 弱引用 | 16 性能、内存与解释器内部 |
| weakref | 弱引用模块 | 13 常用标准库与数据工具 |
| wheel | Wheel 二进制分发包 | 14 依赖、包管理与构建发布 |
| while loop | while 循环 | 05 控制流程与函数 |
| with statement | with 语句 | 08 异常处理与上下文管理 |
| yield | 产出并暂停 | 07 迭代器、生成器与函数式工具 |
| yield from | 委托产出 | 07 迭代器、生成器与函数式工具 |
| zip() | 并行打包函数 | 07 迭代器、生成器与函数式工具 |
| zoneinfo | 时区数据库接口 | 13 常用标准库与数据工具 |

<a id="appendix-c"></a>
## 附录 C：参考依据

- [Python 官方术语表](https://docs.python.org/3/glossary.html)
- [Python 语言参考：数据模型](https://docs.python.org/3/reference/datamodel.html)
- [Python 语言参考：表达式](https://docs.python.org/3/reference/expressions.html)
- [Python 语言参考：复合语句](https://docs.python.org/3/reference/compound_stmts.html)
- [Python 标准库索引](https://docs.python.org/3/library/index.html)
- [Python 类型标注文档](https://docs.python.org/3/library/typing.html)
- [Python asyncio 文档](https://docs.python.org/3/library/asyncio.html)
- [Python Packaging User Guide 术语表](https://packaging.python.org/en/latest/glossary/)
- [Python Packaging User Guide 构建流程](https://packaging.python.org/en/latest/flow/)
- [PEP 8 代码风格](https://peps.python.org/pep-0008/)

说明：文本为编辑性双语辅助材料，非官方中文规范译名。