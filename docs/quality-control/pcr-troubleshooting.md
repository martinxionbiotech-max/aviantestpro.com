---
title: Troubleshooting Guide — Common PCR & DNA Testing Issues for Avian Samples
description: Comprehensive troubleshooting guide for avian PCR and DNA testing, covering DNA extraction issues, PCR amplification failures, weak bands, non-specific amplification, contamination, sex determination ambiguity, and qPCR-specific problems with detailed symptom-cause-solution tables.
canonical: https://aviantestpro.com/knowledge/quality-control/pcr-troubleshooting
keywords: PCR troubleshooting, DNA extraction troubleshooting, PCR failure, PCR contamination, weak PCR bands, non-specific PCR bands, qPCR troubleshooting, melt curve analysis, PCR inhibitors, no amplification, PCR troubleshooting guide, avian DNA testing issues, feather DNA problems, RT-PCR troubleshooting, TaqMan probe troubleshooting
datePublished: 2025-01-15
dateModified: 2026-07-21
---
canonical: https://aviantestpro.com/knowledge/quality-control/pcr-troubleshooting


# Troubleshooting Guide: Common PCR & DNA Testing Issues


## Introduction

This guide addresses the most frequently encountered issues in avian molecular diagnostics at SENO. Problems are organized by workflow stage — extraction, PCR amplification, sex determination, and qPCR — with systematic symptom-cause-solution tables. Always follow the checklist order from simplest to most complex intervention.

---

## 1. DNA Extraction Issues

### 1.1 Low DNA Yield

| Symptom | Check | Solution |
|:--------|:------|:---------|
| A₂₆₀ < 0.1 (≈ < 5 ng/µL) | Sample age — was feather freshly plucked? | If shed feathers → request fresh plucked sample with intact follicles |
| | Follicle count — are visible bulbs present? | Minimum 3–5; if small bird (canary, finch) → use 5–7 |
| | Lysis time — was incubation ≥ 30 min at 56°C? | Extend to 45–60 min; vortex every 10 min |
| | Elution — did you re-apply eluate to membrane? | Perform repeat elution step (adds ~15% yield) |
| | Proteinase K activity | Check expiry; activity declines after 6 months at −20°C |
| | Elution buffer temperature | Pre-warm to 56°C for 15–30% yield improvement |

**Quick Checklist for Low-Yield Samples:**
- [ ] Follicle visible at feather base? (If not → discard, use another feather)
- [ ] Sample collected within last 30 days?
- [ ] Stored at room temperature in paper envelope? (Plastic causes condensation and mold)
- [ ] Proteinase K fresh? (Activity declines after 6 months at −20°C)
- [ ] Wash Buffer 2 ethanol content ≥ 80%? (Evaporation concentrates ethanol, reducing wash efficacy)

### 1.2 DNA Degradation (No High-MW Band on Gel)

| Cause | Prevention | Remedial Action |
|:------|:-----------|:----------------|
| Extended room-temperature storage > 60 days | Extract within 4 weeks of collection | Cannot recover degraded DNA; request fresh sample |
| Freeze-thaw cycles of extracted DNA | Aliquot DNA; freeze only once; store at 4°C for short-term (≤ 1 month) | Discard aliquot; use fresh aliquot |
| Bacterial/fungal growth on sample (visible mold or discoloration) | Store in paper envelope, not plastic; keep dry; silica gel desiccant for humid climates | Cannot salvage; discard; request re-collection |
| DNase contamination during extraction | Use filtered tips; wipe surfaces with 10% bleach + 70% ethanol; change gloves frequently | Re-extract from original sample if available |
| Excessive vortexing of extracted DNA | Reduce vortex speed; use gentle inversion for resuspension | May still amplify short targets; test with PCR |

### 1.3 A₂₆₀/A₂₈₀ Outside Acceptable Range

| Reading | Implication | Action |
|:--------|:------------|:-------|
| < 1.6 | Protein contamination | Repeat wash (Wash Buffer 1 + Wash Buffer 2) on column; or re-digest with additional Proteinase K |
| > 2.0 | RNA contamination | Add 1 µL RNase A (10 mg/mL), incubate 37°C for 10 min, then re-purify |
| 1.6–1.7 | Mild protein carryover | May still amplify; proceed with PCR, note in QC log |
| 1.8–2.0 | Ideal purity range | Proceed with downstream applications |

