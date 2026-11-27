#!/usr/bin/env node
// TERM / ATLAS reproducible CUDA standalone publisher. Node.js >= 18.
// Usage: node scripts/render_cuda.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["CUDA Thread、Warp 与 Thread Block","Thread 是逻辑执行实例；warp 通常由 32 条相邻线程组成；block 是可共享内存并执行块内同步的线程集合，三者不是同一调度层级。"],["SM、CUDA Core 与 Tensor Core","SM 是包含多类计算单元与片上资源的硬件执行单元；CUDA Core 面向部分标量算术；Tensor Core 主要加速特定矩阵运算。"],["Global、Local 与 Shared Memory","global 具有设备级可寻址语义；local 为线程私有但通常位于设备 DRAM；shared 为块内协作的片上存储。"],["Occupancy 与 GPU 利用率","occupancy 衡量驻留 warp 相对硬件上限的比例，不等于有用算术吞吐；高占用率并非所有 Kernel 的最优目标。"],["__syncthreads() 与 __syncwarp()","前者协调整个线程块中的合法参与线程，后者针对显式掩码指定的 warp 成员；不能任意互相替代。"],["原子操作与内存栅栏","原子操作为指定位置提供不可分割的操作及所选顺序语义；内存栅栏约束其他访存的可见顺序，本身不充当线程屏障。"],["cudaMemcpy 与 cudaMemcpyAsync","两者的主机阻塞与设备流行为取决于传输方向、存储类型及使用模式；Async 名称并不保证传输与计算一定重叠。"],["Pinned Memory 与 Unified Memory","pinned 是不可换出的主机页，常支持高效 DMA；Unified Memory 允许 CPU/GPU 协同访问托管数据并由运行时处理迁移。"],["Stream 与 CUDA Graph","Stream 为线性有序任务提交序列；Graph 显式声明节点依赖以复用调度结构并降低重复发射开销。"],["PTX、SASS 与 Cubin","PTX 是虚拟设备指令表示，SASS 是具体 GPU 机器指令；cubin 包含目标架构已编译的设备代码。"],["FP16、BF16、TF32 与 FP32","它们的指数位与尾数精度不同，TF32 尤其是特定 Tensor Core 计算模式而非通用 32 位存储数据类型的同义词。"],["Memory Coalescing 与 Bank Conflict","coalescing 针对 warp 的全局访存事务效率；bank conflict 针对共享内存存储体竞争，优化对象不同。"],["cudaMalloc 与 cudaMallocAsync","前者执行普通设备分配；后者把内存分配与流顺序关联并可由内存池复用资源，正确性依赖分配使用与释放的顺序。"],["Nsight Systems 与 Nsight Compute","Nsight Systems 观察端到端 CPU/GPU 时序与并发，Nsight Compute 深入分析单个 Kernel 的硬件指标与执行瓶颈。"]];
const interviews=[["为何将线程块大小设为 1024 不一定比 256 更快？","更大块可能因寄存器、共享内存和驻留块数限制降低并发；还需考虑工作量、边界浪费和硬件延迟隐藏，必须基于真实负载测量。"],["同一 warp 的线程访问连续 float 数组为什么往往更高效？","相邻 lane 的地址若对齐且集中，可通过较少内存事务服务更多有效字节；具体事务粒度依 GPU 架构。"],["Shared Memory 的访问一定比 Global Memory 快吗？","不一定。shared 需要数据搬运与同步，也可能出现 bank 冲突；当数据复用不足或占用率降低时总时间反而增加。"],["为什么 cudaMemcpyAsync 不总能与计算重叠？","取决于是否使用支持的主机内存、不同流的依赖、GPU 复制引擎及设备能力；同流顺序或隐式同步也会阻止重叠。"],["如何判断一个 Kernel 是计算瓶颈还是访存瓶颈？","用 Nsight Compute 分析相关吞吐与停顿，结合 Roofline 的算术强度、峰值内存带宽和计算吞吐估计性能上界。"],["为什么原子加法不能替代 __syncthreads()？","原子加只保护指定地址的读改写操作，不表示全部线程已完成其他写入；块内阶段性协作需要适当屏障或明确同步协议。"],["为什么寄存器溢出会影响 CUDA Kernel 性能？","溢出临时值通常转到 local memory，该空间一般经设备 DRAM 与缓存访问，可能增加额外访存并影响吞吐。"],["CUDA Graph 适用于哪类工作负载？","重复提交结构相似且任务依赖稳定的多 Kernel 工作流，可减少主机启动开销；需要处理图更新和捕获限制。"],["如果换成新 Embedding 或矩阵数据类型，CUDA 精度正确性怎样验证？","建立高精度参考结果、误差容忍度和输入边界测试，记录混合精度、归约次序和硬件架构；不能只依赖 bitwise 相等。"],["设备端发生非法访问却在下一次 API 调用才报错，为什么？","CUDA 工作通常异步提交，设备执行错误可能延迟到同步或后续 Runtime API 被检查时才向主机报告。"]];
const exams=[["一维网格 80 个 block、每 block 256 个线程，理论总线程数是多少？","80×256=20,480 个线程。实际只有通过边界判断且被分配数据的线程会执行有效工作。"],["对于 n=1,000,000、每 block 256 线程，使用向上取整启动至少需要多少个 block？","ceil(1,000,000/256)=3,907 个 block；网格可能包含 3,907×256=1,000,192 个线程。"],["一个 block 共有 256 个线程，warp size 为 32，包含多少个 warp？","256/32=8 个 warp。"],["每个 block 占用 48 KiB shared memory，SM 可用于此资源的预算为 96 KiB，单由这一资源最多驻留几个 block？","floor(96/48)=2 个；实际还受寄存器、线程数量和架构驻留块上限约束。"],["访存 Kernel 处理 1 GiB 有效数据，耗时 20 ms，有效带宽约是多少？","1 GiB/0.02 s≈53.69 GB/s（十进制 GB/s），需说明字节单位及读写总量假设。"],["一段 Kernel 进行 4×10^9 次 FLOP，搬运 2×10^9 字节，其算术强度是多少？","I=4×10^9/2×10^9=2 FLOP/byte。"],["某 Kernel 运行 5 ms，CUDA Graph 优化后 4 ms，吞吐相同，速度提升倍数是多少？","5/4=1.25×；运行时间缩短 20%。"],["对于 3,200 个元素、128 线程/block、grid-stride 循环，不考虑循环体，至少需要几个 block 覆盖每个元素一次？","ceil(3,200/128)=25；但 grid-stride 也允许更少 block 通过多次迭代处理全部元素。"],["某 warp 中 32 个线程各计算一份浮点结果，并共同累加到一个全局位置，应使用什么避免数据竞争？","可以使用与该类型和架构兼容的原子累加，或先 warp/block 归约再由一个线程执行原子更新。"],["一个 GPU 上同时运行两个流，是否可以直接断言两个 Kernel 一定并行执行？","不能。流允许潜在并发，但实际重叠还取决于资源、依赖、隐式同步及调度机制。"]];
const references=[["NVIDIA CUDA C++ Programming Guide","https://docs.nvidia.com/cuda/cuda-c-programming-guide/"],["NVIDIA CUDA C++ Best Practices Guide","https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/"],["CUDA Runtime API Reference","https://docs.nvidia.com/cuda/cuda-runtime-api/"],["CUDA Driver API Reference","https://docs.nvidia.com/cuda/cuda-driver-api/"],["Parallel Thread Execution ISA","https://docs.nvidia.com/cuda/parallel-thread-execution/"],["Nsight Compute Profiling Guide","https://docs.nvidia.com/nsight-compute/ProfilingGuide/"],["Nsight Systems Documentation","https://docs.nvidia.com/nsight-systems/"],["Compute Sanitizer Documentation","https://docs.nvidia.com/compute-sanitizer/"],["NVIDIA CUDA Libraries","https://developer.nvidia.com/gpu-accelerated-libraries"],["NCCL User Guide","https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/"],["NVIDIA CUTLASS Documentation","https://docs.nvidia.com/cutlass/"],["NVIDIA CUDA Compatibility Guide","https://docs.nvidia.com/deploy/cuda-compatibility/"]];
function parseData(raws){let cs=[],c=null;for(const raw of raws)for(const l of raw.split(/\r?\n/)){if(!l)continue;if(l.startsWith("# ")){if(c)cs.push(c);c={n:cs.length+1,title:l.slice(2),terms:[]};continue;}const p=l.split("|");if(p.length!==4||!c)throw Error("Malformed source: "+l);c.terms.push({en:p[0].trim(),zh:p[1].trim(),abbr:p[2].trim(),definition:p[3].trim()});}if(c)cs.push(c);return cs;}
function makeTsv(cs){return "# CUDA · NVIDIA CUDA Programming and Optimization\n# Source of truth: data/cuda/chapters/01.tsv ... 16.tsv\n"+cs.map(c=>`# ${String(c.n).padStart(2,"0")}. ${c.title}\n`+c.terms.map(t=>[t.en,t.zh,t.abbr,t.definition].join("|")).join("\n")).join("\n\n")+"\n";}
function makeMd(cs){
 const lines=["# CUDA 专有名词中英文对照表","",
 "> CUDA · Bilingual Technical Glossary | NVIDIA GPU 并行编程与优化",
 "",
 "**400 条专业术语 · 16 个章节 · 2026-11-27**","",
 "本册面向 CUDA 开发工程师、GPU Kernel 优化、AI Infra、HPC 和计算机体系结构学习者。涵盖线程层次、Kernel、内存模型、同步、Stream、CUDA Graph、性能建模、浮点精度、编译链路、CUDA API、数值库、Nsight 和多 GPU。",
 "",
 "**适用条件：**具体 API、硬件能力、精度模式、线程块集群和内存排序语义随 CUDA Toolkit 与 GPU 计算能力而变化；请以正在使用版本的 NVIDIA 官方文档为准。",
 "",
 "**审稿状态：**已检查结构、章节数量及英文主术语重复，尚未声称通过独立专家逐条审稿或所有 GPU 架构上的实验验证。",
 "",
 "## 目录","",...cs.map(c=>`- ${String(c.n).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),"","---",""];
 for(const c of cs){lines.push(`## ${String(c.n).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 核心定义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en.replace(/\|/g,"\\|")} | ${t.zh} | ${t.abbr.replace(/\|/g,"\\|")} | ${t.definition} |`),"");}
 lines.push("## 关键概念辨析","","| 对比主题 | 技术要点 |","|---|---|",...contrasts.map(x=>`| ${x[0]} | ${x[1]} |`),"","## 中等难度技术面试题","","以下回答为可追溯的答题思路，具体实现仍以计算能力、运行时和设备指标为准。","");
 interviews.forEach((x,i)=>lines.push(`### 面试 ${i+1}：${x[0]}`,"",`**参考答案：**${x[1]}`,""));
 lines.push("## 中等难度考试题与解析","");
 exams.forEach((x,i)=>lines.push(`### 考试 ${i+1}：${x[0]}`,"",`**解析：**${x[1]}`,""));
 lines.push("## NVIDIA 官方技术来源","","参考资料以 NVIDIA 官方指南、API 参考和工具文档为主，链接并不表示 NVIDIA 参与审稿或对全部译名作出认可。","",...references.map((x,i)=>`${i+1}. [${x[0]}](${x[1]})`),"",
 "## 版本、审稿与维护","","- Canonical source：`data/cuda/chapters/*.tsv`，字段为 `English|中文|abbr|definition`。","- 编译输出：`data/cuda.tsv`、`glossaries/cuda.md`、`pdf/cuda.pdf` 及对应 `docs/` 镜像。","- 单学科可复现校验：`node scripts/render_cuda.mjs --check`。","- 本册为独立出版的中英术语手册，**尚未纳入全站搜索索引**，不代表 400 篇深度 Wiki。");
 return lines.join("\n")+"\n";
}
function toHex(s){let h="";for(let i=0;i<s.length;i++)h+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return h;}
function base64(s){const A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",out=[];for(let i=0;i<s.length;i+=3){const a=s.charCodeAt(i),b=i+1<s.length?s.charCodeAt(i+1):0,c=i+2<s.length?s.charCodeAt(i+2):0;out.push(A[a>>2],A[((a&3)<<4)|(b>>4)],i+1<s.length?A[((b&15)<<2)|(c>>6)]:"=",i+2<s.length?A[c&63]:"=")}return out.join("");}
function makePdf(cs){
 const W=595,H=842,L=46,R=549,pages=[];let ops=[],section="",y=0;
 const color=a=>a.join(" ")+" rg";
 const rect=(x,Y,w,h,c)=>ops.push(color(c),`${x} ${Y} ${w} ${h} re f`);
 const rule=(Y)=>ops.push(".84 .88 .92 RG","0.5 w",`${L} ${Y} m ${R} ${Y} l S`);
 const draw=(x,Y,s,size=10,c=[.12,.23,.35])=>ops.push(color(c),`BT /FC ${size} Tf 1 0 0 1 ${x.toFixed(1)} ${Y.toFixed(1)} Tm <${toHex(String(s))}> Tj ET`);
 const width=(s,size)=>Array.from(String(s)).reduce((sum,ch)=>sum+size*(ch===" "?.33:ch.charCodeAt(0)<128?(/[MmwW@]/.test(ch)?.84:.55):1),0);
 const wrap=(s,size,max)=>{const arr=[];let buf="";for(const ch of Array.from(String(s))){if(buf&&width(buf+ch,size)>max){arr.push(buf);buf=ch}else buf+=ch;}if(buf)arr.push(buf);return arr};
 function page(title="",cont=false){if(ops.length)pages.push(ops.join("\n")+"\n");ops=[];section=title;rect(0,0,W,H,[1,1,1]);rect(0,834,W,8,[.055,.17,.29]);draw(L,806,"TERM / ATLAS    CUDA  ·  BILINGUAL GLOSSARY",9.8,[.1,.26,.40]);rule(792);
  if(title){draw(L,760,title+(cont?"（续）":""),15,[.06,.21,.35]);rule(746);y=731;}else y=767;}
 function term(i,t){const heads=wrap(`${String(i).padStart(2,"0")}  ${t.en}   /   ${t.zh}${t.abbr?"  ["+t.abbr+"]":""}`,10.0,480),defs=wrap(t.definition,9.05,475),h=heads.length*14+defs.length*12.7+15;
  if(y-h<64)page(section,true);
  if(i%2===0)rect(L-4,y-h+3,R-L+8,h,[.962,.973,.983]);
  let yy=y-13;for(const txt of heads){draw(L+3,yy,txt,10,[.055,.2,.34]);yy-=14;}for(const txt of defs){draw(L+16,yy,txt,9.05,[.31,.39,.46]);yy-=12.7;}y-=h;}
 function para(s,size=9.25,indent=0,c=[.30,.38,.45]){const lines=wrap(s,size,R-L-indent-8);if(y-lines.length*(size+5)-9<62)page(section,true);for(const a of lines){draw(L+indent,y,a,size,c);y-=size+5;}y-=9;}
 page();
 rect(0,625,W,174,[.055,.17,.29]);draw(L,743,"CUDA",33,[1,1,1]);draw(L,701,"CUDA Programming & Optimization",18,[.83,.91,.98]);draw(L,665,"400 条中英文术语    ·    16 个专业章节",12,[1,1,1]);
 draw(L,594,"CUDA 知识体系",14);rule(576);
 cs.forEach((c,i)=>draw(L+(i>=8?258:0),546-(i>=8?i-8:i)*29,`${String(c.n).padStart(2,"0")}  ${c.title}`,9.55,[.13,.29,.42]));
 draw(L,233,"线程 · 存储 · 同步 · Stream · 性能 · 生态",10.2,[.16,.33,.45]);
 draw(L,207,"原创专业释义与自测题；源数据数量与结构已自动校验。",9.4,[.29,.39,.48]);
 draw(L,182,"具体能力与 API 语义以目标 CUDA 版本和 GPU 架构为准。",9.4,[.29,.39,.48]);
 draw(L,105,"TERM / ATLAS  ·  2026-11-27",10,[.17,.35,.48]);
 for(const c of cs){page(`${String(c.n).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>term(i+1,t));}
 page("附录 A  ·  CUDA 核心概念辨析");
 contrasts.forEach((x,i)=>{if(y<125)page(section,true);para(`${i+1}. ${x[0]}`,10.4,0,[.08,.24,.38]);para(x[1],9.2,14);});
 page("附录 B  ·  中等难度面试题");
 interviews.forEach((x,i)=>{if(y<120)page(section,true);para(`Q${i+1}. ${x[0]}`,10.4,0,[.08,.24,.38]);para(`答：${x[1]}`,9.2,14);});
 page("附录 C  ·  中等难度考试题");
 exams.forEach((x,i)=>{if(y<120)page(section,true);para(`${i+1}. ${x[0]}`,10.4,0,[.08,.24,.38]);para(`解析：${x[1]}`,9.2,14);});
 page("附录 D  ·  官方技术参考");
 references.forEach((x,i)=>{para(`${i+1}. ${x[0]}`,9.9,0,[.08,.24,.38]);para(x[1],8.6,14);});
 para("本册为独立编写的术语解释；参考资料的作者未参与本册逐条审稿。",9.2,0,[.3,.37,.44]);
 if(ops.length)pages.push(ops.join("\n")+"\n");
 const objects=[null];objects[1]="<< /Type /Catalog /Pages 2 0 R >>";
 objects[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${pages.map((_,i)=>`${6+i*2} 0 R`).join(" ")}] >>`;
 objects[3]="<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [ << /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 >> ] /ToUnicode 4 0 R >>";
 const cmap="/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n/CMapName /Identity-UCS2 def\n/CMapType 2 def\n1 begincodespacerange\n<0000> <FFFF>\nendcodespacerange\n1 beginbfrange\n<0000> <FFFF> <0000>\nendbfrange\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n";
 objects[4]=`<< /Length ${cmap.length} >>\nstream\n${cmap}endstream`;
 objects[5]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
 for(let i=0;i<pages.length;i++){let pn=6+i*2,sid=pn+1;let stream=pages[i]+".84 .88 .92 RG 0.5 w 46 51 m 549 51 l S\n";
 stream+=`${color([.40,.47,.55])} BT /FC 8 Tf 1 0 0 1 46 34 Tm <${toHex("TERM / ATLAS  ·  CUDA")}> Tj ET\n`;
 stream+=`${color([.40,.47,.55])} BT /FC 8 Tf 1 0 0 1 490 34 Tm <${toHex(`${i+1} / ${pages.length}`)}> Tj ET\n`;
 objects[pn]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Resources << /Font << /FC 3 0 R >> >> /Contents ${sid} 0 R >>`;
 objects[sid]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;
 }
 let pdf="%PDF-1.4\n%TERM-ATLAS\n",positions=[0];
 for(let i=1;i<objects.length;i++){positions[i]=pdf.length;pdf+=`${i} 0 obj\n${objects[i]}\nendobj\n`;}
 const xref=pdf.length;pdf+=`xref\n0 ${objects.length}\n0000000000 65535 f \n`;
 for(let i=1;i<objects.length;i++)pdf+=`${String(positions[i]).padStart(10,"0")} 00000 n \n`;
 pdf+=`trailer\n<< /Size ${objects.length} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;
 return {pdf,pages:pages.length};
}
const src=Array.from({length:16},(_,i)=>fs.readFileSync(path.join(ROOT,"data/cuda/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const cs=parseData(src),entries=cs.flatMap(c=>c.terms);
if(cs.length!==16||cs.some(c=>c.terms.length!==25)||entries.length!==400||new Set(entries.map(t=>t.en.toLowerCase())).size!==400||entries.some(t=>!t.en||!t.zh||!t.definition))throw Error("Expected 16 chapters with 25 unique complete terms each");
const tsv=Buffer.from(makeTsv(cs),"utf8"),md=Buffer.from(makeMd(cs),"utf8"),pdf=Buffer.from(makePdf(cs).pdf,"ascii");
const output=[["data/cuda.tsv",tsv],["glossaries/cuda.md",md],["docs/glossaries/cuda.md",md],["pdf/cuda.pdf",pdf],["docs/pdf/cuda.pdf",pdf]];
const check=process.argv.includes("--check");
for(const [rel,bytes] of output){const f=path.join(ROOT,rel);if(check){if(!fs.existsSync(f)||!fs.readFileSync(f).equals(bytes))throw Error("Out-of-sync artifact: "+rel);}else{fs.mkdirSync(path.dirname(f),{recursive:true});fs.writeFileSync(f,bytes);}}
console.log((check?"PASS":"GENERATED")+": 400 terms, 16 chapters, "+output.length+" synchronized artifacts");
