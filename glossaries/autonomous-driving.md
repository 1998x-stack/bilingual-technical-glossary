# 自动驾驶系统 · Autonomous Driving

> TERM / ATLAS · Autonomous Driving Bilingual Technical Glossary | 自动驾驶专有名词中英文对照表

**500 条原创中英文术语 · 20 个专业章节 · 2026-11-27**

从 SAE J3016_202609 驾驶自动化定义、ODD 与动态驾驶任务出发，覆盖线控底盘、相机/雷达/激光雷达、点云和 BEV 感知、占据预测、融合与定位、高精地图、主体行为预测、路口交互、轨迹规划、车辆控制、碰撞风险、端到端驾驶与世界模型、V2X、仿真标准、开放数据集、功能安全/SOTIF 和车队运营。

**技术边界与安全声明：**这是教育性质的术语手册，不构成车辆安全验证或上路运行指导。SAE 等级描述驾驶自动化功能的职责分配，不是按宣传名称对整车统一认证。实现系统时应根据当前标准版本和所在司法辖区法规进行专业安全评估。

**审稿状态：**已程序校验章节、条目字段和英文主术语去重；尚未完成独立安全工程专家逐条审稿、真实道路测试及 PDF 全面视觉与无障碍验收。

## 章节目录

- 01. 自动驾驶体系、SAE 等级与运行设计域（25 条）
- 02. 整车电子电气、车辆接口与执行机构（25 条）
- 03. 环境传感器、采集链与时间空间标定（25 条）
- 04. 视觉道路感知、车道线与可行驶区域（25 条）
- 05. 激光雷达、毫米波雷达与三维点云处理（25 条）
- 06. 三维目标检测、运动目标跟踪与场景实体（25 条）
- 07. 高精定位、惯导融合与地图匹配（25 条）
- 08. 高精地图、道路拓扑与车道语义（25 条）
- 09. 多传感器融合、占据网络与世界表示（25 条）
- 10. 交通参与者运动预测与多智能体交互（25 条）
- 11. 行为决策、交通规则与路口博弈（25 条）
- 12. 轨迹生成、速度规划与约束优化（25 条）
- 13. 车辆动力学、横纵向控制与执行跟踪（25 条）
- 14. 交通安全约束、风险与应急策略（25 条）
- 15. 端到端自动驾驶、模仿学习与世界模型（25 条）
- 16. 车路协同、V2X 与智能交通基础设施（25 条）
- 17. 自动驾驶仿真、场景标准与数字孪生（25 条）
- 18. 驾驶数据集、基准指标与系统性误差分析（25 条）
- 19. 功能安全、SOTIF、网络安全与验证论证（25 条）
- 20. 部署运行、远程协助与数据闭环工程（25 条）

---

## 01. 自动驾驶体系、SAE 等级与运行设计域

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Autonomous Driving | 自动驾驶 |  | 车辆在指定条件下利用感知、决策与控制执行部分或全部驾驶任务的技术领域。 |
| 2 | Automated Driving System | 自动驾驶系统 | ADS | 能够在其设计运行条件下持续执行完整动态驾驶任务的软硬件系统。 |
| 3 | Advanced Driver Assistance System | 高级驾驶辅助系统 | ADAS | 辅助驾驶员完成部分转向或速度控制等任务、仍依赖规定人工监督的系统。 |
| 4 | SAE J3016 Taxonomy | SAE 驾驶自动化分级标准 | J3016 | 用动态驾驶任务、监督与后备责任区分零至五级驾驶自动化的术语体系。 |
| 5 | Level 0 Driving Automation | 零级驾驶自动化 | L0 | 车辆未持续执行转向或纵向控制的驾驶自动化等级。 |
| 6 | Level 1 Driving Automation | 一级驾驶自动化 | L1 | 系统持续辅助转向或纵向速度控制之一且驾驶员持续监督的等级。 |
| 7 | Level 2 Driving Automation | 二级驾驶自动化 | L2 | 系统持续协同控制转向和纵向速度、驾驶员持续监督的等级。 |
| 8 | Level 3 Driving Automation | 三级驾驶自动化 | L3 | 系统在定义条件下执行动态驾驶任务、必要时要求后备用户接管的等级。 |
| 9 | Level 4 Driving Automation | 四级驾驶自动化 | L4 | 系统在定义运行条件下可自行执行驾驶任务及相关后备响应的等级。 |
| 10 | Level 5 Driving Automation | 五级驾驶自动化 | L5 | 在可由人驾驶的全部道路条件下无需驾驶员执行驾驶任务的等级。 |
| 11 | Operational Design Domain | 运行设计域 | ODD | 规定自动驾驶功能允许运行的道路、地理、环境、速度与时间等条件集合。 |
| 12 | ODD Boundary | 运行设计域边界 |  | 区分系统支持与不支持运行条件的约束边界。 |
| 13 | Operational Design Condition | 运行设计条件 |  | 运行设计域中影响系统允许启用的具体道路、天气或交通条件。 |
| 14 | Dynamic Driving Task | 动态驾驶任务 | DDT | 驾驶所需的持续横纵向运动控制及目标事件感知响应等实时操作集合。 |
| 15 | DDT Fallback | 动态驾驶任务后备响应 |  | 在系统无法继续完成 DDT 或离开 ODD 时执行的规定响应。 |
| 16 | Fallback-ready User | 可执行后备响应的用户 |  | 在特定驾驶自动化级别下预期可响应系统接管请求的人员。 |
| 17 | Minimal Risk Condition | 最小风险状态 | MRC | 经后备操作使车辆及其他道路参与者风险尽可能降低的稳定状态。 |
| 18 | Minimal Risk Maneuver | 最小风险机动 | MRM | 系统为达到最小风险状态而执行的受控驾驶操作。 |
| 19 | Driver Monitoring System | 驾驶员监测系统 | DMS | 根据摄像头或其他测量分析驾驶员注意力、状态或接管准备度的系统。 |
| 20 | Driver Engagement | 驾驶员参与程度 |  | 驾驶员在监督与执行驾驶任务中投入注意力和控制的状态。 |
| 21 | Takeover Request | 接管请求 | TOR | 自动化功能向可用的人类驾驶者发出恢复驾驶控制的提示。 |
| 22 | Transition Demand | 控制权转换要求 |  | 系统要求后备用户在规定条件下接管动态驾驶任务的通知。 |
| 23 | Automation Disengagement | 自动化退出 |  | 驾驶自动化功能停止持续承担规定驾驶控制职责的事件。 |
| 24 | Human–Machine Interface | 人机界面 | HMI | 向驾驶员或乘员呈现系统状态、警告和控制输入的交互接口。 |
| 25 | Fallback Strategy | 后备策略 |  | 在故障、能力限制或域退出时保障车辆安全退化的系统计划。 |

## 02. 整车电子电气、车辆接口与执行机构

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Vehicle Platform | 车辆平台 |  | 集成车身、底盘、动力、制动、转向及电子电气系统的整车基础。 |
| 2 | Drive-by-wire | 线控驾驶 |  | 通过电子控制信号而非直接机械连接执行驱动、制动或转向的架构。 |
| 3 | Steer-by-wire | 线控转向 |  | 将转向命令转换为转向执行机构动作的电子控制系统。 |
| 4 | Brake-by-wire | 线控制动 |  | 通过电子指令协调制动压力或制动力的执行系统。 |
| 5 | Throttle-by-wire | 电子节气门控制 |  | 由电子控制器根据驾驶需求调节发动机节气门开度的技术。 |
| 6 | Electronic Control Unit | 电子控制单元 | ECU | 负责执行特定车辆功能的嵌入式计算控制节点。 |
| 7 | Domain Controller | 域控制器 |  | 把相关车辆功能的计算和接口集中到同一电子控制平台的架构。 |
| 8 | Central Vehicle Computer | 中央车辆计算机 |  | 集中承担多项车载计算功能的高性能处理平台。 |
| 9 | Vehicle Control Unit | 整车控制单元 | VCU | 协调动力系统与整车模式、安全及执行指令的控制器。 |
| 10 | Electronic Stability Control | 车身电子稳定控制 | ESC | 通过车轮制动等干预帮助车辆维持期望稳定状态的系统。 |
| 11 | Anti-lock Braking System | 防抱死制动系统 | ABS | 通过调节制动压力减少车轮制动时锁死风险的系统。 |
| 12 | Electric Power Steering | 电动助力转向 | EPS | 利用电机提供转向助力或执行转向控制的机构。 |
| 13 | Actuator Command | 执行器命令 |  | 传递给转向、驱动或制动控制器的目标控制量。 |
| 14 | Actuator Feedback | 执行器反馈 |  | 由执行器报告的实际位置、速度、力矩或工作状态数据。 |
| 15 | Controller Area Network | 控制器局域网络 | CAN | 广泛用于车辆控制节点间通信的串行总线协议。 |
| 16 | CAN FD | 灵活数据速率 CAN | CAN FD | 支持更大数据负载与较高速率数据段的 CAN 扩展协议。 |
| 17 | Automotive Ethernet | 车载以太网 |  | 支持车载高带宽传感与计算通信的以太网技术集合。 |
| 18 | Time-sensitive Networking | 时间敏感网络 | TSN | 为以太网提供时间同步、确定性时延和流量调度能力的标准族。 |
| 19 | Automotive Middleware | 车载软件中间件 |  | 为车内功能提供通信、发现、数据序列化及生命周期管理的软件层。 |
| 20 | AUTOSAR | 汽车开放系统架构 | AUTOSAR | 定义汽车软件组件、接口及运行平台的行业协作标准体系。 |
| 21 | Service-oriented Architecture | 面向服务的车载架构 | SOA | 通过可发现的服务接口组织车载功能和数据交换的设计方式。 |
| 22 | Vehicle State Interface | 车辆状态接口 |  | 向自动驾驶软件提供车速、档位、转向角等车辆状态的数据契约。 |
| 23 | Control Command Gateway | 控制命令网关 |  | 将自动驾驶控制输出转化为具体底盘消息并执行授权检查的组件。 |
| 24 | Vehicle Health Monitor | 车辆健康监控 |  | 监测关键执行器、供电和通信状态并报告异常的机制。 |
| 25 | Redundant Actuation | 冗余执行系统 |  | 提供额外制动、转向或控制通路以应对单点故障的设计。 |

