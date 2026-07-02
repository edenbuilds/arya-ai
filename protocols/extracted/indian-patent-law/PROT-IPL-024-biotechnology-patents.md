# Protocol: Biotechnology Patents

**Protocol ID**: PROT-IPL-024
**Version**: 1.0.0
**Domain**: Indian Patent Law
**Category**: Subject Matter Specific
**Last Updated**: 2026-01-16

---

## Purpose

Comprehensive guide for biotechnology patent strategy in India, covering Section 3(j) exclusions, microorganism patents under Budapest Treaty, plant variety protection, biological material deposits, and regulatory considerations.

---

## Activation Triggers

- Filing biotechnology patent application
- Responding to Section 3(j) objection
- Depositing biological material
- Evaluating plant-related invention patentability
- Assessing Biological Diversity Act compliance

---

## Prerequisites

- Understanding of Section 3(j) framework
- Budapest Treaty deposit knowledge
- Biological Diversity Act awareness
- Technical description of biotechnology invention
- Sequence listings (if applicable)

---

## Core Process

### Step 1: Understanding Section 3(j) Exclusions

#### Section 3(j) - Plants, Animals, Biological Processes:

"Plants and animals in whole or any part thereof other than micro-organisms but including seeds, varieties and species and essentially biological processes for production or propagation of plants and animals"

#### What Section 3(j) Excludes:

| Category | Excluded? | Notes |
|----------|-----------|-------|
| Plants (whole) | Yes | Always excluded |
| Plant parts | Yes | Leaves, stems, roots, etc. |
| Seeds | Yes | Explicitly excluded |
| Plant varieties | Yes | PPVFR Act applies |
| Animals (whole) | Yes | Always excluded |
| Animal parts | Yes | Organs, tissues, etc. |
| Essentially biological processes | Yes | Natural reproduction |

#### What Section 3(j) Permits:

| Category | Patentable? | Notes |
|----------|-------------|-------|
| **Microorganisms** | Yes | Explicit carve-out |
| Technical processes | Yes | Non-essentially biological |
| Modified genes/sequences | Possibly | With technical application |
| Biotech products | Possibly | If not plant/animal part |

### Step 2: Microorganism Patents

#### Definition (Indian Jurisprudence):
- Bacteria, fungi, algae, protozoa, viruses
- Plasmids, cell lines (disputed)
- Genetically modified microorganisms

#### Requirements for Patenting:

1. **Novelty**: New microorganism or new use
2. **Inventive step**: Non-obvious modification
3. **Industrial application**: Useful application
4. **Not naturally occurring**: Must be isolated or modified
5. **Enablement**: Reproducible disclosure

#### Budapest Treaty Deposit:

**International Depositary Authorities (IDAs) in India**:
- Microbial Type Culture Collection (MTCC), Chandigarh
- Microbial Culture Collection (MCC), Pune

**Deposit Requirements**:
| Requirement | Details |
|-------------|---------|
| **When** | Before or on filing date |
| **What** | Viable sample of microorganism |
| **Where** | IDA under Budapest Treaty |
| **Reference** | Accession number in specification |

**Deposit Timeline**:
```
Invention → Deposit at IDA → Receive accession number →
File patent application → Include deposit details in specification
```

### Step 3: Sequence Listing Requirements

#### When Required:
- Nucleotide sequences (10+ nucleotides)
- Amino acid sequences (4+ amino acids)

#### Format (Rule 9(3)):
- WIPO Standard ST.25 format
- Separate sequence listing annex
- Computer-readable format
- Proper sequence identifiers

#### Required Information:
```
<110> Applicant Name
<120> Title of Invention
<130> Application Reference
<140> Application Number
<141> Filing Date
<160> Number of Sequences
<210> SEQ ID NO: 1
<211> Length
<212> Type (DNA/RNA/PRT)
<213> Organism
<400> Sequence
```

### Step 4: Plant-Related Inventions

#### What's Excluded (Section 3(j)):
- Plant varieties
- Seeds
- Plant parts
- Essentially biological processes

#### What May Be Patentable:
| Category | Patentability |
|----------|---------------|
| Isolated plant genes | Possibly (technical application) |
| Plant genetic constructs | Possibly |
| Transformation methods | Yes (technical process) |
| Plant cell lines | Disputed |
| Cultivation methods | If technically inventive |

#### Alternative Protection - PPVFR Act:
- Plant Variety Protection and Farmers' Rights Act, 2001
- Sui generis protection for varieties
- Breeders' rights registration
- Farmers' rights preserved

### Step 5: Biological Diversity Act Compliance

#### Access and Benefit Sharing (ABS):

