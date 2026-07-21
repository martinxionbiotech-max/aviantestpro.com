---title: "Laboratory Quality Control Protocols"
description: "Comprehensive quality control protocols for SENO's avian genetic testing laboratory. Covers per-batch controls, daily QC procedures, periodic QC activities, sample retesting protocols, result release criteria, equipment calibration, environmental monitoring, and non-conformance handling. ISO 9001:2015 and ISO 13485:2016 compliant."
canonical: https://aviantestpro.com/knowledge/quality-control/laboratory-qc-protocols---
canonical: https://aviantestpro.com/knowledge/quality-control/laboratory-qc-protocols


# Laboratory Quality Control Protocols


## QC Framework

SENO operates a multi-level QC system integrated into every testing process. This system is designed to ensure that every test result released from the Zhangjiakou laboratory meets the highest standards of accuracy, reliability, and reproducibility. The QC framework is aligned with ISO 9001:2015 (quality management) and ISO 13485:2016 (medical device QMS) requirements and is subject to both internal and external audit.

## Per-Batch Controls

Every PCR or qPCR run includes the following controls to validate assay performance and detect potential issues:

| Control Type | Frequency | Purpose | Expected Result | Action on Failure |
|:-------------|:---------:|:--------|:----------------|:------------------|
| Positive control | Every run | Confirm assay function | Strong amplification (expected Ct range) | Investigate reagents, repeat run |
| Negative control | Every run | Detect contamination | No amplification (No Ct) | Investigate source, quarantine affected reagents |
| No-template control | Every run | Verify reagent purity | No amplification (No Ct) | Replace reagents, repeat run |
| Internal amplification control | Every sample | Confirm DNA quality and absence of inhibition | Amplification within expected range | Re-extract DNA, dilute if inhibition suspected |
| Extraction blank | Every extraction batch | Monitor extraction reagent contamination | No amplification (No Ct) | Replace extraction reagents, re-extract batch |

### Control Pass/Fail Decision Matrix

| Control Result | Interpretation | Action |
|:---------------|:--------------|:-------|
| Positive Ct valid, Negative NTC no Ct, IAC valid | Run passed | Release results |
| Positive Ct out of range | Assay degradation | Repeat with fresh reagents |
| Negative Ct detected (positive NTC) | Contamination | Investigate source, repeat all samples |
| IAC failed (no Ct) in healthy control | Inhibition | Re-extract or dilute sample |
| Extraction blank positive | Reagent contamination | Replace extraction reagents |

## Daily QC

Daily QC checks ensure that laboratory equipment and environment remain within validated parameters:

| Check Item | Parameter | Method | Action on Failure |
|:-----------|:----------|:-------|:-----------------|
| PCR machine temperature | Block uniformity ± 0.5°C | Thermal validation plate | Service engineer call |
| Freezer temperature | -20°C ± 3°C / -80°C ± 5°C | Digital data logger + alarm | Transfer samples, service freezer |
| Refrigerator temperature | 4°C ± 2°C | Digital data logger + alarm | Transfer reagents, service unit |
| Pipette accuracy | Within spec per volume | Gravimetric check (water weight) | Recalibrate, quarantine affected results |
| Room temperature | 20-25°C | Wall-mounted thermometer | Adjust HVAC |
| Laboratory environment | Surface swabs, air samples | Contact plates, settling plates | If positive: clean, identify source, retest |
| Reagent performance | Control sample amplification | Run positive control with new lot | Investigate lot, contact supplier |

## Periodic QC

| Activity | Frequency | Responsible | Documentation |
|:---------|:---------:|:------------|:--------------|
| Instrument calibration | Quarterly (or per manufacturer) | External calibration service | Calibration certificate |
| Proficiency test participation | Semi-annual (annual minimum) | QC Manager | PT report + evaluation |
| SOP review and update | Annual | QC Manager + Lab Manager | SOP revision log |
| Management review | Semi-annual (quarterly minimum) | CEO + QC Manager + Lab Manager | Review meeting minutes |
| Internal audit | Quarterly | Trained internal auditor | Audit report + CAPA |
| Reagent lot-to-lot validation | Each new lot | QC technician | Lot validation report |
| Method re-validation | Annual or after significant change | R&D + QC | Validation report |
| Equipment maintenance | Per manufacturer schedule | Lab Manager | Maintenance log |
| Staff competency assessment | Annual | Lab Manager | Competency checklist |
| Data integrity audit | Semi-annual | QC Manager | Audit trail review |

## Sample Retesting Protocol

SENO retests approximately **20% of samples** for QC purposes. This robust retesting program ensures the accuracy and reliability of every result:

### Categories Requiring Retesting

| Category | Criteria | Retesting Scope |
|:---------|:---------|:----------------|
| First-time results | Any species, any test type — first submission | Full repeat from DNA extraction |
| Ambiguous results | Weak amplification, unclear band pattern | Full repeat from DNA extraction |
| Inconclusive results | IAC failure, conflicting replicates | Re-extract + repeat |
| Client verification requests | Client asks for result confirmation | Full repeat (no additional charge) |
| Statistical random selection | ~5% of routine results | Full repeat from DNA extraction |
| Post-QC failure re-runs | Previous run failed controls | Repeat extraction + assay |

