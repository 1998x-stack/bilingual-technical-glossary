# 计算机图形学 · Computer Graphics

> TERM / ATLAS · 专业中英文术语手册 | Bilingual Technical Glossary

**500 条中英文术语 · 20 个专业章节 · 2026-11-27**

本册覆盖计算机图形学基础、空间变换、几何建模、光栅化、纹理、PBR 材质、光传输、蒙特卡洛路径追踪、全局光照、动画与仿真、OpenGL/Vulkan/Metal、GPU 着色器、BVH 加速结构、实时渲染优化、NeRF 与 3D Gaussian Splatting。

**重要约定：**相机坐标系、矩阵乘法顺序、左右手系、NDC 深度范围、颜色传递函数与 API 同步行为存在具体平台差异。公式及实现细节应以使用的 API 版本与官方规范为准。

**编辑状态：**20 章和英文术语去重经过结构化检查；未声称独立专家完成逐条审稿或跨阅读器 PDF 视觉与无障碍验收。

## 章节目录

- 01. 图形学概论、渲染系统与图像合成（25 条）
- 02. 线性代数、空间变换与坐标系统（25 条）
- 03. 三维几何、拓扑与网格结构（25 条）
- 04. 曲线曲面、参数化与几何建模（25 条）
- 05. 相机、投影、裁剪与可见性（25 条）
- 06. 光栅化流水线、片段处理与采样（25 条）
- 07. 纹理映射、过滤与纹理资源（25 条）
- 08. 光照、BRDF 与材质着色基础（25 条）
- 09. 辐射度量、光传输与渲染方程（25 条）
- 10. 光线求交、路径追踪与蒙特卡洛积分（25 条）
- 11. 阴影、环境遮蔽与全局光照（25 条）
- 12. 透明、体积渲染、色彩管理与后处理（25 条）
- 13. 动画、骨骼蒙皮与角色运动（25 条）
- 14. 物理仿真、粒子、布料与流体（25 条）
- 15. 图形 API、命令提交与显存资源（25 条）
- 16. GPU 着色语言、计算着色与高级管线（25 条）
- 17. 光线追踪加速结构、遍历与性能（25 条）
- 18. 实时渲染架构、抗锯齿与性能优化（25 条）
- 19. 神经图形学、可微渲染与新视角合成（25 条）
- 20. 格式资源、工具链、评测与生产工程（25 条）

---

## 01. 图形学概论、渲染系统与图像合成

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Computer Graphics | 计算机图形学 | CG | 研究用计算方法表示、处理和合成二维或三维视觉内容的领域。 |
| 2 | Rendering | 渲染 |  | 根据几何、材质、光照和相机生成图像的计算过程。 |
| 3 | Image Synthesis | 图像合成 |  | 从场景数据或算法构建目标图像的技术。 |
| 4 | Real-time Rendering | 实时渲染 |  | 在交互时限内持续生成图像帧的渲染方式。 |
| 5 | Offline Rendering | 离线渲染 |  | 允许较长计算时间追求高质量图像的渲染流程。 |
| 6 | Rendering Pipeline | 渲染流水线 |  | 将场景数据依阶段转换为图像结果的处理架构。 |
| 7 | Scene | 场景 |  | 包含对象、几何、材质、光源、相机和层级关系的描述集合。 |
| 8 | Scene Graph | 场景图 |  | 通过层级节点组织对象变换、属性和渲染关系的数据结构。 |
| 9 | Graphics Primitive | 图形基元 |  | 点、线段、三角形等可由图形系统直接处理的基本几何元素。 |
| 10 | Draw Call | 绘制调用 |  | 向图形 API 提交一次指定几何和状态的绘制命令。 |
| 11 | Render Pass | 渲染通道 |  | 按规定附件、操作和依赖组织的一段渲染工作。 |
| 12 | Frame | 渲染帧 |  | 动画或交互序列中在特定时间生成的一幅图像。 |
| 13 | Frame Rate | 帧率 | FPS | 每秒完成或显示的图像帧数量。 |
| 14 | Frame Time | 帧时间 |  | 生成或显示单帧所需的时间。 |
| 15 | Latency | 渲染延迟 |  | 从输入或提交到可见画面输出之间经历的时间。 |
| 16 | Rasterization | 光栅化 |  | 将连续几何基元转换为离散像素或采样覆盖的过程。 |
| 17 | Ray Tracing | 光线追踪 |  | 通过沿射线求交场景几何模拟可见性与部分光传播的渲染方法。 |
| 18 | Path Tracing | 路径追踪 |  | 以随机采样光路估计渲染方程积分的蒙特卡洛方法。 |
| 19 | Hybrid Rendering | 混合渲染 |  | 结合光栅化、光线追踪或其他技术生成画面的方法。 |
| 20 | Photorealistic Rendering | 照片级真实感渲染 |  | 追求成像结果在光学与视觉感知上接近真实照片的渲染。 |
| 21 | Non-photorealistic Rendering | 非真实感渲染 | NPR | 通过艺术化线条、色块或笔触表现视觉内容的技术。 |
| 22 | Physically Based Rendering | 基于物理的渲染 | PBR | 依据光传输与材质散射近似构建光照计算的渲染方法。 |
| 23 | Graphics API | 图形应用程序接口 |  | 应用程序调用 GPU 绘图资源和命令的编程接口。 |
| 24 | Graphics Driver | 图形驱动 |  | 将图形 API 命令转换为硬件可执行操作的软件层。 |
| 25 | Graphics Debugging | 图形调试 |  | 定位渲染管线、资源、着色器或图像输出错误的过程。 |

## 02. 线性代数、空间变换与坐标系统

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Vector | 向量 |  | 表示具有多个坐标分量的数学对象，常用于位置、方向与颜色。 |
| 2 | Point | 点 |  | 表示空间位置、在仿射变换下受平移影响的几何对象。 |
| 3 | Direction Vector | 方向向量 |  | 表示空间朝向、通常不受平移影响的向量。 |
| 4 | Normal Vector | 法向量 |  | 与曲面切平面垂直、常用于光照计算的方向。 |
| 5 | Dot Product | 点积 |  | 计算向量分量乘积之和，用于夹角和投影。 |
| 6 | Cross Product | 叉积 |  | 对三维向量产生与二者垂直的向量的运算。 |
| 7 | Vector Normalization | 向量归一化 |  | 将非零向量缩放到单位长度的操作。 |
| 8 | Matrix | 矩阵 |  | 用于表示线性映射、坐标变换和其他多维运算的数值数组。 |
| 9 | Matrix Multiplication | 矩阵乘法 |  | 按行列内积复合线性映射或变换的运算。 |
| 10 | Homogeneous Coordinates | 齐次坐标 |  | 在增加尺度分量后统一表示仿射与射影变换的坐标形式。 |
| 11 | Affine Transformation | 仿射变换 |  | 由线性变换和平移构成并保持平行性的几何映射。 |
| 12 | Translation | 平移 |  | 给空间点增加位移向量的变换。 |
| 13 | Rotation | 旋转 |  | 在保持欧氏长度和角度条件下改变方向的变换。 |
| 14 | Scaling | 缩放 |  | 沿一个或多个坐标轴改变几何尺寸的操作。 |
| 15 | Shearing | 错切 |  | 使坐标轴方向发生线性倾斜但保持平行关系的变换。 |
| 16 | Model Matrix | 模型矩阵 |  | 把对象局部坐标映射至世界坐标的矩阵。 |
| 17 | View Matrix | 视图矩阵 |  | 把世界坐标映射至相机或观察坐标系的矩阵。 |
| 18 | Projection Matrix | 投影矩阵 |  | 把观察空间坐标转换到裁剪坐标的矩阵。 |
| 19 | Model–View–Projection Matrix | 模型视图投影矩阵 | MVP | 将局部顶点逐级转换到裁剪空间的组合变换矩阵。 |
| 20 | World Space | 世界空间 |  | 场景对象共享的全局参考坐标系。 |
| 21 | Object Space | 对象局部空间 |  | 以单个模型自身原点和坐标轴定义的坐标系。 |
| 22 | View Space | 观察空间 |  | 以相机位置和朝向为参考的坐标系。 |
| 23 | Clip Space | 裁剪空间 |  | 顶点经投影变换后、透视除法之前所在的齐次坐标空间。 |
| 24 | Normalized Device Coordinates | 归一化设备坐标 | NDC | 透视除法后映射到规定标准立方体范围的坐标。 |
| 25 | Viewport Transform | 视口变换 |  | 把标准化设备坐标映射到窗口或渲染目标像素区域的转换。 |

## 03. 三维几何、拓扑与网格结构

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Polygon Mesh | 多边形网格 | Mesh | 由顶点、边和多边形面构成的离散表面表示。 |
| 2 | Vertex | 顶点 |  | 带有位置及可选法线、颜色和纹理坐标的几何采样点。 |
| 3 | Edge | 边 |  | 连接两个网格顶点并构成面边界的几何元素。 |
| 4 | Face | 面 |  | 由一组有序顶点组成的网格表面单元。 |
| 5 | Triangle Mesh | 三角网格 |  | 所有面均为三角形的离散曲面表示。 |
| 6 | Quad Mesh | 四边形网格 |  | 以四边形为主要面片的网格结构。 |
| 7 | Vertex Buffer | 顶点缓冲区 | VBO | 在 GPU 或图形系统中存放顶点属性数据的缓冲资源。 |
| 8 | Index Buffer | 索引缓冲区 | IBO | 存放顶点索引以复用顶点并组装几何基元的资源。 |
| 9 | Vertex Attribute | 顶点属性 |  | 附着于顶点的位置、法线、切线或纹理坐标等数据。 |
| 10 | Primitive Topology | 基元拓扑 |  | 规定连续顶点索引如何组成点、线或三角形的组织方式。 |
| 11 | Triangle Strip | 三角形带 |  | 相邻三角形共享前后顶点、以较少索引描述连续表面的拓扑。 |
| 12 | Winding Order | 顶点绕序 |  | 按顺时针或逆时针顺序排列面片顶点的约定。 |
| 13 | Face Normal | 面法线 |  | 由面片顶点几何确定的垂直方向。 |
| 14 | Vertex Normal | 顶点法线 |  | 用于平滑明暗插值的顶点法向属性。 |
| 15 | Tangent Space | 切线空间 |  | 由表面切线、副切线和法线形成的局部坐标系。 |
| 16 | Half-edge Data Structure | 半边数据结构 |  | 用成对有向半边高效表示网格顶点、面与邻接关系的结构。 |
| 17 | Manifold Mesh | 流形网格 |  | 局部拓扑邻域符合二维流形性质的表面网格。 |
| 18 | Non-manifold Geometry | 非流形几何 |  | 存在多面共享异常边或不符合二维曲面邻域条件的网格结构。 |
| 19 | Mesh Connectivity | 网格连接关系 |  | 描述顶点、边和面之间邻接与关联的拓扑信息。 |
| 20 | Mesh Simplification | 网格简化 |  | 在控制几何误差条件下减少网格顶点和面数量的过程。 |
| 21 | Edge Collapse | 边折叠 |  | 合并边的两个端点以移除局部网格元素的简化操作。 |
| 22 | Subdivision Surface | 细分曲面 |  | 通过重复细分控制网格并计算极限曲面得到平滑表面的技术。 |
| 23 | Catmull–Clark Subdivision | Catmull–Clark 细分 |  | 利用面点、边点和顶点规则细分多边形网格的经典算法。 |
| 24 | Loop Subdivision | Loop 三角网格细分 |  | 针对三角网格生成平滑极限曲面的细分算法。 |
| 25 | Constructive Solid Geometry | 构造实体几何 | CSG | 通过实体并、交、差等布尔运算组合几何对象的表示方法。 |

