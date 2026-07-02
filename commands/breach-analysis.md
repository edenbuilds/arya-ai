---
description: breach analysis command
---

# Breach Analysis Command

**Task**: Comprehensive analysis of contract breach with remedies evaluation, quantum calculation, and strategic recommendations.

## Workflow

1. **Gather Breach Context**:
   - **Contract details**: Type, parties, subject matter, consideration, date
   - **Breach specifics**: What was breached? When? By whom?
   - **Breach type**: Actual vs anticipatory, material vs non-material
   - **Current status**: Pre-litigation, litigation filed, judgment
   - **Your position**: Plaintiff (innocent party) or defendant (alleged breacher)

2. **Load Relevant Protocols**:
   - IL-CONTRACT-BREACH: Breach classification
   - IL-CONTRACT-DAMAGES: Hadley v. Baxendale, quantum calculation
   - IL-CONTRACT-SPECIFIC-PERFORMANCE: Viability assessment
   - IL-CONTRACT-INJUNCTION: Appropriateness evaluation
   - IL-CONTRACT-RESCISSION: Eligibility check
   - Special contract protocols (if applicable)

3. **Breach Classification**:

   **A. Actual vs Anticipatory** (Hochster v. De La Tour):
   - **Actual**: Failure to perform when due
   - **Anticipatory**: Repudiation before due date
     - Innocent party options: (1) Sue immediately OR (2) Affirm and wait (risk: frustration)

   **B. Material vs Non-Material**:
   - **Material**: Goes to root of contract → Can terminate + damages
   - **Non-Material**: Minor breach → Damages only (cannot terminate)

   **C. Condition vs Warranty** (Sale of Goods Act):
   - **Condition breach**: Essential term → Reject goods + damages OR accept + damages
   - **Warranty breach**: Non-essential → Damages only

4. **Remedies Analysis** (Use contract-remedies-expert agent):

   **A. Damages Calculation** (Section 73-75):
   
   **Hadley v. Baxendale Framework**:
   - **Limb 1 (Natural Consequences)**: Reasonably foreseeable loss
     - Formula: Market price - Contract price (if non-delivery)
     - Example: Contract Rs. 10L, market Rs. 12L → Damages Rs. 2L
   
   - **Limb 2 (Special Damages)**: Parties knew at contract formation
     - Example: Seller knew buyer needed for specific contract → Loss from that contract recoverable
   
   **Duty to Mitigate** (Section 73 proviso):
   - Must take reasonable steps to minimize loss
   - Failure to mitigate → Damages reduced

   **Liquidated Damages** (Section 74):
   - If contract specifies amount → Court awards reasonable compensation (not exceeding stipulated)
   - Genuine pre-estimate upheld (Kailash Nath Associates)

   **Sale of Goods Formulas**:
   - Section 57 (buyer): Market price - Contract price
   - Section 61 (seller): Contract price - Market price (or resale price)

   **B. Specific Performance Viability** (Sections 10-20 Specific Relief Act):
   - Threshold: Damages inadequate? Unique property?
   - Section 14 exclusions: Personal service, standard goods?
   - Discretionary factors: Clean hands, laches, hardship?
   - Viability score: 0-10 (use contract-remedies-expert framework)

   **C. Injunction Appropriateness** (Sections 36-42):
   - **Temporary** (Order 39): Prima facie case + balance of convenience + irreparable injury?
   - **Permanent**: Negative covenant (Section 42 - Lumley v. Wagner)?
   - Section 37 exclusions apply?

   **D. Rescission Eligibility** (Section 64):
   - Grounds: Fraud, misrepresentation, material breach?
   - Disqualifiers: Affirmation, lapse of time, third party rights, impossibility of restitution?
   - Section 75: Rescission + damages available?

