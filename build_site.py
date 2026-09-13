#!/usr/bin/env python3
"""Export the current manifest as a static, project-path-safe working draft.

Run `python3 build_site.py`, then serve `_site` with any static web server.
Only current lessons, their assets, and the compiled books are published.
"""
from pathlib import Path
import posixpath
import shutil
from urllib.parse import quote, unquote, urlsplit, urlunsplit

from bs4 import BeautifulSoup
import serve

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / '_site'


def relative_url(value, page):
    """Convert site-root URLs to relative URLs, retaining queries/fragments."""
    parts = urlsplit(value)
    if parts.scheme or parts.netloc or not parts.path.startswith('/'):
        return value
    target = unquote(parts.path).lstrip('/') or 'index.html'
    path = posixpath.relpath(target, posixpath.dirname(page) or '.')
    return urlunsplit(('', '', quote(path), parts.query, parts.fragment))


def render(content, page):
    soup = BeautifulSoup(content, 'html.parser')
    soup.head.append(soup.new_tag('meta', attrs={'name': 'robots', 'content': 'noindex'}))
    soup.title.string = soup.title.get_text() + ' — Working draft'
    banner = soup.new_tag('aside', attrs={'class': 'draft-notice', 'aria-label': 'Site status'})
    label = soup.new_tag('strong')
    label.string = 'Working draft'
    banner.append(label)
    banner.append(' · CS 201 course materials under revision. Use Brightspace for official assignments, quizzes, and due dates.')
    soup.body.insert(0, banner)
    for tag in list(soup.select('[href], [src]')):
        for attr in ('href', 'src'):
            value = tag.get(attr)
            if value is None:
                continue
            if urlsplit(value).path.startswith(('/d2l/', '/shared/')):
                notice = soup.new_tag('span', attrs={'class': 'lms-notice'})
                notice.string = 'This activity or resource is available in the course on Brightspace.'
                if tag.name == 'a':
                    notice.string = tag.get_text(' ', strip=True) + ' — available in Brightspace.'
                tag.replace_with(notice)
                break
            tag[attr] = relative_url(value, page)
    # Keep wide content usable on phones without changing the teaching source.
    css = soup.new_tag('link', rel='stylesheet', href=relative_url('/draft.css', page))
    soup.head.append(css)
    return str(soup)


def validate():
    """Catch paths that would break under /cs201-course-site/ on Pages."""
    count = 0
    for page in OUTPUT.rglob('*.html'):
        soup = BeautifulSoup(page.read_text(), 'html.parser')
        for tag in soup.select('[href], [src]'):
            for attr in ('href', 'src'):
                value = tag.get(attr)
                if not value:
                    continue
                parts = urlsplit(value)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                assert not parts.path.startswith('/'), (page, value)
                target = (page.parent / unquote(parts.path)).resolve()
                assert target.is_relative_to(OUTPUT.resolve()), (page, value)
                assert target.exists(), (page, value)
        count += 1
    return count


def main():
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    shutil.copy2(ROOT / 'style.css', OUTPUT / 'style.css')
    shutil.copy2(ROOT / 'draft.css', OUTPUT / 'draft.css')
    (OUTPUT / '.nojekyll').touch()
    for mod in serve.MANIFEST['modules']:
        source = ROOT / mod['id']
        for asset in source.rglob('*'):
            if asset.is_file() and asset.suffix.lower() != '.html':
                destination = OUTPUT / asset.relative_to(ROOT)
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(asset, destination)
        for record in mod['pages']:
            page = f"{mod['id']}/{record['file']}"
            content = serve.transform_html((ROOT / page).read_text(), '/' + page)
            destination = OUTPUT / page
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(render(content, page))
    index = serve.generate_index().replace(
        '<p class="subtitle">Course content', '<p class="subtitle">Draft course content')
    index = index.replace('11 modules</p>', '10 modules + reference guides</p>')
    index = index.replace('<p class="hint">', '''<section class="module">
<h2>Read offline</h2>
<p>Download the current draft book as <a href="dist/cs201-course-book.pdf">PDF</a>
 or <a href="dist/cs201-course-book.epub">EPUB</a>,
 or <a href="dist/cs201-course-book.html">read the combined HTML book</a>.</p>
</section><p class="hint">''')
    (OUTPUT / 'index.html').write_text(render(index, 'index.html'))
    (OUTPUT / 'dist').mkdir()
    for name in ('cs201-course-book.pdf', 'cs201-course-book.epub'):
        shutil.copy2(ROOT / 'dist' / name, OUTPUT / 'dist' / name)
    book = (ROOT / 'dist/cs201-course-book.html').read_text()
    (OUTPUT / 'dist/cs201-course-book.html').write_text(render(book, 'dist/cs201-course-book.html'))
    print(f'Built and validated {validate()} HTML pages in {OUTPUT}')


if __name__ == '__main__':
    main()
