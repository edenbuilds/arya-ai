---
description: Description
---

# /check-jurisdiction - Jurisdiction Analysis Command

## Description
Determine correct court jurisdiction (pecuniary, territorial, subject-matter) for filing civil suit under CPC.

## Usage
```
/check-jurisdiction [claim-amount] [brief-facts-including-locations]
```

## Prompt Expansion

You are the civil-procedure-specialist agent. Analyze jurisdiction using IL-CPC-001 protocol.

**JURISDICTION ANALYSIS (CPC Sections 15-20, Commercial Courts Act Section 2-7):**

1. **PECUNIARY JURISDICTION** (Based on claim value)
   - **Claim Amount:** ₹[specify]
   - **Court Fee:** ₹[calculate as per state Court Fees Act - typically 2-7% ad valorem]

   **Forum Determination:**
   - If < ₹3 lakhs AND non-commercial → **District Court** (regular civil court)
   - If ≥ ₹3 lakhs AND commercial dispute → **Commercial Court** (district level) OR **Commercial Division** (High Court if within original jurisdiction)
   - If ≥ ₹3 lakhs BUT non-commercial → **District Court** (or High Court within original jurisdiction if very high value)

2. **SUBJECT-MATTER JURISDICTION**
   **Is this a "Commercial Dispute"?** (Section 2(1)(c) Commercial Courts Act)

   Check if dispute arises from:
   □ Transactions of merchants/bankers/traders
   □ Commercial contracts (distribution, franchising, licensing, JV, shareholders, tech, IP with value)
   □ Infrastructure/construction contracts
   □ Export/import, carriage of goods
   □ Financing/banking/insurance
   □ Partnership (non-family)
   □ IT/software/e-commerce
   □ IP rights (with specified value)

   **EXCLUSIONS:**
   □ Immovable property for exclusive residence
   □ Consumer disputes (go to Consumer Forum)
   □ Oppression & Mismanagement (Companies Act - NCLT)
   □ Succession/testamentary

   **Commercial Dispute?** [Yes/No]
   **Specified Value ≥₹3 lakhs?** [Yes/No]

   → If BOTH Yes: **Commercial Court/Division jurisdiction**

   **Special Jurisdictions:**
   - **RERA:** Real estate homebuyer disputes → RERA Tribunal (concurrent with civil court)
   - **Consumer Forum:** B2C disputes → District/State/National Consumer Commission
   - **Arbitration:** If arbitration clause → Section 9/34/37 applications in court (Commercial Court if ≥₹3 lakhs)

3. **TERRITORIAL JURISDICTION** (Sections 16-20 CPC)
   **Multiple Options - Plaintiff Can Choose:**

   **Section 16: Immovable Property Disputes**
   - **Exclusive:** Where property situated
   - No choice - MUST file where property located

   **Section 17: Compensation for Wrongs (Torts)**
   - Where wrong committed, OR
   - Where defendant resides/carries business

   **Section 18: Other Suits (Default)**
   - Where defendant resides/carries business, OR
   - Where cause of action wholly/partly arose

   **Section 19: Contracts**
   - Where defendant resides/carries business, OR
   - Where cause of action wholly/partly arose, OR
   - Where contract was entered into, OR
   - Where contract to be performed (if specified)

   **Section 20: Multiple Defendants / Multiple Causes of Action**
   - If multiple defendants in different jurisdictions → File where ANY defendant resides (with court permission)
   - If multiple causes of action → File where ANY cause arose

   **Analyze User's Situation:**
   - Defendant Location: [City/State]
   - Property Location (if applicable): [City/State]
   - Cause of Action Locations: [Where events occurred]
   - Contract Execution Location (if applicable): [City/State]
   - Contract Performance Location (if applicable): [City/State]

   **RECOMMENDED FORUM(S):**
   1. [Primary choice - explain why]
   2. [Alternative choice(s) - explain]

4. **RES JUDICATA CHECK** (Section 11 CPC)
   - Has this matter been previously decided between same parties on same subject matter? [Yes/No]
   - If Yes → Court has no jurisdiction (doctrine of res judicata - matter already adjudicated)

5. **FORUM NON CONVENIENS** (Section 24 CPC)
   - Even if jurisdiction exists, is there a more convenient forum?
   - Section 24: Court can transfer to another competent court if:
     - Serving ends of justice
     - Witnesses/evidence in another location
     - Parties agree

6. **COMMERCIAL COURTS SPECIFIC**
   If Commercial Court jurisdiction:
   - **Pre-Institution Mediation (Section 12-A):** MANDATORY (unless exception)
     - Exceptions: Urgent interim relief, summary suits, execution, admiralty
     - Must obtain certificate of non-settlement before filing
     - Timeline: 3-5 months
   - **No Regular Civil Court:** Section 8 bars jurisdiction of courts below Commercial Court
   - **Specified Value Calculation (Section 12):**
     - Consideration value in contract, OR
     - Market value of subject matter, OR
     - Aggregate of multiple reliefs (if same transaction)

7. **PRACTICAL STRATEGIC CONSIDERATIONS**
   - **Home Court Advantage:** Filing where plaintiff located (if permitted)
   - **Defendant's Convenience:** May affect settlement prospects
   - **Witness/Evidence Location:** Where most evidence is
   - **Court Efficiency:** Some courts faster than others (e.g., Commercial Courts vs. regular)
   - **Cost:** Travel, accommodation for hearings

8. **CHALLENGING JURISDICTION**
   If defendant, challenge jurisdiction by:
   - **Before written statement:** File application to reject plaint (Order VII Rule 11) OR return plaint (Order VII Rule 10)
   - **Grounds:**
     - No territorial jurisdiction (wrong court)
     - No pecuniary jurisdiction (value threshold issue)
     - No subject-matter jurisdiction (e.g., not commercial dispute)
     - Res judicata (previously decided)

9. **JURISDICTION SUMMARY**
   **Pecuniary:** [Court type based on value]
   **Territorial:** [Location options with analysis]
   **Subject-Matter:** [Commercial/Special jurisdiction if applicable]

   **RECOMMENDED FILING LOCATION:**
   [Specific court name and location with rationale]

   **ALTERNATIVE OPTIONS:**
   [If multiple territorial options exist]

10. **PROTOCOL REFERENCES**
    - IL-CPC-001: CPC Fundamentals and Jurisdiction
    - IL-COMMERCIAL-001: Commercial Courts Act (if applicable)

**OUTPUT:** Provide clear jurisdiction determination with recommended forum and strategic considerations.
