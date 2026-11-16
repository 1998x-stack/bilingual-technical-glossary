# 线性代数 · Linear Algebra

> 中英双语专业术语手册 | Chinese-English Technical Glossary

**术语总量：289 条 · 专题：12 类**

Vectors, matrices, spaces, eigensystems and factorization

> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。

## 专题目录

- 01. 基础概念与数学记号（23 条）
- 02. 向量与几何（23 条）
- 03. 矩阵类型与基本运算（31 条）
- 04. 线性方程组与消元（24 条）
- 05. 行列式、秩与可逆性（17 条）
- 06. 向量空间、基与维数（31 条）
- 07. 线性映射与表示（24 条）
- 08. 特征值、对角化与规范形（24 条）
- 09. 内积、正交与投影（24 条）
- 10. 二次型、正定性与合同（17 条）
- 11. 矩阵分解与数值计算（28 条）
- 12. 扩展概念与应用（23 条）

---

## 01. 基础概念与数学记号

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | scalar | 标量 |  | 单个数，通常取自实数域或复数域 |
| 2 | vector | 向量 |  | 按序排列的数，或向量空间的元素 |
| 3 | matrix | 矩阵 |  | 按行列排列的元素构成的数组 |
| 4 | entry / component | 元素／分量 |  | 矩阵或向量中的单个数 |
| 5 | real number field | 实数域 |  | 实数构成的数域 |
| 6 | complex number field | 复数域 |  | 复数构成的数域 |
| 7 | field | 数域 |  | 允许加、减、乘和非零除法的集合 |
| 8 | dimension / size | 维数／大小 |  | 矩阵行数与列数；勿与空间维数混淆 |
| 9 | order | 阶数 |  | 常指方阵的行列数 n |
| 10 | row vector | 行向量 |  | 仅有一行的矩阵 |
| 11 | column vector | 列向量 |  | 仅有一列的矩阵 |
| 12 | transpose | 转置 |  | 交换矩阵的行与列 |
| 13 | complex conjugate | 共轭 |  | 将复数虚部变号 |
| 14 | conjugate transpose | 共轭转置 |  | 先共轭再转置；亦称厄米转置 |
| 15 | linear combination | 线性组合 |  | 向量的标量倍数之和 |
| 16 | coefficient | 系数 |  | 线性组合中的权重 |
| 17 | linear dependence | 线性相关 |  | 存在不全为零的系数使和为零 |
| 18 | linear independence | 线性无关 |  | 只有全零系数可得零向量 |
| 19 | span | 生成／张成 |  | 集合中向量全部线性组合构成的空间 |
| 20 | index / subscript | 指标／下标 |  | 用于标识向量、矩阵的元素位置 |
| 21 | summation notation | 求和记号 |  | 将一组项累加的记号 |
| 22 | direct sum symbol | 直和符号 |  | 表示分解成相交仅为零的子空间之和 |
| 23 | identity | 恒等关系 |  | 对规定范围内所有变量成立的关系 |

## 02. 向量与几何

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | zero vector | 零向量 |  | 所有分量为零的向量 |
| 2 | unit vector | 单位向量 |  | 长度等于一的向量 |
| 3 | standard basis vector | 标准基向量 |  | 一个分量为一，其余为零 |
| 4 | position vector | 位置向量 |  | 以原点为起点表示点位置 |
| 5 | direction vector | 方向向量 |  | 表示直线、运动等方向 |
| 6 | vector addition | 向量加法 |  | 按分量相加 |
| 7 | scalar multiplication | 标量乘法 |  | 向量各分量乘同一标量 |
| 8 | dot product | 点积 |  | 实欧氏空间中的标准内积 |
| 9 | cross product | 叉积 |  | 三维向量产生垂直向量的运算 |
| 10 | magnitude / length | 长度／模 |  | 向量的非负长度 |
| 11 | Euclidean norm | 欧几里得范数 |  | 分量平方和开根号 |
| 12 | ℓ₁ norm | 一范数 |  | 分量绝对值之和 |
| 13 | ℓ∞ norm | 无穷范数 |  | 分量绝对值的最大值 |
| 14 | distance | 距离 |  | 衡量两点或向量差异 |
| 15 | angle between vectors | 夹角 |  | 由内积关系确定的夹角 |
| 16 | orthogonal vectors | 正交向量 |  | 实内积等于零的两个向量 |
| 17 | parallel vectors | 平行向量 |  | 两向量成比例（非零情形） |
| 18 | affine combination | 仿射组合 |  | 系数之和为一的线性组合 |
| 19 | convex combination | 凸组合 |  | 非负系数的仿射组合 |
| 20 | affine subspace | 仿射子空间 |  | 线性子空间的平移 |
| 21 | hyperplane | 超平面 |  | 非零法向量定义的余维一仿射集合 |
| 22 | coordinate system | 坐标系 |  | 描述向量位置的参考框架 |
| 23 | change of coordinates | 坐标变换 |  | 同一向量在不同基下的坐标表示 |