## 04. 曲线曲面、参数化与几何建模

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Parametric Curve | 参数曲线 |  | 用连续参数映射生成一维空间轨迹的几何表示。 |
| 2 | Bézier Curve | 贝塞尔曲线 |  | 由控制点和伯恩斯坦基函数定义的多项式参数曲线。 |
| 3 | Bézier Surface | 贝塞尔曲面 |  | 通过二维参数和控制点网格构造的张量积曲面。 |
| 4 | B-spline Curve | B 样条曲线 |  | 使用局部支撑基函数和节点序列定义的分段多项式曲线。 |
| 5 | NURBS | 非均匀有理 B 样条 | NURBS | 用有理基函数和非均匀节点精确或近似描述曲线与曲面的表示。 |
| 6 | Control Point | 控制点 |  | 决定参数曲线或曲面形状的几何参数点。 |
| 7 | Control Polygon | 控制多边形 |  | 按顺序连接曲线控制点形成的辅助几何折线。 |
| 8 | Bernstein Polynomial | 伯恩斯坦多项式 |  | 用于贝塞尔曲线和曲面构造的多项式基函数。 |
| 9 | de Casteljau Algorithm | 德卡斯特里奥算法 |  | 以递归线性插值稳定计算贝塞尔曲线上点的方法。 |
| 10 | Knot Vector | 节点向量 |  | B 样条及 NURBS 中定义分段参数域和连续性结构的序列。 |
| 11 | Curve Continuity | 曲线连续性 |  | 描述相邻曲线段位置、切线和高阶导数连接程度的性质。 |
| 12 | G1 Continuity | 一阶几何连续性 | G1 | 两段曲线在连接点切线方向一致的几何平滑条件。 |
| 13 | C1 Continuity | 一阶参数连续性 | C1 | 两段曲线在连接点位置和一阶导数连续的条件。 |
| 14 | Parametric Surface | 参数曲面 |  | 利用两个参数连续映射到三维位置的曲面表示。 |
| 15 | Implicit Surface | 隐式曲面 |  | 由满足标量函数等于指定值的点集定义的表面。 |
| 16 | Signed Distance Function | 有符号距离函数 | SDF | 以到表面的有向距离描述几何内部与外部的连续函数。 |
| 17 | Level Set | 水平集 |  | 由标量函数达到固定值所确定的点集或曲面。 |
| 18 | Surface of Revolution | 旋转曲面 |  | 将平面轮廓绕某条轴旋转形成的曲面。 |
| 19 | Extrusion | 拉伸建模 |  | 沿指定方向或路径移动二维截面生成三维几何。 |
| 20 | Sweep Surface | 扫掠曲面 |  | 让截面沿空间曲线运动形成的曲面。 |
| 21 | Boolean Modeling | 布尔建模 |  | 通过并集、交集和差集编辑封闭实体形状的方法。 |
| 22 | Tessellation | 曲面镶嵌 |  | 把连续或粗糙表面进一步离散为多边形基元的过程。 |
| 23 | UV Parameterization | UV 参数化 |  | 建立网格表面位置到二维纹理坐标的映射。 |
| 24 | Surface Distortion | 曲面参数畸变 |  | 曲面到二维展开时在面积、角度或长度上产生的变形。 |
| 25 | Retopology | 网格重拓扑 |  | 在保持外形的同时重新设计表面网格边流和面分布的过程。 |

## 05. 相机、投影、裁剪与可见性

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Virtual Camera | 虚拟相机 |  | 渲染场景中定义观察位置、方向、视角和成像参数的抽象设备。 |
| 2 | Camera Coordinate System | 相机坐标系 |  | 以虚拟相机为参考原点和轴向的三维坐标系。 |
| 3 | Perspective Projection | 透视投影 |  | 通过投影中心将三维点映射到二维平面、产生近大远小效果的几何变换。 |
| 4 | Orthographic Projection | 正交投影 |  | 以相互平行投影射线把三维点映射到二维平面的方式。 |
| 5 | Field of View | 视场角 | FOV | 虚拟相机在水平或垂直方向覆盖的角度范围。 |
| 6 | Near Clipping Plane | 近裁剪面 |  | 限制可见视锥中距离相机最近范围的裁剪平面。 |
| 7 | Far Clipping Plane | 远裁剪面 |  | 限制可见视锥最远空间范围的裁剪平面。 |
| 8 | View Frustum | 观察视锥 |  | 透视相机中由视场与近远裁剪面确定的可见空间体。 |
| 9 | Frustum Culling | 视锥剔除 |  | 在绘制前跳过完全位于观察视锥之外物体的优化。 |
| 10 | Back-face Culling | 背面剔除 |  | 根据面片朝向与正反面约定跳过不可见朝向的三角形。 |
| 11 | Occlusion Culling | 遮挡剔除 |  | 跳过被其他几何完全遮挡、不会影响可见结果的对象。 |
| 12 | Clipping | 几何裁剪 |  | 将超出指定裁剪空间的基元截断或丢弃的过程。 |
| 13 | Homogeneous Clipping | 齐次裁剪 |  | 在透视除法之前利用齐次坐标边界裁剪几何基元的步骤。 |
| 14 | Perspective Divide | 透视除法 |  | 将裁剪空间坐标除以齐次 w 分量得到归一化设备坐标的操作。 |
| 15 | Depth Buffer | 深度缓冲 | Z-buffer | 为每个像素或采样位置保存深度以比较遮挡关系的资源。 |
| 16 | Depth Test | 深度测试 |  | 依据预设比较规则判断新片段是否能通过深度可见性检查的操作。 |
| 17 | Depth Write | 深度写入 |  | 在满足规则时更新深度缓冲数值的操作。 |
| 18 | Reversed-Z | 反向 Z 深度映射 |  | 让近处深度取较大值以改善部分浮点深度分布精度的技术。 |
| 19 | Depth Precision | 深度精度 |  | 深度缓冲能够区分相近表面深度数值的能力。 |
| 20 | Z-fighting | 深度闪烁 |  | 两个深度值接近的表面因深度量化误差交替覆盖的伪影。 |
| 21 | Screen Space | 屏幕空间 |  | 经投影和视口变换后按像素位置描述的二维坐标系。 |
| 22 | Scissor Test | 剪裁矩形测试 |  | 将片段处理限制在指定屏幕矩形内的测试。 |
| 23 | Stencil Buffer | 模板缓冲 |  | 每个片段位置保存整数标记、用于遮罩或多阶段渲染的资源。 |
| 24 | Stencil Test | 模板测试 |  | 根据模板缓冲中的整数值决定片段是否保留的测试。 |
| 25 | Visibility Buffer | 可见性缓冲 |  | 存储可见基元标识或局部坐标供后续着色阶段使用的缓冲结构。 |

## 06. 光栅化流水线、片段处理与采样

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Vertex Processing | 顶点处理 |  | 将顶点属性经变换和可编程处理后输出给基元组装的阶段。 |
| 2 | Primitive Assembly | 基元组装 |  | 依据顶点数据和拓扑关系形成三角形、线或点的操作。 |
| 3 | Vertex Shader | 顶点着色器 |  | 逐顶点执行、通常输出裁剪坐标和待插值属性的可编程着色阶段。 |
| 4 | Tessellation Control Shader | 曲面细分控制着色器 |  | 在支持的图形管线中确定细分等级和控制点信息的着色阶段。 |
| 5 | Tessellation Evaluation Shader | 曲面细分计算着色器 |  | 在细分生成的参数位置评价曲面并输出顶点的阶段。 |
| 6 | Geometry Shader | 几何着色器 |  | 在部分图形 API 中以完整基元为输入并可产生新基元的着色阶段。 |
| 7 | Fragment Shader | 片段着色器 |  | 为光栅化产生的片段计算颜色、深度或其他输出的可编程阶段。 |
| 8 | Fragment | 片段 |  | 光栅化基元在像素或采样位置生成的待测试候选记录。 |
| 9 | Pixel Sample | 像素采样点 |  | 在像素内指定位置进行覆盖或着色评估的采样位置。 |
| 10 | Triangle Rasterization | 三角形光栅化 |  | 根据三角形顶点与屏幕覆盖规则生成片段的过程。 |
| 11 | Barycentric Coordinates | 重心坐标 |  | 以三角形顶点加权组合表示平面内点位置的坐标形式。 |
| 12 | Attribute Interpolation | 顶点属性插值 |  | 根据片段位置由三角形顶点属性计算片段对应值的过程。 |
| 13 | Perspective-correct Interpolation | 透视校正插值 |  | 利用齐次 w 调整属性插值以符合透视投影的几何关系。 |
| 14 | Screen-space Derivatives | 屏幕空间偏导数 |  | 估算相邻片段间变量变化率、常用于纹理 LOD 选择的运算。 |
| 15 | Early-Z Test | 提前深度测试 | Early-Z | 在片段着色前尝试执行深度测试以省去被遮挡片段计算的优化。 |
| 16 | Late-Z Test | 延迟深度测试 | Late-Z | 在片段着色后按管线语义执行深度检查的方式。 |
| 17 | Alpha Test | Alpha 阈值测试 |  | 根据透明度或遮罩阈值丢弃部分片段的技术。 |
| 18 | Discard Operation | 片段丢弃 |  | 在片段着色阶段终止当前片段后续处理的操作。 |
| 19 | Color Attachment | 颜色附件 |  | 在渲染通道中接收颜色输出的图像资源。 |
| 20 | Render Target | 渲染目标 |  | 供图形流水线写入最终或中间像素结果的图像。 |
| 21 | Framebuffer | 帧缓冲 |  | 关联一组颜色、深度或模板附件的渲染对象或资源集合。 |
| 22 | Multisample Anti-aliasing | 多重采样抗锯齿 | MSAA | 在像素内保存多个覆盖或深度采样以改善几何边缘的抗锯齿技术。 |
| 23 | Coverage Mask | 覆盖掩码 |  | 描述像素内部哪些多重采样点被基元覆盖的位集合。 |
| 24 | Sample Shading | 逐采样着色 |  | 允许针对多个采样位置分别执行片段着色的渲染配置。 |
| 25 | Resolve Operation | 多采样解析 |  | 把多重采样渲染目标转换为单采样图像的过程。 |

