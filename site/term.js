/* TERM/ATLAS · unified concept reader. No production batch UI. */
'use strict';
const $ = id => document.getElementById(id);
const escapeHTML = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const termKey = term => JSON.stringify([term.category, Number(term.chapter), term.en, term.zh]);
const urlFor = term => './term.html?' + new URLSearchParams({
  category: term.category, chapter: String(term.chapter), en: term.en, zh: term.zh
}).toString();
const catalogURL = category => './index.html?category=' + encodeURIComponent(category) + '#explorer';

function safeBack(category) {
  const fallback = catalogURL(category);
  const raw = new URLSearchParams(location.search).get('from');
  if (!raw) return fallback;
  try {
    const back = new URL(raw, location.href);
    const base = location.pathname.slice(0, location.pathname.lastIndexOf('/') + 1);
    if (back.origin === location.origin && (back.pathname === base || back.pathname === base + 'index.html')) {
      back.hash = '#explorer';
      return back.href;
    }
  } catch (_) { /* invalid or cross-origin return URL */ }
  return fallback;
}

function validReference(value, sourceURL) {
  try {
    const url = new URL(value.replace(/&amp;/g, '&'), sourceURL);
    return url.protocol === 'https:' || url.protocol === 'http:' ? url : null;
  } catch (_) { return null; }
}

