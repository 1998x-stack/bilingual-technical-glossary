#!/usr/bin/env node
// TERM / ATLAS — deterministic NLP handbook publisher. Requires Node.js 18+.
// node scripts/render_nlp.mjs [--check]
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contrasts=[["NLP、NLU 与 NLG","NLP 是整个自然语言处理领域；NLU 侧重语义与意图理解；NLG 侧重根据条件或知识形成语言输出。"],["词语切分与子词词元化","中文词语切分寻求语言学意义上的词边界；BPE、WordPiece 等为模型词表压缩与覆盖而切分，结果不一定是自然词。"],["BPE、WordPiece 与 Unigram","BPE 通常反复合并常见符号对；WordPiece 在指定训练准则下选择子词；Unigram 从候选词表中用概率模型选择切分。"],["Stemming 与 Lemmatization","Stemming 可用字符串截断得到不一定存在的词干；Lemmatization 利用词形和词典信息找规范词元基本形。"],["成分句法与依存句法","成分句法用嵌套短语树刻画结构；依存句法用词间有向中心词关系刻画结构，两者可以转换但并不完全等价。"],["NER、实体链接与共指消解","NER 识别提及边界与类别；实体链接映射到知识库条目；共指消解决定多个提及是否指向同一实体。"],["HMM 与 CRF","HMM 建模隐状态和观测的生成概率；CRF 直接建模给定输入的标签条件分布，便于灵活使用输入特征。"],["静态词向量与上下文化表示","静态向量通常为一个词型固定表示；上下文化表示根据具体句子改变同一个词的向量，有助于区分词义。"],["CBOW 与 Skip-gram","CBOW 根据上下文预测中心词；Skip-gram 根据中心词预测其周围词，两者是 Word2Vec 经典训练方向。"],["Transformer 编码器与自回归解码器","常见编码器允许输入 token 双向交互；自回归解码器使用因果掩码逐步预测后续 token。"],["BERT MLM 与 GPT CLM","MLM 根据被遮蔽 token 左右上下文学习双向表示；CLM 根据前缀预测下一个 token，适合自回归生成。"],["微调与上下文学习","微调通过训练数据更新参数；上下文学习仅改变推理时输入示例与指令，通常不修改模型权重。"],["LoRA 与全参数微调","LoRA 以少量低秩参数表示可训练增量，节省显存与存储；全参数微调允许更新模型大部分权重。"],["抽取式问答与生成式问答","抽取式问答定位上下文中的连续答案跨度；生成式问答可重述综合信息，但更需要证据忠实性验证。"],["BLEU、ROUGE 与 BERTScore","BLEU 偏重译文的 N-gram 精确率，ROUGE 常用于摘要重叠评估，BERTScore 利用上下文化表示匹配；均非真实事实性证明。"],["语音识别 WER 与机器翻译 BLEU","WER 衡量识别词的编辑错误数量；BLEU 比较候选译文与参考译文的 N-gram 重合，指标目标与方向不同。"]];
const interviews=[["中文分词和 BPE 子词切分为什么不能互相替代？","中文分词寻求自然语言词的边界；BPE 主要为限制词表、降低 OOV 而服务模型输入。一个中文词可能拆为多个 token，反之 token 也不必是完整词。"],["为什么不同 tokenizer 下的语言模型困惑度不能直接比较？","困惑度按 token 的平均负对数似然定义，token 粒度不同会改变序列长度与概率单位；应使用相同编码或按字节归一化等可比协议。"],["依存句法中的 projective 与 non-projective 结构有什么区别？","投射依存树在词序表示中满足相应不交叉条件；非投射树需要更一般的解析结构，部分语言中跨距依存较常见。"],["为什么 HMM 的状态转移与 CRF 的特征建模方式不同？","HMM 指定潜状态与观测的联合生成分解；线性链 CRF 对给定整段输入条件下的标签序列归一化，可使用任意输入相关的局部特征。"],["BERT 预训练与 GPT 类模型的目标有哪些结构差异？","BERT 典型 MLM 依赖双向上下文恢复被遮蔽位置；GPT 典型 CLM 用因果掩码建模前缀到下一 token 的条件概率。"],["为什么单纯提高 beam width 不一定提高机器翻译质量？","束宽增加可改善当前模型评分的搜索近似，却不能纠正长度偏好或模型分布失准，可能导致短输出或其他质量下降。"],["词元分类的 token F1 与实体级 F1 为什么不同？","token F1 按位置计分，实体级 F1 通常要求预测片段起止边界和类别全部正确；前者可能掩盖边界碎裂错误。"],["为什么静态词向量难以处理一词多义？","一个词的不同语境共用固定词型向量，无法直接表示 bank 等词的多种含义；上下文化编码器可按语境改变表示。"],["什么情况下微调优于仅使用 few-shot 提示？","当任务标签稳定、可用高质量示例较多、推理成本或格式一致性要求高时，微调可能更适用；仍应比较数据成本、泛化与遗忘风险。"],["如何检查生成摘要是否忠实于源文档？","将摘要拆分为事实断言，检索源文支持片段并检查时间、数量与实体是否一致；ROUGE 高分本身不能保证事实正确。"],["评测多语言 NLP 时为什么不应只看英语性能？","语料规模、形态复杂度、文字系统、分词与领域分布不同，英语分数可能掩盖低资源语言上的明显退化。"],["部署面向企业文档的 NLP 系统，如何处理间接提示注入？","把检索内容视为低信任数据，权限校验和外部工具授权在后端实施，隔离指令与证据，并执行引用核验与最小权限控制。"]];
const exams=[["一个序列 100 个 token，模型对它们平均负对数概率（自然对数）为 2，困惑度是多少？","PPL=exp(2)≈7.389，必须说明以 token 为单位且统一使用自然对数。"],["分类任务 TP=80、FP=20、FN=40，计算 Precision、Recall 和 F1。","P=80/100=0.8，R=80/120≈0.667，F1=2TP/(2TP+FP+FN)=160/220≈0.727。"],["一个实体参考跨度为 token 2–4，系统预测为 2–3 且类型相同，严格实体级匹配能否记为 TP？","不能。严格 span-level 评测要求起止边界和类型完全一致，否则会导致相应 FP 与 FN。"],["Bigram 模型中 count('自然 语言')=30，count('自然')=50，MLE P(语言|自然) 是多少？","30/50=0.6，假定计数来自相同的 bigram 统计口径且无需平滑。"],["某词在 10,000 篇文档中出现于 100 篇，使用 ln(N/df) 的 IDF 等于多少？","ln(10000/100)=ln(100)≈4.605。"],["Attention 有 8 个 head、总隐藏维度 d_model=512，均匀分配时每头维度是多少？","512/8=64。实际模型还可能使用不同的键值头数或投影维度。"],["对两向量 a=(1,0) 与 b=(1,1)，余弦相似度是多少？","a·b/(||a||||b||)=1/√2≈0.7071。"],["WER 参考文本 20 词，出现 2 个替换、1 个删除、1 个插入，WER 为多少？","WER=(S+D+I)/N=(2+1+1)/20=0.20，即 20%。"],["3 句参考摘要中有 6 个不同 bigram，系统摘要命中其中 3 个，按召回定义的 ROUGE-2 Recall 多少？","3/6=0.5；实际实现还需规定重复计数和规范化规则。"],["两个标签分类结果中 TP=30、FP=10、FN=5，F1 是多少？","F1=2TP/(2TP+FP+FN)=60/75=0.8。"],["4 个候选 token 归一化概率为 0.5、0.3、0.15、0.05，Top-p=0.8 的最小采样集合包含几个？","按概率降序取前两个即可，累计概率 0.5+0.3=0.8；实现对阈值等号可能有边界约定。"],["Seq2Seq 参考序列长度 8、预测序列长度 5，是否能仅凭长度判定翻译准确？","不能。长度可以影响长度惩罚和覆盖情况，但准确性还需语义、术语、忠实性和任务评测。"]];
const references=[["Jurafsky & Martin, Speech and Language Processing (3rd ed.)","https://web.stanford.edu/~jurafsky/slp3/"],["Manning, Raghavan & Schütze, Introduction to Information Retrieval","https://nlp.stanford.edu/IR-book/"],["Universal Dependencies — official annotation guidelines","https://universaldependencies.org/"],["Vaswani et al., Attention Is All You Need (NeurIPS 2017)","https://arxiv.org/abs/1706.03762"],["Devlin et al., BERT: Pre-training of Deep Bidirectional Transformers (NAACL 2019)","https://aclanthology.org/N19-1423/"],["Mikolov et al., Efficient Estimation of Word Representations (2013)","https://arxiv.org/abs/1301.3781"],["Sutskever et al., Sequence to Sequence Learning with Neural Networks (2014)","https://arxiv.org/abs/1409.3215"],["Kudo & Richardson, SentencePiece (EMNLP 2018)","https://aclanthology.org/D18-2012/"],["Lewis et al., BART: Denoising Sequence-to-Sequence Pre-training (ACL 2020)","https://aclanthology.org/2020.acl-main.703/"],["Raffel et al., Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (JMLR 2020)","https://jmlr.org/papers/v21/20-074.html"],["Hu et al., LoRA: Low-Rank Adaptation of Large Language Models (2021)","https://arxiv.org/abs/2106.09685"],["Papineni et al., BLEU: A Method for Automatic Evaluation of Machine Translation (ACL 2002)","https://aclanthology.org/P02-1040/"],["Lin, ROUGE: A Package for Automatic Evaluation of Summaries (2004)","https://aclanthology.org/W04-1013/"],["Rajpurkar et al., SQuAD: 100,000+ Questions for Machine Comprehension of Text (2016)","https://aclanthology.org/D16-1264/"],["Hugging Face Transformers Documentation","https://huggingface.co/docs/transformers/"]];
function parseData(raws){const cs=[];let c=null;for(const raw of raws)for(const line of raw.split(/\r?\n/)){if(!line)continue;if(line.startsWith("# ")){if(c)cs.push(c);c={n:cs.length+1,title:line.slice(2),terms:[]};continue;}const p=line.split("|");if(!c||p.length!==4)throw Error("Invalid NLP source row: "+line);c.terms.push({en:p[0].trim(),zh:p[1].trim(),abbr:p[2].trim(),definition:p[3].trim()});}if(c)cs.push(c);return cs;}
function makeTsv(cs){return "# 自然语言处理 | Natural Language Processing (NLP)\n# Canonical source: data/nlp/chapters/*.tsv; 20 chapters, 500 terms\n"+cs.map(c=>`# ${String(c.n).padStart(2,"0")}. ${c.title}\n`+c.terms.map(t=>[t.en,t.zh,t.abbr,t.definition].join("|")).join("\n")).join("\n\n")+"\n";}
function makeMd(cs){
const out=["# 自然语言处理 · Natural Language Processing (NLP)","",
"> TERM / ATLAS · 中英文专业术语手册 | Bilingual Technical Glossary","",
"**500 条术语 · 20 个专业章节 · 2026-11-27**","",
"知识体系覆盖计算语言学、语料库与数据标注、词元化与形态学、句法及语义、统计 NLP、词嵌入、RNN 与 Transformer、预训练语言模型、微调、NER、问答、机器翻译、摘要、语音与多模态语言处理、基准评测及生产治理。",
"",
"**适用范围：**NLP 的语言学概念、神经模型、数据格式及评测协议各有特定前提；不应把词元与词语、抽取式与生成式任务、自动指标与事实正确性混为一谈。",
"",
"**审稿说明：**已自动检查原始条目的字段结构、数量和英文主术语唯一性；独立领域专家逐条事实审稿与 PDF 视觉验收尚未完成。",
"",
"## 章节目录","",...cs.map(c=>`- ${String(c.n).padStart(2,"0")}. ${c.title}（${c.terms.length} 条）`),"","---",""];
for(const c of cs)out.push(`## ${String(c.n).padStart(2,"0")}. ${c.title}`,"","| # | English term | 中文译名 | Abbr. | 核心定义 |","|---:|---|---|---|---|",...c.terms.map((t,i)=>`| ${i+1} | ${t.en} | ${t.zh} | ${t.abbr} | ${t.definition} |`),"");
out.push("## 16 组核心概念辨析","","| 对比对象 | 技术区别及应用边界 |","|---|---|",...contrasts.map(x=>`| ${x[0]} | ${x[1]} |`),"","## 中等难度面试问答","");
interviews.forEach((x,i)=>out.push(`### 面试 ${i+1}：${x[0]}`,"",`**参考答案：**${x[1]}`,""));
out.push("## 中等难度考试题与解析","");
exams.forEach((x,i)=>out.push(`### 考试 ${i+1}：${x[0]}`,"",`**解析：**${x[1]}`,""));
out.push("## 经典教材、学术论文和技术资料","","以下资源用于提供研究背景、模型名称与知识体系，原作者未参与或认可本项目逐条术语审稿。","",...references.map((x,i)=>`${i+1}. [${x[0]}](${x[1]})`),"",
"## 数据维护与发布边界","","- 原始数据：`data/nlp/chapters/*.tsv`，字段为 `English|中文|abbr|definition`。","- 输出文件：`data/nlp.tsv`、`glossaries/nlp.md`、`pdf/nlp.pdf` 和 `docs/` 镜像。","- 生成与一致性校验：`node scripts/render_nlp.mjs` / `node scripts/render_nlp.mjs --check`。","- 本册是独立出版术语表；**未加入全站搜索索引、未生成 500 篇深度 Wiki**。");
return out.join("\n")+"\n";
}
function toHex(s){let z="";for(let i=0;i<s.length;i++)z+=s.charCodeAt(i).toString(16).toUpperCase().padStart(4,"0");return z;}
function base64(s){const A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",out=[];for(let i=0;i<s.length;i+=3){const a=s.charCodeAt(i),b=i+1<s.length?s.charCodeAt(i+1):0,c=i+2<s.length?s.charCodeAt(i+2):0;out.push(A[a>>2],A[((a&3)<<4)|(b>>4)],i+1<s.length?A[((b&15)<<2)|(c>>6)]:"=",i+2<s.length?A[c&63]:"=");}return out.join("");}
function makePdf(cs){
const W=595,H=842,L=47,R=548,pages=[];let ops=[],section="",y=0;
const col=c=>c.join(" ")+" rg",rect=(x,b,w,h,c)=>ops.push(col(c),`${x} ${b} ${w} ${h} re f`);
const rule=b=>ops.push(".83 .87 .91 RG","0.5 w",`${L} ${b} m ${R} ${b} l S`);
const draw=(x,b,s,size=10,c=[.09,.24,.37])=>ops.push(col(c),`BT /FC ${size} Tf 1 0 0 1 ${x.toFixed(1)} ${b.toFixed(1)} Tm <${toHex(String(s))}> Tj ET`);
const mw=(s,z)=>Array.from(String(s)).reduce((n,ch)=>n+z*(ch===" "?.34:ch.charCodeAt(0)<128?(/[MWmw@]/.test(ch)?.8:.56):1),0);
const wrap=(s,z,max)=>{const out=[];let buf="";for(const ch of Array.from(String(s))){if(buf&&mw(buf+ch,z)>max){out.push(buf);buf=ch;}else buf+=ch;}if(buf)out.push(buf);return out;};
function page(title="",cont=false){if(ops.length)pages.push(ops.join("\n")+"\n");ops=[];section=title;rect(0,0,W,H,[1,1,1]);rect(0,834,W,8,[.06,.22,.37]);draw(L,807,"TERM / ATLAS  |  NATURAL LANGUAGE PROCESSING",9.6,[.12,.28,.41]);rule(791);if(title){draw(L,760,title+(cont?"（续）":""),14.4,[.07,.23,.37]);rule(746);y=728;}else y=761;}
function term(i,t){const heads=wrap(`${String(i).padStart(2,"0")}   ${t.en}  /  ${t.zh}${t.abbr?"   ["+t.abbr+"]":""}`,9.8,478),def=wrap(t.definition,9.1,475),h=heads.length*13.5+def.length*12.3+16;if(y-h<62)page(section,true);if(i%2===0)rect(L-4,y-h+3,R-L+8,h,[.965,.976,.985]);let yy=y-13;for(const s of heads){draw(L+3,yy,s,9.8,[.065,.21,.35]);yy-=13.5;}for(const s of def){draw(L+15,yy,s,9.1,[.30,.39,.47]);yy-=12.3;}y-=h;}
function para(s,sz=9.2,indent=0,c=[.30,.39,.46]){const p=wrap(s,sz,R-L-indent-7);if(y-p.length*(sz+5)-9<62)page(section,true);for(const s of p){draw(L+indent,y,s,sz,c);y-=sz+5;}y-=9;}
page();rect(0,624,W,176,[.06,.22,.37]);draw(L,744,"自然语言处理",29,[1,1,1]);draw(L,706,"Natural Language Processing",17.2,[.83,.92,.98]);draw(L,664,"500 条中英文术语   ·   20 个专业章节",12,[1,1,1]);draw(L,595,"NLP KNOWLEDGE MAP  /  20 CHAPTERS",11,[.12,.29,.42]);rule(578);
cs.forEach((c,i)=>draw(L+(i>=10?251:0),551-(i>=10?i-10:i)*26,`${String(c.n).padStart(2,"0")}  ${c.title}`,9.2,[.14,.29,.41]));
draw(L,223,"从语言学与语料库，到 Transformer、IE、MT、评测与治理",9.9,[.2,.35,.46]);draw(L,196,"本册为原创短定义与试题；正式 Wiki 与专家审稿另行进行。",9.25,[.29,.39,.48]);draw(L,101,"TERM / ATLAS  ·  2026-11-27",9.8,[.2,.36,.48]);
for(const c of cs){page(`${String(c.n).padStart(2,"0")}. ${c.title}`);c.terms.forEach((t,i)=>term(i+1,t));}
page("附录 A · NLP 核心概念辨析");contrasts.forEach((x,i)=>{if(y<130)page(section,true);para(`${i+1}. ${x[0]}`,10.3,0,[.08,.24,.38]);para(x[1],9.2,13);});
page("附录 B · 中等难度面试题");interviews.forEach((x,i)=>{if(y<130)page(section,true);para(`Q${i+1}. ${x[0]}`,10.3,0,[.08,.24,.38]);para(`答：${x[1]}`,9.2,13);});
page("附录 C · 中等难度考试题");exams.forEach((x,i)=>{if(y<130)page(section,true);para(`${i+1}. ${x[0]}`,10.3,0,[.08,.24,.38]);para(`解析：${x[1]}`,9.2,13);});
page("附录 D · 教材与原始研究");references.forEach((x,i)=>{para(`${i+1}. ${x[0]}`,9.7,0,[.08,.24,.38]);para(x[1],8.6,13);});
para("词条定义为独立整理的教育性概述，不能替代源论文完整条件与评测协议。",9.1,0,[.3,.38,.45]);
if(ops.length)pages.push(ops.join("\n")+"\n");
const obj=[null];obj[1]="<< /Type /Catalog /Pages 2 0 R >>";obj[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${pages.map((_,i)=>`${6+2*i} 0 R`).join(" ")}] >>`;
obj[3]="<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [<< /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 0 >> /DW 1000 >>] /ToUnicode 4 0 R >>";
const cmap="/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n/CMapName /Identity-UCS2 def\n/CMapType 2 def\n1 begincodespacerange\n<0000> <FFFF>\nendcodespacerange\n1 beginbfrange\n<0000> <FFFF> <0000>\nendbfrange\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n";
obj[4]=`<< /Length ${cmap.length} >>\nstream\n${cmap}endstream`;obj[5]="<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>";
for(let i=0;i<pages.length;i++){const pn=6+2*i,s=pn+1;let stream=pages[i]+".83 .87 .91 RG 0.5 w 47 52 m 548 52 l S\n";
stream+=`${col([.40,.48,.55])} BT /FC 8 Tf 1 0 0 1 47 35 Tm <${toHex("TERM / ATLAS  |  NLP")}> Tj ET\n`;
stream+=`${col([.40,.48,.55])} BT /FC 8 Tf 1 0 0 1 490 35 Tm <${toHex(`${i+1} / ${pages.length}`)}> Tj ET\n`;
obj[pn]=`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${W} ${H}] /Resources << /Font << /FC 3 0 R >> >> /Contents ${s} 0 R >>`;
obj[s]=`<< /Length ${stream.length} >>\nstream\n${stream}endstream`;}
let pdf="%PDF-1.4\n%TERM-ATLAS\n",offs=[0];for(let i=1;i<obj.length;i++){offs[i]=pdf.length;pdf+=`${i} 0 obj\n${obj[i]}\nendobj\n`;}
const start=pdf.length;pdf+=`xref\n0 ${obj.length}\n0000000000 65535 f \n`;for(let i=1;i<obj.length;i++)pdf+=`${String(offs[i]).padStart(10,"0")} 00000 n \n`;
pdf+=`trailer\n<< /Size ${obj.length} /Root 1 0 R >>\nstartxref\n${start}\n%%EOF\n`;return {pdf,pages:pages.length};
}
const raws=Array.from({length:20},(_,i)=>fs.readFileSync(path.join(ROOT,"data/nlp/chapters",String(i+1).padStart(2,"0")+".tsv"),"utf8"));
const cs=parseData(raws),terms=cs.flatMap(x=>x.terms);
if(cs.length!==20||cs.some(c=>c.terms.length!==25)||terms.length!==500||new Set(terms.map(x=>x.en.toLowerCase())).size!==500||terms.some(x=>!x.en||!x.zh||!x.definition))throw Error("Expected 20 chapters and 500 unique complete terms");
const tsv=Buffer.from(makeTsv(cs),"utf8"),md=Buffer.from(makeMd(cs),"utf8"),pdf=Buffer.from(makePdf(cs).pdf,"ascii");
const outputs=[["data/nlp.tsv",tsv],["glossaries/nlp.md",md],["docs/glossaries/nlp.md",md],["pdf/nlp.pdf",pdf],["docs/pdf/nlp.pdf",pdf]];
const check=process.argv.includes("--check");
for(const [rel,buf] of outputs){const file=path.join(ROOT,rel);if(check){if(!fs.existsSync(file)||!fs.readFileSync(file).equals(buf))throw Error("Out of sync: "+rel);}else{fs.mkdirSync(path.dirname(file),{recursive:true});fs.writeFileSync(file,buf);}}
console.log((check?"PASS":"GENERATED")+": 500 terms, 20 chapters, "+outputs.length+" synchronized artifacts");