## 07. 纹理映射、过滤与纹理资源

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Texture Mapping | 纹理映射 |  | 依据表面坐标将图像或程序生成信号附着到几何表面的技术。 |
| 2 | Texture Coordinate | 纹理坐标 | UV | 确定模型表面位置对应二维或三维纹理位置的参数。 |
| 3 | UV Unwrapping | UV 展开 |  | 将三维表面划分并映射到二维纹理域的过程。 |
| 4 | Texture Atlas | 纹理图集 |  | 将多个纹理区域打包进一张较大图像以便资源管理的技术。 |
| 5 | Mipmap | 多级渐远纹理 | Mipmap | 为纹理预计算逐级降低分辨率的图像金字塔。 |
| 6 | Level of Detail | 纹理细节等级 | LOD | 根据投影尺寸选择采样纹理层级的参数。 |
| 7 | Texture Filtering | 纹理过滤 |  | 依据纹理坐标从离散纹素生成连续采样结果的过程。 |
| 8 | Nearest Filtering | 最近邻纹理过滤 |  | 选取最接近目标坐标的纹素值作为结果的方式。 |
| 9 | Bilinear Filtering | 双线性纹理过滤 |  | 在同一级纹理图像中由相邻四个纹素做二维线性插值的方法。 |
| 10 | Trilinear Filtering | 三线性纹理过滤 |  | 在相邻 mipmap 层各做双线性采样后按 LOD 插值的方法。 |
| 11 | Anisotropic Filtering | 各向异性过滤 |  | 考虑投影纹理采样足迹方向差异、降低斜视表面模糊的过滤技术。 |
| 12 | Texture Sampler | 纹理采样器 |  | 定义过滤模式、寻址模式与 LOD 限制的图形资源。 |
| 13 | Texel | 纹素 |  | 纹理图像中某个离散采样位置的像素样本。 |
| 14 | Texture Address Mode | 纹理寻址模式 |  | 定义纹理坐标超出有效范围时采用重复、夹取或镜像等行为的配置。 |
| 15 | Wrap Mode | 重复纹理模式 |  | 将超范围纹理坐标周期性映射回纹理域的寻址方式。 |
| 16 | Clamp Mode | 夹取纹理模式 |  | 把超范围纹理坐标限制到纹理边界或边界色的采样方式。 |
| 17 | Normal Mapping | 法线贴图 |  | 从纹理读取法向扰动以改变表面光照细节的技术。 |
| 18 | Bump Mapping | 凹凸映射 |  | 利用高度变化扰动表面法线、模拟细节而不真正改变几何轮廓的方法。 |
| 19 | Displacement Mapping | 位移贴图 |  | 按高度或位移信号实际改变几何表面位置的技术。 |
| 20 | Parallax Mapping | 视差贴图 |  | 根据视线方向偏移纹理采样坐标以模拟表面深度的技术。 |
| 21 | Environment Mapping | 环境贴图 |  | 利用方向相关纹理近似场景远处环境辐射或反射的技术。 |
| 22 | Cubemap | 立方体贴图 | Cubemap | 以六个方向面纹理表示环绕三维方向空间的图像结构。 |
| 23 | Texture Compression | 纹理压缩 |  | 以专门块编码减少图形纹理的存储占用和带宽需求的技术。 |
| 24 | Sparse Texture | 稀疏纹理 |  | 允许纹理虚拟地址范围大于实际已驻留物理页面的资源形式。 |
| 25 | Virtual Texturing | 虚拟纹理 |  | 按需把巨大纹理的局部页加载到显存、实现细节分块管理的技术。 |

## 08. 光照、BRDF 与材质着色基础

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Lighting Model | 光照模型 |  | 近似或物理建模光源、表面与观察方向之间关系的计算规则。 |
| 2 | Shading | 着色 |  | 根据表面位置、法线、材质与光照计算可见外观的过程。 |
| 3 | Flat Shading | 平面着色 |  | 以单个面法线或面级结果生成多边形统一明暗的方式。 |
| 4 | Gouraud Shading | 高洛德着色 |  | 在顶点处计算光照并将颜色沿基元插值到片段的方法。 |
| 5 | Phong Shading | Phong 逐像素着色 |  | 在片段位置插值法向再计算光照的着色方式。 |
| 6 | Lambertian Reflection | 朗伯反射 |  | 出射辐亮度不随观察方向变化的理想漫反射模型。 |
| 7 | Diffuse Reflection | 漫反射 |  | 光在粗糙或散射表面向多个方向分布出射的反射过程。 |
| 8 | Specular Reflection | 镜面反射 |  | 光沿与镜面方向相关的集中方向反射的行为。 |
| 9 | Blinn–Phong Model | Blinn–Phong 光照模型 |  | 利用半角向量与法线夹角计算经验镜面高光的着色模型。 |
| 10 | Bidirectional Reflectance Distribution Function | 双向反射分布函数 | BRDF | 描述入射方向辐照度对特定出射方向辐亮度贡献的函数。 |
| 11 | Bidirectional Scattering Distribution Function | 双向散射分布函数 | BSDF | 统一描述表面反射和透射方向散射的函数。 |
| 12 | Microfacet Model | 微表面模型 |  | 将粗糙表面视为微小镜面单元分布以计算反射的模型。 |
| 13 | Normal Distribution Function | 微法线分布函数 | NDF | 描述微表面法线方向统计分布的函数。 |
| 14 | GGX Distribution | GGX 微表面分布 |  | 具有较长反射尾部的常用 Trowbridge–Reitz 微表面法线分布。 |
| 15 | Fresnel Equations | 菲涅耳方程 |  | 描述光在介质界面反射与透射比例随角度和折射率变化的公式。 |
| 16 | Schlick Approximation | Schlick 菲涅耳近似 |  | 用简单多项式近似角度相关反射率的技术。 |
| 17 | Geometric Shadowing Function | 微表面遮蔽函数 |  | 描述微表面相互遮挡和掩蔽对可见反射贡献影响的函数。 |
| 18 | Roughness | 表面粗糙度 |  | 控制微表面分布宽窄及反射高光形状的材质参数。 |
| 19 | Metallic Parameter | 金属度参数 |  | 在常见金属度工作流中控制材质按金属或电介质方式近似的参数。 |
| 20 | Base Color | 基色 |  | 材质基础颜色参数，其对金属和非金属散射的含义随工作流变化。 |
| 21 | Albedo | 反照率 |  | 衡量表面反射入射辐射能量比例或反射底色的量，需声明具体定义。 |
| 22 | Energy Conservation | 能量守恒 |  | 要求散射出的总能量不超过相应入射能量的物理约束。 |
| 23 | Emissive Material | 自发光材质 |  | 在着色模型中主动向环境发射辐射的表面材质。 |
| 24 | Normal Map Tangent Basis | 法线贴图切线基 |  | 用于把纹理空间法向转换为场景空间的切线、副切线与法线坐标框架。 |
| 25 | Material Parameterization | 材质参数化 |  | 用一组可编辑数值、贴图和模型定义表面光学行为的过程。 |

## 09. 辐射度量、光传输与渲染方程

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Radiant Flux | 辐射通量 |  | 单位时间传输的辐射能量，单位为瓦。 |
| 2 | Radiant Intensity | 辐射强度 |  | 单位立体角方向上的辐射通量，单位瓦每球面度。 |
| 3 | Irradiance | 辐照度 |  | 单位表面面积接收到的辐射通量，单位瓦每平方米。 |
| 4 | Radiance | 辐亮度 |  | 单位投影面积和单位立体角内的辐射通量密度。 |
| 5 | Solid Angle | 立体角 |  | 以单位球面所截面积度量的三维方向区域大小。 |
| 6 | Spectral Radiance | 光谱辐亮度 |  | 按波长或频率描述辐亮度分布的物理量。 |
| 7 | Visible Spectrum | 可见光谱 |  | 人眼能够感知的电磁波波长范围及其光谱成分。 |
| 8 | Rendering Equation | 渲染方程 |  | 由自发光项与所有入射方向反射贡献积分组成的光传输平衡方程。 |
| 9 | Light Transport | 光传输 |  | 光子或辐射在场景中传播、反射、透射与吸收的过程。 |
| 10 | Incident Radiance | 入射辐亮度 |  | 从指定方向到达表面点的辐射亮度。 |
| 11 | Outgoing Radiance | 出射辐亮度 |  | 由表面点沿给定方向离开的辐射亮度。 |
| 12 | Surface Scattering | 表面散射 |  | 光与材料界面相互作用后发生反射或透射的过程。 |
| 13 | Hemispherical Integral | 半球积分 |  | 对表面法线方向半球内所有入射光方向进行积分的操作。 |
| 14 | Cosine Foreshortening | 余弦投影因子 |  | 辐照能量按入射方向与表面法线夹角余弦缩减的几何因子。 |
| 15 | Visibility Function | 可见性函数 |  | 判断两点之间光路是否被场景几何遮挡的函数。 |
| 16 | Light Source | 光源 |  | 向场景辐射能量并影响物体外观的对象或环境。 |
| 17 | Point Light | 点光源 |  | 在单一位置向外发射辐射的理想化光源。 |
| 18 | Directional Light | 方向光 |  | 以几乎平行的光线方向近似远处光源的模型。 |
| 19 | Area Light | 面光源 |  | 具有有限发光表面积、可产生软阴影的光源。 |
| 20 | Spotlight | 聚光灯 |  | 向有限角度锥形区域发射光线的光源模型。 |
| 21 | Environment Light | 环境光源 |  | 按空间方向定义远处入射辐射的照明模型。 |
| 22 | Inverse-square Law | 平方反比定律 |  | 理想点源辐射在均匀空间中的照度随距离平方倒数衰减。 |
| 23 | Light Sampling | 光源采样 |  | 从光源分布选择位置或方向以估计光照贡献的随机过程。 |
| 24 | Importance Sampling | 重要性采样 |  | 按与积分被积函数贡献相关的概率分布采样以降低方差的方法。 |
| 25 | Multiple Importance Sampling | 多重重要性采样 | MIS | 组合多种采样策略并按权重融合以降低渲染积分估计方差的方法。 |

