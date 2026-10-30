"""MkDocs post-build hook: generate Markdown sidecars + route manifest.

Runs scripts/generate-md.py after every `mkdocs build`, so the Markdown
negotiation assets (site/*/index.md + site/_md/manifest.json) are always
fresh in the deployed output. Wired via mkdocs.yml `hooks:`.

Note: the previous draft of this file wrote a catch-all `/* /index.html 200`
_redirects file. That logic is intentionally NOT wired: Cloudflare Pages'
native directory-index serving handles MkDocs URLs correctly (verified live),
and the catch-all would rewrite every URL to the homepage.
"""
import subprocess
import sys
from pathlib import Path


def on_post_build(config, **kwargs):
    script = Path(__file__).resolve().parent / "scripts" / "generate-md.py"
    subprocess.run([sys.executable, str(script)], check=True)
    return config
