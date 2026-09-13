# CS 201 working draft course site

Public draft: **https://clarissalittler.github.io/cs201-course-site/**

The site publishes the current lessons in `manifest.json`, with a contents page,
previous/next navigation, a working-draft notice, and downloadable course books.
Brightspace remains the source for official assignments, quizzes, and due dates.
Brightspace-only embeds become notices in this public version. External media may
still require a course login.

## Publish updates

Push changes to `main`. The **Publish draft course site** GitHub Actions workflow
builds and validates the static output, then deploys it through GitHub Pages.
The workflow can also be run manually from the repository's Actions tab.
Pages uses **GitHub Actions** as its publishing source.

## Preview locally

```sh
python3 -m venv /tmp/cs201-site-env
/tmp/cs201-site-env/bin/pip install -r requirements-site.txt
/tmp/cs201-site-env/bin/python build_site.py
python3 -m http.server 8201 --directory _site
```

Open http://localhost:8201/ . The `_site` directory is generated and ignored by
Git. The exporter uses relative URLs so the same output works under GitHub's
`/cs201-course-site/` project path. It fails on missing local links or assets.

Edit lesson HTML and `manifest.json`, rather than `_site`. The exporter publishes
only current module pages/assets and the books in `dist`; it excludes the archived
modules, source scripts, audit reports, and `practice-problems.md` answer bank.
The repository itself remains public.

The Pages build copies the existing PDF and EPUB. When lessons change, regenerate
and commit the books with `build_book.py` and `build_epub.py` before publishing
if those downloads should include the edits. Those scripts have additional
requirements (Beautiful Soup, Chrome for PDF, and Pandoc for EPUB).

## Preserved original

`codex/original-course-site-2026-09-13` preserves the original course site.
The reorganized and fact-checked version is on `main`; the September 8 audit is in
`course-review-2026-09-08.md`.