## 10. 光线求交、路径追踪与蒙特卡洛积分

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Ray | 射线 |  | 由起点和方向参数化的半无限直线。 |
| 2 | Primary Ray | 主射线 |  | 从相机出发、寻找场景第一个可见表面的光线。 |
| 3 | Shadow Ray | 阴影射线 |  | 连接着色点与光源采样点以测试遮挡关系的射线。 |
| 4 | Secondary Ray | 次级射线 |  | 从表面散射或反射继续发出的后续追踪射线。 |
| 5 | Ray–Triangle Intersection | 射线三角形求交 |  | 计算射线是否与三角形相交及其参数位置的算法。 |
| 6 | Möller–Trumbore Algorithm | Möller–Trumbore 求交算法 |  | 利用代数方法求射线与三角形交点及重心坐标的算法。 |
| 7 | Ray–Box Intersection | 射线包围盒求交 |  | 判断射线是否经过轴对齐或其他类型包围盒的测试。 |
| 8 | Ray Marching | 射线步进 |  | 沿射线逐步采样场或距离函数以求交或积分的方法。 |
| 9 | Sphere Tracing | 球面追踪 |  | 利用有符号距离场的距离下界自适应推进射线求交的技术。 |
| 10 | Monte Carlo Integration | 蒙特卡洛积分 |  | 用随机样本均值估计高维积分的数值方法。 |
| 11 | Monte Carlo Estimator | 蒙特卡洛估计器 |  | 根据随机样本及其概率密度构造积分近似的统计量。 |
| 12 | Sampling Distribution | 采样分布 |  | 决定随机样本在空间或方向域出现概率的分布。 |
| 13 | Probability Density Function | 概率密度函数 | PDF | 描述连续随机变量在相应测度下的密度函数。 |
| 14 | Variance | 方差 |  | 衡量随机估计结果围绕其期望波动大小的统计量。 |
| 15 | Bias | 估计偏差 |  | 估计器期望与目标真值之间的差异。 |
| 16 | Stratified Sampling | 分层采样 |  | 将采样域分成多个区域并分别抽取样本以改善覆盖的方法。 |
| 17 | Low-discrepancy Sequence | 低差异序列 |  | 在采样空间中具有较均匀覆盖性质的确定性或随机化点序列。 |
| 18 | Quasi-Monte Carlo | 拟蒙特卡洛 |  | 利用低差异序列替代纯随机样本进行数值积分的方法。 |
| 19 | Path Throughput | 路径通量权重 |  | 沿随机光路累计散射函数、余弦和采样密度因子的权重。 |
| 20 | Russian Roulette | 俄罗斯轮盘赌终止 |  | 按概率终止低贡献路径并适当放大存活路径权重的无偏终止技术。 |
| 21 | Next-event Estimation | 下一事件估计 | NEE | 在路径顶点显式采样光源以估计直接照明的方法。 |
| 22 | Bidirectional Path Tracing | 双向路径追踪 | BDPT | 分别从相机与光源构造子路径、再连接估计光传输的方法。 |
| 23 | Metropolis Light Transport | Metropolis 光传输 | MLT | 在路径空间以马尔可夫链采样高贡献路径的渲染技术。 |
| 24 | Denoising | 渲染去噪 |  | 利用空间、时间或学习先验降低低样本渲染噪声的处理。 |
| 25 | Samples per Pixel | 每像素样本数 | SPP | 单个像素用于统计估计颜色的光线或积分样本数量。 |

## 11. 阴影、环境遮蔽与全局光照

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Direct Illumination | 直接照明 |  | 光源未经过其他场景表面反弹而直接到达着色点的光照。 |
| 2 | Indirect Illumination | 间接照明 |  | 经一次或多次表面反射或透射后到达着色点的光照。 |
| 3 | Global Illumination | 全局光照 | GI | 考虑场景间多次光传输对可见外观影响的渲染方法集合。 |
| 4 | Ambient Occlusion | 环境光遮蔽 | AO | 近似衡量着色点附近半球方向被几何阻挡程度的技术。 |
| 5 | Screen-space Ambient Occlusion | 屏幕空间环境遮蔽 | SSAO | 基于深度与法线缓冲估计可见表面邻近遮挡的近似方法。 |
| 6 | Horizon-based Ambient Occlusion | 地平线环境遮蔽 | HBAO | 按局部视方向地平线角度估计屏幕空间遮挡的技术。 |
| 7 | Screen-space Reflections | 屏幕空间反射 | SSR | 利用屏幕可见深度与颜色近似追踪反射的技术。 |
| 8 | Shadow Mapping | 阴影贴图 |  | 从光源视角渲染深度并在着色时比较以判断阴影的技术。 |
| 9 | Shadow Map | 阴影深度图 |  | 保存光源视角下最近可见表面深度的纹理资源。 |
| 10 | Percentage-closer Filtering | 百分比渐近过滤 | PCF | 对多个阴影比较采样结果过滤以平滑阴影边界的技术。 |
| 11 | Variance Shadow Mapping | 方差阴影贴图 | VSM | 利用深度矩估计遮挡概率的阴影过滤方法。 |
| 12 | Cascaded Shadow Maps | 级联阴影贴图 | CSM | 将相机视锥划分为距离段、分别使用阴影贴图提高远近分辨率的技术。 |
| 13 | Soft Shadow | 软阴影 |  | 有限面积光源形成随遮挡几何变化的半影与柔和边界。 |
| 14 | Hard Shadow | 硬阴影 |  | 理想点光源或方向光通常产生的清晰阴影边界。 |
| 15 | Penumbra | 半影 |  | 部分光源被遮挡而导致照明强度逐渐变化的区域。 |
| 16 | Radiosity | 辐射度法 |  | 假定近似漫反射表面并通过面片间能量交换求解全局照明的算法。 |
| 17 | Lightmap | 光照贴图 |  | 预计算或烘焙到纹理中的场景照明数据。 |
| 18 | Light Baking | 光照烘焙 |  | 离线求取静态表面照明并存为贴图或探针的过程。 |
| 19 | Light Probe | 光照探针 |  | 在离散空间位置记录环境照明信息以供插值的采样设施。 |
| 20 | Irradiance Volume | 辐照度体积 |  | 在三维网格中存储和插值间接照明的光照表示。 |
| 21 | Reflection Probe | 反射探针 |  | 在局部空间存储环境反射贴图以近似材质反射的资源。 |
| 22 | Voxel Cone Tracing | 体素锥追踪 |  | 通过体素场中扩展锥形积分近似间接光照的技术。 |
| 23 | Screen-space Global Illumination | 屏幕空间全局光照 | SSGI | 利用当前帧深度、法线和颜色估计部分间接照明的方法。 |
| 24 | Radiance Cache | 辐亮度缓存 |  | 保存可重复使用的场景辐亮度估计以降低多次求解开销的结构。 |
| 25 | Temporal Reprojection | 时间重投影 |  | 利用运动信息把前一帧结果映射到当前帧位置复用历史数据的技术。 |

## 12. 透明、体积渲染、色彩管理与后处理

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Alpha Blending | Alpha 混合 |  | 根据透明度权重组合源颜色与目标颜色的图像合成操作。 |
| 2 | Premultiplied Alpha | 预乘 Alpha |  | 在存储颜色时先把颜色通道乘以对应透明度的表示方法。 |
| 3 | Order-independent Transparency | 顺序无关透明 | OIT | 减少透明物体绘制顺序对混合结果依赖的技术集合。 |
| 4 | Depth Peeling | 深度剥离 |  | 分层提取可见深度表面、用于透明物体排序混合的方法。 |
| 5 | Weighted Blended OIT | 加权混合顺序无关透明 |  | 用加权累积近似透明层合成、减少严格排序要求的方法。 |
| 6 | Refraction | 折射 |  | 光经过不同折射率介质界面时传播方向发生变化的过程。 |
| 7 | Index of Refraction | 折射率 | IOR | 描述介质中光相速度相对真空速度变化的物理量。 |
| 8 | Snell's Law | 斯涅尔定律 |  | 规定折射光线方向与两介质折射率之间关系的定律。 |
| 9 | Total Internal Reflection | 全内反射 |  | 光从高折射率向低折射率介质传播且入射角过大时无法发生传播透射的现象。 |
| 10 | Volume Rendering | 体积渲染 |  | 根据体积介质内吸收、散射与发光沿射线积分生成图像的过程。 |
| 11 | Participating Media | 参与介质 |  | 能在体积内吸收、发射或散射光线的雾、烟、云等介质。 |
| 12 | Extinction Coefficient | 消光系数 |  | 描述单位传播距离内因吸收与外散射减少辐射的系数。 |
| 13 | Phase Function | 相函数 |  | 描述介质内光散射方向概率分布的函数。 |
| 14 | Transmittance | 透射率 |  | 光沿介质路径传播后未被消光的能量比例。 |
| 15 | Beer–Lambert Law | 比尔—朗伯定律 |  | 在适用条件下描述均匀介质透射率随光程指数衰减的定律。 |
| 16 | Volumetric Fog | 体积雾 |  | 通过体积散射模型渲染的雾气效果。 |
| 17 | Bloom | 辉光效果 |  | 让高亮区域向邻域扩散产生视觉泛光的后处理效果。 |
| 18 | Tone Mapping | 色调映射 |  | 将高动态范围辐亮度或图像值映射到显示设备较窄动态范围的过程。 |
| 19 | ACES Tone Mapping | ACES 色调映射 |  | 使用学院色彩编码系统相关变换处理高动态范围图像显示的流程。 |
| 20 | Gamma Encoding | 伽马编码 |  | 通过非线性编码函数将线性光数值转换为适合存储或显示的值。 |
| 21 | Linear Color Space | 线性光颜色空间 |  | 颜色数值按物理光强或三刺激值线性比例表示的空间。 |
| 22 | sRGB Transfer Function | sRGB 传递函数 |  | 规定线性 RGB 与 sRGB 非线性编码之间转换关系的函数。 |
| 23 | Color Grading | 调色 |  | 通过曝光、曲线与颜色变换调整画面审美风格的后期处理。 |
| 24 | Depth of Field | 景深 |  | 成像系统中目标距焦平面不同位置导致模糊程度变化的现象。 |
| 25 | Motion Blur | 运动模糊 |  | 曝光时间内场景或相机移动在图像中造成的空间模糊效果。 |

