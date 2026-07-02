---
id: IL-CORP-RELATED-PARTY-TRANSACTIONS
version: 1.0.0
category: corporate_law
subcategory: board_management
sections:
  - Related Party Definition
  - RPT Identification and Disclosure
  - Board Approval Requirements
  - Shareholder Approval Requirements
  - Audit Committee Role
  - Exemptions and Thresholds
  - Ordinary Course of Business Test
  - Arms Length Pricing
  - Penalty for Non-Compliance
  - Best Practices
dependencies:
  - IL-CORP-BOARD-MEETINGS (Board approval procedure)
  - IL-CORP-AUDIT-COMMITTEE (Audit committee approval)
  - IL-CORP-DIRECTOR-DUTIES (Section 184 disclosure)
related_protocols:
  foundation:
    - IL-COMPANIES-ACT (Companies Act 2013, Section 188)
    - IL-CORP-SHAREHOLDERS-RIGHTS (Shareholder approval via special resolution)
  procedural:
    - IL-CORP-SHAREHOLDER-AGREEMENTS (Related party provisions in SHA)
landmark_cases:
  - Vodafone International Holdings v. Union of India (2012) 6 SCC 613 (RPT disclosure)
  - Serious Fraud Investigation Office v. Ramalinga Raju (2015) (Satyam fraud - RPT manipulation)
---

# RELATED PARTY TRANSACTIONS - INDIAN CORPORATE LAW

## OVERVIEW

Related Party Transactions (RPTs) pose significant conflict-of-interest risks as they involve transactions between the company and persons who can influence company decisions. The Companies Act 2013 introduced stringent disclosure and approval requirements to prevent abuse of RPTs for self-dealing, profit diversion, and asset stripping.

**LEGISLATIVE INTENT**:
- Prevent directors/promoters from benefiting at company's expense
- Ensure RPTs conducted at arms-length terms (fair market value)
- Mandate independent oversight (Audit Committee, independent directors)
- Protect minority shareholders through disclosure and approval

**LEGAL FRAMEWORK**:
- **Companies Act 2013**: Section 188 (RPT approval), Section 184 (Disclosure of interest), Section 177 (Audit Committee)
- **Companies (Meetings of Board and its Powers) Rules 2014**: Rule 15 (RPT exemptions)
- **SEBI LODR Regulations 2015**: Regulation 23 (for listed companies - stricter requirements)
- **Accounting Standards**: AS-18 / Ind AS 24 (Related Party Disclosures in financials)

---

## 1. DEFINITION OF RELATED PARTY

### 1.1 Related Party (Section 2(76))

**Section 2(76)**: "Related party" means:

**Category 1: Directors and Key Managerial Personnel (KMP)**
```
(a) Director or KMP of the company
(b) Director or KMP of holding/subsidiary/associate company
```

**Category 2: Relatives of Directors/KMP**
```
(c) Firm in which director/manager/KMP or relative is partner
(d) Private company in which director/KMP/relative is director or shareholder
(e) Public company where director/KMP/relative is director and holds ≥2% paid-up share capital
(f) Body corporate where director/KMP/relative is director and holds ≥2% paid-up share capital
(g) Body corporate where ≥50% of voting power is controlled by director/KMP/relative or two or more related parties together
(h) Any person on whose advice/directions/instructions director/board is accustomed to act
```

**Category 3: Entities with Significant Influence**
```
(i) Holding/subsidiary/associate company
(j) Subsidiary of holding company (sister companies)
(k) Investing company or venturer (joint venture partner)
```

**"Relative" Definition (Section 2(77))**:
```
Relative means:
1. Spouse
2. Father (including step-father)
3. Mother (including step-mother)
4. Son (including step-son)
5. Son's wife
6. Daughter
7. Daughter's husband
8. Brother (including step-brother)
9. Sister (including step-sister)
```

### 1.2 Practical Examples of Related Parties

**Example 1: Director's Family Members**:
```
Company: ABC Pvt Ltd
Director: Mr. A (Managing Director, 30% shareholder)

Related Parties:
✓ Mr. A (director himself)
✓ Mrs. A (spouse)
✓ Mr. A's father, mother
✓ Mr. A's son, daughter, son's wife, daughter's husband
✓ Mr. A's brother, sister

Transactions with ANY of these persons = Related Party Transaction
```

**Example 2: Director's Other Companies**:
```
Director: Mr. A (director in ABC Pvt Ltd)

Related Party Entities:
✓ XYZ Pvt Ltd (Mr. A is director and holds 10% equity)
✓ PQR Services LLP (Mr. A is designated partner)
✓ LMN Industries Ltd (Mr. A is director and holds 3% equity - public company)
✗ DEF Ltd (Mr. A holds 1% equity, not director) - NOT related party (threshold <2%)

Transactions between ABC Pvt Ltd and XYZ/PQR/LMN = RPT
Transaction between ABC Pvt Ltd and DEF = Not RPT
```

