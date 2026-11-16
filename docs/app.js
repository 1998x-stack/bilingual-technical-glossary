/* TERM/ATLAS · a dependency-free, accessible catalog explorer. */
'use strict';
const $ = (id) => document.getElementById(id);
const SUBJECT_COLORS = ['#6d86e8','#7f73d7','#449bd2','#4bb69d','#e5a760','#db7d97','#6195ab','#7b8db7'];
const SUBJECT_GLYPHS = ['⌘','↗','λ','∇','∞','⊞','∑','∫'];
const PAGE_SIZE = 28;
const state={terms:[],catalog:[],category:'all',topic:'all',query:'',sort:'default',page:1};
function escaped(v){return String(v??'').replace(/[&<>"']/g,s=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[s]));}
function byId(id){return state.catalog.find(item=>item.slug===id);}
function locale(n){return Number(n).toLocaleString('en-US');}
function notify(message){const el=$('toast');el.textContent=message;el.classList.add('show');clearTimeout(notify.t);notify.t=setTimeout(()=>el.classList.remove('show'),2200);}
function download(name,text,type){const blob=new Blob([text],{type});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),3000);}
function updateURL(){const u=new URL(window.location.href);u.search='';if(state.query)u.searchParams.set('q',state.query);if(state.category!=='all')u.searchParams.set('category',state.category);if(state.topic!=='all')u.searchParams.set('topic',state.topic);history.replaceState({},'',u.pathname+u.search+u.hash);}
function applyURL(){const u=new URL(window.location.href);const q=u.searchParams.get('q')||'';const cat=u.searchParams.get('category')||'all';state.query=q;state.category=state.catalog.some(x=>x.slug===cat)?cat:'all';$('search-input').value=q;}
function getVisible(){const q=state.query.toLocaleLowerCase().trim();const terms=state.terms.filter(t=>{
 if(state.category!=='all'&&t.category!==state.category)return false;
 if(state.topic!=='all'&&t.topic!==state.topic)return false;
 if(!q)return true;
 const hay=[t.en,t.zh,t.abbr,t.notation,t.definition,t.topic,byId(t.category)?.zh].join(' ').toLocaleLowerCase();
 return q.split(/\s+/).every(token=>hay.includes(token));
});
if(state.sort==='az')terms.sort((a,b)=>a.en.localeCompare(b.en,'en'));if(state.sort==='za')terms.sort((a,b)=>b.en.localeCompare(a.en,'en'));
return terms;}
function renderSubjects(){const el=$('side-subjects');el.innerHTML='';state.catalog.forEach((s,i)=>{
const a=document.createElement('a');a.className='side-link';a.href='#explorer';a.dataset.category=s.slug;a.innerHTML=`<span class="nav-symbol" style="color:${SUBJECT_COLORS[i%SUBJECT_COLORS.length]}">${SUBJECT_GLYPHS[i%SUBJECT_GLYPHS.length]}</span><span>${escaped(s.zh)}</span><span class="subject-count">${s.count}</span>`;
a.addEventListener('click',()=>chooseCategory(s.slug));el.append(a);});
const select=$('category-filter');state.catalog.forEach(s=>{const opt=document.createElement('option');opt.value=s.slug;opt.textContent=`${s.zh} · ${s.en}`;select.add(opt);});}
function renderCategories(){const grid=$('category-grid');grid.innerHTML='';state.catalog.forEach((s,i)=>{
 const color=SUBJECT_COLORS[i%SUBJECT_COLORS.length];const el=document.createElement('article');el.className='category-card'+(state.category===s.slug?' selected':'');el.style.cursor='pointer';el.tabIndex=0;el.setAttribute('role','button');el.setAttribute('aria-label',`查看${s.zh}，${s.count}条术语`);
 el.innerHTML=`<div class="cat-indicator" style="background:${color}"></div><div class="cat-icon" style="background:${color}19;color:${color}">${SUBJECT_GLYPHS[i%SUBJECT_GLYPHS.length]}</div><div class="cat-title">${escaped(s.zh)}</div><div class="cat-subtitle">${escaped(s.en)}</div><div class="cat-footer"><span>${locale(s.count)} TERMS · ${s.topics} TOPICS</span><span class="cat-arrow">↗</span></div><div class="cat-downloads"><a href="./pdf/${s.slug}.pdf" download>↓ PDF</a><a href="./glossaries/${s.slug}.md" download>↓ Markdown</a></div>`;
 el.querySelectorAll('.cat-downloads a').forEach(a=>a.addEventListener('click',e=>e.stopPropagation()));
 el.addEventListener('click',()=>{chooseCategory(s.slug);document.getElementById('explorer').scrollIntoView({behavior:'smooth'});});
 el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();el.click();}});
 grid.append(el);
 });}