## 13. 动画、骨骼蒙皮与角色运动

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Computer Animation | 计算机动画 |  | 随时间改变场景对象的几何、位姿或材质以生成连续运动的技术。 |
| 2 | Keyframe Animation | 关键帧动画 |  | 在离散时间设置控制参数并通过插值生成中间动画状态的方法。 |
| 3 | Animation Curve | 动画曲线 |  | 定义对象某个属性随时间变化的参数函数或控制曲线。 |
| 4 | Interpolation Curve | 插值曲线 |  | 在给定控制时间点之间构造连续属性数值的曲线。 |
| 5 | Linear Interpolation | 线性插值 | Lerp | 按参数对两个数值或向量进行加权线性组合的操作。 |
| 6 | Spherical Linear Interpolation | 球面线性插值 | Slerp | 沿单位四元数球面最短弧插值旋转的技术。 |
| 7 | Quaternion | 四元数 |  | 由一个实部和三个虚部组成、常用于表示与插值三维旋转的代数对象。 |
| 8 | Euler Angles | 欧拉角 |  | 按指定旋转轴序和三个角度表示三维旋转的一组参数。 |
| 9 | Gimbal Lock | 万向锁 |  | 欧拉角参数化中两个旋转轴重合而丢失自由度的奇异现象。 |
| 10 | Skeletal Animation | 骨骼动画 |  | 通过关节层级变换驱动角色网格形变的动画方法。 |
| 11 | Joint | 关节 |  | 骨骼层级中定义局部旋转、平移或其他自由度的连接位置。 |
| 12 | Bone | 骨骼节点 |  | 构成角色绑定层级并影响网格顶点变换的结构元素。 |
| 13 | Rigging | 角色绑定 |  | 建立骨架、控制器及其与网格变形关联的过程。 |
| 14 | Skinning | 蒙皮 |  | 根据骨骼变换和权重计算角色表面顶点变形的方法。 |
| 15 | Linear Blend Skinning | 线性混合蒙皮 | LBS | 对多个骨骼变换结果按权重线性组合顶点位置的技术。 |
| 16 | Dual Quaternion Skinning | 对偶四元数蒙皮 | DQS | 用对偶四元数插值刚体变换以降低部分 LBS 形变伪影的方法。 |
| 17 | Blend Shape | 混合形状 |  | 通过加权组合预设目标网格形状实现面部或局部变形的技术。 |
| 18 | Morph Target | 形态目标 |  | 为网格指定另一组顶点位置以支持渐变形变的目标形状。 |
| 19 | Forward Kinematics | 正向运动学 | FK | 由关节角度和层级变换推算末端对象位姿的过程。 |
| 20 | Inverse Kinematics | 逆向运动学 | IK | 根据目标末端位姿求解满足约束的关节配置的任务。 |
| 21 | Motion Capture | 动作捕捉 | MoCap | 通过传感器或视觉估计真实人物或物体运动并转换为动画的技术。 |
| 22 | Animation Blending | 动画混合 |  | 按权重或状态规则组合多个动画片段输出角色姿态的技术。 |
| 23 | Animation State Machine | 动画状态机 |  | 根据行为状态与转换条件组织动画片段播放的控制结构。 |
| 24 | Retargeting | 动作重定向 |  | 把一个角色骨骼或动作数据映射到另一角色的动画技术。 |
| 25 | Root Motion | 根节点运动 |  | 由动画序列中的根骨骼或角色根节点定义整体位移与旋转的运动信息。 |

## 14. 物理仿真、粒子、布料与流体

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Physics Simulation | 物理仿真 |  | 通过数值方法近似计算刚体、柔体或流体随时间演化的过程。 |
| 2 | Rigid Body | 刚体 |  | 理想化为内部点间距离保持不变的物理对象。 |
| 3 | Rigid Body Dynamics | 刚体动力学 |  | 根据质量、惯性和外力计算刚体平移及旋转运动的方法。 |
| 4 | Soft Body | 软体 |  | 能够发生连续弹性或塑性变形的可模拟对象。 |
| 5 | Mass–Spring System | 质点弹簧系统 |  | 用质量节点与弹簧约束近似模拟可变形几何的模型。 |
| 6 | Cloth Simulation | 布料模拟 |  | 通过粒子、网格或连续体方法近似计算布面褶皱与运动的过程。 |
| 7 | Collision Detection | 碰撞检测 |  | 判断两个几何对象是否接触、穿透或将发生碰撞的计算任务。 |
| 8 | Broad Phase Collision | 碰撞粗检测 |  | 通过简单包围结构快速筛除不可能碰撞的对象对。 |
| 9 | Narrow Phase Collision | 碰撞精检测 |  | 对粗检测候选对计算精确接触点、法线和穿透信息的阶段。 |
| 10 | Contact Manifold | 接触流形 |  | 用多个接触点及法线近似表示两个物体的接触关系。 |
| 11 | Impulse-based Solver | 冲量式求解器 |  | 通过约束冲量修正碰撞速度和接触条件的数值方法。 |
| 12 | Constraint Solver | 约束求解器 |  | 迭代求解接触、关节及其他物理运动限制的算法模块。 |
| 13 | Verlet Integration | Verlet 积分 |  | 使用位置及历史状态推进运动方程的数值积分族。 |
| 14 | Semi-implicit Euler | 半隐式欧拉积分 |  | 先更新速度再用新速度更新位置的时间积分方法。 |
| 15 | Time Step | 仿真时间步 |  | 数值模拟中一次状态更新对应的物理时间间隔。 |
| 16 | Substepping | 子时间步 |  | 把一个较大仿真间隔划分为若干较短更新步以提高稳定性的技术。 |
| 17 | Particle System | 粒子系统 |  | 用大量独立或相互作用粒子表示烟雾、火焰或碎屑的视觉模拟框架。 |
| 18 | Particle Emitter | 粒子发射器 |  | 规定粒子生成位置、速率、初始速度和寿命的组件。 |
| 19 | Smoothed Particle Hydrodynamics | 光滑粒子流体动力学 | SPH | 以核函数平滑的粒子邻域近似求解流体连续方程的方法。 |
| 20 | Position Based Dynamics | 基于位置的动力学 | PBD | 直接投影位置约束以实现稳定交互式物理模拟的方法。 |
| 21 | Extended Position Based Dynamics | 扩展位置动力学 | XPBD | 引入柔度等机制改善 PBD 对时间步和迭代次数敏感性的算法。 |
| 22 | Navier–Stokes Equations | 纳维—斯托克斯方程 |  | 描述连续介质流体动量守恒和黏性作用的微分方程。 |
| 23 | Advection | 对流输运 |  | 物理量随流体速度场移动的过程。 |
| 24 | Fluid Grid | 流体网格 |  | 用于离散存储压力、速度或密度等流体场的空间格点结构。 |
| 25 | Smoke Simulation | 烟雾模拟 |  | 通过流体速度、密度和光散射近似生成烟雾动态效果的技术。 |

## 15. 图形 API、命令提交与显存资源

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | OpenGL | 开放图形库 | OpenGL | Khronos 维护的跨平台图形 API，具有状态机式命令接口。 |
| 2 | Vulkan | Vulkan 显式图形 API | Vulkan | 由 Khronos 标准化、强调显式资源和同步控制的图形与计算 API。 |
| 3 | Direct3D | Direct3D 图形 API | D3D | Microsoft DirectX 家族中面向 GPU 图形渲染的接口。 |
| 4 | Metal | Metal 图形与计算 API | Metal | Apple 平台提供的 GPU 图形和计算编程接口。 |
| 5 | Shader Module | 着色器模块 |  | 存储可供图形管线使用的已编译着色器代码的对象。 |
| 6 | Graphics Pipeline State | 图形管线状态 | PSO | 封装着色阶段、顶点输入、光栅化和混合规则等配置的状态对象。 |
| 7 | Descriptor Set | 描述符集合 |  | 在 Vulkan 等 API 中把着色器所需缓冲和图像资源绑定到命令的机制。 |
| 8 | Descriptor Binding | 描述符绑定 |  | 规定着色器资源位于哪个描述符集合和绑定槽位的接口约定。 |
| 9 | Uniform Buffer | 统一参数缓冲 | UBO | 保存多个着色阶段共享读取的较小常量数据的 GPU 缓冲资源。 |
| 10 | Storage Buffer | 存储缓冲 | SSBO | 允许着色器按权限读取或写入较大结构化数据的缓冲资源。 |
| 11 | Push Constant | 推送常量 |  | 在支持图形 API 中向管线快速提供少量可更新常量数据的机制。 |
| 12 | Command Buffer | 命令缓冲 |  | 记录 GPU 绘制、复制和同步命令以待提交的对象。 |
| 13 | Command Queue | 命令队列 |  | 接收待执行 GPU 命令并按相应调度语义推进的队列。 |
| 14 | Graphics Queue | 图形队列 |  | 支持图形相关绘制和可用其他命令的设备执行队列。 |
| 15 | Compute Queue | 计算队列 |  | 用于执行通用 GPU 计算派发的设备队列。 |
| 16 | Transfer Queue | 传输队列 |  | 支持数据复制或资源传输命令的设备队列。 |
| 17 | Synchronization Barrier | 同步屏障 |  | 在 GPU 命令间声明执行顺序或内存可见性依赖的机制。 |
| 18 | Pipeline Barrier | 管线屏障 |  | 在部分图形 API 中规定阶段与访问依赖的同步命令。 |
| 19 | Semaphore | 信号量 |  | 用于设备队列之间或主机与设备之间协调操作完成的同步资源。 |
| 20 | Fence | 完成栅栏 |  | 允许主机等待或查询设备命令提交是否完成的同步对象。 |
| 21 | Swapchain | 交换链 |  | 管理供屏幕显示的多张可交换图像及其呈现流程的资源集合。 |
| 22 | Present Operation | 图像呈现 |  | 把完成渲染的交换链图像提交给显示系统的操作。 |
| 23 | Staging Buffer | 暂存缓冲 |  | 用于在主机可访问内存与设备优化资源之间搬运数据的中间缓冲。 |
| 24 | Image Layout Transition | 图像布局转换 |  | 在显式图形 API 中改变图像的允许访问用途或布局状态的过程。 |
| 25 | GPU Memory Allocation | GPU 显存分配 |  | 为缓冲区或图像资源绑定设备内存的管理操作。 |

