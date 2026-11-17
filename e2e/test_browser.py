"""Real Chromium end-to-end checks of the built GitHub Pages site.

Run: python -m pip install playwright==1.56.0
     python -m playwright install --with-deps chromium
     python -m unittest discover -s e2e -v
"""
from __future__ import annotations
import re
import threading
import unittest
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from playwright.sync_api import sync_playwright, expect

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/"docs"
ARTIFACTS=ROOT/"e2e-artifacts"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class ExplorerBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        handler=partial(QuietHandler,directory=str(DOCS))
        cls.httpd=ThreadingHTTPServer(("127.0.0.1",0),handler)
        cls.server_thread=threading.Thread(target=cls.httpd.serve_forever,daemon=True)
        cls.server_thread.start()
        cls.base=f"http://127.0.0.1:{cls.httpd.server_address[1]}"
        cls.pw=sync_playwright().start()
        cls.browser=cls.pw.chromium.launch(headless=True)
        ARTIFACTS.mkdir(exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def setUp(self):
        self.context=self.browser.new_context(viewport={"width":1365,"height":900},device_scale_factor=1)
        self.page=self.context.new_page()
        self.errors=[]
        self.page.on("pageerror",lambda error:self.errors.append(str(error)))

    def tearDown(self):
        try:
            self.page.screenshot(path=str(ARTIFACTS/(self._testMethodName+".png")),full_page=True)
            self.assertEqual(self.errors,[],"JavaScript errors found")
        finally:
            self.context.close()

    def home(self,category):
        self.page.goto(f"{self.base}/?category={category}#explorer")
        expect(self.page.locator("#terms-body tr").first).to_be_visible(timeout=15000)

    def test_published_article_clickthrough_bilingual_semantics(self):
        self.home("ai-infrastructure")
        first=self.page.locator("#terms-body tr").first
        expect(first.locator("a.term-english")).to_have_text("Graphics Processing Unit")
        expect(first.locator("a.term-chinese")).to_have_text("图形处理器")
        first.locator("a.term-english").click()
        expect(self.page).to_have_url(re.compile(r"/term\.html\?"))
        expect(self.page.get_by_role("heading",name="Graphics Processing Unit",level=1)).to_be_visible()
        expect(self.page.get_by_role("heading",name=re.compile("技术原理"),level=2)).to_be_visible()
        expect(self.page.locator("#wiki-article")).to_be_visible()
        expect(self.page.locator("#article-toc a").first).to_be_visible()
        expect(self.page.locator("#detail-state")).to_have_text("专业解析")
        self.assertNotIn("Batch",self.page.locator("main").inner_text())
        self.page.screenshot(path=str(ARTIFACTS/"desktop-wiki.png"),full_page=True)

    def test_new_distributed_training_article_is_published_in_explorer(self):
        self.home("ai-infrastructure")
        self.page.locator("#search-input").fill("distributed data parallel")
        match=self.page.locator("#terms-body tr").first
        expect(match.locator("a.term-english")).to_have_text("Distributed Data Parallel")
        match.locator("a.term-english").click()
        expect(self.page.get_by_role("heading",name="Distributed Data Parallel",level=1)).to_be_visible()
        expect(self.page.locator("#detail-state")).to_have_text("专业解析")
        expect(self.page.get_by_role("heading",name=re.compile("中等难度考试题"),level=2)).to_be_visible()
        expect(self.page.locator("#wiki-article a[href^='https://']").first).to_be_visible()
        self.assertNotIn("Batch 03",self.page.locator("main").inner_text())

    def test_inference_metric_and_paged_attention_articles(self):
        self.home("ai-infrastructure")
        self.page.locator("#search-input").fill("Paged Attention")
        first=self.page.locator("#terms-body tr").first
        expect(first.locator("a.term-english")).to_have_text("Paged Attention")
        first.locator("a.term-english").click()
        expect(self.page.get_by_role("heading",name="Paged Attention",level=1)).to_be_visible()
        expect(self.page.locator("#detail-state")).to_have_text("专业解析")
        expect(self.page.get_by_role("heading",name=re.compile("技术原理"),level=2)).to_be_visible()
        expect(self.page.locator("#wiki-article a[href^='https://']").first).to_be_visible()
        self.assertNotIn("Batch 04", self.page.locator("main").inner_text())

    def test_new_kubernetes_gpu_scheduling_article_is_published_in_explorer(self):
        self.home("ai-infrastructure")
        self.page.locator("#search-input").fill("Kubernetes")
        match=self.page.locator("#terms-body tr").first
        expect(match.locator("a.term-english")).to_have_text("Kubernetes")
        match.locator("a.term-english").click()
        expect(self.page.get_by_role("heading",name="Kubernetes",level=1)).to_be_visible()
        expect(self.page.locator("#detail-state")).to_have_text("专业解析")
        expect(self.page.get_by_role("heading",name=re.compile("技术原理"),level=2)).to_be_visible()
        expect(self.page.locator("#wiki-article a[href^='https://']").first).to_be_visible()
        self.assertNotIn("Batch 05",self.page.locator("main").inner_text())

    def test_storage_and_slo_articles_are_published_in_unified_explorer(self):
        for concept in ("Data Loader", "Service Level Objective"):
            with self.subTest(concept=concept):
                self.home("ai-infrastructure")
                self.page.locator("#search-input").fill(concept)
                match=self.page.locator("#terms-body tr").first
                expect(match.locator("a.term-english")).to_have_text(concept)
                match.locator("a.term-english").click()
                expect(self.page.get_by_role("heading",name=concept,level=1)).to_be_visible()
                expect(self.page.locator("#detail-state")).to_have_text("专业解析")
                expect(self.page.get_by_role("heading",name=re.compile("技术原理"),level=2)).to_be_visible()
                expect(self.page.get_by_role("heading",name=re.compile("中等难度考试题"),level=2)).to_be_visible()
                expect(self.page.locator("#wiki-article a[href^='https://']").first).to_be_visible()
                self.assertNotIn("Batch 06",self.page.locator("main").inner_text())

    def test_observability_and_gpu_efficiency_articles_are_complete(self):
        for concept in ("Logs", "GPU Utilization"):
            with self.subTest(concept=concept):
                self.home("ai-infrastructure")
                self.page.locator("#search-input").fill(concept)
                first=self.page.locator("#terms-body tr").first
                expect(first.locator("a.term-english")).to_have_text(concept)
                first.locator("a.term-english").click()
                expect(self.page.get_by_role("heading",name=concept,level=1)).to_be_visible()
                expect(self.page.locator("#detail-state")).to_have_text("专业解析")
                expect(self.page.get_by_role("heading",name=re.compile("中等难度考试题"),level=2)).to_be_visible()
                expect(self.page.locator("#wiki-article a[href^='https://']").first).to_be_visible()
                self.assertNotIn("Batch 07",self.page.locator("main").inner_text())

    def test_spot_and_reserved_instances_are_full_wiki_articles(self):
        for concept in ("Spot Instance", "Reserved Instance"):
            with self.subTest(concept=concept):
                self.home("ai-infrastructure")
                self.page.locator("#search-input").fill(concept)
                first=self.page.locator("#terms-body tr").first
                expect(first.locator("a.term-english")).to_have_text(concept)
                first.locator("a.term-english").click()
                expect(self.page.get_by_role("heading",name=concept,level=1)).to_be_visible()
                expect(self.page.locator("#detail-state")).to_have_text("专业解析")
                expect(self.page.get_by_role("heading",name=re.compile("技术原理"),level=2)).to_be_visible()
                expect(self.page.locator("#wiki-article a[href^='https://']").first).to_be_visible()
                self.assertNotIn("Batch 08",self.page.locator("main").inner_text())

    def test_unwritten_wiki_is_honestly_short_definition(self):
        self.home("reinforcement-learning")
        self.page.locator("#terms-body tr").first.locator("a.term-chinese").click()
        expect(self.page.locator("#detail-definition")).not_to_be_empty()
        expect(self.page.locator("#wiki-fallback")).to_be_visible()
        expect(self.page.locator("#wiki-article")).to_be_hidden()
        expect(self.page.locator("#detail-state")).to_have_text("术语释义")

    def test_preserves_search_query_and_keyboard_focus(self):
        self.home("ai-infrastructure")
        self.page.keyboard.press("/")
        expect(self.page.locator("#search-input")).to_be_focused()
        self.page.locator("#search-input").fill("graphics processing unit")
        expect(self.page.locator("#terms-body tr").first).to_be_visible()
        self.page.locator("#terms-body tr").first.locator("a.term-english").click()
        self.page.locator("#return-explorer").click()
        expect(self.page.locator("#search-input")).to_have_value("graphics processing unit")
        expect(self.page.locator("#category-filter")).to_have_value("ai-infrastructure")

    def test_mobile_layout_navigation_and_theme(self):
        self.context.close()
        self.context=self.browser.new_context(viewport={"width":390,"height":844},device_scale_factor=1,is_mobile=True,has_touch=True)
        self.page=self.context.new_page()
        self.page.on("pageerror",lambda error:self.errors.append(str(error)))
        self.home("ai-infrastructure")
        self.assertLessEqual(self.page.evaluate("document.documentElement.scrollWidth - innerWidth"),3)
        self.page.locator("#menu-btn").click()
        expect(self.page.locator("#sidebar")).to_have_class(re.compile("open"))
        # An open mobile drawer intentionally covers the content: close it first.
        # Tap outside the open drawer, as an actual mobile user would.
        self.page.mouse.click(370, 110)
        expect(self.page.locator("#sidebar")).not_to_have_class(re.compile("open"))
        self.page.locator("#terms-body tr").first.locator("a.term-english").click()
        expect(self.page.locator("#detail-content")).to_be_visible()
        self.assertLessEqual(self.page.evaluate("document.documentElement.scrollWidth - innerWidth"),3)
        self.page.locator("#theme-toggle").click()
        expect(self.page.locator("body")).to_have_class(re.compile("dark"))
        self.page.screenshot(path=str(ARTIFACTS/"mobile-detail-dark.png"),full_page=True)

    def test_markdown_complex_table_code_and_formula_are_readable_and_escaped(self):
        self.home("ai-infrastructure")
        self.page.locator("#terms-body tr").first.locator("a.term-english").click()
        # Wait for cross-page navigation and deferred term.js initialization.
        # A successful click alone does not guarantee renderMarkdown is loaded.
        expect(self.page).to_have_url(re.compile(r"/term\.html\?"), timeout=15000)
        expect(self.page.locator("#wiki-article")).to_be_visible(timeout=15000)
        self.page.wait_for_function("typeof renderMarkdown === 'function'", timeout=15000)
        result=self.page.evaluate("""() => renderMarkdown(
          '## Example\\n\\n| Item | Value |\\n|---|---|\\n| alpha | **beta** |\\n\\n```python\\nprint("<svg onload=alert(1)>")\\n```\\n\\n\\\\(E=mc^2\\\\)',
          new URL('./wiki/ai-infrastructure/001-graphics-processing-unit.md', location.href)
        ).html""")
        self.assertIn("<table>",result)
        self.assertIn("<pre><code>",result)
        self.assertNotIn("<svg onload",result)
        self.assertIn("E=mc^2",result)
        malicious=self.page.evaluate("""() => renderMarkdown('<img src=x onerror=alert(1)>\\n\\n[x](javascript:alert(1))',location.href).html""")
        self.assertNotIn("<img src=",malicious)
        self.assertNotIn('href="javascript:',malicious)

    def test_new_a2a_article_is_rendered_in_unified_ai_agent_explorer(self):
        self.home("ai-agents")
        self.page.locator("#search-input").fill("Agent2Agent Protocol")
        item=self.page.locator("#terms-body tr").first
        expect(item.locator("a.term-english")).to_have_text("Agent2Agent Protocol (A2A)")
        item.locator("a.term-english").click()
        expect(self.page.locator("#detail-state")).to_have_text("专业解析", timeout=15000)
        expect(self.page.locator("#wiki-article")).to_be_visible(timeout=15000)
        expect(self.page.get_by_role("heading", name=re.compile("技术原理"), level=2)).to_be_visible()
        expect(self.page.locator("#wiki-article")).to_contain_text("Agent Card")
        expect(self.page.locator("#wiki-article")).to_contain_text("Task")
        self.assertNotIn("Batch", self.page.locator("main").inner_text())

    def test_accessible_landmarks_and_focusable_article_navigation(self):
        self.home("ai-infrastructure")
        expect(self.page.get_by_role("main")).to_have_count(1)
        expect(self.page.get_by_role("navigation",name="主要导航")).to_have_count(1)
        self.page.locator("#terms-body tr").first.locator("a.term-english").click()
        expect(self.page.get_by_role("main")).to_have_count(1)
        expect(self.page.get_by_role("navigation",name="文章章节")).to_have_count(1)
        expect(self.page.get_by_role("heading",level=1)).to_have_count(1)
        item=self.page.locator("#article-toc a").first
        self.assertTrue(item.get_attribute("href").startswith("#section-"))
        item.focus()
        expect(item).to_be_focused()
        item.press("Enter")
        self.assertTrue(self.page.url.endswith(item.get_attribute("href")))

if __name__=="__main__":
    unittest.main()
