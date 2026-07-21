# Laboratory Workflow: Sample Reception to Final Report

## Overview

This document describes the end-to-end workflow for processing avian genetic testing samples at SENO's laboratory, from sample reception through to final report delivery.

## Workflow Diagram

```
Sample Receipt → Registration → Inspection → DNA Extraction
                                                  ↓
                                            PCR/qPCR Setup
                                                  ↓
                                            Amplification
                                                  ↓
                                          Post-PCR Analysis
                                                  ↓
                                          Result Interpretation
                                                  ↓
                                               QC Review
                                                  ↓
                                              Reporting
```

## Step 1: Sample Reception

### 1.1 Physical Receipt

| Task | Responsible | Action |
|:-----|:------------|:-------|
| Package inspection | Receiving clerk | Check for leakage, damage, temperature (if cold pack required) |
| Documentation check | Receiving clerk | Verify submission form: species, test type, client ID, number of samples |
| Photo documentation | Receiving clerk | Photograph package condition (for customs claims if needed) |
| Chain of custody | Receiving clerk | Sign and date receipt; scan into LIMS |

### 1.2 Sample Acceptance Criteria

| Sample Type | Accept | Reject (with notification) |
|:------------|:-------|:---------------------------|
| Feathers | Freshly plucked, follicle intact, 3–5 per bird | Shed feathers, no visible follicle, < 2 feathers |
| Swabs | In stabilization solution, sealed tube | Leaking, dry swab without solution, expired stabilizer |
| Blood (EDTA) | 0.1–0.5 mL, not hemolyzed | Clotted, hemolyzed, > 14 days at room temp |
| Blood (FTA card) | Visible blood spot, dry | No visible spot, still moist (mold risk) |

## Step 2: Registration & Labeling

| Task | Detail |
|:-----|:-------|
| Create case in LIMS | Each client = 1 case; each bird = 1 sample entry |
| Assign sample ID | Format: SENO-YYYYMMDD-NNNN (date + sequential) |
| Barcode generation | 2D barcode printed and affixed to primary tube |
| Scan linkage | Barcode linked to client ID, species, test type in LIMS |
| Batch assignment | Grouped by test type and extraction method |

## Step 3: Sample Inspection

### 3.1 Laboratory Inspection

| Test | Method | Record |
|:-----|:-------|:-------|
| Feather follicle check | Magnifying lamp (10×) | 5-point scale: 0=no follicle → 5=excellent |
| Swab condition | Visual | Normal / dried / leaking / contaminated |
| Blood quality | Visual | Normal / hemolyzed / clotted / insufficient |

### 3.2 Chain of Custody Continuation

Each transfer between technicians is logged: time, technician ID, sample count.

## Step 4: DNA Extraction

See [DNA Extraction SOP](dna-extraction-sop.md) for detailed protocol.

### 4.1 Batch Processing

| Parameter | Specification |
|:----------|:--------------|
| Batch size | 48 samples + 2 controls (1 extraction positive, 1 extraction blank) |
| Extraction positive | Known female parrot feather (ZW) |
| Extraction blank | Lysis buffer only (no sample) |
| Time per batch | ~45 min hands-on + 30 min incubation |

### 4.2 Post-Extraction QC

| Test | Criteria | Action if Fail |
|:-----|:---------|:---------------|
| NanoDrop concentration | > 5 ng/µL | Re-extract with additional feathers |
| A260/280 ratio | 1.7–2.0 | Re-purify if < 1.6; check if > 2.1 |
| A260/230 ratio | > 1.5 | Re-purify if < 1.2 |
| Extraction blank | No DNA by NanoDrop | If DNA detected: batch contamination investigation |

## Step 5: PCR/qPCR Setup

### 5.1 Pre-PCR Preparation

- All work performed in **Class 1,000 pre-PCR room**
- Dedicated PCR pipettes (filter tips only)
- UV-decontaminated workstation (30 min before use)
- Reagents thawed on ice, vortexed 5 s, spun 10 s

### 5.2 Plate Layout

| Row | Content | Purpose |
|:---:|:--------|:--------|
| A1–H1 | Positive controls (duplicate) | Assay validation |
| A2–H2 | Negative control (triplicate) | Contamination check |
| A3–H3 | No-template control (triplicate) | Reagent purity |
| A4–H12 | Samples (single if sexing, duplicate if qPCR) | Test subjects |
| H11–H12 | Extraction blank | Extraction quality |

### 5.3 Thermal Cycling

