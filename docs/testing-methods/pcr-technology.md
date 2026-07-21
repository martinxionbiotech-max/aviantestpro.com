---title: PCR Technology
description: SENO's conventional PCR methodology for avian DNA testing — CHD sexing, pathogen detection, thermal cycling protocols, primer design, and troubleshooting optimized for feather and swab samples.
canonical: https://aviantestpro.com/knowledge/testing-methods/pcr-technology
keywords: PCR, polymerase chain reaction, CHD gene, P2/P8 primers, avian sexing, thermal cycling, DNA amplification, primer design
datePublished: 2025-01-15
dateModified: 2026-07-21---
canonical: https://aviantestpro.com/knowledge/testing-methods/pcr-technology


# PCR Technology


## Overview

Polymerase Chain Reaction (PCR) is a molecular biology technique that amplifies specific DNA sequences from small quantities of starting material. PCR is the foundation of avian DNA testing at SENO. Every testing service — from routine sex determination to pathogen screening and microsatellite genotyping — begins with PCR amplification.

SENO's PCR protocols are specifically optimized for avian samples. Unlike human or mammalian PCR, avian DNA extracted from feather follicles presents unique challenges: low template DNA (often 1–10 ng per reaction), melanin co-purification (a known Taq polymerase inhibitor), and degraded DNA from improperly stored samples. Our protocols address each of these challenges through optimized master mixes, adjusted cycling parameters, and validated primer sets.

---

## PCR Process

PCR consists of repeated thermal cycles, each with three main steps that together achieve exponential amplification of the target DNA region. The table below details the typical cycling parameters used at SENO for CHD gene sexing.

| Step | Temperature | Duration | Purpose |
|:-----|:-----------:|:--------:|:--------|
| Initial Denaturation | 94–95°C | 2–5 min | Activate polymerase, denature double-stranded template DNA |
| Denaturation (cycle) | 94–98°C | 15–30 s | Separate double-stranded DNA into single strands |
| Annealing (cycle) | 50–65°C | 15–30 s | Allow primers to bind specifically to target sequences |
| Extension (cycle) | 72°C | 30–60 s/kb | Taq DNA polymerase extends new complementary strand |
| Final Extension | 72°C | 2–5 min | Complete all unfinished strands |
| Hold | 4°C | ∞ | Short-term storage of PCR product |

Annealing temperature is the most critical parameter for specificity. For P2/P8 primers used in CHD sexing, the optimal annealing temperature is 50°C. A 2–3°C increase improves specificity but may reduce yield; a 2–3°C decrease increases yield but may produce non-specific bands.

---

## Applications at SENO

### CHD Gene Sexing

The primary application of conventional PCR at SENO is avian sex determination through amplification of the CHD (Chromo-Helicase-DNA binding) gene. The CHD-Z and CHD-W genes are located on the Z and W sex chromosomes respectively. Conserved primers (P2/P8) amplify an intron region that differs in length between the two genes.

| Primer Set | Target | Forward Sequence (5' → 3') | Reverse Sequence (5' → 3') | Amplicon Size |
|:-----------|:-------|:---------------------------|:---------------------------|:-------------|
| P2/P8 | CHD-Z/W | TCTGCATCGCTAAATCCTTT | CTCCCAAGGATGAGRAAYTG | 350–450 bp |
| 2550F/2718R | CHD-Z/W | GTTACTGATTCGTCTACGAGA | ATTGAAATGATCCAGTGCTTG | 600–700 bp |

- **Male (ZZ):** Single CHD-Z fragment (one band on gel)
- **Female (ZW):** CHD-Z + CHD-W fragments (two bands on gel)

In species where the CHD-Z and CHD-W introns are similar in length (producing co-migrating bands), the alternative 2550F/2718R primer set may be used. For example, some Columbiformes (pigeons, doves) and certain Psittaciformes (parrots) show minimal length polymorphism with P2/P8 and require the alternative set.

The detailed protocol for CHD PCR is described in the [CHD PCR Protocol SOP](../quality-control/chd-pcr-protocol.md).

### Pathogen Detection

Conventional PCR is used for detection of avian DNA viruses when qPCR instrumentation is unavailable or when the target requires amplicon sequencing for confirmation.

| Pathogen | Target Gene | Amplicon Size | Application |
|:---------|:------------|:-------------:|:------------|
| BFDV (PBFD) | ORF1 (Rep) | 540–700 bp | Confirmation of qPCR-positive results |
| PiHV (Pigeon Herpesvirus) | DNA polymerase | 400 bp | Respiratory disease workup |
| PiADV (Adenovirus) | Hexon gene | 500 bp | Enteric disease workup |
| APV (Polyomavirus) | VP1 | 350 bp | Psittacine screening |

### Microsatellite Genotyping

For DNA fingerprinting, PCR amplification of 12 microsatellite loci is performed using fluorescently labeled primers. The resulting amplicons are then analyzed by capillary electrophoresis for allele sizing.

