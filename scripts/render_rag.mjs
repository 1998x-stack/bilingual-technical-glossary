#!/usr/bin/env node
// Deterministic TERM/ATLAS standalone RAG glossary publication.
// node scripts/render_rag.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["RAG 与微调","RAG 在推理时访问外部知识；微调通过训练改变模型参数。两者可结合，RAG 不保证纠正模型固有推理错误。"],["Embedding 检索与 BM25","Embedding 擅长发现表达不同的语义关联；BM25 强调字面词项匹配，专有名词和标识符可能更适合词法检索。"],["稀疏检索与稠密检索","稀疏向量大部分维度为零；稠密向量多数维度非零。这是表示差异，并不直接决定检索质量。"],["Bi-encoder 与 Cross-encoder","双编码器可分别预编码文档，适合大规模召回；交叉编码器联合处理查询文档对，常用于候选重排序。"],["精确近邻与 ANN","精确近邻返回按指定距离真正最近的候选；ANN 通过近似索引加速搜索，可能遗漏精确最近邻。"],["Recall@k 与 Precision@k","Recall@k 是 top-k 命中相关文档数除以全部相关文档数；Precision@k 则除以 k。两者分母不同。"],["相关性与忠实性","检索片段与问题高度相关，并不意味着生成的每个断言都能从片段推出；需要独立检查证据支持。"],["RRF 与分数加权融合","RRF 用排名位置融合，不直接依赖各检索器分数的可比性；加权分数融合通常需要校准。"],["切块重叠与父子检索","重叠切块保留邻近文本但增大索引冗余；父子检索用小片段定位后返回更大上下文。"],["Self-RAG 与 CRAG","Self-RAG 通过学习反思信号决定检索并评判输出；CRAG 重点根据检索质量触发纠错策略。二者不是同一通用标准。"],["GraphRAG 与普通向量 RAG","GraphRAG 将实体关系及社区结构用于检索或汇总，适合关系和整体概览任务；成本与数据质量要求因实现而异。"],["拒答与幻觉","证据不足时明确拒答可能牺牲部分回答覆盖，但比生成无证据断言更符合高可靠性任务目标。"],["权限过滤与提示防护","文档 ACL 和查询时授权属于数据访问层控制；提示词中的安全要求不能替代后端强制权限校验。"],["离线检索评价与线上业务评价","离线指标量化标注集上的召回排序；线上指标还受延迟、成本、用户行为和数据变化影响。"]];
const interviews=[["为什么把切块大小统一设为 1,000 token 并不能保证效果最优？","不同语料的语义单元、表格与上下文依赖不同；需要同时衡量检索召回、证据完整性、冗余与生成质量，通过验证集选择。"],["什么时候先选 BM25 而不是稠密检索？","精确产品型号、错误码、订单号、代码符号等词形极关键时，BM25 或精确字段匹配更稳定；可与语义检索融合。"],["为什么只检查 ANN 索引召回率不能说明 RAG 已经准确？","ANN 召回是对精确向量最近邻的重合度；语义相关标注、证据覆盖以及生成忠实性是不同目标，需要独立测量。"],["为什么多个检索器的分数不能不加处理直接求和？","BM25 与余弦相似度的数值范围和分布不同，直接求和会被尺度主导；可用分数归一化或 RRF 等名次融合。"],["如何处理一个问题需要从两份合同找到相互引用的条款？","先拆解成子查询定位第一份条款及引用键，再按引用键查询第二份并保留来源位置，最终校验两段证据的关联。"],["RAG 返回文档链接为什么仍可能出现伪引用？","仅有链接并不说明链接内容支持特定断言；需要在断言级验证原文片段、时间与适用条件。"],["用户 A 能否用共享向量数据库查询用户 B 文档，即使生成提示要求模型不泄漏？","不能依赖提示词。必须在索引或检索服务执行租户隔离和权限过滤，同时避免跨租户缓存复用。"],["如何评估引用准确性与回答正确性的区别？","引用准确性检验引用是否支持句子；回答正确性检验答案是否符合外部事实或参考真值。错误来源也可能支持错误答案。"],["为什么 Self-RAG 和 CRAG 不应被当作任意 RAG 系统默认具备的功能？","两者源于具体研究设计，分别涉及训练的反思机制或检索纠错流程；通用 RAG 不自动包含这些模块。"],["向量模型升级为什么往往需要重建索引？","不同模型的维度、坐标语义和归一化方式可能不兼容；新查询向量通常不能可靠匹配旧文档向量。"]];
const exams=[["某查询共有 8 个标注相关文档，top-5 返回 3 个相关文档。计算 Recall@5 与 Precision@5。","Recall@5=3/8=0.375；Precision@5=3/5=0.60。"],["三个查询首个相关文档排名分别为 1、2、4。计算 MRR。","MRR=(1+1/2+1/4)/3=7/12≈0.5833。"],["使用 k=60 的 RRF，一份文档分别位列两个检索器的第 1 和第 3，求得分。","1/(60+1)+1/(60+3)=1/61+1/63≈0.03226。"],["上下文上限 8,192 token，系统与用户问题预留 1,024，输出预留 2,048，最多还能放多少检索文本？","忽略额外格式标记和内部开销时，8,192−1,024−2,048=5,120 token。"],["一个向量索引在 100 次查询中累计应返回 1,000 个精确前十邻居，实际命中 920 个，ANN Recall@10 多少？","按累计命中定义为 920/1,000=0.92；这不是人工标注相关性召回。"],["把 10 个文档每份各切成 8 个块、相邻块重叠 100 token，实际索引块数多少？","不考虑空块和特殊过滤条件时是 10×8=80 块；重叠增加存储文本量但不改变该数量。"],["某答案包含 5 条独立事实断言，其中 4 条由证据支持，按简单断言支持率定义忠实性是多少？","支持率 4/5=0.8。真实评测需要定义声明拆分与支持判定规则。"],["向量库包含 100 万条公司文档，某用户只可访问 10 万条。为何不能先返回全球 top-10 再过滤？","这样可使授权集合中的高分证据被未授权结果挤出，导致召回严重下降；应尽可能在检索候选生成前或过程中执行授权过滤。"],["知识库昨晚更新但用户拿到上周答案，最先检查哪几类版本信息？","对比来源文档版本、摄入时间、索引更新时间、查询路由目标及缓存键/失效记录，定位陈旧数据环节。"],["某检索候选前五条重复呈现相同条款，且另一个必要条款未出现，优先考虑什么改进？","增加结果去重或 MMR 多样化，并评估分解检索、父子检索和重排序；用证据覆盖而非单纯 top-k 得分衡量效果。"]];
const references=[["Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks","https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html"],["ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction (NAACL 2022)","https://aclanthology.org/2022.naacl-main.272/"],["Malkov & Yashunin (2018), Hierarchical Navigable Small World Graphs","https://arxiv.org/abs/1603.09320"],["Asai et al. (ICLR 2024), Self-RAG: Learning to Retrieve, Generate, and Critique","https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html"],["Yan et al., Corrective Retrieval Augmented Generation (CRAG)","https://aclanthology.org/2026.findings-aacl.151/"],["Edge et al. (2024), From Local to Global: A Graph RAG Approach","https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/"],["RAGAS: Automated Evaluation of Retrieval Augmented Generation (EACL 2024)","https://aclanthology.org/2024.eacl-demo.16/"],["ARES: Automated Evaluation Framework for RAG Systems (NAACL 2024)","https://aclanthology.org/2024.naacl-long.20/"],["Liu et al. (TACL 2024), Lost in the Middle","https://aclanthology.org/2024.tacl-1.9/"],["Anthropic Engineering, Contextual Retrieval","https://www.anthropic.com/research/contextual-retrieval"],["Microsoft Research GraphRAG project and documentation","https://www.microsoft.com/en-us/research/project/graphrag/"],["NIST AI Risk Management Framework, Generative AI Profile","https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence"]];
function parseChapters(raws){
 const chapters=[];let section=null;
 for(const raw of raws){for(const line of raw.trim().split(/\r?\n/)){if(!line)continue;
 if(line.startsWith("# ")){if(section)chapters.push(section);section={num:chapters.length+1,title:line.slice(2),terms:[]};continue;}
 const fields=line.split("|");if(fields.length!==4||!section)throw Error("Malformed glossary row: "+line);
 section.terms.push({en:fields[0].trim(),zh:fields[1].trim(),abbr:fields[2].trim(),definition:fields[3].trim()});
 }}
 if(section)chapters.push(section);return chapters;
}
function makeTsv(chapters){
 return "# Retrieval-Augmented Generation | 检索增强生成\n# Canonical sources: data/rag/chapters/*.tsv; 14 chapters; 350 terms\n"+chapters.map(c=>`# ${String(c.num).padStart(2,"0")}. ${c.title}\n`+c.terms.map(t=>[t.en,t.zh,t.abbr,t.definition].join("|")).join("\n")).join("\n\n")+"\n";
}
function makeMd(chapters){
 const lines=["# 检索增强生成 · Retrieval-Augmented Generation (RAG)","",
 "> TERM/ATLAS · 专业中英文术语对照表 | Bilingual Technical Glossary","",
 "**350 条术语 · 14 个专业章节 · 2026-11-27**","",
 "覆盖 RAG 基础架构、文档摄入与解析、切块、Embedding、BM25、向量数据库与 ANN、混合检索、重排序、查询规划、证据引用、Agentic RAG、GraphRAG、评测、安全及生产优化。",
 "",
 "**使用边界：**这些定义为独立撰写的简明概括，不表示所有技术属于同一标准；Self-RAG、CRAG、ColBERT、RAGAS 等特指原研究或工具。证据相关性不等于回答忠实性，检索系统本身也不自动提供访问授权保障。",
 "",
 "**编辑状态：**已执行记录格式、章节数量、英文主术语唯一性校验；尚未完成独立专业人员的逐条事实审稿或跨阅读器排版验收。",
 "",
 "## 目录","",...chapters.map(c=>`- ${String(c.num).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),"","---",""];
 for(const c of chapters){lines.push(`## ${String(c.num).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 简明释义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en} | ${t.zh} | ${t.abbr} | ${t.definition} |`),"");}
 lines.push("## 核心概念辨析","","| 对比术语 | 核心区别与限制 |","|---|---|",...contrasts.map(x=>`| ${x[0]} | ${x[1]} |`),"","## 中等难度面试问答","");
 interviews.forEach((q,i)=>lines.push(`### 面试题 ${i+1}. ${q[0]}`,"",`**参考答案：**${q[1]}`,""));
 lines.push("## 中等难度考试题与解析","");
 exams.forEach((q,i)=>lines.push(`### 考试题 ${i+1}. ${q[0]}`,"",`**解析：**${q[1]}`,""));
 lines.push("## 主要论文与官方资料","","以下来源支持相应研究主题与术语边界，引用不意味着研究作者参与或认可本项目术语逐条审查。","",
 ...references.map((r,i)=>`${i+1}. [${r[0]}](${r[1]})`),"","## 维护说明","",
 "- 原始术语：`data/rag/chapters/*.tsv`（`English|中文|abbr|definition`）。",
 "- 导出文件：`data/rag.tsv`、`glossaries/rag.md`、`pdf/rag.pdf`，以及相同内容的 `docs/` 镜像。",
 "- 构建与核验：`node scripts/render_rag.mjs` / `node scripts/render_rag.mjs --check`。",
 "- 本册是独立出版物，**尚未加入全站术语搜索索引**，也未构建 350 篇长篇 Wiki。"
 );
 return lines.join("\n")+"\n";
}
function hex(s){let out="";for(let i=0;i<s.length;i++)out+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return out;}
function toBase64(s){const C="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",a=[];for(let i=0;i<s.length;i+=3){const x=s.charCodeAt(i),y=i+1<s.length?s.charCodeAt(i+1):0,z=i+2<s.length?s.charCodeAt(i+2):0;a.push(C[x>>2],C[((x&3)<<4)|(y>>4)],i+1<s.length?C[((y&15)<<2)|(z>>6)]:"=",i+2<s.length?C[z&63]:"=");}return a.join("");}
function makePdf(chapters){
 const W=595,H=842,L=48,R=547,pages=[];let ops=[],y=0,section="";
 const rgb=a=>a.join(" ")+" rg";
 const rect=(x,b,w,h,color)=>ops.push(rgb(color),`${x} ${b} ${w} ${h} re f`);
 const rule=(y1)=>ops.push(".81 .85 .90 RG","0.6 w",`${L} ${y1} m ${R} ${y1} l S`);
 const text=(x,b,s,size=10,color=[.08,.21,.34])=>ops.push(rgb(color),`BT /FC ${size} Tf 1 0 0 1 ${x} ${b} Tm <${hex(String(s))}> Tj ET`);
 const width=(s,size)=>Array.from(String(s)).reduce((n,ch)=>n+size*(ch===" "?.32:ch.charCodeAt(0)<128?(/[MWmw@]/.test(ch)?.8:.55):1),0);
 const wrap=(s,size,max)=>{const out=[];let line="";for(const ch of Array.from(String(s))){if(line&&width(line+ch,size)>max){out.push(line);line=ch}else line+=ch;}if(line)out.push(line);return out;};
 function page(title="",cont=false){if(ops.length)pages.push(ops.join("\n")+"\n");ops=[];section=title;rect(0,0,W,H,[1,1,1]);rect(0,H-8,W,8,[.07,.20,.33]);text(L,807,"TERM / ATLAS   ·   RAG TECHNICAL GLOSSARY",10,[.1,.24,.37]);rule(791);
  if(title){text(L,761,title+(cont?"（续）":""),15.1,[.06,.24,.36]);rule(744);y=728;}else y=763;}
 function term(idx,t){const headers=wrap(`${String(idx).padStart(2,"0")}   ${t.en}   /   ${t.zh}${t.abbr?"   ["+t.abbr+"]":""}`,10.0,475),definitions=wrap(t.definition,9.2,476),h=headers.length*14+definitions.length*13+15;
  if(y-h<62)page(section,true);
  if(idx%2===0)rect(L-4,y-h+2,R-L+8,h+2,[.963,.973,.981]);
  let at=y-13;headers.forEach(s=>{text(L+3,at,s,10,[.07,.22,.36]);at-=14;});definitions.forEach(s=>{text(L+14,at,s,9.2,[.31,.39,.46]);at-=13;});y-=h;
 }
 function para(s,sz=9.4,indent=0,clr=[.30,.38,.46]){const lines=wrap(s,sz,R-L-indent-8);if(y-lines.length*(sz+5)-9<61)page(section,true);for(const z of lines){text(L+indent,y,z,sz,clr);y-=sz+5;}y-=9;}
 page();
 rect(0,629,W,169,[.07,.20,.33]);text(L,741,"检索增强生成",29,[1,1,1]);text(L,701,"Retrieval-Augmented Generation",17,[.83,.92,.99]);text(L,660,"350 条术语     ·     14 个专题     ·     RAG",12,[1,1,1]);
 text(L,589,"专业知识框架",14);rule(572);
 chapters.forEach((c,i)=>text(L+(i>=7?255:0),540-(i>=7?i-7:i)*37,`${String(c.num).padStart(2,"0")}  ${c.title}`,9.5,[.11,.27,.40]));
 text(L,235,"检索 · 向量表示 · 证据溯源 · 知识图谱 · 评测与安全",10.1,[.17,.32,.43]);
 text(L,205,"源词条与目录数量已自动校验，内容尚未经独立专家逐条审核。",9.3,[.3,.39,.45]);
 text(L,181,"章节、概念辨析与试题均包含于本 PDF。",9.3,[.3,.39,.45]);
 text(L,101,"TERM / ATLAS     2026-11-27",10,[.18,.34,.47]);
 for(const c of chapters){page(`${String(c.num).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>term(i+1,t));}
 page("附录 A · 关键概念辨析");
 contrasts.forEach((x,i)=>{if(y<135)page(section,true);para(`${i+1}. ${x[0]}`,10.5,0,[.08,.24,.36]);para(x[1],9.2,14);});
 page("附录 B · 中等难度面试问答");
 interviews.forEach((x,i)=>{if(y<135)page(section,true);para(`Q${i+1}. ${x[0]}`,10.4,0,[.08,.24,.36]);para(`答：${x[1]}`,9.2,14);});
 page("附录 C · 考试题与解析");
 exams.forEach((x,i)=>{if(y<135)page(section,true);para(`${i+1}. ${x[0]}`,10.4,0,[.08,.24,.36]);para(`解析：${x[1]}`,9.2,14);});
 page("附录 D · 论文与技术来源");
 references.forEach((x,i)=>{para(`${i+1}. ${x[0]}`,9.8,0,[.08,.24,.36]);para(x[1],8.6,14);});
 para("本册内容为独立撰写的简短技术定义，参考论文作者未参与术语审核。",9.4,0,[.3,.38,.47]);
 if(ops.length)pages.push(ops.join("\n")+"\n");
 const objects=[null];
 objects[1]="<< /Type /Catalog /Pages 2 0 R >>";
 objects[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${pages.map((_,i)=>`${6+i*2} 0 R`).join(" ")}] >>`;
 objects[3]="<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [<< /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 >>] /ToUnicode 4 0 R >>";
 const cmap="/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n/CMapName /Identity-UCS2 def\n/CMapType 2 def\n1 begincodespacerange\n<0000> <FFFF>\nendcodespacerange\n1 beginbfrange\n<0000> <FFFF> <0000>\nendbfrange\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n";
 objects[4]=`<< /Length ${cmap.length} >>\nstream\n${cmap}endstream`;
 objects[5]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
 for(let i=0;i<pages.length;i++){const p=6+2*i,s=p+1;let stream=pages[i]+".81 .85 .90 RG 0.5 w 48 51 m 547 51 l S\n";
 stream+=`${rgb([.40,.46,.54])} BT /FC 8 Tf 1 0 0 1 48 34 Tm <${hex("TERM / ATLAS  ·  RAG")}> Tj ET\n`;
 stream+=`${rgb([.40,.46,.54])} BT /FC 8 Tf 1 0 0 1 489 34 Tm <${hex(`${i+1} / ${pages.length}`)}> Tj ET\n`;
 objects[p]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Resources << /Font << /FC 3 0 R >> >> /Contents ${s} 0 R >>`;
 objects[s]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;
 }
 let pdf="%PDF-1.4\n%TERM-ATLAS\n",offset=[0];
 for(let i=1;i<objects.length;i++){offset[i]=pdf.length;pdf+=`${i} 0 obj\n${objects[i]}\nendobj\n`;}
 const x=pdf.length;pdf+=`xref\n0 ${objects.length}\n0000000000 65535 f \n`;
 for(let i=1;i<objects.length;i++)pdf+=`${String(offset[i]).padStart(10,"0")} 00000 n \n`;
 pdf+=`trailer\n<< /Size ${objects.length} /Root 1 0 R >>\nstartxref\n${x}\n%%EOF\n`;
 return {pdf,pages:pages.length};
}
const src=Array.from({length:14},(_,i)=>fs.readFileSync(path.join(ROOT,"data/rag/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const chapters=parseChapters(src),terms=chapters.flatMap(c=>c.terms);
if(chapters.length!==14||chapters.some(c=>c.terms.length!==25)||terms.length!==350||new Set(terms.map(t=>t.en.toLowerCase())).size!==350||terms.some(t=>!t.en||!t.zh||!t.definition))throw Error("Expected 350 unique complete terms");
const tsv=Buffer.from(makeTsv(chapters),"utf8"),md=Buffer.from(makeMd(chapters),"utf8"),pdf=Buffer.from(makePdf(chapters).pdf,"ascii");
const files=[["data/rag.tsv",tsv],["glossaries/rag.md",md],["docs/glossaries/rag.md",md],["pdf/rag.pdf",pdf],["docs/pdf/rag.pdf",pdf]];
const check=process.argv.includes("--check");for(const [p,b] of files){const f=path.join(ROOT,p);if(check){if(!fs.existsSync(f)||!fs.readFileSync(f).equals(b))throw Error("Out of sync: "+p);}else{fs.mkdirSync(path.dirname(f),{recursive:true});fs.writeFileSync(f,b);}}
console.log((check?"PASS":"GENERATED")+": 350 terms, 14 chapters, "+files.length+" synchronized artifacts");
