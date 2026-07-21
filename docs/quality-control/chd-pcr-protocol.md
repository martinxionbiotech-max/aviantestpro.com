---
title: Laboratory SOP — CHD Gene PCR Amplification for Avian Sex Determination
description: Standard operating procedure for PCR amplification of CHD-W and CHD-Z genes from avian genomic DNA for gender identification. Covers primers, reaction mix, thermal cycling protocol, gel electrophoresis, interpretation, quality controls, and troubleshooting.
canonical: https://aviantestpro.com/knowledge/quality-control/chd-pcr-protocol
keywords: CHD PCR, avian sexing, bird DNA sexing, P2 P8 primers, CHD-W, CHD-Z, ZW system, PCR sex determination, bird gender test, gel electrophoresis, agarose gel sexing, PCR protocol, molecular sexing, Z chromosome, W chromosome
datePublished: 2025-01-15
dateModified: 2026-07-21
---
canonical: https://aviantestpro.com/knowledge/quality-control/chd-pcr-protocol


# Laboratory SOP: CHD Gene PCR Amplification for Avian Sex Determination


## 1. Scope

This SOP describes PCR amplification of the CHD-W and CHD-Z genes from extracted avian genomic DNA for gender identification. This protocol applies to all avian species with defined ZW sex chromosome systems, encompassing psittacines (parrots), columbids (pigeons), passerines (songbirds), galliformes (poultry), anseriformes (waterfowl), and falconiformes (raptors). The SOP is to be used by trained laboratory personnel in SENO's molecular diagnostics facility.

## 2. Principle

Conserved primers (P2/P8) flank an intron within the CHD (Chromodomain Helicase DNA-binding) gene. Male birds (ZZ) possess two copies of the CHD-Z gene and produce a single PCR fragment. Female birds (ZW) possess one copy each of CHD-Z and CHD-W, producing two fragments of different sizes due to intron length variation between the two sex chromosomes. The size difference varies by species, ranging from 8–15 bp in some small passerines to 50–100 bp in most psittacines and columbids.

## 3. Reagents & Materials

| Item | Specification | Storage | Supplier |
|:-----|:--------------|:--------|:---------|
| PCR Master Mix (2×) | 0.1 U/µL Taq, 4 mM MgCl₂, 0.4 mM dNTPs | −20°C | SENO Reagent |
| Forward Primer (P2) | 5'-TCTGCATCGCTAAATCCTTT-3', 10 µM | −20°C | Synthesized |
| Reverse Primer (P8) | 5'-CTCCCAAGGATGAGRAAYTG-3', 10 µM | −20°C | Synthesized |
| Nuclease-Free Water | DNase/RNase-free, 0.22 µm filtered | Room temp | Commercial |
| DNA Template | Extracted genomic DNA (10–50 ng) | 4°C or −20°C | From extraction |
| Positive Controls | Male (ZZ) and female (ZW) reference DNA | −20°C | SENO Reference |
| No-Template Control (NTC) | Nuclease-free water | Room temp | — |
| Agarose | Molecular biology grade | Room temp | Commercial |
| 6× Loading Dye | Contains bromophenol blue, xylene cyanol, glycerol | 4°C | Commercial |
| 100 bp DNA Ladder | 100–1,000 bp range, ready-to-use | 4°C | Commercial |
| GelRed or SYBR Safe | 10,000× concentrate, light-sensitive | Room temp, dark | Commercial |
| TAE Buffer (50×) | 2 M Tris, 1 M acetate, 50 mM EDTA, pH 8.0 | Room temp | SENO Reagent |

### Alternate Primer Set

| Primer | Sequence (5' → 3') | Target | Use Case |
|:-------|:-------------------|:-------|:---------|
| 2550F | GTTACTGATTCGTCTACGAGA | CHD-Z + CHD-W | Species with co-migrating P2/P8 bands |
| 2718R | ATTGAAATGATCCAGTGCTTG | CHD-Z + CHD-W | Same as above |
| 1237L | GAGAAACTGTGCAAAACAG | CHD-W only | Female-specific confirmation |
| 1272H | TCCAAGAATCTCTTTGTTG | CHD-Z only | Male confirmation |

## 4. PCR Setup