### 1.4 A₂₆₀/A₂₃₀ Outside Acceptable Range

| Reading | Implication | Action |
|:--------|:------------|:-------|
| < 1.2 | Severe guanidine or organic carryover | Ethanol precipitation or re-purify on fresh column |
| 1.2–1.5 | Moderate carryover | Dilute PCR template 1:5 or 1:10 to reduce inhibitor concentration |
| ≥ 1.5 | Acceptable | Proceed |

---

## 2. PCR Amplification Issues

### 2.1 Complete PCR Failure (No Bands, Including Positive Controls)

| Possible Cause | Test | Fix |
|:---------------|:-----|:-----|
| Thermocycler malfunction | Run temperature verification plate; check block uniformity | Service thermocycler; use alternate instrument |
| Master mix degradation | Check expiry date; verify storage at −20°C | Use fresh master mix from unopened aliquot |
| Primer degradation | Run 5 µL primer on agarose gel (should see band at ~20–25 bp) | Re-synthesize primers; order new aliquot |
| Pipetting error — missing component | Re-check volumes; pipette should be calibrated quarterly | Reprepare master mix carefully |
| Improper cycling program | Verify program loaded correctly (check temperatures and cycles) | Re-load correct program |
| Lid not heating properly | Check lid temperature setting (should be 105°C for 0.2 mL tubes) | Replace lid heating pad |

### 2.2 Sample-Specific Failure (Controls Work, Sample Doesn't)

| Cause | Frequency | Test | Solution |
|:------|:---------:|:-----|:---------|
| PCR inhibitors in DNA | Common (15–20% of feather samples) | Run 1:10 and 1:50 dilution of DNA; if dilutions amplify → inhibition confirmed | Use 1 µL template instead of 2 µL; or re-purify with ethanol precipitation |
| No DNA in sample (empty follicle) | Common | Re-extract fresh feather; verify follicle presence under magnification | Must have visible white bulb at feather base |
| Species incompatibility with P2/P8 primers | Rare (specific species groups) | Try 2550F/2718R primer set | Refer to CHD PCR Protocol § 5.2 for species table |
| Too much DNA (> 200 ng/reaction) | Occasional | Dilute DNA 1:5; excess DNA (> 200 ng) inhibits PCR | Use 1 µL of 1:5 dilution |
| Degraded DNA | Occasional with old samples | Run on gel to check integrity | Request fresh sample |

### 2.3 Weak Bands or High Ct Values

| Symptom | Likely | Action |
|:--------|:-------|:-------|
| Ct 32–35 on healthy bird (qPCR) | Low viral load | Report positive if Ct < 38 with good amplification curve and sigmoidal shape |
| Ct increases on repeat testing | Sample degradation (DNA/RNA breakdown) | Request fresh sample; store swabs in stabilization solution |
| Band visible but faint on gel (conventional PCR) | Low PCR product | Increase cycles to 38 (from 35); increase template to 4 µL |
| Band visible but faint | Poor primer binding (mismatch) | Decrease annealing temp to 48°C; or design species-specific primers |
| Band appears at correct size but very faint | Suboptimal Mg²⁺ concentration | Increase MgCl₂ to 2.5–3.0 mM in final reaction |
| Faint band with tailing | Template excess or degradation | Reduce template to 1 µL; check integrity on gel |

### 2.4 Non-Specific Bands or Multiple Bands

| Cause | Check | Fix |
|:------|:------|:-----|
| Annealing temperature too low | Thermocycler accuracy verified? | Increase from 50°C to 52–53°C |
| Too many cycles | Cycle count in program | Reduce from 35 to 30 cycles |
| Too much template | DNA concentration measured? | Dilute to 10–20 ng/µL (0.5–1 µL/reaction) |
| Primer-dimer | Check 3' complementarity of primers | Increase annealing temp; reduce primer concentration to 0.1 µM |
| Contamination | NTC shows bands | Decontaminate workstation; fresh reagents; UV treat hood |
| GC-rich template producing secondary structures | Check template %GC | Add 5% DMSO or 1 M betaine to reaction |
| Old Taq polymerase with reduced specificity | Taq age and storage | Use fresh enzyme; switch to hot-start Taq |

