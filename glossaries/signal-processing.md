# 信号处理专有名词中英文对照表

# Signal Processing · Chinese–English Technical Glossary

> TERM/ATLAS · 2026 Edition · 术语采用常见信号与系统、DSP 与工程实现语境；释义为独立编写的教学性简述，不代表标准组织的强制译名。

**295 条术语 · 18 个主题 · 中英文对照 / 常用缩写 / 简明释义**

## 学科目录

- 01. 信号与系统基础（17 条）
- 02. 线性系统与卷积（17 条）
- 03. 傅里叶分析（16 条）
- 04. 拉普拉斯与 Z 变换（15 条）
- 05. 采样、量化与重构（19 条）
- 06. 离散傅里叶变换与快速算法（18 条）
- 07. 加窗与谱分析（18 条）
- 08. 数字滤波器与设计（25 条）
- 09. 多速率信号处理（14 条）
- 10. 随机过程与噪声（15 条）
- 11. 统计估计与检测（15 条）
- 12. 自适应滤波与系统辨识（14 条）
- 13. 时频分析与小波（16 条）
- 14. 通信与调制（17 条）
- 15. 音频、语音与图像（15 条）
- 16. 阵列、雷达与生物医学（14 条）
- 17. 实时实现与数值工程（15 条）
- 18. 核心概念辨析与实验术语（15 条）

## 阅读说明

- 连续时间角频率通常用 rad/s，离散时间角频率通常用 rad/sample；Hz 与角频率不可直接混用。
- 常见缩写只在技术文献中广泛使用时标注；空白表示不强行编造缩写。
- 某些译名存在不同学派或行业习惯，遇到不确定情况应结合英文原文与上下文。

---

## 01. 信号与系统基础

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Signal Processing | 信号处理 |  | 对信号进行表征、分析、变换或提取信息的方法总称。 |
| 2 | Continuous-Time Signal | 连续时间信号 | CT | 以连续时间变量描述的信号，如 x(t)。 |
| 3 | Discrete-Time Signal | 离散时间信号 | DT | 仅在离散时间索引上定义的信号，如 x[n]。 |
| 4 | Analog Signal | 模拟信号 |  | 幅值通常连续变化的物理或电信号。 |
| 5 | Digital Signal | 数字信号 |  | 幅值经过量化、可用有限字长编码的离散时间信号。 |
| 6 | Deterministic Signal | 确定性信号 |  | 给定模型与参数即可确定其取值的信号。 |
| 7 | Random Signal | 随机信号 |  | 需要以随机过程描述其统计规律的信号。 |
| 8 | Periodic Signal | 周期信号 |  | 满足某个非零周期平移后数值不变的信号。 |
| 9 | Aperiodic Signal | 非周期信号 |  | 不存在满足周期条件的非零周期的信号。 |
| 10 | Energy Signal | 能量信号 |  | 总能量有限且通常具有零平均功率的信号。 |
| 11 | Power Signal | 功率信号 |  | 时间平均功率有限且非零的信号。 |
| 12 | Unit Impulse | 单位冲激 | δ | 连续时间用狄拉克冲激表示，离散时间用单位样值表示。 |
| 13 | Unit Step | 单位阶跃 | u | 在约定起点前后由零变为一的基准信号。 |
| 14 | Complex Exponential | 复指数信号 |  | 利用指数与相位统一表示振荡和增长衰减。 |
| 15 | Signal-to-Noise Ratio | 信噪比 | SNR | 指定条件下信号功率与噪声功率之比。 |
| 16 | Dynamic Range | 动态范围 |  | 系统可处理的最大与最小有效信号幅度之比。 |
| 17 | Root Mean Square | 均方根值 | RMS | 信号平方的均值再开平方，用于描述有效幅值。 |

## 02. 线性系统与卷积

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | System | 系统 |  | 把输入信号映射为输出信号的规则或设备。 |
| 2 | Linearity | 线性性 |  | 系统满足可加性与齐次性两个条件。 |
| 3 | Time Invariance | 时不变性 |  | 输入整体时移只引起输出相同的时移。 |
| 4 | Linear Time-Invariant System | 线性时不变系统 | LTI | 同时满足线性性与时不变性的系统。 |
| 5 | Causality | 因果性 |  | 某时刻的输出不依赖该时刻之后的输入。 |
| 6 | Bounded-Input Bounded-Output Stability | 有界输入有界输出稳定性 | BIBO | 所有有界输入都产生有界输出。 |
| 7 | Impulse Response | 冲激响应 |  | LTI 系统对单位冲激输入的输出。 |
| 8 | Step Response | 阶跃响应 |  | 系统对单位阶跃输入的输出。 |
| 9 | Convolution | 卷积 |  | 由输入与冲激响应计算 LTI 系统输出的运算。 |
| 10 | Linear Convolution | 线性卷积 |  | 对普通序列定义、输出长度一般增加的卷积。 |
| 11 | Circular Convolution | 循环卷积 |  | 在周期延拓或模 N 索引下定义的卷积。 |
| 12 | Difference Equation | 差分方程 |  | 用离散时间输入输出及其移位描述系统。 |
| 13 | Differential Equation | 微分方程 |  | 用连续时间信号及其导数描述系统。 |
| 14 | Frequency Response | 频率响应 |  | 系统对各频率复指数分量的增益与相位作用。 |
| 15 | Transfer Function | 传递函数 |  | 零初始条件下输出与输入变换之比。 |
| 16 | Group Delay | 群时延 |  | 相位响应对角频率的负导数，描述窄带包络延迟。 |
| 17 | Phase Delay | 相位时延 |  | 相位响应相对于角频率的负比值，需注意相位展开。 |

