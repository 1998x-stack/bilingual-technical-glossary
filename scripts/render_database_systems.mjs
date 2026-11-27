#!/usr/bin/env node
// TERM / ATLAS database systems reproducible publisher (Node.js 18+).
// Usage: node scripts/render_database_systems.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["Database Systems 与 SQL Database","SQL 侧重数据定义与查询语言；数据库系统还需研究页面组织、索引、执行器、优化器、事务和故障恢复等内部机制。"],["B+ Tree 与 LSM Tree","B+ 树通常支持有序随机读与范围访问；LSM 通过内存表及顺序磁盘文件优化写入，但可能承担额外压实、读放大和空间放大。"],["Index Scan 与 Table Scan","索引扫描可减少低选择率查询所需访问页；大范围读取时随机回表可能比顺序扫描更贵，需由代价模型判断。"],["Lock 与 Latch","事务锁通常保护逻辑数据并参与隔离协议；闩锁短时保护共享内存结构，不应跨长事务当成逻辑数据锁使用。"],["两阶段锁 2PL 与严格 2PL","普通 2PL 在释放首个锁后不再获取新锁；严格 2PL 还要求排他锁持有到事务结束，减少脏读写与恢复复杂度。"],["Snapshot Isolation 与 Serializability","SI 读一致快照并通常阻止写写冲突，但可能写偏斜；可串行化要求与某个合法串行事务执行等价。"],["MVCC 与隔离级别","MVCC 是保存与选择版本的实现技术，不是固定隔离级别；它可实现 RC、SI 或配合冲突检测实现可串行化。"],["WAL 与 Checkpoint","WAL 规定数据页刷盘前日志先持久化；Checkpoint 记录恢复所需状态，以减少重启时需要扫描和重放的日志量。"],["Steal/No-steal 与 Force/No-force","前者决定未提交脏页是否允许刷盘，影响是否需要 Undo；后者决定提交时是否强制刷数据页，影响是否需要 Redo。"],["Hash Join 与 Sort–Merge Join","哈希连接常适合等值条件；归并连接利用两侧有序输入，在范围顺序或已排序数据下可能更有优势。"],["逻辑查询计划与物理查询计划","逻辑计划描述结果应如何通过关系运算得到；物理计划选择实际扫描、连接、排序及资源实现算法。"],["Quorum 与线性一致性","有交集的读写仲裁只是协议设计所需条件之一；并发版本比较、失败模型、日志复制及客户端行为还决定最终一致性保证。"],["OLTP 与 OLAP","OLTP 面向高并发短事务和点查；OLAP 面向长扫描、聚合和列裁剪；HTAP 探索同时支持两者的架构。"],["行式存储与列式存储","行式布局使单条记录更新和点查集中；列式布局通常更利于扫描少数列、列内压缩与向量化执行。"]];
const interviews=[["为什么查询优化器可能宁愿全表扫描而不使用已存在的索引？","当谓词选择率很低或大量记录都需要回表时，随机 I/O 与索引遍历成本可能超过顺序扫描；应结合行数、缓存和统计信息判断。"],["数据库中的 B+ 树叶节点一定只存记录指针吗？","不是。二级索引常存记录定位信息，聚簇索引的叶节点可直接保存完整记录或数据；物理布局依引擎而异。"],["如何解释 LSM 的写入、读取与空间放大之间的权衡？","小量增量数据先顺序落盘提高写入效率；更多有序文件会增大查询合并和存储占用，后台压实降低读放大却产生额外写入。"],["为什么 MVCC 不等于可串行化？","版本管理降低读写阻塞但不自动排除读写依赖环；快照隔离可能允许写偏斜，需额外检测或同步规则。"],["事务锁与 B+ 树闩锁为什么不应混用？","事务锁用于逻辑冲突及可能持续整个事务；闩锁仅保护页或内存指针更新，长时间持有会严重阻塞索引并发。"],["为什么提交事务后部分脏页仍未刷盘不会必然丢数据？","在 WAL 的非强制写页设计中，提交日志先被可靠持久化，重启后恢复模块可以据日志 Redo 已提交变更。"],["ARIES 的分析、重做、撤销分别解决什么问题？","分析恢复事务和脏页状态，重做重演必要历史变更，撤销清理未完成事务并记录补偿日志以支持再次崩溃恢复。"],["为什么 2PC 不是分布式一致性算法的替代品？","2PC 协调参与者的原子提交决定，协调者失效时可能阻塞；复制组共识用于在规定故障条件下维持成员对日志顺序或决议一致。"],["如何区别逻辑计划错误和优化器估算错误？","逻辑计划若改变 SQL 的 NULL、重复行或谓词语义会产生错误答案；基数估计失准通常仍输出正确结果但选择效率低的物理计划。"],["数据库线上一次 P99 延迟显著上升，优先检查什么？","将慢查询按等待锁、执行算子、缓存命中、I/O、GC/压实、复制滞后及连接池排队拆分，再比较基线、执行计划与关键指标。"]];
const exams=[["一张表 1,000,000 行，过滤谓词选择率为 0.02，预计返回多少行？","在选择率估计可信且无其他过滤的假设下，1,000,000×0.02=20,000 行。"],["B+ 树每个内部节点最多 100 个子节点，从根到叶需经过 3 层内部节点，理论可索引约多少叶节点？","满树近似可到 100³=1,000,000 个叶节点；实际填充率和根结构会改变数字。"],["缓冲池有 1,024 帧、每帧 8 KiB，总数据页缓存容量是多少？","1,024×8 KiB=8,192 KiB=8 MiB，不含额外管理结构。"],["表 R 有 1,000 行、S 有 200 行，无过滤笛卡尔积最多产生多少行？","1,000×200=200,000 行。"],["两个事务分别读取医生 A/B 的值且各修改不同医生排班，SI 是否足以阻止共同破坏约束？","不一定；这是典型写偏斜，两事务写集合不同，可能都提交并违反跨行业务约束。"],["如果 WAL 写入已经持久化但相应数据页尚未刷盘，崩溃后需要什么恢复操作？","应依据日志重做必要更新；对于未完成事务，还需按具体恢复协议执行撤销。"],["每秒可完成 2,000 个事务，其中 98% 成功，成功 TPS 为多少？","若 2,000 表示尝试事务数，成功吞吐为 2,000×0.98=1,960 TPS。"],["某事务在严格 2PL 中持有排他锁，提交前能否提前释放该锁？","不能，严格 2PL 要求排他锁保留至提交或回滚，以保护未提交修改。"],["三个副本组成多数派复制组，通常需要多少副本可达才能形成多数派？","floor(3/2)+1=2 个；但可形成多数派并不独立证明端到端线性一致性。"],["某分析查询只读取 100 列中的 5 列，在各列大小相同且无其他开销情况下，列式扫描的理想读取比例是多少？","5/100=5%；实际读取比例还受块大小、索引、压缩和谓词要求影响。"]];
const references=[["CMU 15-445/645: Database Systems (Fall 2026)","https://15445.courses.cs.cmu.edu/fall2026/"],["PostgreSQL Documentation: Concurrency Control and MVCC","https://www.postgresql.org/docs/current/mvcc.html"],["PostgreSQL Documentation: Write-Ahead Logging","https://www.postgresql.org/docs/current/wal.html"],["PostgreSQL Documentation: Using EXPLAIN","https://www.postgresql.org/docs/current/using-explain.html"],["SQLite: Architecture of SQLite","https://www.sqlite.org/arch.html"],["SQLite: Query Planning","https://www.sqlite.org/queryplanner.html"],["RocksDB Wiki: Compaction","https://github.com/facebook/rocksdb/wiki/Compaction"],["RocksDB Wiki: RocksDB Overview","https://github.com/facebook/rocksdb/wiki/RocksDB-Overview"],["Mohan et al. (1992): ARIES Recovery Algorithm (IBM)","https://research.ibm.com/publications/aries-a-transaction-recovery-method-supporting-fine-granularity-locking-and-partial-rollbacks-using-write-ahead-logging"],["CockroachDB Documentation: Architecture Overview","https://www.cockroachlabs.com/docs/stable/architecture/overview.html"],["Jepsen: Consistency Models","https://jepsen.io/consistency/models"]];
function parseData(raws){const cs=[];let c=null;for(const raw of raws){for(const line of raw.split(/\r?\n/)){if(!line)continue;if(line.startsWith("# ")){if(c)cs.push(c);c={n:cs.length+1,title:line.slice(2),terms:[]};continue;}const p=line.split("|");if(!c||p.length!==4)throw Error("Invalid source row: "+line);c.terms.push({en:p[0].trim(),zh:p[1].trim(),abbr:p[2].trim(),definition:p[3].trim()});}}if(c)cs.push(c);return cs;}
function makeTsv(cs){return "# 数据库系统 / Database Systems\n# Canonical source: data/database-systems/chapters/*.tsv\n"+cs.map(c=>`# ${String(c.n).padStart(2,"0")}. ${c.title}\n`+c.terms.map(t=>[t.en,t.zh,t.abbr,t.definition].join("|")).join("\n")).join("\n\n")+"\n";}
function makeMd(cs){
const out=["# 数据库系统 · Database Systems","",
"> TERM / ATLAS · 专业中英文术语手册 | Bilingual Technical Glossary","",
"**400 条双语术语 · 16 个专业章节 · 2026-11-27**","",
"区别于已有 SQL 数据库语法手册，本册以数据库内核、存储引擎和系统实现为主线，涵盖物理页与缓冲池、B+ 树/LSM、执行器、查询优化器、并发控制与事务隔离、WAL/ARIES、分布式复制与分析系统。",
"",
"**适用条件：**不同数据库对隔离级别、索引叶节点布局、锁模式与故障持久化的具体实现可能不同；定义中的一般性质应以正在使用的数据库版本和官方文档核对。","",
"**审稿状态：**自动结构和去重检查已完成；独立专家逐条技术事实审稿及 PDF 跨阅读器视觉检查仍待完成。","",
"## 章节目录","",...cs.map(c=>`- ${String(c.n).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),"","---",""];
for(const c of cs){out.push(`## ${String(c.n).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 专业定义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en} | ${t.zh} | ${t.abbr} | ${t.definition} |`),"");}
out.push("## 核心概念辨析","","| 对比对象 | 技术区别 |","|---|---|",...contrasts.map(x=>`| ${x[0]} | ${x[1]} |`),"","## 中等难度面试题与解析","");
interviews.forEach((x,i)=>out.push(`### 面试题 ${i+1}：${x[0]}`,"",`**参考答案：**${x[1]}`,""));
out.push("## 中等难度考试题与解析","");
exams.forEach((x,i)=>out.push(`### 考试题 ${i+1}：${x[0]}`,"",`**解析：**${x[1]}`,""));
out.push("## 官方资料与学术参考","","本册参照系统课程、数据库官方文档和恢复论文构建知识体系；引用不代表原作者已审阅本项目所有词条。","",...references.map((x,i)=>`${i+1}. [${x[0]}](${x[1]})`),"",
"## 编辑与再现","","- 原始数据：`data/database-systems/chapters/*.tsv`，每行 `English|中文|abbr|definition`。","- 生成文件：`data/database-systems.tsv`、`glossaries/database-systems.md`、`pdf/database-systems.pdf` 和 `docs/` 镜像。","- 构建与只读校验：`node scripts/render_database_systems.mjs` 和 `node scripts/render_database_systems.mjs --check`。","- 本册独立出版，**尚未进入网站的正式术语搜索索引**，不计入原有索引计数，也不代表已经生成 400 篇深度 Wiki。");
return out.join("\n")+"\n";
}
function toHex(s){let out="";for(let i=0;i<s.length;i++)out+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return out;}
function base64(s){const A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",v=[];for(let i=0;i<s.length;i+=3){const a=s.charCodeAt(i),b=i+1<s.length?s.charCodeAt(i+1):0,c=i+2<s.length?s.charCodeAt(i+2):0;v.push(A[a>>2],A[((a&3)<<4)|(b>>4)],i+1<s.length?A[((b&15)<<2)|(c>>6)]:"=",i+2<s.length?A[c&63]:"=");}return v.join("");}
function makePdf(cs){
const W=595,H=842,L=46,R=549,pages=[];let ops=[],section="",y=0;
const col=c=>c.join(" ")+" rg",rect=(x,b,w,h,c)=>ops.push(col(c),`${x} ${b} ${w} ${h} re f`);
const line=b=>ops.push(".83 .87 .91 RG","0.5 w",`${L} ${b} m ${R} ${b} l S`);
const draw=(x,b,s,size=10,c=[.10,.24,.35])=>ops.push(col(c),`BT /FC ${size} Tf 1 0 0 1 ${x.toFixed(1)} ${b.toFixed(1)} Tm <${toHex(String(s))}> Tj ET`);
const mw=(s,z)=>Array.from(String(s)).reduce((n,ch)=>n+z*(ch===" "?.34:ch.charCodeAt(0)<128?(/[MWmw@]/.test(ch)?.83:.57):1),0);
const wrap=(s,z,max)=>{const ls=[];let t="";for(const ch of Array.from(String(s))){if(t&&mw(t+ch,z)>max){ls.push(t);t=ch}else t+=ch;}if(t)ls.push(t);return ls;};
function page(title="",cont=false){if(ops.length)pages.push(ops.join("\n")+"\n");ops=[];section=title;rect(0,0,W,H,[1,1,1]);rect(0,834,W,8,[.06,.20,.32]);draw(L,806,"TERM / ATLAS   ·   DATABASE SYSTEMS",9.8,[.09,.28,.42]);line(791);if(title){draw(L,759,title+(cont?"（续）":""),14.9,[.07,.24,.38]);line(745);y=729;}else y=767;}
function term(i,t){const heading=wrap(`${String(i).padStart(2,"0")}  ${t.en}   /   ${t.zh}${t.abbr?"  ["+t.abbr+"]":""}`,9.8,482),description=wrap(t.definition,9.1,477),h=heading.length*13.6+description.length*12.5+15;if(y-h<63)page(section,true);if(i%2===0)rect(L-4,y-h+3,R-L+8,h,[.963,.975,.983]);let yy=y-13;for(const s of heading){draw(L+3,yy,s,9.8,[.06,.22,.35]);yy-=13.6;}for(const s of description){draw(L+16,yy,s,9.1,[.30,.39,.46]);yy-=12.5;}y-=h;}
function para(s,size=9.25,indent=0,c=[.3,.39,.47]){const parts=wrap(s,size,R-L-indent-6);if(y-parts.length*(size+5)-9<62)page(section,true);for(const p of parts){draw(L+indent,y,p,size,c);y-=size+5;}y-=9;}
page();rect(0,625,W,172,[.06,.20,.32]);draw(L,742,"数据库系统",29,[1,1,1]);draw(L,702,"Database Systems",18,[.85,.93,.98]);draw(L,663,"400 条专业术语   ·   16 个知识章节",12,[1,1,1]);draw(L,595,"DATABASE SYSTEMS / KNOWLEDGE MAP",11,[.09,.28,.41]);line(578);
cs.forEach((c,i)=>draw(L+(i>=8?258:0),548-(i>=8?i-8:i)*29,`${String(c.n).padStart(2,"0")}  ${c.title}`,9.4,[.12,.29,.42]));
draw(L,231,"从页与索引，到执行器、事务、恢复和分布式数据库",10,[.19,.34,.47]);draw(L,206,"原始数据及生成文件均可复现；专业审稿仍须独立执行。",9.4,[.29,.39,.46]);draw(L,102,"2026-11-27  |  TERM / ATLAS",10,[.22,.37,.49]);
for(const c of cs){page(`${String(c.n).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>term(i+1,t));}
page("附录 A · 核心概念辨析");contrasts.forEach((x,i)=>{if(y<120)page(section,true);para(`${i+1}. ${x[0]}`,10.5,0,[.08,.25,.38]);para(x[1],9.2,14);});
page("附录 B · 中等难度面试题");interviews.forEach((x,i)=>{if(y<130)page(section,true);para(`Q${i+1}. ${x[0]}`,10.4,0,[.08,.25,.38]);para(`答：${x[1]}`,9.2,14);});
page("附录 C · 中等难度考试题");exams.forEach((x,i)=>{if(y<130)page(section,true);para(`${i+1}. ${x[0]}`,10.4,0,[.08,.25,.38]);para(`解析：${x[1]}`,9.2,14);});
page("附录 D · 官方资料与学术参考");references.forEach((x,i)=>{para(`${i+1}. ${x[0]}`,9.8,0,[.08,.25,.38]);para(x[1],8.6,14);});
para("本册为独立撰写的教育型术语手册，参考文献作者未参与逐条专业审稿。",9.25,0,[.3,.38,.45]);
if(ops.length)pages.push(ops.join("\n")+"\n");
const obj=[null];obj[1]="<< /Type /Catalog /Pages 2 0 R >>";obj[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${pages.map((_,i)=>`${6+2*i} 0 R`).join(" ")}] >>`;
obj[3]="<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [<< /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 >>] /ToUnicode 4 0 R >>";
const cmap="/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n/CMapName /Identity-UCS2 def\n/CMapType 2 def\n1 begincodespacerange\n<0000> <FFFF>\nendcodespacerange\n1 beginbfrange\n<0000> <FFFF> <0000>\nendbfrange\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n";
obj[4]=`<< /Length ${cmap.length} >>\nstream\n${cmap}endstream`;obj[5]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
for(let i=0;i<pages.length;i++){const pn=6+2*i,s=pn+1;let stream=pages[i]+".83 .87 .91 RG 0.5 w 46 51 m 549 51 l S\n";
stream+=`${col([.40,.48,.56])} BT /FC 8 Tf 1 0 0 1 46 34 Tm <${toHex("TERM / ATLAS  ·  Database Systems")}> Tj ET\n`;
stream+=`${col([.40,.48,.56])} BT /FC 8 Tf 1 0 0 1 486 34 Tm <${toHex(`${i+1} / ${pages.length}`)}> Tj ET\n`;
obj[pn]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Resources << /Font << /FC 3 0 R >> >> /Contents ${s} 0 R >>`;
obj[s]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;}
let pdf="%PDF-1.4\n%TERM-ATLAS\n",offset=[0];for(let i=1;i<obj.length;i++){offset[i]=pdf.length;pdf+=`${i} 0 obj\n${obj[i]}\nendobj\n`;}
const xp=pdf.length;pdf+=`xref\n0 ${obj.length}\n0000000000 65535 f \n`;for(let i=1;i<obj.length;i++)pdf+=`${String(offset[i]).padStart(10,"0")} 00000 n \n`;
pdf+=`trailer\n<< /Size ${obj.length} /Root 1 0 R >>\nstartxref\n${xp}\n%%EOF\n`;return {pdf,pages:pages.length};
}
const raw=Array.from({length:16},(_,i)=>fs.readFileSync(path.join(ROOT,"data/database-systems/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const cs=parseData(raw),terms=cs.flatMap(c=>c.terms);
if(cs.length!==16||cs.some(c=>c.terms.length!==25)||terms.length!==400||new Set(terms.map(t=>t.en.toLowerCase())).size!==400||terms.some(t=>!t.en||!t.zh||!t.definition))throw Error("Expected 400 unique, nonempty terms in 16 chapters");
const tsv=Buffer.from(makeTsv(cs),"utf8"),md=Buffer.from(makeMd(cs),"utf8"),pdf=Buffer.from(makePdf(cs).pdf,"ascii");
const outputs=[["data/database-systems.tsv",tsv],["glossaries/database-systems.md",md],["docs/glossaries/database-systems.md",md],["pdf/database-systems.pdf",pdf],["docs/pdf/database-systems.pdf",pdf]];
const check=process.argv.includes("--check");
for(const [rel,buf] of outputs){const filename=path.join(ROOT,rel);if(check){if(!fs.existsSync(filename)||!fs.readFileSync(filename).equals(buf))throw Error("Generated file not synchronized: "+rel);}else{fs.mkdirSync(path.dirname(filename),{recursive:true});fs.writeFileSync(filename,buf);}}
console.log((check?"PASS":"GENERATED")+": 400 terms, 16 chapters, "+outputs.length+" artifacts");
