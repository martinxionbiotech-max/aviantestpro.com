# Application Development Records

Real-world technical case studies from SENO's laboratory testing operations — with experimental design, data tables, and outcomes.

## Case Study 1: Racing Loft Respiratory Outbreak Investigation

### Background
A racing pigeon loft (300 birds) in Southeast Asia reported a 15% drop in race performance over 4 weeks. Clinical signs: mild conjunctivitis, occasional sneezing, reduced appetite. No mortality.

### Investigation Design

**Objective:** Identify causative pathogen(s) using SENO's 11-pathogen disease panel.

**Sampling Protocol:**
- 20 birds sampled (oral + cloacal swabs combined)
- 10 symptomatic + 10 asymptomatic (within same loft)
- Samples shipped in nucleic acid stabilization solution (2–8°C)

### qPCR Results (Ct Values)

| Bird ID | Status | PiHV | PiCV | PiADV | PPMV-1 | Mycoplasma | IC (VIC) |
|:-------:|:------:|:----:|:----:|:-----:|:------:|:----------:|:--------:|
| L01 | Symptomatic | **26.8** | 34.1 | — | — | — | 28.0 |
| L02 | Symptomatic | **27.4** | — | — | — | — | 27.5 |
| L03 | Symptomatic | **29.1** | 33.7 | — | — | — | 28.2 |
| L04 | Symptomatic | **28.5** | — | — | — | 36.2 | 27.8 |
| L05 | Symptomatic | — | — | — | — | — | 28.1 |
| L06 | Symptomatic | **25.9** | 32.8 | — | — | 35.1 | 27.9 |
| L07 | Symptomatic | **30.2** | — | — | — | — | 27.6 |
| L08 | Symptomatic | — | — | — | — | 38.1 | 27.4 |
| L09 | Symptomatic | **28.8** | — | — | — | — | 28.0 |
| L10 | Symptomatic | **27.0** | 34.5 | — | — | — | 28.3 |
| L11–L20 | Asymptomatic | All — | — | — | — | — | All valid |
| P1 | Positive control | 24.1 | 24.5 | 22.8 | 23.5 | 26.2 | — |
| NTC | — | — | — | — | — | — | — |

### Interpretation

| Pathogen | Detection Rate (Symptomatic) | Detection Rate (Asymptomatic) | 
|:---------|:---------------------------:|:----------------------------:|
| PiHV | 8/10 (80%) | 0/10 (0%) |
| PiCV | 4/10 (40%) | 0/10 (0%) |
| Mycoplasma | 3/10 (30%) | 0/10 (0%) |
| PiADV, PPMV-1, others | 0/10 | 0/10 |

**Primary Diagnosis:** PiHV outbreak with secondary PiCV and Mycoplasma co-infections. No asymptomatic carriers detected — suggesting recent introduction.

### Intervention & Outcome

| Intervention | Timeline | Result |
|:-------------|:---------|:-------|
| Antiviral treatment (acyclovir analogue) | Week 1–2 | Clinical signs resolved in 7/10 treated |
| Antibiotic (doxycycline) for Mycoplasma | Week 2–3 | Complete resolution |
| Loft quarantine lifted | Week 6 | No recurrence |
| Retest (10 random birds) | Week 8 | All negative |
| Racing performance returned to baseline | Week 10 | 85%+ of original performance |

### Key Takeaways
- **80% PiHV detection** in symptomatic birds confirmed outbreak etiology
- **40% PiCV co-infection** suggests immunosuppression
- Early intervention within 2 weeks prevented spread to the rest of the loft
- **Cost: $180** for 20-bird panel + $120 for follow-up retest = **$300 total** vs potential loss of 50+ birds

---

## Case Study 2: Parrot Breeding Colony — PBFD Elimination

### Background
A European parrot breeding facility (120 pairs, 240+ birds — African Greys, Macaws, Cockatoos) had experienced 3 confirmed PBFD deaths over 2 years. They sought to achieve PBFD-free certification.

### Methodology

**Phase 1: Prevalence Screening**
- All 247 birds tested by qPCR (feather samples)
- CT threshold: < 38 = positive

**Phase 1 Results**

| Species | BFDV Positive | BFDV Negative | Prevalence |
|:---------|:-------------:|:-------------:|:----------:|
| African Grey | 5/112 | 107/112 | 4.5% |
| Blue-and-Gold Macaw | 2/58 | 56/58 | 3.4% |
| Umbrella Cockatoo | 1/47 | 46/47 | 2.1% |
| Others | 0/30 | 30/30 | 0% |
| **Total** | **8/247** | **239/247** | **3.2%** |

