---title: Quality Control & SOPs
description: SENO's comprehensive quality control framework, standard operating procedures, validation protocols, and troubleshooting guides for avian genetic testing.
canonical: https://aviantestpro.com/knowledge/quality-control/index
keywords: quality control, SOP, validation, PCR troubleshooting, laboratory protocols, avian DNA testing, qPCR validation, ISO 9001, ISO 13485
datePublished: 2025-01-15
dateModified: 2026-07-21---
canonical: https://aviantestpro.com/knowledge/quality-control/index


# Quality Control & SOPs

## Quality Management Framework

SENO's quality system operates on three levels:

| Level | Scope | Responsibility | Frequency |
|:------|:------|:---------------|:----------|
| **Level 1 — Daily QC** | Every PCR run: controls, extraction blanks, replicate testing | Shift lead technician | Every run |
| **Level 2 — Periodic QC** | Proficiency panels, instrument calibration, reagent lot validation | QC manager | Weekly / per lot |
| **Level 3 — System QC** | Internal audit, management review, corrective action follow-up | Quality director | Monthly / quarterly |

## Key Quality Metrics

| Metric | Target | Monitoring Method |
|:-------|:------:|:-----------------|
| DNA sexing accuracy | ≥ 99% | Periodic blind sample panel (200+ samples) |
| NTC contamination rate | < 1% | Quarterly run audit |
| Sample failure rate (re-extraction) | < 5% | Monthly tracking |
| Report turnaround (standard) | 1–2 working days | Daily log review |
| Proficiency testing score | ≥ 95% agreement | Semi-annual external PT |
| Customer dispute rate | < 0.5% | Per-batch QC review |

## Document Directory

| Document | Type | Description |
|:---------|:----:|:------------|
| [Laboratory QC Protocols](laboratory-qc-protocols.md) | Procedure | Daily QC steps, positive control management, run acceptance criteria |
| [DNA Extraction SOP](dna-extraction-sop.md) | SOP | Standardized protocol for genomic DNA extraction from avian feather, blood, and swab samples |
| [CHD PCR Protocol](chd-pcr-protocol.md) | SOP | PCR amplification parameters for CHD-W/CHD-Z sex determination |
| [PBFD qPCR Validation](pbfd-qpcr-validation.md) | Report | Full analytical validation per CLSI EP guidelines: LOD, precision, accuracy |
| [PCR Troubleshooting Guide](pcr-troubleshooting.md) | Reference | 50+ diagnostic entries — amplification failure, contamination, artifacts |
| [Lab Workflow](lab-workflow.md) | Procedure | End-to-end process: sample reception through report generation |
| [Proficiency Testing](proficiency-testing.md) | Program | Internal and external proficiency testing protocols |
| [Accuracy Validation](accuracy-validation.md) | Procedure | Ongoing accuracy monitoring, method comparison, bias assessment |

## Quality Control Personnel

| Role | Staff Count | Key Responsibilities |
|:-----|:-----------:|:--------------------|
| Senior QC Manager | 1 | System-level QC, audit, certification maintenance |
| Lead Technician (shift) | 3 | Run-level QC, control verification, troubleshooting |
| Validation Specialist | 2 | Method validation, lot-to-lot reagent qualification |
| Data Reviewer | 2 | Report QC, discrepancy investigation, CAPA tracking |

## Cross-References

- [ISO 9001:2015 Quality System](../regulatory/iso-9001.md) — Overview of SENO's quality management framework
- [ISO 13485:2016 Medical Devices QMS](../regulatory/iso-13485.md) — Regulatory-compliant QMS documentation
- [Accuracy Validation](accuracy-validation.md) — Method comparison and bias monitoring
- [Proficiency Testing](proficiency-testing.md) — External quality assessment program



SENO operates a **multi-tier quality control framework** that governs every stage of the avian genetic testing workflow — from sample reception through DNA extraction, PCR amplification, result interpretation, and final report issuance. This framework is aligned with our [ISO 9001:2015](/regulatory/iso-9001/) and [ISO 13485:2016](/regulatory/iso-13485/) certified quality management systems and follows CLSI EP guidelines for assay validation.

---

## QC Architecture

| QC Tier | Scope | Frequency | Responsible Team |
|:--------|:------|:---------:|:-----------------|
| Level 1 — Per-Batch Controls | Every analytical run (extraction + PCR) | Each batch | Laboratory Technician |
| Level 2 — Daily QC | Equipment, reagents, lab environment | Every working day | Shift Lead |
| Level 3 — Periodic QC | Calibration, proficiency testing, audits | Quarterly / Semi-annual / Annual | Quality Manager |
| Level 4 — Management Review | Quality objectives, CAPA, trends | Semi-annual | Senior Management |

---

## Standard Operating Procedures

