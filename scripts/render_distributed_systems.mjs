#!/usr/bin/env node
// TERM/ATLAS: reproducible single-subject publisher for distributed systems.
// node scripts/render_distributed_systems.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["线性一致性 vs 可串行化","线性一致性主要约束对象操作的单点生效及实时顺序；可串行化约束跨对象事务可等价为某串行次序。严格可串行化同时包含事务与实时顺序约束。"],["CAP 可用性 vs 业务高可用","CAP 可用性要求非故障节点对每个请求最终响应；工程上的高可用常用 SLO、故障时间与成功率衡量，不可混用。"],["最终一致性 vs 因果一致性","最终一致性强调无新更新时的最终收敛；因果一致性还要求观察结果遵守因果先后关系。"],["Paxos vs Raft","两者皆可实现复制状态机共识；Paxos 从提案仲裁出发，Raft 强调任期、主节点与日志复制的结构化设计。"],["复制 vs 分片","复制为同一逻辑数据保存多个副本；分片把不同数据子集分布在节点上，两者可以组合。"],["同步复制 vs 异步复制","同步策略在成功确认前等待规定数量副本；异步策略先响应再复制，吞吐和失效时数据丢失风险不同。"],["2PC vs Saga","2PC 通过参与者准备与统一决议实现原子提交，但可能阻塞；Saga 通过本地提交和业务补偿处理跨服务流程，通常不提供同样强的隔离性。"],["至少一次投递 vs 恰好一次效果","至少一次可重试但可能重复；恰好一次状态效果依赖去重、事务提交或幂等业务端，并须说明保证边界。"],["事件时间 vs 处理时间","事件时间表示业务事件发生时刻；处理时间由流处理节点当前时钟决定，迟到数据会令窗口结果不同。"],["租约 vs 隔离令牌","租约靠有限时效授权，旧持有者暂停后可能复活；隔离令牌使受保护资源拒绝过期世代操作。"],["故障检测 vs 故障确定","异步网络中超时可能源于延迟而非崩溃，实用故障检测通常只能给出怀疑而不能证明。"],["吞吐量 vs 尾延迟","更高吞吐不代表更低 P99；排队和扇出可使高百分位延迟在资源饱和时迅速上升。"]];
const interviews=[["为何网络分区时不能同时保证线性一致性与 CAP 可用性？","两个无法通信的分区若都必须立即完成读写，就无法就跨分区最新值协调；要守住实时顺序，一侧可能需要拒绝或等待。"],["Raft 中为何不能仅凭多数派复制就任意提交旧任期日志？","Raft 提交规则需结合当前任期条目与日志匹配性质，否则不同任期选举可能让旧条目被覆盖；当前任期条目一旦按规则提交，其前缀也随之提交。"],["为什么仅有 N=3、R=2、W=2 的数量配置不一定得到线性一致性？","需要明确同步确认、版本冲突、失败模型和读写路径；松散仲裁、并发写、节点临时承接等可破坏简单交集推理。"],["逻辑时钟能否推断真实经过了多少毫秒？","不能；Lamport 时钟只保持一类因果顺序信息，不测量真实时间间隔。"],["如何避免带超时的分布式锁让旧主继续写入？","由存储服务验证单调递增隔离令牌，拒绝旧令牌；仅靠租约客户端本地判断不足。"],["一次 RPC 超时后，客户端能否断言服务端未执行？","不能；响应可能丢失或延迟。重试必须考虑幂等键、请求去重或业务补偿。"],["为什么快照隔离仍可能产生写偏斜？","两个事务在同一快照下读到合法前置条件，却修改不同记录，双方不发生同键写冲突而联合结果破坏跨行约束。"],["2PC 的阻塞性体现在哪里？","参与者完成准备并持久化锁定资源后，如果协调者失联，可能无法确定全局决议而必须等待恢复或外部协调。"]];
const exams=[["向量时钟 [2,1,0] 与 [1,2,0] 是否有因果先后？","两向量分别在不同维度领先，既不逐分量小于等于对方，故可视为并发事件。"],["五节点 Raft 集群可承受几个崩溃节点仍继续提交？","使用多数派投票时需至少三个节点在线并可互通，因此通常可承受两个节点崩溃。"],["N=5 的多数派大小是多少？","floor(5/2)+1=3，任意两个大小为 3 的多数派必有至少一个共同成员。"],["三个后端延迟分别为 20、50、80ms 并行扇出，若汇总须等全部完成，理论最短完成时间？","忽略网络与聚合开销时取最长依赖分支，即 80ms，而不是三者求和。"],["故障后允许最多丢失 15 分钟数据、2 小时内恢复，分别对应什么指标？","RPO=15 分钟，RTO=2 小时；前者关注数据可恢复点，后者关注服务恢复时限。"],["若到达率 100 req/s、平均系统内停留时间 0.2s，平均在途请求数是多少？","在满足稳定性等利特尔定律假设时，L=λW=100×0.2=20 个。"],["一个节点每秒处理 300 请求、到达 390 请求，队列会怎样？","若持续超出服务能力且无丢弃或背压，队列期望持续增长，等待延迟无法长期稳定。"],["两阶段提交中的 prepare 阶段允许参与者提前释放全部锁吗？","一般不能；参与者须保证最终提交决议可实现，提前释放可能破坏事务隔离或原子性前提。"]];
const references=[["Designing Data-Intensive Applications, 2nd ed. (Kleppmann & Riccomini)","https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/"],["Time, Clocks, and the Ordering of Events in a Distributed System (Lamport, 1978)","https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/"],["Paxos Made Simple (Lamport, 2001)","https://www.microsoft.com/en-us/research/publication/paxos-made-simple/"],["In Search of an Understandable Consensus Algorithm (Ongaro & Ousterhout, 2014)","https://raft.github.io/"],["Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al., 2007)","https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store"],["MapReduce: Simplified Data Processing on Large Clusters (Dean & Ghemawat, 2004)","https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/"],["Spanner: TrueTime and external consistency (Google Cloud documentation)","https://docs.cloud.google.com/spanner/docs/true-time-external-consistency"],["Jepsen: Consistency Models","https://jepsen.io/consistency/models"]];
function parseData(raws){const chapters=[];let c=null;for(const raw of raws){for(const line of raw.trim().split(/\r?\n/)){if(!line)continue;if(line.startsWith("# ")){if(c)chapters.push(c);c={n:chapters.length+1,title:line.slice(2),terms:[]};continue;}const p=line.split("|");if(p.length!==4||!c)throw Error("Bad row: "+line);c.terms.push({en:p[0].trim(),zh:p[1].trim(),abbr:p[2].trim(),definition:p[3].trim()});}}if(c)chapters.push(c);return chapters;}
function buildTsv(chapters){return "# 分布式系统 / Distributed Systems\n# Canonical sources: data/distributed-systems/chapters/*.tsv\n"+chapters.map(c=>`# ${String(c.n).padStart(2,"0")}. ${c.title}\n`+c.terms.map(t=>[t.en,t.zh,t.abbr,t.definition].join("|")).join("\n")).join("\n\n")+"\n";}
function buildMd(chapters){const lines=[
"# 分布式系统 · Distributed Systems",
"",
"> 中英双语专业技术术语手册 | Bilingual Technical Glossary",
"",
"**400 条术语 · 16 章 · 2026-11-27**",
"",
"覆盖分布式计算模型、网络与 RPC、故障模型、逻辑时钟、CAP 与一致性、复制、Raft/Paxos、事务、分片、分布式计算、消息系统、协调、SRE、安全、性能与形式化验证。中文定义是独立编写的学习用途简释，应结合相关论文的故障模型与适用假设阅读。",
"",
"**编辑状态：**已完成格式、数量、英文主术语去重、技术边界抽样检查；尚未声称通过独立人类领域专家的逐条审稿。",
"",
"## 章节目录",
"",
...chapters.map(c=>`- ${String(c.n).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),"","---",""];
for(const c of chapters){lines.push(`## ${String(c.n).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 简明释义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en} | ${t.zh} | ${t.abbr} | ${t.definition} |`),"");}
lines.push("## 易混淆概念辨析","","| 概念 | 核心区别 |","|---|---|",...contrasts.map(x=>`| ${x[0]} | ${x[1]} |`),"","## 中等难度面试问题与答案","");
interviews.forEach((q,i)=>lines.push(`### 面试题 ${i+1}：${q[0]}`,"",`**参考思路：**${q[1]}`,""));
lines.push("## 中等难度考试题与解析","");
exams.forEach((q,i)=>lines.push(`### 考试题 ${i+1}：${q[0]}`,"",`**解析：**${q[1]}`,""));
lines.push("## 核心参考文献","","下列为原始论文、教材与官方技术资料；列出的资料并不意味着其作者认可本项目全部译名或参与审稿。","",...references.map((r,i)=>`${i+1}. [${r[0]}](${r[1]})`),"","## 使用与维护说明","","- 原始稿：`data/distributed-systems/chapters/*.tsv`。","- 聚合词表：`data/distributed-systems.tsv`；Markdown、PDF 为单学科脚本生成的出版物。","- 原始四列为 `en|zh|abbr|definition`，第三列只用于真实缩写。","- 跨版本或供应商特有的语义需以官方文档及实现契约为准。","- 后续可将审稿确认的词条逐批接入网站检索与长篇 Wiki。");
return lines.join("\n")+"\n";}
function hex(s){let out="";for(let i=0;i<s.length;i++)out+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return out;}
function b64(s){const A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",r=[];for(let i=0;i<s.length;i+=3){const a=s.charCodeAt(i),b=i+1<s.length?s.charCodeAt(i+1):0,c=i+2<s.length?s.charCodeAt(i+2):0;r.push(A[a>>2],A[((a&3)<<4)|(b>>4)],i+1<s.length?A[((b&15)<<2)|(c>>6)]:"=",i+2<s.length?A[c&63]:"=");}return r.join("");}
function buildPdf(cs){
 const W=595,H=842,LEFT=48,RIGHT=548,pages=[];let ops=[],y=0,current="";
 const color=a=>a.join(" ")+" rg";
 const rect=(x,yy,w,h,c)=>ops.push(color(c),`${x} ${yy} ${w} ${h} re f`);
 const line=(x1,y1,x2,y2)=>ops.push(".83 .87 .90 RG","0.6 w",`${x1} ${y1} m ${x2} ${y2} l S`);
 const draw=(x,yy,s,size=10,c=[.1,.20,.31])=>ops.push(color(c),`BT /F1 ${size} Tf 1 0 0 1 ${x} ${yy} Tm <${hex(String(s))}> Tj ET`);
 const measure=(s,sz)=>Array.from(s).reduce((a,z)=>a+sz*(z===" "?.32:z.charCodeAt(0)<128? /[WMmw@]/.test(z)?.78:.58:1),0);
 const wrap=(s,sz,max)=>{let a=[],p="";for(const x of String(s)){if(p&&measure(p+x,sz)>max){a.push(p);p=x;}else p+=x;}if(p)a.push(p);return a;};
 function newPage(title="",cont=false){if(ops.length)pages.push(ops.join("\n")+"\n");ops=[];current=title;rect(0,0,W,H,[1,1,1]);rect(0,H-8,W,8,[.09,.23,.35]);draw(LEFT,805,"TERM / ATLAS     ·     DISTRIBUTED SYSTEMS",9.6,[.1,.28,.42]);line(LEFT,791,RIGHT,791);if(title){draw(LEFT,759,title+(cont?"（续）":""),15.2,[.08,.26,.40]);line(LEFT,746,RIGHT,746);y=729;}else{y=766;}}
 function term(i,t){const head=wrap(`${String(i).padStart(2,"0")}  ${t.en}   /   ${t.zh}${t.abbr?"   ["+t.abbr+"]":""}`,10.0,476),desc=wrap(t.definition,9.1,476),height=13*head.length+12.5*desc.length+16;
 if(y-height<64)newPage(current,true);
 if(i%2===0)rect(LEFT-5,y-height+4,RIGHT-LEFT+10,height,[.965,.974,.983]);
 let a=y-13;head.forEach(s=>{draw(LEFT+2,a,s,10,[.08,.22,.35]);a-=13;});desc.forEach(s=>{draw(LEFT+15,a,s,9.1,[.30,.37,.43]);a-=12.5;});y-=height;}
 function para(text,size=9.5,indent=0,c=[.26,.35,.43]){const a=wrap(text,size,RIGHT-LEFT-indent-8);if(y-a.length*(size+5)-7<61)newPage(current,true);for(const s of a){draw(LEFT+indent,y,s,size,c);y-=size+5;}y-=7;}
 newPage();
 rect(0,635,W,162,[.09,.23,.35]);draw(LEFT,741,"分布式系统",29,[1,1,1]);draw(LEFT,699,"Distributed Systems",17,[.83,.91,.98]);draw(LEFT,662,"400 条双语术语  ·  16 个专业章节",12,[1,1,1]);
 draw(LEFT,591,"术语体系",14);line(LEFT,575,RIGHT,575);
 cs.forEach((c,i)=>draw(LEFT+(i>=8?255:0),546-(i>=8?i-8:i)*30,`${String(c.n).padStart(2,"0")}  ${c.title}`,9.9,[.15,.29,.43]));
 draw(LEFT,227,"涵盖理论基础、共识算法、数据系统及工程实践",10,[.2,.34,.48]);
 draw(LEFT,199,"已核对术语结构与重复项；独立专家专业审稿尚未完成。",9.4,[.3,.39,.49]);
 draw(LEFT,107,"2026-11-27   |   Bilingual Technical Glossary",10,[.25,.37,.5]);
 for(const c of cs){newPage(`${String(c.n).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>term(i+1,t));}
 newPage("附录 A · 易混概念辨析");
 contrasts.forEach((x,i)=>{if(y<112)newPage(current,true);para(`${i+1}. ${x[0]}`,10.9,0,[.08,.25,.39]);para(x[1],9.3,12);});
 newPage("附录 B · 中等难度面试问答");
 interviews.forEach((x,i)=>{if(y<120)newPage(current,true);para(`Q${i+1}. ${x[0]}`,10.8,0,[.08,.25,.39]);para(`答：${x[1]}`,9.3,12);});
 newPage("附录 C · 中等难度考试题");
 exams.forEach((x,i)=>{if(y<120)newPage(current,true);para(`${i+1}. ${x[0]}`,10.8,0,[.08,.25,.39]);para(`解析：${x[1]}`,9.3,12);});
 newPage("附录 D · 参考文献");
 references.forEach((x,i)=>{para(`${i+1}. ${x[0]}`,10.2,0,[.08,.25,.39]);para(x[1],8.7,12);});
 para("本册为独立撰写的概念简释和索引；相关论文作者未参与本册审稿。",9.8,0,[.3,.37,.44]);
 if(ops.length)pages.push(ops.join("\n")+"\n");
 const obj=[null];obj[1]="<< /Type /Catalog /Pages 2 0 R >>";
 obj[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${pages.map((_,i)=>`${5+2*i} 0 R`).join(" ")}] >>`;
 obj[3]="<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [<< /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 >>] >>";
 obj[4]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
 for(let i=0;i<pages.length;i++){const pn=5+2*i,sid=pn+1;
 let stream=pages[i];stream+=".83 .87 .90 RG 0.6 w 48 50 m 548 50 l S\n";
 stream+=`${color([.40,.47,.54])} BT /F1 8.5 Tf 1 0 0 1 48 32 Tm <${hex("TERM / ATLAS · Distributed Systems")}> Tj ET\n`;
 stream+=`${color([.40,.47,.54])} BT /F1 8.5 Tf 1 0 0 1 487 32 Tm <${hex(`${i+1} / ${pages.length}`)}> Tj ET\n`;
 obj[pn]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents ${sid} 0 R >>`;
 obj[sid]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;
 }
 let pdf="%PDF-1.4\n%TERM-ATLAS\n",ofs=[0];for(let i=1;i<obj.length;i++){ofs[i]=pdf.length;pdf+=`${i} 0 obj\n${obj[i]}\nendobj\n`;}
 const xref=pdf.length;pdf+=`xref\n0 ${obj.length}\n0000000000 65535 f \n`;for(let i=1;i<obj.length;i++)pdf+=`${String(ofs[i]).padStart(10,"0")} 00000 n \n`;
 pdf+=`trailer\n<< /Size ${obj.length} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;
 return {pdf,pages:pages.length};
}
const raws=Array.from({length:16},(_,i)=>fs.readFileSync(path.join(ROOT,"data/distributed-systems/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const chapters=parseData(raws),records=chapters.flatMap(c=>c.terms);
if(chapters.length!==16||chapters.some(c=>c.terms.length!==25)||records.length!==400||new Set(records.map(t=>t.en.toLowerCase())).size!==400)throw Error("Validation failed: expected 16 chapters of 25 unique English terms");
for(const t of records)if(!t.en||!t.zh||!t.definition)throw Error("Incomplete term: "+t.en);
const tsv=Buffer.from(buildTsv(chapters),"utf8"),md=Buffer.from(buildMd(chapters),"utf8"),pdf=Buffer.from(buildPdf(chapters).pdf,"ascii");
const outputs=[["data/distributed-systems.tsv",tsv],["glossaries/distributed-systems.md",md],["docs/glossaries/distributed-systems.md",md],["pdf/distributed-systems.pdf",pdf],["docs/pdf/distributed-systems.pdf",pdf]];
const check=process.argv.includes("--check");
for(const [p,b] of outputs){const f=path.join(ROOT,p);if(check){if(!fs.existsSync(f)||!fs.readFileSync(f).equals(b))throw Error("Not synchronized: "+p);}else{fs.mkdirSync(path.dirname(f),{recursive:true});fs.writeFileSync(f,b);}}
console.log((check?"PASS":"GENERATED")+": 400 terms, 16 chapters, "+outputs.length+" artifacts");