### Retesting Workflow

1. **Identification** — Result flagged as requiring retest (automated in LIMS or manual by technician)
2. **Assignment** — Retest assigned to different technician (ensures independence)
3. **Re-extraction** — New DNA extraction from original sample (if sufficient material)
4. **Re-amplification** — Fresh PCR/qPCR run with new controls
5. **Comparison** — Original vs. retest results compared
6. **Reconciliation** — If results match: release. If results differ: investigate and triplicate repeat
7. **Documentation** — All retesting logged in LIMS with full traceability

## Result Release Criteria

Results are released only when all of the following conditions are met:

| Criterion | Verification Method | Documentation |
|:----------|:--------------------|:--------------|
| All controls produce expected results | Visual check of amplification curves / gel images | Run log entry |
| Internal amplification control is valid | IAC Ct within expected range for each sample | Sample-level QC flag |
| Result interpretation is unambiguous | Two-band pattern (female) or single-band (male) clearly visible | Technician interpretation |
| Reviewed by second qualified technician | Independent review of raw data and interpretation | Second review signature in LIMS |
| Retesting completed (if required) | Retest results match original or discrepancy resolved | Retest log entry |
| No outstanding non-conformances | CAPA status checked for affected assays | LIMS workflow gate |

## Equipment Calibration Schedule

| Equipment | Calibration Frequency | Method | Acceptance Criteria |
|:----------|:---------------------:|:-------|:-------------------|
| Thermocyclers (PCR machines) | Quarterly | Thermal validation plate + probe | Well-to-well uniformity ± 0.5°C |
| Real-time PCR instruments | Semi-annual | Calibration dye + ROI test | ROI within specification |
| Pipettes (single/multi-channel) | Quarterly | Gravimetric (4-point calibration) | Within spec per volume range |
| Balances | Semi-annual | Certified reference weights | ± 0.1 mg (analytical) |
| pH meters | Monthly (daily use check) | Buffer standards (pH 4, 7, 10) | ± 0.05 pH units |
| Freezers / refrigerators | Annual (sensor verification) | Independent thermometer comparison | ± 1°C of set point |
| Biological safety cabinets | Annual | HEPA filter certification | ISO Class 5 (Grade A) |
| Ultra-pure water system | Semi-annual | Resistivity + TOC measurement | ≥ 18.2 MΩ·cm, < 10 ppb TOC |

## Environmental Monitoring

| Location | Parameter | Frequency | Action Limits |
|:---------|:----------|:---------:|:--------------|
| PCR setup room | Surface contamination | Weekly | < 1 CFU/contact plate |
| PCR setup room | Airborne contamination | Monthly | < 10 CFU/settle plate (4 hours) |
| DNA extraction area | Surface contamination | Weekly | < 5 CFU/contact plate |
| DNA extraction area | Airborne contamination | Monthly | < 30 CFU/settle plate (4 hours) |
| Amplification/post-PCR area | Amplicon contamination | Weekly | No detectable PCR product |
| Clean room (reagent prep) | Particulate count | Quarterly | ISO Class 8 or better |
| Storage areas | Temperature mapping | Annual | Within specification throughout |

## Non-Conformance and CAPA

| Non-Conformance Severity | Definition | Response Time | Investigation Depth |
|:-------------------------|:-----------|:-------------:|:-------------------|
| Critical | Patient/result safety impact, regulatory breach | Immediate (< 1 hour) | Full root cause analysis |
| Major | QC failure, equipment malfunction affecting results | < 4 hours | Detailed investigation |
| Minor | Documentation error, minor procedure deviation | < 24 hours | Simple root cause |
| Observation | Opportunity for improvement | < 5 business days | Trend analysis |

## Document Control for QC Records

| Record Type | Retention Period | Storage Format | Access Control |
|:------------|:----------------:|:---------------|:--------------|
| QC run logs | 5 years | LIMS + physical backup | All QC staff |
| Calibration certificates | Life of equipment + 5 years | Document control system | Lab Manager + QC Manager |
| Proficiency test reports | 10 years | Document control system | QC Manager |
| CAPA records | 5 years after closure | LIMS | QC Manager |
| Audit reports | 5 years | Document control system | CEO + QC Manager |
| Training records | Employment + 3 years | HR system + LIMS | HR + QC Manager |

## Related Documents

- [DNA Extraction SOP](../quality-control/dna-extraction-sop.md) — Standard operating procedure for DNA extraction
- [CHD PCR Protocol](../quality-control/chd-pcr-protocol.md) — Detailed protocol for CHD gene-based sexing
- [PBFD qPCR Validation](../quality-control/pbfd-qpcr-validation.md) — Validation data for PBFD qPCR assay
- [PCR Troubleshooting](../quality-control/pcr-troubleshooting.md) — Common PCR issues and solutions
- [Proficiency Testing](../quality-control/proficiency-testing.md) — External inter-laboratory comparison program
- [Accuracy Validation](../quality-control/accuracy-validation.md) — Method validation and accuracy data
- [Lab Workflow](../quality-control/lab-workflow.md) — End-to-end sample processing workflow
