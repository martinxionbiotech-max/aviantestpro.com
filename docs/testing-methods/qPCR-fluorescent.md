---title: Real-Time PCR (qPCR) & Fluorescent PCR
description: SENO's qPCR methodology for avian disease detection and quantification — TaqMan probe chemistry, SYBR Green analysis, multiplex panels, CLSI EP validation, and Ct interpretation criteria.
canonical: https://aviantestpro.com/knowledge/testing-methods/qPCR-fluorescent
keywords: qPCR, real-time PCR, TaqMan probe, fluorescent PCR, SYBR Green, Ct value, PBFD, pathogen detection, avian disease, multiplex qPCR
datePublished: 2025-01-15
dateModified: 2026-07-21---
canonical: https://aviantestpro.com/knowledge/testing-methods/qPCR-fluorescent


# Real-Time PCR (qPCR) & Fluorescent PCR


## Overview

Quantitative PCR (qPCR), also known as real-time PCR, monitors DNA amplification in real time using fluorescent signals. Unlike conventional PCR, which detects product only at the end-point (via gel electrophoresis), qPCR captures fluorescence after each cycle, enabling precise quantification of starting template and eliminating the need for post-PCR handling.

At SENO, qPCR is the primary method for disease detection and viral load quantification. Our qPCR assays use both hydrolysis probe (TaqMan) and intercalating dye (SYBR Green) chemistries, depending on the application. All assays are validated following CLSI EP guidelines and run on calibrated real-time PCR instruments.

---

## Detection Chemistries

### TaqMan (Hydrolysis Probe)

TaqMan probes are sequence-specific oligonucleotides labeled with a fluorophore at the 5' end and a quencher at the 3' end. During amplification, the 5'→3' exonuclease activity of Taq polymerase cleaves the probe, separating the fluorophore from the quencher and generating a fluorescence signal proportional to the amount of target accumulated.

| Chemistry | Mechanism | Specificity | Multiplex Capability | SENO Application |
|:----------|:-----------|:-----------:|:--------------------:|:-----------------|
| TaqMan probe | Probe cleavage by 5' nuclease | Target-specific (hybridization required) | High (up to 6 channels) | Pathogen quantification (PBFD, AIV, APV) |
| SYBR Green | Intercalating dye binding to dsDNA | Non-specific (melts with any dsDNA) | Low (single channel) | Sexing verification, melt curve analysis |

### TaqMan Advantages

| Feature | TaqMan | SYBR Green |
|:--------|:------:|:-----------:|
| Sequence specificity | ✓ (probe-dependent) | ✗ (dye binds any dsDNA) |
| Multiplex capability | ✓ (spectrally distinct dyes) | ✗ (single dye) |
| Melt curve analysis | ✗ (probe not melt-compatible) | ✓ (Tm-based confirmation) |
| Background fluorescence | Low | Moderate |
| Cost per reaction | Higher (~$0.50–1.00/reaction) | Lower (~$0.10–0.25/reaction) |

### SENO's TaqMan Multiplex Configuration

SENO's multiplex qPCR assays use up to four spectrally distinct fluorescent channels, enabling simultaneous detection of multiple pathogens or targets in a single reaction.

| Channel | Dye | Excitation (nm) | Emission (nm) | Typical Target |
|:--------|:----|:---------------:|:-------------:|:---------------|
| FAM | 6-FAM | 495 | 520 | BFDV (PBFD) or APV target |
| HEX | Hexachlorofluorescein | 535 | 555 | Second pathogen target |
| ROX | Carboxyrhodamine | 585 | 610 | Internal positive control |
| Cy5 | Cyanine 5 | 649 | 666 | Optional third pathogen target |

---

## qPCR Process

| Step | Temperature | Duration | Fluorescence Reading? |
|:-----|:-----------:|:--------:|:--------------------:|
| Initial Denaturation | 95°C | 3–5 min | No |
| Denaturation | 95°C | 10–15 s | No |
| Annealing + Extension + Read | 60°C | 30–45 s | Yes (each cycle) |
| (Optional) Melt Curve | 60→95°C, ramp 0.5°C/s | ~10 min | Yes (continuous) |
| Hold | 4°C | ∞ | — |

The annealing/extension step is combined into a single 60°C step for TaqMan assays (using Taq polymerases with fast extension kinetics). For SYBR Green assays requiring melt curve analysis, a post-amplification melt curve ramp is added.

---

## Quantification: Ct Values

The cycle threshold (Ct) is the cycle number at which fluorescence exceeds the background threshold. Lower Ct values indicate higher starting target quantity. The relationship between Ct and starting copy number is logarithmic.