function renderCoverage(){const el=$('coverage-chart');el.innerHTML='';const max=Math.max(1,...state.catalog.map(x=>x.count));state.catalog.forEach((s,i)=>{
const div=document.createElement('div');div.className='bar-row';div.innerHTML=`<span class="bar-label" title="${escaped(s.en)}">${escaped(s.zh)}</span><div class="bar-track"><div class="bar-fill" style="background:${SUBJECT_COLORS[i%SUBJECT_COLORS.length]};width:${Math.max(3,100*s.count/max)}%"></div></div><span class="bar-value">${locale(s.count)}</span>`;el.append(div);});}
function renderTopics(){const select=$('topic-filter');const topics=[...new Set(state.terms.filter(t=>state.category==='all'||t.category===state.category).map(t=>t.topic))];topics.sort((a,b)=>a.localeCompare(b,'zh-Hans-CN'));
const current=state.topic;select.replaceChildren(new Option('全部专题 · All topics','all'));
topics.forEach(topic=>select.add(new Option(topic,topic)));if(topics.includes(current))select.value=current;else{state.topic='all';select.value='all';}}
function chooseCategory(value){state.category=value;state.topic='all';state.page=1;$('category-filter').value=value;renderTopics();renderCategories();renderResults();updateURL();document.querySelectorAll('#side-subjects .side-link').forEach(el=>el.classList.toggle('active',el.dataset.category===value));$('sidebar').classList.remove('open');}
function renderResults(){const filtered=getVisible();const count=filtered.length;const lastPage=Math.max(1,Math.ceil(count/PAGE_SIZE));state.page=Math.max(1,Math.min(state.page,lastPage));
const items=filtered.slice((state.page-1)*PAGE_SIZE,state.page*PAGE_SIZE);const body=$('terms-body');body.replaceChildren();
items.forEach((item,i)=>{const meta=byId(item.category);const tr=document.createElement('tr');const en=item.en||'';const abbrev=item.abbr||'';
tr.innerHTML=`<td class="row-number">${String((state.page-1)*PAGE_SIZE+i+1).padStart(3,'0')}</td><td><span class="term-english">${escaped(en)}</span>${abbrev?`<span class="term-abbr">${escaped(abbrev)}</span>`:''}</td><td><span class="term-chinese">${escaped(item.zh)}</span></td><td><span class="term-category">${escaped(meta?.zh||item.category)}</span><span class="term-topic">${escaped(item.topic)}</span></td><td>${escaped(item.definition)}</td><td><button class="copy-term" aria-label="复制术语 ${escaped(en)}" title="复制中英文术语">⧉</button></td>`;
tr.querySelector('button').addEventListener('click',()=>copyText(`${item.en} — ${item.zh}${item.abbr?` (${item.abbr})`:''}\n${item.definition}`));body.append(tr);});
$('empty-state').hidden=count!==0;$('result-count').textContent=`${locale(count)} 条匹配术语`;
$('page-summary').textContent=count?`显示 ${locale((state.page-1)*PAGE_SIZE+1)}–${locale(Math.min(state.page*PAGE_SIZE,count))} / ${locale(count)} 条`:'没有匹配结果';
$('page-number').textContent=`${state.page} / ${lastPage}`;$('prev-page').disabled=state.page<=1;$('next-page').disabled=state.page>=lastPage;$('clear-search').hidden=!state.query;}
async function copyText(text){try{await navigator.clipboard.writeText(text);notify('已复制到剪贴板');}catch(err){const a=document.createElement('textarea');a.value=text;a.style.position='fixed';a.style.opacity='0';document.body.append(a);a.select();const ok=document.execCommand('copy');a.remove();notify(ok?'已复制到剪贴板':'复制失败，请手动选择文字');}}
function exportCSV(){const filtered=getVisible();const cols=['category','chapter','topic','en','zh','abbr','definition','notation'];const quote=s=>'"'+String(s??'').replace(/"/g,'""')+'"';const rows=[cols.join(','),...filtered.map(t=>cols.map(k=>quote(t[k])).join(','))];download('glossary-'+(state.category==='all'?'all':state.category)+'.csv','\ufeff'+rows.join('\r\n'),'text/csv;charset=utf-8');notify(`已准备 ${locale(filtered.length)} 条 CSV 记录`);}
function bind(){const input=$('search-input');let debounce=null;input.addEventListener('input',e=>{clearTimeout(debounce);debounce=setTimeout(()=>{state.query=e.target.value.trim();state.page=1;renderResults();updateURL();},120);});
$('category-filter').addEventListener('change',e=>chooseCategory(e.target.value));$('topic-filter').addEventListener('change',e=>{state.topic=e.target.value;state.page=1;renderResults();updateURL();});$('sort-select').addEventListener('change',e=>{state.sort=e.target.value;state.page=1;renderResults();});
$('prev-page').addEventListener('click',()=>{state.page--;renderResults();$('explorer').scrollIntoView({behavior:'smooth'});});$('next-page').addEventListener('click',()=>{state.page++;renderResults();$('explorer').scrollIntoView({behavior:'smooth'});});
$('jump-search').addEventListener('click',()=>{document.getElementById('explorer').scrollIntoView({behavior:'smooth'});setTimeout(()=>input.focus({preventScroll:true}),300);});$('view-all-subjects').addEventListener('click',()=>document.getElementById('category-grid').scrollIntoView({behavior:'smooth'}));$('download-csv').addEventListener('click',exportCSV);
$('copy-link').addEventListener('click',()=>copyText(window.location.href));$('clear-search').addEventListener('click',()=>{input.value='';state.query='';state.page=1;renderResults();updateURL();input.focus();});$('reset-filters').addEventListener('click',()=>{input.value='';state.query='';chooseCategory('all');});
$('menu-btn').addEventListener('click',()=>{$('sidebar').classList.toggle('open');});document.addEventListener('click',e=>{if(window.innerWidth<980&&!e.target.closest('#sidebar')&&!e.target.closest('#menu-btn'))$('sidebar').classList.remove('open');});
$('theme-toggle').addEventListener('click',()=>{document.body.classList.toggle('dark');try{localStorage.setItem('term-atlas-theme',document.body.classList.contains('dark')?'dark':'light');}catch(e){}});
window.addEventListener('keydown',e=>{if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'||e.key==='/'){e.preventDefault();input.focus();input.select();}if(e.key==='Escape'){$('sidebar').classList.remove('open');if(document.activeElement===input)input.blur();}});
document.querySelectorAll('.side-nav [data-nav]').forEach(el=>el.addEventListener('click',()=>{$('sidebar').classList.remove('open');document.querySelectorAll('.side-nav [data-nav]').forEach(a=>a.classList.remove('active'));el.classList.add('active');}));}
async function main(){try{if(localStorage.getItem('term-atlas-theme')==='dark')document.body.classList.add('dark');}catch(e){}
bind();try{
 const [catalogRes,termsRes]=await Promise.all([fetch('./data/catalog.json'),fetch('./data/terms.json')]);if(!catalogRes.ok||!termsRes.ok)throw Error('Cannot load glossary dataset');
 state.catalog=await catalogRes.json();state.terms=await termsRes.json();applyURL();
 $('stat-total').textContent=locale(state.terms.length);$('stat-categories').textContent=String(state.catalog.length).padStart(2,'0');$('stat-topics').textContent=locale(state.catalog.reduce((a,s)=>a+s.topics,0));
 renderSubjects();renderCategories();renderCoverage();$('category-filter').value=state.category;renderTopics();renderResults();updateURL();
 }catch(err){console.error(err);$('terms-body').innerHTML='<tr><td colspan="6">术语数据暂时无法加载。请使用 HTTP 服务打开本网站，或查看 GitHub 仓库中的 Markdown 文件。</td></tr>';notify('术语索引加载失败');}}
main();