## 03. 环境传感器、采集链与时间空间标定

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Automotive Sensor Suite | 车载传感器组 |  | 由摄像头、激光雷达、雷达、定位和惯性设备组成的车辆感知配置。 |
| 2 | Surround-view Camera | 环视摄像头 |  | 安装于车辆不同方向以覆盖周边视野的摄像设备。 |
| 3 | Front-facing Camera | 前视摄像头 |  | 主要观测车辆行进方向道路、车道与交通参与者的成像设备。 |
| 4 | Fisheye Camera | 鱼眼摄像头 |  | 利用超广角镜头获取近场大视角图像的设备。 |
| 5 | Camera Intrinsic Calibration | 相机内参标定 |  | 估计焦距、主点和镜头畸变等相机内部投影参数的过程。 |
| 6 | Camera Extrinsic Calibration | 相机外参标定 |  | 确定相机与车体或其他传感器间相对位置姿态的过程。 |
| 7 | LiDAR | 激光雷达 | LiDAR | 利用激光测距获得场景三维距离点的主动传感器。 |
| 8 | Spinning LiDAR | 旋转式激光雷达 |  | 通过扫描结构改变激光测距方向以覆盖一定空间范围的设备。 |
| 9 | Solid-state LiDAR | 固态激光雷达 |  | 不依赖传统整体机械旋转扫描的激光测距器件类别。 |
| 10 | Automotive Radar | 车载雷达 |  | 利用无线电反射测量目标距离、速度及部分方位信息的传感器。 |
| 11 | Millimeter-wave Radar | 毫米波雷达 |  | 工作于毫米波频段、常用于车载目标测距测速的雷达设备。 |
| 12 | Frequency-modulated Continuous-wave Radar | 调频连续波雷达 | FMCW | 通过连续发射频率变化信号并分析回波差频进行测距测速的雷达方案。 |
| 13 | Imaging Radar | 成像雷达 |  | 提供较丰富角分辨率或空间结构观测的高分辨率雷达系统。 |
| 14 | Ultrasonic Sensor | 超声波传感器 |  | 利用声波往返传播估计近距离目标距离的设备。 |
| 15 | Global Navigation Satellite System | 全球卫星导航系统 | GNSS | 通过多个导航卫星信号求解接收机位置和时间的系统。 |
| 16 | Inertial Measurement Unit | 惯性测量单元 | IMU | 提供角速度与比力等惯性测量的传感组件。 |
| 17 | Wheel Speed Sensor | 轮速传感器 |  | 测量单个车轮旋转速度以支持运动估计或稳定控制的设备。 |
| 18 | Sensor Timestamp | 传感器时间戳 |  | 记录测量采集时间或其他规定时间基准的元数据。 |
| 19 | Hardware Time Synchronization | 硬件时间同步 |  | 通过硬件时钟、触发线或同步协议协调多传感器采样时间的方法。 |
| 20 | Precision Time Protocol | 精确时间协议 | PTP | 为网络设备时钟提供高精度同步的通信协议族。 |
| 21 | Synchronization Offset | 同步时间偏移 |  | 两个传感器或系统时钟之间的估计时间差。 |
| 22 | Sensor Frame | 传感器坐标系 |  | 固定于某一感知设备、用于表达测量方向和位置的参考系。 |
| 23 | Ego-vehicle Frame | 自车坐标系 |  | 固定在车辆特定参考点的坐标系，用于表达车体附近的运动与目标。 |
| 24 | Hand–Eye Calibration | 手眼形式外参标定 |  | 通过多次相对运动观测求解两个固定坐标系之间变换的标定问题。 |
| 25 | Sensor Data Pipeline | 传感数据处理流水线 |  | 包含采集、解码、时间校准、质量检查与分发的连续处理链。 |

## 04. 视觉道路感知、车道线与可行驶区域

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Road Scene Understanding | 道路场景理解 |  | 根据视觉或融合观测解释道路结构、交通设施及参与者关系的任务。 |
| 2 | Lane Detection | 车道线检测 |  | 在图像或空间表示中识别车道边界标记及其几何位置的任务。 |
| 3 | Lane Marking | 车道标线 |  | 绘制在路面的线条、箭头等引导交通的物理标记。 |
| 4 | Lane Centerline | 车道中心线 |  | 用于描述车道行驶方向和局部几何的参考曲线。 |
| 5 | Lane Boundary | 车道边界 |  | 定义一个车道允许行驶区域左右界限的几何曲线。 |
| 6 | Drivable Area Segmentation | 可行驶区域分割 |  | 按像素或空间区域预测车辆可能合法及物理可通行范围的任务。 |
| 7 | Road Surface Segmentation | 路面分割 |  | 在图像中识别与道路表面对应的语义区域的任务。 |
| 8 | Semantic Segmentation | 语义分割 |  | 为图像每个像素分配道路、人行道、车辆等语义类别的预测任务。 |
| 9 | Instance Segmentation | 实例分割 |  | 区分同类不同车辆或行人个体并生成像素掩码的视觉任务。 |
| 10 | Panoptic Segmentation | 全景分割 |  | 为所有像素赋语义类别并为可数目标区分实例身份的任务。 |
| 11 | Traffic Light Recognition | 交通信号灯识别 |  | 检测交通信号灯并判断颜色、方向和控制含义的过程。 |
| 12 | Traffic Sign Recognition | 交通标志识别 |  | 定位并分类限速、停车和其他道路交通标志的任务。 |
| 13 | Traffic Sign Localization | 交通标志空间定位 |  | 确定交通标志在车辆相机或地图坐标系中的位置的过程。 |
| 14 | Stop Line Detection | 停止线检测 |  | 识别路面停止线及其相对自车空间位置的任务。 |
| 15 | Crosswalk Detection | 人行横道检测 |  | 识别道路上的人行横道区域或标线几何的过程。 |
| 16 | Curb Detection | 路缘检测 |  | 从图像、深度或点云中确定路沿空间位置的任务。 |
| 17 | Free-space Estimation | 自由空间估计 |  | 估计车体附近无明显障碍、可用于候选运动的空间区域。 |
| 18 | Vanishing Point | 消失点 |  | 空间平行线经透视投影在图像中趋于汇聚的点。 |
| 19 | Inverse Perspective Mapping | 逆透视映射 | IPM | 在地面平面假设下把相机图像转换为俯视几何表示的方法。 |
| 20 | Bird's-eye-view Transformation | 鸟瞰变换 | BEV | 把多视角或三维观测映射至车辆周围地面坐标平面的表示过程。 |
| 21 | Lane Topology Estimation | 车道拓扑估计 |  | 推断不同车道段连接、分岔与合流关系的任务。 |
| 22 | Road Edge Detection | 道路边缘检测 |  | 识别路面可行驶区域外轮廓或边界位置的任务。 |
| 23 | Road Hazard Detection | 道路危险物检测 |  | 识别落物、坑洞或异常可撞击对象等路面危险的任务。 |
| 24 | Occlusion Reasoning | 遮挡推理 |  | 基于可见几何及场景关系推断被遮挡区域潜在物体或空间结构的方法。 |
| 25 | Visibility Range Estimation | 可视距离估计 |  | 判断当前环境与传感器条件下能可靠观测的前方距离范围的任务。 |

## 05. 激光雷达、毫米波雷达与三维点云处理

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Point Cloud | 点云 |  | 由空间三维采样点及可选反射率、时间和语义属性组成的数据集合。 |
| 2 | Point Cloud Preprocessing | 点云预处理 |  | 对原始测距点执行时间校正、过滤、降采样和坐标变换的过程。 |
| 3 | Motion Distortion | 运动畸变 |  | 传感器在一次扫描期间运动使各采样点不对应同一瞬时姿态的现象。 |
| 4 | LiDAR Deskewing | 激光点云去运动畸变 |  | 利用扫描时序和车辆运动估计校正不同点采集时的姿态差异。 |
| 5 | Ground Point Removal | 地面点去除 |  | 识别并分离点云中属于路面或地形的测量点的处理。 |
| 6 | Ground Plane Estimation | 地面平面估计 |  | 根据点云局部几何拟合道路或近似水平接触平面的任务。 |
| 7 | Voxel Downsampling | 体素降采样 |  | 将空间分为体素并用代表点减少点云规模的方法。 |
| 8 | Radius Outlier Removal | 半径离群点滤除 |  | 根据给定距离内邻点数量移除孤立点的点云过滤方法。 |
| 9 | Statistical Outlier Removal | 统计离群点滤除 |  | 通过邻域距离分布识别可能异常点的点云清洗方法。 |
| 10 | Point Cloud Clustering | 点云聚类 |  | 依据空间距离、密度或特征把测量点分成候选目标集合的过程。 |
| 11 | Euclidean Cluster Extraction | 欧氏距离聚类 |  | 根据点间欧氏邻接关系提取连通点簇的算法。 |
| 12 | Point Cloud Registration | 点云配准 |  | 估计两个点云之间旋转与平移使其空间结构对齐的任务。 |
| 13 | Iterative Closest Point | 迭代最近点 | ICP | 交替建立对应点并估计刚体变换的点集配准算法。 |
| 14 | Normal Distributions Transform | 正态分布变换 | NDT | 将参考点云表示为局部高斯栅格以优化扫描对齐的算法。 |
| 15 | LiDAR Reflectivity | 激光反射强度 |  | 由物体材质、距离及传感器等因素共同决定的测距回波强度属性。 |
| 16 | Range Image | 距离图 |  | 按扫描角度索引组织每条射线测得距离的二维图像表示。 |
| 17 | Radar Range | 雷达距离 |  | 由雷达回波传播时延或等效测量过程得到的目标径向距离。 |
| 18 | Radial Velocity | 径向速度 |  | 目标相对雷达沿视线方向的速度分量。 |
| 19 | Doppler Shift | 多普勒频移 |  | 由物体与传感器相对径向运动导致接收信号频率偏移的现象。 |
| 20 | Range–Doppler Map | 距离多普勒图 |  | 雷达处理链按距离和径向速度维度组织回波能量的表示。 |
| 21 | Radar Cross Section | 雷达散射截面 | RCS | 描述目标在特定条件下对雷达信号散射强度的等效面积量。 |
| 22 | Radar Detection | 雷达目标检测 |  | 从回波噪声和杂波中判断候选目标是否存在的信号处理过程。 |
| 23 | Constant False Alarm Rate | 恒虚警率检测 | CFAR | 按周边背景估计调整检测阈值以控制虚警水平的方法。 |
| 24 | Radar Ghost Target | 雷达虚假目标 |  | 由多径反射或处理歧义等造成的不存在目标的测量假象。 |
| 25 | Radar–LiDAR Fusion | 雷达激光融合 |  | 结合雷达速度优势与激光空间几何信息估计目标状态的技术。 |

