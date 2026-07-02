---
description: contract review command
---

# Contract Review Command

**Task**: Comprehensive legal review of existing contracts or specific clauses for validity, enforceability, risks, and compliance.

## Workflow

1. **Input Contract**:
   - User provides contract text or specific clause
   - Or describes clause verbally

2. **Identify Contract Type and Stage**:
   - Type (sale, service, guarantee, bailment, agency, partnership, other)
   - Stage (draft, executed, performance ongoing, disputed)

3. **Load Relevant Protocols**:
   - Formation protocols (IL-CONTRACT-FORMATION, IL-CONTRACT-CAPACITY, IL-CONTRACT-FREE-CONSENT, IL-CONTRACT-LEGALITY)
   - Special contract protocols (based on type)
   - Remedies protocols (if breach/dispute context)

4. **Systematic Review Framework**:

   **A. Validity Check (Section 10 Elements)**:
   - ✓/✗ **Parties**: Identified, capacity verified (not minor, unsound mind)
   - ✓/✗ **Offer and Acceptance**: Clear, unconditional, communicated
   - ✓/✗ **Consideration**: Present (Rs. amount stated), past/present/future, real
   - ✓/✗ **Free Consent**: No coercion, fraud, misrepresentation, undue influence, mistake
   - ✓/✗ **Lawful Object**: Section 23 compliance (not forbidden, fraudulent, immoral, opposed to public policy)
   - ✓/✗ **Not Expressly Void**: Section 26-30 (restraint of marriage, trade, legal proceedings, wagering, uncertainty)
   - ✓/✗ **Certainty**: Section 29 (terms definite and ascertainable)
   - ✓/✗ **Possibility**: Performance possible

   **B. Clause-Specific Analysis**:
   
   **Restraint Clauses** (Section 27):
   - Non-compete: Post-employment void (Niranjan Shankar Golikari); during employment if reasonable
   - Sale of goodwill exception: Reasonable restraint valid
   - Geographic/time limits: Reasonableness assessment

   **Liquidated Damages** (Section 74):
   - Genuine pre-estimate or penalty? (Indian law: both enforceable as ceiling)
   - Reasonable amount? (Kailash Nath Associates: genuine pre-estimate upheld)
   - Effect: Court awards reasonable compensation not exceeding stipulated

   **Indemnity/Guarantee Clauses** (Sections 124-147):
   - 2 parties (indemnity) or 3 parties (guarantee)?
   - Co-extensive liability clause (Section 128)
   - Discharge conditions clear (Sections 133-141)?
   - Continuing vs specific guarantee (Section 129)

   **Termination Clauses**:
   - Grounds clear and lawful?
   - Notice period reasonable?
   - Consequences specified (return of property, payment of dues)?
   - Termination for convenience vs cause

   **Force Majeure Clauses**:
   - Events covered (acts of God, war, epidemic, government action)?
   - Notice requirements?
   - Effect (suspend performance or terminate)?
   - Broader than Section 56 frustration?

   **Arbitration Clauses** (Section 28 + Arbitration Act 1996):
   - Valid (not ouster of courts - dispute resolution only)
   - Seat/venue specified?
   - Arbitrator appointment mechanism?
   - Governing law stated?

   **Payment Terms**:
   - Amount clear and certain?
   - Schedule (advance, milestones, completion)?
   - Mode (bank transfer, cheque)?
   - Interest on delayed payment?

   **Performance Obligations**:
   - Who, what, when, where, how (Sections 37-50)?
   - Reciprocal promises (mutual/dependent/independent - Sections 51-58)?
   - Time of essence clause (if applicable)?

   **C. Risk Identification**:

   **Legal Risks**:
   - Unenforceability (void/voidable clauses)
   - Section 23 violation (unlawful object)
   - Section 27 violation (restraint of trade)
   - Ambiguity (Section 29 certainty)
   - Unfair terms (undue influence, unconscionable)

   **Commercial Risks**:
   - Unlimited liability exposure
   - No termination rights
   - Inadequate remedies
   - No force majeure protection
   - Weak dispute resolution clause

   **Compliance Risks**:
   - Stamp duty (state Stamp Act)
   - Registration (if immovable property - Registration Act 1908)
   - Regulatory approvals (sector-specific)
   - Tax implications

   **D. Missing Clauses**:
   - Essential clauses absent (subject matter, consideration, performance, termination)
   - Risk mitigation clauses absent (force majeure, limitation of liability, indemnity)
   - Dispute resolution absent or inadequate

5. **Review Output**:

