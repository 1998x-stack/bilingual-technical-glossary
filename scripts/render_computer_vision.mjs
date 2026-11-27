#!/usr/bin/env node
// TERM / ATLAS — reproducible Computer Vision handbook publisher.
// node scripts/render_computer_vision.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["计算机视觉与图像处理","图像处理强调滤波、增强、恢复等像素变换；计算机视觉还要推断对象、几何、动作及场景语义，两者有交叉。"],["图像分辨率与实际空间分辨率","像素宽高反映离散采样规模；能分辨的实际细节还依赖镜头、传感器、光学模糊与物距。"],["相机内参与外参","内参 K 描述相机坐标到像素坐标的映射；外参 R、t 描述世界坐标与相机坐标的相对位姿。"],["仿射变换与单应变换","仿射保持平行直线；一般单应变换允许透视畸变，可映射不同视角下的同一平面。"],["形态学 Dilation 与卷积扩张率","形态学膨胀扩大前景或局部上界；卷积 dilation rate 扩大卷积核采样间隔，两者不能混为同一操作。"],["SIFT 与 ORB","SIFT 利用尺度空间及梯度直方图构造浮点描述子；ORB 结合 FAST 与旋转 BRIEF 输出紧凑二值描述子。"],["基础矩阵 F 与本质矩阵 E","F 描述像素坐标中的双视图对极约束；E 对应已标定相机的归一化坐标，包含相对旋转和平移方向。"],["单目深度与双目度量深度","单目预测常受绝对尺度不确定性限制；已知焦距和基线的校正双目可通过视差恢复度量深度。"],["CNN 与 ViT","CNN 的局部卷积和权重共享引入空间归纳偏置；ViT 利用 patch token 与注意力显式建模位置间关系。"],["两阶段与单阶段检测器","两阶段先获得候选区域再分类回归；单阶段直接在特征图或查询集合上预测，速度与质量需具体测量。"],["目标检测 IoU、AP 与 mAP","IoU 衡量单次框重叠；AP 概括某类检测在阈值变化下的精确率召回率；mAP 在类别及约定阈值上聚合 AP。"],["语义、实例与全景分割","语义分割为像素赋类别；实例分割区分同类的不同物体；全景分割同时覆盖全部像素并标注可数目标身份。"],["光流、视觉里程计与 SLAM","光流估计帧间像素表观运动；视觉里程计估计相机轨迹；SLAM 还要联合维护环境地图与全局一致性。"],["NeRF 与 3D Gaussian Splatting","NeRF 常通过连续场和射线体积分合成视角；3DGS 使用显式高斯基元和泼溅光栅化，性能与重建结果依场景而异。"],["CLIP 与可视化语言模型","CLIP 通过图文对比学习获得共享表示，适合检索和零样本分类；生成式 VLM 通常进一步融合视觉特征与语言解码能力。"],["模型精度、鲁棒性与安全性","离线准确率只描述某个样本分布；遮挡、分布外输入、隐私泄露及对抗干扰需单独测评与治理。"]];
const interviews=[["为什么图像 resize 前通常需要考虑抗混叠滤波？","下采样会降低采样率，未先抑制超出新奈奎斯特限制的高频纹理可能发生频谱混叠，使边缘和纹理产生虚假模式。"],["相机内参矩阵与外参各负责什么？","相机外参将世界点映射到相机坐标，内参把相机归一化投影映射为像素坐标，常写为 p~K[R|t]X。"],["为什么特征匹配后还要执行 RANSAC？","描述子最近邻包含误匹配，直接估计几何模型会受异常点影响；RANSAC 通过内点一致性选择较可靠的几何解释。"],["单目相机做 SfM 为什么常存在尺度歧义？","仅由投影几何无法区分整体场景与平移共同乘相同尺度后的解，需已知长度、IMU、深度或其他约束恢复米制尺度。"],["为什么语义分割 mIoU 高不意味着实例分割质量高？","mIoU 关注类别像素集合，即使两个相邻同类物体被合并也可能得高分；实例任务需要正确区分对象并匹配掩码。"],["如何解释 COCO AP 与 AP50 的差别？","COCO 主 AP 在 0.50 到 0.95 的多个 IoU 阈值上平均，AP50 只在 0.50 阈值下评估，因此 AP50 通常对定位精度要求较宽松。"],["什么情况下 CNN 在小数据集上可能比从零训练 ViT 更稳？","CNN 的局部归纳偏置和参数共享有助于有限样本学习；ViT 表现还受预训练、增强、模型规模与训练配置影响。"],["DETR 为什么引入集合预测和二分图匹配？","它把检测输出表示为固定数量对象查询的集合，通过一对一匹配分配训练目标，在原始设计中可减少传统锚框与 NMS 依赖。"],["NeRF 和 3DGS 在表示与渲染上的主要区别？","NeRF 多采用连续神经场及射线采样积分，3DGS 用显式可优化三维高斯投影和 alpha 合成；两者都依赖相机标定和多视图监督。"],["为什么把训练图像随机翻转时也要变换标注？","目标框、像素掩码、关键点及左右语义会随图像坐标变换而改变；只变图像不变标签会制造错误监督。"],["检测系统从 30 FPS 降到 10 FPS，应如何定位瓶颈？","拆分摄像头解码、预处理、模型推理、后处理、数据拷贝和显示阶段，比较 p50/p99 时延及设备利用率后优化主要耗时环节。"],["视觉语言模型给出的图片事实为什么仍需核对？","VLM 可受到训练偏差、分辨率和 OCR 限制，生成并不等于证据；应定位可见图像区域、检查文本数字并在高风险任务中人工审核。"]];
const exams=[["原图尺寸 1920×1080，等比例缩小到宽 640，输出高度应是多少？","缩放比为 640/1920=1/3，因此高度为 1080/3=360。"],["给定两个框 A=[0,0,4,4]、B=[2,2,6,6]，计算 IoU。","交集面积 2×2=4，两个框各 16；并集 16+16−4=28，IoU=4/28=1/7≈0.1429。"],["双目系统焦距 f=800 像素、基线 B=0.1 米、视差 d=40 像素，深度是多少？","Z=fB/d=800×0.1/40=2 米，要求已校正双目并采用相容坐标单位。"],["32×32 图像经 3×3 卷积，stride=1、padding=1、dilation=1，输出空间大小是多少？","按 floor((32+2−3)/1)+1=32，输出仍为 32×32。"],["640×480 三通道 uint8 图像未压缩像素数据多少字节？","640×480×3=921,600 字节，约 0.879 MiB，不计文件头与内存对齐。"],["分类数据有 200 张图，其中 160 张 Top-1 预测正确，Top-1 Accuracy？","160/200=0.8，即 80%。"],["某前景分割的 TP=80、FP=20、FN=40，Dice 系数是多少？","Dice=2TP/(2TP+FP+FN)=160/220≈0.7273。"],["某类别分割 TP=80、FP=20、FN=40，IoU 是多少？","IoU=TP/(TP+FP+FN)=80/140≈0.5714。"],["一张图分成 16×16 patch，输入为 224×224，每个 patch 不重叠，共多少视觉 token？","每轴 224/16=14，共 14×14=196 个 patch token；若额外使用 CLS token 则合计 197。"],["视频有 300 帧、帧率 30 FPS，持续时间是多少？","300/30=10 秒，忽略时间戳抖动与丢帧。"],["模型每张图平均推理 25 ms，完全串行、无其他开销时上限约多少 FPS？","1/0.025=40 FPS；完整管线通常还受前后处理和设备并发影响。"],["某检测器在 IoU 0.5 和 0.75 下 AP 分别为 0.70 与 0.50，能否宣称 COCO AP 是 0.60？","不能。COCO 主 AP 需从 0.50 到 0.95 共十个 IoU 阈值平均；仅两点均值不是该正式指标。"]];
const references=[["Szeliski, Computer Vision: Algorithms and Applications (2nd ed.)","https://link.springer.com/book/10.1007/978-3-030-34372-9"],["Stanford CS231n: Deep Learning for Computer Vision (2026)","https://cs231n.stanford.edu/2026/schedule.html"],["OpenCV Documentation","https://docs.opencv.org/4.x/"],["PyTorch Torchvision: Models and Pre-trained Weights","https://docs.pytorch.org/vision/stable/models.html"],["COCO: Detection Evaluation Metrics","https://cocodataset.org/dataset/detection-eval.htm"],["He et al., Deep Residual Learning for Image Recognition (2015)","https://arxiv.org/abs/1512.03385"],["Dosovitskiy et al., An Image Is Worth 16x16 Words (2020)","https://arxiv.org/abs/2010.11929"],["Carion et al., End-to-End Object Detection with Transformers (2020)","https://arxiv.org/abs/2005.12872"],["Kirillov et al., Segment Anything (2023)","https://arxiv.org/abs/2304.02643"],["Mildenhall et al., NeRF: Representing Scenes as Neural Radiance Fields (2020)","https://arxiv.org/abs/2003.08934"],["Kerbl et al., 3D Gaussian Splatting for Real-Time Radiance Field Rendering (2023)","https://arxiv.org/abs/2308.04079"],["Radford et al., Learning Transferable Visual Models from Natural Language Supervision (2021)","https://arxiv.org/abs/2103.00020"],["Ho et al., Denoising Diffusion Probabilistic Models (2020)","https://arxiv.org/abs/2006.11239"],["KITTI Vision Benchmark Suite","https://www.cvlibs.net/datasets/kitti/"],["ImageNet Project","https://www.image-net.org/"]];
function parseData(raws){let chapters=[],ch=null;for(const raw of raws)for(const l of raw.split(/\r?\n/)){if(!l)continue;if(l.startsWith("# ")){if(ch)chapters.push(ch);ch={n:chapters.length+1,title:l.slice(2),terms:[]};continue;}const p=l.split("|");if(!ch||p.length!==4)throw Error("Malformed CV record: "+l);ch.terms.push({en:p[0].trim(),zh:p[1].trim(),abbr:p[2].trim(),definition:p[3].trim()});}if(ch)chapters.push(ch);return chapters;}
function makeTsv(chapters){return "# Computer Vision | 计算机视觉\n# Canonical source: data/computer-vision/chapters/*.tsv; 20 chapters; 500 entries\n"+chapters.map(c=>`# ${String(c.n).padStart(2,"0")}. ${c.title}\n`+c.terms.map(t=>[t.en,t.zh,t.abbr,t.definition].join("|")).join("\n")).join("\n\n")+"\n";}
function makeMd(chapters){const o=["# 计算机视觉 · Computer Vision","","> TERM / ATLAS — Computer Vision Bilingual Technical Glossary | 计算机视觉专有名词中英文对照表","",
"**500 条双语专业术语 · 20 个章节 · 2026-11-27**","",
"覆盖视觉基础、摄像机成像、图像预处理、经典滤波与形态学、局部特征、几何与相机标定、立体视觉、SfM/SLAM、光流、CNN、ViT、自监督学习、检测分割、人体姿态、三维重建、NeRF/3DGS、生成模型、VLM、评测和生产系统。",
"",
"**定义边界：**不同视觉任务使用不同目标与指标；分类准确率、目标检测 AP、分割 mIoU、点云距离和重投影误差不可直接等同。具体算法与硬件能力需参考其论文及官方文档。","",
"**审核状态：**原始数据已进行字段、章节计数、英文主术语唯一性等程序化校验；独立专家逐条审稿、PDF 实际视觉验收及多平台兼容性核验仍需进行。","",
"## 章节目录","",...chapters.map(c=>`- ${String(c.n).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),"","---",""];
for(const c of chapters){o.push(`## ${String(c.n).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 专业定义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en} | ${t.zh} | ${t.abbr} | ${t.definition} |`),"");}
o.push("## 核心概念辨析","","| 概念对比 | 技术区别 |","|---|---|",...contrasts.map(x=>`| ${x[0]} | ${x[1]} |`),"","## 中等难度技术面试问答","");
interviews.forEach((x,i)=>o.push(`### 面试题 ${i+1}：${x[0]}`,"",`**参考答案：**${x[1]}`,""));
o.push("## 中等难度考试题与解析","");
exams.forEach((x,i)=>o.push(`### 考试题 ${i+1}：${x[0]}`,"",`**解析：**${x[1]}`,""));
o.push("## 经典教材、论文和官方技术资料","","以下参考资源用于明确技术定义和研究背景，不代表参考文献的作者已逐条审阅本册。","",...references.map((x,i)=>`${i+1}. [${x[0]}](${x[1]})`),"",
"## 构建与发布说明","","- 原始条目：`data/computer-vision/chapters/*.tsv`（`English|中文|abbr|definition`）。",
"- 生成资源：`data/computer-vision.tsv`、`glossaries/computer-vision.md`、`pdf/computer-vision.pdf` 及 `docs/` 对应镜像。",
"- 只读校验：`node scripts/render_computer_vision.mjs --check`。",
"- 本册是独立出版的 500 条简明术语，**尚未纳入网站搜索索引，也不是 500 篇长篇 Wiki**。");
return o.join("\n")+"\n";}
function toHex(s){let x="";for(let i=0;i<s.length;i++)x+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return x;}
function base64(s){const A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",out=[];for(let i=0;i<s.length;i+=3){const a=s.charCodeAt(i),b=i+1<s.length?s.charCodeAt(i+1):0,c=i+2<s.length?s.charCodeAt(i+2):0;out.push(A[a>>2],A[((a&3)<<4)|(b>>4)],i+1<s.length?A[((b&15)<<2)|(c>>6)]:"=",i+2<s.length?A[c&63]:"=");}return out.join("");}
function makePdf(cs){
 const W=595,H=842,L=48,R=547,pages=[];let ops=[],section="",y=0;
 const col=c=>c.join(" ")+" rg",rect=(x,b,w,h,c)=>ops.push(col(c),`${x} ${b} ${w} ${h} re f`);
 const line=b=>ops.push(".84 .87 .91 RG","0.5 w",`${L} ${b} m ${R} ${b} l S`);
 const draw=(x,b,s,z=10,c=[.1,.23,.35])=>ops.push(col(c),`BT /FC ${z} Tf 1 0 0 1 ${x.toFixed(1)} ${b.toFixed(1)} Tm <${toHex(String(s))}> Tj ET`);
 const width=(s,z)=>Array.from(String(s)).reduce((a,x)=>a+z*(x===" "?.32:x.charCodeAt(0)<128?(/[MWmw@]/.test(x)?.79:.54):1),0);
 const wrap=(s,z,max)=>{const a=[];let t="";for(const x of Array.from(String(s))){if(t&&width(t+x,z)>max){a.push(t);t=x}else t+=x;}if(t)a.push(t);return a;};
 function page(title="",cont=false){if(ops.length)pages.push(ops.join("\n")+"\n");ops=[];section=title;rect(0,0,W,H,[1,1,1]);rect(0,834,W,8,[.06,.20,.35]);draw(L,807,"TERM / ATLAS   ·   COMPUTER VISION",10,[.10,.27,.43]);line(792);if(title){draw(L,759,title+(cont?"（续）":""),14.4,[.07,.23,.37]);line(746);y=730;}else y=768;}
 function entry(i,t){const head=wrap(`${String(i).padStart(2,"0")}   ${t.en}  /  ${t.zh}${t.abbr?"  ["+t.abbr+"]":""}`,9.8,478),defs=wrap(t.definition,9.1,471),h=head.length*13.7+defs.length*12.6+15;if(y-h<63)page(section,true);if(i%2===0)rect(L-4,y-h+3,R-L+8,h+1,[.964,.974,.985]);let pos=y-13;for(const l of head){draw(L+3,pos,l,9.8,[.07,.21,.35]);pos-=13.7;}for(const l of defs){draw(L+14,pos,l,9.1,[.32,.39,.45]);pos-=12.6;}y-=h;}
 function para(s,z=9.3,indent=0,c=[.31,.39,.46]){const a=wrap(s,z,R-L-indent-8);if(y-a.length*(z+5)-9<61)page(section,true);for(const l of a){draw(L+indent,y,l,z,c);y-=z+5;}y-=9;}
 page();rect(0,624,W,176,[.06,.20,.35]);draw(L,746,"计算机视觉",29,[1,1,1]);draw(L,708,"Computer Vision",19,[.82,.91,.99]);draw(L,668,"500 条双语术语   ·   20 个知识章节",12,[1,1,1]);draw(L,598,"THE VISUAL INTELLIGENCE KNOWLEDGE MAP",10.5,[.11,.28,.43]);line(580);
 cs.forEach((c,i)=>draw(L+(i>=10?251:0),554-(i>=10?i-10:i)*26,`${String(c.n).padStart(2,"0")}   ${c.title}`,9.15,[.14,.29,.43]));
 draw(L,225,"成像 · 几何 · 感知 · 深度学习 · 三维 · 多模态",10,[.19,.34,.47]);draw(L,198,"原创简明释义、概念辨析与配套题解",9.4,[.28,.38,.46]);draw(L,103,"TERM / ATLAS  ·  2026-11-27",9.8,[.21,.35,.48]);
 for(const c of cs){page(`${String(c.n).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>entry(i+1,t));}
 page("附录 A · 核心概念辨析");contrasts.forEach((x,i)=>{if(y<124)page(section,true);para(`${i+1}. ${x[0]}`,10.3,0,[.08,.24,.37]);para(x[1],9.1,14);});
 page("附录 B · 中等难度面试题");interviews.forEach((x,i)=>{if(y<124)page(section,true);para(`Q${i+1}. ${x[0]}`,10.3,0,[.08,.24,.37]);para(`答：${x[1]}`,9.1,14);});
 page("附录 C · 中等难度考试题");exams.forEach((x,i)=>{if(y<124)page(section,true);para(`${i+1}. ${x[0]}`,10.3,0,[.08,.24,.37]);para(`解析：${x[1]}`,9.1,14);});
 page("附录 D · 教材、论文与技术来源");references.forEach((x,i)=>{para(`${i+1}. ${x[0]}`,9.7,0,[.09,.24,.38]);para(x[1],8.5,14);});para("所有术语定义及题解均为本项目独立概括，参考作者未参与专业审稿。",9.1);
 if(ops.length)pages.push(ops.join("\n")+"\n");
 const obj=[null];obj[1]="<< /Type /Catalog /Pages 2 0 R >>";obj[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${pages.map((_,i)=>`${6+2*i} 0 R`).join(" ")}] >>`;
 obj[3]="<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [<< /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 >>] /ToUnicode 4 0 R >>";
 const cmap="/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n/CMapName /Identity-UCS2 def\n/CMapType 2 def\n1 begincodespacerange\n<0000> <FFFF>\nendcodespacerange\n1 beginbfrange\n<0000> <FFFF> <0000>\nendbfrange\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n";
 obj[4]=`<< /Length ${cmap.length} >>\nstream\n${cmap}endstream`;
 obj[5]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
 for(let i=0;i<pages.length;i++){const pn=6+2*i,s=pn+1;let stream=pages[i]+".84 .87 .91 RG 0.5 w 48 52 m 547 52 l S\n";
 stream+=`${col([.40,.48,.55])} BT /FC 8 Tf 1 0 0 1 48 35 Tm <${toHex("TERM / ATLAS  ·  Computer Vision")}> Tj ET\n`;
 stream+=`${col([.40,.48,.55])} BT /FC 8 Tf 1 0 0 1 490 35 Tm <${toHex(`${i+1} / ${pages.length}`)}> Tj ET\n`;
 obj[pn]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Resources << /Font << /FC 3 0 R >> >> /Contents ${s} 0 R >>`;
 obj[s]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;}
 let pdf="%PDF-1.4\n%TERM-ATLAS\n",offs=[0];for(let i=1;i<obj.length;i++){offs[i]=pdf.length;pdf+=`${i} 0 obj\n${obj[i]}\nendobj\n`;}
 const xref=pdf.length;pdf+=`xref\n0 ${obj.length}\n0000000000 65535 f \n`;for(let i=1;i<obj.length;i++)pdf+=`${String(offs[i]).padStart(10,"0")} 00000 n \n`;
 pdf+=`trailer\n<< /Size ${obj.length} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;return {pdf,pages:pages.length};
}
const raw=Array.from({length:20},(_,i)=>fs.readFileSync(path.join(ROOT,"data/computer-vision/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const cs=parseData(raw),terms=cs.flatMap(c=>c.terms);
if(cs.length!==20||cs.some(c=>c.terms.length!==25)||terms.length!==500||new Set(terms.map(t=>t.en.toLowerCase())).size!==500||terms.some(t=>!t.en||!t.zh||!t.definition))throw Error("Expected 500 unique complete terms in 20 chapters");
const data=Buffer.from(makeTsv(cs),"utf8"),md=Buffer.from(makeMd(cs),"utf8"),pdf=Buffer.from(makePdf(cs).pdf,"ascii");
const outputs=[["data/computer-vision.tsv",data],["glossaries/computer-vision.md",md],["docs/glossaries/computer-vision.md",md],["pdf/computer-vision.pdf",pdf],["docs/pdf/computer-vision.pdf",pdf]];
const check=process.argv.includes("--check");
for(const [rel,buf] of outputs){const filename=path.join(ROOT,rel);if(check){if(!fs.existsSync(filename)||!fs.readFileSync(filename).equals(buf))throw Error("Not synchronized: "+rel);}else{fs.mkdirSync(path.dirname(filename),{recursive:true});fs.writeFileSync(filename,buf);}}
console.log((check?"PASS":"GENERATED")+": 500 terms, 20 chapters, "+outputs.length+" matching publications");
