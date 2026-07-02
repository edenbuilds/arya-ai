# Protocol: Prior Art Search Strategy

**Protocol ID**: PROT-IPL-010
**Version**: 1.0.0
**Domain**: Indian Patent Law
**Category**: Patentability Analysis
**Last Updated**: 2026-01-16

---

## Purpose

Comprehensive guide for conducting prior art searches for Indian patent applications, including database selection, search strategies, and documentation requirements for patentability, freedom-to-operate, and opposition/invalidity purposes.

---

## Activation Triggers

- Evaluating patentability of new invention
- Preparing patent application
- Freedom-to-operate analysis
- Opposition/revocation evidence gathering
- Due diligence in IP transactions

---

## Prerequisites

- Invention disclosure or technical description
- Understanding of relevant technology field
- Access to patent and non-patent databases
- Knowledge of IPC/CPC classification

---

## Core Process

### Step 1: Define Search Scope

#### Identify Key Elements:
1. **Technical features** - What the invention does
2. **Problem solved** - Technical challenge addressed
3. **Field of invention** - Technology domain
4. **Closest prior art** - Known existing solutions

#### Determine Search Purpose:

| Purpose | Scope | Date Range |
|---------|-------|------------|
| Patentability | Similar inventions | No time limit |
| FTO | In-force patents | Current + unexpired |
| Opposition | Anticipating prior art | Before priority date |
| Invalidity | All prior art | Before priority date |

### Step 2: Select Databases

#### Indian Patent Database:

**InPASS (Indian Patent Advanced Search System)**
- URL: https://iprsearch.ipindia.gov.in/publicsearch
- Coverage: All Indian patents and applications
- Features: Full-text search, Boolean operators, wildcards
- Best for: Indian prior art, Form 3 compliance check

**Limitations**:
- No bulk download
- Limited Boolean string length
- AND/OR fixed between entries

#### Global Patent Databases:

| Database | Coverage | Best For |
|----------|----------|----------|
| Espacenet | 130+ countries | European/global search |
| PATENTSCOPE | PCT applications | International filings |
| USPTO | US patents | American prior art |
| Google Patents | Multiple countries | Quick keyword search |
| The Lens | Global + scholarly | Comprehensive search |

#### Non-Patent Literature:

- Google Scholar
- PubMed (life sciences)
- IEEE Xplore (electronics/computing)
- ScienceDirect
- arXiv (physics, CS, math)
- ResearchGate
- University theses databases

### Step 3: Develop Search Strategy

#### Keyword Search:

1. **Primary Keywords**: Core technical terms
2. **Synonyms**: Alternative terminology
3. **Related Terms**: Adjacent concepts
4. **Translations**: For foreign databases

**Boolean Operators**:
- AND: Narrow results (term1 AND term2)
- OR: Broaden results (synonym1 OR synonym2)
- NOT: Exclude (term AND NOT exception)

**Wildcards**:
- `*` : Multiple characters (comput* = computer, computing, computational)
- `?` : Single character (defen?e = defense, defence)

#### Classification Search:

**IPC (International Patent Classification)**:
- 8 sections (A-H)
- Hierarchical structure
- Example: A61K 31/00 (Medicinal preparations)

**CPC (Cooperative Patent Classification)**:
- More detailed than IPC
- Used by EPO and USPTO

**Strategy**: Combine classification with keywords for targeted results.

### Step 4: Execute Search

#### Systematic Approach:

1. **Broad search first**: Identify relevant patent families
2. **Refine with classification**: Narrow to specific field
3. **Keyword variations**: Cover synonyms
4. **Date filters**: Apply as appropriate
5. **Assignee/applicant search**: Known competitors

#### InPASS Search Tips:

```
Field Options:
- Title
- Abstract
- Claims
- Full Specification
- Applicant Name
- Inventor Name
- Application Number
- IPC

Search Strategy:
1. Start with title/abstract keywords
2. Add IPC classification
3. Use wildcards for variations
4. Check applicant name for competitors
```

### Step 5: Analyze Results

#### For Each Relevant Document:

1. **Technical Disclosure**: What is taught?
2. **Priority Date**: Effective date of disclosure
3. **Claim Scope**: What is protected?
4. **Status**: Active, expired, pending?
5. **Relevance**: Impact on patentability/FTO