**Example 3: Holding-Subsidiary Relationship**:
```
Holding Company: Parent Ltd (holds 60% equity in Subsidiary Ltd)
Subsidiary Company: Subsidiary Ltd
Sister Company: Sister Ltd (Parent Ltd holds 70% equity)

Related Parties from Subsidiary Ltd's perspective:
✓ Parent Ltd (holding company)
✓ Sister Ltd (subsidiary of holding company)

Transaction between Subsidiary Ltd and Parent Ltd = RPT
Transaction between Subsidiary Ltd and Sister Ltd = RPT
```

---

## 2. RELATED PARTY TRANSACTIONS REQUIRING APPROVAL (Section 188)

### 2.1 Transactions Covered by Section 188

**Section 188(1)**: Following transactions with related parties require board/shareholder approval:

```
(a) SALE, PURCHASE, OR SUPPLY OF GOODS OR MATERIALS
    - Purchase of raw materials from director's company
    - Sale of finished goods to related party

(b) SELLING OR DISPOSING OF, OR BUYING, PROPERTY OF ANY KIND
    - Purchase/sale of land, building, machinery
    - "Property" includes movable and immovable property

(c) LEASING OF PROPERTY OF ANY KIND
    - Office premises leased from director's company
    - Equipment leased to related party

(d) AVAILING OR RENDERING OF ANY SERVICES
    - Consulting services, IT services, administrative services
    - Management services, marketing services

(e) APPOINTMENT OF RELATED PARTY TO ANY OFFICE OR PLACE OF PROFIT
    - Appointing director's son as employee (if salary >₹2.5 lakh/month)
    - Appointing director's relative as consultant

(f) UNDERWRITING SUBSCRIPTION OF SECURITIES
    - Related party underwrites company's securities issue

(g) ANY OTHER TRANSACTION AS PRESCRIBED
    - Rules may prescribe additional transactions
```

### 2.2 Thresholds for Approval

**Approval Authority Based on Transaction Value**:

| Transaction Type | Board Approval | Shareholder Approval (Special Resolution) |
|---|---|---|
| **Sale/Purchase/Supply of Goods** | ₹1 crore OR 10% of turnover, whichever LOWER | >10% of turnover OR >₹100 crore, whichever LOWER |
| **Leasing of Property** | ₹1 crore OR 10% of turnover OR 10% of net worth, whichever LOWER | >10% of net worth OR >₹100 crore, whichever LOWER |
| **Availing/Rendering Services** | ₹50 lakh OR 10% of turnover, whichever LOWER | >10% of turnover OR >₹50 crore, whichever LOWER |
| **Appointment to Office of Profit** | Remuneration >₹2.5 lakh/month | N/A (Board approval sufficient) |

**Example - Threshold Calculation**:
```
Company: ABC Ltd
Annual Turnover: ₹50 crore
Net Worth: ₹30 crore

Transaction: Purchase of goods from director's company (₹6 crore per annum)

Threshold Analysis:
- Board Approval Threshold: LOWER of (₹1 crore OR 10% of ₹50 crore = ₹5 crore) = ₹1 crore
- Shareholder Approval Threshold: LOWER of (10% of ₹50 crore = ₹5 crore OR ₹100 crore) = ₹5 crore

Transaction Value: ₹6 crore
- Exceeds Board Approval Threshold (₹1 crore) ✓
- Exceeds Shareholder Approval Threshold (₹5 crore) ✓

REQUIRED APPROVALS:
1. Audit Committee recommendation ✓
2. Board approval (interested director cannot vote) ✓
3. Shareholder approval via SPECIAL RESOLUTION (interested shareholders cannot vote) ✓
```

---

## 3. BOARD APPROVAL PROCESS

### 3.1 Audit Committee Recommendation (Section 177)

**Section 177(4)(iv)**: Audit Committee must review and approve all related party transactions BEFORE board approval.

**Audit Committee Composition**:
- Minimum 3 directors
- Majority: Independent directors
- All members: Non-executive directors
- Listed companies: 2/3rd independent directors

**Audit Committee Review**:
1. Verify transaction is in ordinary course of business (if claimed)
2. Verify arms-length pricing (fair market value)
3. Review justification, commercial rationale
4. Assess conflict of interest, impact on minority shareholders
5. Recommend approval/rejection to board

**Example - Audit Committee Recommendation**:
```
AUDIT COMMITTEE RECOMMENDATION

Transaction: Office lease from Director A's company (₹80 lakh per annum)

Audit Committee Review (Meeting dated June 10, 2024):

Present:
- Independent Director 1 (Chair)
- Independent Director 2
- Non-Executive Director 3

Analysis:
1. Ordinary Course: Office lease is in ordinary course of business ✓
2. Market Rent: Comparable properties in area rent for ₹75-85 lakh per annum
3. Arms Length: Proposed rent ₹80 lakh is within market range ✓
4. Commercial Rationale: Company needs office space, existing premises inadequate
5. Conflict: Director A has pecuniary interest (100% ownership of lessor company)

RECOMMENDATION:
Audit Committee RECOMMENDS approval of office lease at ₹80 lakh per annum, subject to:
(a) 3-year lock-in period with annual 5% escalation
(b) 90-day termination notice by either party
(c) Rent review after 3 years based on prevailing market rates

Approved Unanimously (3/3 members voted YES)
```

