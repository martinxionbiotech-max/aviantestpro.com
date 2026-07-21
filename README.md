# SENO Avian Genetic Test — Technical Documentation Center

Technical documentation for Zhangjiakou SENO Testing Center Co., Ltd. — a professional avian genetic testing laboratory.

**Main Website:** [aviantestpro.com](https://aviantestpro.com)  
**Target Deploy:** `docs.aviantestpro.com`  

## Project Structure

```
avian-docs/
├── docs/
│   ├── index.md                 # Homepage (entity-driven)
│   ├── INDEX.md                 # Full document index
│   ├── robots.txt               # AI crawler policy
│   ├── llms.txt                 # AI context map
│   ├── about/                   # Facility, team, certifications, IP
│   ├── gender-testing/          # DNA sexing methodology & species
│   ├── disease-testing/         # PBFD, APV, pigeon panel, AIV
│   ├── pigeon-genetics/         # Performance genes, fingerprinting, parentage
│   ├── sample-guide/            # Collection protocols & international shipping
│   ├── testing-methods/         # PCR, qPCR, capillary electrophoresis
│   ├── quality-control/         # Lab QC, proficiency testing, validation
│   ├── regulatory/              # ISO 9001, ISO 13485, shipping regulations
│   ├── species-guides/          # Psittacines, pigeons, passerines
│   ├── faq/                     # General, sample, shipping FAQ
│   ├── case-studies/            # Real-world application records
│   └── glossary/                # Technical terminology
├── overrides/main.html          # Schema.org JSON-LD + OG meta + footer
├── mkdocs.yml                   # MkDocs configuration
├── requirements.txt             # Python dependencies
└── .github/workflows/deploy-cloudflare.yml  # Cloudflare Pages CI/CD
```

## Quick Start

```bash
pip install -r requirements.txt
mkdocs build --strict
mkdocs serve  # local preview at http://localhost:8000
```

## Deployment

Push to GitHub main branch → Cloudflare Pages auto-builds.

Alternatively:
```bash
wrangler pages deploy site/ --project-name=avian-docs
```

## Stats

- **50 content pages** across 12 knowledge sections
- **38 technical documents** in full table index
- **3 Schema.org types**: Organization, WebSite, TechArticle
- **0 broken refs**, 0 nav warnings
- **4.7 MB** built site size
