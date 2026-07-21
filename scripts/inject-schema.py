#!/usr/bin/env python3
"""Inject Schema.org JSON-LD into built HTML files for SENO avian docs."""
import json, os, re

SITE_DIR = os.path.join(os.path.dirname(__file__), '..', 'site')
SITE_URL = 'https://docs.aviantestpro.com'
ORG_NAME = 'Zhangjiakou SENO Testing Center Co., Ltd.'

ORGANIZATION_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": f"{SITE_URL}/#organization",
    "name": ORG_NAME,
    "alternateName": "SENO International Avian Genetic Test",
    "url": SITE_URL,
    "sameAs": ["https://aviantestpro.com"],
    "description": "Professional avian genetic testing laboratory specializing in bird DNA sexing, avian disease PCR detection, and racing pigeon genetic analysis.",
    "contactPoint": {
        "@type": "ContactPoint",
        "email": "lab@aviantestpro.com",
        "telephone": "+86-13323237275",
        "contactType": "laboratory services"
    }
}

WEBSITE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": f"{SITE_URL}/#website",
    "url": SITE_URL,
    "name": "SENO Avian Genetic Test — Technical Documentation Center",
    "description": "Technical documentation for SENO International Avian Genetic Test.",
    "publisher": {"@id": f"{SITE_URL}/#organization"}
}

for root, dirs, files in os.walk(SITE_DIR):
    for fname in files:
        if fname.endswith('.html') and fname != '404.html':
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                html = f.read()
            if 'application/ld+json' in html:
                continue
            schema_block = (
                f'<script type="application/ld+json">{json.dumps(ORGANIZATION_SCHEMA, indent=2)}</script>\n'
                f'<script type="application/ld+json">{json.dumps(WEBSITE_SCHEMA, indent=2)}</script>\n'
            )
            html = html.replace('</head>', f'{schema_block}</head>')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
    print(f"Schema injection complete. Processed {len(files)} files in {root}")