## 16. GPU 着色语言、计算着色与高级管线

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Shader | 着色器 |  | 在 GPU 图形或计算管线中执行的可编程函数或程序阶段。 |
| 2 | GLSL | OpenGL 着色语言 | GLSL | 用于 OpenGL 等环境并可编译为相关中间表示的着色语言。 |
| 3 | HLSL | 高级着色语言 | HLSL | 由 Microsoft 发展、常用于 Direct3D 生态的 GPU 着色语言。 |
| 4 | SPIR-V | 标准可移植中间表示 | SPIR-V | Khronos 定义的用于图形与并行计算着色器的中间语言格式。 |
| 5 | Shader Compilation | 着色器编译 |  | 把高级着色源代码转换为中间表示或 GPU 机器代码的过程。 |
| 6 | Shader Reflection | 着色器反射 |  | 查询着色器使用的资源、输入输出变量和布局等元数据的功能。 |
| 7 | Compute Shader | 计算着色器 |  | 用于通用并行任务、以线程组方式执行的可编程 GPU 阶段。 |
| 8 | Workgroup | 工作组 |  | 计算着色器中允许共享组内存并执行组内同步的线程集合。 |
| 9 | Workgroup Size | 工作组尺寸 |  | 决定单个计算工作组在各维度包含多少调用实例的配置。 |
| 10 | Dispatch Call | 计算派发调用 |  | 指定工作组数量并提交计算着色器执行的命令。 |
| 11 | Shared Workgroup Memory | 工作组共享内存 |  | 同一计算工作组内调用实例可共同访问的片上或逻辑共享存储。 |
| 12 | Subgroup | 子组 |  | 硬件可高效执行投票和交换等集体操作的一组 shader 调用实例。 |
| 13 | Wave Intrinsic | 波前内建操作 |  | 在相关 GPU 着色语言中对子组内线程执行集体操作的原语。 |
| 14 | Derivative Instruction | 屏幕导数指令 |  | 估计相邻片段间值变化以支持纹理 LOD 等操作的 GPU 指令。 |
| 15 | Geometry Amplification | 几何扩增 |  | 由一个输入基元产生多个输出基元或细分结果的管线能力。 |
| 16 | Mesh Shader | 网格着色器 |  | 在支持硬件与 API 上以工作组直接生成网格基元的可编程阶段。 |
| 17 | Task Shader | 任务着色器 |  | 在某些网格着色管线中决定后续网格工作负载并传递负载数据的阶段。 |
| 18 | Amplification Shader | 放大着色器 |  | 在部分图形 API 中控制网格着色工作组派发的可编程阶段。 |
| 19 | Ray Generation Shader | 光线生成着色器 |  | 在硬件光线追踪管线中发射初始射线并组织结果的着色阶段。 |
| 20 | Closest-hit Shader | 最近命中着色器 |  | 处理射线与场景最近有效交点结果的可编程阶段。 |
| 21 | Any-hit Shader | 任意命中着色器 |  | 允许检查候选光线交点并决定忽略或接受的着色阶段。 |
| 22 | Miss Shader | 未命中着色器 |  | 在射线没有命中场景几何时提供环境或默认结果的阶段。 |
| 23 | Callable Shader | 可调用着色器 |  | 供光线追踪着色器调用执行特定逻辑的可编程函数阶段。 |
| 24 | Shader Binding Table | 着色器绑定表 | SBT | 将光线追踪着色器组与各类几何命中记录关联的数据结构。 |
| 25 | Specialization Constant | 特化常量 |  | 允许在管线创建或编译特化阶段固定着色器常量的参数机制。 |

## 17. 光线追踪加速结构、遍历与性能

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Acceleration Structure | 求交加速结构 |  | 通过空间或对象层级组织减少光线与所有基元逐一求交的结构。 |
| 2 | Bounding Volume | 包围体 |  | 用简单几何形状包裹复杂物体以支持快速相交排除测试的容器。 |
| 3 | Axis-aligned Bounding Box | 轴对齐包围盒 | AABB | 各边与坐标轴平行的盒状包围体。 |
| 4 | Oriented Bounding Box | 有向包围盒 | OBB | 允许按对象方向旋转、包裹几何的盒状包围体。 |
| 5 | Bounding Volume Hierarchy | 包围体层次结构 | BVH | 以嵌套包围盒树层级组织场景基元以加速射线求交的结构。 |
| 6 | Binary BVH | 二叉 BVH |  | 每个内部节点具有两个子节点的包围体层次结构。 |
| 7 | Wide BVH | 宽分支 BVH |  | 每个内部节点允许多于两个子节点以提高并行遍历效率的结构。 |
| 8 | BVH Traversal | BVH 遍历 |  | 沿包围体树搜索与射线可能相交的叶子基元的过程。 |
| 9 | BVH Construction | BVH 构建 |  | 按空间划分和代价准则组织基元为树形包围结构的算法。 |
| 10 | BVH Refit | BVH 包围盒更新 |  | 在拓扑不变条件下重算变形几何的层级包围体的过程。 |
| 11 | Surface Area Heuristic | 表面积启发式 | SAH | 以包围盒面积和预期遍历、求交成本选择 BVH 划分的准则。 |
| 12 | Spatial Split | 空间分割 |  | 沿空间位置切分节点中的几何区域以改善包围体紧致性的技术。 |
| 13 | Object Split | 对象划分 |  | 把基元分配到不同节点而不必切割原始基元的层次构建方法。 |
| 14 | k-d Tree | k-d 树 |  | 按坐标轴交替设置分割平面递归划分空间的二叉树结构。 |
| 15 | Uniform Grid Acceleration | 均匀网格加速 |  | 将空间划为规则单元并存储相关基元以加速求交的方法。 |
| 16 | Octree | 八叉树 |  | 递归把三维空间分成八个子体积的层次空间索引。 |
| 17 | Top-level Acceleration Structure | 顶层加速结构 | TLAS | 在支持硬件光追的 API 中按实例组织底层几何加速结构的资源。 |
| 18 | Bottom-level Acceleration Structure | 底层加速结构 | BLAS | 在硬件光追 API 中保存单一或多个几何对象求交组织的资源。 |
| 19 | Instance Acceleration | 实例加速 |  | 利用同一几何数据与不同变换实例复用求交加速结构的技术。 |
| 20 | Ray Packet | 射线包 |  | 把方向或来源相近的一组射线共同处理以提高相干性的方式。 |
| 21 | Ray Coherence | 射线相干性 |  | 相邻射线在空间位置、方向或所访问加速节点上相似的性质。 |
| 22 | Stackless Traversal | 无栈树遍历 |  | 利用节点链接或编码状态避免显式遍历栈的求交方法。 |
| 23 | Traversal Cost | 遍历成本 |  | 访问加速结构节点并执行包围测试所耗费的计算开销。 |
| 24 | Intersection Cost | 基元求交成本 |  | 计算射线与三角形或其他几何对象相交所需的运算开销。 |
| 25 | Ray Tracing Performance | 光追性能 |  | 以每秒射线数、有效样本、耗时及图像质量共同评价光线追踪工作负载的性能。 |