## 06. 三维目标检测、运动目标跟踪与场景实体

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | 3D Object Detection | 三维目标检测 |  | 预测车辆、行人或其他目标的三维位置、尺寸、朝向及类别的任务。 |
| 2 | 3D Bounding Box | 三维边界框 |  | 用中心、尺寸和朝向描述物体近似空间范围的标注。 |
| 3 | Oriented Bounding Box | 有向包围盒 | OBB | 允许相对参考坐标轴旋转的三维目标包围框。 |
| 4 | Axis-aligned Bounding Box | 轴对齐包围盒 | AABB | 所有边保持与坐标轴平行的三维空间矩形盒。 |
| 5 | Multi-object Tracking | 多目标跟踪 | MOT | 在连续帧中估计多个目标状态并维护跨时刻身份的任务。 |
| 6 | Tracking-by-detection | 先检测后跟踪 |  | 以逐帧检测目标为输入、通过时间关联生成目标轨迹的方法。 |
| 7 | Track Association | 轨迹关联 |  | 判断新的检测观测应该更新哪个已有目标轨迹的过程。 |
| 8 | Kalman Tracking | 卡尔曼目标跟踪 |  | 利用状态预测、测量残差与协方差更新目标轨迹的技术。 |
| 9 | Joint Probabilistic Data Association | 联合概率数据关联 | JPDA | 在关联不确定时按多种候选测量归属概率更新目标状态的方法。 |
| 10 | Multiple Hypothesis Tracking | 多假设跟踪 | MHT | 维护并延迟决定不同目标测量关联假设的多目标跟踪方法。 |
| 11 | Appearance Embedding | 外观嵌入 |  | 将目标图像区域编码为向量以辅助跨帧身份匹配的表示。 |
| 12 | Track ID | 轨迹身份标识 |  | 对同一物理对象跨时间的观测保持一致的编号。 |
| 13 | Track Fragmentation | 轨迹碎裂 |  | 同一真实物体被拆成多个短轨迹段的跟踪错误。 |
| 14 | Identity Switch | 跟踪身份切换 | IDSW | 对同一真实对象错误分配新身份或与其他目标交换身份的事件。 |
| 15 | Track Confidence | 轨迹置信度 |  | 表示目标轨迹当前存在概率、观测质量或模型可靠性的评分。 |
| 16 | Occlusion Handling | 目标遮挡处理 |  | 目标短时被其他物体挡住时维持轨迹预测和身份的机制。 |
| 17 | Object Existence Probability | 目标存在概率 |  | 估计一个检测或轨迹确实对应真实物理对象的概率。 |
| 18 | Object Velocity Estimation | 目标速度估计 |  | 结合时间序列观测推断其他道路参与者速度的任务。 |
| 19 | Object Acceleration Estimation | 目标加速度估计 |  | 根据运动状态及多帧观测推断目标速度变化率的过程。 |
| 20 | Static Object Classification | 静态目标识别 |  | 区分固定路边设施和可移动交通参与者的目标状态识别任务。 |
| 21 | Vulnerable Road User | 弱势道路使用者 | VRU | 包括行人和骑行者等在碰撞中较缺乏物理防护的交通参与者类别。 |
| 22 | Pedestrian Detection | 行人检测 |  | 在道路场景中定位并识别人类行人的视觉或融合感知任务。 |
| 23 | Cyclist Detection | 骑行者检测 |  | 识别骑自行车或其他二轮非机动车道路参与者的目标检测任务。 |
| 24 | Occupancy-aware Detection | 占据感知检测 |  | 结合周围空间占据表征辅助目标定位及可见性判断的感知方法。 |
| 25 | Scene Entity Graph | 场景实体关系图 |  | 以检测对象为节点、空间与交互关系为边组织交通场景状态的图表示。 |

## 07. 高精定位、惯导融合与地图匹配

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Vehicle Localization | 车辆定位 |  | 根据感知、地图和运动测量估计自车在参考坐标系中位姿的任务。 |
| 2 | Absolute Localization | 绝对定位 |  | 将车辆位姿锚定到全球或已知地图坐标框架的状态估计。 |
| 3 | Relative Localization | 相对定位 |  | 估计车辆相对过去位置、局部地图或其他主体的运动位姿。 |
| 4 | GNSS Positioning | 卫星导航定位 |  | 利用多颗导航卫星观测计算接收器位置的技术。 |
| 5 | Real-time Kinematic Positioning | 实时动态载波差分定位 | RTK | 通过基准站修正和载波相位提升卫星定位精度的方法。 |
| 6 | Precise Point Positioning | 精密单点定位 | PPP | 利用精密卫星轨道与钟差等数据改善单站卫星定位的技术。 |
| 7 | Inertial Navigation System | 惯性导航系统 | INS | 通过积分惯性传感器测量估计姿态、速度和位置的系统。 |
| 8 | GNSS–INS Fusion | 卫星惯导融合 |  | 将 GNSS 位置或速度测量与惯性传播模型联合估计车辆状态的方法。 |
| 9 | Wheel Odometry | 车轮里程计 |  | 根据轮速和运动学模型推算车辆相对位移的估计方法。 |
| 10 | Dead Reckoning | 航位推算 |  | 从已知初始状态积分速度、航向或惯性信息计算后续位置的方法。 |
| 11 | Map Matching | 地图匹配 |  | 把估计位置和运动轨迹对应到道路或车道地图结构的技术。 |
| 12 | Lane-level Localization | 车道级定位 |  | 估计自车处于哪条车道及其在车道内的相对位置的任务。 |
| 13 | LiDAR Map Localization | 点云地图定位 |  | 把当前激光扫描与预建三维地图配准以求车辆位姿的方法。 |
| 14 | Visual Localization | 视觉定位 |  | 利用当前图像与地图、特征或参考图像确定车辆位置的方法。 |
| 15 | Visual–Inertial Odometry | 视觉惯性里程计 | VIO | 将相机与 IMU 结合估计连续运动状态的算法。 |
| 16 | Graph-based Localization | 图优化式定位 |  | 通过多时刻状态和测量因子联合优化车辆轨迹的定位方法。 |
| 17 | Pose Graph Optimization | 位姿图优化 |  | 依据相对运动和绝对观测等约束调整多个位姿的数值优化过程。 |
| 18 | Extended Kalman Filter | 扩展卡尔曼滤波 | EKF | 以非线性模型一阶线性化递推更新高斯状态估计的算法。 |
| 19 | Unscented Kalman Filter | 无迹卡尔曼滤波 | UKF | 通过 sigma 点传播非线性模型近似计算均值与协方差的滤波算法。 |
| 20 | Particle Localization | 粒子定位 |  | 通过带权随机样本近似非高斯车辆位姿后验分布的方法。 |
| 21 | Covariance Propagation | 协方差传播 |  | 根据运动模型与噪声统计更新定位不确定性矩阵的过程。 |
| 22 | Localization Drift | 定位漂移 |  | 估计位置或朝向误差随时间积累而逐渐偏离真实状态的现象。 |
| 23 | Yaw Angle | 航向角 |  | 描述车辆车体相对于参考坐标的水平转动方向的角度。 |
| 24 | Heading Error | 航向误差 |  | 车辆当前方向与参考路径或目标方向之间的角度差。 |
| 25 | Localization Integrity | 定位完整性 |  | 及时识别定位结果不可信并向下游报告风险的能力。 |

## 08. 高精地图、道路拓扑与车道语义

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | High-definition Map | 高精地图 | HD Map | 含有车道级拓扑、道路几何与交通语义的结构化地图。 |
| 2 | Lanelet | 车道片段 | Lanelet | 用左右边界及方向规则定义的可路由道路片段数据单元。 |
| 3 | Lanelet2 | Lanelet2 地图框架 |  | 以 lanelet、关系和交通规则构建可供路径规划使用的地图数据模型。 |
| 4 | Lane Graph | 车道连接图 |  | 用车道段为节点及可达转移为边表示道路拓扑的图。 |
| 5 | Road Topology | 道路拓扑 |  | 描述路段、车道、交叉口及其连通关系的离散结构。 |
| 6 | Lane Boundary Geometry | 车道边界几何 |  | 用离散点、样条或其他曲线参数描述车道物理边界的表示。 |
| 7 | Lane Centerline Geometry | 车道中心线几何 |  | 沿车道可行驶方向定义平滑参考路线的空间曲线。 |
| 8 | Road Segment | 道路片段 |  | 具有规定几何和道路属性的相邻路径区间。 |
| 9 | Intersection Geometry | 交叉口几何 |  | 描述交叉口内车道连接和可行驶区域形状的地图元素。 |
| 10 | Junction Connectivity | 路口连接关系 |  | 规定进入路口车道与可合法驶出的车道之间的关系。 |
| 11 | Lane Change Permission | 车道变换许可 |  | 由交通规则和车道线属性定义是否允许跨车道的地图语义。 |
| 12 | Speed Limit Attribute | 限速属性 |  | 表示道路或车道允许最高速度的结构化地图字段。 |
| 13 | Stop Sign Association | 停车标志关联 |  | 把交通停车标志或停车规则对应到受其约束道路区段的关系。 |
| 14 | Traffic Signal Group | 信号灯控制组 |  | 关联一个或多个路口通行流与特定信号灯控制逻辑的地图对象。 |
| 15 | Crosswalk Geometry | 人行横道几何 |  | 用多边形或边界集合描述行人过街区域的地图实体。 |
| 16 | Yield Rule | 让行规则 |  | 规定在特定冲突交通情形下谁应先行或避让的交通约束。 |
| 17 | Right-of-way | 通行优先权 |  | 在特定交通规则条件下某条交通流或主体具有优先通行资格的关系。 |
| 18 | Route Network | 道路路由网络 |  | 用于计算起点至目标连通路线的道路拓扑图。 |
| 19 | Route Planning | 道路路线规划 |  | 在车道或路网图上选择连接出发地和目的地的行驶路线的任务。 |
| 20 | Map Tile | 地图分片 |  | 按地理区域切割管理和更新的局部地图数据单元。 |
| 21 | Map Versioning | 地图版本管理 |  | 追踪地图几何、语义字段和道路变化的历史版本机制。 |
| 22 | Map Change Detection | 地图变化检测 |  | 识别真实道路结构与已有地图表示不一致的过程。 |
| 23 | Online Map Construction | 在线地图构建 |  | 根据实时感知推断局部车道、边界和交通语义的技术。 |
| 24 | Mapless Driving | 弱地图依赖驾驶 |  | 在不依赖完整预建高精地图条件下进行环境理解和驾驶决策的方案。 |
| 25 | Map Confidence | 地图信息置信度 |  | 评估当前地图元素是否与现实道路环境一致的可靠度指标。 |