### 3.2 Board Approval (Section 188(1))

**Board Resolution Requirements**:
- Ordinary resolution (simple majority of eligible directors)
- **Interested directors cannot vote** (Section 184(2))
- Quorum: Disinterested directors only (minimum 2 disinterested directors)

**Board Resolution Contents**:
1. Description of transaction (parties, nature, value, duration)
2. Commercial rationale, benefit to company
3. Audit Committee recommendation
4. Confirmation: Ordinary course of business + Arms-length terms (if applicable)
5. Authorization: Officers authorized to execute documents

**Example - Board Resolution**:
```
RESOLUTION NO. 12/2024-25: APPROVAL OF RELATED PARTY TRANSACTION

The Board considered the proposal to lease office premises from M/s. Property Holdings Pvt Ltd (company owned 100% by Director A) for a period of 3 years at an annual rent of ₹80,00,000.

Director A disclosed his interest in the transaction as 100% shareholder and director of Property Holdings Pvt Ltd.

The Board noted the Audit Committee's recommendation dated June 10, 2024, which recommended approval after verifying:
(a) Transaction is in ordinary course of business
(b) Rent is at arms-length (market rate ₹75-85 lakh per annum)

RESOLVED THAT:
1. The Board approves leasing office premises at [address] from M/s. Property Holdings Pvt Ltd for 3 years commencing July 1, 2024 at an annual rent of ₹80,00,000 plus applicable taxes.

2. The transaction is in the ORDINARY COURSE OF BUSINESS and on ARMS-LENGTH TERMS.

3. The Managing Director is authorized to execute the lease agreement and all related documents.

VOTING:
Present: Directors A, B, C, D, E (5 directors)
Interested Director: A (cannot vote per Section 184(2))
Eligible Voters: B, C, D, E (4 directors)
Votes: YES (4), NO (0)
Resolution PASSED unanimously (100% of eligible voters)
```

---

## 4. SHAREHOLDER APPROVAL REQUIREMENTS

### 4.1 When Shareholder Approval Required

**Section 188(1)**: Shareholder approval (special resolution) required if RPT exceeds thresholds:

```
Transaction Type                          Shareholder Approval Threshold
----------------------------------------- -------------------------------------
Sale/Purchase/Supply of Goods             >10% turnover OR >₹100 crore (lower)
Leasing of Property                       >10% net worth OR >₹100 crore (lower)
Availing/Rendering Services               >10% turnover OR >₹50 crore (lower)
```

**Special Resolution Requirements**:
- 75% majority of votes cast
- Interested shareholders CANNOT vote (Section 188(1)(ii))
- Notice must disclose: Nature, value, terms, commercial rationale

### 4.2 Voting Restrictions (Section 188(1)(ii))

**Interested Shareholders Cannot Vote**:
```
The following shareholders CANNOT VOTE on RPT special resolution:
1. Related party shareholder (if the related party is a shareholder)
2. Directors whose relatives are interested
3. Key managerial personnel whose relatives are interested
```

**Example - Interested Shareholder Voting**:
```
Company: ABC Pvt Ltd
Shareholders:
- Director A: 40% equity
- Director A's brother: 10% equity
- Public Shareholders: 50% equity (25 shareholders)

Transaction: Purchase of land from Director A for ₹5 crore (exceeds shareholder approval threshold)

General Meeting for RPT Approval:
- Total Shareholding: 100%
- Interested Shareholders: Director A (40%) + Director A's brother (10%) = 50%
- Eligible Voters: Public Shareholders (50%)

Voting:
- Public Shareholders: 35% voted YES, 10% voted NO, 5% abstained
- Result: 35% YES out of 45% votes cast = 77.8% approval
- Threshold: 75% required
- Resolution PASSED ✓

If Director A's brother had voted (incorrectly):
- Total votes cast: 95% (45% public + 50% interested)
- Resolution would be VOID (interested shareholders voted)
```

### 4.3 Explanatory Statement (Section 102)

**Notice Must Include Explanatory Statement**:
```
Companies Act 2013, Section 102: Explanatory statement must set out:
1. Material facts concerning RPT
2. Nature of concern/interest of director/KMP/related party
3. Commercial rationale, benefit to company
4. Any other information material to decision
```