## 03. 矩阵类型与基本运算

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | square matrix | 方阵 |  | 行数与列数相同 |
| 2 | rectangular matrix | 矩形矩阵 |  | 行数和列数可以不同 |
| 3 | zero matrix | 零矩阵 |  | 所有元素为零 |
| 4 | identity matrix | 单位矩阵 |  | 主对角线为一，其余为零 |
| 5 | diagonal matrix | 对角矩阵 |  | 非主对角线元素均为零 |
| 6 | scalar matrix | 标量矩阵 |  | 主对角线元素均为同一常数 |
| 7 | upper triangular matrix | 上三角矩阵 |  | 主对角线以下元素均为零 |
| 8 | lower triangular matrix | 下三角矩阵 |  | 主对角线以上元素均为零 |
| 9 | band matrix | 带状矩阵 |  | 非零元素集中在主对角线附近 |
| 10 | sparse matrix | 稀疏矩阵 |  | 大多数元素为零 |
| 11 | dense matrix | 稠密矩阵 |  | 多数位置含非零元素 |
| 12 | symmetric matrix | 对称矩阵 |  | 实或复矩阵等于其转置 |
| 13 | skew-symmetric matrix | 斜对称矩阵 |  | 转置等于自身负值 |
| 14 | Hermitian matrix | 厄米矩阵 |  | 共轭转置等于自身 |
| 15 | skew-Hermitian matrix | 斜厄米矩阵 |  | 共轭转置等于自身负值 |
| 16 | orthogonal matrix | 正交矩阵 |  | 实矩阵的列构成标准正交基 |
| 17 | unitary matrix | 酉矩阵 |  | 复矩阵的列构成标准正交基 |
| 18 | normal matrix | 正规矩阵 |  | 可被酉相似对角化的复方阵 |
| 19 | idempotent matrix | 幂等矩阵 |  | 平方等于自身 |
| 20 | permutation matrix | 置换矩阵 |  | 每行每列恰有一个一 |
| 21 | block matrix | 分块矩阵 |  | 将矩阵按子矩阵分组 |
| 22 | matrix addition | 矩阵加法 |  | 同型矩阵逐元素相加 |
| 23 | matrix multiplication | 矩阵乘法 |  | 通过行与列内积构成乘积 |
| 24 | matrix power | 矩阵的幂 |  | 方阵与自身连乘 |
| 25 | Hadamard product | 逐元素乘积 |  | 对应元素相乘 |
| 26 | Kronecker product | 克罗内克积 |  | 将元素替换为缩放矩阵块 |
| 27 | trace | 矩阵迹 |  | 方阵主对角线元素之和满足 AA⁻¹ = A⁻¹A = I |
| 28 | inverse matrix | 逆矩阵 |  | 满足 AA⁻¹ = A⁻¹A = I |
| 29 | invertible matrix | 可逆矩阵 |  | 存在双侧逆矩阵的方阵 |
| 30 | singular matrix | 奇异矩阵 |  | 不可逆的方阵 |
| 31 | nonsingular matrix | 非奇异矩阵 |  | 可逆方阵的另一名称 |

