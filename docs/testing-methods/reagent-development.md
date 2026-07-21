---title: Self-Developed Reagents
description: SENO's proprietary molecular biology reagents for avian testing — PCR master mixes, qPCR probe sets, DNA extraction kits, primer panels, and stabilization buffers developed under ISO 13485.
canonical: https://aviantestpro.com/knowledge/testing-methods/reagent-development
keywords: reagent development, PCR master mix, TaqMan probe, primer design, DNA extraction kit, in-house reagents, ISO 13485, in-vitro diagnostic reagents
datePublished: 2025-01-15
dateModified: 2026-07-21---
canonical: https://aviantestpro.com/knowledge/testing-methods/reagent-development


# Self-Developed Reagents


## Overview

SENO designs, develops, and manufactures proprietary molecular testing reagents specifically optimized for avian sample types. This in-house reagent program reduces dependency on external commercial suppliers, enables cost-effective testing services, and allows rapid customization of assays for novel species or emerging pathogens.

Our reagent development laboratory is part of the ISO 13485:2016 certified medical device quality management system, meaning our reagents are produced under the same quality standards as commercial in-vitro diagnostic (IVD) kits. The development process follows a structured pipeline from design concept through analytical validation, lot release, and ongoing stability monitoring.

---

## Reagent Portfolio

| Reagent Type | Application | Development Status | Production Capacity |
|:-------------|:------------|:------------------:|:-------------------:|
| PCR master mixes | CHD gene amplification for sexing | ✓ Production (since 2017) | 10,000 reactions/month |
| qPCR probe sets | Pathogen detection (PBFD, APV, AIV) | ✓ Production (since 2018) | 5,000 reactions/month |
| DNA extraction kits | Silica column-based purification | ✓ Production (since 2016) | 5,000 preps/month |
| Primer panels | Pigeon disease (11-plex) | ✓ Production (since 2020) | 2,000 reactions/month |
| Stabilization buffers | Swab collection and transport | ✓ Production (since 2019) | 3,000 tubes/month |
| Novel sexing primer sets | Cross-species validation | ○ R&D (in validation) | — |
| Multiplex qPCR master mix | Multi-target detection (4-channel) | ○ R&D (optimization) | — |

---

## Reagent Development Pipeline

New reagents are developed through SENO's structured pipeline, from concept through to commercial production.

### Phase 1: Design & In Silico Analysis

| Activity | Tool / Method | Duration | Deliverable |
|:---------|:--------------|:---------|:------------|
| Literature review | PubMed, GenBank review | 1 week | Background report |
| Sequence retrieval | NCBI Nucleotide, Ensembl | 1 day | Sequence set |
| Primer design | Primer3, Primer-BLAST, OligoAnalyzer | 2–3 days | Primer candidates (5–10 pairs) |
| In silico specificity | BLASTn against nr database | 1 day | Specificity report |
| Secondary structure check | mFold, UNAFold | 1 day | ΔG estimates for hairpins and dimers |
| Probe design (qPCR) | Primer3 + manual Tm matching | 2 days | TaqMan probe candidates |

### Phase 2: Wet-Lab Optimization

| Activity | Test Conditions | Duration | Acceptance Criteria |
|:---------|:----------------|:---------|:--------------------|
| Gradient PCR | 10°C gradient around predicted Tm | 2 days | Single band at optimal Tm |
| MgCl₂ titration | 1.0–4.0 mM in 0.5 mM increments | 2 days | Optimal yield + specificity at 1.5–2.5 mM |
| Annealing temp optimization | ± 5°C from calculated Tm in 1°C steps | 2 days | Sharp single band, Ct minimum for qPCR |
| Primer concentration matrix | 0.1–0.5 µM in 0.1 µM steps | 1 day | Optimal at 0.2–0.3 µM |
| Sensitivity assessment | 10-fold dilution series (10⁶→1 copy) | 2 days | LoD determined |
| Cross-reactivity panel | 10–20 related species/organisms | 2–3 days | No non-specific amplification |

### Phase 3: Analytical Validation

