#!/usr/bin/env python3
"""
Build a single HTML/PDF course book from the current CS 201 module pages.

The book order comes from manifest.json. Each source page is sanitized for
offline/print output, combined into one document, and rendered to PDF with
headless Chrome when available.
"""

from __future__ import annotations

import html
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, unquote, urlsplit

from bs4 import BeautifulSoup


ROOT = Path(__file__).parent.resolve()
MANIFEST_PATH = ROOT / "manifest.json"
STYLE_PATH = ROOT / "style.css"
OUTPUT_DIR = ROOT / "dist"
BOOK_HTML_PATH = OUTPUT_DIR / "cs201-course-book.html"
BOOK_PDF_PATH = OUTPUT_DIR / "cs201-course-book.pdf"

SHARED_PREFIXES = ("/shared/", "/d2l/")
BOOK_DATE = "April 21, 2026"
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


@dataclass(frozen=True)
class PageRecord:
    module_id: str
    module_title: str
    module_index: int
    file_name: str
    page_title: str
    page_index: int
    source_path: Path
    anchor_id: str

    @property
    def path_from_root(self) -> Path:
        return self.source_path.relative_to(ROOT)

    @property
    def is_module_overview(self) -> bool:
        return self.file_name.lower().endswith("overview.html")

    @property
    def is_module_summary(self) -> bool:
        return self.file_name.lower().endswith("summary.html")

    @property
    def is_reference(self) -> bool:
        return self.module_id == "module-reference"

    @property
    def kind(self) -> str:
        if self.is_reference:
            return "reference"
        if self.is_module_overview:
            return "overview"
        if self.is_module_summary:
            return "summary"
        return "lesson"

    @property
    def classes(self) -> str:
        classes = ["book-page", f"book-page-{self.kind}"]
        if self.page_index == 1:
            classes.append("chapter-opener")
        return " ".join(classes)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "page"


def normalize_text(value: str) -> str:
    text = html.unescape(value).replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def load_manifest() -> dict:
    with MANIFEST_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def build_records(manifest: dict) -> list[PageRecord]:
    records: list[PageRecord] = []
    for module_index, module in enumerate(manifest["modules"], start=1):
        for page_index, page in enumerate(module["pages"], start=1):
            source_path = ROOT / module["id"] / page["file"]
            page_slug = slugify(page["file"].removesuffix(".html"))
            anchor_id = f"{module['id']}-{page_slug}"
            records.append(
                PageRecord(
                    module_id=module["id"],
                    module_title=module["title"],
                    module_index=module_index,
                    file_name=page["file"],
                    page_title=page["title"],
                    page_index=page_index,
                    source_path=source_path,
                    anchor_id=anchor_id,
                )
            )
    return records


def gather_inline_styles(records: Iterable[PageRecord]) -> list[str]:
    styles: list[str] = []
    seen: set[str] = set()
    for record in records:
        soup = BeautifulSoup(record.source_path.read_text(encoding="utf-8", errors="replace"), "html.parser")
        for style_tag in soup.find_all("style"):
            css = style_tag.get_text("\n", strip=True)
            if css and css not in seen:
                seen.add(css)
                styles.append(css)
    return styles


def is_external_url(url: str) -> bool:
    if not url:
        return False
    lower = url.lower()
    return lower.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "data:"))


def resolve_local_target(current_dir: Path, url: str) -> Path | None:
    if not url or url.startswith("#") or is_external_url(url):
        return None

    parts = urlsplit(url)
    raw_path = unquote(parts.path)
    if not raw_path or raw_path.startswith("#"):
        return None
    if raw_path.startswith(SHARED_PREFIXES):
        return None

    if raw_path.startswith("/"):
        candidate = (ROOT / raw_path.lstrip("/")).resolve()
    else:
        candidate = (current_dir / raw_path).resolve()

    try:
        candidate.relative_to(ROOT)
    except ValueError:
        return None

    return candidate


def to_output_href(target: Path) -> str:
    rel_path = Path(os.path.relpath(target, start=BOOK_HTML_PATH.parent))
    return quote(rel_path.as_posix(), safe="/")