## 09. 多传感器融合、占据网络与世界表示

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Sensor Fusion | 多传感器融合 |  | 把不同传感器的互补测量联合推断为一致环境或车辆状态的过程。 |
| 2 | Early Fusion | 早期融合 |  | 在较底层数据或特征阶段融合不同感知模态的策略。 |
| 3 | Late Fusion | 后期融合 |  | 分别获得各模态预测后再对决策或目标结果进行融合的方法。 |
| 4 | Feature-level Fusion | 特征级融合 |  | 在深度网络中将不同传感器编码特征进行聚合的机制。 |
| 5 | Decision-level Fusion | 决策级融合 |  | 依据多传感器各自的检测或分类结果生成联合结论的方式。 |
| 6 | BEV Feature Fusion | 鸟瞰特征融合 |  | 把多相机、激光等传感器信息映射到共同鸟瞰平面后整合的技术。 |
| 7 | Bird's-eye View Representation | 鸟瞰场景表示 | BEV | 以车辆周围地面坐标组织空间语义与目标特征的表示。 |
| 8 | Multi-camera BEV | 多相机鸟瞰表征 |  | 由不同方向相机图像共同构建自车周围空间特征的技术。 |
| 9 | Lift–Splat–Shoot | 提升泼溅推理结构 | LSS | 先将图像特征关联深度、投影到 BEV，再进行下游预测的架构。 |
| 10 | Occupancy Grid | 占据栅格 |  | 用离散网格值表示空间单元是否被物体占据的结构。 |
| 11 | 3D Occupancy Prediction | 三维占据预测 |  | 预测三维体素中被物体占据的概率及可选语义的感知任务。 |
| 12 | Semantic Occupancy | 语义占据 |  | 为占据空间单元同时分配车辆、道路或障碍类别的表示。 |
| 13 | Free-space Occupancy | 空闲空间占据状态 |  | 表达未被测得障碍占用且可供空间推理的体素或栅格状态。 |
| 14 | Unknown Space | 未知空间 |  | 因传感覆盖不足无法可靠判断空闲或占据的环境区域。 |
| 15 | Occupancy Flow | 占据流 |  | 描述空间占据状态随时间变化及运动趋势的动态场表示。 |
| 16 | Dynamic Occupancy | 动态占据 |  | 同时表示当前位置和未来可能运动变化的空间占据状态。 |
| 17 | Sensor Confidence | 传感置信度 |  | 表示特定模态或观测在当前环境条件下可靠性的数值或等级。 |
| 18 | Measurement Covariance | 测量协方差 |  | 描述传感器输出误差方差与分量间相关性的统计矩阵。 |
| 19 | Cross-modal Attention | 跨模态注意力 |  | 通过查询键值相关性让不同感知模态交换信息的神经网络机制。 |
| 20 | Temporal Feature Fusion | 时序特征融合 |  | 结合相邻时刻特征改善被遮挡目标识别和状态估计的方法。 |
| 21 | Ego-motion Compensation | 自车运动补偿 |  | 校正车辆自身位姿变化对不同时间感知测量的影响。 |
| 22 | Spatial Alignment | 空间对齐 |  | 将不同传感器观测转换到统一坐标系以建立几何对应的过程。 |
| 23 | Uncertainty-aware Fusion | 不确定性感知融合 |  | 根据不同观测噪声和置信程度调整融合权重或估计方式的方法。 |
| 24 | World Representation | 环境世界表示 |  | 对道路几何、物体、自由空间及可预测动态的结构化内部表达。 |
| 25 | Perception Failure Detection | 感知故障检测 |  | 识别传感器缺失、模型异常或感知输出不可信事件的处理机制。 |

## 10. 交通参与者运动预测与多智能体交互

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Motion Prediction | 运动预测 |  | 推断周围交通参与者在未来若干时间内可能行驶轨迹的任务。 |
| 2 | Trajectory Forecasting | 轨迹预测 |  | 根据历史状态和道路信息估计未来位置序列的任务。 |
| 3 | Behavior Prediction | 行为预测 |  | 判断其他车辆或行人可能执行的让行、转弯或变道行为。 |
| 4 | Intention Recognition | 交通意图识别 |  | 推断目标主体潜在目标车道、行进方向或行为计划的过程。 |
| 5 | Multi-modal Prediction | 多模态轨迹预测 |  | 输出多个不同的合理未来轨迹及其相应概率的预测方式。 |
| 6 | Unimodal Forecast | 单模态预测 |  | 以一个主要未来结果或单峰状态分布描述运动趋势的预测方式。 |
| 7 | Prediction Horizon | 预测时间范围 |  | 轨迹预测从当前时刻向未来延伸的时长。 |
| 8 | Historical Context Window | 历史上下文窗口 |  | 输入预测模型的过去若干时刻轨迹与感知状态数据。 |
| 9 | Social Interaction Modeling | 交通交互建模 |  | 在预测中显式考虑主体间让行、跟车、合流等相互影响的机制。 |
| 10 | Agent Interaction Graph | 交通主体交互图 |  | 以车辆、行人节点和交互边组织多主体关系的图结构。 |
| 11 | Social Pooling | 社会交互特征聚合 |  | 从邻近主体状态中聚合交互信息用于轨迹预测的技术。 |
| 12 | Lane-conditioned Prediction | 车道条件轨迹预测 |  | 以道路拓扑和可行车道约束生成主体未来轨迹的预测方法。 |
| 13 | Map-aware Prediction | 地图感知运动预测 |  | 结合车道几何、路权与交通信号信息推断未来行为的技术。 |
| 14 | Goal-based Prediction | 目标驱动预测 |  | 先推断主体可能目的位置或区域，再产生对应轨迹的方案。 |
| 15 | Scene-conditioned Prediction | 场景条件预测 |  | 根据全部相关交通参与者及静动态场景特征预测未来运动的方法。 |
| 16 | Joint Motion Prediction | 联合运动预测 |  | 同时建模多个主体未来轨迹之间相互依赖的预测问题。 |
| 17 | Marginal Motion Prediction | 边际轨迹预测 |  | 分别为单个主体输出未来轨迹分布、未显式生成联合结果的方式。 |
| 18 | Trajectory Probability | 轨迹候选概率 |  | 表示一个未来轨迹模式在模型分布下相对可能性的权重。 |
| 19 | Prediction Calibration | 预测概率校准 |  | 检查预测轨迹分布的置信水平与真实发生频率相符合的性质。 |
| 20 | Average Displacement Error | 平均位移误差 | ADE | 对预测与真实轨迹对应时间点的空间距离求平均的指标。 |
| 21 | Final Displacement Error | 最终位移误差 | FDE | 计算预测终点与真实终点之间空间距离的指标。 |
| 22 | Miss Rate | 轨迹预测漏中率 | MR | 真实轨迹未落入预测候选容差区域的样本比例。 |
| 23 | Collision Prediction | 潜在碰撞预测 |  | 根据未来运动估计主体之间可能产生空间重叠的情形。 |
| 24 | Yield Behavior Prediction | 让行行为预测 |  | 判断其他交通主体是否准备减速、等待或放弃优先通行的任务。 |
| 25 | Interaction-aware Forecast | 交互感知预测 |  | 允许主体预测随其他参与者和自车计划改变而调整的模型。 |

## 11. 行为决策、交通规则与路口博弈

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Behavior Planning | 驾驶行为规划 |  | 决定跟车、让行、变道、超车或停车等离散驾驶行为的过程。 |
| 2 | Decision Making | 自动驾驶决策 |  | 根据目标、规则、场景及风险从可选驾驶策略中选择行动的过程。 |
| 3 | Finite-state Machine | 有限状态机 | FSM | 以离散状态及事件触发转移组织驾驶逻辑的模型。 |
| 4 | Behavior Tree | 行为树 | BT | 用层级选择、顺序和条件节点组织可执行驾驶行为的结构。 |
| 5 | Rule-based Planning | 基于规则的行为规划 |  | 利用显式交通规范和手工条件决定驾驶行为的方法。 |
| 6 | Rule Compliance | 交通规则遵循 |  | 驾驶行为在指定道路交通法规与局部约束下保持合规的性质。 |
| 7 | Route Following | 路线跟随 |  | 根据给定路网目标持续选择能够保持全局路线的驾驶行为。 |
| 8 | Lane Keeping | 车道保持 |  | 控制车辆继续沿当前有效行驶车道移动的驾驶行为。 |
| 9 | Lane Change Decision | 变道决策 |  | 判断何时以及向哪条车道安全转移的规划步骤。 |
| 10 | Gap Acceptance | 交通间隙接受 |  | 在合流、变道或穿越路口时评估可用交通时间或空间间隙的决策。 |
| 11 | Merge Decision | 合流决策 |  | 在汇入主路或邻接车道时确定通行顺序和加减速策略的过程。 |
| 12 | Overtaking Decision | 超车决策 |  | 综合路线、前车速度及交通规则判断能否绕过慢车的规划任务。 |
| 13 | Yield Decision | 让行决策 |  | 根据优先权与预测冲突判断自车应等待还是继续行驶的决策。 |
| 14 | Stop Decision | 停车决策 |  | 确定必须制动至静止的位置、时机及触发规则的过程。 |
| 15 | Intersection Negotiation | 路口通行协商 |  | 依据优先权、车流与主体交互选择安全穿越路口时机的过程。 |
| 16 | Unprotected Left Turn | 无保护左转 |  | 在缺少专用通行保护时需判断对向车辆和行人间隙的左转场景。 |
| 17 | Roundabout Navigation | 环岛通行 |  | 根据环形道路的车道、入口让行与出口关系规划的驾驶任务。 |
| 18 | Four-way Stop | 四向停车路口 |  | 多入口存在停牌控制、需根据到达和优先权规则协调通行的场景。 |
| 19 | Traffic Signal Compliance | 交通信号遵循 |  | 根据车辆所受信号灯状态决定停止、等待或通行的能力。 |
| 20 | Right-of-way Reasoning | 通行优先权推理 |  | 在特定路口和车道交通规则下判断各主体优先关系的过程。 |
| 21 | Occluded Intersection Handling | 遮挡路口处理 |  | 在交叉口视野被遮挡时采取减速、观察和保守规划的策略。 |
| 22 | Decision Hysteresis | 决策滞回 |  | 通过改变切换阈值或保持状态减少驾驶行为频繁抖动的机制。 |
| 23 | Commitment to Maneuver | 机动承诺机制 |  | 在满足安全条件时维持已选择的变道或通过行为、减少无谓反复的策略。 |
| 24 | Contingency Planning | 应急备选规划 |  | 预先保留无法完成首选机动时可立即执行的替代策略。 |
| 25 | Traffic Negotiation | 交通交互协商 |  | 通过车速、间隙和运动意图与其他道路使用者形成可通行关系的过程。 |

