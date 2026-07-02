---
description: Determine if dispute qualifies for Commercial Court jurisdiction under Commercial Courts Act, 2015.
argument-hint: [brief-dispute-description] [amount-involved]
---

# /commercial-court-check - Commercial Dispute Classification

## Description
Determine if dispute qualifies for Commercial Court jurisdiction under Commercial Courts Act, 2015.

## Usage
```
/commercial-court-check [brief-dispute-description] [amount-involved]
```

## Prompt Expansion

You are the commercial-litigation-specialist agent. Analyze using IL-COMMERCIAL-001 protocol.

**COMMERCIAL DISPUTE CLASSIFICATION:**

**TWO-PART TEST:**
1. **Specified Value ≥ ₹3 lakhs?**
2. **"Commercial Dispute" under Section 2(1)(c)?**

Both must be YES for Commercial Court jurisdiction.

---

**PART 1: SPECIFIED VALUE CALCULATION (Section 12)**

**User's Claim Amount:** ₹[specify]

**Calculation Method:**
- If transaction has consideration → Value = consideration stated in contract
- If no consideration → Market value of subject matter
- If multiple reliefs from same transaction → Aggregate all
- Counterclaim value NOT added (each side's claim evaluated separately)

**Specified Value:** ₹[calculate]
**≥ ₹3 lakhs?** [Yes / No]

If NO → **Regular Civil Court** (not Commercial Court)
If YES → Proceed to Part 2

---

**PART 2: "COMMERCIAL DISPUTE" DEFINITION** (Section 2(1)(c))

**Does dispute arise out of:**

**Category A: Commercial Transactions**
□ Transactions of merchants/bankers/financiers/traders
□ Purchase/sale of goods (mercantile activity)
□ Mercantile agency
□ Factoring
□ Mercantile documents (bills of exchange, promissory notes)

**Category B: Commercial Contracts**
□ Trade and commerce contracts
□ Distribution agreements
□ Licensing agreements
□ Franchising
□ Consulting
□ Joint ventures
□ Shareholders agreements
□ Subscription/investment agreements
□ Technology development
□ Intellectual property rights (with Specified Value)

**Category C: Infrastructure & Construction**
□ EPC (Engineering, Procurement, Construction) contracts
□ Sub-contracting
□ Concession agreements
□ Power purchase agreements

**Category D: Carriage & Logistics**
□ Carriage of goods (road, rail, air, sea)
□ Warehousing
□ Logistics and supply chain

**Category E: International Trade**
□ Export/import transactions
□ Foreign trade
□ Letters of credit

**Category F: Financial Services**
□ Financing agreements
□ Banking services
□ Loan agreements
□ Securitization
□ Structured finance
□ Investment banking

**Category G: Insurance**
□ Insurance and reinsurance contracts

**Category H: Partnership**
□ Partnership agreements (excluding family partnerships)

**Category I: Technology & E-Commerce**
□ IT agreements
□ Software licensing
□ E-commerce transactions
□ Domain names
□ Digital services

**Category J: Intellectual Property**
□ Patents, trademarks, copyrights (with Specified Value)
□ Trade secrets
□ Designs

**Category K: Corporate**
□ Matters relating to listed companies (not oppression/mismanagement)

**Category L: Admiralty**
□ Admiralty and maritime law disputes

**EXCLUSIONS (Not Commercial Disputes):**
□ Immovable property transactions for **exclusive residence** use
□ Actions under **Consumer Protection Act** (consumer disputes)
□ Relief against **Oppression and Mismanagement** (Companies Act - NCLT)
□ **Testamentary or succession** matters

**Analysis of User's Dispute:**
[Map user's facts to categories above]

**Commercial Dispute?** [Yes / No - specify category]

---

**CONCLUSION:**

**Specified Value ≥ ₹3 lakhs:** [Yes/No]
**Commercial Dispute:** [Yes/No]

**RESULT:**
□ **COMMERCIAL COURT JURISDICTION** (Both yes)
   - File in: Commercial Court (district level) OR Commercial Division (High Court original jurisdiction areas)

□ **REGULAR CIVIL COURT** (One or both no)
   - File in: District Court or High Court (based on pecuniary jurisdiction)

---

**IF COMMERCIAL COURT JURISDICTION:**

**MANDATORY COMPLIANCE:**

1. **Pre-Institution Mediation (Section 12-A)**
   - **MANDATORY** unless exception applies
   - **Exceptions:** Urgent interim relief, summary suits (Order XXXVII), execution, admiralty
   - **Procedure:** File application with Mediation Centre → 3-5 months → Certificate of settlement/non-settlement
   - **If not done:** Plaint liable to rejection

2. **Strict Timelines**
   - **Written Statement:** 120 days ABSOLUTE (no extension beyond)
   - **Interim Applications:** 30-60 days disposal
   - **Trial Target:** 12-18 months

3. **Case Management Hearings (Order XV-A)**
   - First CMH: Within 4 weeks of summons
   - Proactive case management by court
   - Firm timelines set

4. **Modified CPC Procedures**
   - Evidence-in-chief by affidavit (Order XVIII)
   - Summary judgment possible (Order XIII-A)
   - Limited adjournments

5. **Appeals**
   - **75% deposit required** to file appeal (Section 13(1-A))
   - No second appeal (only SLP to Supreme Court)
   - Commercial Appellate Division

**STRATEGIC IMPLICATIONS:**

**Advantages:**
- Faster disposal (18-24 months avg vs. 5-10 years regular court)
- Specialized judges with commercial law expertise
- Strict timelines prevent delay tactics
- 75% deposit deters frivolous appeals by defendant

**Disadvantages:**
- 120-day written statement deadline strict (if defendant)
- Pre-institution mediation delays filing (3-5 months)
- 75% deposit burden (if appealing)
- No second appeal (finality)

**RECOMMENDATION:**
[Based on classification, provide strategic guidance]

---

**PROTOCOL REFERENCES:**
- IL-COMMERCIAL-001: Commercial Courts Act, 2015 Procedures
- IL-CPC-001: CPC Fundamentals and Jurisdiction (general jurisdiction)

**OUTPUT:** Provide clear classification with procedural implications and strategic considerations.
