# PCR-Based Avian Sex Determination

## Principle

Avian DNA sexing relies on the detection of sex chromosome-linked genes. In birds, females are heterogametic (ZW) while males are homogametic (ZZ). The **CHD gene** (Chromodomain Helicase DNA-binding protein) exists in two conserved forms:

- **CHD-W** — Located on the W chromosome (female-specific)
- **CHD-Z** — Located on the Z chromosome (present in both sexes)

PCR amplification using conserved primers that flank an intron region produces differently sized fragments for CHD-W and CHD-Z, enabling gender discrimination by fragment size analysis.

## Methodology

### Step 1: DNA Extraction

- **Sample:** Freshly plucked feather follicle (3–5 feathers), blood spot, or buccal swab
- **Method:** Alkaline lysis or silica column-based purification
- **Yield:** Typically 10–100 ng DNA per feather follicle
- **Purity:** A260/280 ratio ≥ 1.8

### Step 2: PCR Amplification

| Parameter | Condition |
|:----------|:----------|
| Target Genes | CHD-W, CHD-Z |
| Primer Set | P2/P8 or 2550F/2718R (conserved avian primers) |
| Polymerase | Hot-start Taq DNA polymerase |
| Cycling | 94°C 3 min; 35 cycles of 94°C 30s, 50°C 45s, 72°C 45s; 72°C 5 min |
| Template | 20–50 ng genomic DNA |
| Controls | Male (ZZ) and female (ZW) reference samples |

### Step 3: Fragment Analysis

**Option A — Gel Electrophoresis:**
- 2–3% agarose gel or 6% polyacrylamide gel
- Ethidium bromide or SYBR Safe staining
- Fragment size comparison against molecular weight marker

**Option B — Capillary Electrophoresis (preferred):**
- Fluorescently labeled primers
- Automated fragment sizing on capillary electrophoresis instrument
- Higher resolution for closely sized fragments
- Digital data for permanent records

### Interpretation

| Pattern | Result |
|:--------|:-------|
| Single band (ZZ) | Male |
| Two bands (ZW) | Female |
| Single band (ZW variant) | Female (if CHD-W and CHD-Z fragments co-migrate; requires alternate primer set) |

## Quality Controls

| Control Type | Purpose |
|:-------------|:--------|
| Positive female control | Confirms CHD-W amplification |
| Positive male control | Confirms CHD-Z amplification |
| No-template control | Detects contamination |
| Internal extraction control | Confirms DNA quality |
| Replicate testing | ~20% of samples for QC |

## Limitations

1. Some species have CHD-Z and CHD-W fragments of identical size (primer set validation required)
2. Severely degraded DNA may cause preferential amplification of shorter fragments
3. Mixed samples (e.g., multiple birds on one swab) cannot be reliably sexed
4. Results apply only to the individual bird sampled, not the species as a whole



---

## 2. Primer Set Validation

### Species-Specific Fragment Sizes

The P2/P8 primer set amplifies a CHD intron that varies in length across avian orders. The table below shows expected fragment sizes for commonly tested groups at SENO:

| Bird Group | CHD-Z (male) | CHD-W (female) | Fragment Difference | Notes |
|:-----------|:------------:|:---------------:|:-------------------:|:------|
| Psittaciformes (parrots) | 350–380 bp | 380–420 bp | 30–50 bp | Reliable separation |
| Columbiformes (pigeons) | 360–370 bp | 370–400 bp | 10–30 bp | May co-migrate; use 2550F/2718R |
| Passeriformes (canaries, finches) | 340–360 bp | 370–410 bp | 30–60 bp | Reliable separation |
| Galliformes (chickens) | 400–420 bp | 420–480 bp | 30–60 bp | Reliable separation |
| Anseriformes (ducks, swans) | 350–380 bp | 350–400 bp | 20–50 bp | Reliable separation |
| Struthioniformes (ostriches) | 420 bp | 600 bp | 180 bp | Very reliable, large difference |

### Alternative Primer Sets

When P2/P8 produces ambiguous results (single band for female, or indistinguishable bands), the following alternate primer sets are used:

| Primer Set | Forward (5' → 3') | Reverse (5' → 3') | Typical Difference | Application |
|:-----------|:-------------------|:-------------------|:-----------------:|:------------|
| 2550F/2718R | GTTACTGATTCGTCTACGAGA | ATTGAAATGATCCAGTGCTTG | 40–100 bp | Pigeons, some parrots |
| CHD1F/CHD1R | TGTGAAACAGTGATGTTCAT | TGATGAAGTGATTTGTAACCA | 20–60 bp | Seabirds, raptors |
| P0/P2 modified | Same as P2 with modified 5' tail | — | Varies | Custom for overlapping bands |