## 12. 轨迹生成、速度规划与约束优化

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Trajectory Planning | 轨迹规划 |  | 在道路、障碍和车辆动力学约束下生成带时间参数的驾驶状态序列。 |
| 2 | Frenet Coordinate System | 弗雷内路径坐标系 |  | 用沿参考路径弧长和横向偏移描述车辆位置的曲线坐标系。 |
| 3 | Cartesian Trajectory | 笛卡尔轨迹 |  | 在世界或局部欧氏坐标系中表示车辆时变位置与朝向的轨迹。 |
| 4 | Reference Line | 参考线 |  | 沿车道中心或规划路线生成、供轨迹优化依托的空间曲线。 |
| 5 | Reference Path Smoothing | 参考路径平滑 |  | 降低地图离散中心线曲率突变以提高轨迹可跟踪性的过程。 |
| 6 | Path–Speed Decoupling | 路径速度解耦 |  | 先确定几何路径、再独立计算沿路径速度随时间变化的规划方法。 |
| 7 | Joint Space–Time Planning | 时空联合规划 |  | 在同一优化过程中联合决定车辆空间路径与到达时间的技术。 |
| 8 | Speed Profile | 速度曲线 |  | 描述沿时间或路径弧长变化的期望车速序列。 |
| 9 | Acceleration Profile | 加速度曲线 |  | 描述期望纵向加速度随时间或路径位置变化的函数。 |
| 10 | Jerk Profile | 加加速度曲线 |  | 描述加速度时间变化率并用于舒适性约束的轨迹量。 |
| 11 | Curvature Profile | 曲率曲线 |  | 表示路径上各位置曲率变化的函数。 |
| 12 | Curvature Constraint | 曲率约束 |  | 限制车辆可实现路径弯曲程度的几何约束。 |
| 13 | Lateral Acceleration Limit | 横向加速度限制 |  | 根据速度和路径曲率设置允许侧向加速度上限的条件。 |
| 14 | Vehicle Kinematic Feasibility | 车辆运动学可行性 |  | 规划轨迹符合转向几何和速度层级运动约束的性质。 |
| 15 | Dynamic Feasibility | 车辆动力学可行性 |  | 规划状态与控制符合轮胎附着、惯性及执行器动力学限制的性质。 |
| 16 | Obstacle Avoidance Constraint | 障碍避让约束 |  | 要求自车车身及运动轨迹与预测障碍占据区域保持规定间隔的限制。 |
| 17 | Space–Time Graph | 路径时间图 | ST Graph | 以路径弧长和时间为轴表达障碍物运动与可行速度区间的表示。 |
| 18 | Quadratic Programming | 二次规划 | QP | 以二次目标与线性约束求解路径或控制优化变量的优化问题。 |
| 19 | Nonlinear Programming | 非线性规划 | NLP | 目标或约束包含非线性函数的轨迹优化问题。 |
| 20 | Sequential Quadratic Programming | 序列二次规划 | SQP | 通过反复求解局部二次子问题处理非线性规划的算法族。 |
| 21 | Model Predictive Planning | 模型预测式规划 |  | 在滚动有限时间窗口内重复优化车辆未来轨迹的策略。 |
| 22 | Spline Trajectory | 样条轨迹 |  | 使用分段多项式及连续性约束表示平滑车辆运动的轨迹。 |
| 23 | Quintic Polynomial Trajectory | 五次多项式轨迹 |  | 可通过位置、速度和加速度端点条件构建的五次参数曲线。 |
| 24 | Trajectory Replanning | 轨迹重规划 |  | 根据新感知和预测结果定期更新已有未来轨迹的过程。 |
| 25 | Trajectory Validation | 轨迹有效性检查 |  | 在执行前检查候选轨迹碰撞、限速、曲率和动态约束是否满足的步骤。 |

## 13. 车辆动力学、横纵向控制与执行跟踪

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Vehicle Dynamics | 车辆动力学 |  | 研究车辆质量、轮胎力、惯性与驾驶输入如何决定运动状态的理论。 |
| 2 | Bicycle Model | 自行车模型 |  | 将左右车轮对合并为等效前后车轮的简化车辆运动学或动力学模型。 |
| 3 | Kinematic Bicycle Model | 运动学自行车模型 |  | 在低侧滑近似下依据轴距、转向角及车速计算车辆平面运动的模型。 |
| 4 | Dynamic Bicycle Model | 动力学自行车模型 |  | 进一步考虑侧偏角、轮胎侧向力和车辆横摆惯性等效应的车辆模型。 |
| 5 | Wheelbase | 轴距 |  | 车辆前后车轴参考中心之间的纵向距离。 |
| 6 | Track Width | 轮距 |  | 车辆同一车轴左右车轮参考中心之间的横向距离。 |
| 7 | Steering Angle | 转向角 |  | 车轮或等效前轮相对车体纵轴的旋转角。 |
| 8 | Yaw Rate | 横摆角速度 |  | 车辆绕垂直轴旋转的角速度。 |
| 9 | Sideslip Angle | 车辆侧偏角 |  | 车辆速度方向与车体纵向轴之间的夹角。 |
| 10 | Tire Slip Angle | 轮胎侧偏角 |  | 车轮指向与接触点实际平面运动方向之间的夹角。 |
| 11 | Cornering Stiffness | 轮胎侧偏刚度 |  | 在线性近似范围内轮胎横向力对侧偏角变化的局部斜率。 |
| 12 | Friction Circle | 轮胎附着圆 |  | 描述纵向和横向轮胎力合成受可用路面摩擦限制的近似边界。 |
| 13 | Longitudinal Control | 纵向控制 |  | 通过驱动与制动调整车辆速度、跟车距离和停车位置的控制任务。 |
| 14 | Lateral Control | 横向控制 |  | 通过转向等输入使车辆跟踪期望道路位置和航向的控制任务。 |
| 15 | Cruise Control | 巡航速度控制 | CC | 维持车辆目标行驶速度的反馈控制功能。 |
| 16 | Adaptive Cruise Control | 自适应巡航控制 | ACC | 根据前车距离和相对速度调节车速的驾驶辅助控制功能。 |
| 17 | Proportional–Integral–Derivative Control | 比例积分微分控制 | PID | 组合当前、累计和变化率误差生成控制量的经典方法。 |
| 18 | Pure Pursuit | 纯跟踪控制 |  | 通过参考路径上的预瞄点计算车辆转向曲率的几何跟踪算法。 |
| 19 | Stanley Controller | Stanley 路径跟踪控制 |  | 基于横向位置误差与航向误差构建转向输入的控制方法。 |
| 20 | Linear Quadratic Regulator | 线性二次调节器 | LQR | 对线性系统和二次性能目标求解最优状态反馈的方法。 |
| 21 | Model Predictive Control | 模型预测控制 | MPC | 在滚动时间窗口内求解有约束预测优化并实施首段控制的策略。 |
| 22 | Feedforward Steering | 前馈转向 |  | 根据参考路径曲率和车辆模型预先产生转向分量的控制方式。 |
| 23 | Feedback Steering | 反馈转向 |  | 依据实际轨迹跟踪误差实时修正方向控制输入的方法。 |
| 24 | Actuator Delay Compensation | 执行器延迟补偿 |  | 在控制规划中预测转向或制动指令到生效之间的时间滞后。 |
| 25 | Control Saturation | 控制饱和 |  | 转向、驱动或制动力命令达到执行器上下限而不能继续增加的现象。 |

## 14. 交通安全约束、风险与应急策略

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Collision Risk Estimation | 碰撞风险估计 |  | 根据主体位置、预测轨迹和不确定性评估可能碰撞的概率与严重性。 |
| 2 | Time to Collision | 碰撞时间 | TTC | 在给定相对运动简化假设下估计两主体发生接触的剩余时间。 |
| 3 | Time Headway | 车头时距 | THW | 自车到达前车当前参考位置所需时间的近似车距指标。 |
| 4 | Stopping Distance | 停车距离 |  | 包含驾驶或系统反应时间和制动过程所需路程的总体距离。 |
| 5 | Braking Distance | 制动距离 |  | 车辆实际开始制动后直至停止所行驶的距离。 |
| 6 | Safety Distance | 安全间距 |  | 根据速度、反应时间、不确定性及规则设置的最小车间距离。 |
| 7 | Emergency Braking | 紧急制动 |  | 当风险过高时施加较强制动力减速或停止车辆的操作。 |
| 8 | Automatic Emergency Braking | 自动紧急制动 | AEB | 在即将发生碰撞时自动警告或制动以降低风险的辅助安全功能。 |
| 9 | Forward Collision Warning | 前向碰撞预警 | FCW | 通过前方目标与相对运动判断可能追尾并警告驾驶者的功能。 |
| 10 | Lane Departure Warning | 车道偏离预警 | LDW | 车辆无意跨越车道边界时向驾驶者发出提醒的功能。 |
| 11 | Lane Keeping Assist | 车道保持辅助 | LKA | 在规定条件下通过转向辅助减少意外偏离车道的系统。 |
| 12 | Blind Spot Detection | 盲区监测 | BSD | 检测车辆侧后方盲区内相关交通参与者并发出提示的功能。 |
| 13 | Minimum Risk Maneuver Planning | 最小风险机动规划 |  | 在能力不足或关键故障时确定安全降速、靠边或停车策略的过程。 |
| 14 | Emergency Trajectory | 应急轨迹 |  | 用于避险或风险缓解、并受车辆极限与周边交通约束的短期轨迹。 |
| 15 | Fail-safe Behavior | 故障安全行为 |  | 检测故障后采取停止或其他降低风险措施的系统响应策略。 |
| 16 | Fail-operational Capability | 故障后持续运行能力 |  | 在规定部分故障下仍能完成受限或全部功能的系统设计能力。 |
| 17 | Fallback Trajectory | 后备轨迹 |  | 首选轨迹不可执行时可快速切换的保守运动计划。 |
| 18 | Safety Constraint | 安全约束 |  | 在规划和控制过程中必须满足的碰撞、速度或最小距离限制。 |
| 19 | Control Barrier Function | 控制屏障函数 | CBF | 通过不变性约束限制控制指令、防止状态进入危险集合的函数。 |
| 20 | Responsibility-sensitive Safety | 责任敏感安全模型 | RSS | 以形式化安全距离和响应规则定义部分交通交互责任的模型框架。 |
| 21 | Reachable Set | 可达状态集 |  | 在给定模型、控制限制与不确定性下未来可能到达的状态集合。 |
| 22 | Safe Set | 安全状态集 |  | 按照预定义碰撞与约束条件被认为可接受的系统状态集合。 |
| 23 | Risk-aware Planning | 风险感知规划 |  | 在优化目标和约束中加入碰撞概率、后果与模型不确定性的规划方法。 |
| 24 | Uncertainty-aware Control | 不确定性感知控制 |  | 根据模型和观测可信度调整控制策略或安全裕度的技术。 |
| 25 | Safety Supervisor | 安全监督模块 |  | 独立检查感知规划控制结果并在必要时阻断不安全命令的系统组件。 |

