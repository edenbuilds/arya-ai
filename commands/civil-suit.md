---
description: Analyze civil dispute, determine jurisdiction and maintainability, develop pleading strategy, assess interim relief prospects, and provide comprehensive litigation roadmap using CPC framework.
argument-hint: <dispute-description>
---

# Slash Command: /civil-suit - Comprehensive Civil Litigation Strategy

## Purpose
Analyze civil dispute, determine jurisdiction and maintainability, develop pleading strategy, assess interim relief prospects, and provide comprehensive litigation roadmap using CPC framework.

## Usage
```
/civil-suit <dispute-description>
```

## What This Command Does

When you invoke `/civil-suit`, I will systematically:

1. **Case Assessment:**
   - Analyze dispute facts and parties
   - Identify causes of action (breach of contract, specific performance, injunction, partition, etc.)
   - Determine applicable legal framework (CPC, Specific Relief Act, Limitation Act)

2. **Jurisdiction Analysis:**
   - Assess pecuniary jurisdiction (District vs High Court)
   - Determine territorial jurisdiction (Section 16-20 CPC)
   - Evaluate subject matter jurisdiction (civil court vs specialized tribunal)

3. **Limitation Period Calculation:**
   - Identify applicable Article (Limitation Act 1963)
   - Calculate limitation period from cause of action date
   - Advise on condonation of delay (if time-barred)

4. **Maintainability Assessment:**
   - Verify locus standi (standing to sue)
   - Check res judicata (prior adjudication on same matter)
   - Assess jurisdictional challenges

5. **Pleading Strategy:**
   - Draft comprehensive plaint/written statement framework
   - Structure material facts and legal arguments
   - Frame precise prayers for relief
   - Identify essential documents to file

6. **Interim Relief Prospects:**
   - Evaluate eligibility for temporary injunction (Order XXXIX)
   - Apply three-pronged test: prima facie case, balance of convenience, irreparable injury
   - Assess ex-parte ad-interim application viability
   - Recommend attachment/receiver strategies (Order XXXVIII, XL)

7. **Trial and Evidence Planning:**
   - Develop documentary evidence list (Order XI)
   - Identify witnesses and examination strategy
   - Plan trial timeline and milestones

8. **Execution Planning:**
   - Assess decree enforceability
   - Identify judgment debtor's assets (immovable, movable, bank accounts)
   - Recommend execution modes (Order XXI)

9. **Cost-Benefit Analysis:**
   - Estimate litigation costs vs dispute value
   - Assess probability of success
   - Evaluate settlement vs litigation trade-offs

10. **Alternative Remedies:**
    - Consumer forum (if consumer dispute)
    - Arbitration (if arbitration clause exists)
    - Specialized tribunals (RERA, NCLT, DRT)
    - Mediation/conciliation

## Example Usage

### Example 1: Specific Performance Suit
```
/civil-suit Builder agreed to sell flat for Rs. 80 lakhs. Sale agreement dated 1st Jan 2023. I paid Rs. 60 lakhs (75%). Builder now refusing to execute sale deed, wants to sell to someone else at higher price. Agreement registered. Property in Mumbai.
```