## 04. 线性方程组与消元

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | system of linear equations | 线性方程组 |  | 未知数只以一次线性形式出现 |
| 2 | homogeneous system | 齐次线性方程组 |  | 右端常数向量为零 |
| 3 | nonhomogeneous system | 非齐次线性方程组 |  | 右端向量非零 |
| 4 | coefficient matrix | 系数矩阵 |  | 未知数系数构成的矩阵 |
| 5 | augmented matrix | 增广矩阵 |  | 系数矩阵与常数列拼接 |
| 6 | solution vector | 解向量 |  | 满足所有方程的未知向量 |
| 7 | general solution | 通解 |  | 描述所有解的表达式 |
| 8 | particular solution | 特解 |  | 满足非齐次方程的一个具体解 |
| 9 | trivial solution | 零解 |  | 齐次系统始终具有的解 |
| 10 | consistent system | 相容／有解 |  | 至少存在一个解 |
| 11 | inconsistent system | 不相容／无解 |  | 不存在满足所有方程的解 |
| 12 | unique solution | 唯一解 |  | 解集恰含一个向量 |
| 13 | infinitely many solutions | 无穷多解 |  | 解集包含无穷多个向量 |
| 14 | free variable | 自由变量 |  | 可独立取值的非主元变量 |
| 15 | pivot variable | 主元变量 |  | 对应主元列的变量 |
| 16 | pivot | 主元 |  | 消元中用于确定行领先位置的元素 |
| 17 | elementary row operation | 初等行变换 |  | 交换、倍乘或倍加矩阵行 |
| 18 | row echelon form (REF) | 行阶梯形 | REF | 非零行主元逐行右移 |
| 19 | reduced row echelon form (RREF) | 简化行阶梯形 | RREF | 主元为一且主元列其余为零 |
| 20 | Gaussian elimination | 高斯消元法 |  | 经行消元形成阶梯形 |
| 21 | Gauss–Jordan elimination | 高斯—若尔当消元法 |  | 消至简化行阶梯形 |
| 22 | back substitution | 回代 |  | 从末行向前求未知数 |
| 23 | row equivalence | 行等价 |  | 能经有限次初等行变换互化 |
| 24 | elementary matrix | 初等矩阵 |  | 对单位矩阵做一次初等变换得到 |

## 05. 行列式、秩与可逆性

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | determinant | 行列式 |  | 方阵对应的一个标量 |
| 2 | 2×2 determinant | 二阶行列式 |  | 二维方阵行列式的基本公式 |
| 3 | minor | 余子式 |  | 删去指定行列后子式的行列式 |
| 4 | cofactor | 代数余子式 |  | 带符号的余子式 |
| 5 | cofactor expansion | 余子式展开 |  | 按一行或一列展开行列式 |
| 6 | adjugate matrix | 伴随矩阵 |  | 代数余子式矩阵的转置 |
| 7 | sign of permutation | 排列符号 |  | 标记排列的奇偶性 |
| 8 | permutation | 置换／排列 |  | 元素位置的一一重排 |
| 9 | inversion count | 逆序数 |  | 排列中逆序对的个数 |
| 10 | matrix rank | 矩阵的秩 |  | 线性无关行或列的最大数目 |
| 11 | full rank | 满秩 |  | 秩达到矩阵可达到的最大值 |
| 12 | full column rank | 列满秩 |  | 所有 n 列线性无关 |
| 13 | full row rank | 行满秩 |  | 所有 m 行线性无关 |
| 14 | rank-deficient | 秩亏 |  | 秩未达到最大可能值 |
| 15 | invertible matrix theorem | 可逆矩阵定理 |  | 多种方阵可逆条件相互等价 |
| 16 | elementary divisor | 初等因子 |  | 多项式或规范形理论中的基本因子 |
| 17 | multiplicativity of determinant | 行列式的乘法性 |  | 矩阵乘积的行列式等于乘积 |

