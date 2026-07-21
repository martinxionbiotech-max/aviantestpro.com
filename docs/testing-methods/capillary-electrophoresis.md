---title: Capillary Electrophoresis
description: SENO's capillary electrophoresis technology for avian DNA fragment analysis — CHD sexing confirmation, microsatellite fingerprinting, allele calling, and high-throughput genotyping protocols.
canonical: https://aviantestpro.com/knowledge/testing-methods/capillary-electrophoresis
keywords: capillary electrophoresis, fragment analysis, DNA fingerprinting, microsatellite, allele calling, GeneMapper, CE instrumentation, avian genotyping
datePublished: 2025-01-15
dateModified: 2026-07-21---
canonical: https://aviantestpro.com/knowledge/testing-methods/capillary-electrophoresis


# Capillary Electrophoresis


## Overview

Capillary electrophoresis (CE) separates DNA fragments by size using an electric field within a narrow, liquid-filled capillary. Unlike traditional agarose gel electrophoresis — which separates fragments by migration through a porous gel matrix — CE passes fragments through a polymer-filled capillary while detecting fluorescently labeled molecules by laser-induced fluorescence as they pass a detection window.

CE provides base-pair resolution of DNA fragments, making it the method of choice for applications that require precise sizing: distinguishing CHD-Z and CHD-W amplicons that may differ by only 10–30 base pairs, and scoring microsatellite alleles for individual DNA fingerprinting and parentage verification.

SENO operates two CE instruments supporting high-throughput processing for sexing, fingerprinting, and research applications. CE analysis is performed on PCR products amplified using fluorescently labeled primers as described in our [PCR Technology](pcr-technology.md) section.

---

## Principle of Operation

CE separates DNA fragments based on their electrophoretic mobility through a sieving polymer. Smaller fragments migrate faster and reach the detector earlier. A laser excites fluorescent dyes attached to the labeled primers, and the emitted fluorescence is recorded by a CCD camera. An internal size standard (labeled with a spectrally distinct dye) is co-injected with each sample, enabling fragment sizing by interpolation.

| Component | Function |
|:----------|:---------|
| Capillary (36–50 cm length, 50 µm ID) | Separation channel filled with linear polymer matrix |
| Polymer matrix | Sieving medium — separates fragments by size |
| Running buffer | Provides electrical continuity (1× or 10× Genetic Analyzer Buffer) |
| Laser (488 nm / 514 nm) | Excites fluorescent dyes on labeled primers |
| CCD camera | Records fluorescence emission across multiple spectral channels |
| POP-4™ or POP-7™ polymer | Commercial sieving polymers optimized for different size ranges |

---

## Advantages Over Gel Electrophoresis

| Feature | Agarose Gel Electrophoresis | Capillary Electrophoresis |
|:--------|:---------------------------:|:-------------------------:|
| Resolution | ± 10–20 bp | ± 1–2 bp (single base pair) |
| Throughput | 20–50 samples per gel | 96–384 samples per run |
| Sample volume required | 8–10 µL PCR product | ~1 µL of diluted PCR product |
| Automation | Manual (gel pouring, loading, imaging) | Fully automated (plate loading → data export) |
| Data format | Image (gel photo) | Digital (electropherogram: peaks × sizes) |
| Quantification | Visual estimation (band intensity) | Precise (peak area, peak height, RFU) |
| Multiplex detection | Separate gels or co-migrating bands | Multi-color detection (4–6 dyes per capillary) |
| Reproducibility between runs | Moderate | High (± 0.5 bp sizing precision) |
| Hands-on time per 96 samples | ~45 min (gel prep + loading + imaging) | ~15 min (plate setup + instrument start) |
| Data export to LIMS | Manual (gel image annotation) | Automated (allele tables, peak lists) |

---

## SENO's CE Applications

### DNA Sexing Fragment Analysis

CE provides precise sizing of CHD-W and CHD-Z amplicons, resolving fragments that may appear as a single band on agarose gel. This is particularly valuable for species where the CHD-Z and CHD-W intron lengths are similar.

| Parameter | CE Sexing | Gel Sexing |
|:----------|:---------:|:----------:|
| Fragment size accuracy | ± 1 bp | ± 10–20 bp |
| Detection of small CHD-W/Z differences | Down to 5 bp difference | Typically needs ≥ 20 bp |
| Automated allele calling | Yes (GeneMapper) | No (manual band scoring) |
| Sample volume requirement | 1 µL of 1:20 dilution | 8 µL undiluted |
| Turnaround for 96 samples | ~3 hours (instrument) + 30 min (analysis) | ~2 hours (gel) + 30 min (imaging/analysis) |

