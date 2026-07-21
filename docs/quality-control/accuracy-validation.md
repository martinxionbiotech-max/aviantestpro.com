---
title: Method Validation & Accuracy Assurance — SENO Avian Genetic Testing
description: SENO's standardized validation framework for avian genetic testing assays, following CLSI EP guidelines and ISO 9001/ISO 13485 requirements. Analytical and diagnostic validation parameters, ongoing accuracy monitoring, verification vs. validation distinctions, and re-validation triggers.
canonical: https://aviantestpro.com/knowledge/quality-control/accuracy-validation
keywords: method validation, assay validation, accuracy, precision, CLSI EP, analytical sensitivity, diagnostic sensitivity, LOD, ROC-AUC, PCR validation, qPCR validation, inter-laboratory reproducibility, Bland-Altman, Levey-Jennings, proficiency testing, ISO 13485 validation
datePublished: 2025-01-15
dateModified: 2026-07-21
---
canonical: https://aviantestpro.com/knowledge/quality-control/accuracy-validation


# Method Validation & Accuracy Assurance


All testing methods at SENO undergo a **standardized validation process** before clinical use. The validation framework follows Clinical and Laboratory Standards Institute (CLSI) EP guidelines and meets the requirements of our [ISO 9001:2015](../regulatory/iso-9001.md) and [ISO 13485:2016](../regulatory/iso-13485.md) certified quality management systems.

---

## Validation Framework

SENO's validation workflow consists of three phases, each documented in a validation file that is reviewed and approved by both R&D and Quality Management.

| Phase | Activities | Deliverable | Timeline |
|:------|:-----------|:------------|:---------|
| **Phase 1 — Analytical Validation** | LOD, specificity, precision (repeatability + reproducibility), linearity, amplification efficiency, LOQ | Validation Plan + Analytical Data Report | 4–8 weeks |
| **Phase 2 — Diagnostic Validation** | Clinical sample panel testing (minimum 100 clinical samples), sensitivity/specificity calculation, ROC analysis | Diagnostic Accuracy Report | 4–12 weeks |
| **Phase 3 — Ongoing Monitoring** | Internal QC, proficiency testing, retest rate tracking, complaint investigation, QC chart monitoring | Quarterly QC Review | Perpetual |

---

## Validation Parameters

The table below defines the core validation parameters measured for every quantitative assay (qPCR). Conventional PCR assays (e.g., CHD sexing) are validated on concordance rather than quantitative metrics.

| Parameter | Abbreviation | Definition | SENO Acceptance Criterion | Example (PBFD qPCR) |
|:----------|:------------:|:-----------|:------------------------:|:-------------------:|
| Analytical Sensitivity (Limit of Detection) | LOD | Lowest concentration detected with ≥ 95% confidence | Documented per assay | 10 copies/reaction |
| Analytical Specificity | — | No cross-reactivity with related or common co-infecting organisms | Panel of 6+ organisms tested | 9 organisms tested, all negative |
| Precision (Repeatability) | r | Same-day, same-operator, same-instrument variation | CV < 3% (Ct) | 0.6% CV |
| Reproducibility (Inter-assay) | R | Day-to-day, operator-to-operator variation | CV < 5% (Ct) | 0.96% CV |
| Diagnostic Sensitivity | DSe | Proportion of true positives correctly identified | ≥ 95% | 95.9% |
| Diagnostic Specificity | DSp | Proportion of true negatives correctly identified | ≥ 95% | 98.0% |
| Area Under ROC Curve | ROC-AUC | Overall ability to discriminate positive from negative | ≥ 0.95 | 0.97 |
| Linearity (Dynamic Range) | — | Range over which target concentration is proportional to signal | R² ≥ 0.98 | R² = 0.998 |
| Amplification Efficiency | E | PCR efficiency calculated from standard curve slope | 90–110% | 100.1% |
| Limit of Quantification | LOQ | Lowest concentration quantifiable with CV < 3% (Ct) | CV < 3% (Ct) | 100 copies |
| Inter-laboratory Reproducibility | — | Results consistent across different laboratories | Qualitative: 100% agreement; quantitative: CV < 10% | In progress |

### Parameter Measurement Methods

| Parameter | CLSI Reference | Method |
|:----------|:--------------:|:-------|
| LOD | EP-17 A2 | Probit analysis from 60+ replicates across 5+ concentrations near estimated detection limit |
| Precision | EP-15 A3 | 20 replicates of 3 concentrations over 5 days |
| Linearity | EP-6 A2 | 8–10 concentration points across dynamic range; linear regression |
| Diagnostic accuracy | EP-12 A2 (qualitative), EP-24 A3 (quantitative) | Clinical panel with reference standard; McNemar's test for paired comparison |

---

## Validation by Test Type

Each test category follows a tailored validation approach reflecting the assay format and intended use.

| Test Type | Assay Format | Validation Approach | Key Metrics | Status |
|:----------|:-------------|:--------------------|:------------|:------:|
| DNA Sexing (CHD PCR) | Conventional PCR + Gel | Known-sex birds (50+ species, 200+ individuals); Sanger sequencing of ambiguous results | ≥ 99% concordance | Validated |
| PBFD / BFDV Detection | qPCR (TaqMan) | CLSI EP-17 (LOD), EP-15 (precision), EP-12 (qualitative); 138 clinical samples | LOD 10 copies; DSe 95.9%; DSp 98.0% | Validated |
| APV Detection | qPCR (TaqMan) | Same CLSI framework; spiked tissue samples + clinical panel | LOD 20 copies; DSe ≥ 95% | Validated |
| AIV Detection | qPCR (TaqMan) | OIE-referenced primer/probe set; avian influenza subtypes panel | LOD 15 copies; DSe ≥ 95% | Validated |
| DNA Fingerprinting | Multiplex STR Capillary | Population allele frequency in 15+ populations; Mendelian inheritance check | DP > 0.9999; PI > 10⁶ | Validated |
| Performance Gene Testing (Pigeons) | SNP Genotyping | Population association study (2,500 racing pigeons); independent replication (800 birds) | Significant p < 0.01 | Validated |
| Pigeon Disease Panel (11-plex) | Multiplex PCR + RT-PCR | Target-specific LOD for each of 11 pathogens; 200+ clinical samples panel | Per-target LOD 10–50 copies | Validated |