## 15. 端到端自动驾驶、模仿学习与世界模型

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | End-to-end Driving | 端到端驾驶 |  | 使用可学习模型直接从传感表示或图像生成驾驶行为或轨迹的技术范式。 |
| 2 | Modular Autonomous Driving | 模块化自动驾驶 |  | 将感知、定位、预测、规划及控制组织为显式接口子系统的架构。 |
| 3 | Imitation Learning | 模仿学习 | IL | 根据人类或专家驾驶轨迹学习动作或策略的机器学习方法。 |
| 4 | Behavior Cloning | 行为克隆 | BC | 把专家示范的观测动作配对作为监督训练策略的方案。 |
| 5 | Closed-loop Learning | 闭环驾驶学习 |  | 在模型动作影响后续观测的环境交互中优化驾驶策略的方法。 |
| 6 | Open-loop Training | 开环轨迹训练 |  | 根据固定离线数据拟合动作或轨迹、不在训练中执行预测反馈的方式。 |
| 7 | Distribution Shift | 数据分布偏移 |  | 模型实际运行观测与训练数据分布不同导致泛化困难的现象。 |
| 8 | Covariate Shift in Imitation | 模仿学习观测偏移 |  | 模型动作偏差逐渐引导车辆进入示范数据中少见状态的误差累积现象。 |
| 9 | Dataset Aggregation | 数据集聚合 | DAgger | 通过迭代收集当前策略状态和专家标签降低模仿学习状态偏移的方法。 |
| 10 | Multi-camera Policy | 多相机驾驶策略 |  | 联合使用车身周边多个图像视角预测车辆未来行为的模型。 |
| 11 | Temporal Driving Model | 时序驾驶模型 |  | 利用历史图像和车辆状态推断当前决策或未来轨迹的模型。 |
| 12 | Bird's-eye-view Transformer | 鸟瞰 Transformer |  | 通过注意力把多视角视觉特征转换为统一鸟瞰空间表示的架构。 |
| 13 | Vectorized Scene Representation | 向量化场景表示 |  | 以车道折线、对象状态和关系替代完整栅格描述驾驶场景的表示。 |
| 14 | Occupancy-centric Planning | 占据中心规划 |  | 把未来空间占据预测作为轨迹避障和驾驶选择的重要输入的技术。 |
| 15 | World Model | 驾驶世界模型 |  | 学习交通环境动态变化并可对候选动作结果进行预测的环境模型。 |
| 16 | Latent Dynamics Model | 潜在动力学模型 |  | 在学习到的紧凑隐变量空间中预测未来交通状态的模型。 |
| 17 | Action-conditioned Prediction | 动作条件场景预测 |  | 根据自车候选动作预测周边主体或场景随后变化的模型任务。 |
| 18 | Generative Trajectory Model | 生成式轨迹模型 |  | 使用概率生成模型输出多个条件驾驶轨迹候选的架构。 |
| 19 | Diffusion Planner | 扩散式轨迹规划器 |  | 通过扩散去噪过程生成符合场景约束的车辆未来轨迹的方法。 |
| 20 | Vision–Language–Action Driving | 视觉语言动作驾驶模型 | VLA | 联合视觉、语言提示及驾驶动作学习决策的多模态策略方向。 |
| 21 | Language-conditioned Driving | 语言条件驾驶 |  | 根据自然语言目标或语义提示影响行驶决策和轨迹的技术。 |
| 22 | Driving Foundation Model | 驾驶基础模型 |  | 利用大规模多场景驾驶数据预训练、可迁移到多种车辆任务的共享模型。 |
| 23 | Teacher–Student Distillation | 教师学生蒸馏 |  | 通过高容量教师输出或表示训练轻量化车载学生模型的方法。 |
| 24 | Policy Uncertainty Estimation | 策略不确定性估计 |  | 衡量学习型驾驶策略对特定动作选择可信程度的模型技术。 |
| 25 | Hybrid Learned Planner | 混合学习规划器 |  | 将学习型轨迹评分或生成与规则及可行性约束结合的驾驶规划方式。 |

## 16. 车路协同、V2X 与智能交通基础设施

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Vehicle-to-everything Communication | 车联网通信 | V2X | 车辆与其他车辆、道路设施、行人设备或网络之间的信息交换技术。 |
| 2 | Vehicle-to-vehicle Communication | 车车通信 | V2V | 车辆之间直接或间接交换位置、速度和协同信息的通信方式。 |
| 3 | Vehicle-to-infrastructure Communication | 车路通信 | V2I | 车辆与路侧单元或交通设施之间的数据交换机制。 |
| 4 | Vehicle-to-pedestrian Communication | 车人通信 | V2P | 车辆与行人或骑行者设备间共享存在和潜在风险信息的方式。 |
| 5 | Vehicle-to-network Communication | 车网通信 | V2N | 车辆通过蜂窝等网络连接云端和服务平台的通信模式。 |
| 6 | Roadside Unit | 路侧通信单元 | RSU | 安装在道路基础设施处用于车路信息交换的通信设备。 |
| 7 | On-board Unit | 车载通信单元 | OBU | 集成在车辆内支持 V2X 消息接收和发送的设备。 |
| 8 | Cellular V2X | 蜂窝车联网 | C-V2X | 基于蜂窝无线技术支持车端与周边或网络信息交换的通信标准体系。 |
| 9 | Dedicated Short-range Communication | 专用短程通信 | DSRC | 面向车用场景的一类短距离无线通信技术。 |
| 10 | Basic Safety Message | 基本安全消息 | BSM | 用于广播车辆位置、速度和其他安全相关状态的消息类型。 |
| 11 | Cooperative Awareness Message | 协作感知通告 | CAM | 在部分车联网标准中广播车辆运动及基础状态的消息。 |
| 12 | Decentralized Environmental Notification Message | 分布式环境事件消息 | DENM | 用于发布道路危险事件与相关地理、时间信息的协作消息。 |
| 13 | Signal Phase and Timing | 信号相位与剩余时间 | SPaT | 描述交通信号状态及预测切换时间的结构化消息内容。 |
| 14 | MAP Message | 路口地图消息 | MAP | 在 V2X 生态中描述交叉口几何和车道连接关系的数据消息。 |
| 15 | Cooperative Perception | 协同感知 |  | 结合车辆与路侧或其他车辆的观测扩大环境可感知范围的技术。 |
| 16 | Collective Perception Message | 集体感知消息 | CPM | 传送协同检测对象及传感信息的标准化消息类别。 |
| 17 | Infrastructure Perception | 路侧基础设施感知 |  | 通过部署在道路上的传感器检测交通目标和环境状态的系统能力。 |
| 18 | Intersection Management | 交叉口协同管理 |  | 依据多个车辆意图与信号控制优化路口通行顺序的方法。 |
| 19 | Platooning | 车辆编队行驶 |  | 多辆车通过协同控制以较小间距成队运行的交通方式。 |
| 20 | Cooperative Adaptive Cruise Control | 协同自适应巡航 | CACC | 结合车辆间通信与传感数据改善跟车速度控制的技术。 |
| 21 | Cooperative Lane Change | 协同变道 |  | 多车交换意图或状态并协调安全变道时机的驾驶行为。 |
| 22 | V2X Latency | 车联网通信延迟 |  | 从消息生成到接收并用于决策之间的时间差。 |
| 23 | V2X Trust Management | 车联网信任管理 |  | 验证车路消息发送方身份及数据完整性的安全处理机制。 |
| 24 | Misbehavior Detection | 异常车联网消息检测 |  | 识别伪造、不一致或恶意车路消息的安全能力。 |
| 25 | Edge-assisted Driving | 边缘协助驾驶 |  | 利用道路边缘计算为车端提供环境感知或交通协调辅助的模式。 |

## 17. 自动驾驶仿真、场景标准与数字孪生

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Autonomous Driving Simulation | 自动驾驶仿真 |  | 在虚拟交通环境中重现传感、车辆运动及交通交互以测试驾驶系统的过程。 |
| 2 | CARLA Simulator | CARLA 自动驾驶仿真器 | CARLA | 用于自动驾驶感知、规划和闭环评测的开源城市道路仿真平台。 |
| 3 | Scenario-based Testing | 场景化测试 |  | 围绕明确道路条件、交通主体和事件组合评估系统行为的方法。 |
| 4 | Test Scenario | 测试场景 |  | 规定道路、主体、行为、初始条件与评价目标的结构化测试案例。 |
| 5 | Logical Scenario | 逻辑场景 |  | 以参数范围和约束而非单一固定数值定义的一类测试情况。 |
| 6 | Concrete Scenario | 具体场景 |  | 为逻辑场景参数指定确定数值后得到的可执行案例。 |
| 7 | Functional Scenario | 功能场景 |  | 以自然语言或高层语义概括道路情境和预期驾驶任务的场景定义。 |
| 8 | Scenario Parameterization | 场景参数化 |  | 用车速、道路几何、天气及主体行为等变量控制测试环境的方法。 |
| 9 | Scenario Coverage | 场景覆盖度 |  | 量化测试集合覆盖预定环境、风险和交通交互条件的程度。 |
| 10 | Scenario Generation | 场景生成 |  | 通过采样、规则或优化生成新的交通仿真测试案例的技术。 |
| 11 | Scenario Mutation | 场景变异 |  | 系统改变既有场景参数以探索失败边界的测试策略。 |
| 12 | Adversarial Scenario Search | 对抗场景搜索 |  | 有目的地优化交通主体或环境条件以触发系统薄弱行为的测试方法。 |
| 13 | ASAM OpenDRIVE | ASAM 道路网络描述标准 | OpenDRIVE | 对道路几何、车道与相关交通基础设施进行结构化描述的开放标准。 |
| 14 | ASAM OpenSCENARIO | ASAM 动态驾驶场景标准 | OpenSCENARIO | 描述交通参与者行为、时序和场景测试条件的标准体系。 |
| 15 | ASAM OpenCRG | ASAM 道路表面网格标准 | OpenCRG | 用于精细描述道路表面高程或粗糙度等特征的开放数据标准。 |
| 16 | OpenSCENARIO DSL | OpenSCENARIO 场景描述语言 | OSC DSL | 用于以领域特定语言形式定义参数化交通场景与行为的方式。 |
| 17 | Simulation Time Step | 仿真时间步 |  | 每次虚拟物理状态更新对应的离散模拟时间间隔。 |
| 18 | Synchronous Simulation | 同步仿真 |  | 所有参与组件按统一步长或时钟协调推进模拟状态的模式。 |
| 19 | Asynchronous Simulation | 异步仿真 |  | 不同模拟组件按各自时间调度执行并交换数据的运行模式。 |
| 20 | Sensor Simulation | 传感器仿真 |  | 根据虚拟场景生成相机、激光、雷达等设备近似测量的过程。 |
| 21 | Vehicle Dynamics Simulation | 车辆动力学仿真 |  | 利用轮胎、悬架和车体力学模型计算模拟车辆运动的过程。 |
| 22 | Closed-loop Simulation | 闭环仿真 |  | 将被测驾驶策略动作反馈到场景中、影响后续观测的评测方式。 |
| 23 | Open-loop Replay | 开环数据回放 |  | 按记录数据固定播放历史观测、模型输出不影响后续输入的测试方式。 |
| 24 | Digital Twin for Driving | 驾驶系统数字孪生 |  | 根据道路或车辆真实数据维持相应数字模型以辅助调试与评测的框架。 |
| 25 | Simulation-to-reality Gap | 仿真现实差距 |  | 仿真中的外观、动力学及交通行为与真实部署分布之间的偏差。 |