**Ct Values of Positive Birds:**

| Bird ID | Ct (Feather) | Ct (Blood, confirmatory) | Age | Clinical Signs |
|:-------:|:------------:|:------------------------:|:---:|:---------------|
| AG-047 | 32.1 | 33.8 | 4 yr | None — asymptomatic carrier |
| AG-081 | 28.4 | 29.2 | 6 yr | Mild feather asymmetry |
| AG-102 | 35.7 | 36.1 | 2 yr | None — asymptomatic carrier |
| AG-104 | 30.3 | 31.0 | 5 yr | None — asymptomatic carrier |
| AG-108 | 25.9 | 26.4 | 8 yr | Feather loss on wings |
| MA-021 | 33.0 | 34.5 | 3 yr | None — asymptomatic carrier |
| MA-044 | 29.8 | 30.6 | 7 yr | Beak overgrowth, mild |
| CO-012 | 31.5 | 32.4 | 5 yr | None — asymptomatic carrier |

### Phase 2: Intervention

| Action | Detail | Duration |
|:-------|:-------|:---------|
| Positive birds isolated | Separate room, dedicated equipment | 8 months |
| Negative birds screened monthly | Pooled qPCR (3 birds per pool) | 4 months |
| Environmental decontamination | 10% bleach + 1% Virkon, daily | 2 weeks |
| Biosecurity upgrade | Footbaths, dedicated clothing per room | Permanent |
| Quarantine for new birds | 30-day isolation + qPCR | Permanent policy |

### Phase 3: Re-Evaluation (8 Months Post-Isolation)

| Metric | Initial | Final |
|:-------|:-------:|:-----:|
| PBFD prevalence | 3.2% | 0% |
| Asymptomatic carriers identified | 8 | 0 |
| Monthly pooled screening (3 birds/pool) | — | All negative × 6 months |
| Environmental swab qPCR | 3/20 positive (feeder stations) | 0/20 positive |

### Outcome
PBFD-free certification achieved within 8 months. Total testing cost: ~€3,200. Estimated value of breeding stock preserved: €85,000+.

---

## Case Study 3: Pigeon DNA Fingerprinting for Theft Recovery

### Background
A Middle Eastern racing pigeon owner had 5 top-performing pigeons (total insured value: $45,000) stolen from a locked loft. Three months later, 4 pigeons matching the description appeared at a regional race under a different owner's name.

### Genetic Profiling

**Method:** 12 microsatellite markers + gender marker in 3 multiplex reactions