| Locus | Repeat Motif | Size Range | Label Dye |
|:------|:-------------|:----------:|:----------|
| Pgi01 | (CA)₁₉ | 180–220 bp | FAM (blue) |
| Pgi02 | (GT)₂₃ | 140–180 bp | HEX (green) |
| Pgi03 | (CA)₁₅ | 200–240 bp | FAM (blue) |
| Pgi04 | (ATCT)₁₂ | 160–200 bp | TAMRA (yellow) |
| Pgi05–Pgi12 | Various | 120–320 bp | Mixed |

See [Capillary Electrophoresis →](capillary-electrophoresis.md) for details on post-PCR fragment analysis.

---

## PCR Platform

SENO operates a fleet of thermal cyclers to support routine testing and R&D workloads.

| Instrument | Capacity | Typical Use | Validation Status |
|:-----------|:--------:|:------------|:-----------------|
| Applied Biosystems VeritiPro | 96-well (6 blocks) | CHD sexing, routine genotyping | ✓ Calibrated bi-annually |
| Bio-Rad T100 | 96-well | Pathogen detection, R&D | ✓ Calibrated bi-annually |
| Bio-Rad C1000 Touch | 96-well + 384-well | High-throughput fingerprinting | ✓ Calibrated bi-annually |

---

## PCR Optimization for Avian Samples

### Melanin Inhibition

Feather-derived DNA often contains melanin, a potent inhibitor of Taq DNA polymerase. SENO's protocols mitigate this through:

| Strategy | Implementation | Effect |
|:---------|:---------------|:-------|
| Inhibitor-resistant polymerase | Modified Taq with BSA (0.1 µg/µL) | Restores activity in melanin presence |
| Extended denaturation | Initial denaturation 5 min at 95°C | Improved template accessibility |
| Increased polymerase units | 0.05 U/µL → 0.1 U/µL | Compensates for partial inhibition |
| Additive | 3% DMSO or 5% glycerol | Reduces secondary structure interference |

### Low Template Amplification

Feather follicle samples typically yield 5–20 ng DNA per reaction. When template is limited (< 5 ng), the following adjustments are applied:

| Adjustment | Standard Protocol | Low-Template Adaptation |
|:-----------|:-----------------:|:-----------------------:|
| Template volume | 2 µL | 4–6 µL |
| Cycles | 35 | 38–40 |
| Extension time | 45 s | 60 s |
| Primer concentration | 0.2 µM | 0.3 µM |
| Polymerase units | 0.5 U | 1.0 U |

---

## Quality Controls in PCR

Every PCR run at SENO includes a standardized set of controls to ensure valid results. These controls are part of our [Level 1 QC protocol](../quality-control/laboratory-qc-protocols.md).

| Control | Content | Expected Result | Purpose |
|:--------|:--------|:----------------|:--------|
| Positive control (ZZ) | Known male DNA (single band) | Single amplicon | Verifies PCR chemistry works |
| Positive control (ZW) | Known female DNA (two bands) | Two amplicons | Verifies sex differentiation |
| Negative control (NTC) | Nuclease-free water | No amplification | Detects reagent contamination |
| Extraction blank | Lysis buffer (no sample) | No amplification | Detects extraction contamination |

---

## Troubleshooting Common PCR Issues

| Problem | Possible Cause | Solution |
|:--------|:---------------|:---------|
| No amplification in any sample | Taq polymerase inactive or expired | Check expiry; repeat with fresh master mix |
| No amplification in NTC but samples amplify | Inactive enzyme in master mix or incorrect cycling | Verify thermocycler program; re-run gradient |
| Weak or faint bands | Low template DNA (< 1 ng) | Re-PCR with increased template (4–6 µL) or re-extract |
| Smearing across lanes | Degraded template DNA | Re-collect sample; reduce cycles to 30–33 |
| Multiple non-specific bands | Annealing temperature too low | Increase annealing temp by 2°C; re-optimize gradient |
| Bands in NTC | Amplicon carryover contamination | UV-decontaminate workstation; use fresh reagents; change pipettes |
| Female appears as single band | CHD-W/Z same size in this species | Use alternative 2550F/2718R primer set |
| Faint bands in all lanes including NTC | Primer-dimer formation | Reduce primer concentration to 0.1 µM; re-design primers |

See [PCR Troubleshooting Guide](../quality-control/pcr-troubleshooting.md) for a comprehensive troubleshooting reference.

---

## Cross-References

- [CHD PCR Protocol SOP](../quality-control/chd-pcr-protocol.md) — Full step-by-step PCR protocol for sexing
- [qPCR / Fluorescent PCR →](qPCR-fluorescent.md) — Real-time PCR methodology for quantification
- [Capillary Electrophoresis →](capillary-electrophoresis.md) — Post-PCR fragment analysis
- [Reagent Development →](reagent-development.md) — Self-developed master mixes and primers
- [PCR Troubleshooting Guide](../quality-control/pcr-troubleshooting.md) — Comprehensive issue resolution
- [DNA Extraction SOP](../quality-control/dna-extraction-sop.md) — Template preparation protocol

---

*This document describes SENO's conventional PCR methodology. For diagnostic qPCR protocols, see [qPCR / Fluorescent PCR →](qPCR-fluorescent.md). For protocol-specific SOPs, refer to the [Quality Control section](../quality-control/index.md). Questions about PCR optimization should be directed to rd@senobio.com.*