## 03. 傅里叶分析

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Fourier Series | 傅里叶级数 | FS | 把周期信号分解为离散谐波的级数表示。 |
| 2 | Continuous-Time Fourier Series | 连续时间傅里叶级数 | CTFS | 连续时间周期信号的谐波展开。 |
| 3 | Discrete-Time Fourier Series | 离散时间傅里叶级数 | DTFS | 离散时间周期序列的有限谐波展开。 |
| 4 | Fourier Transform | 傅里叶变换 | FT | 将信号映射到频率域的积分或广义变换。 |
| 5 | Continuous-Time Fourier Transform | 连续时间傅里叶变换 | CTFT | 连续时间信号的连续频谱表示。 |
| 6 | Discrete-Time Fourier Transform | 离散时间傅里叶变换 | DTFT | 离散时间序列的周期性连续频率谱。 |
| 7 | Inverse Fourier Transform | 傅里叶逆变换 | IFT | 由频谱重构对应的时域信号。 |
| 8 | Fourier Transform Pair | 傅里叶变换对 |  | 相互对应的时域表示与频域表示。 |
| 9 | Magnitude Spectrum | 幅度谱 |  | 傅里叶变换复值的模。 |
| 10 | Phase Spectrum | 相位谱 |  | 傅里叶变换复值的相位角。 |
| 11 | Power Spectrum | 功率谱 |  | 频率分量功率分布的描述，需明确归一化定义。 |
| 12 | Spectral Symmetry | 频谱对称性 |  | 实信号的傅里叶谱满足共轭对称关系。 |
| 13 | Parseval's Theorem | 帕塞瓦尔定理 |  | 信号能量可等价地在时域和频域计算。 |
| 14 | Convolution Theorem | 卷积定理 |  | 时域卷积对应频域乘法，反之亦然。 |
| 15 | Duality Property | 对偶性质 |  | 傅里叶变换在一定约定下具有时频互换的对偶关系。 |
| 16 | Time-Frequency Uncertainty Principle | 时频不确定性原理 |  | 信号不可能同时在时间与频率上任意集中。 |

## 04. 拉普拉斯与 Z 变换

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Laplace Transform | 拉普拉斯变换 |  | 通过复频率变量表示连续时间信号及系统。 |
| 2 | Bilateral Laplace Transform | 双边拉普拉斯变换 |  | 积分时间范围覆盖整个实数轴的拉普拉斯变换。 |
| 3 | Unilateral Laplace Transform | 单边拉普拉斯变换 |  | 常用于带初始条件的因果系统分析。 |
| 4 | Region of Convergence | 收敛域 | ROC | 使拉普拉斯或 Z 变换收敛的复变量区域。 |
| 5 | Complex Frequency | 复频率 |  | 包含指数增长衰减与振荡成分的复变量。 |
| 6 | Pole | 极点 |  | 传递函数发生奇异性的复平面位置。 |
| 7 | Zero | 零点 |  | 传递函数分子为零且未被约去的位置。 |
| 8 | Pole-Zero Plot | 零极点图 |  | 在复平面展示系统零点与极点的图。 |
| 9 | Z-Transform | Z 变换 |  | 以复变量 z 表示离散时间序列的变换。 |
| 10 | Bilateral Z-Transform | 双边 Z 变换 |  | 对全体整数时间索引求和的 Z 变换。 |
| 11 | Unilateral Z-Transform | 单边 Z 变换 |  | 常用于处理单边序列及初始条件。 |
| 12 | Unit Circle | 单位圆 |  | Z 平面上模长为一的复数轨迹。 |
| 13 | System Function | 系统函数 |  | 离散 LTI 系统冲激响应的 Z 变换。 |
| 14 | Minimum-Phase System | 最小相位系统 |  | 稳定因果系统的逆系统也稳定因果的常见类别。 |
| 15 | All-Pass System | 全通系统 |  | 幅频响应为常数、仅改变相位的系统。 |