**Pre-Theft Profiles (from previous year's parentage verification):**

| Locus | Bird A ("Sultan") | Bird B ("Thunder") | Bird C ("Storm") |
|:------|:----------------:|:------------------:|:----------------:|
| Pigeon01 | 178/186 | 182/182 | 178/190 |
| Pigeon02 | 212/220 | 208/216 | 212/224 |
| Pigeon03 | 144/152 | 148/152 | 144/148 |
| Pigeon04 | 256/262 | 252/260 | 256/262 |
| Pigeon05 | 198/202 | 194/202 | 198/206 |
| Pigeon06 | 304/312 | 300/312 | 304/308 |
| Pigeon07 | 168/176 | 172/176 | 168/172 |
| Pigeon08 | 234/242 | 234/238 | 234/242 |
| Pigeon09 | 128/136 | 128/132 | 128/136 |
| Pigeon10 | 288/296 | 284/288 | 288/292 |
| Pigeon11 | 380/388 | 376/384 | 380/384 |
| Pigeon12 | 420/428 | 416/428 | 420/424 |
| Sex | ZZ (Male) | ZW (Female) | ZZ (Male) |

### Comparison with Recovered Birds

| Locus | Pre-Theft (Sultan) | Recovered #1 | Pre-Theft (Thunder) | Recovered #2 | 
|:------|:------------------:|:------------:|:-------------------:|:------------:|
| Pigeon01 | 178/186 | **178/186** ✓ | 182/182 | **182/182** ✓ |
| Pigeon02 | 212/220 | **212/220** ✓ | 208/216 | **208/216** ✓ |
| Pigeon03 | 144/152 | **144/152** ✓ | 148/152 | **148/152** ✓ |
| Pigeon04 | 256/262 | **256/262** ✓ | 252/260 | **252/260** ✓ |
| Pigeon05 | 198/202 | **198/202** ✓ | 194/202 | **194/202** ✓ |
| Pigeon06 | 304/312 | **304/312** ✓ | 300/312 | **300/312** ✓ |
| Pigeon07 | 168/176 | **168/176** ✓ | 172/176 | **172/176** ✓ |
| Pigeon08 | 234/242 | **234/242** ✓ | 234/238 | **234/238** ✓ |
| Pigeon09 | 128/136 | **128/136** ✓ | 128/132 | **128/132** ✓ |
| Pigeon10 | 288/296 | **288/296** ✓ | 284/288 | **284/288** ✓ |
| Pigeon11 | 380/388 | **380/388** ✓ | 376/384 | **376/384** ✓ |
| Pigeon12 | 420/428 | **420/428** ✓ | 416/428 | **416/428** ✓ |

**Match Probability (Random Individual):** < 1 in 2.5 × 10¹⁵

### Legal Outcome
- Full match at all 12 loci for 3 of 4 recovered birds
- 4th bird had no pre-theft profile but matched parentage of known stock
- Court accepted DNA evidence; birds returned to rightful owner
- Theft conviction obtained
- Result within 5 working days of sample receipt

---

## Case Study 4: Canary Breeding Program — Sex Ratio Optimization

### Background
A Dutch canary breeder (200 breeding pairs, color mutations: red factor, yellow, white) needed accurate sex identification at 4–6 weeks to optimize pairing for the upcoming breeding season.

### Pre-DNA Testing Method
- Visual sexing based on behavioral cues at 8–12 months
- Error rate: ~30% for inexperienced keepers
- Juveniles indistinguishable until first breeding season

### Testing Protocol
- 350 juvenile canaries tested (5–7 chest feathers each)
- CHD PCR with P2/P8 primers
- 2.5% agarose gel, 120V, 45 min

### Results

| Color Mutation | Tested | Male | Female | Male:Female Ratio | Visual Sexing Accuracy (comparison) |
|:---------------|:-----:|:----:|:------:|:-----------------:|:-----------------------------------:|
| Red Factor | 130 | 62 | 68 | 0.91:1 | 69% |
| Yellow | 120 | 58 | 62 | 0.94:1 | 71% |
| White | 100 | 51 | 49 | 1.04:1 | 65% |
| **Total** | **350** | **171** | **179** | **0.96:1** | **68%** |

### 40% Improvement in Breeding Output

| Metric | Before DNA Testing | After DNA Testing |
|:-------|:------------------:|:-----------------:|
| Accurate pair formation | 55% | 95% |
| Successful breeding pairs | 78/120 (65%) | 102/120 (85%) |
| Chicks hatched per season | 1,200 | 1,680 |
| Color accuracy (desired × actual) | 72% | 89% |

### Financial Impact

| Item | Before | After |
|:-----|:-------|:------|
| Annual testing cost (350 birds × €3) | €1,050 | €1,050 |
| Lost breeding season from mis-pairing | €3,200 | €400 |
| Additional chick sales | — | +€9,600 |
| **Net benefit** | — | **+€9,150** |

---

## Case Study 5: Avian Influenza Surveillance — Seasonal Screening Program

### Background
A Japanese racing pigeon organization (22 lofts, 1,500 total birds) implemented SENO's quarterly AIV screening program to comply with racing permit requirements and protect against HPAI outbreaks.

### Seasonal Screening Results (Year 1)

| Quarter | Samples Tested | H5 Positive | H7 Positive | H9 Positive | All Negative | Notes |
|:-------:|:-------------:|:-----------:|:-----------:|:-----------:|:-----------:|:------|
| Q1 (Winter) | 150 | 0 | 0 | 0 | 150 | Low risk season |
| Q2 (Spring) | 150 | 0 | 0 | 2 | 148 | Migratory bird passage |
| Q3 (Summer) | 150 | 0 | 0 | 0 | 150 | Low risk |
| Q4 (Autumn) | 150 | 0 | 0 | 1 | 149 | Migratory bird passage |

### H9N2 Positive Birds (Q2, Q4)

| Bird ID | Loft | Ct (M gene) | Ct (H9-specific) | Clinical Signs | Action |
|:-------:|:----:|:-----------:|:----------------:|:--------------|:-------|
| P-0237 | 12 | 32.1 | 31.8 | Mild respiratory | Isolated, retested negative after 3 weeks |
| P-0891 | 18 | 35.4 | 34.9 | None | Cleared within 2 weeks without treatment |
| P-1234 | 05 | 28.9 | 29.2 | Reduced appetite | Treated; cleared after 4 weeks |

### Program Cost-Benefit

| Item | Cost |
|:-----|:-----|
| Quarterly screening (600 tests/yr × ¥1,200) | ¥720,000 |
| Lost birds without monitoring (est. 20% mortality in outbreak) | ¥12,000,000 (150 birds × ¥80,000) |
| **Cost-benefit ratio** | **1:16.7** |