**Example - Explanatory Statement**:
```
EXPLANATORY STATEMENT PURSUANT TO SECTION 102

Item No. 5: Approval of Related Party Transaction (Land Purchase)

The Board of Directors proposes to purchase land measuring 2 acres at [location] from Mr. A (Managing Director and 40% shareholder) for a consideration of ₹5,00,00,000.

COMMERCIAL RATIONALE:
The company requires land for establishing a new manufacturing facility. The proposed land is ideally located near existing facility, with good connectivity and infrastructure. The purchase will enable vertical integration and increase production capacity by 50%.

VALUATION:
Independent valuation by registered valuer: ₹4.8 crore to ₹5.2 crore
Proposed purchase price: ₹5 crore (within valuation range, arms-length)

NATURE OF INTEREST:
Mr. A is the Managing Director holding 40% equity in the company. He is the owner of the land being purchased. Mr. A has pecuniary interest in the transaction.

Mr. A and his relatives (holding 10% equity) shall NOT VOTE on this resolution.

The Board recommends the resolution for approval of members.

By Order of the Board
For ABC Private Limited

Company Secretary
Date: July 1, 2024
```

---

## 5. EXEMPTIONS FROM SECTION 188 (Rule 15)

### 5.1 Transactions NOT Requiring Approval

**Companies (Meetings of Board) Rules 2014, Rule 15**: Following RPTs are EXEMPT from Section 188 approval:

```
EXEMPT TRANSACTIONS:

(1) Transactions between holding company and wholly-owned subsidiary
    - Holding owns 100% equity in subsidiary
    - No minority shareholder protection needed

(2) Transactions between two wholly-owned subsidiaries of same holding
    - Sister companies with common 100% holding
    - Example: Parent Ltd owns 100% of Sub A and Sub B → Transaction between Sub A and Sub B exempt

(3) Transactions in ordinary course of business at arms-length
    - Must satisfy BOTH conditions (ordinary course AND arms-length)
    - Board must pass resolution confirming both conditions

(4) Loans to employees (including directors as employees) per company policy
    - Housing loans, vehicle loans, education loans
    - Within approved HR policy limits
```

**IMPORTANT**: Listed companies have stricter rules under SEBI LODR (fewer exemptions).

### 5.2 Ordinary Course of Business Test

**What is "Ordinary Course of Business"?**

Business activities that are:
1. **Regular and Routine**: Part of company's normal operations
2. **Consistent with Business Model**: Aligned with company's objects (MOA)
3. **Not One-Time/Extraordinary**: Recurring transactions (not exceptional deals)

**Examples**:

| Transaction | Company Business | Ordinary Course? |
|---|---|---|
| Purchase of raw materials from related party supplier | Manufacturing company | ✓ YES (regular purchase) |
| Sale of goods to related party distributor | Manufacturing company | ✓ YES (regular sales) |
| Office lease from related party | Any company | ✓ YES (all companies need office space) |
| Purchase of land from director | Manufacturing company | ✗ NO (capital expenditure, not routine) |
| Loan to director's company | Non-banking company | ✗ NO (lending not part of business unless NBFC) |
| IT services from related party | Any company | ✓ YES (all companies need IT support) |

**Landmark Case - ICICI Bank v. Prakash Kaur (2008)**:
```
Facts: Bank provided loan to related party. Claimed transaction in ordinary course (bank's business is lending).
Held: Transaction in ordinary course IF:
(a) Type of transaction is part of business, AND
(b) Terms are usual terms (not exceptional/preferential terms)
Principle: "Ordinary course" requires both nature AND terms to be ordinary.
```

### 5.3 Arms-Length Pricing Test

**What is "Arms-Length"?**

Transaction at **fair market value** (price that independent third parties would agree to in open market).

**Arms-Length Pricing Methods**:

1. **Comparable Uncontrolled Price (CUP)**:
   - Compare with price charged to unrelated third parties
   - Example: Company sells Product X to related party at ₹100/unit. Sells same product to unrelated customers at ₹95-105/unit → Arms-length ✓

2. **Market Benchmarking**:
   - Compare with prevailing market rates
   - Example: Office rent to related party at ₹80 lakh/year. Market rent for comparable properties ₹75-85 lakh/year → Arms-length ✓

3. **Independent Valuation**:
   - Engage registered valuer for property/asset transactions
   - Example: Purchase land from director at ₹5 crore. Independent valuation: ₹4.8-5.2 crore → Arms-length ✓

4. **Cost Plus Method**:
   - Cost + reasonable markup
   - Example: Related party provides services at cost (₹10 lakh) + 15% markup = ₹11.5 lakh. Industry markup 10-20% → Arms-length ✓

**Example - Arms-Length Analysis**:
```
Transaction: Purchase of software development services from director's company

Related Party Charges: ₹50 lakh per annum (5 developers × ₹10 lakh each)

Market Benchmarking:
- Market rate for software developers: ₹8-12 lakh per annum per developer
- Related party charging: ₹10 lakh per developer (midpoint of market range)

Conclusion: Transaction at ARMS-LENGTH ✓

If Related Party Charged ₹15 lakh per developer:
- Rate above market range (₹8-12 lakh)
- NOT arms-length ✗
- Shareholder approval required (cannot claim exemption)
```