## 05. 采样、量化与重构

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Sampling | 采样 |  | 从连续时间信号中按时刻取得离散样本。 |
| 2 | Sampling Rate | 采样率 | fs | 单位时间采集的样本数量，单位通常为 Hz。 |
| 3 | Sampling Period | 采样周期 | Ts | 相邻均匀采样时刻的时间间隔。 |
| 4 | Nyquist-Shannon Sampling Theorem | 奈奎斯特－香农采样定理 |  | 满足带限与足够采样率等条件时可无失真重构信号。 |
| 5 | Nyquist Frequency | 奈奎斯特频率 |  | 均匀采样率的一半，即 fs/2。 |
| 6 | Nyquist Rate | 奈奎斯特速率 |  | 对最高频率 B 的基带带限信号，临界采样率为 2B。 |
| 7 | Aliasing | 混叠 |  | 采样导致不同模拟频率分量对应相同离散频率。 |
| 8 | Anti-Aliasing Filter | 抗混叠滤波器 | AAF | 采样前抑制会折叠到目标频带的高频分量。 |
| 9 | Bandlimited Signal | 带限信号 |  | 频谱在有限频率区间外为零的信号。 |
| 10 | Ideal Reconstruction | 理想重构 |  | 满足定理条件时通过理想低通或 sinc 插值恢复原信号。 |
| 11 | Sinc Interpolation | 辛克插值 |  | 采用 sinc 核从均匀采样值恢复带限信号。 |
| 12 | Zero-Order Hold | 零阶保持 | ZOH | 在相邻更新时刻之间保持前一输出值。 |
| 13 | Quantization | 量化 |  | 把连续或高精度幅值映射到有限离散级别。 |
| 14 | Quantization Step Size | 量化步长 |  | 相邻量化等级对应的输入幅值间隔。 |
| 15 | Quantization Error | 量化误差 |  | 量化前后幅值之差。 |
| 16 | Bit Depth | 位深度 |  | 表示每个样本所用的量化位数。 |
| 17 | Dithering | 抖动处理 |  | 在量化前加入受控噪声以减轻相关失真或伪迹。 |
| 18 | Analog-to-Digital Converter | 模数转换器 | ADC | 把连续模拟输入转换成数字编码的电路。 |
| 19 | Digital-to-Analog Converter | 数模转换器 | DAC | 把数字编码转换成模拟输出的电路。 |

## 06. 离散傅里叶变换与快速算法

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Discrete Fourier Transform | 离散傅里叶变换 | DFT | 把 N 个时域样本变换为 N 个离散频率系数。 |
| 2 | Inverse Discrete Fourier Transform | 离散傅里叶逆变换 | IDFT | 从 DFT 频谱系数恢复长度为 N 的序列。 |
| 3 | Fast Fourier Transform | 快速傅里叶变换 | FFT | 高效计算 DFT 的算法家族，并非另一种变换。 |
| 4 | Inverse Fast Fourier Transform | 逆快速傅里叶变换 | IFFT | 高效计算 IDFT 的算法实现。 |
| 5 | Radix-2 FFT | 基二快速傅里叶变换 |  | 把变换规模按 2 的因子递归分解的 FFT 算法。 |
| 6 | Decimation in Time | 按时间抽取 | DIT | 通过拆分时域样本实现 FFT 的分解方案。 |
| 7 | Decimation in Frequency | 按频率抽取 | DIF | 通过拆分频域输出实现 FFT 的分解方案。 |
| 8 | Butterfly Operation | 蝶形运算 |  | FFT 中对若干样本进行加减与旋转因子组合的基本步骤。 |
| 9 | Twiddle Factor | 旋转因子 |  | FFT 分解中使用的复指数乘数。 |
| 10 | Bit-Reversal Permutation | 位逆序置换 |  | 某些基二 FFT 实现中采用的索引重排。 |
| 11 | FFT Bin | FFT 频点 |  | DFT 离散频率采样位置，对应的频率与采样率有关。 |
| 12 | Frequency Resolution | 频率分辨率 |  | 区分相近频率分量的能力，需区分频点间距与真实可分辨能力。 |
| 13 | Bin Spacing | 频点间距 |  | 均匀 DFT 的相邻频点间距 fs/N。 |
| 14 | Zero Padding | 补零 |  | 在变换前添加零以加密频率采样，不能提升真实谱分辨能力。 |
| 15 | Spectral Leakage | 频谱泄漏 |  | 有限时窗截断使能量扩散到邻近频率。 |
| 16 | Picket-Fence Effect | 栅栏效应 |  | 有限离散频点可能漏过连续频谱峰值。 |
| 17 | Overlap-Add Method | 重叠相加法 | OLA | 通过分块卷积并相加重叠输出实现长序列处理。 |
| 18 | Overlap-Save Method | 重叠保留法 | OLS | 使用重叠分块并丢弃失真边界样本的快速卷积方法。 |

## 07. 加窗与谱分析

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Window Function | 窗函数 |  | 对有限数据段加权以调节频谱泄漏与分辨率。 |
| 2 | Rectangular Window | 矩形窗 |  | 观测区间内权重恒为一的窗。 |
| 3 | Hann Window | 汉宁窗／Hann 窗 |  | 端点趋近于零的余弦型窗，标准英文为 Hann。 |
| 4 | Hamming Window | 海明窗 |  | 具有特定余弦系数的窗，用于抑制旁瓣。 |
| 5 | Blackman Window | 布莱克曼窗 |  | 包含多个余弦项、旁瓣抑制较强的窗。 |
| 6 | Kaiser Window | 凯泽窗 |  | 通过参数调节主瓣宽度与旁瓣的窗。 |
| 7 | Gaussian Window | 高斯窗 |  | 以高斯函数构造平滑加权的窗。 |
| 8 | Main Lobe | 主瓣 |  | 窗函数频率响应中心附近的主要能量区域。 |
| 9 | Side Lobe | 旁瓣 |  | 主瓣之外的频率响应局部峰值。 |
| 10 | Side-Lobe Attenuation | 旁瓣衰减 |  | 用来衡量旁瓣相对主瓣高度的指标。 |
| 11 | Equivalent Noise Bandwidth | 等效噪声带宽 | ENBW | 表示窗对宽带噪声功率积分效应的等效带宽。 |
| 12 | Coherent Gain | 相干增益 |  | 窗对恰好落在频点上的正弦分量幅度的缩放系数。 |
| 13 | Periodogram | 周期图 |  | 用有限长度数据傅里叶变换的平方估计功率谱。 |
| 14 | Welch's Method | 韦尔奇法 |  | 分段、加窗并平均周期图的功率谱估计方法。 |
| 15 | Bartlett's Method | 巴特利特法 |  | 对不重叠分段的周期图取平均的谱估计方法。 |
| 16 | Power Spectral Density | 功率谱密度 | PSD | 单位频率上的平均功率分布，单位依输入而定。 |
| 17 | Cross Spectral Density | 互功率谱密度 | CSD | 描述两个过程在频率域相关关系的谱量。 |
| 18 | Magnitude-Squared Coherence | 幅值平方相干函数 | MSC | 归一化互谱强度，值通常介于零与一之间。 |

