#!/usr/bin/env python3
"""
Build a standalone EPUB course book from the current CS 201 module pages.

Reuses the sanitization pipeline in build_book.py (script/nav/banner/practice
stripping, image and link rewriting), then restructures the heading hierarchy so
the e-reader navigation nests as Module -> Lesson -> Section, embeds a generated
cover, and calls pandoc to produce a reflowable EPUB 3.

Usage: python3 build_epub.py
Requires: pandoc on PATH. Cover generation additionally uses Pillow (optional).
"""

from __future__ import annotations

import html
import shutil
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup

import build_book as bb

ROOT = Path(__file__).parent.resolve()
OUTPUT_DIR = ROOT / "dist"
EPUB_PATH = OUTPUT_DIR / "cs201-course-book.epub"
SOURCE_PATH = OUTPUT_DIR / "_epub_source.html"
COVER_PATH = OUTPUT_DIR / "_epub_cover.png"
CSS_PATH = OUTPUT_DIR / "_epub_style.css"

# EPUB metadata — adjust author/publisher/rights to taste.
BOOK_TITLE = "CS 201: Computer Systems"
BOOK_AUTHOR = "Clarissa Littler"
BOOK_PUBLISHER = "Portland Community College"
BOOK_LANG = "en-US"
BOOK_DATE = "2026-09-08"
BOOK_RIGHTS = "© 2026 Portland Community College. Course materials for CS 201."
BOOK_DESCRIPTION = (
    "A compiled, offline-readable edition of the CS 201 Computer Systems course: "
    "C and integer/floating-point representation, x86-64 assembly, processes and "
    "signals, threads, file I/O and sockets, the memory hierarchy, virtual memory "
    "and linking, and kernel organization, plus quick-reference guides."
)


def demote_headings(content: BeautifulSoup) -> None:
    """Shift in-content headings down one level (h3->h4, h2->h3) so the page
    title can sit at h2 and the module at h1. Content only reaches h3, so the
    deepest result is h4 — safely within h1..h6."""
    for level in (3, 2):  # high-to-low so a tag is never bumped twice
        for tag in content.find_all(f"h{level}"):
            tag.name = f"h{level + 1}"


def render_page_section(record: bb.PageRecord, page_lookup: dict[Path, str]) -> str:
    """Sanitize a page with build_book's pipeline, then adapt it for EPUB.

    The book-page section/header wrappers keep pandoc from treating the lesson
    title as a native heading (so it never reaches the nav), so we flatten each
    page to a bare <h2> carrying the page's anchor id — preserving cross-page
    links — followed by its content with headings demoted one level."""
    raw = bb.sanitize_page(record, page_lookup)
    soup = BeautifulSoup(raw, "html.parser")

    content = soup.select_one(".book-page-content")
    if content is not None:
        demote_headings(content)

        # Resolve image sources to absolute filesystem paths so pandoc embeds
        # them regardless of its working directory (sanitize_page made them
        # relative to dist/).
        for img in content.find_all("img"):
            src = img.get("src", "")
            if not src or bb.is_external_url(src) or src.startswith("#"):
                continue
            candidate = (OUTPUT_DIR / src).resolve()
            if candidate.exists():
                img["src"] = str(candidate)

        content_inner = "".join(str(child) for child in content.contents)
    else:
        content_inner = ""

    title = html.escape(record.page_title)
    return f'<h2 id="{record.anchor_id}">{title}</h2>\n{content_inner}'