---

## 6. DISCLOSURE REQUIREMENTS

### 6.1 Disclosure to Board (Section 184)

**Section 184(1)**: Every director must disclose nature of concern/interest in:
- Any contract/arrangement with company
- Any body corporate (where director has significant influence)

**Timing of Disclosure**:
1. At first board meeting after becoming interested
2. At first board meeting after interest arises
3. General notice at start of financial year (for continuing interests)

**General Notice Format**:
```
GENERAL NOTICE UNDER SECTION 184(2)

To: The Board of Directors, ABC Pvt Ltd

I, [Name], Director (DIN: XXXXXXXX), hereby give GENERAL NOTICE that I am interested in the following entities and any transactions between these entities and the company shall be deemed transactions in which I have an interest:

1. XYZ Pvt Ltd - Director and 40% shareholder
2. PQR Services LLP - Designated Partner
3. Supplier Co Ltd - Director

This notice shall be in force for the financial year 2024-25. I undertake to abstain from voting on any Board resolutions concerning transactions with the above entities.

Signed: [Name]
Date: April 1, 2024
```

### 6.2 Disclosure in Board's Report (Section 134)

**Section 134(3)(h)**: Board's Report must contain:
- Details of contracts/arrangements with related parties (pursuant to Section 188(1))
- Form AOC-2 annexed (particulars of RPTs)

**Form AOC-2 Contents**:
```
FORM AOC-2: Related Party Transactions

(Pursuant to Section 134(3)(h) and Rule 8(2) of Companies (Accounts) Rules 2014)

1. Name of related party: XYZ Pvt Ltd
2. Nature of relationship: Company in which Director A is director and shareholder (40%)
3. Nature of transaction: Purchase of raw materials
4. Duration: April 1, 2024 to March 31, 2025
5. Value of transaction: ₹3,50,00,000
6. Salient terms: Market price, 30-day credit period
7. Date of approval by Board: June 15, 2024
8. Amount paid as advance: Nil
9. Date of shareholders' approval (if required): N/A (within board approval threshold)
10. Arms-length justification: Market rate benchmarking (₹X per kg, market range ₹Y-Z per kg)
```

### 6.3 Disclosure in Financial Statements (AS-18 / Ind AS 24)

**Accounting Standards**: Financial statements must disclose:
1. Names of related parties and nature of relationship
2. Description of RPTs (nature, value)
3. Outstanding balances (receivables, payables)
4. Terms and conditions of RPTs

**Example - Financial Statement Note**:
```
NOTE 30: RELATED PARTY TRANSACTIONS

A. Related Parties:
   1. Key Managerial Personnel:
      - Mr. A (Managing Director)
      - Ms. B (CFO)
      - Mr. C (Company Secretary)

   2. Entities where KMP has significant influence:
      - XYZ Pvt Ltd (Director A holds 40%)
      - PQR Services LLP (Director A is partner)

B. Transactions with Related Parties (FY 2024-25):

   Purchase of Goods:
   - XYZ Pvt Ltd: ₹3.50 crore (FY 2023-24: ₹2.80 crore)

   Rent Paid:
   - PQR Services LLP: ₹0.80 crore (FY 2023-24: ₹0.75 crore)

   Remuneration to KMP:
   - Mr. A (MD): ₹1.20 crore (FY 2023-24: ₹1.10 crore)
   - Ms. B (CFO): ₹0.60 crore (FY 2023-24: ₹0.55 crore)

C. Outstanding Balances:
   - Payable to XYZ Pvt Ltd: ₹0.30 crore (trade credit, 30 days)
   - Security deposit to PQR Services LLP: ₹0.20 crore (refundable)
```

---

## 7. LISTED COMPANY REQUIREMENTS (SEBI LODR)

### 7.1 SEBI LODR Regulation 23

**Stricter Requirements for Listed Companies**:

1. **Prior Approval**: All material RPTs require prior shareholder approval
   - "Material RPT": >10% of annual consolidated turnover OR >₹1,000 crore, whichever LOWER

2. **Related Party Definition Broader**: Includes promoters, promoter group entities

3. **No Interested Shareholder Voting**: Related party and entities controlled by related party cannot vote

4. **Audit Committee Omnibus Approval**: Can grant omnibus approval for repetitive RPTs (quarterly review)

5. **Disclosure to Stock Exchanges**: Within 2 days of board/shareholder approval

**Example - Material RPT for Listed Company**:
```
Company: ABC Ltd (listed on NSE)
Annual Consolidated Turnover: ₹500 crore

Material RPT Threshold: LOWER of (10% of ₹500 crore = ₹50 crore OR ₹1,000 crore) = ₹50 crore

Transaction: Purchase of goods from promoter group company for ₹60 crore per annum

Compliance:
1. Audit Committee approval ✓
2. Board approval (interested directors cannot vote) ✓
3. Shareholder approval via ORDINARY RESOLUTION (SEBI requirement, not special resolution) ✓
4. Disclosure to stock exchange within 2 days ✓
5. Promoter and promoter group cannot vote ✓
```