### 2.5 Contamination (Bands in No-Template Control)

| Type | Source | Solution |
|:-----|:-------|:---------|
| Carryover contamination | Previous PCR product aerosolized | Physical separation of pre-PCR and post-PCR areas (dedicated rooms if possible) |
| | Same pipette used for pre- and post-PCR handling | Dedicated pipette sets per area; color-coded |
| | Pipette aerosol reaching barrel | Filter tips exclusively; no exceptions |
| Genomic contamination | Reagent contamination | Aliquot all reagents; discard contaminated aliquot |
| | Contaminated water | Use fresh nuclease-free water from sealed bottle |
| | Sample-to-sample during DNA extraction | Change gloves between samples; open tubes one at a time |
| Environmental contamination | Amplicon on surfaces, lab coats, equipment | Decontaminate with 10% bleach (10 min contact); UV irradiation (30 min); regular surface swab monitoring |

### Decontamination Protocol for Carryover

| Method | Application | Effectiveness |
|:-------|:------------|:--------------|
| 10% sodium hypochlorite (bleach) | Surfaces, pipettes (external), floors | Excellent — destroys DNA by oxidation |
| UV irradiation (254 nm, 30 min) | Open workstations, PCR cabinets, laminar flow hoods | Good — but does not penetrate debris |
| 70% ethanol | Non-porous surfaces | Moderate — sanitizes but does not degrade DNA |
| Commercial DNA decontamination solutions (e.g., DNA Away, DNA Erase) | Surfaces, equipment | Good — follow manufacturer contact time |
| HCl-based decontamination | Glassware | Excellent — but corrosive |

---

## 3. Sex Determination Ambiguity

### 3.1 Single Band But Expected Double (Suspected Female)

| Species | Known Issue | Solution |
|:--------|:------------|:---------|
| Eclectus Parrot | CHD-Z and CHD-W frequently co-migrate on 2.5% agarose | Use 2550F/2718R primers (larger amplicon, better resolution) |
| Cockatiel | Intron size variation reported; some individuals show < 10 bp difference | Confirm with alternate primer set or capillary electrophoresis |
| Budgerigar | Small size difference (8–12 bp between Z and W fragments) | Use 3.5% agarose gel run at 80 V for 60 min; or capillary electrophoresis |
| Pigeon | Generally resolves well; Z and W differ by ~25 bp | If single band → male; if ambiguous → re-run on CE |
| Lovebird (Agapornis) | Some species have < 15 bp difference | Use 2550F/2718R set; if still ambiguous → sequence |
| Macaw (Ara spp.) | Generally clean resolution on 2.5% agarose | Standard protocol sufficient |

### 3.2 Three or More Bands

