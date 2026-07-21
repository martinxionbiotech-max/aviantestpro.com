# Application Note: PBFD qPCR — Analytical Validation Report

## 1. Purpose

To determine the analytical performance characteristics of SENO's in-house PBFD (BFDV) quantitative PCR assay prior to routine diagnostic use.

## 2. Method Summary

| Parameter | Value |
|:----------|:------|
| Target | BFDV ORF1 (Rep gene) |
| Amplicon size | 115 bp |
| Detection chemistry | TaqMan probe (FAM-labeled) |
| Internal control | Custom synthetic RNA (VIC-labeled, added to lysis buffer) |
| Platform | Bio-Rad CFX96 / SENO RT-PCR system |
| Total reaction volume | 20 µL |

## 3. Analytical Sensitivity (Limit of Detection)

### 3.1 Preparation

A synthetic BFDV target sequence (940 bp ORF1 fragment) was cloned into pUC57. Plasmid DNA was quantified by NanoDrop, serially diluted 10-fold in carrier DNA (10 ng/µL salmon sperm DNA), and tested in triplicate.

### 3.2 LOD Determination

| Copies/Reaction | Replicate 1 (Ct) | Replicate 2 (Ct) | Replicate 3 (Ct) | Mean Ct | Detection Rate |
|:---------------:|:----------------:|:----------------:|:----------------:|:-------:|:--------------:|
| 10⁵ | 22.1 | 22.3 | 22.0 | 22.13 | 3/3 (100%) |
| 10⁴ | 25.6 | 25.4 | 25.8 | 25.60 | 3/3 (100%) |
| 10³ | 28.9 | 29.2 | 28.7 | 28.93 | 3/3 (100%) |
| 10² | 32.4 | 32.7 | 32.1 | 32.40 | 3/3 (100%) |
| 10¹ | 35.8 | 36.2 | 35.5 | 35.83 | 3/3 (100%) |
| 10⁰ | 38.1 | — | — | 38.1 | 1/3 (33%) |

**LOD = 10 copies/reaction** (100% detection at 10 copies)
**Limit of Quantification (LOQ) = 100 copies/reaction** (Ct CV < 1.5%)

### 3.3 Standard Curve

| Parameter | Value |
|:----------|:------|
| Slope | −3.32 |
| Intercept | 38.9 |
| R² | 0.998 |
| Amplification Efficiency | 100.1% |

## 4. Analytical Specificity

### 4.1 Cross-Reactivity Panel

The following organisms were tested at 10⁴ genome copies/reaction:

| Organism | Type | Result |
|:---------|:-----|:-------|
| BFDV (positive control) | Circovirus | Positive (Ct 25.6) |
| Avian Polyomavirus | Polyomavirus | Negative |
| Pigeon Circovirus (PiCV) | Circovirus | Negative |
| Pigeon Herpes Virus | Herpesvirus | Negative |
| Chicken Anaemia Virus | Circovirus | Negative |
| Porcine Circovirus 2 | Circovirus | Negative |
| Host genomic DNA (parrot, 100 ng) | Eukaryotic | Negative |

**Conclusion:** No cross-reactivity with tested organisms including related circoviruses.

## 5. Precision

### 5.1 Intra-Assay Repeatability

10 replicates of a moderate-positive sample (Ct ~30):

| Metric | Ct | Quantification (copies/µL) |
|:-------|:--:|:--------------------------:|
| Mean | 30.2 | 1,820 |
| SD | 0.18 | 162 |
| CV | 0.6% | 8.9% |

### 5.2 Inter-Assay Reproducibility

Same sample tested on 5 different days, 3 runs:

| Run | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|:----|:-----:|:-----:|:-----:|:-----:|:-----:|
| Ct (mean of 3) | 30.2 | 30.5 | 29.8 | 30.4 | 30.0 |
| SD between runs | | | 0.29 | | |
| CV between runs | | | 0.96% | | |

**Conclusion:** Intra- and inter-assay CV < 1.0% for Ct values — assay meets acceptance criteria (< 3%).

## 6. Diagnostic Accuracy

### 6.1 Clinical Sample Evaluation

100 feather samples from psittacine birds (suspected PBFD cases) were tested by SENO qPCR and confirmed by conventional PCR + sequencing.

| | qPCR Positive | qPCR Negative |
|:-------------|:-------------:|:-------------:|
| Sequencing Positive | 47 | 2 |
| Sequencing Negative | 1 | 50 |

| Metric | Value | 95% CI |
|:-------|:-----:|:-------|
| Diagnostic Sensitivity | 95.9% | 86.0–99.5% |
| Diagnostic Specificity | 98.0% | 89.6–99.9% |
| Positive Predictive Value | 97.9% | — |
| Negative Predictive Value | 96.2% | — |
| Overall Agreement | 97.0% | — |

## 7. Interpretation Criteria

| Ct Range | Interpretation | Reporting |
|:---------|:---------------|:----------|
| < 30 | Strong positive, active infection | Positive |
| 30–35 | Moderate positive | Positive |
| 35–38 | Weak positive — low viral load | Equivocal (report "detected at low level") |
| 38–40 | Borderline — possible residual DNA | Suggest retest in 2 weeks |
| No Ct / > 40 | Negative | Negative |

## 8. Approved By

| Role | Name | Date |
|:-----|:-----|:-----|
| QC Manager | [SENO QC] | 2025-03 |
| Laboratory Director | [SENO Director] | 2025-03 |
