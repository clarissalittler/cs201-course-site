#!/usr/bin/env python3
"""
Minimal dev server for CS 201 course content.

Serves module HTML files with:
- Local CSS injected (replaces broken D2L template refs)
- Prev/Next navigation bar for flipping through pages
- Keyboard shortcuts: Left/Right arrow keys to navigate

Usage: python3 serve.py [port]   (default: 8201)
"""

import http.server
import json
import os
import re
import sys
import urllib.parse

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8201
ROOT = os.path.dirname(os.path.abspath(__file__))


def load_manifest():
    with open(os.path.join(ROOT, "manifest.json")) as f:
        return json.load(f)


def build_page_list(manifest):
    """Return flat ordered list of (url_path, title, module_title)."""
    pages = []
    for mod in manifest["modules"]:
        for page in mod["pages"]:
            # Use unquoted paths for internal lookups; quote only for HTML hrefs
            url = f"/{mod['id']}/{page['file']}"
            pages.append((url, page["title"], mod["title"]))
    return pages


MANIFEST = load_manifest()
PAGES = build_page_list(MANIFEST)
# Map url_path -> (index, title, module_title)
PAGE_INDEX = {url: (i, title, mtitle) for i, (url, title, mtitle) in enumerate(PAGES)}

# CSS/JS refs from D2L that we want to strip (link tags + script with src)
D2L_ASSET_RE = re.compile(
    r'<link[^>]*href=["\'][^"\']*(?:/shared/|/d2l/)[^"\']*["\'][^>]*/?>',
    re.IGNORECASE,
)

# Strip all <script ...src="...">...</script> blocks that reference external/D2L resources
SCRIPT_STRIP_RE = re.compile(
    r'<script[^>]*src=["\'][^"\']*["\'][^>]*>[\s\S]*?</script>',
    re.IGNORECASE,
)


def make_nav_html(url_path):
    """Build the sticky nav bar for a given page."""
    info = PAGE_INDEX.get(url_path)
    if info is None:
        return ""
    idx, title, module_title = info

    prev_link = ""
    next_link = ""
    if idx > 0:
        prev_url, prev_title, _ = PAGES[idx - 1]
        prev_href = urllib.parse.quote(prev_url)
        prev_link = f'<a href="{prev_href}" id="nav-prev-link">&larr; {prev_title}</a>'
    if idx < len(PAGES) - 1:
        next_url, next_title, _ = PAGES[idx + 1]
        next_href = urllib.parse.quote(next_url)
        next_link = f'<a href="{next_href}" id="nav-next-link">{next_title} &rarr;</a>'

    return f"""<div id="cs201-nav">
  <span class="nav-prev">{prev_link}</span>
  <span class="nav-center"><a href="/">{module_title}</a></span>
  <span class="nav-next">{next_link}</span>
</div>
<script>
document.addEventListener('keydown', function(e) {{
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  if (e.key === 'ArrowLeft') {{
    var prev = document.getElementById('nav-prev-link');
    if (prev) window.location = prev.href;
  }} else if (e.key === 'ArrowRight') {{
    var next = document.getElementById('nav-next-link');
    if (next) window.location = next.href;
  }}
}});
</script>"""


def transform_html(content, url_path):
    """Inject local CSS and nav into a module HTML page."""
    # Strip D2L asset references and external scripts
    content = D2L_ASSET_RE.sub("", content)
    content = SCRIPT_STRIP_RE.sub("", content)

    # Compute relative path to root for CSS
    depth = url_path.strip("/").count("/")
    css_prefix = "../" * depth
    css_link = f'<link rel="stylesheet" href="{css_prefix}style.css">'

    # Inject CSS right after <head> or at the start
    if "<head>" in content:
        content = content.replace("<head>", f"<head>\n{css_link}", 1)
    elif "<head " in content.lower():
        content = re.sub(
            r"(<head[^>]*>)", rf"\1\n{css_link}", content, count=1, flags=re.I
        )
    else:
        content = css_link + "\n" + content

    # Inject nav after <body> tag
    nav = make_nav_html(url_path)
    if nav:
        if re.search(r"<body[^>]*>", content, re.I):
            content = re.sub(
                r"(<body[^>]*>)", rf"\1\n{nav}", content, count=1, flags=re.I
            )

    return content


class CS201Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        # Parse path
        path = urllib.parse.unquote(urllib.parse.urlparse(self.path).path)

        # Serve index at root
        if path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(generate_index().encode("utf-8"))
            return

        # Check if this is a module HTML file
        file_path = os.path.join(ROOT, path.lstrip("/"))
        if (
            path.startswith("/module-")
            and path.endswith(".html")
            and os.path.isfile(file_path)
        ):
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            content = transform_html(content, path)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
            return

        # Everything else: static files
        super().do_GET()

    def log_message(self, format, *args):
        # Quieter logging
        if args and "404" not in str(args[1] if len(args) > 1 else ""):
            return
        super().log_message(format, *args)


def generate_index():
    """Generate the main index page from the manifest."""
    modules_html = []
    for mod in MANIFEST["modules"]:
        links = []
        for page in mod["pages"]:
            href = urllib.parse.quote(f"/{mod['id']}/{page['file']}")
            links.append(f'        <li><a href="{href}">{page["title"]}</a></li>')
        first_url = urllib.parse.quote(f"/{mod['id']}/{mod['pages'][0]['file']}")
        modules_html.append(
            f'    <section class="module">\n'
            f'      <h2><a href="{first_url}">{mod["title"]}</a></h2>\n'
            f"      <ul>\n" + "\n".join(links) + "\n      </ul>\n"
            f"    </section>"
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{MANIFEST['title']}</title>
  <link rel="stylesheet" href="/style.css">
  <style>
    body {{ padding: 2rem 1.5rem; }}
    h1 {{ margin-bottom: 0.3rem; }}
    .subtitle {{ color: var(--muted); margin-bottom: 2rem; }}
    .module {{ margin-bottom: 1.5rem; }}
    .module h2 {{ font-size: 1.2rem; border: none; padding: 0; margin-bottom: 0.4rem; }}
    .module h2 a {{ color: var(--fg); }}
    .module h2 a:hover {{ color: var(--accent); }}
    .module ul {{ list-style: none; padding: 0; }}
    .module li {{ padding: 0.2rem 0; }}
    .module li::before {{ content: "\\2022"; color: var(--muted); margin-right: 0.5rem; }}
    .hint {{ color: var(--muted); font-size: 0.85rem; margin-top: 2rem; }}
    kbd {{ background: var(--code-bg); border: 1px solid var(--border); border-radius: 3px; padding: 0.1em 0.4em; font-size: 0.85em; }}
  </style>
</head>
<body>
  <div class="container-fluid">
    <h1>{MANIFEST['title']}</h1>
    <p class="subtitle">Course content — {len(MANIFEST['modules'])} modules</p>
{chr(10).join(modules_html)}
    <p class="hint">Use <kbd>&larr;</kbd> <kbd>&rarr;</kbd> arrow keys to flip between pages.</p>
  </div>
</body>
</html>"""


if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), CS201Handler) as httpd:
        print(f"Serving CS 201 at http://localhost:{PORT}")
        print(f"  {len(PAGES)} pages across {len(MANIFEST['modules'])} modules")
        print(f"  Arrow keys navigate between pages")
        print(f"  Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")