## 06. 向量空间、基与维数

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | vector space | 向量空间 |  | 满足向量加法与标量乘法公理的集合 |
| 2 | linear space | 线性空间 |  | 向量空间的另一常用名称 |
| 3 | subspace | 子空间 |  | 对加法和标量乘法封闭的非空子集 |
| 4 | trivial subspace | 平凡子空间 |  | 仅包含零向量 |
| 5 | proper subspace | 真子空间 |  | 不等于整个向量空间的子空间 |
| 6 | spanning set | 生成集 |  | 可线性组合生成全空间的集合 |
| 7 | basis | 基 |  | 线性无关且张成全空间的向量组 |
| 8 | standard basis | 标准基 |  | 坐标空间最常用的基 |
| 9 | ordered basis | 有序基 |  | 顺序已指定的一组基向量 |
| 10 | dimension | 维数 |  | 有限维空间任一基的向量个数 |
| 11 | infinite-dimensional | 无限维 |  | 不存在有限基 |
| 12 | coordinate vector | 坐标向量 |  | 向量相对给定有序基的系数 |
| 13 | change-of-basis matrix | 基变换矩阵 |  | 将不同基下的坐标相互转换 |
| 14 | transition matrix | 过渡矩阵 |  | 基变换矩阵的常见别名 |
| 15 | sum of subspaces | 子空间之和 |  | 所有 u+w 构成的子空间 |
| 16 | intersection of subspaces | 子空间交 |  | 同时属于两个子空间的向量 |
| 17 | direct sum | 直和 |  | U∩W={0} 时的子空间和 |
| 18 | complementary subspace | 补空间 |  | 与 U 共同直和组成 V 的子空间 |
| 19 | codimension | 余维数 |  | 子空间相对于母空间少的维数 |
| 20 | quotient space | 商空间 |  | 将相差 U 中元素的向量视为等价 |
| 21 | linear span | 线性包 |  | 生成／张成的另一名称 |
| 22 | null space / kernel | 零空间 |  | 满足 Ax=0 的向量集合 |
| 23 | column space | 列空间 |  | 矩阵各列张成的空间 |
| 24 | row space | 行空间 |  | 矩阵各行张成的空间 |
| 25 | left null space | 左零空间 |  | 与所有列向量正交的空间（实数） |
| 26 | image / range | 像空间 |  | 线性映射实际能得到的输出 |
| 27 | domain | 定义域 |  | 映射允许输入的对象集合 |
| 28 | codomain | 陪域 |  | 映射声明的目标空间 |
| 29 | nullity | 零度／核维数 |  | 映射的核的维数 |
| 30 | rank–nullity theorem | 秩—零度定理 |  | 定义域维数等于像与核维数之和 |
| 31 | Grassmann's formula | 格拉斯曼公式 |  | 两个有限维子空间和的维数公式 |

## 07. 线性映射与表示

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | map / function | 映射／函数 |  | 从定义域向陪域的规则 |
| 2 | linear map | 线性映射 |  | 保持线性组合的映射 |
| 3 | linear transformation | 线性变换 |  | 通常指空间到自身的线性映射 |
| 4 | linear operator | 线性算子 |  | 线性变换的常见称呼 |
| 5 | matrix representation | 矩阵表示 |  | 给定基下表达线性映射的矩阵 |
| 6 | kernel | 核 |  | 被映到零的全部输入 |
| 7 | image | 像 |  | 映射所有可能的输出 |
| 8 | injective / one-to-one | 单射 |  | 不同输入有不同输出（线性情形） |
| 9 | surjective / onto | 满射 |  | 陪域中每个元素均可取得 |
| 10 | bijective | 双射 |  | 同时是单射与满射 |
| 11 | isomorphism | 同构 |  | 可逆线性映射 |
| 12 | automorphism | 自同构 |  | 从空间到自身的可逆线性映射 |
| 13 | linear functional | 线性泛函 |  | 取值为标量的线性映射 |
| 14 | dual space | 对偶空间 |  | 所有线性泛函构成的空间满足 fⁱ(vⱼ)=δᵢⱼ 的函数组 |
| 15 | dual basis | 对偶基 |  | 满足 fⁱ(vⱼ)=δᵢⱼ 的函数组 |
| 16 | projection operator | 投影算子 |  | 将对象映到某个子空间的幂等算子 |
| 17 | identity operator | 恒等算子 |  | 保持每个向量不变 |
| 18 | zero operator | 零算子 |  | 将全部向量映成零 |
| 19 | composition of maps | 映射的复合 |  | 先作用 T 再作用 S |
| 20 | inverse map | 逆映射 |  | 撤销可逆映射的作用 |
| 21 | basis independence | 基底不变性 |  | 抽象性质不依赖基的选择 |
| 22 | invariant subspace | 不变子空间 |  | 经线性算子作用后仍在该子空间 |
| 23 | matrix equivalence | 矩阵等价 |  | 通过左右可逆矩阵变换得到 |
| 24 | similarity transformation | 相似变换 |  | 表示同一线性算子在不同基下的矩阵 |