**Agent Response:**
```markdown
## Civil Litigation Strategy: Specific Performance Suit

### Case Overview
- **Parties:** You (Purchaser) vs Builder (Vendor)
- **Dispute:** Breach of contract to sell immovable property
- **Relief Sought:** Specific performance + permanent injunction
- **Property Location:** Mumbai
- **Agreement Value:** Rs. 80 lakhs
- **Payment Made:** Rs. 60 lakhs (75%)

### Jurisdiction Analysis
**Pecuniary Jurisdiction:**
- Suit value: Rs. 80 lakhs (property value)
- Forum: District Court, Mumbai (suits < Rs. 2 crores)
  - Alternative: Bombay High Court (original civil jurisdiction if > Rs. 2 lakhs)
  - Recommendation: District Court (lower court fees, faster disposition)

**Territorial Jurisdiction:**
- Property located in Mumbai → Mumbai courts have jurisdiction (Section 16 CPC)
- Builder's place of business (if Mumbai) → Additional jurisdiction (Section 20 CPC)

**Subject Matter Jurisdiction:**
- Civil court has jurisdiction (immovable property specific performance)
- RERA NOT applicable (sale agreement already executed, not under-construction project)

### Limitation Analysis
**Article 54: Specific Performance**
- **Limitation Period:** 3 YEARS
- **Starting Point:** Date of breach (when builder refused to execute sale deed)
- **Your Timeline:**
  - Agreement: 1st Jan 2023
  - Breach: [Date builder refused] (assume recent - within limitation)
- **Status:** WITHIN LIMITATION ✓
- **Condonation:** Not required

### Maintainability Assessment
**Locus Standi:** ✓ You have enforceable contract
**Res Judicata:** None (no prior suit on same matter)
**Jurisdictional Bar:** None (civil court jurisdiction clear)
**Conclusion:** SUIT MAINTAINABLE

### Cause of Action
1. **Breach of Contract:** Builder's refusal to execute sale deed (Transfer of Property Act Section 55)
2. **Specific Performance:** Specific Relief Act Section 10 (suit for specific performance)
3. **Part Performance:** Section 53A TPA (you have paid 75%, entitled to protection)

### Pleading Strategy

**Plaint Structure:**

**I. Parties**
1. Plaintiff: You (name, address)
2. Defendant: Builder (name, registered office)

**II. Jurisdiction**
3. Pecuniary: Rs. 80 lakhs (within District Court limits)
4. Territorial: Property in Mumbai
5. Valuation for court fees: Rs. 80 lakhs

**III. Facts (Material Facts):**
6. Agreement for sale executed on 1st Jan 2023 (Annex P-1)
7. Agreement registered vide Doc No. [___] dated [___]
8. Property description: Flat No. [___], [Address]
9. Total consideration: Rs. 80 lakhs
10. Payment schedule: [As per agreement]
11. Payment made till date: Rs. 60 lakhs (75%) with receipts (Annex P-2)
12. Time for execution of sale deed: [As per agreement - typically possession + balance payment]
13. Plaintiff ready and willing to pay balance Rs. 20 lakhs
14. Defendant refused to execute sale deed on [Date] via email/letter (Annex P-3)
15. Defendant attempting to sell to third party (if evidence available)
16. Plaintiff suffered mental agony and financial loss

**IV. Legal Grounds**
17. Specific Relief Act Section 10: Plaintiff entitled to specific performance
18. Transfer of Property Act Section 53A: Part performance protection (possession + payment)
19. Defendant in breach of contractual obligation

**V. Prayers for Relief:**

WHEREFORE, the Plaintiff most respectfully prays that this Hon'ble Court may be pleased to:
(a) Decree specific performance of the Agreement for Sale dated 1st Jan 2023;
(b) Direct the Defendant to execute and register the sale deed in favor of the Plaintiff within [30/60] days from the date of decree;
(c) Direct the Defendant to deliver vacant and peaceful possession of the property;
(d) Decree permanent injunction restraining the Defendant from selling/transferring the property to any third party;
(e) Award interest on Rs. 60 lakhs @ 12% per annum from date of breach till execution of sale deed;
(f) Award compensation for mental agony and financial loss: Rs. [5-10 lakhs];
(g) Award costs of the suit;
(h) Pass such other and further orders as this Hon'ble Court deems fit.

**Documents to File:**
- Annex P-1: Agreement for Sale (registered copy)
- Annex P-2: Payment receipts (Rs. 60 lakhs)
- Annex P-3: Builder's refusal letter/email
- Annex P-4: Title documents of property (if available)
- Annex P-5: Correspondence with builder

### Interim Relief Strategy

**Application for Temporary Injunction (Order XXXIX Rule 1-2):**

**Relief Sought:**
- Restrain Defendant from selling/transferring property to third party
- Restrain Defendant from creating any encumbrance on property

**Three-Pronged Test:**

**1. Prima Facie Case:** STRONG ✓
- Valid registered sale agreement
- 75% payment made (substantial part performance)
- Builder's clear refusal = breach
- Section 53A protection (part performance)

**2. Balance of Convenience:** IN FAVOR OF PLAINTIFF ✓
- Plaintiff paid Rs. 60 lakhs (significant investment at risk)
- Builder has other inventory (can sell other units)
- If sold to third party, plaintiff loses property (damages inadequate remedy)
- Builder not prejudiced (can receive balance Rs. 20 lakhs + sale deed execution)

**3. Irreparable Injury:** YES ✓
- Immovable property is UNIQUE (not fungible)
- Monetary damages cannot compensate loss of specific property
- Section 10 Specific Relief Act presumes inadequacy of compensation for immovable property
- If third party purchases in good faith, plaintiff's remedy extinguished

**Conclusion:** STRONG CASE for interim injunction

**Strategy:**
- File plaint WITH interim application (IA)
- Seek ex-parte ad-interim injunction (urgent - prevent third-party sale)
- Offer undertaking to:
  - Pay balance Rs. 20 lakhs into court (or escrow)
  - Not alienate property
  - Abide by final decree
- Likelihood of success: HIGH (70-80%)

### Trial and Evidence

**Documentary Evidence:**
1. Agreement for Sale (Annex P-1) - Prove contract
2. Payment receipts (Annex P-2) - Prove part performance
3. Refusal communication (Annex P-3) - Prove breach
4. Title documents - Prove Defendant's ownership
5. Readiness letters - Prove Plaintiff's readiness to perform

**Oral Evidence:**
1. Plaintiff's affidavit (examination-in-chief)
2. Witnesses (if any - e.g., person present during refusal discussion)

**Defendant's Likely Defenses:**
1. Time not of essence (delay in payment) - Counter: Ready and willing to pay balance
2. Plaintiff in breach (some covenant violated) - Counter: Substantial compliance, waiver
3. Agreement voidable (misrepresentation, fraud) - Counter: Registered agreement, 75% paid
4. Specific performance discretionary - Counter: Section 10 mandatory unless special circumstances

**Plaintiff's Counter:**
- Section 53A protection (possession + payment = no eviction)
- Section 16(c) Specific Relief Act (time NOT of essence unless expressly stated)
- Ready and willing to perform (tender balance payment)

### Execution Planning (If Decree Granted)

**Decree Content:**
- Direct Defendant to execute sale deed within 30/60 days
- If Defendant fails, Court empowered to execute (Section 32 Specific Relief Act)
- Permanent injunction against third-party sale

**Execution:**
- Obtain certified decree copy
- Deposit balance Rs. 20 lakhs as per decree
- If Defendant fails to execute, approach Registrar with court's endorsement
- Registrar registers sale deed (as if executed by Defendant)

### Cost-Benefit Analysis

**Litigation Costs (Estimate):**
- Court fees: Rs. 2.5 lakhs (ad valorem on Rs. 80 lakhs @ ~3%)
- Advocate fees: Rs. 2-5 lakhs (depending on seniority)
- Miscellaneous (filing, notary, certified copies): Rs. 50,000
- **Total:** Rs. 5-8 lakhs

**Timeline:**
- Interim injunction hearing: 2-4 weeks
- Trial completion: 1-2 years (if contested)
- Decree execution: 6 months after decree
- **Total:** 2-3 years (estimate)

**Probability of Success:** 75-80%
- Strong case (registered agreement, 75% payment)
- Part performance protection (Section 53A)
- Specific performance mandatory (Section 10 - unless special circumstances)

**Risk Factors:**
- If builder shows plaintiff's breach (e.g., delayed payment beyond grace period)
- If property value declined (court may award damages instead of specific performance - rare)
- If third party already purchased in good faith (bona fide purchaser for value without notice)

### Alternative Remedies

**1. Negotiated Settlement:**
- Offer: Execute sale deed + balance Rs. 20 lakhs payment
- Leverage: Threat of litigation + injunction (builder cannot sell to third party)
- Outcome: Faster, lower cost (no litigation fees)
- Timeline: 1-2 months
- **Recommendation:** ATTEMPT FIRST before filing suit

**2. Mediation (Pre-litigation):**
- Approach builder with mediation proposal
- Neutral third party facilitates settlement
- Cost: Rs. 50,000-1 lakh (mediator fees)
- Timeline: 30-60 days
- **Recommendation:** If settlement discussions initiated

**3. Arbitration (If Arbitration Clause Exists):**
- Check sale agreement for arbitration clause
- If exists, invoke arbitration (Section 8 Arbitration Act - court SHALL refer)
- Timeline: 12 months (faster than court litigation)
- Cost: Arbitrator fees (Rs. 2-5 lakhs)
- **Applicability:** Check agreement (if no clause, NOT available)

### Recommended Strategy

**Phase 1: Pre-Litigation (Weeks 1-4)**
1. Send legal notice to builder:
   - Demand execution of sale deed within 15 days
   - State readiness to pay balance Rs. 20 lakhs
   - Warn of legal action (specific performance suit + injunction)

2. Attempt settlement/mediation:
   - If builder responds positively, negotiate timeline
   - If builder unresponsive/refuses, proceed to litigation

**Phase 2: Litigation (If Phase 1 Fails)**
1. File plaint with interim injunction application (Week 5)
2. Seek ex-parte ad-interim injunction (same day/within 2-3 days)
3. Notice of motion hearing (2-4 weeks) - argue interim injunction
4. Trial (1-2 years)
5. Execution of decree (if granted)

**Phase 3: Parallel Track**
- Caveat filing: File caveat in District Court (prevent builder from obtaining ex-parte orders)
- Property search: Verify if builder has created third-party interests (encumbrance certificate)

### Final Recommendation

**Immediate Actions:**
1. Send legal notice (within 7 days)
2. File caveat (within 7 days - prevent ex-parte orders by builder)
3. Gather all documents (agreement, receipts, communications)
4. Attempt settlement (15-30 days)

**If Settlement Fails:**
5. File specific performance suit with interim injunction (Week 5-6)
6. Pursue interim injunction vigorously (prevents third-party sale)
7. Prepare for trial

**Probability Assessment:**
- **Settlement:** 40% (builder may agree if faced with injunction threat)
- **Interim Injunction:** 70-80% (strong case)
- **Final Decree:** 75-80% (specific performance likely granted)

**Overall Recommendation:** PROCEED WITH LITIGATION (high probability of success, property value justifies cost)

---

**Would you like me to:**
1. Draft the legal notice to builder?
2. Prepare the plaint and interim application?
3. Conduct settlement negotiation strategy?
4. Analyze builder's potential defenses in detail?
```