function inlineMarkdown(value, sourceURL) {
  const tokens = [];
  const protect = html => {
    const id = tokens.length;
    tokens.push(html);
    return '\uE000' + id + '\uE001';
  };
  let raw = String(value);
  raw = raw.replace(/`([^`]+)`/g, (_, code) => protect('<code>' + escapeHTML(code) + '</code>'));
  raw = raw.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, href) => {
    const target = validReference(href.trim(), sourceURL);
    if (!target) return label;
    const external = target.origin !== location.origin ? ' target="_blank" rel="noopener noreferrer"' : '';
    return protect('<a href="' + escapeHTML(target.href) + '"' + external + '>' + escapeHTML(label) + '</a>');
  });
  return escapeHTML(raw)
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[^*])\*([^*]+)\*/g, '$1<em>$2</em>')
    .replace(/\uE000([0-9]+)\uE001/g, (_, id) => tokens[Number(id)] ?? '');
}

function renderMarkdown(markdown, sourceURL) {
  const lines = markdown.replace(/\r\n?/g, '\n').split('\n');
  const result = [], headings = [];
  let paragraph = [], list = '', code = null, hideNavigation = false;
  const closeParagraph = () => { if (paragraph.length) result.push('<p>' + inlineMarkdown(paragraph.join(' '), sourceURL) + '</p>'); paragraph = []; };
  const closeList = () => { if (list) result.push('</' + list + '>'); list = ''; };
  for (let i = 0; i < lines.length; i++) {
    const text = lines[i].trim(), raw = lines[i];
    if (hideNavigation) {
      if (!/^##\s/.test(text)) continue;
      hideNavigation = false;
    }
    if (/^##\s+(?:\d+\.\s*)?知识导航/.test(text)) { closeParagraph(); closeList(); hideNavigation = true; continue; }
    if (/^#\s/.test(text)) continue; // The semantic H1 is the term title above.
    if (/^>\s*(?:TERM\/ATLAS|AI Infra Wiki|AI Infra Wiki ·)/i.test(text)) continue; // Internal editorial metadata.
    if (/^\`\`\`/.test(text)) {
      closeParagraph(); closeList();
      if (code === null) code = [];
      else { result.push('<pre><code>' + escapeHTML(code.join('\n')) + '</code></pre>'); code = null; }
      continue;
    }
    if (code !== null) { code.push(raw); continue; }
    if (!text) { closeParagraph(); closeList(); continue; }
    const heading = text.match(/^(#{2,4})\s+(.+)$/);
    if (heading) {
      closeParagraph(); closeList();
      const level = Math.min(4, heading[1].length), id = 'section-' + (headings.length + 1);
      const label = heading[2].replace(/^\d+\.\s*/, '');
      headings.push({id, label});
      result.push('<h' + level + ' id="' + id + '">' + inlineMarkdown(heading[2], sourceURL) + '</h' + level + '>');
      continue;
    }
    if (/^---+$/.test(text)) { closeParagraph(); closeList(); result.push('<hr>'); continue; }
    if (text.startsWith('|') && lines[i+1] && /^\s*\|?[\s:|\-]+\|?\s*$/.test(lines[i+1]) && lines[i+1].includes('-')) {
      closeParagraph(); closeList();
      const cells = line => line.replace(/^\|/, '').replace(/\|$/, '').split('|').map(v => v.trim());
      const cols = cells(text);
      result.push('<div class="article-table-wrap"><table><thead><tr>' + cols.map(c => '<th>' + inlineMarkdown(c, sourceURL) + '</th>').join('') + '</tr></thead><tbody>');
      i++;
      while (i + 1 < lines.length && lines[i+1].trim().startsWith('|')) {
        const row = cells(lines[++i].trim());
        result.push('<tr>' + row.map(c => '<td>' + inlineMarkdown(c, sourceURL) + '</td>').join('') + '</tr>');
      }
      result.push('</tbody></table></div>');
      continue;
    }
    if (text.startsWith('> ')) {
      closeParagraph(); closeList(); result.push('<blockquote>' + inlineMarkdown(text.slice(2), sourceURL) + '</blockquote>'); continue;
    }
    const ordered = text.match(/^\d+\.\s+(.+)$/), bullet = text.match(/^[-*]\s+(.+)$/);
    if (ordered || bullet) {
      closeParagraph(); const type = ordered ? 'ol' : 'ul';
      if (list !== type) { closeList(); list = type; result.push('<' + type + '>'); }
      result.push('<li>' + inlineMarkdown((ordered || bullet)[1], sourceURL) + '</li>');
      continue;
    }
    closeList();
    paragraph.push(text);
  }
  closeParagraph(); closeList();
  if (code !== null) result.push('<pre><code>' + escapeHTML(code.join('\n')) + '</code></pre>');
  return {html: result.join('\n'), headings};
}

function createAnchor(term, label) {
  const link = document.createElement('a');
  link.href = urlFor(term);
  link.textContent = label || term.en;
  return link;
}

function renderRelated(term, terms) {
  const within = terms.filter(t => t.category === term.category && t.topic === term.topic);
  const current = within.findIndex(t => termKey(t) === termKey(term));
  const near = within.slice(Math.max(0, current - 3), Math.max(0, current - 3) + 8);
  for (const t of near) {
    const a = createAnchor(t, t.en + ' · ' + t.zh);
    if (termKey(t) === termKey(term)) a.className = 'current';
    $('related-terms').append(a);
    const side = createAnchor(t, t.zh);
    $('related-side').append(side);
  }
  const siblings = terms.filter(t => t.category === term.category);
  const position = siblings.findIndex(t => termKey(t) === termKey(term));
  const neighbors = [[position - 1, 'prev-term', '← '], [position + 1, 'next-term', '→ ']];
  for (const [idx, id, prefix] of neighbors) {
    if (idx < 0 || idx >= siblings.length) continue;
    const a = $(id);
    a.href = urlFor(siblings[idx]);
    a.textContent = prefix + siblings[idx].en + ' · ' + siblings[idx].zh;
    a.hidden = false;
  }
}

async function main() {
  try { if (localStorage.getItem('term-atlas-theme') === 'dark') document.body.classList.add('dark'); } catch (_) {}
  $('theme-toggle').addEventListener('click', () => {
    document.body.classList.toggle('dark');
    try { localStorage.setItem('term-atlas-theme', document.body.classList.contains('dark') ? 'dark' : 'light'); } catch (_) {}
  });
  $('menu-btn').addEventListener('click', () => $('sidebar').classList.toggle('open'));
  document.addEventListener('click', event => {
    if (innerWidth < 980 && !event.target.closest('#sidebar') && !event.target.closest('#menu-btn')) $('sidebar').classList.remove('open');
  });
  const params = new URLSearchParams(location.search);
  const category = params.get('category'), chapter = Number(params.get('chapter')), en = params.get('en'), zh = params.get('zh');
  if (!category || !Number.isInteger(chapter) || !en || !zh) { $('detail-loading').hidden = true; $('detail-error').hidden = false; return; }
  try {
    const [termsRes, catalogRes, wikiRes] = await Promise.all([
      fetch('./data/terms.json'), fetch('./data/catalog.json'),
      fetch('./data/wiki-index.json').catch(() => null),
    ]);
    if (!termsRes.ok || !catalogRes.ok) throw Error('Glossary dataset is unavailable');
    const terms = await termsRes.json(), catalog = await catalogRes.json();
    let wiki = {articles: []};
    let wikiUnavailable = false;
    if (wikiRes && wikiRes.ok) wiki = await wikiRes.json();
    else wikiUnavailable = true;
    const entry = terms.find(t => t.category === category && t.chapter === chapter && t.en === en && t.zh === zh);
    if (!entry) throw Error('No matching term');
    document.title = entry.en + ' · TERM/ATLAS';
    const domain = catalog.find(c => c.slug === entry.category);
    const domainName = domain?.zh || entry.category;
    const back = safeBack(entry.category);
    $('return-explorer').href = back;
    $('sidebar-back').href = back;
    $('category-link').href = catalogURL(entry.category);
    $('category-link').textContent = domainName;
    $('topic-text').textContent = entry.topic;
    $('detail-title').textContent = entry.en;
    $('detail-zh').textContent = entry.zh + (entry.abbr ? ' · ' + entry.abbr : '');
    $('detail-category').textContent = domainName;
    $('detail-topic').textContent = entry.topic;
    $('detail-definition').textContent = entry.definition;
    if (entry.notation) { $('detail-notation').textContent = '常用记号：' + entry.notation; $('detail-notation').hidden = false; }
    renderRelated(entry, terms);
    $('copy-term-link').addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(location.href); $('copy-term-link').textContent = '已复制'; }
      catch (_) { $('copy-term-link').textContent = '请从地址栏复制链接'; }
    });
    const article = wiki.articles.find(a => termKey(a) === termKey(entry));
    if (article && /^wiki\/[a-z0-9-]+\/[0-9]{3}-[a-z0-9-]+\.md$/.test(article.path)) {
      $('detail-state').textContent = '专业解析';
      $('detail-state').className = 'detail-has-article';
      const response = await fetch('./' + article.path);
      if (!response.ok) throw Error('Published article could not be loaded');
      const data = renderMarkdown(await response.text(), new URL('./' + article.path, location.href));
      $('wiki-article').innerHTML = data.html;
      $('wiki-article').hidden = false;
      if (data.headings.length) {
        $('toc-card').hidden = false;
        for (const h of data.headings) {
          const a = document.createElement('a');
          a.href = '#' + h.id; a.textContent = h.label;
          $('article-toc').append(a);
        }
      }
    } else {
      $('detail-state').textContent = '术语释义';
      $('wiki-fallback').hidden = false;
      if (wikiUnavailable) $('wiki-fallback').querySelector('p').textContent = '术语定义已载入；延伸解析索引暂时不可用，请稍后重试。';
    }
    $('detail-loading').hidden = true; $('detail-content').hidden = false;
  } catch (error) {
    console.error(error);
    $('detail-loading').hidden = true; $('detail-error').hidden = false;
    if (!/No matching term/.test(error.message)) $('detail-error').querySelector('p').textContent = '术语或文章数据暂时无法加载，请从检索页重新进入。';
  }
}
main();
