# Protocol: Patentability Analysis

**Protocol ID**: PROT-IPL-011
**Version**: 1.0.0
**Domain**: Indian Patent Law
**Category**: Patentability Assessment
**Last Updated**: 2026-01-16

---

## Purpose

Comprehensive framework for evaluating patentability of inventions under Indian patent law, including novelty, inventive step, industrial applicability, and subject matter eligibility analysis under Section 3.

---

## Activation Triggers

- Evaluating invention disclosure for patent filing
- Preparing patentability opinion
- Responding to examination objections
- Advising on R&D investment decisions
- Due diligence in technology acquisition

---

## Prerequisites

- Complete invention disclosure
- Prior art search results
- Understanding of technology field
- Knowledge of Section 3 exclusions

---

## Core Process

### Step 1: Subject Matter Eligibility (Section 3)

**First hurdle**: Is the invention excluded from patentability?

#### Section 3 Exclusions:

| Section | Exclusion | Examples |
|---------|-----------|----------|
| 3(a) | Frivolous or contrary to law | Perpetual motion machines |
| 3(b) | Contrary to public order/morality | Human cloning |
| 3(c) | Mere discovery of natural substances | Naturally occurring gene sequences |
| 3(d) | New forms without enhanced efficacy | Polymorphs, salts, esters |
| 3(e) | Mere admixture | Simple physical mixtures |
| 3(f) | Mere arrangement/rearrangement | Reconfiguration without technical effect |
| 3(h) | Method of agriculture/horticulture | Farming methods |
| 3(i) | Medical treatment methods | Surgical, therapeutic, diagnostic methods on humans |
| 3(j) | Plants, animals (except microorganisms) | Seeds, varieties, biological processes |
| 3(k) | Mathematical methods, computer programs per se, algorithms | Pure software, business methods |
| 3(l) | Literary, artistic works | Copyright subject matter |
| 3(m) | Mental acts, rules, methods | Game rules |
| 3(n) | Presentation of information | Data display methods |
| 3(o) | Topography of ICs | Covered by separate Act |
| 3(p) | Traditional knowledge | TKDL documented knowledge |

### Step 2: Deep Dive - Critical Section 3 Analyses

#### Section 3(d) - Pharmaceutical Evergreening:

**What's Excluded**:
- New forms of known substances
- Derivatives with same activity
- **UNLESS** enhanced efficacy shown

**Novartis Test (Supreme Court 2013)**:
- "Efficacy" = "therapeutic efficacy" for pharmaceuticals
- Must show **clinical improvement**, not just physicochemical
- Bioavailability alone insufficient
- Comparative data required

**Best Practice**:
- Include comparative efficacy data in specification
- Document clinical improvements
- Avoid claiming mere polymorphs/salts without efficacy data

#### Section 3(k) - Computer-Related Inventions:

**What's Excluded**:
- Mathematical methods
- Business methods
- Computer programs "per se"
- Algorithms

**2025 CRI Guidelines - Technical Effect Test**:

1. Is there a **technical problem** being solved?
2. Does solution involve **technical means**?
3. Is there a **technical effect** beyond normal software execution?

**Allowable CRIs**:
- Technical contribution to computer system operation
- Hardware efficiency improvements
- Network performance optimization
- Security system enhancements

**Not Allowable**:
- Pure business processes implemented in software
- Data manipulation without technical effect
- User interface improvements alone

### Step 3: Novelty Analysis (Section 2(1)(l))

**Test**: Is the invention anticipated by prior art?

#### Prior Art Definition:
- Published anywhere in the world before priority date
- Publicly known or used in India before priority date

#### Anticipation Requirements:
All essential features of claim must be **explicitly or inherently disclosed** in a single prior art reference.

#### Analysis Framework:

```
For each independent claim:
1. List all claim elements
2. Compare element-by-element with closest prior art
3. Identify:
   - Disclosed elements
   - Inherently present elements
   - Missing elements (differentiators)
```

**If any element missing** → Claim is novel

### Step 4: Inventive Step Analysis (Section 2(1)(ja))

**Definition**: "Feature of an invention that involves technical advance as compared to existing knowledge or having economic significance or both and that makes the invention not obvious to a person skilled in the art"

#### TSM (Teaching-Suggestion-Motivation) Test:

Would POSITA (Person of Ordinary Skill in the Art):
1. Have **motivation** to combine references?
2. Have **expectation of success**?
3. Have **teaching** how to combine?

#### Analysis Steps:

1. **Define POSITA**: Educational background, experience level
2. **Identify closest prior art**: Most relevant single reference
3. **Identify differences**: Between claim and prior art
4. **Evaluate obviousness**: Would combination be obvious?

#### Secondary Considerations (may support non-obviousness):
- Commercial success
- Long-felt need
- Failure of others
- Unexpected results
- Industry skepticism

### Step 5: Industrial Applicability (Section 2(1)(ac))

**Test**: Can invention be made or used in any industry?

**Generally satisfied if**:
- Concrete, real-world application identified
- Not mere abstract concept
- Practical utility demonstrated

### Step 6: Sufficiency of Disclosure (Section 10)

**Requirements**:
1. **Full description**: Enable POSITA to practice
2. **Best mode**: Disclose preferred embodiment
3. **Clear claims**: Definite scope of protection
4. **Fair basis**: Claims supported by description

---

## Patentability Opinion Structure

```
PATENTABILITY OPINION

Subject: [Invention Title]
Date: [Date]
Prepared By: [Name]

EXECUTIVE SUMMARY:
[Overall patentability assessment]

1. SUBJECT MATTER ELIGIBILITY
- Section 3(d) Analysis: [Pass/Fail - Reasoning]
- Section 3(k) Analysis: [Pass/Fail - Reasoning]
- Other Section 3 Considerations: [If applicable]

2. NOVELTY ANALYSIS
- Closest Prior Art: [Citation]
- Novel Elements: [List differentiators]
- Assessment: [Novel/Not Novel]

3. INVENTIVE STEP ANALYSIS
- POSITA Definition: [Description]
- Technical Advance: [Description]
- Obviousness Assessment: [Non-obvious/Obvious]
- Secondary Considerations: [If applicable]

4. INDUSTRIAL APPLICABILITY
- Assessment: [Yes/No]
- Industry Application: [Identified use]

5. DISCLOSURE ASSESSMENT
- Enablement: [Sufficient/Insufficient]
- Best Mode: [Disclosed/Not Disclosed]
- Claim Support: [Adequate/Inadequate]

CONCLUSION:
[Patentable / Not Patentable / Patentable with modifications]

RECOMMENDATIONS:
[Suggested claim scope, specification improvements, etc.]
```

---

## Quality Checklist

- [ ] All Section 3 exclusions analyzed
- [ ] Prior art search comprehensive
- [ ] Novelty assessed claim-by-claim
- [ ] POSITA properly defined
- [ ] Inventive step analysis documented
- [ ] Industrial applicability confirmed
- [ ] Disclosure sufficiency verified
- [ ] Recommendations actionable

---

## Common Patentability Mistakes

1. **Ignoring Section 3(d)**: Critical for pharma
2. **CRI technical effect missing**: Focus on technical contribution
3. **Combining multiple references wrongly**: Need motivation
4. **Broad POSITA definition**: Makes everything obvious
5. **Missing secondary considerations**: Support non-obviousness

---

## Related Protocols

- PROT-IPL-010: Prior Art Search Strategy
- PROT-IPL-002: Patent Specification Drafting
- PROT-IPL-025: CRI Patent Strategy
- PROT-IPL-026: Pharmaceutical Patent Strategy

---

## Legal References

- Patents Act, 1970: Sections 2(1)(j), 2(1)(ja), 2(1)(l), 3, 10
- CRI Guidelines 2025
- Novartis AG v. Union of India (SC, 2013)
- Ferid Allani v. Union of India (2020)
- Microsoft v. Assistant Controller (Madras HC, 2023)

---

## Sources

- [Patentability Requirements - BananaIP](https://www.bananaip.com/intellepedia/patentability-requirements-in-india-patent-law-analysis/)
- [Section 3(d) Analysis - DrugPatentWatch](https://www.drugpatentwatch.com/blog/indian-pharmaceutical-patent-prosecution-the-changing-role-of-section-3d/)
- [CRI Guidelines 2025 - IPO](https://www.iam-media.com/article/indian-patent-office-releases-highly-anticipated-examination-guidelines-computer-related-inventions)