---

## 8. PENALTIES AND CONSEQUENCES

### 8.1 Penalties under Section 188

**Section 188(4)**: If RPT entered into without compliance:

```
CONSEQUENCES:

1. Contract VOIDABLE at option of board (can be rescinded)

2. Director Liability:
   - Refund gains made from RPT to company
   - Compensate losses caused to company

3. Criminal Penalty (if contravention deliberate):
   - Imprisonment: Up to 1 YEAR
   - Fine: ₹25,000 to ₹5,00,000
```

**Example - Voidable Contract**:
```
Scenario: Director A's company supplies goods to ABC Ltd at ₹120/unit (market rate ₹80/unit). Total supply ₹2 crore. No board/shareholder approval obtained.

Consequences:
1. Contract VOIDABLE: Board can rescind contract, refuse payment
2. Director A Liability:
   - Refund excess profit: (₹120 - ₹80) × quantity = ₹50 lakh
   - Compensate company for losses (if any)
3. Criminal Prosecution: If contravention found to be deliberate fraud → Imprisonment + fine
```

### 8.2 Interested Director Voting

**Section 184(2)**: If interested director votes on RPT:
```
Penalty:
- Fine: ₹1 LAKH per contravention

Consequence:
- Resolution voidable (if interested director's vote was decisive)
```

**Example**:
```
Board: 5 directors (A, B, C, D, E)
Quorum: 2 directors
Transaction: Approve loan to Director A's company

Voting:
- Director A voted YES (interested director - should not vote)
- Directors B, C voted YES
- Directors D, E voted NO
- Result: 4 YES (including A), 2 NO → Resolution PASSED

Analysis:
- If Director A had not voted: 3 YES (B, C), 2 NO (D, E) → Resolution STILL PASSED
- Director A's vote was NOT decisive
- Resolution VALID (but Director A liable for ₹1 lakh fine)

If Director A's vote was decisive:
- If only Directors B, D, E present: 2 YES, 2 NO (tie) → Resolution FAILS
- If Director A voted: 3 YES, 2 NO → Resolution PASSED
- Director A's vote was DECISIVE → Resolution VOIDABLE
```

### 8.3 Satyam Fraud Case (Serious Fraud Investigation Office v. Ramalinga Raju, 2015)

**Facts**:
- Ramalinga Raju (Chairman of Satyam Computer Services) siphoned ₹7,000+ crore via RPTs
- Inflated assets, revenues via fake invoices from related party companies
- Board unaware (Raju controlled board, no independent oversight)

**Held**:
- Raju convicted of fraud (Section 447), forgery, criminal conspiracy
- Sentenced to 7 years imprisonment
- Ordered to pay ₹5 crore penalty

**Principle**:
- RPT disclosure and approval requirements exist to prevent exactly this type of fraud
- Independent director oversight critical (Section 149 introduced post-Satyam)
- Audit committee scrutiny mandatory (Section 177 strengthened post-Satyam)

**Application**:
- Companies must establish robust RPT policies
- Audit committee must review ALL RPTs (not rubber-stamp approval)
- Independent valuations for material RPTs
- Whistleblower mechanism to report RPT violations

---

## 9. BEST PRACTICES FOR RPT GOVERNANCE

### 9.1 Related Party Transaction Policy

**Every company should adopt RPT Policy covering**:
1. Definition of related parties (aligned with Section 2(76))
2. Identification and disclosure procedure
3. Approval matrix (Audit Committee → Board → Shareholders)
4. Thresholds for different approval levels
5. Arms-length pricing methodology
6. Exemptions (if any)

**Sample Policy Excerpt**:
```
RPT POLICY - ABC PVT LTD

1. OBJECTIVE: Ensure all RPTs are conducted transparently, on arms-length terms, with proper disclosure and approval.

2. IDENTIFICATION: Directors/KMP shall disclose all related parties annually (by April 30) and update quarterly.

3. APPROVAL MATRIX:

   Value                          Approval Required
   ----------------------------- -----------------------------------------
   ≤₹10 lakh                     CFO approval (if ordinary course + arms-length)
   ₹10 lakh - ₹1 crore           Audit Committee + Board approval
   >₹1 crore (below threshold)   Audit Committee + Board approval
   >Threshold (Section 188)      Audit Committee + Board + Shareholder (special resolution)

4. ARMS-LENGTH PRICING:
   - Finance team to obtain market benchmarking/independent valuation
   - Audit Committee to review pricing justification
   - No RPT approved without arms-length pricing verification

5. QUARTERLY REVIEW: Audit Committee to review all RPTs entered during quarter (compliance check).
```

### 9.2 Annual RPT Review