## 08. 数字滤波器与设计

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Digital Filter | 数字滤波器 |  | 在离散时间域改变信号频率成分的算法系统。 |
| 2 | Finite Impulse Response Filter | 有限冲激响应滤波器 | FIR | 冲激响应长度有限的滤波器类别。 |
| 3 | Infinite Impulse Response Filter | 无限冲激响应滤波器 | IIR | 冲激响应通常无限延续的递归滤波器类别。 |
| 4 | Low-Pass Filter | 低通滤波器 | LPF | 主要通过低频并抑制高频的滤波器。 |
| 5 | High-Pass Filter | 高通滤波器 | HPF | 主要通过高频并抑制低频的滤波器。 |
| 6 | Band-Pass Filter | 带通滤波器 | BPF | 主要通过指定频带的滤波器。 |
| 7 | Band-Stop Filter | 带阻滤波器 | BSF | 主要抑制指定频带的滤波器。 |
| 8 | Notch Filter | 陷波滤波器 |  | 对窄频带施加显著衰减的滤波器。 |
| 9 | Cutoff Frequency | 截止频率 |  | 用于界定通带或阻带边界的特征频率，判定约定依滤波器而异。 |
| 10 | Passband | 通带 |  | 滤波器要求保留目标信号的频带。 |
| 11 | Stopband | 阻带 |  | 滤波器要求强烈抑制信号的频带。 |
| 12 | Transition Band | 过渡带 |  | 通带与阻带之间的频率区间。 |
| 13 | Passband Ripple | 通带波纹 |  | 通带增益相对目标响应的起伏。 |
| 14 | Stopband Attenuation | 阻带衰减 |  | 阻带信号相对于参考增益被削弱的程度。 |
| 15 | Filter Order | 滤波器阶数 |  | 决定系统复杂度与响应特性的阶数指标。 |
| 16 | Linear-Phase Filter | 线性相位滤波器 |  | 在目标频段具有仿射相位响应的滤波器。 |
| 17 | Butterworth Filter | 巴特沃斯滤波器 |  | 模拟低通原型通带幅度单调且最大平坦的滤波器家族。 |
| 18 | Chebyshev Type I Filter | 切比雪夫 I 型滤波器 |  | 具有通带等波纹响应的经典滤波器家族。 |
| 19 | Chebyshev Type II Filter | 切比雪夫 II 型滤波器 |  | 具有阻带等波纹响应的经典滤波器家族。 |
| 20 | Elliptic Filter | 椭圆滤波器 |  | 通带与阻带均可等波纹、过渡带较陡的滤波器家族。 |
| 21 | Biquad Filter | 双二阶滤波器 |  | 由二阶有理传递函数构成的滤波单元。 |
| 22 | Second-Order Section | 二阶节 | SOS | 将高阶滤波器拆分为多个二阶小节的实现形式。 |
| 23 | Bilinear Transform | 双线性变换 |  | 通过复平面映射将模拟滤波器转换为数字滤波器。 |
| 24 | Frequency Prewarping | 频率预畸变 |  | 补偿双线性变换非线性频率映射的设计步骤。 |
| 25 | Forward-Backward Filtering | 前向－后向滤波 |  | 先正向再反向滤波以抵消相位延迟，属于非因果离线处理。 |