```
## Contract Review Report

### Contract Details
- **Type**: [Contract type]
- **Parties**: [Party 1] and [Party 2]
- **Date**: [If executed]
- **Status**: [Draft / Executed / Performing / Disputed]

### Validity Assessment

#### Section 10 Compliance
- ✓ **Valid** / ⚠ **Voidable** / ✗ **Void**

**Element-by-Element Check**:
| Element | Status | Analysis |
|---------|--------|----------|
| Parties | ✓/✗ | [Capacity verified / Issue identified] |
| Offer & Acceptance | ✓/✗ | [Clear / Ambiguous] |
| Consideration | ✓/✗ | [Present / Absent / Inadequate] |
| Free Consent | ✓/✗ | [No vitiation / Coercion/Fraud/etc. suspected] |
| Lawful Object | ✓/✗ | [Lawful / Section 23 violation] |
| Not Expressly Void | ✓/✗ | [Compliant / Section 26-30 violation] |
| Certainty | ✓/✗ | [Certain / Vague - Section 29] |
| Possibility | ✓/✗ | [Possible / Impossible] |

**Overall**: [Valid and enforceable / Voidable with grounds / Void and unenforceable]

### Clause-Specific Analysis

#### [Clause Name - e.g., "Non-Compete Clause (Clause 8)"]
**Text**: "[Quote clause]"

**Analysis**:
- **Statutory Provision**: Section 27 Indian Contract Act
- **Validity**: ✓ Valid / ⚠ Problematic / ✗ Void
- **Reasoning**: [Post-employment non-compete generally void per Niranjan Shankar Golikari; recommend removal or limitation to during-employment only]
- **Risk Level**: 🔴 High / 🟡 Medium / 🟢 Low
- **Recommendation**: [Specific action - remove, revise, clarify]

[Repeat for each significant clause]

### Risk Matrix

| Risk Category | Severity | Likelihood | Impact | Mitigation |
|---------------|----------|------------|--------|------------|
| **Legal**: Section 27 violation (non-compete) | 🔴 High | High | Clause void; no protection | Remove or limit to employment period |
| **Legal**: Ambiguous payment terms | 🟡 Medium | Medium | Disputes over amount/timing | Clarify with specific schedule |
| **Commercial**: No termination for convenience | 🟡 Medium | Low | Locked into unfavorable contract | Add termination clause with notice |
| **Compliance**: Stamp duty not mentioned | 🟢 Low | High | Penalty for non-stamping | Ensure proper stamping before execution |

### Missing Clauses

1. **Force Majeure**: ✗ Absent
   - **Impact**: No protection from supervening events beyond Section 56
   - **Recommendation**: Add comprehensive force majeure clause

2. **Limitation of Liability**: ✗ Absent
   - **Impact**: Unlimited exposure for consequential damages
   - **Recommendation**: Add cap on damages (except for fraud/gross negligence)

3. **Confidentiality**: ✗ Absent
   - **Impact**: No protection for trade secrets/proprietary information
   - **Recommendation**: Add if sensitive information exchanged

[Continue for all missing essential/recommended clauses]

### Recommendations

#### Critical (Immediate Action Required):
1. **Remove/Revise Non-Compete Clause**: Section 27 violation (void)
2. **Clarify Payment Terms**: Add specific amount, schedule, mode (Section 29 certainty)
3. **Add Stamp Duty**: Calculate and affix stamps before execution

#### Important (Should Address):
1. **Add Force Majeure Clause**: Protect from events beyond control
2. **Add Termination for Convenience**: Allow exit with notice
3. **Specify Dispute Resolution**: Add arbitration clause (Arbitration Act 1996)

#### Suggested (Enhance Protection):
1. **Add Limitation of Liability**: Cap damages exposure
2. **Add Confidentiality Clause**: If sensitive information
3. **Add Severability Clause**: Invalid clause doesn't void entire contract

### Revised Clause Suggestions

#### [For Each Problematic Clause]

**Original Clause 8 (Non-Compete)**:
"[Quote original]"

**Issue**: Post-employment restraint void (Section 27)

**Revised Clause**:
"During the term of this Agreement, the Employee shall not directly or indirectly engage in any business competing with the Employer within [geographic area]. This restriction shall cease upon termination of employment."

**Justification**: Limited to employment period (valid); geographic limit reasonable

[Repeat for each clause needing revision]

### Execution Checklist
- [ ] Revise problematic clauses per recommendations
- [ ] Add missing essential clauses
- [ ] Verify parties' capacity (not minor, unsound mind)
- [ ] Calculate stamp duty (per state Stamp Act)
- [ ] Determine registration requirement (if immovable property)
- [ ] Both parties review revised draft
- [ ] Execute with witnesses (2 per party)
- [ ] Affix stamps and register (if required)

### Summary
**Overall Assessment**: [Strong / Acceptable with Revisions / Weak - Major Issues]

**Key Concerns**: [Top 3 issues]

**Action Required**: [Critical actions before execution / Recommended improvements]

**Legal Opinion**: [Brief conclusion on enforceability and risk level]
```

6. **Follow-Up Options**:
   - Provide revised clause drafts for identified issues
   - Use `/draft-contract` to create entirely new agreement
   - Use `contract-law-specialist` agent for deeper analysis of specific clauses
   - Use `contract-remedies-expert` agent if breach/dispute context

**Use contract-law-specialist agent for complex legal interpretation questions.**

---
**Version**: 1.0.0
