#!/usr/bin/env node
// Deterministic single-domain PDF / Markdown build. Run: node scripts/render_algorithms.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["O / Ω / Θ","分别表示渐近上界、下界与紧界。"],["贪心 / 动态规划","贪心依赖可证明的局部选择性质；动态规划比较并缓存子问题最优解。"],["分治 / 动态规划","分治子问题通常独立；动态规划利用重叠子问题。"],["BFS / Dijkstra","BFS 用于等权或无权路径；Dijkstra 要求所有可用边权非负。"],["NP-hard / NP-complete","NP 完全必须属于 NP 且 NP 困难；NP 困难不必属于 NP。"],["最短路径 / 最小生成树","前者优化指定路径代价；后者优化连通全部顶点的边权总和。"],["摊还 / 平均复杂度","摊还约束操作序列并不依赖随机分布；平均复杂度需指定输入分布。"],["最大流 / 最小割","最大流量与最小源汇割容量由最大流最小割定理联系。"]];
const questions=[["比较排序为何需要 Ω(n log n) 次比较？","比较决策树需区分 n! 种排列，树高至少 log₂(n!)。"],["0-1 背包的一维 DP 为什么逆序枚举容量？","避免同一物品在本轮状态转移中被重复选择。"],["Dijkstra 为什么不能直接处理负边权？","贪心确定当前最短距离的性质需要非负边权。"],["如何证明 NP 完全性？","证明属于 NP，再从已知 NP 完全问题给出保真假实例的多项式归约。"],["最小生成树与最短路区别是什么？","前者最小化连接全图的总边权；后者优化指定顶点间路径权值。"],["二分图最大匹配怎样转成最大流？","源到左侧、左右匹配边、右侧到汇点均赋单位容量，最大流即匹配规模。"]];
function parseData(raws){return raws.map((s,i)=>{const a=s.trim().split(/\r?\n/);let title=a.shift().slice(2);return {number:i+1,title,terms:a.map(x=>{const [en,zh,abbr,definition]=x.split("|");return {en,zh,abbr,definition}})}});}
function makeTsv(cs){return "# 算法设计与分析 / Algorithm Design and Analysis\n# Generated from data/algorithms/chapters/*.tsv\n"+cs.map(c=>`# ${String(c.number).padStart(2,"0")}. ${c.title}\n`+c.terms.map(x=>[x.en,x.zh,x.abbr,x.definition].join("|")).join("\n")).join("\n\n")+"\n";}
function makeMd(cs){
 const out=["# 算法设计与分析 · Algorithm Design and Analysis","> 专业技术术语中英文对照表 | Bilingual Technical Glossary","",`**总量：500 条 · 15 个专题 · 2026-11-26**`,"","中文定义由本项目原创撰写，面向算法课程、技术面试与专业考试。部分术语依赖计算模型或输入假设；请以参考教材与原论文为准。","**审稿状态：**已进行数量、结构和重复检查；尚未取得独立专家逐条事实审稿。","", "## 目录",...cs.map(c=>`- ${String(c.number).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),""];
 for(const c of cs){out.push(`## ${String(c.number).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 简明释义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en} | ${t.zh} | ${t.abbr} | ${t.definition} |`),"")}
 out.push("## 核心概念辨析","","| 概念 | 关键区别 |","|---|---|",...contrasts.map(x=>`| ${x[0]} | ${x[1]} |`),"","## 中等难度面试与考试自测","");
 questions.forEach((q,i)=>out.push(`### ${i+1}. ${q[0]}`,"",`参考答案：${q[1]}`,""));
 out.push("## 参考资料","","- Cormen, Leiserson, Rivest, Stein. *Introduction to Algorithms*, 4th ed. MIT Press, 2022.","- Kleinberg & Tardos. *Algorithm Design*. Pearson, 2005.","- Sedgewick & Wayne. *Algorithms*, 4th ed. Addison-Wesley, 2011.","- Skiena. *The Algorithm Design Manual*, 3rd ed. Springer, 2020.","- Princeton Algorithms: https://algs4.cs.princeton.edu/home/","- MIT OpenCourseWare: https://ocw.mit.edu/","- CP-Algorithms (补充材料): https://cp-algorithms.com/","","> 本册为独立撰写的短定义和索引，不代表参考资料作者的审稿认可。");
 return out.join("\n")+"\n";
}
function hexU(s){let out="";for(let i=0;i<s.length;i++)out+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return out;}
function b64(s){const a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",out=[];for(let i=0;i<s.length;i+=3){let x=s.charCodeAt(i),y=i+1<s.length?s.charCodeAt(i+1):0,z=i+2<s.length?s.charCodeAt(i+2):0;out.push(a[x>>2],a[((x&3)<<4)|(y>>4)],i+1<s.length?a[((y&15)<<2)|(z>>6)]:"=",i+2<s.length?a[z&63]:"=")}return out.join("");}
function makePdf(cs){
 const WIDTH=595,HEIGHT=842,PAD=45,MAX=550,pg=[];let ops=[],y=0,section="";
 function col(c){return c.join(" ")+" rg"}
 function textAt(x,y,t,size=10,c=[.13,.23,.35]){ops.push(col(c),`BT /FZ ${size} Tf 1 0 0 1 ${x} ${y} Tm <${hexU(String(t))}> Tj ET`)}
 function box(x,y,w,h,c){ops.push(col(c),`${x} ${y} ${w} ${h} re f`)}
 function drawLine(x,y,x2,y2){ops.push(".83 .87 .91 RG","0.5 w",`${x} ${y} m ${x2} ${y2} l S`)}
 function measure(s,size){return Array.from(s).reduce((n,ch)=>n+size*(ch===" "? .34 :ch.charCodeAt(0)<128? .58:1),0)}
 function lines(s,size,max=488){let out=[],buf="";for(const ch of Array.from(s)){if(buf&&measure(buf+ch,size)>max){out.push(buf);buf=""}buf+=ch;}if(buf)out.push(buf);return out}
 function page(name="",cont=false){
  if(ops.length)pg.push(ops.join("\n")+"\n");
  ops=[];section=name;box(0,0,WIDTH,HEIGHT,[1,1,1]);box(0,835,595,7,[.08,.25,.39]);
  textAt(PAD,807,"TERM / ATLAS   ·   算法设计与分析",10);
  drawLine(PAD,793,MAX,793);
  if(name){textAt(PAD,764,name+(cont?"（续）":""),16,[.05,.23,.37]);drawLine(PAD,748,MAX,748);y=734;}else y=752;
 }
 function term(i,t){
  const heads=lines(`${i}. ${t.en}  /  ${t.zh}${t.abbr?" ["+t.abbr+"]":""}`,10.2);
  const defs=lines(t.definition,9.0,475);const h=heads.length*14+defs.length*13+13;
  if(y-h<62)page(section,true);
  if(i%2===0)box(PAD-3,y-h+2,MAX-PAD+7,h,[.96,.973,.981]);
  let yy=y-12;for(const h of heads){textAt(PAD+2,yy,h,10.2,[.05,.18,.31]);yy-=14;}
  for(const d of defs){textAt(PAD+16,yy,d,9,[.31,.38,.45]);yy-=13;}y-=h;
 }
 page();
 box(0,627,595,170,[.08,.25,.39]);
 textAt(PAD,736,"算法设计与分析",27,[1,1,1]);
 textAt(PAD,698,"Algorithm Design and Analysis",16,[.86,.93,1]);
 textAt(PAD,654,"500 条术语    15 个章节    中英双语",12,[1,1,1]);
 textAt(PAD,593,"术语目录",15);drawLine(PAD,576,MAX,576);
 cs.forEach((c,i)=>textAt(PAD+(i>=8?257:0),548-(i>=8?i-8:i)*29,`${String(c.number).padStart(2,"0")} ${c.title} (${c.terms.length})`,10));
 textAt(PAD,233,"编辑与审稿说明",12);
 textAt(PAD,204,"定义原创整理；已核对记录数量、数据结构与英文术语唯一性。",9.6);
 textAt(PAD,181,"仍需独立领域专家逐条复核技术定义与适用条件。",9.6);
 textAt(PAD,103,"2026.11  ·  TERM / ATLAS",10);
 for(const c of cs){page(`${String(c.number).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>term(i+1,t));}
 page("附录 A  核心概念辨析");
 contrasts.forEach((x,i)=>{let ds=lines(x[1],9.4,465),h=38+ds.length*13;if(y-h<66)page(section,true);textAt(PAD,y-13,`${i+1}. ${x[0]}`,11);let yy=y-30;ds.forEach(s=>{textAt(PAD+15,yy,s,9.4,[.33,.39,.45]);yy-=13});y-=h});
 page("附录 B  中等难度自测");
 questions.forEach((q,i)=>{let qs=lines(`${i+1}. ${q[0]}`,10.4),as=lines("参考答案："+q[1],9.2),h=qs.length*15+as.length*13+19;if(y-h<66)page(section,true);let yy=y-12;qs.forEach(s=>{textAt(PAD,yy,s,10.4);yy-=15});as.forEach(s=>{textAt(PAD+10,yy,s,9.2,[.30,.37,.45]);yy-=13});y-=h});
 page("附录 C  参考资料");
 ["Cormen et al. Introduction to Algorithms, 4th ed., MIT Press, 2022.","Kleinberg & Tardos. Algorithm Design, Pearson, 2005.","Sedgewick & Wayne. Algorithms, 4th ed., Addison-Wesley, 2011.","Skiena. The Algorithm Design Manual, 3rd ed., Springer, 2020.","https://algs4.cs.princeton.edu/home/","https://ocw.mit.edu/","https://cp-algorithms.com/"].forEach((x,i)=>{textAt(PAD,y-14,`${i+1}. ${x}`,10);y-=30});
 textAt(PAD,337,"本册原创撰写，并非对书籍的逐句复制或作者审稿认可。",10);
 if(ops.length)pg.push(ops.join("\n")+"\n");
 const fonts="[1 [207 270 342 467 462 797 710 239 374] 10 [374 423 605 238 375 238 334 462] 18 26 462 27 28 238 29 31 605 32 [344 748 684 560 695 739 563 511 729 793 318 312 666 526 896 758 772 544 772 628 465 607 753 711 972 647 620 607 374 333 374 606 500 239 417 503 427 529 415 264 444 518 241 230 495 228 793 527 524] 81 [524 504 338 336 277 517 450 652 466 452 407 370 258 370 605]]";
 const obj=[null];obj[1]="<< /Type /Catalog /Pages 2 0 R >>";obj[2]=`<< /Type /Pages /Count ${pg.length} /Kids [${pg.map((_,i)=>`${5+i*2} 0 R`).join(" ")}] >>`;
 obj[3]=`<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [ << /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 /W ${fonts} >> ] >>`;
 obj[4]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
 pg.forEach((p,i)=>{let id=5+i*2,contentID=id+1;const foot=".83 .87 .91 RG 0.5 w 45 51 m 550 51 l S\n"+col([.41,.48,.55])+` BT /FZ 8 Tf 1 0 0 1 45 34 Tm <${hexU("TERM / ATLAS · Algorithms")}> Tj ET\n`+col([.41,.48,.55])+` BT /FZ 8 Tf 1 0 0 1 498 34 Tm <${hexU(`${i+1} / ${pg.length}`)}> Tj ET\n`;let stream=p+foot;obj[id]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /FZ 3 0 R >> >> /Contents ${contentID} 0 R >>`;obj[contentID]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;});
 let pdf="%PDF-1.4\n%TERM-ATLAS\n",pos=[0];for(let i=1;i<obj.length;i++){pos.push(pdf.length);pdf+=`${i} 0 obj\n${obj[i]}\nendobj\n`;}let xref=pdf.length;pdf+=`xref\n0 ${obj.length}\n0000000000 65535 f \n`;for(let i=1;i<obj.length;i++)pdf+=`${String(pos[i]).padStart(10,"0")} 00000 n \n`;pdf+=`trailer\n<< /Size ${obj.length} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;return {pdf,pages:pg.length};
}
const sources=Array.from({length:15},(_,i)=>fs.readFileSync(path.join(ROOT,"data/algorithms/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const c=parseData(sources),list=c.flatMap(x=>x.terms);
if(c.map(x=>x.terms.length).join(",")!=="30,35,40,25,30,40,25,60,35,30,25,25,35,35,30"||list.length!==500||new Set(list.map(x=>x.en.toLowerCase())).size!==500)throw Error("term validation failure");
const tsv=makeTsv(c),md=makeMd(c),pdf=Buffer.from(makePdf(c).pdf,"ascii");
const outputs=[["data/algorithms.tsv",Buffer.from(tsv)],["glossaries/algorithms.md",Buffer.from(md)],["docs/glossaries/algorithms.md",Buffer.from(md)],["pdf/algorithms.pdf",pdf],["docs/pdf/algorithms.pdf",pdf]];
const check=process.argv.includes("--check");for(const [p,b] of outputs){const f=path.join(ROOT,p);if(check){if(!fs.existsSync(f)||!fs.readFileSync(f).equals(b))throw Error("Out of sync: "+p)}else{fs.mkdirSync(path.dirname(f),{recursive:true});fs.writeFileSync(f,b)}}
console.log((check?"PASS":"GENERATED")+": 500 terms, 15 chapters, "+outputs.length+" artifacts");