**Section 6 Requirements**:
| Applicant | Requirement |
|-----------|-------------|
| Non-Indian | Prior NBA approval before filing |
| Indian with foreign participation | Prior NBA approval |
| Indian citizen/company | Prior intimation to SBB |

**Application Process**:
1. Identify biological resource used
2. Apply to National Biodiversity Authority (NBA)
3. Obtain approval/permission
4. Disclose in patent application
5. Comply with benefit-sharing conditions

#### Consequences of Non-Compliance:
- Ground for pre-grant opposition (Section 25(1))
- Ground for revocation (Section 64)
- NBA can impose conditions
- Benefit-sharing requirements

### Step 6: Claim Drafting for Biotech

#### Microorganism Claims:
```
"An isolated microorganism [species] having [characteristic],
deposited under accession number [IDA reference],
capable of [function/industrial application]."
```

#### Process Claims:
```
"A method for producing [product] comprising:
(a) culturing [microorganism] under [conditions];
(b) expressing [gene/protein];
(c) isolating [product] by [technique]."
```

#### Gene/Sequence Claims (if permissible):
```
"An isolated nucleic acid molecule comprising:
(a) a nucleotide sequence as set forth in SEQ ID NO: [X]; or
(b) a nucleotide sequence having at least [90]% identity to (a);
wherein said molecule encodes a protein having [function]."
```

### Step 7: Responding to Section 3(j) Objections

#### Strategy Framework:

1. **Narrow to microorganisms**:
   - Focus claims on microbial aspects
   - Avoid plant/animal terminology

2. **Emphasize technical process**:
   - Non-essentially biological
   - Human intervention essential
   - Technical character demonstrated

3. **Distinguish from nature**:
   - Show isolation or modification
   - Technical effect demonstrated
   - Industrial application clear

4. **Alternative claim strategies**:
   - Process claims instead of product
   - Use/application claims
   - Composition claims (formulations)

---

## Decision Tree: Biotech Patentability

```
Is the invention:
│
├─ Whole plant/animal → NOT PATENTABLE
│
├─ Plant/animal part (seeds, organs) → NOT PATENTABLE
│
├─ Plant variety → NOT PATENTABLE (use PPVFR)
│
├─ Essentially biological process → NOT PATENTABLE
│   (natural reproduction/selection)
│
├─ Microorganism → POTENTIALLY PATENTABLE
│   ├─ Naturally occurring → Limited (need isolation)
│   └─ Modified/isolated → Patentable (with deposit)
│
├─ Technical process for biotech → POTENTIALLY PATENTABLE
│   └─ Human intervention essential
│
├─ Isolated gene/sequence → UNCERTAIN
│   ├─ With technical application → May be patentable
│   └─ Mere discovery → Not patentable
│
└─ Biological material-based product → ANALYZE
    ├─ Not plant/animal part → May be patentable
    └─ Is plant/animal part → NOT PATENTABLE
```

---

## Quality Checklist

- [ ] Section 3(j) analysis completed
- [ ] Biological material deposited (if needed)
- [ ] Accession number included in specification
- [ ] Sequence listing in ST.25 format
- [ ] NBA/SBB compliance verified
- [ ] Claims avoid excluded categories
- [ ] Technical process clearly described
- [ ] Industrial application demonstrated

---

## Common Biotech Patent Mistakes

1. **Claiming plant parts**: Clearly excluded
2. **Missing deposit**: Required for microorganisms
3. **Wrong sequence format**: Use ST.25
4. **No NBA clearance**: Invalidity ground
5. **Essentially biological process**: Must show technical intervention
6. **Discovery vs. invention**: Must have technical application

---

## Related Protocols

- PROT-IPL-011: Patentability Analysis
- PROT-IPL-015: Traditional Knowledge and TKDL
- PROT-IPL-002: Patent Specification Drafting
- PROT-IPL-019: Pharmaceutical Patents

---

## Legal References

- Patents Act, 1970: Section 3(j)
- Patents Rules, 2003: Rule 9(3) (sequence listing)
- Biological Diversity Act, 2002: Section 6
- Budapest Treaty on Deposit of Microorganisms
- PPVFR Act, 2001

---

## Sources

- [Biotech Patents India - IPO Guidelines](https://ipindia.gov.in/writereaddata/Portal/IPOGuidelinesManuals/1_33_1_biotech-guidelines.pdf)
- [Biological Diversity Act - NBA](http://nbaindia.org/)
- [MTCC - IDA India](https://mtccindia.res.in/)
- [Section 3(j) Analysis - Lexology](https://www.lexology.com/library/detail.aspx?g=section-3j-india-biotech)