## 18. 驾驶数据集、基准指标与系统性误差分析

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Autonomous Driving Dataset | 自动驾驶数据集 |  | 包含道路传感观测、车辆状态、标注与可选未来轨迹的研究数据集合。 |
| 2 | Waymo Open Dataset | Waymo 开放数据集 |  | 面向自动驾驶感知、运动预测和端到端研究的数据资源系列。 |
| 3 | nuScenes Dataset | nuScenes 数据集 |  | 包含多传感器都市道路数据及三维目标、地图等标注的自动驾驶数据集。 |
| 4 | KITTI Vision Benchmark | KITTI 视觉基准 |  | 提供车载视觉、激光和定位等任务评测的道路场景数据集。 |
| 5 | Argoverse Dataset | Argoverse 数据集 |  | 面向交通感知、地图及主体运动预测的自动驾驶数据资源。 |
| 6 | BDD100K Dataset | BDD100K 驾驶视觉数据集 |  | 覆盖多样时段天气和道路场景的视频与图像标注数据集。 |
| 7 | Sensor Calibration Metadata | 传感器标定元数据 |  | 记录相机内外参、激光安装关系及采样设备配置的数据字段。 |
| 8 | Object Detection Average Precision | 目标检测平均精度 | AP | 按精确率召回率曲线汇总一类目标检测结果质量的指标。 |
| 9 | Mean Average Precision | 检测平均精度均值 | mAP | 按规定类别及评价条件对多个 AP 数值求平均的指标。 |
| 10 | 3D Intersection over Union | 三维交并比 | 3D IoU | 预测三维物体框与真实框交集体积除以并集体积的几何指标。 |
| 11 | Center Distance Error | 中心位置误差 |  | 预测物体中心与参考中心之间的空间距离偏差。 |
| 12 | Orientation Error | 朝向估计误差 |  | 预测目标航向与参考航向之间经角度周期归一化计算的偏差。 |
| 13 | Velocity Estimation Error | 速度估计误差 |  | 模型估计目标速度与参考速度在规定坐标系及时间点之间的差异。 |
| 14 | Minimum ADE | 最小平均位移误差 | minADE | 从多个候选未来轨迹中选择平均位移误差最小者作为评分的指标。 |
| 15 | Minimum FDE | 最小终点位移误差 | minFDE | 从多个候选轨迹中选取终点误差最小值的评价指标。 |
| 16 | Collision Rate | 碰撞率 |  | 在规定驾驶任务和测试分布下发生碰撞的次数或运行比例。 |
| 17 | Route Completion | 路线完成率 |  | 衡量车辆按指定路线到达进度或完成比例的任务指标。 |
| 18 | Intervention Rate | 接管干预率 |  | 在规定行驶距离、时间或场景数中人类干预自动化行为的频率。 |
| 19 | Disengagement Rate | 自动驾驶退出率 |  | 按规定计量单位统计自动驾驶功能意外或人工退出的频率。 |
| 20 | Traffic Rule Violation Rate | 交通规则违规率 |  | 按统一规则判定的驾驶违规事件占总运行单位的比例。 |
| 21 | Driving Comfort Metric | 驾驶舒适性指标 |  | 通过纵横向加速度、加加速度等量评价乘坐平顺性的指标。 |
| 22 | Closed-loop Driving Score | 闭环驾驶综合评分 |  | 根据闭环仿真中的任务完成、安全、效率等结果构建的聚合评分。 |
| 23 | Counterfactual Evaluation | 反事实评测 |  | 估计车辆采取未实际执行动作时可能产生的系统结果的方法。 |
| 24 | Error Taxonomy | 驾驶错误分类体系 |  | 把漏检、误判、轨迹冲突、控制抖动等失败按根因组织的分析结构。 |
| 25 | Data Leakage | 数据泄漏 |  | 训练数据包含测试场景或可推断答案的信息导致评测结果虚高的现象。 |

## 19. 功能安全、SOTIF、网络安全与验证论证

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Functional Safety | 功能安全 |  | 控制电气电子系统失效引发不合理风险的工程活动和要求体系。 |
| 2 | ISO 26262 | 道路车辆功能安全标准 | ISO 26262 | 面向道路车辆电气电子系统生命周期功能安全的国际标准系列。 |
| 3 | ISO 21448 | 预期功能安全标准 | ISO 21448 | 针对系统功能不足或可预见误用引起风险的预期功能安全指导标准。 |
| 4 | Safety of the Intended Functionality | 预期功能安全 | SOTIF | 针对无明显系统故障也可能因感知和决策能力不足产生的风险开展安全分析的领域。 |
| 5 | Automotive Safety Integrity Level | 汽车安全完整性等级 | ASIL | 依据危险严重度、暴露概率及可控性确定的汽车功能安全风险等级。 |
| 6 | Hazard Analysis and Risk Assessment | 危害分析与风险评估 | HARA | 识别可能危险事件并确定必要功能安全要求的工程流程。 |
| 7 | Functional Safety Concept | 功能安全概念 |  | 把安全目标细化为车辆级功能安全要求的架构描述。 |
| 8 | Technical Safety Concept | 技术安全概念 |  | 把功能安全要求分配到系统硬件和软件设计中的技术方案。 |
| 9 | Safety Goal | 安全目标 |  | 为减轻特定危险事件风险定义的最高层安全要求。 |
| 10 | Safety Requirement | 安全要求 |  | 为预防、检测或控制危险事件而必须满足的系统性能或行为约束。 |
| 11 | Safety Case | 安全论证案卷 |  | 以主张、证据和推理结构论证系统在规定条件下满足安全要求的资料集合。 |
| 12 | Safety Argument | 安全论证 |  | 把具体安全主张与支持证据通过逻辑关系关联的推理。 |
| 13 | Hazardous Event | 危险事件 |  | 危险源与特定运行情境组合后可能对人员或环境造成损害的事件。 |
| 14 | Risk Classification | 风险分类 |  | 依据严重度、发生可能性和可控性等准则划分风险等级的过程。 |
| 15 | SOTIF Triggering Condition | SOTIF 触发条件 |  | 使预期功能不足暴露并可能引发危险行为的特定场景或输入条件。 |
| 16 | Known Unsafe Scenario | 已知不安全场景 |  | 已识别系统能力不足且存在不能接受风险的运行情景。 |
| 17 | Unknown Unsafe Scenario | 未知不安全场景 |  | 在设计和验证阶段尚未识别、但实际可能引发风险的场景类别。 |
| 18 | Operational Safety Monitor | 运行安全监视器 |  | 在车辆执行中持续检查安全前提、感知健康和控制边界的独立或半独立组件。 |
| 19 | Fault Detection and Isolation | 故障检测与隔离 | FDI | 识别故障存在及定位相关部件或信号来源的技术。 |
| 20 | Fault Tolerance | 容错 |  | 在部分组件故障发生后仍能保持规定安全或服务能力的系统性质。 |
| 21 | Freedom from Interference | 免受相互干扰 |  | 保证一个软件或硬件组件不会意外破坏另一关键组件的安全要求的设计原则。 |
| 22 | Cybersecurity Engineering | 车辆网络安全工程 |  | 识别并控制车辆通信、软件更新和计算接口攻击风险的活动。 |
| 23 | ISO/SAE 21434 | 道路车辆网络安全工程标准 | ISO/SAE 21434 | 规定道路车辆网络安全风险管理与产品生命周期工程活动的国际标准。 |
| 24 | Threat Analysis and Risk Assessment | 威胁分析与风险评估 | TARA | 识别可能攻击路径及损害后果并确定网络安全保护优先级的过程。 |
| 25 | Verification and Validation | 验证与确认 | V&V | 分别检查系统是否符合规定要求和是否满足预期实际使用需求的工程过程。 |

## 20. 部署运行、远程协助与数据闭环工程

| # | English term | 中文译名 | Abbr. | 专业定义 |
|---:|---|---|---|---|
| 1 | Autonomous Fleet Operations | 自动驾驶车队运营 |  | 管理多辆自动驾驶车辆的任务调度、状态监控、运维及应急流程的体系。 |
| 2 | Fleet Management | 车队管理 |  | 协调车辆任务、位置、服务能力与维护资源的运营功能。 |
| 3 | Remote Assistance | 远程协助 |  | 在车辆无法独立完成特定问题时由远端人员提供高层指导或支持的机制。 |
| 4 | Remote Operation | 远程操作 |  | 远端人员通过通信链路直接控制或规定车辆动作的操作模式。 |
| 5 | Teleoperation | 远程驾驶操控 |  | 远程操作者连续承担部分或全部车辆运动控制的交互方式。 |
| 6 | Fleet Dispatching | 车队派单调度 |  | 根据服务请求、车辆位置及能力分配运输或运营任务的过程。 |
| 7 | Operational Monitoring | 运行监控 |  | 持续收集车辆健康、场景状态和安全事件以支持运营的机制。 |
| 8 | Vehicle Telemetry | 车辆遥测 |  | 由车端传回速度、位置、健康、网络等运行状态数据的机制。 |
| 9 | Health Check | 健康检查 |  | 按既定规则检测车辆、传感器和计算服务是否处于可用状态的操作。 |
| 10 | Heartbeat Message | 心跳消息 |  | 用于周期性报告系统进程或控制节点存活状态的消息。 |
| 11 | Watchdog Timer | 看门狗定时器 |  | 在软件或硬件未按时响应时触发故障处理的监控机制。 |
| 12 | Over-the-air Update | 空中软件更新 | OTA | 通过无线网络向车辆分发、验证和安装软件或配置的升级方式。 |
| 13 | Rollback Strategy | 升级回滚策略 |  | 当软件更新失效时将系统恢复至已验证版本的部署方案。 |
| 14 | Shadow Mode | 影子模式 |  | 让候选自动驾驶模型并行计算但不直接控制车辆、以便比较行为的评测方式。 |
| 15 | Canary Deployment | 金丝雀部署 |  | 先在少量受控车辆或场景启用新版本以监测问题的发布策略。 |
| 16 | Data Logging | 车端数据记录 |  | 按规定条件持续保存传感器、控制输出及事件元数据的过程。 |
| 17 | Event-triggered Logging | 事件触发日志 |  | 只在预定异常、接管或关键场景发生时重点保存相关数据的策略。 |
| 18 | Data Curation | 驾驶数据整理 |  | 对采集的驾驶数据去重、标注、质量检查和筛选的流程。 |
| 19 | Active Learning | 主动学习 |  | 利用模型不确定性或样本价值选择下一批人工标注数据的方法。 |
| 20 | Hard Case Mining | 困难场景挖掘 |  | 从大量记录中识别稀有、错误高发或模型不确定驾驶片段的技术。 |
| 21 | Data Flywheel | 数据闭环飞轮 |  | 用线上失败数据持续改进标注、训练、评测和部署的循环体系。 |
| 22 | Model Registry | 模型注册中心 |  | 集中管理模型版本、元数据、验证结果与发布状态的系统组件。 |
| 23 | Continuous Integration for ADS | 自动驾驶持续集成 |  | 自动执行驾驶软件构建、模块测试和数据一致性校验的工程流程。 |
| 24 | Continuous Validation | 持续验证 |  | 对新代码、模型或数据更新重复执行规定场景和安全相关检查的流程。 |
| 25 | Release Gate | 发布门禁 |  | 在车端部署前要求指定质量、安全和评测条件全部满足的控制点。 |

## 16 组核心概念辨析