def replace_iframe(iframe_tag, soup: BeautifulSoup) -> None:
    title = iframe_tag.get("title", "").strip()
    label = f'Interactive activity "{html.escape(title)}"' if title else "Interactive activity"
    replacement = soup.new_tag("div", attrs={"class": "book-interactive-note"})
    replacement.string = f"{label} is omitted from the PDF edition."
    iframe_tag.replace_with(replacement)


def rewrite_asset_url(tag, attr_name: str, current_dir: Path, page_lookup: dict[Path, str]) -> None:
    url = tag.get(attr_name)
    if not url:
        return

    if url.startswith("#") or is_external_url(url):
        return

    parts = urlsplit(url)
    raw_path = unquote(parts.path)
    if raw_path.startswith(SHARED_PREFIXES):
        if tag.name == "img":
            tag.decompose()
        elif tag.name == "a":
            tag.unwrap()
        else:
            tag.decompose()
        return

    target = resolve_local_target(current_dir, url)
    if target is None:
        return

    if target.suffix.lower() == ".html" and target in page_lookup:
        tag[attr_name] = f"#{page_lookup[target]}"
        return

    if target.exists():
        tag[attr_name] = to_output_href(target)


def remove_empty_elements(soup: BeautifulSoup) -> None:
    meaningful = {"img", "table", "pre", "code", "figure", "iframe", "hr", "br", "ul", "ol"}
    changed = True
    while changed:
        changed = False
        for tag in list(soup.find_all(True)):
            if tag.name in meaningful:
                continue
            if tag.get("id") == "cs201-nav":
                tag.decompose()
                changed = True
                continue
            text = tag.get_text(" ", strip=True).replace("\xa0", "")
            if tag.find(True):
                continue
            if not text:
                tag.decompose()
                changed = True


def is_practice_heading(tag) -> bool:
    if tag.name not in HEADING_TAGS:
        return False
    return normalize_text(tag.get_text(" ", strip=True)).lower() in {
        "practice problem",
        "practice problems",
    }


def is_practice_intro(tag) -> bool:
    if tag.name not in {"p", "div"}:
        return False
    text = normalize_text(tag.get_text(" ", strip=True)).lower()
    return text.startswith(
        "use these practice problems to check your understanding"
    )


def is_practice_prompt(tag) -> bool:
    if tag.name not in {"p", "div"}:
        return False
    text = normalize_text(tag.get_text(" ", strip=True)).lower()
    return text.startswith("practice problem:")


def is_d2l_practice_iframe(tag) -> bool:
    if tag.name != "iframe":
        return False
    src = tag.get("src", "")
    return "quicklink.d2l" in src.lower()


def remove_practice_content(body: BeautifulSoup) -> None:
    for tag in list(body.find_all(True)):
        if (
            is_practice_heading(tag)
            or is_practice_intro(tag)
            or is_practice_prompt(tag)
            or is_d2l_practice_iframe(tag)
        ):
            tag.decompose()


def sanitize_page(record: PageRecord, page_lookup: dict[Path, str]) -> str:
    soup = BeautifulSoup(record.source_path.read_text(encoding="utf-8", errors="replace"), "html.parser")
    body = soup.body or soup

    for tag in soup.find_all(["script", "style", "link", "meta", "noscript"]):
        tag.decompose()

    for selector in ("#cs201-nav", ".banner-img", ".bg-img-wrapper", "footer"):
        for tag in body.select(selector):
            tag.decompose()

    first_h1 = body.find("h1")
    if first_h1 is not None:
        first_h1.decompose()

    remove_practice_content(body)

    for iframe in list(body.find_all("iframe")):
        replace_iframe(iframe, soup)

    for image in list(body.find_all("img")):
        rewrite_asset_url(image, "src", record.source_path.parent, page_lookup)

    for anchor in list(body.find_all("a")):
        rewrite_asset_url(anchor, "href", record.source_path.parent, page_lookup)
        anchor.attrs.pop("target", None)
        anchor.attrs.pop("rel", None)

    for tag in body.find_all(True):
        tag.attrs.pop("loading", None)

    remove_empty_elements(body)

    inner_html = "".join(str(child) for child in body.contents).strip()
    return f"""<section id="{record.anchor_id}" class="{record.classes}">
  <header class="book-page-header">
    <p class="book-module-label">{html.escape(record.module_title)}</p>
    <h1>{html.escape(record.page_title)}</h1>
  </header>
  <div class="book-page-content">
{inner_html}
  </div>
</section>"""