Full CLSI EP-compliant validation as described in [qPCR Validation →](qPCR-fluorescent.md#qpcr-validation-clsi-ep-compliance).

| Validation Parameter | Test Design | Acceptance Criteria |
|:---------------------|:------------|:--------------------|
| Limit of Detection (LoD) | 3 independent runs, 5 replicates per concentration, 10-fold serial dilution | ≥ 95% detection |
| Precision (repeatability) | 10 replicates within a single run | CV < 3% (Ct) |
| Reproducibility | 3 runs × 5 days | CV < 5% (Ct) |
| Accuracy | 50 known samples compared to sequencing or reference method | ≥ 95% concordance |
| Robustness | Deliberate variations in template conc., cycle number, annealing temp | ± 1 Ct vs. standard |

### Phase 4: Lot Release & Stability

| Test | Frequency | Method | Acceptance Criteria |
|:-----|:----------|:-------|:--------------------|
| Visual inspection | Each lot | Clarity, color, absence of precipitation | Clear, colorless, no particles |
| pH measurement | Each lot | pH meter | 8.0–8.5 (for master mixes) |
| Activity assay | Each lot | Amplify positive control; compare Ct/band to reference | Ct ± 1.0 or band ± 20% intensity |
| Sterility test | Each lot | Membrane filtration + 14-day culture or compendial method | No growth |
| Endotoxin (extraction kits) | Each lot | LAL assay | < 10 EU/mL |
| Accelerated stability | 3 lots | 37°C / 25°C / 4°C; test monthly | Activity ≥ 80% of initial at T=0 |
| Real-time stability | All lots | 25°C; test quarterly for 12 months | Activity ≥ 80% of initial |

---

## Key Reagent Specifications

### PCR Master Mix (for CHD Sexing)

| Component | Specification | Purpose |
|:----------|:--------------|:--------|
| DNA polymerase | Modified Taq (N-terminal deletion) | Thermal stability, 5'→3' exonuclease for probe assays |
| Buffer | 1×: 10 mM Tris-HCl (pH 8.3), 50 mM KCl | Optimal reaction environment |
| MgCl₂ | 2.5 mM (1.5–4.0 mM range available) | Cofactor for polymerase activity |
| dNTPs | 0.4 mM each (dATP, dCTP, dGTP, dTTP) | Building blocks for DNA synthesis |
| BSA | 0.1 µg/µL | Stabilizes polymerase, counteracts melanin inhibition |
| Stabilizers | 0.1% Triton X-100, 5% glycerol | Long-term storage, freeze-thaw protection |
| Volume per reaction | 12.5 µL (2× concentration) | Convenient single-tube format |

### qPCR Probe Sets — Design Parameters

| Parameter | Acceptance Specification | Rationale |
|:----------|:------------------------|:-----------|
| Probe Tm | 68–72°C (5–10°C above primer Tm) | Ensures probe binds before primers extend |
| Probe length | 18–30 nucleotides | Balances specificity and cost |
| GC content | 40–60% | Sufficient binding stability |
| No G at 5' end | Design rule | G quenches 5' fluorophore |
| No runs of > 4 same nucleotide | Design rule | Reduces non-specific binding |
| Reporter dye | FAM, HEX, ROX, or Cy5 | Compatible with CFX96 and QuantStudio optics |
| Quencher dye | BHQ-1 or BHQ-2 | Low background, matched to reporter emission |
| Internal control | Exogenous synthetic RNA (VIC/HEX labeled) | Added at extraction, amplifies independently |

### Stabilization Buffer (for Swab Transport)

| Parameter | Specification |
|:----------|:--------------|
| Cell lysis / preservation | Guanidine-based chaotropic agent (2–4 M) |
| Nuclease inhibition | ≥ 0.1% SDS + 10 mM EDTA |
| pH | 6.5–7.5 (phosphate or Tris buffer) |
| Shelf life | 12 months at room temperature (25°C) |
| Compatibility | Directly compatible with silica-column DNA extraction |
| Storage | Room temperature (15–30°C) |

---

## Quality Assurance

All reagents undergo a comprehensive quality assurance process before release for clinical testing.

| QA Step | Description | Verifies |
|:--------|:------------|:---------|
| Incoming raw material QC | Test all raw materials (enzymes, dNTPs, primers, probes, buffers) before use | Purity, activity, concentration |
| In-process QC | Monitor critical parameters during manufacturing (pH, viscosity, mixing homogeneity) | Process consistency |
| Lot-release QC | Test every lot against established specifications | Lot-to-lot consistency |
| 21 CFR Part 11 compliance | Electronic records, audit trails, and signatures | Data integrity |
| Stability monitoring | Real-time (25°C, 12 months) + accelerated (37°C, 1 month) | Product shelf life |

---

## Lot-to-Lot Consistency

Lot-to-lot consistency is one of the most important quality metrics for diagnostic reagents. SENO maintains a rolling comparison of new lots against a reference lot.

| Test | Method | Acceptance Criteria |
|:-----|:--------|:--------------------|
| Activity comparison | Amplify 3 positive controls (high, medium, low concentration) | Ct difference ≤ 1.0 vs. reference lot |
| Specificity comparison | Amplify 3 negative controls (NTC + 2 near-neighbor organisms) | No false positives |
| Extraction efficiency (kits) | Extract 10 parallel samples | Yield within ± 20% of reference lot |
| Shelf-life extrapolation | Accelerated stability at 37°C, compare T=0 vs. T=14 days | Activity ≥ 90% of initial |

---

## Dry Reagent R&D (In Progress)

SENO is actively developing a next-generation dry reagent format for room-temperature stable master mixes. This format eliminates cold-chain requirements and simplifies international shipping.

| Parameter | Current (Liquid) | Dry Format (Goal) |
|:----------|:----------------:|:-----------------:|
| Storage temperature | −20°C | Room temperature (15–30°C) |
| Shelf life | 12–24 months | 18–24 months |
| Shipping | Cold chain (dry ice or ice packs) | Room temperature |
| Reconstitution | Not required | Add nuclease-free water |
| Performance | Current baseline | Equivalent to liquid format |
| Target availability | — | 2027 |

---

## ISO 13485 Manufacturing

SENO's reagent manufacturing facility is ISO 13485:2016 certified, meeting medical device quality management standards for in-vitro diagnostic reagents. Key ISO 13485 elements implemented in our reagent production:

| ISO 13485 Clause | Implementation in Reagent Manufacturing |
|:-----------------|:----------------------------------------|
| 7.2 — Design and Development | Structured design control: design inputs → design outputs → design review → design transfer |
| 7.4 — Purchasing | Supplier qualification: performance audits, incoming inspection of raw materials |
| 7.5 — Production and Service Provision | Environmental monitoring (clean room Class 100,000), equipment calibration, batch records |
| 7.6 — Monitoring and Measuring Equipment | Thermocyclers, pH meters, pipettes, NanoDrop — all calibrated with NIST-traceable standards |
| 8.2 — Monitoring and Measurement | Lot release testing, in-process inspections, final product testing |
| 8.3 — Nonconforming Product | Quarantine and disposition system for non-conforming lots |
| 8.5 — Corrective and Preventive Action | CAPA system: root cause investigation, corrective action, effectiveness verification |

For full details on our ISO 13485 certification, see [Certifications →](../about/certifications.md) and [ISO 13485 Details →](../regulatory/iso-13485.md).

---

## Cross-References

- [PCR Technology →](pcr-technology.md) — Master mix application in conventional PCR
- [qPCR / Fluorescent PCR →](qPCR-fluorescent.md) — Probe set application in real-time PCR
- [Capillary Electrophoresis →](capillary-electrophoresis.md) — Fragment analysis primer panels
- [Accuracy Validation](../quality-control/accuracy-validation.md) — Reagent validation data
- [PBFD qPCR Validation](../quality-control/pbfd-qpcr-validation.md) — Example assay using self-developed reagents
- [Certifications](../about/certifications.md) — ISO 13485 and ISO 9001 certification details
- [ISO 13485 Details](../regulatory/iso-13485.md) — Medical device QMS scope
- [ISO 9001 Details](../regulatory/iso-9001.md) — General quality management scope

---

## Frequently Asked Questions

**Q: Are SENO's reagents compatible with standard laboratory instruments?**
A: Yes. All reagents are designed for compatibility with common laboratory equipment including standard thermal cyclers (ABI, Bio-Rad), real-time PCR platforms (CFX96, QuantStudio), and capillary electrophoresis instruments (ABI 3500, SeqStudio). No proprietary instrumentation is required.

**Q: Does SENO sell reagents to other laboratories?**
A: Primarily, SENO's reagents are developed for internal use in our testing center's diagnostic services. Custom batches for partner laboratories and reserach collaborations are considered on a case-by-case basis. Contact rd@senobio.com for inquiries.

**Q: How does SENO ensure lot-to-lot consistency?**
A: Every production lot undergoes release testing against a stored reference lot using quantitative activity, specificity, and sensitivity assays. Acceptance criteria require Ct differences ≤ 1.0 cycles and ≥ 95% concordance on clinical samples between the new lot and the reference.

**Q: What is the shelf life of SENO's master mixes?**
A: Liquid PCR master mixes and qPCR probe sets are stable for 12–24 months when stored at −20°C. Stabilization buffers and DNA extraction reagents are stable for 12 months at room temperature. Each lot is labeled with a manufacturing date and expiration date.

**Q: Are the reagents optimized for difficult avian samples?**
A: Yes. This is one of the primary advantages of our in-house development program. Our PCR master mixes contain additives (BSA, DMSO, optimized MgCl₂) that counteract melanin and hemoglobin inhibition commonly encountered in feather and blood samples. Low-template amplification enhancers support detection from as few as 10 copies of target.

**Q: Can SENO develop custom primer/probe sets for novel species?**
A: Yes. The R&D team can develop and validate custom assays for novel species or emerging pathogens. The typical timeline is 4–8 weeks from sequence submission to validated assay, depending on complexity. Contact rd@senobio.com to discuss custom assay development.

---

*This document describes SENO's self-developed reagent program. For reagent performance data, refer to the [Accuracy Validation](../quality-control/accuracy-validation.md) page. For custom development inquiries, contact rd@senobio.com.*
