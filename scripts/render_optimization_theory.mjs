#!/usr/bin/env node
// Reproducible TERM/ATLAS Optimization Theory single-subject renderer.
// node scripts/render_optimization_theory.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["凸优化 vs 非凸优化","凸目标在凸可行域上的任意局部极小点就是全局极小点；非凸问题通常只能依赖局部条件和额外结构保证。"],["必要条件 vs 充分条件","梯度为零和海森半正定一般只是局部极小值必要条件；梯度为零且海森正定可保证严格局部极小值。"],["KKT 条件 vs 强对偶","KKT 是在适当约束资格与凸性等条件下的最优性刻画；强对偶是原始与对偶最优值相等的性质，两者不能直接互相替代。"],["弱对偶 vs 强对偶","最小化原问题的任意对偶可行值给出下界是弱对偶；最优值相等才是强对偶，常需额外条件。"],["LP 可行 vs LP 有界","可行仅说明至少一个满足约束的点存在；有界还需目标在可行域上不能无限改善。"],["单纯形法 vs 内点法","单纯形法沿基与极点结构换基；内点法以屏障或原始—对偶路径接近最优，均可解决大型 LP。"],["梯度下降 vs 牛顿法","梯度下降主要用一阶信息；牛顿法求解局部二阶模型并利用曲率，但会增加线性系统求解开销。"],["BFGS vs L-BFGS","BFGS 更新并存储密集曲率近似；L-BFGS 仅保留少量历史向量，更适合高维变量。"],["L1 vs L2 正则化","L1 常促进解稀疏，L2 通常鼓励参数整体收缩但一般不使其恰好为零。"],["SGD vs AdamW","SGD 使用随机梯度与统一或带动量步长；AdamW 用坐标自适应矩估计并解耦权重衰减。"],["全局最优 vs 局部最优","局部最优只在邻域中不可改善；全局最优要求整个可行域中不存在更好点。"],["鲁棒优化 vs 分布鲁棒优化","鲁棒优化对参数不确定集合内所有值保证约束；分布鲁棒优化对候选概率分布集合的最坏期望优化。"],["Pareto 最优 vs 加权和最优","Pareto 最优是非支配性质；加权和是生成一些 Pareto 解的标量化方法，非凸前沿可能无法完整覆盖。"],["在线遗憾 vs 随机训练损失","遗憾衡量累计在线决策相对于基准策略的差额；训练损失是具体数据或期望风险函数值。"]];
const interviews=[["为什么凸优化的局部最优点是全局最优点？","若存在更好的另一可行点，则连接它与局部解的线段仍可行；凸性使线段上足够近的点也更好，与局部最优矛盾。"],["在什么条件下 KKT 能够作为充分最优性条件？","对于可微凸最小化问题，凸不等式约束、仿射等式与原始/对偶可行、驻点及互补性成立时，KKT 给出全局最优；资格条件主要用于必要性。"],["为什么 2 阶海森半正定不能证明严格局部极小值？","例如 f(x)=x^3 在 x=0 处梯度为零、二阶导也为零，却不是局部极小值。"],["为什么整数规划往往比线性规划更难？","整数约束使可行解离散、破坏连续凸结构；许多组合优化决策问题是 NP 困难的，通常依赖割与分支界。"],["什么时候 L-BFGS 比完整 BFGS 更适合？","当参数维度很大、无法承担 O(n²) 曲率矩阵存储时，L-BFGS 用固定历史步长与梯度差控制内存开销。"],["为什么 0/1 约束的大 M 建模要特别谨慎？","M 过小会误删合法方案，过大会削弱 LP 松弛和数值稳定性；应根据变量边界给出可验证的有效常数。"],["AdamW 与 Adam 直接加 L2 惩罚有何不同？","在坐标自适应预条件器下，L2 梯度惩罚与参数乘性衰减不再等价；AdamW 单独处理权重衰减。"],["ADMM 是否总能收敛到任意非凸问题的全局解？","不能；经典收敛保证依赖凸性、闭性、鞍点存在等条件，非凸 ADMM 通常需要额外假设且一般只能获得局部驻点保证。"],["为什么贝叶斯优化适用于昂贵黑箱目标？","概率代理模型根据有限评估估计均值和不确定性，采集函数权衡探索与利用，减少高成本的真实函数调用。"],["什么是 Pareto 非支配，为什么一个多目标问题可能有多个解？","不同目标之间存在冲突，一个解若无法在不损害任何目标下改善另一个目标，就可能位于 Pareto 前沿，通常不存在唯一的全面最好解。"]];
const exams=[["对于 f(x)=x²+4x+7，求无约束最小点和最小值。","f'(x)=2x+4=0 得 x*=-2；f''=2>0，代入得到 f(-2)=3。"],["判断 f(x)=x⁴ 是否严格凸，以及是否在所有点都强凸。","x⁴ 在实数域严格凸；但其二阶导 12x² 在零处为零，无法找到全域正的强凸参数。"],["最小化 x²，约束 x≥1，写出最优解与对应 KKT 乘子。","写 g(x)=1-x≤0，L=x²+λ(1-x)。x*=1，驻点 2-λ=0，故 λ*=2，互补成立。"],["凸问题存在 Slater 点是否必然意味着有唯一最优解？","不必然。Slater 常用于强对偶与乘子存在；唯一性通常需严格凸性及最优解存在等额外条件。"],["函数 f(x)=x³ 在 x=0 处一阶和二阶必要条件是否成立，能否认定最小值？","梯度和二阶导均为零，弱的一二阶必要形式满足，但任意邻域存在正负函数值，因此不是局部极小值。"],["设 LP 的原始可行目标值为 12、对偶可行目标值为 10，最优值已知的界是什么？","对最小化 LP，弱对偶给出 10≤p*≤12；差距 2 表示当前解未由该对偶证书证明最优。"],["若梯度下降在 f(x)=0.5 x² 上使用固定步长 α，何时迭代收敛到 0？","更新 x_{k+1}=(1-α)x_k；要求 |1-α|<1，即 0<α<2。"],["目标为 f(x)=|x|，求 x=0 处的凸次微分。","∂f(0)=[-1,1]；零属于该集合，验证 x=0 为全局最小点。"],["一个 3 维密集 BFGS 海森近似矩阵有多少元素？","3×3=9 个元素；一般密集表示需 O(n²) 存储。"],["两个目标均需最小化，A=(2,5)、B=(3,4)，A 是否支配 B？","不是：A 的第一目标较好但第二目标较差，B 也不支配 A；二者在该集合中互不支配。"]];
const references=[["Convex Optimization — Boyd & Vandenberghe (2004)","https://stanford.edu/~boyd/cvxbook/"],["Numerical Optimization — Nocedal & Wright (2nd ed.)","https://link.springer.com/book/10.1007/978-0-387-40065-5"],["Nonlinear Programming — Bertsekas","https://faculty.engineering.asu.edu/bertsekas/books/nonlinear-programming-convex-optimization"],["Proximal Algorithms — Parikh & Boyd (2014)","https://stanford.edu/~boyd/papers/prox_algs.html"],["Distributed Optimization and Statistical Learning via ADMM — Boyd et al. (2011)","https://stanford.edu/~boyd/papers/admm_distr_stats.html"],["NEOS Guide — Optimization Problems and Algorithms","https://neos-guide.org/guide/"],["CVXPY — Disciplined Convex Programming Tutorial","https://www.cvxpy.org/tutorial/dcp/"],["Introduction to Online Convex Optimization — Hazan","https://mitpress.mit.edu/9780262046985/introduction-to-online-convex-optimization/"]];
function parseData(raws){const cs=[];let current=null;for(const raw of raws){for(const line of raw.trim().split(/\r?\n/)){if(!line)continue;if(line.startsWith("# ")){if(current)cs.push(current);current={n:cs.length+1,title:line.slice(2),terms:[]};continue;}const p=line.split("|");if(p.length!==4||!current)throw Error("Malformed source: "+line);current.terms.push({en:p[0].trim(),zh:p[1].trim(),abbr:p[2].trim(),definition:p[3].trim()});}}if(current)cs.push(current);return cs;}
function makeTsv(cs){return "# 最优化理论 / Optimization Theory\n# Canonical sources: data/optimization-theory/chapters/*.tsv\n"+cs.map(c=>`# ${String(c.n).padStart(2,"0")}. ${c.title}\n`+c.terms.map(t=>[t.en,t.zh,t.abbr,t.definition].join("|")).join("\n")).join("\n\n")+"\n";}
function makeMd(cs){const out=[
"# 最优化理论 · Optimization Theory",
"",
"> 400 个专业术语中英文对照 | Bilingual Technical Glossary",
"",
"**400 条双语术语 · 16 个专业章节 · 2026-11-27**",
"",
"涉及数学规划、凸优化、无约束和约束优化、KKT 与对偶、线性规划、整数规划、数值方法、一阶与二阶算法、近端方法、随机梯度、大规模与分布式优化、全局优化、多目标与鲁棒优化、动态规划与最优控制。",
"",
"本册对英文技术术语提供独立撰写的中文定义。各算法的性质依赖凸性、可行性、光滑性、约束资格、故障模型和数值条件等假设，不能脱离假设引用为普遍保证。",
"",
"**专业审稿状态：**结构、数量、英文主词条唯一性已自动核验；尚未完成独立领域专家逐条事实审稿。参阅末尾来源。",
"",
"## 章节目录","",...cs.map(c=>`- ${String(c.n).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),"","---",""
];
for(const c of cs){out.push(`## ${String(c.n).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 简明释义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en} | ${t.zh} | ${t.abbr} | ${t.definition} |`),"");}
out.push("## 核心术语辨析","","| 对比对象 | 关键区别 |","|---|---|",...contrasts.map(x=>`| ${x[0]} | ${x[1]} |`),"","## 中等难度面试题与答案","");
interviews.forEach((q,i)=>out.push(`### 面试题 ${i+1}. ${q[0]}`,"",`**参考答案：**${q[1]}`,""));
out.push("## 中等难度考试题与解析","");
exams.forEach((q,i)=>out.push(`### 考试题 ${i+1}. ${q[0]}`,"",`**解析：**${q[1]}`,""));
out.push("## 权威来源与延伸阅读","","以下书籍和技术资料用于术语边界和理论主题的参考；不代表作者逐条认可本项目译名与释义。","",...references.map((r,i)=>`${i+1}. [${r[0]}](${r[1]})`),"","## 维护说明","","- 原始数据：`data/optimization-theory/chapters/*.tsv`，每行 `en|zh|abbr|definition`。","- 汇总：`data/optimization-theory.tsv`；出版文件由专用渲染脚本生成。","- 可复现验证：`node scripts/render_optimization_theory.mjs --check`。","- 后续需额外审稿方可将词条用于专业 Wiki 的经过复核版本。");
return out.join("\n")+"\n";}
function hex(s){let out="";for(let i=0;i<s.length;i++)out+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return out;}
function b64(s){const A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",arr=[];for(let i=0;i<s.length;i+=3){const a=s.charCodeAt(i),b=i+1<s.length?s.charCodeAt(i+1):0,c=i+2<s.length?s.charCodeAt(i+2):0;arr.push(A[a>>2],A[((a&3)<<4)|(b>>4)],i+1<s.length?A[((b&15)<<2)|(c>>6)]:"=",i+2<s.length?A[c&63]:"=");}return arr.join("");}
function buildPdf(cs){
 const W=595,H=842,LEFT=46,RIGHT=549,pages=[];let ops=[],y=0,current="";
 const col=a=>a.join(" ")+" rg";
 const rect=(x,yy,w,h,c)=>ops.push(col(c),`${x} ${yy} ${w} ${h} re f`);
 const line=(x1,y1,x2,y2)=>ops.push(".82 .86 .90 RG","0.55 w",`${x1} ${y1} m ${x2} ${y2} l S`);
 const asciiSafe=s=>String(s).replace(/Ł/g,"L").replace(/ł/g,"l").replace(/ᵀ/g,"T").replace(/–|—/g,"-").replace(/ε/g,"epsilon").replace(/²/g,"2").replace(/³/g,"3").replace(/⁴/g,"4").replace(/α/g,"alpha").replace(/≥/g,">=").replace(/≤/g,"<=").replace(/∂/g,"d");
 const draw=(x,yy,s,size=10,c=[.1,.22,.34])=>ops.push(col(c),`BT /F1 ${size} Tf 1 0 0 1 ${x} ${yy} Tm <${hex(asciiSafe(s))}> Tj ET`);
 const measure=(s,sz)=>Array.from(asciiSafe(s)).reduce((n,ch)=>n+sz*(ch===" "?.33:ch.charCodeAt(0)<128?/[WMmw@]/.test(ch)?.78:.56:1),0);
 const wrap=(s,sz,max)=>{let out=[],buf="";for(const ch of Array.from(asciiSafe(s))){if(buf&&measure(buf+ch,sz)>max){out.push(buf);buf=ch;}else buf+=ch;}if(buf)out.push(buf);return out;};
 function page(title="",cont=false){if(ops.length)pages.push(ops.join("\n")+"\n");ops=[];current=title;rect(0,0,W,H,[1,1,1]);rect(0,834,W,8,[.06,.24,.37]);draw(LEFT,803,"TERM / ATLAS     OPTIMIZATION THEORY",10,[.08,.27,.4]);line(LEFT,789,RIGHT,789);if(title){draw(LEFT,756,title+(cont?"（续）":""),15,[.06,.25,.37]);line(LEFT,743,RIGHT,743);y=726;}else y=764;}
 function term(i,t){const heading=wrap(`${String(i).padStart(2,"0")}.  ${t.en}  /  ${t.zh}${t.abbr?"   ["+t.abbr+"]":""}`,9.9,480),desc=wrap(t.definition,9.15,477);const height=heading.length*13.4+desc.length*12.4+16;if(y-height<62)page(current,true);if(i%2===0)rect(LEFT-4,y-height+3,RIGHT-LEFT+8,height,[.961,.975,.982]);let yy=y-13;for(const z of heading){draw(LEFT+2,yy,z,9.9,[.08,.21,.31]);yy-=13.4;}for(const z of desc){draw(LEFT+13,yy,z,9.15,[.31,.38,.46]);yy-=12.4;}y-=height;}
 function paragraph(s,size=9.5,indent=0,c=[.31,.37,.44]){const ls=wrap(s,size,RIGHT-LEFT-indent-5);if(y-ls.length*(size+5)-9<60)page(current,true);for(const x of ls){draw(LEFT+indent,y,x,size,c);y-=size+5;}y-=9;}
 page();
 rect(0,635,W,163,[.06,.24,.37]);draw(LEFT,742,"最优化理论",29,[1,1,1]);draw(LEFT,700,"Optimization Theory",17,[.86,.93,.98]);draw(LEFT,662,"400 条双语术语   /   16 个专业章节",12,[1,1,1]);
 draw(LEFT,591,"章节目录",14);line(LEFT,574,RIGHT,574);
 cs.forEach((c,i)=>draw(LEFT+(i>=8?256:0),547-(i>=8?i-8:i)*29,`${String(c.n).padStart(2,"0")}  ${c.title}`,9.5,[.12,.28,.41]));
 draw(LEFT,235,"从凸分析与 KKT，到数值优化、随机算法和最优控制",10,[.2,.33,.46]);
 draw(LEFT,207,"原创术语释义，格式与重复项已经校验。",9.7,[.25,.34,.44]);
 draw(LEFT,183,"专业事实审稿及跨阅读器版式检查仍需单独完成。",9.7,[.25,.34,.44]);
 draw(LEFT,107,"2026-11-27   ·   Bilingual Technical Glossary",10,[.24,.36,.50]);
 for(const c of cs){page(`${String(c.n).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>term(i+1,t));}
 page("附录 A · 核心术语辨析");
 contrasts.forEach((x,i)=>{if(y<120)page(current,true);paragraph(`${i+1}. ${x[0]}`,10.5,0,[.08,.25,.39]);paragraph(x[1],9.25,13);});
 page("附录 B · 中等难度面试题");
 interviews.forEach((x,i)=>{if(y<120)page(current,true);paragraph(`Q${i+1}. ${x[0]}`,10.3,0,[.08,.25,.39]);paragraph(`答：${x[1]}`,9.2,12);});
 page("附录 C · 中等难度考试题");
 exams.forEach((x,i)=>{if(y<120)page(current,true);paragraph(`${i+1}. ${x[0]}`,10.3,0,[.08,.25,.39]);paragraph(`解析：${x[1]}`,9.2,12);});
 page("附录 D · 参考教材与论文");
 references.forEach((x,i)=>{paragraph(`${i+1}. ${x[0]}`,9.8,0,[.08,.25,.39]);paragraph(x[1],8.7,13);});
 paragraph("本册内容为原创概念简释及索引，不代表原始作者对具体译名、公式或定义的逐条审稿认可。",9.6,0,[.3,.37,.45]);
 if(ops.length)pages.push(ops.join("\n")+"\n");
 const objects=[null];objects[1]="<< /Type /Catalog /Pages 2 0 R >>";
 objects[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${pages.map((_,i)=>`${5+2*i} 0 R`).join(" ")}] >>`;
 objects[3]="<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [<< /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 >>] >>";
 objects[4]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
 for(let i=0;i<pages.length;i++){const pn=5+2*i,sid=pn+1;let stream=pages[i]+".82 .86 .90 RG 0.55 w 46 49 m 549 49 l S\n";
 stream+=`${col([.37,.46,.54])} BT /F1 8.5 Tf 1 0 0 1 46 33 Tm <${hex("TERM / ATLAS  |  Optimization Theory")}> Tj ET\n`;
 stream+=`${col([.37,.46,.54])} BT /F1 8.5 Tf 1 0 0 1 485 33 Tm <${hex(`${i+1} / ${pages.length}`)}> Tj ET\n`;
 objects[pn]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents ${sid} 0 R >>`;
 objects[sid]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;
 }
 let pdf="%PDF-1.4\n%TERM-ATLAS\n",offsets=[0];
 for(let i=1;i<objects.length;i++){offsets[i]=pdf.length;pdf+=`${i} 0 obj\n${objects[i]}\nendobj\n`;}
 const xref=pdf.length;pdf+=`xref\n0 ${objects.length}\n0000000000 65535 f \n`;
 for(let i=1;i<objects.length;i++)pdf+=`${String(offsets[i]).padStart(10,"0")} 00000 n \n`;
 pdf+=`trailer\n<< /Size ${objects.length} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;
 return {pdf,pages:pages.length};
}
const sources=Array.from({length:16},(_,i)=>fs.readFileSync(path.join(ROOT,"data/optimization-theory/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const cs=parseData(sources),terms=cs.flatMap(c=>c.terms);
if(cs.length!==16||cs.some(c=>c.terms.length!==25)||terms.length!==400||new Set(terms.map(t=>t.en.toLowerCase())).size!==400||terms.some(t=>!t.en||!t.zh||!t.definition))throw Error("Optimization source validation failed");
const tsv=Buffer.from(makeTsv(cs),"utf8"),md=Buffer.from(makeMd(cs),"utf8"),pdf=Buffer.from(buildPdf(cs).pdf,"ascii");
const files=[["data/optimization-theory.tsv",tsv],["glossaries/optimization-theory.md",md],["docs/glossaries/optimization-theory.md",md],["pdf/optimization-theory.pdf",pdf],["docs/pdf/optimization-theory.pdf",pdf]];
const check=process.argv.includes("--check");for(const [rel,buf] of files){const f=path.join(ROOT,rel);if(check){if(!fs.existsSync(f)||!fs.readFileSync(f).equals(buf))throw Error("Out of sync: "+rel);}else{fs.mkdirSync(path.dirname(f),{recursive:true});fs.writeFileSync(f,buf);}}
console.log((check?"PASS":"GENERATED")+": 400 terms, 16 chapters, "+files.length+" synchronized artifacts");
