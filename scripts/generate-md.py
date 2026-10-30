#!/usr/bin/env python3
"""Generate Markdown sidecars + route manifest for SENO avian docs (data.aviantestpro.com).

Runs AFTER `mkdocs build`. Reads the final built HTML in site/, converts each
sitemap-listed (canonical, indexable) page into a Markdown sidecar next to its
index.html, and writes site/_md/manifest.json mapping public URL paths to the
sidecar assets. The Cloudflare Pages middleware (functions/_middleware.js) uses
the manifest to serve Markdown for `Accept: text/markdown` requests.

Exit codes:
  0 - success (non-critical warnings allowed)
  1 - critical failure (missing HTML, missing manifest entries, empty output)
"""
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert

SITE_DIR = Path(__file__).resolve().parent.parent / "site"
MANIFEST_DIR = SITE_DIR / "_md"
MANIFEST_PATH = MANIFEST_DIR / "manifest.json"
SITEMAP_PATH = SITE_DIR / "sitemap.xml"
MIN_MD_BYTES = 400  # below this = suspicious, warn (critical only if empty)

TAG_STRIP = ["script", "style", "link", "meta", "noscript", "form", "button",
             "input", "select", "textarea", "iframe", "svg", "video", "audio",
             "label", "template", "canvas"]

SELECTOR_STRIP = [
    "a.headerlink",            # ¶ permalink anchors
    "img.twemoji",             # emoji SVG images (huge data URIs)
    ".md-source-file",         # "last updated" metadata footer (kept in HTML only)
    ".tabbed-set > .tabbed-labels",
]


def sitemap_urls() -> list[str]:
    if not SITEMAP_PATH.exists():
        raise SystemExit(f"CRITICAL: missing {SITEMAP_PATH}")
    xml = SITEMAP_PATH.read_text(encoding="utf-8")
    urls = re.findall(r"<loc>\s*(.*?)\s*</loc>", xml)
    return [u.strip() for u in urls if u.strip()]


def url_to_html_path(url: str) -> Path:
    path = urllib.parse.urlparse(url).path
    if path in ("", "/"):
        return SITE_DIR / "index.html"
    return SITE_DIR / path.strip("/") / "index.html"


def url_to_md_relpath(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    if path in ("", "/"):
        return "/index.md"
    return "/" + path.strip("/") + "/index.md"


def preprocess(article) -> None:
    for tag in TAG_STRIP:
        for el in article.find_all(tag):
            el.decompose()
    for sel in SELECTOR_STRIP:
        for el in article.select(sel):
            el.decompose()
    # Admonitions -> blockquote with bold title, more readable for AI clients
    for box in article.find_all("div", class_=lambda c: c and "admonition" in c):
        kind = "Note"
        for cls in box.get("class", []):
            if cls in ("note", "warning", "danger", "tip", "info", "success",
                       "question", "example", "quote", "abstract", "bug", "failure"):
                kind = cls.capitalize()
                break
        title_el = box.find(["p", "div"], class_="admonition-title")
        title = title_el.get_text(" ", strip=True) if title_el else kind
        if title_el:
            title_el.decompose()
        body = md_convert(str(box), heading_style="ATX", bullets="-").strip()
        block = f"> **{title}:** " + body.replace("\n", "\n> ")
        quote = BeautifulSoup(f"<blockquote>{block}</blockquote>", "html.parser")
        box.replace_with(quote)


def convert_page(url: str) -> str | None:
    html_path = url_to_html_path(url)
    if not html_path.exists():
        return None
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    article = soup.select_one("article.md-content__inner.md-typeset") or soup.find("article")
    if article is None:
        article = soup.body or soup
    # Strip nav/tools FIRST so the extracted H1 text is clean (no ¶ permalink)
    preprocess(article)
    h1_el = article.find("h1")
    h1 = h1_el.get_text(" ", strip=True) if h1_el else None
    desc_el = soup.find("meta", attrs={"name": "description"})
    meta_desc = desc_el["content"].strip() if desc_el and desc_el.get("content") else None
    # prettify() gives markdownify proper newlines (minified HTML collapses lists)
    body = md_convert(article.prettify(), heading_style="ATX", bullets="-")
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    if h1:
        first_line = body.split("\n", 1)[0].lstrip("#").strip()
        if first_line != h1:
            body = f"# {h1}\n\n{body}"
    if meta_desc and meta_desc != h1 and meta_desc not in body:
        lines = body.split("\n", 1)
        body = lines[0] + "\n\n> " + meta_desc + "\n\n" + (lines[1] if len(lines) > 1 else "")
    return body + "\n"


def main() -> int:
    urls = sitemap_urls()
    if not urls:
        print("CRITICAL: sitemap.xml contains no URLs")
        return 1

    manifest: dict[str, str] = {}
    warnings = 0
    failures = 0
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)

    for url in urls:
        md_rel = url_to_md_relpath(url)
        md_path = SITE_DIR / md_rel.lstrip("/")
        md = convert_page(url)
        if md is None:
            print(f"CRITICAL: no HTML for {url}")
            failures += 1
            continue
        if not md.strip():
            print(f"CRITICAL: empty Markdown for {url}")
            failures += 1
            continue
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(md, encoding="utf-8")
        if len(md.encode("utf-8")) < MIN_MD_BYTES:
            print(f"WARN: short Markdown ({len(md.encode('utf-8'))}B) for {url}")
            warnings += 1
        path = urllib.parse.urlparse(url).path or "/"
        manifest[path] = md_rel

    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # Integrity: every manifest entry must point at an existing file
    for path, md_rel in manifest.items():
        if not (SITE_DIR / md_rel.lstrip("/")).exists():
            print(f"CRITICAL: manifest entry missing on disk: {path} -> {md_rel}")
            failures += 1

    print(f"pages={len(urls)} generated={len(manifest)} warnings={warnings} failures={failures}")
    print(f"manifest: {MANIFEST_PATH.relative_to(SITE_DIR.parent)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