def build_toc(manifest: dict, records: list[PageRecord]) -> str:
    anchor_by_file = {record.source_path: record.anchor_id for record in records}
    sections: list[str] = []
    for module in manifest["modules"]:
        items: list[str] = []
        for page in module["pages"]:
            source_path = ROOT / module["id"] / page["file"]
            anchor_id = anchor_by_file[source_path]
            items.append(
                f'      <li><a href="#{anchor_id}">{html.escape(page["title"])}</a></li>'
            )
        sections.append(
            "\n".join(
                [
                    '  <section class="toc-module">',
                    f"    <h2>{html.escape(module['title'])}</h2>",
                    "    <ol>",
                    *items,
                    "    </ol>",
                    "  </section>",
                ]
            )
        )
    return "\n".join(sections)


def build_book_css(base_css: str, inline_styles: list[str]) -> str:
    inline_css = "\n\n".join(inline_styles)
    return f"""{base_css}

{inline_css}

@page {{
  size: Letter;
  margin: 0.7in 0.7in 0.8in;
}}

html {{
  font-size: 14px;
}}

body {{
  margin: 0;
  color: #18212b;
  background: #f4f1e8;
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.65;
}}

a {{
  color: #0d4a73;
}}

h1, h2, h3 {{
  font-family: "Helvetica Neue", Arial, sans-serif;
}}

.book-shell {{
  max-width: 8.5in;
  margin: 0 auto;
}}

.book-cover,
.book-contents,
.book-page {{
  background: #fffdf8;
  box-shadow: none;
}}

.book-cover {{
  min-height: 9.2in;
  padding: 1.1in 0.9in 0.9in;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  border-bottom: 8px solid #0d4a73;
  break-after: page;
}}

.book-cover-kicker {{
  margin: 0 0 0.35rem;
  color: #536271;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 0.82rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}}

.book-cover h1 {{
  margin: 0;
  font-size: 2.6rem;
  line-height: 1.05;
  color: #102033;
}}

.book-cover p {{
  max-width: 32rem;
  margin: 0.9rem 0 0;
  font-size: 1.05rem;
}}

.book-meta {{
  color: #536271;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 0.95rem;
}}

.book-contents {{
  padding: 0.85in 0.8in 0.9in;
  break-after: page;
}}

.book-contents h1 {{
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 2rem;
  border-bottom: 2px solid #d8d1c2;
  padding-bottom: 0.35rem;
}}

.toc-module {{
  break-inside: avoid-page;
  margin-top: 1.3rem;
}}

.toc-module h2 {{
  margin: 0 0 0.45rem;
  border: none;
  padding: 0;
  font-size: 1.1rem;
  color: #102033;
}}

.toc-module ol {{
  margin: 0;
  padding-left: 1.25rem;
}}

.toc-module li {{
  margin: 0.18rem 0;
}}

.book-page {{
  padding: 0.8in 0.8in 0.9in;
  break-before: page;
}}

.book-page-header {{
  margin-bottom: 1.2rem;
  padding-bottom: 0.7rem;
  border-bottom: 2px solid #d8d1c2;
}}

.chapter-opener .book-page-header {{
  padding-top: 1.4rem;
  border-top: 8px solid #0d4a73;
}}

.book-page-header h1 {{
  margin: 0;
  font-size: 2rem;
  line-height: 1.15;
  border: none;
  padding: 0;
}}

.book-page-reference .book-page-header h1 {{
  font-size: 1.7rem;
}}

.book-module-label {{
  margin: 0 0 0.3rem;
  color: #536271;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 0.8rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}}

.book-page-content > .container-fluid {{
  max-width: none;
  margin: 0;
  padding: 0;
}}

.book-page-content .row {{
  display: block;
}}

.book-page-content [class*="col-"] {{
  width: auto;
  max-width: none;
}}

.book-page-content .offset-sm-1,
.book-page-content .offset-md-1,
.book-page-content .offset-md-2 {{
  margin-left: 0;
}}

.book-page-content h1 {{
  display: none;
}}

.book-page-content h2 {{
  margin-top: 1.8rem;
  break-after: avoid-page;
}}

.book-page-content h3,
.book-page-content table,
.book-page-content pre,
.book-page-content .card,
.book-page-content .alert,
.book-page-content .asidebox {{
  break-inside: avoid-page;
}}

.book-page-content pre {{
  white-space: pre-wrap;
  word-break: break-word;
  overflow-wrap: anywhere;
  max-width: 100%;
}}

.book-page-content code {{
  overflow-wrap: anywhere;
  word-break: break-word;
}}

.book-page-content pre code {{
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  word-break: break-word;
}}

.book-page-content table {{
  table-layout: fixed;
}}

.book-page-content th,
.book-page-content td {{
  overflow-wrap: anywhere;
  word-break: break-word;
}}

.book-page-content img {{
  display: block;
  margin: 0.9rem auto;
}}

.book-page-content figure {{
  margin: 1rem auto;
  text-align: center;
}}

.book-page-content figure img {{
  margin-bottom: 0.4rem;
}}

.book-page-content figcaption {{
  color: #536271;
  font-size: 0.92rem;
}}

.book-page-content .table-responsive {{
  overflow: visible;
}}

.book-page-content .card {{
  margin: 1rem 0;
  border: 1px solid #d8d1c2;
  border-radius: 6px;
  background: #faf8f2;
}}

.book-page-content .card-body {{
  padding: 1rem 1.1rem;
}}

.book-page-content .alert-secondary {{
  background: #f1f5f9;
  border-color: #64748b;
}}

.book-page-content .asidebox {{
  padding: 0.9rem 1rem;
  margin: 1rem 0;
  border-left: 4px solid #64748b;
  background: #f8fafc;
}}

.book-interactive-note {{
  margin: 1rem 0;
  padding: 0.85rem 1rem;
  border-left: 4px solid #b45309;
  background: #fff7ed;
  color: #7c2d12;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 0.95rem;
}}

@media screen {{
  body {{
    padding: 1.5rem 0;
  }}

  .book-cover,
  .book-contents,
  .book-page {{
    margin: 0 auto 1.5rem;
    border: 1px solid #d8d1c2;
  }}
}}
"""