**Audit Committee Responsibilities**:
1. **Annual Update**: Directors submit updated list of related parties (April)
2. **Omnibus Approval**: Approve repetitive RPTs for year (e.g., regular purchases within approved limits)
3. **Quarterly Review**: Review all RPTs entered during quarter
4. **Exception Reporting**: Investigate RPTs that violated policy/threshold

**Example - Omnibus Approval**:
```
AUDIT COMMITTEE OMNIBUS APPROVAL (FY 2024-25)

Transaction: Purchase of raw materials from XYZ Pvt Ltd (Director A's company)
Approval: Up to ₹4 crore per annum, quarterly instalments of ₹1 crore
Conditions:
(a) Ordinary course of business
(b) Market rate pricing (CFO to verify quarterly)
(c) Payment terms: 30-day credit (standard terms)
(d) Quarterly review by Audit Committee

Validity: April 1, 2024 to March 31, 2025
Review Dates: July 2024, October 2024, January 2025, April 2025

Approved: June 1, 2024
Audit Committee Members: Independent Directors 1, 2, 3 (unanimous)
```

### 9.3 Independent Valuation

**When to Obtain Independent Valuation**:
1. Property transactions (land, building)
2. Asset purchase/sale (machinery, intangible assets)
3. Material RPTs (>₹1 crore or >10% threshold)
4. Disputed transactions (where arms-length pricing questioned)

**Valuer Requirements**:
- Registered valuer under Companies Act 2013 (Rule 18)
- No conflict of interest (not related to related party)
- Report must detail valuation methodology, assumptions, range

**Example - Valuation Report Summary**:
```
INDEPENDENT VALUATION REPORT

Property: Land, 2 acres at [location]
Valuer: ABC Valuers (Registered Valuer No. IBBI/RV/05/2020/12345)
Date: June 1, 2024

Valuation Methodology:
1. Comparable Sales Method: ₹4.9 crore (based on 3 comparable sales in last 6 months)
2. Income Capitalization Method: ₹5.1 crore (based on rental yield)
3. Land Residual Method: ₹5.0 crore (based on development potential)

VALUATION RANGE: ₹4.8 crore to ₹5.2 crore
FAIR MARKET VALUE: ₹5.0 crore (midpoint)

Conclusion: Proposed purchase price of ₹5.0 crore is within valuation range and represents fair market value. Transaction at ARMS-LENGTH.

Signed: ABC Valuers
Date: June 1, 2024
```

---

## 10. PRACTICAL SCENARIOS

### Scenario 1: Office Lease from Director

```
Company: ABC Pvt Ltd
Director: Mr. A (owns property through XYZ Pvt Ltd, where A is director and 100% shareholder)
Transaction: Office lease at ₹60 lakh per annum

STEP 1: Identify Related Party
- XYZ Pvt Ltd is related party (Director A is director and shareholder)
- Transaction: Leasing of property → Covered by Section 188

STEP 2: Check Threshold
- Company turnover: ₹10 crore, Net worth: ₹5 crore
- Lease threshold: LOWER of (₹1 crore OR 10% of ₹10 crore = ₹1 crore OR 10% of ₹5 crore = ₹50 lakh) = ₹50 lakh
- Transaction value: ₹60 lakh > ₹50 lakh → Board approval required
- Shareholder threshold: LOWER of (10% of ₹5 crore = ₹50 lakh OR ₹100 crore) = ₹50 lakh
- Transaction value: ₹60 lakh > ₹50 lakh → Shareholder approval ALSO required

STEP 3: Audit Committee Approval
- Obtain market benchmarking (comparable properties rent for ₹55-70 lakh)
- Verify arms-length (₹60 lakh within range ✓)
- Audit Committee recommends approval

STEP 4: Board Approval
- Director A discloses interest
- Director A cannot vote
- Board approves resolution (disinterested directors vote)

STEP 5: Shareholder Approval
- Special resolution (75% majority required)
- Director A and relatives cannot vote
- Explanatory statement filed with notice
- Resolution passed with 80% approval (of eligible voters)

STEP 6: Documentation
- Lease agreement executed
- Form AOC-2 filed in Board's Report
- Disclosure in financial statements (Ind AS 24)
- ROC filing (Form MGT-14 within 30 days)
```

### Scenario 2: Purchase of Goods (Ordinary Course)

```
Company: Manufacturing Ltd
Director: Ms. B (director in Supplier Ltd, holds 5% equity)
Transaction: Purchase of raw materials from Supplier Ltd (₹80 lakh per annum)

STEP 1: Identify Related Party
- Supplier Ltd is related party (Director B is director and holds >2% equity)
- Transaction: Purchase of goods → Covered by Section 188

STEP 2: Check Exemption
- Ordinary course of business: Manufacturing company regularly purchases raw materials ✓
- Arms-length pricing: Market rate ₹75-85 lakh per annum, transaction at ₹80 lakh ✓
- BOTH conditions satisfied → Transaction EXEMPT (Rule 15)

STEP 3: Board Resolution Confirming Exemption
- Board passes resolution confirming:
  (a) Transaction in ordinary course of business
  (b) Transaction at arms-length terms
- Director B discloses interest, abstains from voting
- Resolution passed (no shareholder approval required due to exemption)

STEP 4: Documentation
- Disclosure in Form AOC-2 (in Board's Report)
- Disclosure in financial statements
- Quarterly review by Audit Committee (confirm pricing remains arms-length)
```