| Ct Range | Interpretation | Clinical Meaning |
|:---------|:---------------|:-----------------|
| < 25 | High viral load / strong positive | Active infection, high shedding |
| 25–30 | Moderate viral load / positive | Active infection, moderate shedding |
| 30–35 | Low viral load / positive | Possible subclinical or early infection |
| 35–38 | Very low viral load | Equivocal — report as "detected at low level" |
| 38–40 | Borderline | Suggest retest in 2 weeks |
| No Ct (≥ 40) | Negative | No target detected |

### Standard Curve

Quantification requires a standard curve generated from serial dilutions of a known-concentration target (typically plasmid DNA). SENO's PBFD qPCR assay, for example, has the following standard curve parameters:

| Parameter | SENO PBFD qPCR | Acceptance Criteria |
|:----------|:--------------:|:-------------------:|
| Slope | −3.32 | −3.1 to −3.6 (90–110% efficiency) |
| Intercept | 38.9 | Method-specific |
| R² | 0.998 | ≥ 0.98 |
| Efficiency | 100.1% | 90–110% |
| Dynamic range | 10¹–10⁶ copies/reaction | ≥ 5 logs |
| LoD | 10 copies/reaction | 95% detection rate |

---

## Advantages Over Conventional PCR

| Feature | Conventional PCR | qPCR |
|:--------|:----------------:|:----:|
| Detection method | End-point (gel) | Real-time (fluorescence) |
| Quantification | Semi-quantitative (band intensity) | Fully quantitative (Ct vs. standard curve) |
| Sensitivity | ~100 copies/reaction | ~10 copies/reaction |
| Dynamic range | ~2–3 logs | 5–8 logs |
| Turnaround time | 3–4 hours (incl. gel) | 1–2 hours |
| Post-PCR handling | Required (gel preparation, loading, staining) | Not required (closed-tube system) |
| Contamination risk | Higher (open-tube handling after PCR) | Lower (sealed plate, no post-PCR processing) |
| Multiplex capability | Limited (2–4 targets with band sizing) | 4–6 targets (spectral discrimination) |
| Data format | Gel image (qualitative) | Amplification curve (quantitative) |
| Automation | Semi-automated | Fully automated plate -> data pipeline |

---

## SENO's qPCR Applications

### Pathogen Quantification

| Application | Detection Chemistry | Pathogens / Targets | Clinical Purpose |
|:------------|:--------------------|:--------------------|:-----------------|
| PBFD quantitative | TaqMan (FAM) | BFDV — ORF1 (Rep gene) | Viral load monitoring, treatment response |
| AIV screening | TaqMan (FAM/HEX) | Avian Influenza (M gene, H5, H7, H9 subtypes) | Outbreak investigation |
| Avian Polyomavirus | TaqMan (FAM) | APV — VP1 gene | Psittacine screening |
| Pigeon disease panel | Triplex TaqMan | BFDV + APV + Internal control | Comprehensive health screening |
| Circovirus screening | SYBR Green + melt | PiCV, BFDV | Research applications |
| Housekeeping gene | TaqMan (HEX) | GAPDH or β-actin | Sample quality assessment |

### Multiplex Disease Panels

SENO has developed multiplex qPCR panels for comprehensive disease screening. These panels detect multiple pathogens in a single reaction, reducing cost and turnaround time.

| Panel Name | Targets | Channels | Reaction Time |
|:-----------|:--------|:--------:|:-------------:|
| Pigeon Health Panel | BFDV + APV + PiHV + IC | FAM + HEX + ROX + Cy5 | 75 min |
| Psittacine Panel | BFDV + APV + AIV + IC | FAM + HEX + ROX + Cy5 | 75 min |
| Respiratory Panel | PiHV + PiADV + Mycoplasma + IC | FAM + HEX + ROX + Cy5 | 80 min |

---

## qPCR Validation: CLSI EP Compliance

All qPCR assays at SENO are validated following CLSI EP guidelines. The table below summarizes the validation parameters and acceptance criteria. Full validation reports are maintained for each assay.

