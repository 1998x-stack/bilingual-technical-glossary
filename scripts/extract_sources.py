from pathlib import Path
import fitz,re,json,csv
OUT=Path(__file__).resolve().parents[1]; SRC=OUT/'pdf'
CONFIG={
'ai-agents':('ai-agents.pdf',3,(86,208,369),['基础概念与角色','模型能力与推理','任务规划与决策','工具使用与环境交互','上下文、记忆与状态','检索与知识增强','工作流与编排模式','多智能体协作','MCP：模型上下文协议','A2A：智能体间协议','执行状态、持久化与恢复','评测体系与常见基准','安全防护与治理','智能体攻击与风险','工程化、成本与可观测性','开发实践与生态术语']),
'linear-algebra':('linear-algebra.pdf',2,(52,163,412),['基础概念与数学记号','向量与几何','矩阵类型与基本运算','线性方程组与消元','行列式、秩与可逆性','向量空间、基与维数','线性映射与表示','特征值、对角化与规范形','内积、正交与投影','二次型、正定性与合同','矩阵分解与数值计算','扩展概念与应用']),
'reinforcement-learning':('reinforcement-learning.pdf',2,(232,84,345),['基础概念与交互机制','马尔可夫决策过程与建模','价值函数与贝尔曼方程','蒙特卡洛、时序差分与资格迹','策略类别与经典表格算法','策略梯度、信赖域与行动者—评论家','深度强化学习与训练工程','分布式价值、风险与不确定性','探索、规划与模型学习','模仿学习与离线强化学习','多智能体与层级强化学习','奖励模型、RLHF 与偏好优化','评测、基准与常见环境','高级主题与应用']),
'deep-learning':('deep-learning.pdf',2,(252,62,369),['基础概念与张量','学习范式与数据处理','神经网络与基础模块','训练流程与梯度优化','损失函数、泛化与评估','卷积网络与计算机视觉','序列模型与时序学习','注意力机制与 Transformer','自监督、对比与表示学习','自然语言处理与大语言模型','生成模型与扩散模型','多模态学习与视觉语言','图神经网络与结构化学习','强化学习与对齐','模型压缩与高效微调','推理服务与系统部署','训练系统、分布式与工程','安全、可解释性与研究方法']),
'large-language-models':('large-language-models.pdf',2,(228,50,340),['基础概念与模型类别','数据、词元与文本表示','网络结构与 Transformer','预训练目标与训练策略','训练优化与分布式技术','指令微调与模型适配','偏好优化与人类反馈','提示工程与上下文学习','推理、解码与采样','模型推理加速与服务','检索增强生成与知识库','Agent 与工具使用','多模态大模型','评测与基准','安全、对齐与可信性','LLMOps 与部署工程']),
'probability-theory':('probability-theory.pdf',2,(58,205,409),['概率空间与事件','计数原理与经典概率','条件概率、独立性与贝叶斯公式','随机变量与分布函数','常见离散概率分布','常见连续概率分布','多维随机变量与联合分布','数字特征与矩','随机变量函数与变换','收敛与极限定理','条件期望与鞅','随机过程','泊松过程与布朗运动','测度论概率基础','统计推断与贝叶斯统计','信息论与概率不等式'])}
def lines(pg):
 out=[]
 for b in pg.get_text('dict')['blocks']:
  for l in b.get('lines',[]):
   s=''.join(p['text'] for p in l['spans']).strip()
   if s: out.append((float(l['bbox'][0]),float(l['bbox'][1]),s))
 return sorted(out,key=lambda z:(z[1],z[0]))
def extract(slug):
 fname,start,(cx,ex,dx),topics=CONFIG[slug]; doc=fitz.open(SRC/fname)
 found=[]; chapter=1; seen=set()
 for page in range(start,len(doc)):
  L=lines(doc[page]); marks=[]
  if slug in ('ai-agents','linear-algebra'): reg=r'CHAPTER\s+(\d{1,2})'
  elif slug=='deep-learning': reg=r'SECTION\s+(\d{1,2})'
  elif slug=='reinforcement-learning':reg=r'^(\d{2})$'
  else:reg=r'^(\d{2})\s+[^\d].{2,}'
  for x,y,s in L:
   m=re.search(reg,s,re.I)
   if m and 0<int(m.group(1))<=len(topics) and y<785 and (slug!='reinforcement-learning' or (y<110 and 40<x<65)):marks.append((y,int(m.group(1))))
  EN=[(x,y,s) for x,y,s in L if ex-5<=x<=ex+5 and 100<y<800]
  ZH=[(x,y,s) for x,y,s in L if cx-5<=x<=cx+5 and 100<y<800]
  DE=[(x,y,s) for x,y,s in L if dx-5<=x<=dx+5 and 100<y<800]
  anchors=[]
  for z in ZH:
   matches=sorted(EN,key=lambda a:abs(a[1]-z[1]))[:1]
   if not matches or abs(matches[0][1]-z[1])>3.5:continue
   e=matches[0]
   if z[2] in ['中文译名','中文术语','中文常用译法'] or 'english term' in e[2].lower() or not re.search('[A-Za-z]',e[2]):continue
   if len(e[2])>115 or len(z[2])>60:continue
   anchors.append((z,e))
  used=set(); anchors2=[]
  for z,e in anchors:
   key=(round(z[1]),e[2]);
   if key in used:continue
   used.add(key);anchors2.append((z,e))
  for i,(z,e) in enumerate(anchors2):
   y=z[1]; end=anchors2[i+1][0][1] if i+1<len(anchors2) else 803
   nextmark=min((my for my,n in marks if y<my<end),default=end);end=min(end,nextmark)
   es=[v[2] for v in EN if y-2.1<=v[1]<min(end-1,y+35)]
   ds=[v[2] for v in DE if y-2.1<=v[1]<min(end-1,y+38)]
   english=' '.join(es) if es else e[2]; definition=''.join(ds)
   if not definition or len(english)>120:continue
   prior=[n for my,n in marks if my<y]
   if prior:chapter=prior[-1]
   cn=z[2].strip(); key=(chapter,english.lower(),cn.lower())
   if key in seen:continue
   seen.add(key)
   abbr='';m=re.search(r'\(([A-Z][A-Za-z0-9+./_-]{1,18})\)\s*$',english)
   if m:abbr=m.group(1)
   if slug=='reinforcement-learning':
    bb=[s for x,yy,s in L if 165<=x<=190 and abs(yy-y)<3]
    if bb:abbr=bb[0]
   found.append({'category':slug,'chapter':chapter,'topic':topics[chapter-1],'en':english,'zh':cn,'abbr':abbr,'definition':definition})
  if marks:chapter=marks[-1][1]
 print(slug,len(found),'FIRST',found[:1]);return found
if __name__=='__main__':
 data=[]
 for slug in CONFIG:data.extend(extract(slug))
 (OUT/'data/terms.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
 with (OUT/'data/terms.csv').open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
 print('Total',len(data))