## 08. 特征值、对角化与规范形

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | eigenvalue | 特征值 |  | 特征向量对应的缩放因子 |
| 2 | eigenvector | 特征向量 |  | 非零且受矩阵作用后方向不变的向量 |
| 3 | characteristic equation | 特征方程 |  | 用于求矩阵特征值的方程 |
| 4 | characteristic polynomial | 特征多项式 |  | 其根是特征值的多项式 |
| 5 | eigenspace | 特征空间 |  | 给定特征值的特征向量及零向量 |
| 6 | spectrum | 谱 |  | 矩阵的全部特征值集合 |
| 7 | spectral radius | 谱半径 |  | 所有特征值模的最大值 |
| 8 | algebraic multiplicity | 代数重数 |  | 特征值作为特征多项式根的重数 |
| 9 | geometric multiplicity | 几何重数 |  | 特征空间的维数 |
| 10 | diagonalization | 对角化 |  | 用可逆矩阵将矩阵化为对角形式 |
| 11 | diagonalizable | 可对角化 |  | 存在由特征向量构成的基 |
| 12 | similar matrices | 相似矩阵 |  | 描述同一线性算子的不同基表示 |
| 13 | spectral decomposition | 谱分解 |  | 正规矩阵的酉对角分解 |
| 14 | spectral theorem | 谱定理 |  | 实对称／复厄米矩阵可正交／酉对角化 |
| 15 | Cayley–Hamilton theorem | 凯莱—哈密顿定理 |  | 矩阵满足自己的特征多项式 |
| 16 | minimal polynomial | 最小多项式 |  | 使矩阵为零的最低次数首一多项式 |
| 17 | generalized eigenvector | 广义特征向量 |  | 满足某次幂核条件的非零向量 |
| 18 | Jordan canonical form | 若尔当标准形 |  | 由若尔当块构成的相似标准形 |
| 19 | Jordan block | 若尔当块 |  | 主对角线为 λ、超对角线为一 |
| 20 | eigendecomposition | 特征分解 |  | 可对角化矩阵的特征向量分解 |
| 21 | rational canonical form | 有理标准形 |  | 由伴随块描述的相似规范形 |
| 22 | companion matrix | 伴随矩阵（多项式） |  | 对应指定首一多项式的特殊矩阵 |
| 23 | invariant factor | 不变因子 |  | 多项式模结构中的相似不变量 |
| 24 | dominant eigenvector | 主特征向量 |  | 对应模最大特征值的特征向量 |

## 09. 内积、正交与投影

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | inner product | 内积 |  | 满足正定性与（共轭）对称性的乘积 |
| 2 | inner product space | 内积空间 |  | 定义了内积的向量空间 |
| 3 | Euclidean space | 欧氏空间 |  | 通常指带标准内积的实向量空间 |
| 4 | Hermitian inner product | 厄米内积 |  | 复向量空间的标准内积 |
| 5 | norm | 范数 |  | 满足非负、齐次与三角不等式的长度函数 |
| 6 | induced norm | 诱导范数 |  | 由向量范数定义的矩阵算子范数 |
| 7 | Frobenius norm | 弗罗贝尼乌斯范数 |  | 矩阵各元素模平方之和的平方根 |
| 8 | orthonormal set | 单位正交集 |  | 向量两两正交且各自单位长度 |
| 9 | orthonormal basis | 标准正交基 |  | 既是基又是单位正交集 |
| 10 | orthogonal complement | 正交补 |  | 与 U 中所有向量正交的集合 |
| 11 | orthogonal projection | 正交投影 |  | 向子空间投影，残差与子空间正交 |
| 12 | projection matrix | 投影矩阵 |  | 表示线性投影的矩阵 |
| 13 | orthogonal projector | 正交投影矩阵 |  | 同时幂等且厄米的投影矩阵 |
| 14 | Gram–Schmidt process | 格拉姆—施密特正交化 |  | 把线性无关向量正交规范化 |
| 15 | orthogonalization | 施密特正交化 |  | 构造相互正交向量的过程 |
| 16 | orthogonal decomposition | 正交分解 |  | 将向量分解为正交部分 |
| 17 | Pythagorean theorem | 毕达哥拉斯定理 |  | 适用于正交向量的长度关系 |
| 18 | Cauchy–Schwarz inequality | 柯西—施瓦茨不等式 |  | 内积绝对值的上界 |
| 19 | triangle inequality | 三角不等式 |  | 范数的重要性质 |
| 20 | least squares | 最小二乘法 |  | 寻找残差平方和最小的解 |
| 21 | normal equations | 正规方程 |  | 实数最小二乘问题的驻点方程 |
| 22 | orthogonal change of basis | 正交基变换 |  | 通过正交矩阵改变坐标基 |
| 23 | isometry | 等距映射 |  | 保持距离或长度的映射 |
| 24 | linear isometry | 线性等距 |  | 保持内积的线性映射（适当维度） |