| Parameter | CLSI Guideline | SENO Protocol | Acceptance Criteria |
|:----------|:---------------|:--------------|:--------------------|
| Limit of Blank (LoB) | EP17 | 20 replicates of negative matrix | No positive calls |
| Limit of Detection (LoD) | EP17 | 3 independent runs, 5 replicates per level over 10 dilutions | ≥ 95% detection at LoD |
| Limit of Quantification (LoQ) | EP17 | Precision profile across dynamic range | CV ≤ 25% (copies/µL) |
| Precision | EP05 | 2 runs/day × 5 days, 3 replicates each | Ct CV < 3% |
| Linearity / Dynamic Range | EP06 | 7–9 concentration levels, 3 replicates each | R² ≥ 0.98, efficiency 90–110% |
| Specificity | EP12 | 20 related/near-neighbor organisms tested | No cross-reactivity |
| Interference | EP07 | Hemoglobin, melanin, heparin spiked samples | Ct shift < 1.5 cycles |

For a complete validation example, see [PBFD qPCR Validation Report](../quality-control/pbfd-qpcr-validation.md).

---

## Internal Controls

Every qPCR reaction at SENO includes an internal control (IC) to monitor for PCR inhibition — a common issue in avian samples due to melanin, hemoglobin, or other co-purified inhibitors.

| Control Type | Chemistry | Target | Expected Ct | Action if Ct Out of Range |
|:-------------|:----------|:-------|:-----------:|:---------------------------|
| Internal Positive Control (IPC) | TaqMan (ROX/Cy5) | Synthetic target spiked into master mix | Ct 28–32 | Repeat with diluted or re-purified DNA |
| Extraction Control (EC) | TaqMan (HEX) | Exogenous RNA added to lysis buffer | Ct 25–30 | Extraction failure — re-extract |
| No Template Control (NTC) | — | Nuclease-free water | No Ct | Contamination — repeat with fresh reagents |

---

## Instrumentation

SENO operates multiple qPCR instruments to support routine diagnostics and R&D.

| Instrument | Capacity | Filter Channels | Applications | Calibration |
|:-----------|:--------:|:---------------:|:-------------|:------------|
| Bio-Rad CFX96 Touch | 96-well | 5 (FAM, HEX, ROX, Cy5, Cy5.5) | All diagnostic qPCR | Quarterly |
| Bio-Rad CFX384 Touch | 384-well | 5 (FAM, HEX, ROX, Cy5, Cy5.5) | High-throughput screening | Quarterly |
| Applied Biosystems QuantStudio 3 | 96-well | 4 (FAM, VIC, ROX, Cy5) | R&D, validation studies | Bi-annual |

---

## Cross-References

- [PBFD qPCR Validation Report](../quality-control/pbfd-qpcr-validation.md) — Complete CLSI EP validation data
- [PCR Technology →](pcr-technology.md) — Conventional PCR methodology (complementary technique)
- [Capillary Electrophoresis →](capillary-electrophoresis.md) — Post-PCR fragment analysis
- [Reagent Development →](reagent-development.md) — Self-developed qPCR probe sets
- [Laboratory QC Protocols](../quality-control/laboratory-qc-protocols.md) — Daily and periodic QC procedures
- [Accuracy Validation](../quality-control/accuracy-validation.md) — Method validation framework

---

## Frequently Asked Questions

**Q: What is the difference between qPCR and conventional PCR?**
A: qPCR measures amplification in real time using fluorescent signals, enabling precise quantification without post-PCR gel analysis. Conventional PCR detects product only at the end-point. qPCR is more sensitive (~10 vs. ~100 copies), faster (1–2 vs. 3–4 hours), and less prone to contamination (closed-tube system).

**Q: Why does SENO use TaqMan probes instead of SYBR Green?**
A: TaqMan probes provide sequence-specific detection, enabling multiplexing (multiple targets in one reaction) and eliminating false positives from primer-dimer or non-specific amplification. SYBR Green is used only for melt curve analysis in specific applications.

**Q: How do you interpret a Ct of 36?**
A: A Ct of 36 indicates very low target levels. The result is reported as "detected at low level" and may suggest subclinical infection, early-stage disease, or residual nucleic acid from a resolved infection. A follow-up sample in 2–4 weeks is recommended to assess trend.

**Q: What internal controls are used in qPCR reactions?**
A: SENO uses a synthetic internal positive control (IPC) added to the master mix (ROX-labeled) and an extraction control (exogenous RNA added during lysis, HEX-labeled). Both must give Ct values within their expected ranges for the reaction to be valid.

**Q: How is qPCR quantified?**
A: A standard curve is generated from serial dilutions of a known-concentration plasmid containing the target sequence. The Ct values of unknown samples are interpolated against this curve to calculate copy numbers. Standard curves are run with each batch or weekly for established assays with stable performance.

---

*This document describes SENO's qPCR methodology and applications. For detailed validation data for specific assays, refer to the [Quality Control section](../quality-control/index.md). For protocol-specific inquiries, contact quality@senobio.com.*