| 对比主题 | 技术区别与适用条件 |
|---|---|
| ADAS 与 ADS | ADAS 主要向驾驶员提供驾驶辅助，具体监督责任随功能等级变化；ADS 在运行设计域内持续执行完整 DDT。不能把 L2 辅助驾驶等同于 L4 无人驾驶。 |
| SAE L2、L3 与 L4 | L2 要求驾驶员持续监督；L3 在规定条件下由系统执行 DDT、需要时要求后备用户响应；L4 在自身 ODD 内由系统承担适当后备响应，无需人工负责缓解风险。 |
| ODD 与 MRC | ODD 限定功能允许进入的环境条件；MRC 是系统通过后备行动尽可能降低风险后达到的状态，二者不属于同一分类层次。 |
| Sensor Fusion 的 Early、Late 与 BEV 融合 | 早期融合使用低层数据/特征，后期融合组合模块预测；BEV 融合先建立共同鸟瞰几何空间，仍需校准和时间对齐。 |
| Camera、LiDAR 与 Radar | 相机提供丰富纹理与语义，LiDAR 直接获取三维几何测距，雷达可直接提供径向速度信息；雨雾遮挡及分辨率限制因模态而异。 |
| 3D Detection 与 Occupancy Prediction | 3D 检测输出预设对象的边界框与类别；占据预测对空间网格是否被物体占用做密集估计，可覆盖未归入对象类别的障碍。 |
| Odometry、Localization 与 SLAM | 里程计积分相对运动并积累误差；定位利用外部地图或绝对观测锚定姿态；SLAM 在地图未知时联合估计位姿与地图。 |
| HD Map 与 Online Map | HD Map 保存预先构建且需维护的车道与交通语义；在线地图直接从当前观测估计局部几何，可能降低对预建地图的依赖。 |
| Trajectory Forecasting 与 Ego Planning | 预测估计他车/行人未来可能行为分布；自车规划选择满足路线、安全与动力学约束的候选动作，二者需协同而不可混为同一任务。 |
| Behavior Planning 与 Trajectory Planning | 行为规划选择变道、让行或停车等驾驶策略；轨迹规划进一步给出随时间变化的位置、速度和控制可行性。 |
| Path 与 Trajectory | 路径描述几何曲线，不自带时间；轨迹为每个状态指定时间，因此需要额外满足速度、加速度和执行器能力。 |
| ACC 与 AEB | ACC 正常工况下按设定车距/车速执行持续跟车控制；AEB 在碰撞风险高时触发减速或制动，两者目标与触发条件不同。 |
| TTC 与 THW | TTC 在指定相对运动假设下估计相撞时间；THW 用车距除以自车速度估计车头时距，不直接说明是否会碰撞。 |
| Open-loop 与 Closed-loop Driving Evaluation | 开环回放不让模型动作改变后续观测；闭环评测会模拟动作对交通状态的反馈，因此更能暴露轨迹偏差的累积和交互影响。 |
| ISO 26262 与 ISO 21448 SOTIF | ISO 26262 主要覆盖电气/电子系统故障相关功能安全；ISO 21448 针对预期功能不足和合理可预见误用带来的不合理风险，二者互补。 |
| Remote Assistance 与 Teleoperation | 远程协助可提供高层建议、路线或任务支持；远程驾驶操控直接控制车辆运动，需要单独定义操作者职责、通信安全及后备策略。 |

## 12 道中等难度技术面试题

### 面试 1：为什么 SAE L2 系统即使能同时转向与控速也不意味着驾驶员可以脱离监控？

**参考答案：**SAE 等级按 DDT 和持续监督及后备责任区分。L2 属驾驶员持续监督下的驾驶支持，只有满足适用 ODD 且符合更高等级职责分配的 ADS 才承担相应系统任务。

### 面试 2：为什么 ODD 验证不能只按行政地理围栏判断？

**参考答案：**ODD 可同时包含道路类别、气象、照度、交通复杂性、速度和传感器可用性。处于地理区域内也可能因暴雨、大雾或施工超出功能域。

### 面试 3：为什么 3D 感知系统需要外参与时间同步同时正确？

**参考答案：**不同传感器坐标不统一会产生空间偏移；时间未对齐会把运动中的不同瞬间观测错误组合，两者都可导致融合后的假目标或定位误差。

### 面试 4：LiDAR 与毫米波雷达在目标速度估计上有哪些互补？

**参考答案：**LiDAR 通常提供精细三维结构但需要多帧差分估速；FMCW 雷达能从多普勒获得径向速度，却有角分辨率和多径等局限。

### 面试 5：为什么在线占据预测不能完全替代目标级跟踪？

**参考答案：**Occupancy 能表征未知障碍空间占据，目标跟踪则维护身份、速度、类别及行为历史；规划通常需要密集空间和对象动态双重信息。

### 面试 6：为什么仅靠轮速积分的定位长期运行会漂移？

**参考答案：**轮胎打滑、半径标定误差、编码器噪声和方向模型误差在积分中持续累积，需要 GNSS、地图匹配或回环等外部约束。

### 面试 7：为何其他交通主体的运动预测通常应该输出多个可能未来？

**参考答案：**同一道路状态可能对应左转、直行、让行等多种意图，单一路径会掩盖决策不确定性，规划需要对不同模式的风险作保守评估。

### 面试 8：为什么 Frenet 坐标对车道内规划方便但在复杂路口可能受限？

**参考答案：**在清晰参考线附近纵向弧长和横向偏移易表达车道约束；路线分岔、交叉或大幅偏离参考线时投影可能不唯一或不稳定。

### 面试 9：MPC 在车辆控制中与简单 PID 有何主要差异？

**参考答案：**MPC 显式使用车辆模型、有限时间窗和输入或状态约束优化未来控制序列；PID 常根据局部误差产生控制，不直接优化整段未来可行轨迹。

### 面试 10：为什么仅靠固定 TTC 阈值难以保证安全？

**参考答案：**TTC 常假设当前相对速度保持不变，忽略目标加速度、侧向机动、道路附着和测量不确定性；安全决策应与可达集、制动能力及场景语义结合。

### 面试 11：为什么开放环路轨迹预测评分好不保证闭环驾驶好？

**参考答案：**学习策略在执行中会进入与离线日志不同的状态，单步位置误差无法充分反映交通互动、累积偏移和安全恢复能力。

### 面试 12：为什么 ISO 26262 认证或 SOTIF 文档都不能单独证明无人驾驶已达到零风险？

**参考答案：**标准提供系统化风险控制、验证与证据框架，不保证绝对安全；实际安全依赖具体 ODD、操作策略、硬件、软件及持续测试运营。

## 12 道中等难度考试题与参考解析

### 考试 1：自车与前车间距 36m，假定相对接近速度恒为 12m/s，简化 TTC 是多少？

**解析：**TTC=36/12=3s。若相对速度非正或有加速度，此简单定义需重新解释。

### 考试 2：跟车距离 24m，自车车速 12m/s，THW 是多少？

**解析：**THW=24/12=2s；它不等同于碰撞时间。

### 考试 3：车速 v=20m/s，在固定减速度 a=5m/s² 下理想制动距离是多少？

**解析：**d=v²/(2a)=400/10=40m，不包括系统或人的反应距离。

### 考试 4：上述车辆存在 1.5s 响应延迟且延迟期匀速运行，含延迟的总停止路程是多少？

**解析：**反应距离 20×1.5=30m，加制动距离 40m，总共约 70m。

### 考试 5：运动学自行车模型轴距 2.5m、车速 10m/s、前轮转角 0.1rad，近似横摆角速度是多少？

**解析：**ω=v tan(δ)/L=10×tan(0.1)/2.5≈0.401rad/s，忽略轮胎侧滑。

### 考试 6：某未来轨迹三处预测点位置误差分别为 1m、2m、3m，ADE 多少？

**解析：**ADE=(1+2+3)/3=2m，在等间隔同权采样下成立。

### 考试 7：预测终点与真实终点的二维偏差为 (3m,4m)，FDE 是多少？

**解析：**FDE=√(3²+4²)=5m。

### 考试 8：雷达每秒输出 20 帧，理想相邻输出间隔多少毫秒？

**解析：**1000/20=50ms，具体硬件和软件延迟还需单独统计。

### 考试 9：两个 3D 包围盒体积分别 8m³ 与 10m³，交集体积 4m³，3D IoU 是多少？

**解析：**IoU=4/(8+10−4)=4/14≈0.286。

### 考试 10：系统 100 次测试中有 92 次成功完成路线，任务成功率是多少？

**解析：**92/100=92%，还应报告有效场景分布及碰撞或违规事件。

### 考试 11：驾驶策略开环预测误差逐渐减小，但闭环碰撞率升高，是否可以直接发布？

**解析：**不能。应优先调查闭环分布偏移、交互与安全约束，满足发布门禁后才可考虑实际部署。

### 考试 12：自动驾驶功能在 ODD 外遭遇大雾，该如何从技术术语层面描述正确处理？

**解析：**应检测 ODD 退出，按系统等级和安全设计执行后备响应，必要时实施最小风险机动；不能继续假设感知和驾驶能力可靠。

## 技术标准、官方文档与学术资料

以下资源用于建立技术概念与版本背景；来源作者未参与本册逐条审稿，标准原文内容应以版权方正式版本为准。

1. [SAE J3016_202609 — Driving Automation Taxonomy (current revision September 2026)](https://saemobilus.sae.org/standards/j3016_202609-taxonomy-definitions-terms-related-driving-automation-systems-road-motor-vehicles)
2. [Autoware Documentation — Autonomous Driving Stack](https://docs.autoware.org/main/design/autoware-architecture-v2/)
3. [ASAM OpenDRIVE — Road Network Description Standard](https://www.asam.net/standards/detail/opendrive/)
4. [ASAM OpenSCENARIO V2.0.0 — Scenario Description Standard](https://www.asam.net/standards/detail/openscenario/v200/)
5. [CARLA Simulator — Official Website](https://carla.org/)
6. [CARLA 1.0 — November 2026 Release Notes](https://carla.org/2026/11/17/release-1.0/)
7. [ISO 26262-1:2018 — Functional Safety Vocabulary](https://www.iso.org/standard/68383.html)
8. [ISO 21448:2022 — Safety of the Intended Functionality](https://www.iso.org/standard/77490.html)
9. [Waymo Open Dataset](https://waymo.com/open/)
10. [nuScenes — Multimodal Autonomous Driving Dataset](https://www.nuscenes.org/)
11. [KITTI Vision Benchmark Suite](https://www.cvlibs.net/datasets/kitti/)
12. [Argoverse Dataset](https://www.argoverse.org/)
13. [Lanelet2 — High-definition Road Map Framework](https://github.com/fzi-forschungszentrum-informatik/Lanelet2)
14. [Mobileye RSS — On a Formal Model of Safe and Scalable Self-driving Cars](https://arxiv.org/abs/1708.06374)
15. [Autoware Foundation Repository](https://github.com/autowarefoundation/autoware)

## 构建与发布边界

- 原始章节：`data/autonomous-driving/chapters/*.tsv`，字段 `English|中文|abbr|definition`。
- 生成文件：`data/autonomous-driving.tsv`、`glossaries/autonomous-driving.md`、`pdf/autonomous-driving.pdf` 及 `docs/` 镜像。
- 确定性构建：`node scripts/render_autonomous_driving.mjs`；只读一致性检查：`node scripts/render_autonomous_driving.mjs --check`。
- 作为独立出版手册，不应在未接入网站搜索数据前改变现有索引学科数或术语总数；**500 条短定义不是 500 篇深度 Wiki**。
