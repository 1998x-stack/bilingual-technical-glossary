#!/usr/bin/env node
// TERM / ATLAS — deterministic Computer Graphics publisher. Node.js >= 18.
// node scripts/render_computer_graphics.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["Computer Graphics 与 Computer Vision","图形学根据几何、材质与光照合成图像；视觉从图像推断几何、类别和运动。两者在逆向渲染和神经重建中相互结合。"],["Rasterization 与 Ray Tracing","光栅化由基元投影到屏幕求覆盖；光追从射线与场景求交。两者可混合使用，不能简单断言其中一种总更快。"],["Object、World、View 与 Clip Space","局部模型坐标经模型矩阵到世界，经视图矩阵到相机，投影后到齐次裁剪空间，再经过透视除法得到 NDC。"],["透视除法与透视校正插值","透视除法把齐次坐标除以 w；属性透视校正插值则使用各顶点的逆 w 权重，避免屏幕线性插值失真。"],["Flat、Gouraud 与 Phong Shading","平面着色常每面一个法向；Gouraud 在顶点算光照再插值颜色；Phong 在片段插值法向再算光照。"],["BRDF 与 BSDF","BRDF 仅描述反射方向分布；BSDF 涵盖反射与透射。材质实现须注意相应测度、法向与能量约束。"],["Base Color 与 Albedo","Base Color 是材质工作流的可编辑参数；反照率有具体的辐射能量意义，两者在金属材质或不同着色模型中不必相同。"],["Radiance 与 Irradiance","辐亮度按投影面积与立体角定义、具方向性；辐照度对入射半球积分后按表面积度量。它们单位不同。"],["Direct 与 Indirect Lighting","直接光来自光源到表面的首段路径；间接光经历反弹或透射。AO 只近似局部遮蔽，不等于物理全局光照。"],["Path Tracing 与普通 Ray Casting","简单射线投射通常求第一可见交点；路径追踪通过随机反弹光路估计包含间接照明的渲染积分。"],["MSAA、FXAA 与 TAA","MSAA 增加几何覆盖采样；FXAA 用单帧后处理平滑边缘；TAA 复用历史采样但可能产生拖影。"],["Shadow Mapping 与 Ray-traced Shadows","阴影贴图从光源视角比较有限分辨率深度；射线阴影以几何求交判断遮挡，精度和成本取决于实现。"],["BVH 与 Uniform Grid","BVH 按嵌套包围体组织几何；均匀网格按规则空间单元索引基元。性能取决于场景空间分布和射线类型。"],["OpenGL 与 Vulkan","OpenGL 采用较多隐式状态管理；Vulkan 暴露资源、命令与同步细节以便显式控制，编码复杂度与性能不可一概而论。"],["Linear RGB 与 sRGB","光照合成和大部分物理颜色运算应在线性光数值上进行；sRGB 通常采用非线性编码，混合前需要明确转换。"],["NeRF 与 3D Gaussian Splatting","NeRF 以连续神经场及体积积分合成视角；3DGS 用显式三维高斯与投影合成。两者均需针对视角质量、内存和速度实测。"]];
const interviews=[["为什么 60 FPS 的真实帧时间预算不能把全部 16.67ms 都交给像素着色器？","CPU 更新、命令提交、顶点处理、几何、后处理及同步也占用帧时间。应先画出完整帧图并以 GPU 时间线定位耗时阶段。"],["模型到屏幕的 MVP 变换经过哪些坐标空间？","通常依次由对象空间经 Model 到世界、View 到相机、Projection 到齐次裁剪坐标；裁剪后除以 w 得到 NDC，再映射到视口。"],["为什么三角形纹理坐标不能简单按屏幕重心权重线性插值？","透视投影不是仿射映射，必须用各顶点属性除以 w 的加权结果再除以逆 w 权重和，才能恢复正确纹理透视关系。"],["为什么在线性 RGB 与 sRGB 编码值上进行相同 Alpha 混合可能输出不同颜色？","sRGB 对线性光值执行非线性编码。物理混色应先转回线性光域，再混合、再执行显示编码，否则会产生亮度偏差。"],["BRDF 为什么需要满足非负性、能量守恒与可能的互易性？","这些约束避免负散射、无源材料输出超过入射能量，并在常见非磁性线性介质条件下满足光路互易物理规律。"],["为什么路径追踪只有 1 spp 时容易产生明显噪声？","蒙特卡洛估计方差随样本量降低而减小，少量样本难覆盖高贡献光路；重要性采样和 MIS 可有效降低方差。"],["为什么 AO 不能代替全局光照？","AO 主要衡量局部几何遮挡，不显式模拟完整入射辐射和不同表面之间的能量交换，无法正确重现颜色渗透等效果。"],["在动态场景中 BVH 应完全重建还是 Refit？","若仅顶点或实例变换小幅变化，Refit 可便宜更新包围盒；若拓扑或空间重叠严重恶化，重建可能获得更优遍历成本。"],["Vulkan 的管线屏障与信号量主要区别是什么？","管线屏障描述设备操作间的阶段和内存依赖；信号量常用于队列间或提交间同步，二者的适用范围取决于 Vulkan 版本和同步 API。"],["TAA 的历史重投影为何容易产生拖影？","运动向量、遮挡显露和历史有效性检测不准时会把过去帧的错误颜色累积到当前位置，需限制或重置历史。"],["为什么延迟渲染并不总适合透明对象？","G-buffer 通常每像素只保留一个可见表面材质状态，难以正确处理多层透明与顺序混合，常结合前向透明通道。"],["NeRF 与 3DGS 在数据结构和渲染算法上如何区分？","NeRF 多查询连续密度与外观并进行沿射线积分；3DGS 优化显式高斯基元并投影混合。比较需固定输入视图和画质目标。"]];
const exams=[["目标帧率为 60 FPS，单帧时间预算是多少毫秒？","1000/60≈16.67 ms。若系统有呈现与同步开销，渲染阶段可用时间更少。"],["一张 RGBA8、1024×1024 纹理在不含 mipmap 与压缩时需要多少 MiB？","1024×1024×4 字节=4,194,304 字节=4 MiB。"],["一张 512×512 RGBA8 纹理保留完整 mipmap 链，理想总容量大约多少 MiB？","基础层是 1 MiB，所有层近似乘以 4/3，因此约为 1.333 MiB，忽略额外对齐。"],["向量 n=(0,0,1)、光线方向 l=(0,0,1)，Lambert 余弦因子是多少？","max(0,n·l)=1；需假设两向量均已单位化。"],["两向量 a=(1,0,0)、b=(0,1,0) 的点积与夹角是多少？","a·b=0，且两者单位化，所以夹角为 90°。"],["深度测试中两个几乎重合面出现闪烁，属于什么典型现象？如何减轻？","Z-fighting。可改善 near/far 配置、采用 Reversed-Z、适当的深度偏移或避免共面几何。"],["纹理长宽各从 1024 降至 256，未压缩每像素大小不变时基础层数据量缩小多少倍？","每轴缩小 4 倍，面积缩小 4×4=16 倍。"],["简单蒙特卡洛估计，f(x)=2、采样 pdf(x)=0.5，则该样本对积分估计贡献是多少？","单样本贡献 f(x)/p(x)=2/0.5=4，需保证所选测度和支持集适用。"],["某 2560×1440 渲染目标采用 RGBA16F，每个像素 8 字节，未计 MSAA 时多少 MiB？","2560×1440×8=29,491,200 字节≈28.125 MiB。"],["一帧的 Geometry、Lighting、Postprocessing 各耗时 4、6、3 ms，完全串行总时间是多少？","4+6+3=13 ms，理论渲染阶段吞吐约 76.9 FPS；还需考虑 CPU、同步和呈现。"],["采样 4 spp 相比 1 spp，独立同分布蒙特卡洛估计的标准差理想缩小到多少？","在方差有限且样本独立时，标准差按 1/√N 缩放，因此缩小到 1/2；不是误差降至 1/4。"],["一个网格 10,000 个三角形，每三角形独立存 3 个 32 位索引，总索引数据多少字节？","10,000×3×4=120,000 字节，约 117.19 KiB。"]];
const refs=[["Pharr, Jakob & Humphreys, Physically Based Rendering (4th edition)","https://pbr-book.org/4ed/contents"],["Scratchapixel — Computer Graphics and Ray Tracing","https://www.scratchapixel.com/"],["Khronos Vulkan Specification","https://docs.vulkan.org/spec/latest/"],["Khronos OpenGL Reference Documentation","https://www.khronos.org/opengl/wiki/"],["Khronos glTF 2.0 Specification","https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html"],["Microsoft Direct3D 12 Graphics Documentation","https://learn.microsoft.com/en-us/windows/win32/direct3d12/direct3d-12-graphics"],["Apple Metal Documentation","https://developer.apple.com/metal/"],["OpenUSD Documentation","https://openusd.org/release/index.html"],["NVIDIA OptiX Programming Guide","https://raytracing-docs.nvidia.com/optix8/guide/index.html"],["RenderDoc Graphics Debugger","https://renderdoc.org/"],["Blender Manual","https://docs.blender.org/manual/en/latest/"],["SIGGRAPH Course: Real-Time Rendering Resources","https://www.realtimerendering.com/"],["Mildenhall et al. (2020), NeRF: Representing Scenes as Neural Radiance Fields","https://arxiv.org/abs/2003.08934"],["Kerbl et al. (2023), 3D Gaussian Splatting for Real-Time Radiance Field Rendering","https://arxiv.org/abs/2308.04079"],["Müller et al. (2022), Instant Neural Graphics Primitives","https://nvlabs.github.io/instant-ngp/"]];
function parseData(raws){const chapters=[];let ch=null;for(const raw of raws)for(const line of raw.split(/\r?\n/)){if(!line)continue;if(line.startsWith("# ")){if(ch)chapters.push(ch);ch={n:chapters.length+1,title:line.slice(2),terms:[]};continue;}const p=line.split("|");if(!ch||p.length!==4)throw Error("Malformed source: "+line);ch.terms.push({en:p[0].trim(),zh:p[1].trim(),abbr:p[2].trim(),definition:p[3].trim()});}if(ch)chapters.push(ch);return chapters;}
function makeTsv(chapters){return "# Computer Graphics | 计算机图形学\n# Canonical source: data/computer-graphics/chapters/01.tsv ... 20.tsv\n"+chapters.map(c=>`# ${String(c.n).padStart(2,"0")}. ${c.title}\n`+c.terms.map(t=>[t.en,t.zh,t.abbr,t.definition].join("|")).join("\n")).join("\n\n")+"\n";}
function makeMd(chapters){
const out=["# 计算机图形学 · Computer Graphics","","> TERM / ATLAS · 专业中英文术语手册 | Bilingual Technical Glossary","",
"**500 条中英文术语 · 20 个专业章节 · 2026-11-27**","",
"本册覆盖计算机图形学基础、空间变换、几何建模、光栅化、纹理、PBR 材质、光传输、蒙特卡洛路径追踪、全局光照、动画与仿真、OpenGL/Vulkan/Metal、GPU 着色器、BVH 加速结构、实时渲染优化、NeRF 与 3D Gaussian Splatting。",
"",
"**重要约定：**相机坐标系、矩阵乘法顺序、左右手系、NDC 深度范围、颜色传递函数与 API 同步行为存在具体平台差异。公式及实现细节应以使用的 API 版本与官方规范为准。",
"",
"**编辑状态：**20 章和英文术语去重经过结构化检查；未声称独立专家完成逐条审稿或跨阅读器 PDF 视觉与无障碍验收。",
"",
"## 章节目录","",...chapters.map(c=>`- ${String(c.n).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),"","---",""];
for(const c of chapters)out.push(`## ${String(c.n).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 核心定义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en} | ${t.zh} | ${t.abbr} | ${t.definition} |`),"");
out.push("## 16 组专业概念辨析","","| 对比概念 | 技术区别与边界 |","|---|---|",...contrasts.map(x=>`| ${x[0]} | ${x[1]} |`),"","## 中等难度面试问答","");
interviews.forEach((x,i)=>out.push(`### 面试题 ${i+1}：${x[0]}`,"",`**参考答案：**${x[1]}`,""));
out.push("## 中等难度考试题与解析","");
exams.forEach((x,i)=>out.push(`### 考试题 ${i+1}：${x[0]}`,"",`**解析：**${x[1]}`,""));
out.push("## 经典教材、API 规范与原始论文","","以下资料用于确认概念背景和研究来源，不表示作者参与或认可本项目所有具体定义。","",...refs.map((r,i)=>`${i+1}. [${r[0]}](${r[1]})`),"",
"## 出版与维护说明","","- 原始数据：`data/computer-graphics/chapters/*.tsv`，每行 `English|中文|abbr|definition`。","- 生成文件：`data/computer-graphics.tsv`、`glossaries/computer-graphics.md`、`pdf/computer-graphics.pdf`，及相同内容的 `docs/` 镜像。","- 可复现构建：`node scripts/render_computer_graphics.mjs`，只读校验：`node scripts/render_computer_graphics.mjs --check`。","- **本册是独立出版的简明术语表，尚未接入网站正式搜索索引，亦非 500 篇专家审稿的深度 Wiki。**");
return out.join("\n")+"\n";}
function toHex(s){let v="";for(let i=0;i<s.length;i++)v+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return v;}
function base64(s){const A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",r=[];for(let i=0;i<s.length;i+=3){const a=s.charCodeAt(i),b=i+1<s.length?s.charCodeAt(i+1):0,c=i+2<s.length?s.charCodeAt(i+2):0;r.push(A[a>>2],A[((a&3)<<4)|(b>>4)],i+1<s.length?A[((b&15)<<2)|(c>>6)]:"=",i+2<s.length?A[c&63]:"=");}return r.join("");}
function makePdf(chapters){
const W=595,H=842,L=47,R=548,pages=[];let ops=[],section="",y=0;
const color=c=>c.join(" ")+" rg";
const rect=(x,b,w,h,c)=>ops.push(color(c),`${x} ${b} ${w} ${h} re f`);
const line=b=>ops.push(".84 .87 .91 RG","0.5 w",`${L} ${b} m ${R} ${b} l S`);
const draw=(x,b,s,size=10,c=[.1,.23,.36])=>ops.push(color(c),`BT /FC ${size} Tf 1 0 0 1 ${x.toFixed(1)} ${b.toFixed(1)} Tm <${toHex(String(s))}> Tj ET`);
const width=(s,z)=>Array.from(String(s)).reduce((n,ch)=>n+z*(ch===" "?.33:ch.charCodeAt(0)<128?(/[MWmw@]/.test(ch)?.81:.56):1),0);
const wrap=(s,z,max)=>{const a=[];let buf="";for(const c of Array.from(String(s))){if(buf&&width(buf+c,z)>max){a.push(buf);buf=c;}else buf+=c;}if(buf)a.push(buf);return a;};
function page(title="",cont=false){if(ops.length)pages.push(ops.join("\n")+"\n");ops=[];section=title;rect(0,0,W,H,[1,1,1]);rect(0,834,W,8,[.07,.19,.34]);draw(L,808,"TERM / ATLAS  ·  COMPUTER GRAPHICS",9.8,[.1,.26,.42]);line(792);if(title){const headings=wrap(title+(cont?"（续）":""),14.2,496);for(let i=0;i<headings.length;i++)draw(L,760-i*17,headings[i],14.2,[.08,.24,.37]);const sep=746-17*(headings.length-1);line(sep);y=sep-16;}else y=767;}
function entry(i,t){const head=wrap(`${String(i).padStart(2,"0")}   ${t.en}  /  ${t.zh}${t.abbr?"   ["+t.abbr+"]":""}`,9.8,478),def=wrap(t.definition,9.15,474),h=head.length*13.9+def.length*12.8+15;if(y-h<62)page(section,true);if(i%2===0)rect(L-4,y-h+2,R-L+8,h+2,[.966,.976,.985]);let pos=y-13;for(const a of head){draw(L+3,pos,a,9.8,[.07,.22,.36]);pos-=13.9;}for(const a of def){draw(L+15,pos,a,9.15,[.31,.4,.47]);pos-=12.8;}y-=h;}
function para(s,z=9.2,indent=0,c=[.29,.39,.47]){const a=wrap(s,z,R-L-indent-8);if(y-a.length*(z+5)-9<62)page(section,true);for(const l of a){draw(L+indent,y,l,z,c);y-=z+5;}y-=9;}
page();rect(0,625,W,173,[.07,.19,.34]);draw(L,744,"计算机图形学",29,[1,1,1]);draw(L,704,"Computer Graphics",19,[.82,.92,.99]);draw(L,666,"500 条中英术语    ·    20 个专业章节",12,[1,1,1]);draw(L,593,"THE GRAPHICS & RENDERING KNOWLEDGE MAP",10.4,[.12,.28,.43]);line(577);
chapters.forEach((c,i)=>draw(L+(i>=10?252:0),552-(i>=10?i-10:i)*25.2,`${String(c.n).padStart(2,"0")}  ${c.title}`,9.1,[.13,.3,.43]));
draw(L,226,"几何 · 光照 · 渲染 · GPU · 动画 · 神经图形",10,[.19,.34,.47]);draw(L,198,"源数据可校验；独立技术审稿和阅读器验收另行进行",9.25,[.29,.39,.47]);draw(L,102,"TERM / ATLAS   2026-11-27",9.8,[.22,.36,.48]);
for(const c of chapters){page(`${String(c.n).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>entry(i+1,t));}
page("附录 A · 核心概念辨析");contrasts.forEach((x,i)=>{if(y<128)page(section,true);para(`${i+1}. ${x[0]}`,10.3,0,[.08,.24,.38]);para(x[1],9.2,13);});
page("附录 B · 中等难度面试问答");interviews.forEach((x,i)=>{if(y<128)page(section,true);para(`Q${i+1}. ${x[0]}`,10.3,0,[.08,.24,.38]);para(`答：${x[1]}`,9.2,13);});
page("附录 C · 中等难度考试题");exams.forEach((x,i)=>{if(y<128)page(section,true);para(`${i+1}. ${x[0]}`,10.3,0,[.08,.24,.38]);para(`解析：${x[1]}`,9.2,13);});
page("附录 D · 教材、规范与技术来源");refs.forEach((x,i)=>{para(`${i+1}. ${x[0]}`,9.7,0,[.08,.24,.38]);para(x[1],8.6,13);});para("本手册为独立编写的教育性术语概述，引用不代表任何源作者参与审稿。",9.2);
if(ops.length)pages.push(ops.join("\n")+"\n");
const obj=[null];obj[1]="<< /Type /Catalog /Pages 2 0 R >>";obj[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${pages.map((_,i)=>`${6+2*i} 0 R`).join(" ")}] >>`;
obj[3]="<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [<< /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 >>] /ToUnicode 4 0 R >>";
const cmap="/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n/CMapName /Identity-UCS2 def\n/CMapType 2 def\n1 begincodespacerange\n<0000> <FFFF>\nendcodespacerange\n1 beginbfrange\n<0000> <FFFF> <0000>\nendbfrange\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n";
obj[4]=`<< /Length ${cmap.length} >>\nstream\n${cmap}endstream`;
obj[5]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
for(let i=0;i<pages.length;i++){const p=6+2*i,s=p+1;let stream=pages[i]+".84 .87 .91 RG 0.5 w 47 52 m 548 52 l S\n";
stream+=`${color([.4,.48,.55])} BT /FC 8 Tf 1 0 0 1 47 35 Tm <${toHex("TERM / ATLAS  ·  Computer Graphics")}> Tj ET\n`;
stream+=`${color([.4,.48,.55])} BT /FC 8 Tf 1 0 0 1 490 35 Tm <${toHex(`${i+1} / ${pages.length}`)}> Tj ET\n`;
obj[p]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Resources << /Font << /FC 3 0 R >> >> /Contents ${s} 0 R >>`;
obj[s]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;}
let pdf="%PDF-1.4\n%TERM-ATLAS\n",offset=[0];for(let i=1;i<obj.length;i++){offset[i]=pdf.length;pdf+=`${i} 0 obj\n${obj[i]}\nendobj\n`;}
const xref=pdf.length;pdf+=`xref\n0 ${obj.length}\n0000000000 65535 f \n`;for(let i=1;i<obj.length;i++)pdf+=`${String(offset[i]).padStart(10,"0")} 00000 n \n`;
pdf+=`trailer\n<< /Size ${obj.length} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;return {pdf,pages:pages.length};
}
const raw=Array.from({length:20},(_,i)=>fs.readFileSync(path.join(ROOT,"data/computer-graphics/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const cs=parseData(raw),terms=cs.flatMap(c=>c.terms);
if(cs.length!==20||cs.some(c=>c.terms.length!==25)||terms.length!==500||new Set(terms.map(x=>x.en.toLowerCase())).size!==500||terms.some(x=>!x.en||!x.zh||!x.definition))throw Error("Expected 20 chapters and 500 unique complete terms");
const data=Buffer.from(makeTsv(cs),"utf8"),md=Buffer.from(makeMd(cs),"utf8"),pdf=Buffer.from(makePdf(cs).pdf,"ascii");
const outputs=[["data/computer-graphics.tsv",data],["glossaries/computer-graphics.md",md],["docs/glossaries/computer-graphics.md",md],["pdf/computer-graphics.pdf",pdf],["docs/pdf/computer-graphics.pdf",pdf]];
const check=process.argv.includes("--check");
for(const [relative,bytes] of outputs){const file=path.join(ROOT,relative);if(check){if(!fs.existsSync(file)||!fs.readFileSync(file).equals(bytes))throw Error("Out-of-sync artifact: "+relative);}else{fs.mkdirSync(path.dirname(file),{recursive:true});fs.writeFileSync(file,bytes);}}
console.log((check?"PASS":"GENERATED")+": 500 terms, 20 chapters, "+outputs.length+" matching artifacts");