In practice, CE is used as a confirmatory method for difficult sexing cases (where gel results are ambiguous) and as the primary method for species known to have small CHD intron length differences.

### DNA Fingerprinting (Microsatellite Genotyping)

DNA fingerprinting at SENO uses a panel of 12 microsatellite loci for individual identification and parentage verification. The discriminatory power of this panel is exceptionally high (DP > 0.9999).

| Locus | Repeat Motif | Size Range (bp) | Fluorescent Label | Alleles Observed | He (Expected) |
|:------|:-------------|:---------------:|:-----------------:|:----------------:|:-------------:|
| Pgi01 | (CA)₁₉ | 180–220 | FAM (blue) | 12 | 0.81 |
| Pgi02 | (GT)₂₃ | 140–180 | HEX (green) | 15 | 0.85 |
| Pgi03 | (CA)₁₅ | 200–240 | FAM (blue) | 10 | 0.78 |
| Pgi04 | (ATCT)₁₂ | 160–200 | TAMRA (yellow) | 8 | 0.72 |
| Pgi05 | (CA)₁₇ | 120–160 | FAM (blue) | 14 | 0.83 |
| Pgi06 | (GT)₁₈ | 220–260 | HEX (green) | 11 | 0.80 |
| Pgi07 | (CA)₂₁ | 170–210 | FAM (blue) | 13 | 0.82 |
| Pgi08 | (CA)₁₆ | 130–170 | TAMRA (yellow) | 10 | 0.77 |
| Pgi09 | (GT)₁₅ | 240–280 | HEX (green) | 9 | 0.75 |
| Pgi10 | (ATCT)₁₀ | 150–190 | FAM (blue) | 7 | 0.69 |
| Pgi11 | (CA)₁₄ | 280–320 | HEX (green) | 12 | 0.81 |
| Pgi12 | (GT)₂₀ | 190–230 | TAMRA (yellow) | 11 | 0.79 |

- **Combined Power of Discrimination (PD):** > 0.9999
- **Combined Exclusion Probability (PE, single parent):** > 0.999
- **Combined Exclusion Probability (PE, both parents):** > 0.99999

### Product Quality Verification

CE fragment analysis is used to confirm PCR product specificity:

| Purpose | PCR Product | CE Check | Outcome |
|:--------|:------------|:---------|:--------|
| Verify CHD amplicon sizes | Sexing PCR | Fragment sizing ± 1 bp | Confirms expected Z/W pattern |
| Check for primer-dimer | Any PCR | Peak < 80 bp confirmed as primer-dimer | Excluded from analysis |
| Confirm multiplex fidelity | Multiplex PCR | Expected peak pattern in each dye channel | All loci amplified |

---

## CE Workflow

| Step | Action | Responsible | Duration |
|:-----|:-------|:------------|:---------|
| 1 — PCR with labeled primers | Amplify targets using fluorescently labeled forward primers | Technician | 1.5–2 h |
| 2 — Post-PCR cleanup (optional) | Remove unincorporated primers and dNTPs | Technician | 15 min |
| 3 — Sample dilution | Dilute PCR product (1:10–1:40 in Hi-Di formamide) depending on yield | Technician | 5 min |
| 4 — Add internal size standard | Add GeneScan™ 500 LIZ™ or equivalent to each sample | Technician | 5 min |
| 5 — Denaturation | 95°C for 3 min, then snap-cool on ice | Technician | 5 min |
| 6 — Plate setup | Transfer samples to 96- or 384-well plate, seal with septa | Technician | 10 min |
| 7 — Instrument run | Load plate, select assay, start CE run | Technician | 25–60 min (per injection) |
| 8 — Data export | Automated size calling and allele detection software processes raw data | Software | 10–15 min |
| 9 — Manual review | Technician reviews electropherograms, adjusts bin assignments | Senior Tech | 15–30 min |
| 10 — LIMS upload | Final allele calls exported to LIMS for report generation | Software | 5 min |

---

## CE Instrumentation

SENO operates two capillary electrophoresis instruments for routine testing and R&D.

| Instrument | Capillary Count | Sample Capacity | Run Time (96 samples) | Applications |
|:-----------|:---------------:|:---------------:|:---------------------:|:-------------|
| Applied Biosystems 3500 Genetic Analyzer | 8 capillaries | 96-well plates | ~45 min | Sexing fragment analysis, fingerprinting |
| Applied Biosystems SeqStudio Flex | 4 capillaries | 96-well plates | ~60 min | Fingerprinting, research, validation |

Both instruments support multi-color detection (6-dye capability), automated polymer filling, and walk-away operation. Regular maintenance includes:

