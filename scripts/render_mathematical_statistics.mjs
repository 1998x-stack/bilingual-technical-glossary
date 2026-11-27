#!/usr/bin/env node
// Reproducible TERM/ATLAS single-subject Mathematical Statistics publisher.
// node scripts/render_mathematical_statistics.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["总体参数、估计量与估计值","总体参数是未知的固定目标；估计量是随机样本的函数；估计值是本次样本给出的具体数值。"],["总体标准差与标准误","总体标准差描述个体取值离散程度；标准误描述估计量在重复抽样下的波动。"],["数据分布与抽样分布","数据分布是单个观察变量的概率规律；抽样分布是从重复样本计算统计量后的概率规律。"],["无偏性与相合性","无偏性要求每个样本量下估计期望等于真值；相合性要求样本量增长时估计依概率接近真值。二者互不等价。"],["充分统计量与完全统计量","充分性保证不丢失关于模型参数的抽样信息；完全性排除非平凡零期望函数，二者是不同性质。"],["置信区间与贝叶斯可信区间","频率学派置信区间的概率保证针对随机抽样程序；可信区间给定数据与先验后可有明确后验概率解释。"],["置信区间、预测区间和容忍区间","三者分别关注固定参数、未来随机观测、总体指定比例的覆盖；即使同为 95% 也有不同覆盖对象。"],["p 值与原假设为真概率","p 值是原假设模型下得到至少如此极端统计量的概率，不是给定数据后原假设为真的概率。"],["第一类错误、第二类错误与功效","第一类错误是原假设真时误拒绝；第二类错误是在指定备择下漏拒绝；功效为 1−第二类错误率。"],["统计显著性与实际显著性","较小 p 值并不保证效应足够大或有业务价值；应联合报告效应量、区间及研究设计。"],["风险比与优势比","风险比比较事件发生概率，优势比比较事件优势；基准事件不罕见时两者数值差异可能明显。"],["多重检验的 FWER 与 FDR","FWER 约束至少出现一次假阳性的概率；FDR 控制所有发现中假发现比例的期望。"],["Bootstrap 与置换检验","Bootstrap 常近似估计量的抽样分布；置换检验在适当可交换性零假设下构造检验统计量的参考分布。"],["回归相关与因果关系","回归关联可能受到混杂、选择或反向因果影响；因果解释通常需要随机化或明确识别假设。"]];
const interviews=[["为什么样本方差常用 n−1 作为分母？","估计总体均值消耗一个自由度；独立同分布且有限方差下，中心化平方和期望是 (n−1)σ²，因此除以 n−1 无偏。"],["如何区分 p 值和第一类错误率？","显著性水平是检验程序事先控制的错误上界；p 值则是本次观察到的数据在零假设下的极端性指标。"],["什么情况下 t 区间是精确而不是渐近近似？","独立正态样本、总体方差未知且按样本方差学生化时，样本均值与方差的特定独立结构给出精确 t 分布。"],["Rao–Blackwell 化为什么可以改善估计？","把原估计量对充分统计量取条件期望，仍保持无偏，并借条件方差分解使平方损失风险不增加。"],["为什么置信区间不是“真参数有 95% 的频率概率位于该已知区间”？","在频率模型中参数视为固定；95% 针对重复抽样区间包含参数的长期比例。观测后区间已固定。"],["为什么小 p 值不代表效果大？","给定固定的非零效应，当样本量足够大时标准误可趋近零，检验可能拒绝极小、缺乏实际意义的效应。"],["为什么两组独立样本均值比较通常优先考虑 Welch t 检验？","Welch 不强制相同方差，并通过估计标准误及自由度调整降低异方差时传统合并方差检验的失真风险。"],["卡方检验在稀疏列联表中有什么问题？","小期望频数会影响渐近卡方参考分布准确性，需考虑精确检验或适当重抽样方法。"],["为何在挑选最佳模型后直接报告原始 p 值可能错误？","模型选择依赖同一数据，会改变估计量与检验统计量的条件分布，引入选择后推断偏差。"],["Bootstrap 对时间序列是否可以直接逐点有放回抽样？","一般不能；逐点抽样破坏序列相关结构，常需要分块 Bootstrap 或其他保留依赖的方案。"],["为什么简单回归中的显著系数通常不能直接解释为因果效应？","模型残差可能包含与解释变量相关的混杂因素；需随机分配、合理工具变量或其他可辩护的识别设计。"],["贝叶斯可信区间与频率置信区间何时可能相似？","在大样本、正则模型和较弱先验影响等条件下，后验渐近正态可与似然估计区间近似一致，但不构成普遍保证。"]];
const exams=[["IID 样本总体标准差 12、样本量 36，样本均值的标准误是多少？","SE=σ/√n=12/6=2。"],["100 次独立伯努利试验，样本成功比例 0.4，估算比例标准误。","将 p 用样本比例替代，SE≈√(0.4×0.6/100)≈0.049。"],["样本 1、2、3 的无偏样本方差是多少？","均值为 2，平方离差和为 2，除以 n−1=2，得到 s²=1。"],["单样本检验 n=25、样本均值 105、零假设均值 100、样本标准差 10，t 统计量？","t=(105−100)/(10/√25)=2.5，自由度为 24。"],["在 H0 下 X~Binomial(10,0.5)，计算 P(X≥9)。","P(X≥9)=[C(10,9)+C(10,10)]/2¹⁰=11/1024≈0.0107。"],["对指数分布率参数 λ，观察到样本 1、2、3，极大似然估计是多少？","n=3，总观测和为 6，指数率 MLE 为 n/Σxi=0.5。"],["20 次独立、零假设均为真且单次 α=0.05 的检验，至少一次误拒绝的概率？","1−(1−0.05)^20≈0.642；说明多重比较需要错误率控制。"],["4 个 p 值为 0.001、0.020、0.049、0.200，BH 控制 q=0.05 时拒绝几个假设？","与 i×0.05/4 阈值比较，最大满足条件的是 i=2，所以拒绝前 2 个。"],["回归模型的残差平方和为 20，总平方和为 100，带截距模型 R² 多少？","R²=1−RSS/TSS=1−20/100=0.8。"],["2×2 表中 a=30、b=10、c=20、d=40，样本优势比是多少？","OR=(a×d)/(b×c)=30×40/(10×20)=6。"],["Beta(2,2) 先验，二项样本成功 8 次失败 2 次，后验均值是多少？","后验为 Beta(10,4)，均值 10/(10+4)=5/7≈0.714。"],["若随机变量 Xₙ 依概率收敛到 2，Yₙ 依分布收敛到标准正态，XₙYₙ 的极限分布？","由 Slutsky 定理，XₙYₙ 依分布收敛到 2Z，即 N(0,4)。"]];
const references=[["Casella & Berger, Statistical Inference (2nd ed.)","https://www.cengage.com/c/statistical-inference-2e-casella-berger/9780534243128"],["Wasserman, All of Statistics (Springer, 2004)","https://link.springer.com/book/10.1007/978-0-387-21736-9"],["van der Vaart, Asymptotic Statistics (Cambridge University Press)","https://www.cambridge.org/core/books/asymptotic-statistics/A3C7DAD3F7E66A1FA60E9C8FE132EE1D"],["Lehmann & Romano, Testing Statistical Hypotheses (4th ed.)","https://link.springer.com/book/10.1007/978-3-030-70578-7"],["Efron & Tibshirani, An Introduction to the Bootstrap (CRC)","https://www.routledge.com/An-Introductionto-the-Bootstrap/Efron-Tibshirani/p/book/9780429246593"],["NIST/SEMATECH Engineering Statistics Handbook","https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook"]];
function parseData(raws){let cs=[],c=null;for(const raw of raws){for(const s of raw.trim().split(/\r?\n/)){if(!s)continue;if(s.startsWith("# ")){if(c)cs.push(c);c={n:cs.length+1,title:s.slice(2),terms:[]};continue;}const p=s.split("|");if(p.length!==4||!c)throw Error("Invalid term "+s);c.terms.push({en:p[0].trim(),zh:p[1].trim(),abbr:p[2].trim(),definition:p[3].trim()});}}if(c)cs.push(c);return cs;}
function makeTsv(cs){return "# 数理统计 | Mathematical Statistics\n# Canonical sources: data/mathematical-statistics/chapters/*.tsv\n"+cs.map(c=>`# ${String(c.n).padStart(2,"0")}. ${c.title}\n`+c.terms.map(t=>[t.en,t.zh,t.abbr,t.definition].join("|")).join("\n")).join("\n\n")+"\n";}
function makeMd(cs){
 const o=["# 数理统计 · Mathematical Statistics","","> Professional Bilingual Statistical Glossary | 专业中英文术语对照表","",`**${cs.reduce((n,c)=>n+c.terms.length,0)} 条术语 · ${cs.length} 个专业章节 · 2026-11-27**`,"",
 "以经典数理统计课程体系组织：统计模型、常见分布、抽样分布、充分性、估计、置信区间、假设检验、渐近理论、似然推断、回归与实验设计，以及非参数、重抽样、贝叶斯与现代应用。定义均为独立撰写的简明概括，具体结论须考虑分布、独立性、正则性、样本设计和识别假设。","",
 "**编辑审稿状态：**结构、字段、计数和英文术语重复项自动校验；未宣称独立专家逐条技术审稿。","",
 "## 目录","",...cs.map(c=>`- ${String(c.n).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),"","---",""];
 for(const c of cs){o.push(`## ${String(c.n).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 简明释义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en} | ${t.zh} | ${t.abbr} | ${t.definition} |`),"");}
 o.push("## 核心概念辨析","","| 概念组合 | 定义区别与适用范围 |","|---|---|",...contrasts.map(c=>`| ${c[0]} | ${c[1]} |`),"","## 中等难度面试题与答案","");
 interviews.forEach((q,i)=>o.push(`### 面试 ${i+1}. ${q[0]}`,"",`**参考思路：**${q[1]}`,""));
 o.push("## 中等难度考试题与解析","");
 exams.forEach((q,i)=>o.push(`### 考试 ${i+1}. ${q[0]}`,"",`**解析：**${q[1]}`,""));
 o.push("## 参考教材与技术资料","","以下资料为学科体系及术语定义的参考，并非各作者逐条审阅的证明。","",...references.map((r,i)=>`${i+1}. [${r[0]}](${r[1]})`),"","## 维护与重建","","- 原始词表：`data/mathematical-statistics/chapters/*.tsv`。","- 导出：`data/mathematical-statistics.tsv`、`glossaries/mathematical-statistics.md` 与 `pdf/mathematical-statistics.pdf`。","- 构建校验：`node scripts/render_mathematical_statistics.mjs --check`。","- PDF 需独立进行中文字符与跨阅读器版面检查；专业 Wiki 须另行逐条审稿。");
 return o.join("\n")+"\n";
}
function uhex(s){let out="";for(let i=0;i<s.length;i++)out+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return out;}
function b64(s){const T="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",o=[];for(let i=0;i<s.length;i+=3){const a=s.charCodeAt(i),b=i+1<s.length?s.charCodeAt(i+1):0,c=i+2<s.length?s.charCodeAt(i+2):0;o.push(T[a>>2],T[((a&3)<<4)|(b>>4)],i+1<s.length?T[((b&15)<<2)|(c>>6)]:"=",i+2<s.length?T[c&63]:"=");}return o.join("");}
function buildPdf(cs){
 const W=595,H=842,L=48,R=548,pages=[];let ops=[],current="",y=0;
 const col=a=>a.join(" ")+" rg", rect=(x,y,w,h,rgb)=>ops.push(col(rgb),`${x} ${y} ${w} ${h} re f`);
 const line=(x,y,x2,y2)=>ops.push(".83 .87 .91 RG","0.55 w",`${x} ${y} m ${x2} ${y2} l S`);
 const draw=(x,y,t,size=10,rgb=[.12,.22,.33])=>ops.push(col(rgb),`BT /FC ${size} Tf 1 0 0 1 ${x} ${y} Tm <${uhex(String(t))}> Tj ET`);
 const m=(s,z)=>Array.from(String(s)).reduce((n,x)=>n+z*(x===" "?.32:x.charCodeAt(0)<128?(/[WMmw@]/.test(x)?.78:.57):1),0);
 const wrap=(s,z,max)=>{let parts=[],buf="";for(const x of Array.from(String(s))){if(buf&&m(buf+x,z)>max){parts.push(buf);buf=x;}else buf+=x;}if(buf)parts.push(buf);return parts;};
 function page(title="",cont=false){if(ops.length)pages.push(ops.join("\n")+"\n");ops=[];current=title;rect(0,0,W,H,[1,1,1]);rect(0,H-8,W,8,[.08,.22,.36]);draw(L,808,"TERM / ATLAS    ·    MATHEMATICAL STATISTICS",9.5,[.12,.25,.39]);line(L,795,R,795);
  if(title){draw(L,765,title+(cont?"（续）":""),15,[.09,.23,.37]);line(L,750,R,750);y=731;}else y=771;}
 function term(i,t){const h=wrap(`${String(i).padStart(2,"0")}  ${t.en}   /   ${t.zh}${t.abbr?"  ["+t.abbr+"]":""}`,10,480),d=wrap(t.definition,9.2,475),height=h.length*13.5+d.length*12.5+16;if(y-height<61)page(current,true);if(i%2===0)rect(L-4,y-height+2,R-L+8,height+1,[.960,.972,.982]);let yy=y-14;h.forEach(s=>{draw(L+3,yy,s,10,[.06,.18,.32]);yy-=13.5;});d.forEach(s=>{draw(L+14,yy,s,9.2,[.31,.38,.45]);yy-=12.5;});y-=height;}
 function para(s,z=9.4,ind=0,rgb=[.32,.39,.46]){const p=wrap(s,z,R-L-ind-6),needed=p.length*(z+5)+8;if(y-needed<60)page(current,true);p.forEach(x=>{draw(L+ind,y,x,z,rgb);y-=z+5;});y-=8;}
 page();rect(0,632,W,165,[.08,.22,.36]);draw(L,743,"数理统计",29,[1,1,1]);draw(L,703,"Mathematical Statistics",17,[.82,.91,.98]);draw(L,660,"400 条双语术语  ·  16 个专业章节",12,[1,1,1]);
 draw(L,594,"章节目录",14);line(L,577,R,577);
 cs.forEach((c,i)=>draw(L+(i>=8?252:0),551-(i>=8?i-8:i)*29,`${String(c.n).padStart(2,"0")}   ${c.title}`,9.6,[.14,.28,.42]));
 draw(L,236,"从抽样分布与统计推断，延展至回归、贝叶斯和现代统计",10,[.2,.34,.46]);
 draw(L,205,"专业释义与试题为独立创作，计数及字段已自动校验。",9.4,[.28,.37,.45]);
 draw(L,179,"独立专家事实审稿及跨阅读器字体排版检查仍需进行。",9.4,[.28,.37,.45]);
 draw(L,103,"2026-11-27  ·  Professional Chinese-English Glossary",9.8,[.23,.36,.49]);
 for(const c of cs){page(`${String(c.n).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>term(i+1,t));}
 page("附录 A  ·  核心概念辨析");for(let i=0;i<contrasts.length;i++){if(y<125)page(current,true);para(`${i+1}. ${contrasts[i][0]}`,10.7,0,[.08,.23,.36]);para(contrasts[i][1],9.2,13);}
 page("附录 B  ·  中等难度面试问答");for(let i=0;i<interviews.length;i++){if(y<126)page(current,true);para(`Q${i+1}. ${interviews[i][0]}`,10.6,0,[.08,.23,.36]);para(`答：${interviews[i][1]}`,9.2,13);}
 page("附录 C  ·  中等难度考试与解析");for(let i=0;i<exams.length;i++){if(y<126)page(current,true);para(`${i+1}. ${exams[i][0]}`,10.6,0,[.08,.23,.36]);para(`解析：${exams[i][1]}`,9.2,13);}
 page("附录 D  ·  教材与来源");for(let i=0;i<references.length;i++){para(`${i+1}. ${references[i][0]}`,10,0,[.08,.23,.36]);para(references[i][1],8.8,13);}para("本册为独立整理的释义和题解，引用资料的作者并未参与逐项审核。",9.2,0,[.3,.36,.43]);
 if(ops.length)pages.push(ops.join("\n")+"\n");
 const objs=[null];objs[1]="<< /Type /Catalog /Pages 2 0 R >>";
 objs[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${pages.map((_,i)=>`${6+2*i} 0 R`).join(" ")}] >>`;
 objs[3]="<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [<< /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 >>] /ToUnicode 4 0 R >>";
 const cmap=`/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n/CMapName /Identity-UCS2 def\n/CMapType 2 def\n1 begincodespacerange\n<0000> <FFFF>\nendcodespacerange\n1 beginbfrange\n<0000> <FFFF> <0000>\nendbfrange\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n`;
 objs[4]=`<< /Length ${cmap.length} >>\nstream\n${cmap}endstream`;
 objs[5]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
 for(let i=0;i<pages.length;i++){let p=6+2*i,sid=p+1;let stream=pages[i]+".83 .87 .91 RG 0.5 w 48 52 m 548 52 l S\n";
 stream+=`${col([.41,.48,.56])} BT /FC 8 Tf 1 0 0 1 48 35 Tm <${uhex("TERM / ATLAS  ·  Mathematical Statistics")}> Tj ET\n`;
 stream+=`${col([.41,.48,.56])} BT /FC 8 Tf 1 0 0 1 488 35 Tm <${uhex(`${i+1} / ${pages.length}`)}> Tj ET\n`;
 objs[p]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Resources << /Font << /FC 3 0 R >> >> /Contents ${sid} 0 R >>`;
 objs[sid]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;
 }
 let pdf="%PDF-1.4\n%TERM-ATLAS\n",offs=[0];for(let i=1;i<objs.length;i++){offs[i]=pdf.length;pdf+=`${i} 0 obj\n${objs[i]}\nendobj\n`;}
 const xref=pdf.length;pdf+=`xref\n0 ${objs.length}\n0000000000 65535 f \n`;for(let i=1;i<objs.length;i++)pdf+=`${String(offs[i]).padStart(10,"0")} 00000 n \n`;
 pdf+=`trailer\n<< /Size ${objs.length} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;return {pdf,pages:pages.length};
}
const source=Array.from({length:16},(_,i)=>fs.readFileSync(path.join(ROOT,"data/mathematical-statistics/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const chapters=parseData(source),terms=chapters.flatMap(c=>c.terms);
if(chapters.length!==16||chapters.some(c=>c.terms.length!==25)||terms.length!==400||new Set(terms.map(t=>t.en.toLowerCase())).size!==400||terms.some(t=>!t.en||!t.zh||!t.definition))throw Error("Validation failed: expected 400 unique complete terms");
const tsv=Buffer.from(makeTsv(chapters),"utf8"),md=Buffer.from(makeMd(chapters),"utf8"),pdf=Buffer.from(buildPdf(chapters).pdf,"ascii");
const outputs=[["data/mathematical-statistics.tsv",tsv],["glossaries/mathematical-statistics.md",md],["docs/glossaries/mathematical-statistics.md",md],["pdf/mathematical-statistics.pdf",pdf],["docs/pdf/mathematical-statistics.pdf",pdf]];
const check=process.argv.includes("--check");for(const [p,b] of outputs){const f=path.join(ROOT,p);if(check){if(!fs.existsSync(f)||!fs.readFileSync(f).equals(b))throw Error("Not synchronized: "+p)}else{fs.mkdirSync(path.dirname(f),{recursive:true});fs.writeFileSync(f,b)}}
console.log((check?"PASS":"GENERATED")+": 400 terms, 16 chapters, "+outputs.length+" synchronized artifacts");