## Protocols Utilized

This command invokes and synthesizes:

- IL-CPC-BASICS.md - Civil procedure fundamentals, jurisdiction
- IL-CPC-PLEADINGS.md - Plaint structure, material facts
- IL-CPC-INTERIM-RELIEF.md - Temporary injunctions (Order XXXIX)
- IL-CPC-TRIAL.md - Evidence, witness examination
- IL-CPC-EXECUTION.md - Decree execution procedures
- IL-CPC-APPEALS.md - Appellate remedies
- IL-SPECIFIC-RELIEF-ACT.md - Specific performance, injunctions (Sections 10, 14)
- IL-LIMITATION-ACT.md - Limitation periods, condonation
- IL-PROPERTY-TRANSFER-BASICS.md - Section 53A (part performance)
- IL-CONTRACT-LAW.md - Breach of contract, remedies
- IL-ARBITRATION-ACT.md - Arbitration vs litigation assessment

## Agent Used

**Primary Agent:** civil-litigation-strategist

The command delegates comprehensive analysis to the civil litigation strategist agent, which provides:
- Multi-layered jurisdiction analysis
- Strategic pleading development
- Interim relief tactical planning
- Trial and execution roadmaps
- Cost-benefit assessments
- Alternative dispute resolution evaluation

## Output Format

The command provides a structured litigation strategy memo including:
- Executive case overview
- Detailed jurisdiction and limitation analysis
- Maintainability assessment
- Comprehensive pleading framework
- Interim relief prospects with three-pronged test application
- Trial and evidence strategy
- Execution planning
- Cost estimates and timeline projections
- Probability of success assessment
- Alternative remedies evaluation
- Phased action recommendations

---

**Version:** 1.0  
**Last Updated:** December 2025  
**Domain:** Civil Procedure (CPC 1908, Specific Relief Act 1963, Limitation Act 1963)