### 4.1 Reaction Mix Preparation (per 25 µL reaction)

| Component | Volume (µL) | Final Concentration | Notes |
|:----------|:-----------:|:--------------------|:------|
| 2× PCR Master Mix | 12.5 | 1× | Contains Taq, dNTPs, MgCl₂, buffer |
| P2 Primer (10 µM) | 0.5 | 0.2 µM | Forward |
| P8 Primer (10 µM) | 0.5 | 0.2 µM | Reverse |
| DNA Template | 2.0 | 10–50 ng | Pipette carefully; avoid cross-contamination |
| Nuclease-Free Water | 9.5 | — | Adjust if template volume changes |
| **Total** | **25.0** | — | — |

### 4.2 Master Mix Preparation

1. Calculate total reactions needed (samples + controls + 10% overage for pipetting loss)
2. Prepare master mix in a 1.5 mL microcentrifuge tube on ice: order = water → buffer → primers
3. Vortex gently (5 s, low speed to avoid foaming), spin down (5 s in mini-centrifuge)
4. Dispense 23 µL per PCR tube (use fresh pipette tip for each tube)
5. Add 2 µL template DNA to each tube (cap closed before moving to next sample)
6. Add 2 µL nuclease-free water to NTC tube
7. Close all caps firmly, spin down briefly (1,000 × g, 10 s at 4°C)

### 4.3 Thermal Cycling Protocol

| Step | Temperature | Time | Cycles | Notes |
|:-----|:-----------:|:----:|:------:|:------|
| Initial Denaturation | 94°C | 3 min | 1 | Ensures complete genomic DNA denaturation |
| Denaturation | 94°C | 30 s | | Standard denaturation |
| Annealing | 50°C | 45 s | 35× | Temperature may be optimized per species (48–55°C) |
| Extension | 72°C | 45 s | | 1 min/kb for amplicons > 600 bp (2550F/2718R set) |
| Final Extension | 72°C | 5 min | 1 | Complete partial extension products |
| Hold | 4°C | ∞ | — | Light-sensitive; protect from prolonged UV if using SYBR |

### 4.4 Touch-Down PCR (for Difficult Samples or Ambiguous Results)

| Step | Temperature | Time | Cycles |
|:-----|:-----------:|:----:|:------:|
| Initial Denaturation | 94°C | 3 min | 1× |
| Touch-down Denaturation | 94°C | 30 s | |
| Touch-down Annealing | 65 → 50°C (−1°C/cycle) | 45 s | 15× (decreasing 1°C/cycle) |
| Touch-down Extension | 72°C | 45 s | |
| Standard cycles | 94°C / 50°C / 72°C | 30 s / 45 s / 45 s | 20× |
| Final Extension | 72°C | 5 min | 1× |

### 4.5 Thermocycler Setup

| Parameter | Setting |
|:----------|:--------|
| Lid temperature | 105°C |
| Ramp rate | 3°C/s (default; reduce to 2°C/s for difficult GC-rich templates) |
| Volume | 25 µL |
| Tube type | 0.2 mL thin-wall PCR strip or plate |
| Reaction cover | Optical seal or pressure caps |

## 5. Post-PCR Analysis

### 5.1 Agarose Gel Electrophoresis

| Parameter | Specification | Alternative |
|:----------|:--------------|:------------|
| Gel type | 2.5% agarose in 1× TAE | 3.0–3.5% for species with < 15 bp difference |
| Stain | GelRed (1×) or SYBR Safe (1×) | Ethidium bromide (0.5 µg/mL) — with appropriate safety controls |
| Voltage | 120 V (constant) | 80–100 V for better resolution of small differences |
| Run time | 40 min | 50–60 min for higher resolution |
| Ladder | 100 bp DNA ladder (5 µL) | Low-molecular-weight ladder for < 15 bp resolution |
| Sample loading | 8 µL PCR product + 2 µL 6× loading dye | 10 µL total per well |

### 5.2 Expected Fragment Sizes