---

## Ongoing Accuracy Monitoring

Even after initial validation, every assay is continuously monitored through a multi-layered QC system.

| Monitor | Frequency | Method | Target | Responsible |
|:--------|:----------|:-------|:------:|:------------|
| Internal batch QC | Every batch | Positive / negative / NTC / IAC / extraction blank | 100% pass | Laboratory Technician |
| Intra-laboratory duplicate | 5% of samples | Blind duplicate testing by separate analyst | 100% agreement | Quality Manager |
| Inter-laboratory proficiency | Annually | External accredited PT provider (e.g., RCPA, QCMD) | 100% pass | Quality Manager |
| Retest rate | Monthly | Number of retests / total samples × 100% | < 2% | Quality Manager |
| Client discrepancy rate | Continuous | Complaints received / total reports × 100% | < 0.5% | Quality Manager |
| QC chart monitoring (Levey-Jennings) | Continuous per control lot | Plot Ct values against established mean ± 3 SD | No Westgard rule violations | Laboratory Supervisor |
| Method comparison (new vs. old) | On method change | 40+ paired clinical samples, Bland-Altman analysis | Bias ≤ 5% of mean | R&D Team |

### Levey-Jennings QC Rules Applied

| Westgard Rule | Description | Action |
|:--------------|:------------|:-------|
| 1₂s | One control value exceeds ± 2 SD | Warning; inspect controls |
| 1₃s | One control value exceeds ± 3 SD | Reject batch; investigate root cause |
| 2₂s | Two consecutive values exceed ± 2 SD (same side) | Reject batch; systematic error |
| R₄s | Two controls differ by > 4 SD | Reject batch; random error |
| 10x | Ten consecutive values on same side of mean | Reject batch; trend — calibrate instrument |

---

## Verification vs. Validation

It is important to distinguish between verification and validation, as both are required under ISO 13485.

| Term | Definition | SENO Application | Regulatory Reference |
|:-----|:----------|:-----------------|:-------------------:|
| **Verification** | Confirming that specified requirements have been fulfilled through objective evidence | Each production lot of IVD reagents is functionally tested against a reference lot before release | ISO 13485 § 7.3.6 |
| **Validation** | Confirming that the method is suitable for its intended use through objective evidence | Complete CLSI EP validation protocol performed before clinical deployment of any new assay | ISO 13485 § 7.3.7 |

---

## When Re-Validation Is Required

A full or partial re-validation is triggered under the following circumstances:

| Change | Re-Validation Scope | Minimum Sample Size |
|:-------|:--------------------|:-------------------:|
| New primer/probe set for existing target | Full analytical validation (LOD, specificity, precision, linearity) | 60+ replicates |
| New instrument platform (e.g., different qPCR model) | Precision + linearity comparison (40+ samples) | 40 paired samples |
| New reagent supplier or formulation | Equivalency study (40+ paired samples) | 40 paired samples |
| SOP revision affecting critical parameters | Partial re-validation of affected parameters | Per parameter |
| PT failure or quality incident | Investigation-led — may trigger full re-validation | Determined by investigation |
| More than 12 months since last validation | Precision re-check (repeatability + reproducibility) | 20 replicates |
| Change in sample matrix (e.g., feather to blood) | Matrix equivalency study | 20 paired samples per matrix |

---

## Laboratory Accreditation and External Audits

| Accreditation / Audit | Body | Scope | Frequency | Last Completed |
|:----------------------|:-----|:------|:---------:|:--------------:|
| ISO 9001:2015 | TÜV Rheinland / SGS | Quality management system | Annual surveillance + 3-year recertification | 2026 Q1 |
| ISO 13485:2016 | TÜV Rheinland / SGS | Medical device QMS | Annual surveillance + 3-year recertification | 2026 Q1 |
| CMA (China Metrology Accreditation) | CNAS | Laboratory testing competence | Annual | 2025 Q4 |
| CNAS-CL02 (ISO 15189 equivalent) | CNAS | Medical laboratory quality | Biennial | 2026 Q2 |
| Proficiency testing programmes | RCPA / QCMD / external PT provider | Inter-laboratory comparison | Annually per assay | 2026 Q2 |

---

## Cross-References

- [PBFD qPCR Validation Report](../quality-control/pbfd-qpcr-validation.md) — Full CLSI EP validation data for the BFDV qPCR assay
- [Laboratory QC Protocols](../quality-control/laboratory-qc-protocols.md) — Daily, per-batch, and periodic QC procedures
- [Proficiency Testing](../quality-control/proficiency-testing.md) — External and internal proficiency assessment
- [PCR Troubleshooting](../quality-control/pcr-troubleshooting.md) — Resolving amplification issues and ambiguous results
- [DNA Extraction SOP](../quality-control/dna-extraction-sop.md) — Pre-analytical quality control
- [CHD PCR Protocol](../quality-control/chd-pcr-protocol.md) — Sex determination assay specifications
- [Glossary](../glossary/index.md) — Key validation terminology

---

*This document is maintained by SENO's R&D and Quality Management teams. Validation files are controlled documents. For enquiries, contact quality@senobio.com.*