## 09. 多速率信号处理

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Multirate Signal Processing | 多速率信号处理 |  | 在不同采样率之间实现信号变换与处理。 |
| 2 | Downsampling | 下采样 |  | 通过保留部分样本降低采样率的操作。 |
| 3 | Upsampling | 上采样 |  | 通过插入零样本等操作提高离散时间采样率。 |
| 4 | Decimation | 抽取 |  | 通常指先抗混叠低通再降采样的组合处理。 |
| 5 | Interpolation | 插值 |  | 利用相邻样本估计中间取值，数字插值常含上采样与滤波。 |
| 6 | Resampling | 重采样 |  | 把离散信号转换到新的采样时间网格。 |
| 7 | Rational Resampling | 有理比重采样 |  | 按整数比 L/M 改变采样率的处理。 |
| 8 | Polyphase Decomposition | 多相分解 |  | 将滤波器系数按相位子序列分组以高效多速率实现。 |
| 9 | Polyphase Filter Bank | 多相滤波器组 |  | 利用多相结构实现高效频带拆分或合成的滤波器组。 |
| 10 | Cascaded Integrator-Comb Filter | 级联积分梳状滤波器 | CIC | 无需通用乘法器的高效抽取或插值滤波器结构。 |
| 11 | Half-Band Filter | 半带滤波器 |  | 过渡频率围绕四分之一采样率、具有特殊系数结构的滤波器。 |
| 12 | Noble Identity | 贵族恒等式 |  | 在多速率系统中交换滤波与采样率变换位置的等价关系。 |
| 13 | Channelizer | 信道化器 |  | 把宽带输入分解为多个较窄频带通道的系统。 |
| 14 | Perfect Reconstruction Filter Bank | 完全重构滤波器组 | PRFB | 分析与合成后能恢复输入，至多差一个固定增益或延迟。 |

## 10. 随机过程与噪声

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Random Process | 随机过程 |  | 随时间演化的一族随机变量。 |
| 2 | Stationary Process | 平稳随机过程 |  | 其统计性质在时间平移下保持不变的随机过程。 |
| 3 | Strict-Sense Stationarity | 严平稳 | SSS | 所有有限维联合分布均对时间平移不变。 |
| 4 | Wide-Sense Stationarity | 宽平稳 | WSS | 均值为常数且自相关只依赖时差的随机过程。 |
| 5 | Ergodicity | 遍历性 |  | 在适当条件下单条样本路径的时间统计可反映总体统计。 |
| 6 | Autocorrelation Function | 自相关函数 | ACF | 度量同一信号在不同时间点之间的相关程度。 |
| 7 | Cross-Correlation Function | 互相关函数 | CCF | 度量两个信号在不同时间位移下的相关程度。 |
| 8 | Autocovariance Function | 自协方差函数 |  | 反映信号中心化后不同时间点之间的协方差。 |
| 9 | White Noise | 白噪声 |  | 具有平坦功率谱密度的理想随机噪声模型。 |
| 10 | Gaussian Noise | 高斯噪声 |  | 其幅度或有限维联合分布服从高斯模型的噪声。 |
| 11 | Colored Noise | 有色噪声 |  | 功率谱密度随频率变化的噪声。 |
| 12 | Additive White Gaussian Noise | 加性高斯白噪声 | AWGN | 以相加方式叠加、具有高斯统计与白谱特性的噪声模型。 |
| 13 | Noise Floor | 噪声底 |  | 在给定测量配置下可观察到的背景噪声水平。 |
| 14 | Signal-to-Interference-plus-Noise Ratio | 信干噪比 | SINR | 目标信号功率与干扰及噪声总功率之比。 |
| 15 | Wiener-Khinchin Theorem | 维纳－辛钦定理 |  | 在适当条件下平稳过程的自相关与功率谱密度互为傅里叶变换。 |

## 11. 统计估计与检测

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Estimator | 估计量 |  | 由观测数据推断未知参数或信号的计算规则。 |
| 2 | Bias | 偏差 |  | 估计量期望与真实参数之间的差。 |
| 3 | Variance | 方差 |  | 估计量围绕其期望的离散程度。 |
| 4 | Mean Squared Error | 均方误差 | MSE | 估计误差平方的期望，包含偏差与方差影响。 |
| 5 | Maximum Likelihood Estimation | 最大似然估计 | MLE | 选择使观测数据似然最大的参数。 |
| 6 | Maximum A Posteriori Estimation | 最大后验估计 | MAP | 利用先验分布与似然寻找后验概率最大的参数。 |
| 7 | Minimum Mean Square Error Estimation | 最小均方误差估计 | MMSE | 以最小化平均平方误差为目标的估计。 |
| 8 | Matched Filter | 匹配滤波器 |  | 在指定加性白噪声模型中最大化采样输出信噪比的线性滤波器。 |
| 9 | Hypothesis Testing | 假设检验 |  | 根据观测证据在不同统计假设之间作决策。 |
| 10 | Likelihood Ratio Test | 似然比检验 | LRT | 以两个假设的似然比构造判决规则。 |
| 11 | Neyman-Pearson Criterion | 奈曼－皮尔逊准则 |  | 在限制虚警率下最大化检测概率的判决准则。 |
| 12 | False Alarm Rate | 虚警率 |  | 无目标时错误报告存在目标的概率或速率。 |
| 13 | Detection Probability | 检测概率 | Pd | 目标存在时正确报告存在目标的概率。 |
| 14 | Receiver Operating Characteristic | 受试者工作特征曲线 | ROC | 展示检测率与虚警率随阈值变化关系的曲线。 |
| 15 | Cramér-Rao Lower Bound | 克拉美－罗下界 | CRLB | 在正则条件下无偏估计量方差的理论下界。 |