| Cause | Frequency | Resolution |
|:------|:---------:|:-----------|
| Mixed sample (two birds' DNA) | Common with shared swabs or nest samples | Confirm with client; request single-bird samples; repeat with fresh individual samples |
| Non-specific amplification | Occasional (low-stringency conditions) | Re-PCR with touch-down protocol (65→50°C, −1°C/cycle); increase annealing temp |
| Primer-dimer artifact | Common at low template concentrations | Run gel longer (60 min); primer-dimer runs at < 100 bp, well below target bands |
| Heteroduplex formation | Occasional (two different CHD alleles in female) | Re-run on higher-resolution gel (3% agarose at 60 V overnight); heteroduplex bands appear between target bands |
| Cross-contamination during gel loading | Rare | Check loading order; repeat PCR from original template |

### 3.3 No Bands (Sample with Known Sex — Troubleshooting)

| Scenario | Check | Action |
|:---------|:------|:-------|
| DNA passes QC (good A₂₆₀/A₂₈₀, visible on gel) but PCR fails | PCR inhibitor present | 1:10 dilution of DNA; retest |
| | Primer mismatch for species | Check species compatibility table; use 2550F/2718R |
| DNA fails QC | Extraction issue | Re-extract with fresh feather sample |

---

## 4. qPCR-Specific Issues

### 4.1 Poor Amplification Curves

| Curve Shape | Cause | Fix |
|:------------|:------|:-----|
| Flat line (no signal, no rise by cycle 45) | No target present OR failed reaction | Check all controls; verify probe not degraded; confirm baseline subtraction settings |
| Late rise with low plateau (ΔRn < 0.5) | Low target concentration or partial inhibition | Dilute sample 1:5 and re-run; spike with positive control to confirm no inhibition |
| Early rise in all wells including NTC (Ct < 30 in NTC) | Probe degradation releasing free fluorophore | Use fresh probe aliquot; store probes in dark at −20°C |
| Erratic baseline with fluctuations | Air bubble in well | Re-spin plate (2,000 × g, 2 min) before running; ensure optical seal fully adhered |
| Curves shift right on repeats | Sample degradation over time or pipetting inconsistency | Aliquot sample once; use fresh aliquot for repeat |
| No plateau at high cycles | Suboptimal reaction efficiency | Check primer design; verify probe Tm (should be 8–10°C above primer Tm) |
| Double sigmoid curve | Two amplification targets or probe binding to two sites | Check probe specificity in silico; run melt curve (for SYBR) or gel |

### 4.2 Melt Curve Issues (SYBR Green Assays)

| Melt Peak Pattern | Interpretation | Action |
|:------------------|:---------------|:-------|
| Single sharp peak at expected Tm (~78°C for CHD amplicons) | Specific amplification ✓ | No action needed |
| Single sharp peak at unexpected Tm (e.g., 82°C vs 78°C) | Non-specific product or primer-dimer | Check by gel electrophoresis; redesign primers if needed |
| Two distinct peaks | Two products present (possible CHD-W + CHD-Z in females — expected) | Confirm with gel: two bands at expected sizes = correct |
| Broad peak (Tm range > 2°C) | Heterogeneous product; possible mispriming or degraded template | Reduce annealing temp; use fresh template |
| No peak (flat line, no melt transition) | No amplification | Check amplification curves; verify template, primers, and master mix |
| Multiple small peaks < 75°C | Primer-dimer (common at low template) | Increase template; reduce primer concentration; use hot-start Taq |
| Peak at low Tm with additional peaks at expected Tm | Primer-dimer + specific product | Run gel to confirm both present; reduce primer concentration |

### 4.3 Standard Curve and Efficiency Issues

| Problem | Indication | Fix |
|:--------|:-----------|:-----|
| Slope outside −3.1 to −3.6 (90–110% efficiency) | Suboptimal reaction | Redesign primers; optimize Mg²⁺ concentration; check for inhibitors in standard dilutions |
| R² < 0.98 | Poor pipetting accuracy in dilution series | Use fresh standard; prepare dilutions with calibrated pipettes; vortex each dilution |
| Non-linear standard curve | Standard degradation or dilution error | Prepare new standard from fresh plasmid; verify concentration by spectrophotometry |
| Low endpoint fluorescence (plateau) | Probe or SYBR concentration too low | Increase probe to 0.3 µM or SYBR to 1× final |

### 4.4 Multiplex qPCR Issues

| Problem | Cause | Solution |
|:--------|:-------|:---------|
| One channel fails but others work | Probe degradation in that channel | Replace probe; store all probes protected from light |
| Channel cross-talk (FAM signal bleeding into VIC) | Inadequate spectral compensation | Run single-channel controls for spectral calibration |
| Competition between assays | Overlapping targets at high concentration | Reduce template; or use separate reactions for high-abundance targets |
| One assay has higher Ct than expected in multiplex | Competitive inhibition | Reduce primer concentration for dominant assay; optimize primer ratio |

---

## Cross-References

- [DNA Extraction SOP](/quality-control/dna-extraction-sop/) — Pre-PCR sample processing protocol
- [CHD PCR Protocol](/quality-control/chd-pcr-protocol/) — Standard PCR conditions for avian sexing
- [Accuracy Validation](/quality-control/accuracy-validation/) — Assay validation parameters
- [Pigeon Disease Panel](/disease-testing/pigeon-disease-panel/) — Multiplex PCR target information

---

*This document is maintained by SENO's R&D and Quality teams. For unresolved issues, contact lab.support@senobio.com.*
