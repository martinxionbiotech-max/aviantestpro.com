---title: Testing Methods & Technology
description: SENO Testing Center's comprehensive suite of molecular biology techniques for avian genetic testing — conventional PCR, qPCR, capillary electrophoresis, and self-developed reagents.
canonical: https://aviantestpro.com/knowledge/testing-methods/index
keywords: avian DNA testing, PCR technology, qPCR, capillary electrophoresis, fragment analysis, reagent development, CHD sexing, microsatellite fingerprinting
datePublished: 2025-01-15
dateModified: 2026-07-21---
canonical: https://aviantestpro.com/knowledge/testing-methods/index


# Testing Methods & Technology


SENO employs a comprehensive suite of molecular biology techniques optimized for avian sample types. Our self-developed reagents are designed for the specific challenges of feather and swab samples, including melanin inhibition resistance and low-template (low-copy number) amplification. All methods are validated following CLSI EP guidelines and operate under our [ISO 9001:2015](../regulatory/iso-9001.md) and [ISO 13485:2016](../regulatory/iso-13485.md) certified quality management systems.

---

## Core Technologies

| Method | Application | Key Advantage | Link |
|:-------|:------------|:--------------|:-----|
| Conventional PCR | DNA sexing, genotyping | Cost-effective, gel-visible results | [Details →](pcr-technology.md) |
| qPCR / Fluorescent PCR | Pathogen detection, quantification | Real-time Ct values, higher sensitivity | [Details →](qPCR-fluorescent.md) |
| Capillary Electrophoresis | Fragment analysis, fingerprinting | Base-pair resolution of alleles | [Details →](capillary-electrophoresis.md) |
| Reagent Development | Custom primer/probe design | Species-optimized assay performance | [Details →](reagent-development.md) |

---

## Method Selection Guide

The choice of testing method depends on the specific diagnostic or analytical question. The table below provides a quick-reference guide for common testing scenarios.

| Testing Scenario | Recommended Method | Sample Type | Turnaround |
|:-----------------|:-------------------|:------------|:-----------|
| Determine bird sex | Conventional PCR (P2/P8) + gel | Plucked feathers (3–5) | 1–2 days |
| Screen for PBFD | qPCR (TaqMan) | Swab or feather | 1–2 days |
| Screen for APV / Polyomavirus | qPCR (TaqMan) | Swab or feather | 1–2 days |
| Investigate disease outbreak | Multiplex qPCR panel | Oral + cloacal swab | 2–3 days |
| Racing pigeon performance | SNP analysis (PCR + CE) | Feather or blood | 3–5 days |
| Theft recovery / ID | Microsatellite CE (12 loci) | Feather or blood | 3–5 days |
| Parentage confirmation | Microsatellite CE + analysis | Feather or blood from parent + offspring | 3–5 days |
| Virology research | qPCR or conventional PCR + sequencing | Feather, swab, or tissue | 5–7 days |

---

## Technology Comparison

Each technology has distinct performance characteristics that make it suitable for particular applications. The following comparison highlights the key differences across our four core methods.

| Feature | PCR | qPCR | CE | Reagent R&D |
|:--------|:---:|:----:|:--:|:-----------:|
| Quantification | No | Yes (Ct) | Relative (peak height) | N/A |
| Sensitivity | ~100 copies | ~10 copies | ~50 copies | Design-dependent |
| Resolution | ~10 bp (gel) | 1 Ct (~2×) | 1 bp | N/A |
| Time to result | 3–4 h | 1.5–2 h | 4–5 h | 2–4 weeks |
| Cost per reaction | Low | Medium | Medium-high | Variable |
| Multiplex capacity | 2–4 targets | 4–6 targets | 10–20 markers | Unlimited |
| Post-PCR handling | Required (gel) | Not required | Required (plate prep) | N/A |
| Automation level | Semi-automated | Fully automated | Fully automated | Manual |

---

## Validation Framework

Every testing method at SENO undergoes a standardized validation process before being deployed for clinical or diagnostic use. Our validation framework follows CLSI EP guidelines — the same standards used by human molecular diagnostics laboratories.

| CLSI Guideline | Application | Key Metrics |
|:---------------|:------------|:------------|
| EP05 — Precision | Intra- and inter-assay reproducibility | SD, CV (< 3% for Ct, < 5% for fragment size) |
| EP06 — Linearity | Dynamic range of qPCR assays | R² ≥ 0.98, efficiency 90–110% |
| EP07 — Interference | Melanin, hemoglobin, heparin resistance testing | Ct shift < 1.5 cycles |
| EP12 — Qualitative Performance | Clinical sensitivity / specificity | ≥ 95% agreement with sequencing |
| EP15 — User Verification | Method verification in SENO's lab | Pass/fail against manufacturer claims |
| EP17 — Detection Limits | Limit of Blank (LoB), Limit of Detection (LoD), Limit of Quantification (LoQ) | LoD ≤ 10 copies/reaction (qPCR) |

For detailed validation data, see [Accuracy Validation](../quality-control/accuracy-validation.md) and [PBFD qPCR Validation](../quality-control/pbfd-qpcr-validation.md).