## 12. 自适应滤波与系统辨识

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Adaptive Filter | 自适应滤波器 |  | 根据输入输出数据自动更新参数的滤波器。 |
| 2 | System Identification | 系统辨识 |  | 利用观测输入输出估计系统模型与参数。 |
| 3 | Least Mean Squares Algorithm | 最小均方算法 | LMS | 基于瞬时误差梯度更新滤波权重的自适应算法。 |
| 4 | Normalized Least Mean Squares | 归一化最小均方算法 | NLMS | 按输入能量归一化更新步长的 LMS 变体。 |
| 5 | Recursive Least Squares | 递归最小二乘算法 | RLS | 递归更新加权最小二乘解的自适应算法。 |
| 6 | Step Size | 步长 |  | 控制自适应参数单步更新幅度的系数。 |
| 7 | Convergence Rate | 收敛速度 |  | 自适应估计接近稳定解的速度。 |
| 8 | Misadjustment | 失调量 |  | 自适应算法稳态误差相对理论最优误差的超额比例。 |
| 9 | Adaptive Noise Cancellation | 自适应噪声抵消 | ANC | 利用参考噪声自适应估计并去除干扰。 |
| 10 | Acoustic Echo Cancellation | 声学回声消除 | AEC | 估计并抑制声学回声路径引起的回传信号。 |
| 11 | Wiener Filter | 维纳滤波器 |  | 在二阶统计已知时最小化均方误差的线性滤波器。 |
| 12 | Kalman Filter | 卡尔曼滤波器 | KF | 在线性高斯状态空间模型中递归估计隐状态。 |
| 13 | Extended Kalman Filter | 扩展卡尔曼滤波器 | EKF | 对非线性状态模型局部线性化的递归估计方法。 |
| 14 | State-Space Model | 状态空间模型 |  | 以隐状态递推与观测方程描述动态系统。 |

## 13. 时频分析与小波

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Short-Time Fourier Transform | 短时傅里叶变换 | STFT | 对局部时间窗内信号计算傅里叶变换。 |
| 2 | Inverse Short-Time Fourier Transform | 短时傅里叶逆变换 | ISTFT | 通过窗函数与重叠重构由短时频谱恢复信号。 |
| 3 | Spectrogram | 语谱图／时频谱图 |  | 以时间与频率坐标展示局部频谱强度的图。 |
| 4 | Time-Frequency Representation | 时频表示 | TFR | 联合描述信号的时间位置与频率内容。 |
| 5 | Gabor Transform | 伽博变换 |  | 通常使用高斯窗构造的短时傅里叶型表示。 |
| 6 | Constant-Q Transform | 恒 Q 变换 | CQT | 使分析频带中心频率与带宽比值近似恒定的变换。 |
| 7 | Wavelet Transform | 小波变换 | WT | 用缩放和平移的小波分析不同时间尺度的信号。 |
| 8 | Continuous Wavelet Transform | 连续小波变换 | CWT | 按连续尺度和平移参数计算小波系数。 |
| 9 | Discrete Wavelet Transform | 离散小波变换 | DWT | 用离散尺度和位置构造可高效计算的小波分解。 |
| 10 | Wavelet Packet Transform | 小波包变换 | WPT | 对低频与高频子带进一步分解的小波分析。 |
| 11 | Multiresolution Analysis | 多分辨率分析 | MRA | 在嵌套尺度空间中描述信号近似与细节的框架。 |
| 12 | Mother Wavelet | 母小波 |  | 通过缩放和平移生成小波函数族的基函数。 |
| 13 | Scalogram | 尺度图 |  | 展示小波系数能量随时间与尺度变化的图。 |
| 14 | Hilbert Transform | 希尔伯特变换 |  | 以特定卷积核形成相位正交分量的线性变换。 |
| 15 | Analytic Signal | 解析信号 |  | 由实信号及其希尔伯特变换构成的复信号。 |
| 16 | Instantaneous Frequency | 瞬时频率 |  | 解析信号相位对时间的导数经归一化得到的局部频率。 |

## 14. 通信与调制

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Modulation | 调制 |  | 利用基带信息改变载波参数的过程。 |
| 2 | Demodulation | 解调 |  | 从调制信号中恢复传输信息的过程。 |
| 3 | Carrier Frequency | 载波频率 |  | 用于承载基带信息的周期信号频率。 |
| 4 | Baseband Signal | 基带信号 |  | 频谱集中在零频附近的待传输信息信号。 |
| 5 | Passband Signal | 通带信号 |  | 频谱围绕非零载频分布的信号。 |
| 6 | Amplitude Modulation | 幅度调制 | AM | 通过改变载波幅值承载信息的调制方式。 |
| 7 | Frequency Modulation | 频率调制 | FM | 通过改变载波瞬时频率承载信息的调制方式。 |
| 8 | Phase Modulation | 相位调制 | PM | 通过改变载波相位承载信息的调制方式。 |
| 9 | Quadrature Amplitude Modulation | 正交幅度调制 | QAM | 通过两个正交载波的幅度组合传递符号。 |
| 10 | Phase-Shift Keying | 相移键控 | PSK | 将有限离散相位映射为数字通信符号。 |
| 11 | Frequency-Shift Keying | 频移键控 | FSK | 将离散载频映射为数字通信符号。 |
| 12 | Orthogonal Frequency-Division Multiplexing | 正交频分复用 | OFDM | 通过相互正交的多个子载波并行传输数据。 |
| 13 | Symbol Rate | 符号率 |  | 每秒传输的调制符号数，单位为波特。 |
| 14 | Bit Error Rate | 误码率 | BER | 接收错误比特数与总接收比特数之比。 |
| 15 | Inter-Symbol Interference | 码间干扰 | ISI | 相邻符号波形在判决时刻相互影响的现象。 |
| 16 | Pulse Shaping | 脉冲成形 |  | 通过滤波控制符号波形频谱与码间干扰。 |
| 17 | Root-Raised-Cosine Filter | 根升余弦滤波器 | RRC | 发送与接收端常成对使用的脉冲成形滤波器。 |