See specific protocol:
- **Sexing:** [CHD PCR Protocol](chd-pcr-protocol.md)
- **Disease:** [PBFD qPCR Validation](pbfd-qpcr-validation.md) or panel-specific protocol

## Step 6: Post-PCR Analysis

### 6.1 Sexing — Gel Electrophoresis

| Task | Detail |
|:-----|:-------|
| Gel documentation | UV transilluminator + digital image capture |
| Band sizing | Compare to 100 bp ladder using gel analysis software |
| Result entry | Male/Female/Inconclusive entered into LIMS |
| Image storage | Gel image filed with LIMS record |

### 6.2 Disease — qPCR Analysis

| Task | Detail |
|:-----|:-------|
| Baseline correction | Auto baseline (3–15 cycles) with manual override if needed |
| Threshold setting | 10× SD of baseline fluorescence (or manual: 0.1 RFU) |
| Ct value extraction | Export to LIMS via automated data interface |
| Amplification curve review | Manual review of all curves for artifacts |

### 6.3 DNA Fingerprinting — Capillary Electrophoresis

| Task | Detail |
|:-----|:-------|
| Fragment analysis | GeneMapper or equivalent software |
| Allele calling | Automated with manual bin review |
| Profile export | Tab-delimited file for LIMS import |

## Step 7: Result Interpretation

### 7.1 Automated Rules (LIMS)

| Rule | Condition | Action |
|:-----|:----------|:-------|
| Sexing — two bands | CHD-W + CHD-Z detected | Auto-assign "Female" |
| Sexing — one band | CHD-Z only detected | Auto-assign "Male" |
| Sexing — no band | No PCR product | Auto-assign "Inconclusive — re-extract" |
| qPCR — Ct < 38 | Target detected | Auto-assign "Positive" |
| qPCR — Ct 38–40 | Target detected at low level | Auto-assign "Weak positive — retest recommended" |
| qPCR — no Ct | No target | Auto-assign "Negative" |

### 7.2 Manual Review (Technician)

- All "Inconclusive" results reviewed by senior technician
- All "Weak positive" results reviewed by QC officer
- Discordant duplicates (sexing: male/female from same sample) → repeat with alternate primers
- Fingerprinting profiles with < 10/12 loci called → re-run

## Step 8: QC Review

### 8.1 Batch QC Review

| QC Element | Acceptance Criteria |
|:-----------|:--------------------|
| Positive control | Correct result (expected species/sex) |
| Negative control | No amplification |
| NTC | No amplification |
| Extraction blank | No amplification |
| IC (VIC channel) | Ct 25–32 in all samples |

### 8.2 Batch Release

All QC criteria must pass before any results from the batch are released.

## Step 9: Reporting

### 9.1 Report Format

| Field | Example |
|:------|:--------|
| Client ID | Royal Pigeon Loft |
| Case ID | SENO-20260401-1122 |
| Sample ID | SENO-20260401-1122-001 |
| Species | Racing Homer |
| Test | DNA Sexing |
| Method | CHD PCR (P2/P8) |
| Result | Female (ZW) |
| Confidence | > 99% |
| Date Tested | 2026-04-02 |
| QC Status | Passed |
| Authorized By | [SENO QC] |

### 9.2 Delivery Methods

| Method | Format | Delivery Time |
|:-------|:-------|:--------------|
| Email | PDF | Within 1 hour of final QC |
| Client Portal | Web download | Real-time |
| Hard copy (upon request) | Printed + signed | 2–3 business days |

## Step 10: Sample Storage & Disposal

| Phase | Condition | Duration |
|:------|:----------|:---------|
| Original sample (feather/swab) | Room temperature, dry | 3 months post-report |
| Extracted DNA | −20°C | 12 months post-extraction |
| PCR product (sexing) | −20°C | 1 month (then discarded) |
| qPCR plate | 4°C (sealed) | 1 week (then discarded) |
| CE data files | LIMS storage | Permanent |

## Estimated Turnaround Times

| Test Type | Hands-On Time | Instrument Time | Total Lab Time |
|:----------|:-------------:|:---------------:|:--------------:|
| DNA Sexing (batch of 48) | 2.5 hours | 2.5 hours | 5 hours |
| Disease qPCR (96-well plate) | 3 hours | 2 hours | 5 hours |
| DNA Fingerprinting (48) | 4 hours | 3 hours | 7 hours |
| Performance Gene (48) | 3 hours | 3 hours | 6 hours |

> **Lab turnaround: 1–2 working days for most tests.**
> **Total client turnaround (incl. shipping): 7–10 business days.**