### Scenario 3: Appointment of Director's Relative

```
Company: Tech Pvt Ltd
Director: Mr. C (Managing Director)
Transaction: Appoint Mr. C's son as Senior Manager (salary ₹30 lakh per annum)

STEP 1: Identify Related Party
- Mr. C's son is related party (relative of director)
- Transaction: Appointment to office of profit (salary >₹2.5 lakh per month = ₹30 lakh/12 = ₹2.5 lakh/month exactly)

STEP 2: Check Threshold
- Threshold: ₹2.5 lakh per month → Transaction EXACTLY at threshold
- Interpretation: At threshold = Board approval required (conservative approach)

STEP 3: Audit Committee & Board Approval
- Audit Committee reviews:
  (a) Qualification: MBA from top institute, 5 years experience ✓
  (b) Market salary: Senior managers earn ₹25-35 lakh per annum ✓
  (c) Arms-length: ₹30 lakh within market range ✓
  (d) Nepotism concern: Appointment based on merit (qualification + experience)
- Audit Committee recommends approval
- Board approves (Director C discloses interest, abstains from voting)

STEP 4: Documentation
- Employment contract executed
- Disclosure in Form AOC-2
- Disclosure in financial statements (remuneration to related party)

NOTE: No shareholder approval required (appointment to office of profit does not trigger shareholder approval threshold per Section 188)
```

---

## STRATEGIC CONSIDERATIONS

### When to Seek Legal/Professional Advice

**Complex RPT Scenarios Requiring Expert Advice**:
1. **Large Material Transactions**: RPTs >₹10 crore or >50% of turnover/net worth
2. **Structured Transactions**: Multiple inter-linked RPTs that may circumvent thresholds
3. **Cross-Border RPTs**: Transactions with foreign related parties (transfer pricing, FEMA implications)
4. **Disputed Arms-Length Pricing**: When fair market value is unclear or disputed
5. **Post-Merger RPTs**: Newly-related parties after M&A (transition period issues)

### Red Flags for Audit Committees

**Indicators of Potentially Abusive RPTs**:
1. **Above-Market Pricing**: RPT pricing significantly above comparable market rates
2. **Circular Transactions**: Company A → Company B → Company C → Company A (round-tripping)
3. **Sudden Increase in RPT Volume**: 200%+ increase in RPT value year-over-year (without business justification)
4. **Non-Arm's Length Terms**: Interest-free loans, extended credit periods (not offered to third parties)
5. **Lack of Documentation**: No written contracts, informal arrangements
6. **Retroactive Approvals**: Seeking approval after transaction already executed

---

## COMPLIANCE CHECKLIST

**Annual Compliance (Start of Financial Year)**:
- [ ] Directors submit updated list of related parties (Form MBP-1)
- [ ] Company Secretary prepares consolidated related party register
- [ ] Audit Committee reviews RPT policy, updates if required
- [ ] Omnibus approvals granted for repetitive RPTs

**Transaction-Level Compliance**:
- [ ] Identify transaction and related party
- [ ] Check if exemption applicable (ordinary course + arms-length)
- [ ] Determine approval required (Audit Committee / Board / Shareholders)
- [ ] Obtain independent valuation (if material property/asset transaction)
- [ ] Audit Committee recommends (verify arms-length pricing)
- [ ] Board approves (interested director discloses, abstains from voting)
- [ ] Shareholder approval (if threshold exceeded, interested shareholders abstain)
- [ ] Execute transaction documents
- [ ] ROC filing (Form MGT-14 if required, within 30 days)

**Quarterly Compliance**:
- [ ] Audit Committee reviews all RPTs entered during quarter
- [ ] Verify compliance with omnibus approval limits
- [ ] Investigate any threshold violations or policy breaches

**Year-End Compliance**:
- [ ] Prepare Form AOC-2 (all RPTs for the year)
- [ ] Disclose RPTs in Board's Report (Section 134)
- [ ] Disclose RPTs in financial statements (Ind AS 24 / AS 18)
- [ ] Auditor reviews RPT disclosures (audit opinion)

---

## LEGAL DISCLAIMER

This protocol provides information on related party transactions under Indian law. It is for informational purposes only and does not constitute legal advice. Companies should consult qualified corporate lawyers, company secretaries, and chartered accountants for specific RPT compliance matters. Legal provisions and penalties are subject to amendments. SEBI regulations apply to listed companies with stricter requirements.

---

**Last Updated**: December 5, 2025
**Version**: 1.0.0
**Protocol ID**: IL-CORP-RELATED-PARTY-TRANSACTIONS