def build_source_html(manifest: dict, records: list[bb.PageRecord]) -> str:
    page_lookup = {r.source_path.resolve(): r.anchor_id for r in records}

    body_parts: list[str] = []
    seen_modules: set[str] = set()
    module_titles = {m["id"]: m["title"] for m in manifest["modules"]}

    for record in records:
        if record.module_id not in seen_modules:
            seen_modules.add(record.module_id)
            module_slug = bb.slugify(record.module_id)
            body_parts.append(
                f'<h1 id="mod-{module_slug}" class="epub-module-title">'
                f'{html.escape(module_titles[record.module_id])}</h1>'
            )
        body_parts.append(render_page_section(record, page_lookup))

    body = "\n".join(body_parts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{html.escape(BOOK_TITLE)}</title>
</head>
<body>
{body}
</body>
</html>
"""


def build_epub_css() -> str:
    inline_styles = bb.gather_inline_styles(bb.build_records(bb.load_manifest()))
    inline_css = "\n\n".join(inline_styles)
    return f"""/* Reading-oriented stylesheet for the EPUB edition. */
body {{
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.6;
}}
h1, h2, h3, h4 {{
  font-family: "Helvetica Neue", Arial, sans-serif;
  line-height: 1.2;
}}
h1.epub-module-title {{
  page-break-before: always;
  border-bottom: 3px solid #0d4a73;
  padding-bottom: 0.3em;
  color: #102033;
}}
.book-page-header {{
  margin-top: 1.4em;
  border-bottom: 1px solid #ccc;
}}
.book-module-label {{
  color: #536271;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 0.8em;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 0.2em;
}}
pre {{
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow-wrap: anywhere;
  background: #f4f4f4;
  padding: 0.6em 0.8em;
  border-radius: 4px;
  font-family: "DejaVu Sans Mono", "Courier New", monospace;
  font-size: 0.85em;
}}
code {{
  font-family: "DejaVu Sans Mono", "Courier New", monospace;
  overflow-wrap: anywhere;
}}
table {{
  border-collapse: collapse;
  margin: 1em 0;
}}
th, td {{
  border: 1px solid #bbb;
  padding: 0.35em 0.6em;
  text-align: left;
}}
img {{
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1em auto;
}}
.alert, .asidebox, .card {{
  border-left: 4px solid #64748b;
  background: #f1f5f9;
  padding: 0.7em 1em;
  margin: 1em 0;
}}
.book-interactive-note {{
  border-left: 4px solid #b45309;
  background: #fff7ed;
  color: #7c2d12;
  padding: 0.7em 1em;
  margin: 1em 0;
  font-size: 0.95em;
}}

/* Author-supplied inline styles carried over from the source pages. */
{inline_css}
"""


def generate_cover(path: Path) -> bool:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("note: Pillow not available; building EPUB without a cover image",
              file=sys.stderr)
        return False

    W, H = 1600, 2400
    bg = (16, 32, 51)       # deep navy
    accent = (13, 74, 115)  # book spine blue
    cream = (244, 241, 232)
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, 90, H], fill=accent)
    draw.rectangle([120, 300, W - 120, 316], fill=accent)
    draw.rectangle([120, H - 360, W - 120, H - 344], fill=accent)

    def font(size, bold=True):
        name = "DejaVuSerif-Bold.ttf" if bold else "DejaVuSerif.ttf"
        for base in ("/usr/share/fonts/truetype/dejavu/",):
            p = Path(base) / name
            if p.exists():
                return ImageFont.truetype(str(p), size)
        return ImageFont.load_default()

    mono = None
    monop = Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")
    if monop.exists():
        mono = ImageFont.truetype(str(monop), 60)

    draw.text((120, 200), "COMPILED COURSE BOOK", font=font(46), fill=(120, 150, 180))
    draw.text((120, 430), "CS 201", font=font(240), fill=cream)
    draw.text((120, 720), "Computer", font=font(150), fill=cream)
    draw.text((120, 890), "Systems", font=font(150), fill=cream)

    if mono is not None:
        snippet = [
            "int main(void) {",
            "    return 0xCA5;",
            "}",
        ]
        y = 1250
        for line in snippet:
            draw.text((140, y), line, font=mono, fill=(120, 150, 180))
            y += 90

    draw.text((120, H - 320), BOOK_AUTHOR, font=font(58), fill=cream)
    draw.text((120, H - 240), BOOK_PUBLISHER, font=font(46, bold=False),
              fill=(150, 170, 190))

    img.save(path, "PNG")
    return True


def build_metadata_args() -> list[str]:
    meta = {
        "title": BOOK_TITLE,
        "creator": BOOK_AUTHOR,
        "publisher": BOOK_PUBLISHER,
        "lang": BOOK_LANG,
        "date": BOOK_DATE,
        "rights": BOOK_RIGHTS,
        "description": BOOK_DESCRIPTION,
    }
    args: list[str] = []
    for key, value in meta.items():
        args += ["--metadata", f"{key}={value}"]
    return args


def main() -> int:
    if not shutil.which("pandoc"):
        print("error: pandoc not found on PATH", file=sys.stderr)
        return 1

    manifest = bb.load_manifest()
    records = bb.build_records(manifest)
    OUTPUT_DIR.mkdir(exist_ok=True)

    SOURCE_PATH.write_text(build_source_html(manifest, records), encoding="utf-8")
    CSS_PATH.write_text(build_epub_css(), encoding="utf-8")
    has_cover = generate_cover(COVER_PATH)

    cmd = [
        "pandoc",
        str(SOURCE_PATH),
        "-f", "html",
        "-t", "epub3",
        "-o", str(EPUB_PATH),
        "--toc",
        "--toc-depth=2",
        "--split-level=1",
        "--css", str(CSS_PATH),
    ]
    cmd += build_metadata_args()
    if has_cover:
        cmd += ["--epub-cover-image", str(COVER_PATH)]

    subprocess.run(cmd, check=True)

    # Tidy intermediates; keep only the .epub.
    for tmp in (SOURCE_PATH, CSS_PATH, COVER_PATH):
        tmp.unlink(missing_ok=True)

    size_kb = EPUB_PATH.stat().st_size / 1024
    print(f"EPUB book: {EPUB_PATH} ({size_kb:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