## 15. 音频、语音与图像

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Audio Signal Processing | 音频信号处理 |  | 对声音波形进行分析、增强、编码或合成的方法。 |
| 2 | Speech Enhancement | 语音增强 |  | 减弱噪声或失真以改善语音可懂度和质量。 |
| 3 | Voice Activity Detection | 语音活动检测 | VAD | 判断音频片段中是否包含语音活动。 |
| 4 | Pitch | 音高 |  | 与听觉基频感知密切相关的声音特征。 |
| 5 | Fundamental Frequency | 基频 | F0 | 周期信号的最低重复频率，常用于描述声带振动。 |
| 6 | Formant | 共振峰 |  | 声道共振在语音谱中形成的主要频率区域。 |
| 7 | Mel-Frequency Cepstral Coefficient | 梅尔频率倒谱系数 | MFCC | 基于梅尔频标滤波与倒谱变换提取的语音特征。 |
| 8 | Cepstrum | 倒谱 |  | 对谱对数进行逆变换得到的表征。 |
| 9 | Linear Predictive Coding | 线性预测编码 | LPC | 用过去采样预测当前信号并构建语音模型的方法。 |
| 10 | Pre-Emphasis | 预加重 |  | 在处理前相对增强某些高频分量的滤波步骤。 |
| 11 | Dynamic Range Compression | 动态范围压缩 | DRC | 通过随电平变化的增益缩小强弱声差异。 |
| 12 | Image Filtering | 图像滤波 |  | 对二维离散信号执行空间或频率域变换。 |
| 13 | Two-Dimensional Fourier Transform | 二维傅里叶变换 | 2D FT | 把图像等二维信号映射到二维空间频率域。 |
| 14 | Convolution Kernel | 卷积核 |  | 在局部邻域对样本加权求和的系数矩阵或序列。 |
| 15 | Edge Detection | 边缘检测 |  | 定位图像中强度快速变化的空间结构。 |

## 16. 阵列、雷达与生物医学

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Sensor Array | 传感器阵列 |  | 由多个空间分布的传感器联合采集信号的结构。 |
| 2 | Beamforming | 波束形成 |  | 联合加权多通道信号以增强特定方向的响应。 |
| 3 | Delay-and-Sum Beamforming | 延时求和波束形成 |  | 按传播时差对齐阵列通道后求和的波束形成方法。 |
| 4 | Direction of Arrival | 波达方向 | DOA | 入射波相对于阵列坐标系的方向参数。 |
| 5 | Steering Vector | 导向矢量 |  | 描述特定入射方向在阵列各通道相位或幅值响应的向量。 |
| 6 | Multiple Signal Classification | 多重信号分类算法 | MUSIC | 利用信号与噪声子空间正交性估计来波方向的方法。 |
| 7 | Synthetic Aperture Radar | 合成孔径雷达 | SAR | 利用平台运动合成大孔径实现高分辨率雷达成像。 |
| 8 | Range-Doppler Processing | 距离－多普勒处理 |  | 联合估计回波传播距离与径向速度的处理方法。 |
| 9 | Pulse Compression | 脉冲压缩 |  | 通过编码波形与匹配滤波兼顾发射能量和距离分辨率。 |
| 10 | Electrocardiogram | 心电图信号 | ECG | 记录心脏电活动随时间变化的生理信号。 |
| 11 | Electroencephalogram | 脑电图信号 | EEG | 通过头皮或其他电极记录脑部电活动的信号。 |
| 12 | Electromyogram | 肌电图信号 | EMG | 记录肌肉电活动的信号。 |
| 13 | Baseline Wander | 基线漂移 |  | 低频趋势造成信号基准线缓慢偏移的现象。 |
| 14 | Artifact Removal | 伪迹去除 |  | 抑制运动、电极接触等非目标来源的测量干扰。 |

## 17. 实时实现与数值工程

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Real-Time Signal Processing | 实时信号处理 |  | 必须在规定处理时限内完成的信号计算。 |
| 2 | Latency | 延迟 |  | 输入发生到输出可用之间的时间差。 |
| 3 | Throughput | 吞吐量 |  | 单位时间可处理的数据量或样本数。 |
| 4 | Block Processing | 分块处理 |  | 把信号分成数据块后执行计算的处理模式。 |
| 5 | Streaming Processing | 流式处理 |  | 在数据连续到达时增量执行的处理模式。 |
| 6 | Fixed-Point Arithmetic | 定点运算 |  | 以固定缩放因子与有限整数表示执行数值计算。 |
| 7 | Floating-Point Arithmetic | 浮点运算 |  | 以尾数和指数形式表达数值并执行运算。 |
| 8 | Numerical Precision | 数值精度 |  | 计算中有效数字与舍入误差的表征。 |
| 9 | Coefficient Quantization | 系数量化 |  | 把滤波器等算法系数映射到有限字长表示。 |
| 10 | Overflow | 溢出 |  | 数值超出目标表示范围的现象。 |
| 11 | Saturation Arithmetic | 饱和算术 |  | 溢出时将结果钳制到表示范围边界。 |
| 12 | Circular Buffer | 环形缓冲区 |  | 在固定容量内循环复用存储位置的数据结构。 |
| 13 | Direct Memory Access | 直接内存访问 | DMA | 硬件无需 CPU 逐字节搬运即可传输数据的机制。 |
| 14 | Single Instruction Multiple Data | 单指令多数据 | SIMD | 用同一条指令并行处理多个数据元素的体系结构。 |
| 15 | Finite Word Length Effect | 有限字长效应 |  | 量化和舍入对数值滤波器行为与稳定性造成的影响。 |

