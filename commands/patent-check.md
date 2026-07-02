---
description: Description
---

# /patent-check - Patentability Assessment

## Description
Assess whether invention meets patentability criteria under Patents Act 1970 (novelty, inventive step, industrial application, non-exclusion).

## Usage
```
/patent-check [invention-description]
```

## Prompt Expansion

You are the **ip-law-specialist** agent. Analyze using IL-IP-001 protocol.

**INVENTION**: [User's invention description]

**PATENTABILITY ANALYSIS** (Section 2(1)(j) Patents Act):

Conduct comprehensive three-part test:

1. **NOVELTY (New)** - Section 2(1)(l)
   - Prior art search (publications, public use anywhere in world)
   - Prior publication: YES/NO
   - Prior public use: YES/NO
   - **NO grace period** in India (unlike USA 12 months)
   - Conclusion: ✓ NOVEL / ✗ NOT NOVEL

2. **INVENTIVE STEP (Non-Obvious)** - Section 2(1)(ja)
   - Technical advance over prior art: YES/NO
   - Economic significance: YES/NO
   - Person skilled in art test: Would skilled person arrive at invention as obvious next step?
   - Conclusion: ✓ INVENTIVE / ✗ OBVIOUS

3. **INDUSTRIAL APPLICATION (Useful)** - Section 2(1)(ac)
   - Capable of being made/used in industry: YES/NO
   - Practical utility: YES/NO
   - Conclusion: ✓ INDUSTRIALLY APPLICABLE / ✗ PURELY THEORETICAL

4. **NON-EXCLUDED SUBJECT MATTER** (Sections 3, 4)
   Check each Section 3 exclusion:
   - Mathematical method/algorithm (Section 3(k))
   - Computer program per se (Section 3(k)) [BUT software with technical contribution MAY be patentable]
   - Business method (Section 3(k))
   - Medical treatment method (Section 3(h)) [BUT pharmaceutical products patentable]
   - New form of known substance WITHOUT enhanced efficacy (Section 3(d) - Evergreening)
   - Plant/animal variety (Section 3(i))
   - Traditional knowledge (Section 3(j))

   **IF PHARMACEUTICAL**:
   Section 3(d) Evergreening Check:
   - New salt/ester/polymorph/dosage form of known drug?
   - Enhanced known EFFICACY proved?
   - Novartis 2013 SC: Enhanced THERAPEUTIC efficacy (better clinical outcome) required
   - Improved bioavailability alone ≠ enhanced efficacy
   - Conclusion: ✓ ENHANCED EFFICACY SHOWN / ✗ EVERGREENING (NOT PATENTABLE)

**CONCLUSION**:
✅ PATENTABLE / ❌ NOT PATENTABLE

**IF PATENTABLE**:
- Prior art search required (Indian Patent Office, USPTO, EPO databases)
- File Provisional Specification (secure priority date)
- File Complete Specification within 12 months
- Request Examination within 48 months
- Timeline: 2-4 years typical for grant

**PROTOCOL REFERENCE**: IL-IP-001 Sections 2-3 (Patentability Criteria, Non-Patentable Subject Matter)

**LEGAL DISCLAIMER**: This analysis provides legal information about patentability criteria. It does NOT constitute patentability opinions or freedom-to-operate opinions. Patent prosecution requires expertise of registered patent agents. Consult qualified patent professionals before filing applications or commercializing inventions.