## 10. 二次型、正定性与合同

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | quadratic form | 二次型 |  | 关于向量分量的齐次二次多项式 |
| 2 | bilinear form | 双线性型 |  | 对两个自变量分别线性的函数 |
| 3 | symmetric bilinear form | 对称双线性型 |  | 交换输入不改变数值 |
| 4 | Hermitian form | 厄米型 |  | 复向量空间的共轭对称型厄米 A 且 xᴴAx>0（x≠0） |
| 5 | positive definite matrix | 正定矩阵 |  | 厄米 A 且 xᴴAx>0（x≠0）厄米 A 且 xᴴAx≥0 |
| 6 | positive semidefinite matrix | 半正定矩阵 |  | 厄米 A 且 xᴴAx≥0厄米 A 且 xᴴAx<0（x≠0） |
| 7 | negative definite matrix | 负定矩阵 |  | 厄米 A 且 xᴴAx<0（x≠0）厄米 A 且 xᴴAx≤0 |
| 8 | negative semidefinite matrix | 半负定矩阵 |  | 厄米 A 且 xᴴAx≤0 |
| 9 | indefinite matrix | 不定矩阵 |  | 其二次型可取正值也可取负值 |
| 10 | congruent matrices | 合同矩阵 |  | 通过可逆合同变换得到（实数） |
| 11 | Sylvester's law of inertia | 惯性定律 |  | 实对称二次型合同变换保持正负零惯性数 |
| 12 | inertia | 惯性指数 |  | 正、负、零特征值的个数 |
| 13 | principal minor | 主子式 |  | 行指标与列指标相同的子式 |
| 14 | leading principal minor | 顺序主子式 |  | 左上角 k 阶主子式 |
| 15 | Sylvester's criterion | 西尔维斯特判别法 |  | 实对称矩阵正定的判别条件 |
| 16 | Rayleigh quotient | 雷利商 |  | 厄米矩阵方向上的二次型比值 |
| 17 | signature | 符号数／惯性差 |  | 实对称型正负惯性数之差 |