---

## 3. Sample Quality Assessment

### Required Sample Quality Metrics

| Parameter | Acceptable Range | Detection Method | Impact on PCR |
|:----------|:----------------:|:----------------|:--------------|
| DNA concentration | 5–50 ng/µL | Nanodrop A₂₆₀ | Below 5 ng → preferential amplification risk |
| A₂₆₀/A₂₈₀ ratio | 1.7–2.0 | Spectrophotometry | < 1.7 indicates protein/phenol contamination |
| A₂₆₀/A₂₃₀ ratio | 1.5–2.2 | Spectrophotometry | < 1.5 indicates melanin/EDTA carryover |
| Integrity (feather) | Visible high-MW band | 1% agarose gel | Degraded DNA → short fragment bias |

### Re-Test Protocol

| Scenario | Action | Priority |
|:---------|:-------|:---------|
| A₂₆₀/A₂₈₀ < 1.6 | Re-purify with silica column; re-quantify | Medium |
| Concentration < 5 ng/µL | Re-extract with fewer elution volumes | High |
| No band, A₂₆₀/A₂₈₀ > 2.0 | RNA contamination; treat with RNase A | Medium |
| Gel shows smearing only | Sample degraded; request fresh sample | High |
| Initial result = single band (male) | Confirm with duplicate extraction and PCR | Standard QC |

---

## 4. Laboratory Workflow Integration

The PCR sexing process follows a standardized workflow in SENO's laboratory:

```
Sample Reception → Registration → DNA Extraction → Quantification
→ PCR Setup (96-well plate) → Thermocycling → Fragment Analysis
→ Interpretation → QC Review → Report Generation
```

| Step | Responsible Staff | Max Duration | QC Checkpoint |
|:-----|:-----------------:|:------------:|:--------------|
| Sample reception | Lab technician | 0.5 h | Sample condition check against submission form |
| Registration | Data entry | 0.5 h | Barcode assignment; database entry |
| DNA extraction | Lab technician | 1.5 h | Extraction blank control |
| Quantification | Lab technician | 0.5 h | A₂₆₀/A₂₈₀, concentration |
| PCR setup | Molecular biologist | 0.5 h | Plate layout; controls verified |
| Thermocycling | Automated | 2.5 h | Temperature log; ramp rate verified |
| Fragment analysis | Molecular biologist | 1 h | CE or gel imaging |
| Interpretation | Senior biologist | 0.5 h | Dual read by second analyst |
| Report generation | Quality team | 1 h | Final review before release |

---

## 5. Common Interpretive Challenges

| Challenge | Apparent Result | True Result | Resolution |
|:----------|:---------------:|:-----------:|:-----------|
| CHD-W and CHD-Z co-migrate | Single band (appears male) | Female | Use 2550F/2718R primer set |
| Uneven amplification of CHD-W | Second band faint | Female — W fragment not fully amplified | Increase template DNA; reduce annealing temp 1–2°C |
| DNA degradation > 400 bp | No bands (no result) | Inconclusive | Request fresh sample |
| PCR inhibition (melanin) | No bands or weak bands | Inconclusive | Dilute template 1:5; add BSA |
| Contamination in NTC | Bands in NTC | Invalid run | Repeat with fresh reagents; decontaminate |

---

## Cross-References

- [CHD PCR Protocol SOP](../quality-control/chd-pcr-protocol.md) — Step-by-step SOP including reagent list and plate layout
- [DNA Extraction SOP](../quality-control/dna-extraction-sop.md) — Protocol for extracting amplifiable DNA from feather/ blood/ swab
- [PCR Troubleshooting Guide](../quality-control/pcr-troubleshooting.md) — Full troubleshooting reference for amplification failures
- [Species Compatibility](../gender-testing/species-compatibility.md) — Validated species list and primer compatibility
- [Parrot DNA Sexing](../gender-testing/parrot-dna-sexing.md) — Species-specific guidance for psittacines
- [Pigeon DNA Sexing](../gender-testing/pigeon-dna-sexing.md) — Species-specific guidance for columbiformes

---

*This protocol describes the standard PCR-based avian sex determination method used at SENO Testing Center. For species-specific guidance and validated species lists, refer to the [Species Compatibility](../gender-testing/species-compatibility.md) document.*