def render_book_html(manifest: dict, records: list[PageRecord]) -> str:
    page_lookup = {record.source_path.resolve(): record.anchor_id for record in records}
    page_sections = [sanitize_page(record, page_lookup) for record in records]
    toc_html = build_toc(manifest, records)
    base_css = STYLE_PATH.read_text(encoding="utf-8")
    inline_styles = gather_inline_styles(records)
    css = build_book_css(base_css, inline_styles)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(manifest['title'])} - Book</title>
  <style>
{css}
  </style>
</head>
<body>
  <main class="book-shell">
    <section class="book-cover">
      <p class="book-cover-kicker">Compiled Course Book</p>
      <h1>{html.escape(manifest['title'])}</h1>
      <p>This PDF compiles the current HTML course modules and reference guides into a single print-oriented book. Interactive D2L activities are replaced with notes where necessary.</p>
      <p class="book-meta">{len(records)} pages compiled from {len(manifest['modules'])} manifest sections<br>{BOOK_DATE}</p>
    </section>
    <section class="book-contents">
      <h1>Contents</h1>
{toc_html}
    </section>
{''.join(page_sections)}
  </main>
</body>
</html>
"""


def find_chrome() -> str | None:
    for candidate in ("google-chrome", "chromium", "chromium-browser"):
        chrome = shutil.which(candidate)
        if chrome:
            return chrome
    return None


def render_pdf(html_path: Path, pdf_path: Path) -> bool:
    chrome = find_chrome()
    if not chrome:
        print("warning: no Chrome/Chromium executable found; wrote HTML only", file=sys.stderr)
        return False

    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--allow-file-access-from-files",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return True


def main() -> int:
    manifest = load_manifest()
    records = build_records(manifest)
    OUTPUT_DIR.mkdir(exist_ok=True)

    html_output = render_book_html(manifest, records)
    BOOK_HTML_PATH.write_text(html_output, encoding="utf-8")

    pdf_built = False
    try:
        pdf_built = render_pdf(BOOK_HTML_PATH, BOOK_PDF_PATH)
    except subprocess.CalledProcessError as exc:
        print("warning: PDF render failed; wrote HTML only", file=sys.stderr)
        if exc.stderr:
            print(exc.stderr.strip(), file=sys.stderr)

    print(f"HTML book: {BOOK_HTML_PATH}")
    if pdf_built:
        print(f"PDF book:  {BOOK_PDF_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