| Primer Set | CHD-Z (male) | CHD-W (female) | Size Difference | Species Examples |
|:-----------|:------------:|:--------------:|:---------------:|:-----------------|
| P2/P8 | ~350–400 bp | ~380–450 bp | 20–60 bp | Most psittacines, pigeons, falcons |
| 2550F/2718R | ~600–650 bp | ~650–700 bp | 15–50 bp | Psittacines with small P2/P8 difference |
| P2/1272H | ~350–400 bp | — (no binding) | N/A | Male-only confirmation |
| 1237L/P8 | — (no binding) | ~350–400 bp | N/A | Female-only confirmation |

### 5.3 Interpretation

| Gel Pattern | Result | Confidence | Action if Uncertain |
|:------------|:-------|:-----------|:--------------------|
| Single band (~350–400 bp) | Male (ZZ) | High | Confirm with alternate primer set if species is known to have small size difference |
| Two bands (~350 + ~400 bp) | Female (ZW) | High | Both bands should be of similar intensity |
| Faint single band | Male (low DNA) | Moderate | Repeat with increased template (4 µL) or re-extract |
| Single band, suspected female | Ambiguous | Low | Use 2550F/2718R primers or capillary electrophoresis |
| Smear or multiple bands > 5 | Non-specific amplification | Low | Repeat with touch-down protocol; increase annealing temp to 53°C |
| No band | PCR failure | N/A | Check DNA extraction quality; repeat protocol |
| Three or more distinct bands | Mixed sample or contamination | Low | Confirm sample source; request single-bird re-collection |

## 6. Quality Controls

| Control | Expected Result | Failure Action | Documentation |
|:--------|:---------------|:---------------|:--------------|
| Female positive (ZW) | Two bands (CHD-Z + CHD-W) | Troubleshoot master mix, primers, or thermocycler | Record in QC log |
| Male positive (ZZ) | One band (CHD-Z) | Troubleshoot master mix, primers, or thermocycler | Record in QC log |
| NTC (water) | No band | Repeat with fresh reagents; UV-decontaminate workstation | Incident report if recurring |
| Internal extraction control (IAC) | Positive amplification | If negative: check extraction SOP compliance | Re-extraction record |

## 7. Troubleshooting

| Problem | Possible Cause | Solution | Source (See) |
|:--------|:---------------|:---------|:-------------|
| No amplification in any sample | Taq polymerase inactive | Check expiry; repeat with fresh master mix | PCR Troubleshooting § 2.1 |
| No amplification in NTC but samples have single band | Contamination in template | Re-extract; check extraction reagents | PCR Troubleshooting § 2.2 |
| Weak bands | Low DNA template | Re-PCR with 4 µL template or re-extract | PCR Troubleshooting § 2.3 |
| Smearing across lane | DNA degradation | Re-collect fresh sample | PCR Troubleshooting § 1.2 |
| Female appears as single band | CHD-W/CHD-Z same size (species-specific) | Use 2550F/2718R primers | PCR Troubleshooting § 3.1 |
| Bands present in NTC | Amplicon carryover | UV-decontaminate workstation; fresh reagents; separate pre/post-PCR areas | PCR Troubleshooting § 2.5 |
| Extra bands in some samples | Mixed sample (two birds) | Confirm with client; request single-bird samples | PCR Troubleshooting § 3.2 |
| Ghost ladder in gel | Old TAE buffer | Prepare fresh 1× TAE buffer | — |

## 8. Documentation and Records

| Record | Retention | Format |
|:-------|:----------|:-------|
| PCR setup sheet | 3 years | Laboratory notebook or LIMS |
| Gel image | 3 years | Electronic (JPEG/TIFF) + print |
| QC control sheet | 3 years | LIMS or PDF |
| Result report | 10 years (per CLIA) | Signed PDF in LIMS |
| Troubleshooting log | 3 years | LIMS incident tracking |

## Cross-References

- [DNA Extraction SOP](/quality-control/dna-extraction-sop/) — Pre-PCR sample processing
- [PCR Troubleshooting](/quality-control/pcr-troubleshooting/) — Amplification failure resolution
- [Accuracy Validation](/quality-control/accuracy-validation/) — Assay validation data
- [Glossary](/glossary/) — Key terms (CHD, ZW, amplicon, etc.)

---

*This SOP is a controlled document. Unauthorized modification is prohibited. For protocol revisions, contact quality@senobio.com.*