5. **Defenses Analysis** (If defendant):

   **Performance Excuses**:
   - Section 56 impossibility/frustration
   - Force majeure clause
   - Other party's breach (prevented performance)

   **Validity Defenses**:
   - Contract void (minor, unlawful object, mutual mistake)
   - Contract voidable (coercion, fraud, misrepresentation, undue influence)

   **Contributory Breach**:
   - Other party also breached
   - Set-off/counterclaim possible

   **Mitigation Failure**:
   - Plaintiff failed to mitigate loss
   - Damages should be reduced

6. **Strategic Analysis Output**:

```
## Breach Analysis Report

### Breach Summary
- **Contract**: [Type - e.g., Sale of Goods Agreement dated DD/MM/YYYY]
- **Parties**: [Plaintiff] vs [Defendant]
- **Breached Obligation**: [Specific term breached]
- **Breach Date**: [DD/MM/YYYY]
- **Your Position**: Plaintiff (innocent party) / Defendant (alleged breacher)

### Breach Classification

#### Type
- **Actual** ✓ / **Anticipatory** ☐
- **Material** ✓ / **Non-Material** ☐
- **Condition** ✓ / **Warranty** ☐ (if Sale of Goods)

#### Analysis
[Detailed analysis of breach type, severity, and statutory basis]

**Statutory Basis**: Section 39 (anticipatory breach) / Section 73 (damages) / Section 12-13 Sale of Goods Act (condition/warranty)

**Effect**: 
- Plaintiff can [terminate contract / continue + claim damages / both]
- Defendant's obligation [discharged / continues / both]

### Remedies Evaluation

#### 1. Damages (Section 73-75)

**Quantum Calculation**:

**Limb 1 - Natural Consequences** (Section 73):
- [Description of loss]: Rs. [amount]
- Calculation: [Formula/reasoning]
- **Subtotal**: Rs. [amount]

**Limb 2 - Special Damages** (Section 73):
- [Description of special loss]: Rs. [amount]
- Basis: [Parties knew at contract formation]
- **Subtotal**: Rs. [amount]

**Less: Mitigation Deduction**:
- Plaintiff's duty to mitigate (Section 73 proviso)
- [Steps taken / should have taken]
- Deduction: Rs. [amount]

**Liquidated Damages** (if applicable - Section 74):
- Stipulated amount: Rs. [amount]
- Ceiling effect: Court awards reasonable (not exceeding stipulated)

**TOTAL DAMAGES CLAIM**: Rs. [amount]

**Viability**: ✓ Always available (if breach proved)

#### 2. Specific Performance (Sections 10-20 Specific Relief Act)

**Viability Score**: [X/10]

| Factor | Score | Analysis |
|--------|-------|----------|
| Subject Matter (unique?) | [/3] | [Land/unique goods/standard goods] |
| Section 14 Exclusions | [/2] | [Personal service? Standard goods?] |
| Plaintiff's Conduct | [/2] | [Clean hands? Laches?] |
| Hardship Balance | [/2] | [Plaintiff loss vs Defendant hardship] |
| Damages Adequacy | [/1] | [Inadequate / Adequate] |
| **TOTAL** | **[X/10]** | |

**Interpretation**:
- 9-10: **Highly viable** (pursue specific performance)
- 6-8: **Viable** (consider specific performance + damages alternative)
- 3-5: **Marginal** (damages may be better)
- 0-2: **Not viable** (pursue damages only)

**Recommendation**: [Pursue / Don't pursue specific performance]

#### 3. Injunction (Sections 36-42)

**Temporary Injunction** (Order 39 Rule 1-2):
- **Prima Facie Case**: ✓/✗ [Analysis]
- **Balance of Convenience**: ✓/✗ [Plaintiff vs Defendant hardship]
- **Irreparable Injury**: ✓/✗ [Cannot be compensated by money?]
- **Result**: All three satisfied ✓ / Not satisfied ✗

**Permanent Injunction** (Section 36-42):
- **Negative Covenant** (Section 42): ✓/✗ [Lumley v. Wagner principle applicable?]
- **Section 37 Exclusions**: ✓/✗ [Any exclusion applies?]
- **Recommendation**: [Pursue / Don't pursue injunction]

#### 4. Rescission (Section 64)

**Grounds Present**: ✓/✗
- Fraud (Section 17): ✓/✗
- Misrepresentation (Section 18): ✓/✗
- Material Breach (Section 39): ✓/✗

**Disqualifiers**:
- Affirmation: ✓/✗ [Continued performance? Lapse of time?]
- Third Party Rights: ✓/✗ [Bona fide purchaser?]
- Impossibility of Restitution: ✓/✗ [Can return benefit?]

**Result**: Eligible ✓ / Not Eligible ✗

**Section 75**: Rescission + Damages available (for fraud/breach cases)

### Strategic Recommendation

**Primary Remedy**: [Damages / Specific Performance / Injunction / Rescission]

**Justification**: [Reasoning based on viability, quantum, success probability]

**Alternative Remedies** (plead in alternative):
1. [Alternative 1]
2. [Alternative 2]

**Quantum Prediction**:
- **Expected Recovery**: Rs. [amount]
- **Success Probability**: [percentage]%
- **Timeline**: [months to judgment]

**Pleading Strategy**:
- **Prayer 1**: [Primary remedy]
- **Prayer 2**: [Damages in addition / alternative]
- **Prayer 3**: [Interim relief - temporary injunction if needed]

### Defenses Analysis

[If defendant position]

**Available Defenses**:
1. **[Defense 1]**: [Analysis + statutory basis]
2. **[Defense 2]**: [Analysis + statutory basis]

**Counterclaim Potential**: ✓/✗
- [If other party also breached / contributory factors]

**Set-Off**: ✓/✗
- [Amount defendant can set off against claim]

### Evidence Required

**For Plaintiff**:
1. **Contract**: [Original/copy, properly stamped]
2. **Proof of Breach**: [Correspondence, delivery receipts, etc.]
3. **Proof of Loss**: [Invoices, market price evidence, financial records]
4. **Mitigation Evidence**: [Steps taken to minimize loss]

**For Defendant**:
1. **Performance Evidence**: [If claiming performed]
2. **Excuse Evidence**: [Force majeure, impossibility]
3. **Contributory Breach**: [Other party's breach prevented performance]

### Timeline and Limitation

- **Limitation Period**: 3 years from breach (Article 113 Limitation Act 1963)
- **Breach Date**: [DD/MM/YYYY]
- **Limitation Expires**: [DD/MM/YYYY]
- **Urgency**: [Time remaining]

**Immediate Actions**:
1. [Action 1 - e.g., Issue legal notice]
2. [Action 2 - e.g., Gather evidence]
3. [Action 3 - e.g., Attempt settlement]

### Cost-Benefit Analysis

| Item | Amount (Rs.) |
|------|--------------|
| **Expected Recovery** | [amount] |
| **Legal Costs** (estimated) | [amount] |
| **Court Fees** | [amount] |
| **Timeline** | [months] |
| **Net Benefit** | [recovery - costs] |

**Recommendation**: Pursue Litigation ✓ / Attempt Settlement ✓ / Abandon ✗

**Settlement Range**: Rs. [min] to Rs. [max] (based on risk-adjusted recovery)

### Summary

**Key Points**:
1. [Key point 1]
2. [Key point 2]
3. [Key point 3]

**Action Required**: [Immediate next steps]

**Legal Opinion**: [Brief conclusion on strength of case and recommended strategy]
```

7. **Follow-Up Actions**:
   - Draft legal notice (if pre-litigation)
   - File suit (if litigation decision made)
   - Calculate exact damages quantum with documentary proof
   - Engage contract-remedies-expert agent for detailed remedies quantification
   - Use contract-law-specialist agent for validity/interpretation issues

**Use contract-remedies-expert agent for complex damages calculations and multi-remedy scenarios.**

---
**Version**: 1.0.0