## 18. 核心概念辨析与实验术语

| # | English term | 中文术语 | Abbr. | 简明释义 |
|---:|---|---|---|---|
| 1 | Normalization | 归一化 |  | 按指定尺度调整信号或频谱，必须说明采用的规范。 |
| 2 | One-Sided Spectrum | 单边频谱 |  | 仅呈现非负频率的频谱，通常需为能量一致性调整系数。 |
| 3 | Two-Sided Spectrum | 双边频谱 |  | 同时呈现正频率与负频率的频谱。 |
| 4 | Angular Frequency | 角频率 | ω | 以弧度每秒或弧度每样本表示的频率变量。 |
| 5 | Hertz | 赫兹 | Hz | 每秒一个周期的频率单位。 |
| 6 | Radians per Sample | 弧度每采样点 | rad/sample | 离散时间角频率的常用单位。 |
| 7 | Normalized Frequency | 归一化频率 |  | 把频率按采样率或奈奎斯特频率缩放，须说明约定。 |
| 8 | Spectral Centroid | 频谱质心 |  | 按谱幅值或功率权重计算的频率中心指标。 |
| 9 | Peak Frequency | 峰值频率 |  | 在指定频带内谱值最大的位置。 |
| 10 | Harmonic | 谐波 |  | 频率为基频整数倍的周期成分。 |
| 11 | Total Harmonic Distortion | 总谐波失真 | THD | 非基波谐波均方根相对基波均方根的比例。 |
| 12 | Signal-to-Noise-and-Distortion Ratio | 信噪失真比 | SINAD | 信号有效功率相对噪声与失真功率总和的比值。 |
| 13 | Effective Number of Bits | 有效位数 | ENOB | 根据实际转换器噪声与失真性能换算的等效分辨率。 |
| 14 | Power Cepstrum | 功率倒谱 |  | 由对数功率谱构成的倒谱表示，具体归一化需说明。 |
| 15 | Phase Unwrapping | 相位展开 |  | 通过消除相位的 2π 跳变形成连续相位轨迹。 |

---

## 重点易混术语辨析

**FFT 与 DFT**：DFT 是有限序列的数学变换；FFT 是快速计算 DFT 的算法族。

**DTFT 与 DFT**：DTFT 在频率上连续且以 2π 为周期；DFT 对有限序列只给出 N 个频点。

**采样率与奈奎斯特频率**：采样率 fs 是每秒样本数；奈奎斯特频率 fs/2；基带带限信号的奈奎斯特速率为最高频率的两倍。

**混叠与频谱泄漏**：混叠由采样引起频谱重叠；泄漏由有限观测窗使频谱能量扩散。

**补零与分辨率**：补零细化频率采样网格，通常不提高区分相近真实频率分量的能力。

**卷积与互相关**：卷积涉及时间反转后相乘积分或求和；互相关衡量两个信号随相对位移的相似程度。

**FIR 与 IIR**：FIR 冲激响应有限；IIR 响应通常无限延续。两者不是简单按是否使用反馈直接等价分类。

**Hann 与 Hamming**：Hann 窗和 Hamming 窗采用不同余弦系数；“Hanning”是常见俗称，规范英文为 Hann。

**谱与功率谱密度**：谱的幅值、平方幅值与 PSD 的频率单位及归一化不同，不能直接比较数值。

**LTI 稳定性与因果性**：稳定性约束输入输出有界关系；因果性约束输出对未来输入的依赖，两者独立。

**群时延与相位时延**：群时延为负相位斜率；相位时延为负相位除以角频率，二者一般并不相同。

**插值与上采样**：单纯插入零是上采样的一个步骤；插值还需要适当滤波以恢复中间值。

## 参考资料与术语核验入口

以下资料用于知识结构与术语核对，并非逐条翻译来源：

- [MIT OCW — Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/)
- [SciPy — Signal Processing Reference](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [IEEE Signal Processing Society — Technical Committees](https://signalprocessingsociety.org/community-involvement/technical-committees)

## 数据与版本说明

- 数据源：`data/signal-processing.tsv`（英文、中文、缩写、释义，以 `|` 分隔）。
- 结构化检索：`data/terms.json` / `data/terms.csv`。
- PDF 下载：[`pdf/signal-processing.pdf`](../pdf/signal-processing.pdf)。
- 术语总量按本手册实际逐行统计，不进行跨领域去重。
- 欢迎通过 Pull Request 提交来源充分、上下文明确的修订。