| Maintenance | Frequency | Action |
|:------------|:----------|:-------|
| Polymer replacement | Per run | Replace with fresh POP-4 or POP-7 |
| Buffer replacement | Per run | Fresh 1× running buffer |
| Capillary conditioning | Weekly | Conditioning run (polymer wash + electro-kinetic conditioning) |
| Capillary replacement | Every 1,500 injections or annually | When resolution degrades or signal intensity drops |
| Instrument calibration | Quarterly | Dye spectral calibration, size standard verification |
| Preventive maintenance | Bi-annual | Pump seal replacement, optical alignment check, fan filter cleaning |

---

## Quality Controls in CE

| Control | Content | Expected Result | Purpose |
|:--------|:--------|:----------------|:--------|
| Size standard | GS500 LIZ (35, 50, 75, 100, 139, 150, 160, 200, 250, 300, 340, 350, 400, 450, 490, 500 bp) | All peaks present, within ± 0.5 bp | Sizing accuracy |
| Positive control (known genotype) | Amplified DNA from reference individual | Expected allele sizes ± 1 bp | Assay setup verification |
| Negative control | Nuclease-free water through PCR | No peaks above threshold | Contamination detection |
| Allelic ladder | Pool of known alleles for each locus | All expected allele bins called | Sizing consistency across runs |
| Blank injection | Hi-Di formamide only | No peaks | Capillary cleanliness |

---

## Troubleshooting CE Issues

| Problem | Possible Cause | Solution |
|:--------|:---------------|:---------|
| No signal in any sample | Laser off, polymer not filled, injection failure | Check instrument status; re-run with fresh polymer |
| Weak signal (low RFU) | Insufficient PCR product, over-dilution | Reduce dilution (1:10 instead of 1:40); increase injection time |
| Split peaks / doublets | Salt in sample, incomplete denaturation | Add cleanup step; re-denature at 95°C for 3 min |
| Sizing off by > 1 bp | Degraded size standard, expired polymer | Replace size standard; use fresh polymer |
| Broad peaks | Old polymer, degraded capillary | Replace polymer; check capillary life count |
| Spikes in electropherogram | Air bubbles, impurities in polymer | Degas polymer; purge capillaries |
| Pull-up between dye channels | Saturated signal in one dye channel | Reduce injection time or dilute sample further |
| Late fragment pull (differential migration) | Overloaded sample | Dilute and re-inject at lower concentration |

---

## Cross-References

- [PCR Technology →](pcr-technology.md) — PCR amplification step before CE analysis
- [qPCR / Fluorescent PCR →](qPCR-fluorescent.md) — Alternative fluorescent detection method
- [Reagent Development →](reagent-development.md) — Fluorescent primer design and production
- [DNA Fingerprinting](/pigeon-genetics/dna-fingerprinting.md) — Microsatellite genotyping applications
- [Parentage Verification](/pigeon-genetics/parentage-verification.md) — CE-based parentage analysis
- [Laboratory Workflow](/quality-control/lab-workflow.md) — End-to-end sample processing pipeline
- [Accuracy Validation](/quality-control/accuracy-validation.md) — CE method performance data

---

## Frequently Asked Questions

**Q: Why use CE instead of agarose gel electrophoresis for sexing?**
A: CE provides single-base-pair resolution, enabling confident discrimination of CHD-Z and CHD-W fragments that differ by as few as 5–10 bp. Agarose gel can miss small differences, leading to incorrect sex assignment in species where CHD introns are nearly identical in length.

**Q: How many microsatellite loci does SENO use for fingerprinting?**
A: Our standard DNA fingerprinting panel includes 12 microsatellite loci, providing a combined power of discrimination exceeding 0.9999. This means the probability of two unrelated individuals sharing the same profile is less than 1 in 10,000.

**Q: What size standard does SENO use?**
A: We use GeneScan™ 500 LIZ™ (16 fragments from 35 to 500 bp) for most applications. For microsatellites with larger alleles (> 400 bp), we use GeneScan™ 600 LIZ™.

**Q: Can CE distinguish between same-sex siblings?**
A: Yes. While CHD sexing identifies the genetic sex, microsatellite fingerprinting by CE distinguishes individual identity regardless of sex. Same-sex siblings will have different microsatellite profiles (unless they are identical twins, which is extremely rare in birds).

**Q: How long does a CE run take?**
A: For the ABI 3500 (8 capillaries), a full 96-sample run takes approximately 45 minutes. For the SeqStudio Flex (4 capillaries), approximately 60 minutes. Total turnaround including plate preparation and data analysis is about 3–4 hours for 96 samples.

---

*This document describes SENO's capillary electrophoresis methodology and applications. For CE protocol SOPs, refer to the [Quality Control section](/quality-control/). For questions about fingerprinting applications, contact info@senobio.com.*