## 18. 实时渲染架构、抗锯齿与性能优化

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Deferred Shading | 延迟着色 |  | 先把场景几何属性写入中间缓冲、再在屏幕空间计算部分光照的架构。 |
| 2 | Forward Shading | 前向着色 |  | 在绘制几何片段时直接计算材质与灯光颜色的渲染架构。 |
| 3 | Forward+ Rendering | Forward+ 渲染 |  | 把屏幕分块并为每块构建光源列表的前向着色优化方案。 |
| 4 | Clustered Shading | 簇式着色 |  | 按屏幕位置及深度划分簇并为每簇维护光源集合的着色方法。 |
| 5 | G-buffer | 几何缓冲 | G-buffer | 保存可见片段法线、材质、深度等信息供延迟着色使用的缓冲集合。 |
| 6 | Tiled Lighting | 分块光照 |  | 把屏幕分成小块并为各块筛选相关光源的照明优化技术。 |
| 7 | Light Culling | 光源剔除 |  | 在着色前排除不能影响某个区域或对象的光源的过程。 |
| 8 | Tiled Deferred Rendering | 分块延迟渲染 |  | 结合屏幕 tile 与延迟材质数据计算可见表面光照的架构。 |
| 9 | Temporal Anti-aliasing | 时间抗锯齿 | TAA | 通过抖动采样和历史帧重投影聚合降低空间锯齿的技术。 |
| 10 | Spatial Anti-aliasing | 空间抗锯齿 |  | 仅使用单帧或空间邻域信息降低采样伪影的方法集合。 |
| 11 | Fast Approximate Anti-aliasing | 快速近似抗锯齿 | FXAA | 基于亮度边缘分析执行局部图像平滑的后处理抗锯齿方法。 |
| 12 | Subpixel Morphological Anti-aliasing | 子像素形态学抗锯齿 | SMAA | 结合边缘模式与子像素覆盖估计改善抗锯齿的算法。 |
| 13 | Temporal Upscaling | 时间超分辨率 |  | 利用历史帧和运动信息重建高于内部渲染分辨率的输出画面的方法。 |
| 14 | Spatial Upscaling | 空间升采样 |  | 利用当前帧的空间插值或重建提高图像输出分辨率的方法。 |
| 15 | Dynamic Resolution Scaling | 动态分辨率调整 | DRS | 根据设备负载改变内部渲染分辨率以维持帧时间预算的策略。 |
| 16 | Motion Vector Buffer | 运动向量缓冲 |  | 记录像素或物体跨帧屏幕位移以支持重投影的图像资源。 |
| 17 | History Buffer | 历史帧缓冲 |  | 保存前一帧颜色或中间数据供时间累积复用的资源。 |
| 18 | Ghosting Artifact | 时间拖影伪影 |  | 错误历史重投影或混合使运动物体留下残影的现象。 |
| 19 | Disocclusion | 显露区域 |  | 由于观察角度或物体运动、当前帧中新出现且前帧被遮挡的区域。 |
| 20 | GPU Profiling | GPU 性能剖析 |  | 通过设备计数器和执行时间测量分析图形工作瓶颈的过程。 |
| 21 | Overdraw | 重复像素绘制 |  | 同一像素或采样位置因多层几何被多次着色或覆盖的现象。 |
| 22 | Batching | 绘制批处理 |  | 合并具有相容状态的对象命令以减少 CPU 提交和驱动管理成本的优化。 |
| 23 | Instanced Rendering | 实例化渲染 |  | 一次提交多个共享几何而变换或属性不同的对象实例的技术。 |
| 24 | Level-of-detail Mesh | 网格细节等级 | Mesh LOD | 按屏幕投影大小或距离切换不同复杂度几何的方案。 |
| 25 | Frame Pacing | 帧节奏控制 |  | 控制帧提交与呈现时间间隔以减少画面卡顿的技术。 |

## 19. 神经图形学、可微渲染与新视角合成

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | Neural Graphics | 神经图形学 |  | 结合神经网络与图形学表示、渲染和编辑流程的研究方向。 |
| 2 | Neural Rendering | 神经渲染 |  | 利用可学习场或基元模型合成图像和视角的渲染技术。 |
| 3 | Differentiable Rendering | 可微渲染 |  | 允许渲染结果误差对场景参数计算梯度的算法与系统。 |
| 4 | Inverse Graphics | 逆向图形学 |  | 根据图像观测估计场景几何、材质、光照和相机等潜在因素的任务。 |
| 5 | Inverse Rendering | 逆向渲染 |  | 从目标图像反推可解释该图像的物理或神经场景参数的优化问题。 |
| 6 | Novel View Synthesis | 新视角合成 | NVS | 根据已知视角及场景表示合成未观测相机位置图像的任务。 |
| 7 | Neural Radiance Field | 神经辐射场 | NeRF | 用可学习连续函数表示密度和视角相关辐射并进行体渲染的场景模型。 |
| 8 | Neural Signed Distance Field | 神经有符号距离场 |  | 以神经网络近似几何 SDF 函数的隐式表面表示方法。 |
| 9 | Positional Encoding | 神经位置编码 |  | 把位置或方向输入映射为高维周期特征以表示细节的技术。 |
| 10 | Fourier Feature Mapping | 傅里叶特征映射 |  | 通过正弦余弦频率变换坐标以帮助网络学习高频变化的方法。 |
| 11 | Hash Grid Encoding | 哈希网格编码 |  | 用多尺度哈希表中的可训练特征对空间坐标编码的方法。 |
| 12 | Instant Neural Graphics Primitives | 即时神经图形基元 | Instant-NGP | 利用高效多尺度编码和 GPU 内核加速神经场优化的方案。 |
| 13 | Radiance Field | 辐射场 |  | 以空间位置和方向为自变量表示场景辐射或相关散射属性的函数。 |
| 14 | Volume Density Field | 体密度场 |  | 为空间坐标赋予光学密度、用于体积累积与可见性估计的场。 |
| 15 | 3D Gaussian Splatting | 三维高斯泼溅 | 3DGS | 用可优化三维高斯基元与投影混合高效表示和渲染场景的方法。 |
| 16 | Gaussian Primitive | 高斯基元 |  | 具有三维均值、协方差、不透明度和外观参数的空间基元。 |
| 17 | Gaussian Covariance | 高斯协方差 |  | 描述三维高斯基元尺度与方向的正定对称矩阵。 |
| 18 | Splat Rasterization | 泼溅光栅化 |  | 将空间基元投影到图像平面并累积可见颜色的计算过程。 |
| 19 | Alpha Compositing | Alpha 合成 |  | 按不透明度与指定层级顺序组合多个颜色贡献的过程。 |
| 20 | Photometric Loss | 光度损失 |  | 比较渲染图像与真实观测在颜色或光照上的误差的目标函数。 |
| 21 | Silhouette Loss | 轮廓损失 |  | 利用渲染轮廓与参考分割轮廓差异约束场景形状的损失。 |
| 22 | Neural Texture | 神经纹理 |  | 通过可训练特征纹理及解码网络表示材质或外观细节的技术。 |
| 23 | Neural Material Model | 神经材质模型 |  | 通过学习函数近似复杂表面反射或其他材质光学特性的表示。 |
| 24 | Scene Parameter Optimization | 场景参数优化 |  | 通过渲染误差迭代更新几何、材质、光照或相机参数的过程。 |
| 25 | Neural Reconstruction Artifact | 神经重建伪影 |  | 由视角覆盖不足、训练或几何估计错误造成的场景渲染缺陷。 |

## 20. 格式资源、工具链、评测与生产工程

| # | English term | 中文译名 | Abbr. | 核心定义 |
|---:|---|---|---|---|
| 1 | glTF | GL 传输格式 | glTF | Khronos 标准化的三维场景、材质、动画与资源交换格式。 |
| 2 | USD | 通用场景描述 | USD | 支持分层组合、引用与协作场景组织的三维场景描述系统。 |
| 3 | OBJ File Format | Wavefront OBJ 网格格式 | OBJ | 使用文本存储几何顶点、面和部分属性的经典模型交换格式。 |
| 4 | FBX | FBX 三维资产格式 | FBX | 用于交换三维几何、骨骼和动画等资源的文件格式。 |
| 5 | Material Definition Language | 材质定义语言 | MDL | 描述可组合物理材质外观的 NVIDIA 材质语言。 |
| 6 | Asset Pipeline | 资产处理流水线 |  | 从建模、烘焙、压缩到打包和运行时加载图形资源的工作流程。 |
| 7 | Content Creation Tool | 数字内容制作工具 | DCC | 用于创建三维模型、纹理、动画与特效的专业软件。 |
| 8 | Blender | Blender 三维创作软件 |  | 提供建模、动画、材质、渲染及合成能力的开源 DCC 软件。 |
| 9 | RenderDoc | RenderDoc 图形调试器 |  | 捕获图形帧并检查绘制命令、资源与着色器状态的工具。 |
| 10 | Nsight Graphics | Nsight Graphics 分析器 |  | NVIDIA 提供的图形调试与 GPU 图形性能分析工具。 |
| 11 | GPU Frame Capture | GPU 帧捕获 |  | 记录单帧图形命令、状态与资源供离线调试的过程。 |
| 12 | Shader Profiling | 着色器性能剖析 |  | 测量着色器执行耗时、指令和硬件等待的分析流程。 |
| 13 | Frame-time Budget | 帧时间预算 |  | 为达到目标 FPS 可供单帧渲染管线使用的最大时间。 |
| 14 | CPU–GPU Synchronization | CPU—GPU 同步 |  | 协调主机线程与设备图形命令执行进度的机制。 |
| 15 | Resource Lifetime | 资源生命周期 |  | 图形缓冲、图像和其他对象从创建到最后使用及销毁的有效时间范围。 |
| 16 | Resource Aliasing | 资源内存别名 |  | 不同生命周期不重叠的图形资源复用同一物理内存区域的技术。 |
| 17 | Render Graph | 渲染依赖图 |  | 描述渲染阶段资源读写依赖、调度和生命周期的有向图结构。 |
| 18 | Frame Graph | 帧图 |  | 组织一帧内多次渲染通道及中间资源依赖的工程抽象。 |
| 19 | Transient Resource | 临时渲染资源 |  | 仅在部分帧图阶段存在、可复用底层显存的短期对象。 |
| 20 | GPU Memory Budget | GPU 显存预算 |  | 为纹理、几何、缓冲和中间目标规定的设备内存容量上限。 |
| 21 | Image Quality Metric | 图像质量指标 |  | 量化渲染结果与参考画面差异或视觉感知质量的度量。 |
| 22 | Peak Signal-to-noise Ratio | 峰值信噪比 | PSNR | 根据像素均方误差与最大信号幅度计算的重建质量指标。 |
| 23 | Structural Similarity Index | 结构相似度指标 | SSIM | 利用亮度、对比度和结构局部统计比较图像相似度的指标。 |
| 24 | Learned Perceptual Image Patch Similarity | 学习型感知图像块相似度 | LPIPS | 利用预训练深度特征距离评估图像感知差异的指标。 |
| 25 | Visual Regression Testing | 视觉回归测试 |  | 比较软件变更前后渲染画面或图像质量指标以发现异常的测试。 |

## 16 组专业概念辨析

