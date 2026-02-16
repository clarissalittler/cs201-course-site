#!/usr/bin/env python3
"""
Mechanical cleanup of CS 201 course HTML files exported from D2L.

Fixes applied:
1.  Remove empty elements: <pre></pre>, <pre>&nbsp;</pre>, <ol></ol>,
    <p></p>, <h2></h2>, empty alert divs, empty asidebox divs, <p><b></b></p>
2.  Fix double-encoded HTML entities in code blocks:
    &amp;amp; → &amp;  |  &amp;gt; → &gt;  |  &amp;lt; → &lt;  |  &amp;nbsp; → &nbsp;
3.  Fix wrong <title> tags (derive from <h1> content)
4.  Fix "Week N" → "Module N" in footers
5.  Fix "LessonN:" → "Lesson N:" footer spacing
6.  Remove data-d2l-editor-default-img-style attribute
7.  Remove Brightspace font CSS links
8.  Rewrite D2L /content/enforced/ image paths to relative img/ paths
9.  Remove stray escaped closing tags in code blocks (</stdio.h> etc.)
10. Remove duplicate "[link opens in new tab]" text
11. Fix "Affect" → "Effect" column headers in assembly tables
12. Fix "Lesson2:" → "Lesson 2:" (missing space variants)
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CHANGES = []  # log of (file, description) tuples


def log(filepath, desc):
    CHANGES.append((str(filepath), desc))


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        original = f.read()

    content = original

    # --- 1. Remove empty elements ---

    # Empty <pre></pre> and <pre>&nbsp;</pre>
    for pat in [r"<pre></pre>\n?", r"<pre>&nbsp;</pre>\n?", r"<pre> </pre>\n?"]:
        new = re.sub(pat, "", content)
        if new != content:
            log(filepath, f"Removed empty <pre> elements")
            content = new

    # Empty <ol></ol>
    new = re.sub(r"<ol></ol>\n?", "", content)
    if new != content:
        log(filepath, "Removed empty <ol></ol>")
        content = new

    # Empty <p></p>
    new = re.sub(r"<p></p>\n?", "", content)
    if new != content:
        log(filepath, "Removed empty <p></p>")
        content = new

    # Empty <h2></h2>
    new = re.sub(r"<h2></h2>\n?", "", content)
    if new != content:
        log(filepath, "Removed empty <h2></h2>")
        content = new

    # Empty alert divs
    new = re.sub(r'<div class="alert alert-secondary"></div>\n?', "", content)
    if new != content:
        log(filepath, "Removed empty alert divs")
        content = new

    # Empty asidebox divs
    new = re.sub(r'<div class="asidebox"></div>\n?', "", content)
    if new != content:
        log(filepath, "Removed empty asidebox div")
        content = new

    # Empty <p><b></b></p>
    new = re.sub(r"<p><b></b></p>\n?", "", content)
    if new != content:
        log(filepath, "Removed empty <p><b></b></p>")
        content = new

    # --- 2. Fix double-encoded HTML entities ---

    double_encoded = [
        ("&amp;amp;", "&amp;"),
        ("&amp;gt;", "&gt;"),
        ("&amp;lt;", "&lt;"),
        ("&amp;nbsp;", "&nbsp;"),
    ]
    for old, new_val in double_encoded:
        if old in content:
            log(filepath, f"Fixed double-encoded entity: {old} → {new_val}")
            content = content.replace(old, new_val)

    # --- 3. Fix wrong <title> tags by deriving from <h1> ---

    title_match = re.search(r"<title>(.*?)</title>", content)
    h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.DOTALL)
    if title_match and h1_match:
        current_title = title_match.group(1).strip()
        h1_text = re.sub(r"<[^>]+>", "", h1_match.group(1)).strip()

        # Fix known-bad generic titles
        bad_titles = ["PCC D2L", "Lesson 3: Signed Integer Encoding"]
        # Also fix "Week Overview" / "Weekly Overview" → use h1
        if current_title in bad_titles or current_title.startswith("Week"):
            new = content.replace(
                f"<title>{current_title}</title>",
                f"<title>{h1_text}</title>",
            )
            if new != content:
                log(filepath, f"Fixed <title>: '{current_title}' → '{h1_text}'")
                content = new

        # Fix title/h1 minor mismatches (missing words etc.)
        elif current_title == "Summary" and "Module" in h1_text:
            new = content.replace(
                f"<title>{current_title}</title>",
                f"<title>{h1_text}</title>",
            )
            if new != content:
                log(filepath, f"Fixed <title>: '{current_title}' → '{h1_text}'")
                content = new

    # --- 4. Fix "Week N" → "Module N" in footers ---

    new = re.sub(
        r"End of Week (\d+)",
        r"End of Module \1",
        content,
    )
    if new != content:
        log(filepath, "Fixed 'Week N' → 'Module N' in footer")
        content = new

    # --- 5. Fix "LessonN:" spacing in footers ---

    new = re.sub(r"Lesson(\d+):", r"Lesson \1:", content)
    if new != content:
        log(filepath, "Fixed 'LessonN:' → 'Lesson N:' spacing")
        content = new

    # Also fix "Lesson2:" etc. without space
    new = re.sub(r"End of Lesson(\d)", r"End of Lesson \1", content)
    if new != content:
        log(filepath, "Fixed footer lesson spacing")
        content = new

    # --- 6. Remove D2L editor attributes ---

    new = re.sub(r'\s*data-d2l-editor-default-img-style="true"', "", content)
    if new != content:
        log(filepath, "Removed data-d2l-editor-default-img-style attributes")
        content = new

    # --- 7. Remove Brightspace font CSS ---

    new = re.sub(
        r'<link[^>]*href="https://s\.brightspace\.com[^"]*"[^>]*/?>',
        "",
        content,
    )
    if new != content:
        log(filepath, "Removed Brightspace font CSS link")
        content = new

    # --- 8. Rewrite D2L /content/enforced/ image paths to relative ---

    def rewrite_img_path(m):
        full = m.group(0)
        # Extract just the filename from the D2L path
        path_match = re.search(
            r'/content/enforced/[^"]*/(img/[^"]+)', full
        )
        if path_match:
            relative = path_match.group(1)
            result = full.replace(m.group(1), relative)
            log(filepath, f"Rewrote image path to relative: {relative}")
            return result
        return full

    new = re.sub(
        r'(<img[^>]*src=")(/content/enforced/[^"]+)(")',
        lambda m: m.group(1) + re.search(r"img/[^\"]+", m.group(2)).group() + m.group(3)
        if re.search(r"img/[^\"]+", m.group(2))
        else m.group(0),
        content,
    )
    if new != content:
        # Count how many were rewritten
        count = content.count("/content/enforced/") - new.count("/content/enforced/")
        log(filepath, f"Rewrote {count} D2L image path(s) to relative")
        content = new

    # --- 9. Remove stray escaped closing tags in code blocks ---

    # These appear as &lt;/stdio.h&gt; &lt;/stdlib.h&gt; etc. at end of code blocks
    stray_tags = [
        r"&lt;/stdio\.h&gt;",
        r"&lt;/stdlib\.h&gt;",
        r"&lt;/unistd\.h&gt;",
        r"&lt;/sys&gt;",
    ]
    for tag_pat in stray_tags:
        new = re.sub(tag_pat, "", content)
        if new != content:
            log(filepath, f"Removed stray closing tag: {tag_pat}")
            content = new

    # Clean up leftover whitespace from removed stray tags
    # Pattern: } followed by whitespace then </code> (where the stray tags were between them)
    new = re.sub(r"}\s{2,}(</code>)", r"}\n\1", content)
    if new != content:
        content = new

    # --- 10. Remove duplicate "[link opens in new tab]" ---

    new = re.sub(
        r"\[link opens in new tab\](</a>)\s*\[link opens in new tab\]",
        r"\1",
        content,
    )
    if new != content:
        log(filepath, "Removed duplicate '[link opens in new tab]' text")
        content = new

    # --- 11. Fix "Affect" → "Effect" in table headers ---

    new = re.sub(r"<th>Affect</th>", "<th>Effect</th>", content)
    if new != content:
        log(filepath, "Fixed 'Affect' → 'Effect' table header")
        content = new

    # --- Write back if changed ---

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    total_files = 0
    changed_files = 0

    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Skip hidden dirs and non-module dirs
        dirnames[:] = [d for d in dirnames if d.startswith("module-")]
        for fname in filenames:
            if not fname.endswith(".html"):
                continue
            filepath = os.path.join(dirpath, fname)
            total_files += 1
            if fix_file(filepath):
                changed_files += 1

    # Summary
    print(f"\nProcessed {total_files} HTML files, modified {changed_files}")
    print(f"Total fixes applied: {len(CHANGES)}\n")

    # Group changes by file
    from collections import defaultdict

    by_file = defaultdict(list)
    for fpath, desc in CHANGES:
        short = os.path.relpath(fpath, ROOT)
        by_file[short].append(desc)

    for fpath in sorted(by_file):
        print(f"  {fpath}:")
        for desc in by_file[fpath]:
            print(f"    - {desc}")
        print()


if __name__ == "__main__":
    main()