#### Comparison Chart:

```
| Feature | Invention | Prior Art 1 | Prior Art 2 | Prior Art 3 |
|---------|-----------|-------------|-------------|-------------|
| Element A | X | X | X | - |
| Element B | X | X | - | X |
| Element C | X | - | X | - |
| Element D | X | - | - | - |
```

### Step 6: Document Search

#### Search Report Should Include:

1. **Search strategy**: Keywords, classifications, databases
2. **Date of search**: Important for ongoing monitoring
3. **Documents found**: Citation details
4. **Relevance assessment**: Impact analysis
5. **Claim mapping**: Features vs. prior art
6. **Conclusion**: Patentability/FTO opinion

---

## Search Types by Purpose

### Patentability Search

**Objective**: Determine if invention is novel and non-obvious

**Scope**:
- All published prior art worldwide
- Patents and non-patent literature
- No date limitation for search

**Key Questions**:
- Is every claim element disclosed in single reference? (anticipation)
- Would combination be obvious to POSITA? (inventive step)

### Freedom-to-Operate Search

**Objective**: Identify in-force patents that may cover proposed activity

**Scope**:
- Focus on granted patents
- Current + unexpired
- India-specific for Indian operations

**Key Questions**:
- Do any claims cover proposed product/process?
- Can design-around be implemented?

### Opposition/Invalidity Search

**Objective**: Find prior art to challenge patent validity

**Scope**:
- Prior art dated before priority date
- Any public disclosure counts
- Including abandoned/expired applications

**Key Focus**:
- Section 8 compliance (foreign filings)
- Section 3 subject matter exclusions
- Best mode non-disclosure

---

## Quality Checklist

- [ ] Search purpose clearly defined
- [ ] Multiple databases searched
- [ ] Both patent and non-patent literature covered
- [ ] Classification codes utilized
- [ ] Keyword variations exhausted
- [ ] Results documented with citations
- [ ] Relevance analysis completed
- [ ] Search report generated

---

## Common Search Mistakes

1. **Single database reliance**: Miss relevant art
2. **Keyword-only search**: Miss classification hits
3. **Ignoring non-patent lit**: Critical for validity
4. **Wrong date filtering**: Missing relevant art
5. **Incomplete documentation**: Cannot reproduce search

---

## Search Report Template

```
PRIOR ART SEARCH REPORT

Subject: [Brief description of invention]
Search Purpose: [Patentability/FTO/Opposition]
Date of Search: [Date]
Searcher: [Name]

1. SEARCH STRATEGY

Keywords Used:
- Primary: [list]
- Synonyms: [list]
- Related: [list]

Classifications:
- IPC: [codes]
- CPC: [codes]

Databases Searched:
- [Database 1]: [date range]
- [Database 2]: [date range]
- [Database 3]: [date range]

2. SEARCH RESULTS SUMMARY

Total Documents Retrieved: [Number]
Relevant Documents: [Number]

3. RELEVANT PRIOR ART

Document 1:
- Citation: [Full citation]
- Priority Date: [Date]
- Relevance: [High/Medium/Low]
- Key Disclosure: [Summary]

[Repeat for each relevant document]

4. CLAIM MAPPING

[Feature comparison table]

5. CONCLUSION

[Patentability opinion / FTO assessment / Opposition viability]

6. LIMITATIONS

[Any known gaps in search coverage]
```

---

## Related Protocols

- PROT-IPL-011: Patentability Analysis
- PROT-IPL-040: Freedom-to-Operate Analysis
- PROT-IPL-006: Pre-Grant Opposition
- PROT-IPL-008: Patent Revocation

---

## Legal References

- Patents Act, 1970: Section 2(1)(l) - Prior art definition
- Manual of Patent Office Practice: Chapter on Examination

---

## Sources

- [InPASS Search Guide - BananaIP](https://www.bananaip.com/intellepedia/indian-patent-database-inpass-patent-search-guide/)
- [Patentability Search Guide - Mondaq](https://www.mondaq.com/india/patent/1617250/patentability-search-importance-process-tools-for-patents)
- [IP Databases Guide - IISc](https://iptel.iisc.ac.in/ip-databases/)
