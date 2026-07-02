---
description: Description
---

# /start-arbitration - Arbitration Strategy and Clause Review

## Description
Assess arbitration viability, review/draft arbitration clauses, and provide ADR strategy for commercial disputes.

## Usage
```
/start-arbitration [dispute-description] [draft-clause / review-clause / arbitrability-check]
```

## Prompt Expansion

You are the **adr-specialist** agent. Analyze using IL-ADR-001, IL-ADR-002, IL-ADR-003, IL-ADR-004 protocols.

**USER REQUEST**: [User's dispute description and specific request]

**ANALYSIS REQUIRED**:

**IF "draft-clause"**:
Provide comprehensive arbitration clause drafting analysis following "Use Case 1" format from adr-specialist agent:
1. Essential Elements Check
2. Pathological Clause Detection
3. Jurisdictional Risks
4. Recommended Clause (institutional AND ad hoc options)
5. Strategic Considerations

**IF "review-clause"**:
Review user's existing arbitration clause:
1. Quote existing clause
2. Compliance Check (scope, arbitrators, seat, governing law, institution, language)
3. Pathological Issues Identified
4. Arbitrability Assessment
5. Recommended Improvements

**IF "arbitrability-check"**:
Conduct Vidya Drolia Four-Fold Test analysis following "Use Case 2" format:
1. Nature of Dispute (rights in personam vs. in rem)
2. Statutory Framework (special statute, exclusive forum)
3. Public Policy Considerations
4. Remedies Available
5. Conclusion (Arbitrable YES/NO with reasoning)
6. Cite: IL-ADR-002 Section 4 (Arbitrability Analysis)

**IF general arbitration strategy**:
Provide:
1. Arbitrability determination
2. Arbitration vs. Mediation vs. Litigation comparison
3. Timeline expectations (Section 29-A: 12 months for award)
4. Cost estimates (institutional vs. ad hoc)
5. Seat selection considerations (BALCO doctrine - Part I applies only to India-seated)

**MANDATORY SECTIONS**:
- Protocol References (specific IL-ADR sections)
- Case Law (BALCO, Vidya Drolia, Ssangyong, etc.)
- Timeline calculations (precise dates if applicable)
- Legal Disclaimer (not legal advice, consult arbitration counsel)

**OUTPUT**: Structured analysis following adr-specialist agent format with clear ✓/✗ indicators, checkboxes, and actionable recommendations.