---

## Sample Compatibility

Our methods are validated for a broad range of sample types commonly submitted for avian testing. Each sample type presents unique challenges that our protocols and reagents are designed to address.

| Sample Type | Compatible Methods | Key Challenge | SENO Solution |
|:------------|:-------------------|:--------------|:--------------|
| Plucked feather follicle | PCR, qPCR, CE | Low DNA yield, melanin inhibition | Optimized lysis buffer + melanin-resistant PCR mix |
| Oral / cloacal swab | PCR, qPCR | Inhibitors from mucus, bacteria | Stabilization buffer with inhibitor removal |
| Blood (EDTA) | PCR, qPCR, CE | Hemoglobin interference | Purification step + amplification enhancers |
| Blood (FTA card) | PCR | Low input, storage degradation | Small-punch protocol with extended extension time |
| Tissue (post-mortem) | PCR, qPCR, CE | DNA degradation, PCR inhibitors | Short-amplicon design (< 200 bp) |
| Eggshell membrane | PCR | Very low DNA yield | Nested PCR approach |
| Feather (non-follicle) | PCR (limited) | No genomic DNA, keratin | Not recommended — use follicle-containing feathers |

---

## Quality Control Integration

All testing methods are governed by SENO's multi-tier quality control framework, which is documented in detail in the [Quality Control & SOPs](../quality-control/index.md) section. Key QC elements that apply across all methods include:

| QC Element | Frequency | Method Applicability |
|:-----------|:----------|:--------------------:|
| Positive controls | Every batch | PCR, qPCR, CE |
| Negative controls | Every batch | PCR, qPCR, CE |
| No-template control (NTC) | Every batch | PCR, qPCR, CE |
| Extraction blank | Every batch | PCR, qPCR |
| Internal amplification control | Every qPCR reaction | qPCR only |
| Ladder / size standard | Every CE injection | CE only |
| Inter-operator comparison | Quarterly | All methods |
| External proficiency testing | Annually | All methods |

---

## Method Development Pipeline

New testing methods are developed through SENO's structured R&D pipeline, from concept through to clinical deployment.

| Phase | Activities | Duration | Deliverable |
|:------|:-----------|:---------|:------------|
| 1 — Feasibility | Literature review, in-silico primer design, BLAST analysis | 1–2 weeks | Design report |
| 2 — Optimization | Gradient PCR, annealing temp matrix, MgCl₂ titration | 2–4 weeks | Optimized protocol |
| 3 — Validation | CLSI EP studies (precision, sensitivity, specificity) | 4–8 weeks | Validation report |
| 4 — Verification | 50+ clinical samples, comparison with reference method | 2–4 weeks | Verification report |
| 5 — Deployment | SOP drafting, technician training, QC target setting | 1–2 weeks | Released SOP |

---

## Cross-References

- [PCR Technology →](pcr-technology.md) — Detailed conventional PCR methodology
- [qPCR / Fluorescent PCR →](qPCR-fluorescent.md) — Real-time PCR detection chemistry
- [Capillary Electrophoresis →](capillary-electrophoresis.md) — Fragment analysis and DNA fingerprinting
- [Reagent Development →](reagent-development.md) — Self-developed reagent design and manufacturing
- [Laboratory Workflow](../quality-control/lab-workflow.md) — End-to-end sample processing pipeline
- [Quality Control & SOPs](../quality-control/index.md) — QC framework governing all testing methods

---

## Frequently Asked Questions

**Q: Which method is best for routine sexing?**
A: Conventional PCR with P2/P8 primers followed by agarose gel electrophoresis. It is cost-effective, reliable (> 99% concordance with known-sex birds across 50+ species), and requires no specialized instrumentation beyond a thermocycler and gel system.

**Q: When should qPCR be used instead of conventional PCR?**
A: qPCR is preferred when quantification is needed (viral load for disease monitoring), when higher sensitivity is required (detecting early or low-level infections), or when minimizing contamination risk from post-PCR handling is critical (closed-tube detection).

**Q: What is capillary electrophoresis used for in avian testing?**
A: Capillary electrophoresis enables base-pair resolution fragment sizing, which is essential for DNA sexing fragment analysis (distinguishing CHD-W and CHD-Z amplicons that may differ by only 10–30 bp) and microsatellite-based DNA fingerprinting for individual identification and parentage verification.

**Q: Does SENO develop its own reagents?**
A: Yes. SENO designs and manufactures proprietary PCR master mixes, qPCR probe sets, DNA extraction kits, primer panels, and stabilization buffers. These reagents are specifically optimized for avian sample types and are produced in our ISO 13485-certified facility.

**Q: Are all methods validated?**
A: Yes. Every testing method undergoes full CLSI EP-compliant validation before deployment. Validation data — including sensitivity, specificity, precision, and accuracy — is documented and maintained per method. See [Accuracy Validation](../quality-control/accuracy-validation.md) for details.

---

*This page provides an overview of SENO's testing methods portfolio. For detailed protocols and SOPs, refer to the individual method pages and the [Quality Control section](../quality-control/index.md). For inquiries about method validation data, contact quality@senobio.com.*