| 对比概念 | 技术区别与边界 |
|---|---|
| Computer Graphics 与 Computer Vision | 图形学根据几何、材质与光照合成图像；视觉从图像推断几何、类别和运动。两者在逆向渲染和神经重建中相互结合。 |
| Rasterization 与 Ray Tracing | 光栅化由基元投影到屏幕求覆盖；光追从射线与场景求交。两者可混合使用，不能简单断言其中一种总更快。 |
| Object、World、View 与 Clip Space | 局部模型坐标经模型矩阵到世界，经视图矩阵到相机，投影后到齐次裁剪空间，再经过透视除法得到 NDC。 |
| 透视除法与透视校正插值 | 透视除法把齐次坐标除以 w；属性透视校正插值则使用各顶点的逆 w 权重，避免屏幕线性插值失真。 |
| Flat、Gouraud 与 Phong Shading | 平面着色常每面一个法向；Gouraud 在顶点算光照再插值颜色；Phong 在片段插值法向再算光照。 |
| BRDF 与 BSDF | BRDF 仅描述反射方向分布；BSDF 涵盖反射与透射。材质实现须注意相应测度、法向与能量约束。 |
| Base Color 与 Albedo | Base Color 是材质工作流的可编辑参数；反照率有具体的辐射能量意义，两者在金属材质或不同着色模型中不必相同。 |
| Radiance 与 Irradiance | 辐亮度按投影面积与立体角定义、具方向性；辐照度对入射半球积分后按表面积度量。它们单位不同。 |
| Direct 与 Indirect Lighting | 直接光来自光源到表面的首段路径；间接光经历反弹或透射。AO 只近似局部遮蔽，不等于物理全局光照。 |
| Path Tracing 与普通 Ray Casting | 简单射线投射通常求第一可见交点；路径追踪通过随机反弹光路估计包含间接照明的渲染积分。 |
| MSAA、FXAA 与 TAA | MSAA 增加几何覆盖采样；FXAA 用单帧后处理平滑边缘；TAA 复用历史采样但可能产生拖影。 |
| Shadow Mapping 与 Ray-traced Shadows | 阴影贴图从光源视角比较有限分辨率深度；射线阴影以几何求交判断遮挡，精度和成本取决于实现。 |
| BVH 与 Uniform Grid | BVH 按嵌套包围体组织几何；均匀网格按规则空间单元索引基元。性能取决于场景空间分布和射线类型。 |
| OpenGL 与 Vulkan | OpenGL 采用较多隐式状态管理；Vulkan 暴露资源、命令与同步细节以便显式控制，编码复杂度与性能不可一概而论。 |
| Linear RGB 与 sRGB | 光照合成和大部分物理颜色运算应在线性光数值上进行；sRGB 通常采用非线性编码，混合前需要明确转换。 |
| NeRF 与 3D Gaussian Splatting | NeRF 以连续神经场及体积积分合成视角；3DGS 用显式三维高斯与投影合成。两者均需针对视角质量、内存和速度实测。 |

## 中等难度面试问答

### 面试题 1：为什么 60 FPS 的真实帧时间预算不能把全部 16.67ms 都交给像素着色器？

**参考答案：**CPU 更新、命令提交、顶点处理、几何、后处理及同步也占用帧时间。应先画出完整帧图并以 GPU 时间线定位耗时阶段。

### 面试题 2：模型到屏幕的 MVP 变换经过哪些坐标空间？

**参考答案：**通常依次由对象空间经 Model 到世界、View 到相机、Projection 到齐次裁剪坐标；裁剪后除以 w 得到 NDC，再映射到视口。

### 面试题 3：为什么三角形纹理坐标不能简单按屏幕重心权重线性插值？

**参考答案：**透视投影不是仿射映射，必须用各顶点属性除以 w 的加权结果再除以逆 w 权重和，才能恢复正确纹理透视关系。

### 面试题 4：为什么在线性 RGB 与 sRGB 编码值上进行相同 Alpha 混合可能输出不同颜色？

**参考答案：**sRGB 对线性光值执行非线性编码。物理混色应先转回线性光域，再混合、再执行显示编码，否则会产生亮度偏差。

### 面试题 5：BRDF 为什么需要满足非负性、能量守恒与可能的互易性？

**参考答案：**这些约束避免负散射、无源材料输出超过入射能量，并在常见非磁性线性介质条件下满足光路互易物理规律。

### 面试题 6：为什么路径追踪只有 1 spp 时容易产生明显噪声？

**参考答案：**蒙特卡洛估计方差随样本量降低而减小，少量样本难覆盖高贡献光路；重要性采样和 MIS 可有效降低方差。

### 面试题 7：为什么 AO 不能代替全局光照？

**参考答案：**AO 主要衡量局部几何遮挡，不显式模拟完整入射辐射和不同表面之间的能量交换，无法正确重现颜色渗透等效果。

### 面试题 8：在动态场景中 BVH 应完全重建还是 Refit？

**参考答案：**若仅顶点或实例变换小幅变化，Refit 可便宜更新包围盒；若拓扑或空间重叠严重恶化，重建可能获得更优遍历成本。

### 面试题 9：Vulkan 的管线屏障与信号量主要区别是什么？

**参考答案：**管线屏障描述设备操作间的阶段和内存依赖；信号量常用于队列间或提交间同步，二者的适用范围取决于 Vulkan 版本和同步 API。

### 面试题 10：TAA 的历史重投影为何容易产生拖影？

**参考答案：**运动向量、遮挡显露和历史有效性检测不准时会把过去帧的错误颜色累积到当前位置，需限制或重置历史。

### 面试题 11：为什么延迟渲染并不总适合透明对象？

**参考答案：**G-buffer 通常每像素只保留一个可见表面材质状态，难以正确处理多层透明与顺序混合，常结合前向透明通道。

### 面试题 12：NeRF 与 3DGS 在数据结构和渲染算法上如何区分？

**参考答案：**NeRF 多查询连续密度与外观并进行沿射线积分；3DGS 优化显式高斯基元并投影混合。比较需固定输入视图和画质目标。

## 中等难度考试题与解析

### 考试题 1：目标帧率为 60 FPS，单帧时间预算是多少毫秒？

**解析：**1000/60≈16.67 ms。若系统有呈现与同步开销，渲染阶段可用时间更少。

### 考试题 2：一张 RGBA8、1024×1024 纹理在不含 mipmap 与压缩时需要多少 MiB？

**解析：**1024×1024×4 字节=4,194,304 字节=4 MiB。

### 考试题 3：一张 512×512 RGBA8 纹理保留完整 mipmap 链，理想总容量大约多少 MiB？

**解析：**基础层是 1 MiB，所有层近似乘以 4/3，因此约为 1.333 MiB，忽略额外对齐。

### 考试题 4：向量 n=(0,0,1)、光线方向 l=(0,0,1)，Lambert 余弦因子是多少？

**解析：**max(0,n·l)=1；需假设两向量均已单位化。

### 考试题 5：两向量 a=(1,0,0)、b=(0,1,0) 的点积与夹角是多少？

**解析：**a·b=0，且两者单位化，所以夹角为 90°。

### 考试题 6：深度测试中两个几乎重合面出现闪烁，属于什么典型现象？如何减轻？

**解析：**Z-fighting。可改善 near/far 配置、采用 Reversed-Z、适当的深度偏移或避免共面几何。

### 考试题 7：纹理长宽各从 1024 降至 256，未压缩每像素大小不变时基础层数据量缩小多少倍？

**解析：**每轴缩小 4 倍，面积缩小 4×4=16 倍。

### 考试题 8：简单蒙特卡洛估计，f(x)=2、采样 pdf(x)=0.5，则该样本对积分估计贡献是多少？

**解析：**单样本贡献 f(x)/p(x)=2/0.5=4，需保证所选测度和支持集适用。

### 考试题 9：某 2560×1440 渲染目标采用 RGBA16F，每个像素 8 字节，未计 MSAA 时多少 MiB？

**解析：**2560×1440×8=29,491,200 字节≈28.125 MiB。

### 考试题 10：一帧的 Geometry、Lighting、Postprocessing 各耗时 4、6、3 ms，完全串行总时间是多少？

**解析：**4+6+3=13 ms，理论渲染阶段吞吐约 76.9 FPS；还需考虑 CPU、同步和呈现。

### 考试题 11：采样 4 spp 相比 1 spp，独立同分布蒙特卡洛估计的标准差理想缩小到多少？

**解析：**在方差有限且样本独立时，标准差按 1/√N 缩放，因此缩小到 1/2；不是误差降至 1/4。

### 考试题 12：一个网格 10,000 个三角形，每三角形独立存 3 个 32 位索引，总索引数据多少字节？

**解析：**10,000×3×4=120,000 字节，约 117.19 KiB。

## 经典教材、API 规范与原始论文

以下资料用于确认概念背景和研究来源，不表示作者参与或认可本项目所有具体定义。

1. [Pharr, Jakob & Humphreys, Physically Based Rendering (4th edition)](https://pbr-book.org/4ed/contents)
2. [Scratchapixel — Computer Graphics and Ray Tracing](https://www.scratchapixel.com/)
3. [Khronos Vulkan Specification](https://docs.vulkan.org/spec/latest/)
4. [Khronos OpenGL Reference Documentation](https://www.khronos.org/opengl/wiki/)
5. [Khronos glTF 2.0 Specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
6. [Microsoft Direct3D 12 Graphics Documentation](https://learn.microsoft.com/en-us/windows/win32/direct3d12/direct3d-12-graphics)
7. [Apple Metal Documentation](https://developer.apple.com/metal/)
8. [OpenUSD Documentation](https://openusd.org/release/index.html)
9. [NVIDIA OptiX Programming Guide](https://raytracing-docs.nvidia.com/optix8/guide/index.html)
10. [RenderDoc Graphics Debugger](https://renderdoc.org/)
11. [Blender Manual](https://docs.blender.org/manual/en/latest/)
12. [SIGGRAPH Course: Real-Time Rendering Resources](https://www.realtimerendering.com/)
13. [Mildenhall et al. (2020), NeRF: Representing Scenes as Neural Radiance Fields](https://arxiv.org/abs/2003.08934)
14. [Kerbl et al. (2023), 3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)
15. [Müller et al. (2022), Instant Neural Graphics Primitives](https://nvlabs.github.io/instant-ngp/)

## 出版与维护说明

- 原始数据：`data/computer-graphics/chapters/*.tsv`，每行 `English|中文|abbr|definition`。
- 生成文件：`data/computer-graphics.tsv`、`glossaries/computer-graphics.md`、`pdf/computer-graphics.pdf`，及相同内容的 `docs/` 镜像。
- 可复现构建：`node scripts/render_computer_graphics.mjs`，只读校验：`node scripts/render_computer_graphics.mjs --check`。
- **本册是独立出版的简明术语表，尚未接入网站正式搜索索引，亦非 500 篇专家审稿的深度 Wiki。**