## 11. 矩阵分解与数值计算

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | LU decomposition | LU 分解 |  | 拆成下三角与上三角因子 |
| 2 | PLU factorization | PLU 分解 |  | 带行置换的 LU 分解 |
| 3 | QR decomposition | QR 分解 |  | 正交／酉因子与上三角因子的乘积 |
| 4 | singular value decomposition (SVD) | 奇异值分解 | SVD | 适用于任意矩阵的重要分解AᴴA 特征值的非负平方根 |
| 5 | singular value | 奇异值 |  | AᴴA 特征值的非负平方根 |
| 6 | left singular vector | 左奇异向量 |  | 矩阵 SVD 中 U 的列 |
| 7 | right singular vector | 右奇异向量 |  | 矩阵 SVD 中 V 的列 |
| 8 | spectral norm | 谱范数 |  | 最大奇异值 |
| 9 | nuclear norm | 核范数 |  | 所有奇异值之和 |
| 10 | Moore–Penrose pseudoinverse | 伪逆 |  | 可统一表示最小二乘最小范数解 |
| 11 | generalized inverse | 广义逆 |  | 放宽逆矩阵条件的矩阵；定义需注明 |
| 12 | minimum-norm solution | 最小范数解 |  | 在可行解中范数最小的解 |
| 13 | condition number | 条件数 |  | 衡量问题对输入扰动的敏感性 |
| 14 | ill-conditioned matrix | 病态矩阵 |  | 输入微小变化可能显著影响解 |
| 15 | well-conditioned matrix | 良态矩阵 |  | 对扰动相对不敏感 |
| 16 | numerical stability | 数值稳定性 |  | 算法不显著放大舍入误差的性质 |
| 17 | round-off error | 舍入误差 |  | 有限精度表示与计算产生的误差 |
| 18 | truncation error | 截断误差 |  | 用有限步骤近似无限过程的误差 |
| 19 | floating-point number | 浮点数 |  | 计算机近似表示实数的形式 |
| 20 | Cholesky decomposition | 乔列斯基分解 |  | 厄米正定矩阵的三角分解 |
| 21 | LDLᴴ factorization | LDLᴴ 分解 |  | 厄米矩阵的三角—对角分解 |
| 22 | Householder transformation | 豪斯霍尔德变换 |  | 用反射实现正交化／消元 |
| 23 | Givens rotation | 吉文斯旋转 |  | 只作用两个坐标的正交旋转 |
| 24 | pivoting | 主元选取 |  | 消元时重排行／列以提高稳健性 |
| 25 | conjugate gradient method (CG) | 共轭梯度法 | CG | 求解对称正定系统的迭代算法 |
| 26 | generalized minimal residual (GMRES) | GMRES 方法 | GMRES | 通过 Krylov 子空间最小化残差 |
| 27 | Krylov subspace | Krylov 子空间 |  | 由矩阵幂作用产生的子空间 |
| 28 | low-rank approximation | 矩阵低秩近似 |  | 用较低秩矩阵逼近原矩阵 |

## 12. 扩展概念与应用

| # | English term | 中文译名 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | affine map | 仿射映射 |  | 线性变换加上平移 |
| 2 | linear regression | 线性回归 |  | 用线性模型拟合数据 |
| 3 | design matrix | 设计矩阵 |  | 回归分析中的特征数据矩阵 |
| 4 | covariance matrix | 协方差矩阵 |  | 记录变量两两协方差的矩阵 |
| 5 | correlation matrix | 相关矩阵 |  | 由标准化协方差构成的矩阵 |
| 6 | Gram matrix | 格拉姆矩阵 |  | 由向量两两内积组成的矩阵 |
| 7 | Hessian matrix | 海森矩阵 |  | 标量函数二阶偏导构成的矩阵 |
| 8 | Jacobian matrix | 雅可比矩阵 |  | 多元函数的一阶偏导矩阵 |
| 9 | gradient | 梯度 |  | 标量函数的一阶偏导向量 |
| 10 | principal component analysis (PCA) | 主成分分析 | PCA | 通过正交方向解释数据方差 |
| 11 | principal component | 主成分 |  | 数据方差最大的依次正交方向 |
| 12 | whitening | 白化 |  | 变换变量，使协方差成为单位矩阵 |
| 13 | linear discriminant analysis (LDA) | 线性判别分析 | LDA | 利用线性投影增强类别可分性 |
| 14 | stochastic matrix | 马尔可夫矩阵 |  | 非负且行和为一（行随机约定） |
| 15 | stationary vector | 稳态向量 |  | 在转移作用下保持不变的分布 |
| 16 | matrix exponential | 矩阵指数 |  | 由矩阵幂级数定义的函数 |
| 17 | matrix logarithm | 矩阵对数 |  | 满足指数关系的矩阵函数（需条件） |
| 18 | tensor product | 张量积 |  | 构造更高维线性空间的运算 |
| 19 | Frobenius inner product | 迹内积 |  | 矩阵空间的标准内积 |
| 20 | kernel method | 核方法 |  | 以核函数隐式计算内积的方法 |
| 21 | matrix completion | 矩阵补全 |  | 由部分观测恢复缺失矩阵元素 |
| 22 | graph Laplacian | 图拉普拉斯矩阵 |  | 描述图结构的矩阵 |
| 23 | adjacency matrix | 邻接矩阵 |  | 编码图节点间连接关系 |

---

原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/linear-algebra.pdf)

本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。