All laboratory procedures are documented as controlled SOPs with version history in SENO's document management system. SOPs are reviewed annually and updated whenever a method change or CAPA necessitates revision.

| Document | Description | Last Reviewed |
|:---------|:------------|:-------------:|
| [DNA Extraction SOP](dna-extraction-sop.md) | Genomic DNA extraction from feather follicles — step-by-step protocol with troubleshooting | 2026-Q1 |
| [CHD PCR Protocol](chd-pcr-protocol.md) | PCR amplification for avian sex determination — setup, cycling, gel analysis, troubleshooting | 2026-Q1 |
| [PBFD qPCR Validation](pbfd-qpcr-validation.md) | Analytical validation report for BFDV qPCR assay — LOD, specificity, precision, diagnostic accuracy | 2025-Q4 |
| [PCR Troubleshooting](pcr-troubleshooting.md) | Comprehensive guide to resolving PCR failures, contamination, ambiguous sexing, and qPCR issues | 2026-Q1 |
| [Lab Workflow](lab-workflow.md) | End-to-end laboratory process: sample reception → registration → extraction → PCR → interpretation → reporting | 2026-Q1 |

---

## Validation & Accuracy

All testing methods must pass a standardized validation process before clinical use. Validation data is maintained in a dedicated validation file per method.

| Test Type | Validation Approach | Key Metric | Reference |
|:----------|:--------------------|:-----------|:----------|
| DNA Sexing (CHD PCR) | Known-sex birds (50+ species) | ≥ 99% concordance | [Accuracy Validation](accuracy-validation.md) |
| Disease qPCR (PBFD, APV, AIV) | Clinical samples × sequencing confirmation | ROC-AUC ≥ 0.95 | [PBFD qPCR Validation](pbfd-qpcr-validation.md) |
| DNA Fingerprinting | Population allele frequency | DP > 0.9999 | [Application Records](/case-studies/application-records.md) |
| Performance Genes | Population association study (2,500 pigeons) | Significant p < 0.01 | [Application Records](/case-studies/application-records.md) |

---

## Proficiency & External Quality Assessment

SENO participates in annual proficiency testing (PT) through accredited external providers and conducts internal proficiency assessments to ensure ongoing accuracy.

| Assessment Type | Frequency | Performance (2023–2025) | Reference |
|:----------------|:----------|:-----------------------:|:----------|
| External PT — DNA Sexing | Annually | 100% (30/30) | [Proficiency Testing](proficiency-testing.md) |
| External PT — qPCR Detection | Annually | 100% (10/10) | [Proficiency Testing](proficiency-testing.md) |
| Internal Blind Re-test | Quarterly | ≥ 99% agreement | [Proficiency Testing](proficiency-testing.md) |
| Inter-operator Comparison | Quarterly | ≤ 1.5 Ct difference (qPCR) | [Proficiency Testing](proficiency-testing.md) |

---

## Quality Metrics Dashboard

SENO tracks the following key quality indicators on a monthly basis. Targets are reviewed annually during management review.

| Metric | 2026 Target | 2025 Actual | 2024 Actual |
|:-------|:-----------:|:-----------:|:-----------:|
| Report accuracy | ≥ 99.5% | 99.7% | 99.6% |
| On-time delivery (within TAT) | ≥ 95% | 96.2% | 95.8% |
| Proficiency test pass rate | 100% | 100% | 100% |
| Client satisfaction score | ≥ 4.5 / 5.0 | 4.7 | 4.6 |
| Retest rate | < 2% | 1.3% | 1.5% |
| Client discrepancy rate | < 0.5% | 0.2% | 0.3% |
| Instrument calibration compliance | 100% | 100% | 100% |

---

## Key Documents

- [Laboratory QC Protocols](laboratory-qc-protocols.md) — Per-batch, daily, and periodic QC procedures with detailed pass/fail criteria
- [DNA Extraction SOP](dna-extraction-sop.md) — Genomic DNA extraction protocol from feather follicles
- [CHD PCR Protocol](chd-pcr-protocol.md) — Standard PCR protocol for avian CHD gene amplification
- [PBFD qPCR Validation](pbfd-qpcr-validation.md) — Full CLSI EP-compliant validation report
- [PCR Troubleshooting](pcr-troubleshooting.md) — Comprehensive guide to resolving amplification issues
- [Lab Workflow](lab-workflow.md) — End-to-end process from sample reception to report generation
- [Proficiency Testing](proficiency-testing.md) — External and internal proficiency assessment data
- [Accuracy Validation](accuracy-validation.md) — Method validation framework and accuracy data across test types

---

*This document is maintained by SENO's Quality Management team. All SOPs and protocols are controlled documents and should not be reproduced without authorization. For questions, contact quality@senobio.com.*
