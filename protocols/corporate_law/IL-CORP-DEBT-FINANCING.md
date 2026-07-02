---
id: IL-CORP-DEBT-FINANCING
version: 1.0.0
category: corporate_law
subcategory: corporate_finance
sections:
  - Types of Debt Financing
  - Term Loans
  - Working Capital Financing
  - External Commercial Borrowings (ECB)
  - Corporate Bonds
  - Inter-Corporate Deposits
  - Board Approvals and Limits
  - Security and Collateral
  - Debt Covenants
  - Default and Remedies
dependencies:
  - IL-CORP-BOARD-MEETINGS (Board approval for borrowing)
  - IL-CORP-DEBENTURES (Long-term debt instruments)
  - IL-CORP-RELATED-PARTY-TRANSACTIONS (Loans from related parties)
related_protocols:
  foundation:
    - IL-COMPANIES-ACT (Companies Act 2013, Section 180, 186)
    - IL-CORP-SHAREHOLDERS-RIGHTS (Shareholder approval for borrowing limits)
  procedural:
    - IL-IBC-CIRP-INITIATION (Debt default and insolvency)
landmark_cases:
  - State Bank of India v. Videocon Industries Ltd (2020) (Debt default and CIRP initiation)
  - ICICI Bank v. Prakash Kaur (2008) (Loan classification as RPT)
---

# DEBT FINANCING - INDIAN CORPORATE LAW

## OVERVIEW

Debt financing involves raising capital through borrowing (loans, bonds, debentures) that must be repaid with interest. Unlike equity, debt does not dilute ownership and interest is tax-deductible, but creates fixed repayment obligations and increases financial leverage. Companies use debt financing for capex, working capital, acquisitions, and refinancing.

**DEBT vs EQUITY**:

| Parameter | Debt | Equity |
|---|---|---|
| **Ownership** | No dilution (lenders have no voting rights) | Dilution (shareholders have voting rights) |
| **Repayment** | Fixed repayment schedule (principal + interest) | No repayment (permanent capital) |
| **Cost** | Interest (tax-deductible, so post-tax cost lower) | Dividend (not tax-deductible) + dilution cost |
| **Risk** | High leverage = high financial risk, default → insolvency | No default risk (no fixed payments) |
| **Control** | No control (unless covenants breached) | Shareholders control via voting |

**TYPES OF DEBT FINANCING**:
1. **Term Loans**: Bank loans for fixed tenure (1-10 years) with repayment schedule
2. **Working Capital Financing**: Short-term loans (overdraft, cash credit, bill discounting) for operations
3. **External Commercial Borrowings (ECB)**: Foreign currency loans from overseas lenders
4. **Corporate Bonds**: Listed debt securities (publicly traded bonds)
5. **Debentures**: Unlisted debt securities (private placement or public issue)
6. **Inter-Corporate Deposits (ICDs)**: Unsecured loans from one company to another

**LEGAL FRAMEWORK**:
- **Companies Act 2013**: Section 180 (Borrowing limits), Section 186 (Loans and investments by company)
- **Reserve Bank of India Act**: RBI regulations on ECB, ICD
- **SEBI (Issue and Listing of Debt Securities) Regulations 2008**: Corporate bonds
- **Insolvency and Bankruptcy Code 2016**: Debt default and insolvency

---

## 1. TERM LOANS

### 1.1 Term Loan Structure

**Definition**: Loan with fixed repayment schedule over specific tenure (1-10 years).

**Types by Tenure**:
```
SHORT-TERM LOAN: 1-3 years tenure
- Used for: Working capital, inventory, receivables financing
- Interest Rate: 9-12% per annum (floating rate, linked to MCLR)

MEDIUM-TERM LOAN: 3-7 years tenure
- Used for: Equipment purchase, moderate capex, business expansion
- Interest Rate: 10-13% per annum

LONG-TERM LOAN: 7-20 years tenure
- Used for: Large capex (plant, machinery, real estate), infrastructure projects
- Interest Rate: 11-14% per annum (project loans may have 15-20 year tenure)
```

**Example - Term Loan Structure**:
```
Company: Manufacturing Ltd
Loan: ₹50 crore term loan from SBI for machinery purchase
Tenure: 5 years
Interest Rate: 11.5% per annum (floating, MCLR + 2%)
Repayment: Quarterly installments (₹2.5 crore principal + interest)

Repayment Schedule (Quarterly):
Year 1: Q1-Q4: ₹2.5 cr principal + ₹1.44 cr interest (11.5% on ₹50 cr) = ₹3.94 cr per quarter
Year 2: Q1-Q4: ₹2.5 cr principal + ₹1.15 cr interest (11.5% on ₹40 cr average) = ₹3.65 cr per quarter
Year 3: Q1-Q4: ₹2.5 cr principal + ₹0.86 cr interest (11.5% on ₹30 cr average) = ₹3.36 cr per quarter
Year 4: Q1-Q4: ₹2.5 cr principal + ₹0.58 cr interest (11.5% on ₹20 cr average) = ₹3.08 cr per quarter
Year 5: Q1-Q4: ₹2.5 cr principal + ₹0.29 cr interest (11.5% on ₹10 cr average) = ₹2.79 cr per quarter

Total Interest Paid: ₹14.4 crore (28.8% of principal over 5 years)
```

### 1.2 Loan Documentation

**Key Loan Documents**:

**1. Sanction Letter**:
- Bank issues sanction letter (loan approved, subject to conditions)
- Contains: Loan amount, interest rate, tenure, repayment schedule, security, conditions precedent (CP), conditions subsequent (CS)

**2. Loan Agreement**:
- Legal contract between borrower (company) and lender (bank)
- Clauses: Disbursement, repayment, interest calculation, prepayment, default events, covenants

**3. Security Documents**:
- **Hypothecation Deed**: Charge over movable assets (machinery, inventory, receivables)
- **Mortgage Deed**: Charge over immovable property (land, building)
- **Pledge**: Physical possession of securities (shares, bonds) transferred to lender
- **Guarantee**: Personal guarantee by promoters, corporate guarantee by group companies

**4. Inter-Creditor Agreement (ICA)**:
- If multiple lenders (consortium lending), ICA governs priority, sharing of security, decision-making

**Example - Loan Documentation Checklist**:
```
Term Loan: ₹100 crore from consortium (SBI ₹50 cr, ICICI ₹30 cr, HDFC ₹20 cr)

Documents:
1. Sanction Letters (3 separate letters from SBI, ICICI, HDFC)
2. Loan Agreements (3 separate agreements)
3. Inter-Creditor Agreement (1 ICA among SBI, ICICI, HDFC - security sharing 50:30:20)
4. Hypothecation Deed (charge over machinery worth ₹150 cr)
5. Mortgage Deed (charge over factory land and building worth ₹80 cr)
6. Personal Guarantee (MD and 2 promoters guarantee ₹100 cr loan)
7. Corporate Guarantee (holding company guarantees ₹100 cr loan)

Security Coverage: ₹230 cr assets charged (machinery ₹150 cr + property ₹80 cr) for ₹100 cr loan = 2.3x coverage ✓
```

### 1.3 Conditions Precedent (CP) and Conditions Subsequent (CS)

**Conditions Precedent**: Must be satisfied BEFORE disbursement.

```
TYPICAL CPs:
1. Board resolution approving loan
2. Shareholder resolution approving borrowing (if required under Section 180)
3. Execution of loan documents (loan agreement, security documents)
4. Creation of security (CERSAI registration for hypothecation/mortgage)
5. Insurance policies (property, plant, machinery, key man insurance)
6. Submission of financial statements, projections
7. No material adverse change (MAC) since sanction
```

**Conditions Subsequent**: Must be satisfied AFTER disbursement (ongoing compliance).

```
TYPICAL CSs:
1. Submit quarterly financials (within 45 days of quarter-end)
2. Submit annual audited financials (within 6 months of FYE)
3. Maintain debt service coverage ratio (DSCR) ≥1.5x
4. Maintain debt-equity ratio ≤2:1
5. Do not create additional security on charged assets (negative pledge)
6. Do not sell/transfer charged assets without lender consent
7. Do not change nature of business
8. Maintain net worth ≥₹50 crore
```

**Breach of CS**: Lender can recall loan (demand immediate repayment), invoke security (sell charged assets).

---

## 2. WORKING CAPITAL FINANCING

### 2.1 Types of Working Capital Facilities

**1. Cash Credit (CC)**:
- **Limit**: Sanctioned limit (e.g., ₹10 crore)
- **Drawing**: Withdraw up to limit as needed (revolving facility)
- **Interest**: Charged only on amount drawn (not on full limit)
- **Security**: Hypothecation of inventory, receivables (stock and debtors)
- **Tenure**: Renewed annually

**2. Overdraft (OD)**:
- **Limit**: Overdraw from current account up to sanctioned limit
- **Drawing**: Flexible (draw/repay as needed)
- **Interest**: Charged on daily outstanding balance
- **Security**: Fixed deposit, shares, property
- **Tenure**: Renewed annually

**3. Bill Discounting/Factoring**:
- **Mechanism**: Company sells receivables to bank at discount (immediate cash)
- **Discount**: Bank charges 12-15% per annum on receivable value
- **Recourse**: With recourse (company liable if customer doesn't pay) or without recourse (bank bears risk)
- **Example**: ₹1 crore receivable due in 90 days → Bank pays ₹97 lakh immediately (3% discount for 90 days)

**4. Letter of Credit (LC)**:
- **Purpose**: Payment guarantee for imports (bank pays supplier if company defaults)
- **Mechanism**: Company opens LC with bank, supplier ships goods, bank pays supplier upon presenting documents
- **Security**: Margin money (10-25% of LC value) + general security
- **Tenure**: 90-180 days (import transaction cycle)

**Example - Cash Credit Utilization**:
```
Company: Textile Ltd
CC Limit: ₹15 crore (interest rate 11% per annum)
Security: Hypothecation of inventory (₹25 cr) and receivables (₹20 cr)

Month 1 (Peak Season): Utilization ₹14 crore (93% of limit)
Interest: ₹14 cr × 11% ÷ 12 months = ₹12.83 lakh

Month 2 (Off Season): Utilization ₹6 crore (40% of limit)
Interest: ₹6 cr × 11% ÷ 12 months = ₹5.5 lakh

Month 3 (Moderate): Utilization ₹10 crore (67% of limit)
Interest: ₹10 cr × 11% ÷ 12 months = ₹9.17 lakh

Total Interest (3 months): ₹12.83 + ₹5.5 + ₹9.17 = ₹27.5 lakh

Advantage: Interest paid only on utilized amount (not on full ₹15 cr limit), flexible repayment
```

### 2.2 Working Capital Assessment

**Operating Cycle Method**:
```
Operating Cycle = Inventory Days + Receivables Days - Payables Days

Working Capital Requirement = (Revenue × Operating Cycle Days) ÷ 365

Example:
Company: FMCG Ltd
Annual Revenue: ₹500 crore
Inventory Days: 60 days (raw material 20 days, WIP 15 days, finished goods 25 days)
Receivables Days: 45 days (credit sales, 45-day credit period)
Payables Days: 30 days (supplier credit)

Operating Cycle: 60 + 45 - 30 = 75 days
Working Capital Requirement: (₹500 cr × 75) ÷ 365 = ₹102.7 crore

Bank CC Limit: 80% of working capital = ₹82 crore (balance ₹20.7 cr from own funds)
```

**Turnover Method (Tandon Committee)**:
```
NWCR (Net Working Capital Requirement) = 25% of Projected Annual Turnover (for manufacturing)

Example:
Projected Turnover: ₹400 crore
NWCR: 25% × ₹400 cr = ₹100 crore

Bank Finance: 75% of NWCR = ₹75 crore
Promoter Contribution (Margin): 25% of NWCR = ₹25 crore
```

---

## 3. EXTERNAL COMMERCIAL BORROWINGS (ECB)

### 3.1 ECB Overview

**Definition**: Foreign currency loans from overseas lenders (foreign banks, FIs, suppliers, bondholders).

**Purpose**: Cheaper funding (USD/EUR interest rates 3-5% vs INR 10-12%), large-ticket loans (₹500+ crore).

**Eligible Borrowers** (RBI ECB Guidelines):
- All entities eligible to receive FDI
- Listed companies (any amount)
- Unlisted companies (subject to sectoral limits)

**Recognized Lenders**:
- Foreign banks, financial institutions
- International capital markets (bondholders)
- Suppliers/buyers (trade credit >3 years)
- Foreign equity holders (shareholder loan)

### 3.2 ECB Limits and All-In-Cost

**ECB Limits (per financial year)**:
```
AUTOMATIC ROUTE (no RBI approval required):
- Infrastructure companies: No limit
- Manufacturing companies: Up to USD 750 million per FY
- Services companies: Up to USD 750 million per FY
- Other entities: Up to USD 50 million per FY

APPROVAL ROUTE (RBI approval required): Above automatic route limits
```

**All-In-Cost (AIC) Ceiling**:
```
All-In-Cost = Interest Rate + Other Costs (upfront fee, commitment fee, hedging cost)

AIC Ceiling (indicative, subject to RBI revision):
- 3-5 year ECB: Benchmark Rate (LIBOR/SOFR) + 350-450 bps (3.5-4.5%)
- 5-10 year ECB: Benchmark Rate + 450-500 bps (4.5-5%)

Example:
ECB: USD 100 million, 5-year tenor
Interest Rate: SOFR (5%) + Spread (4%) = 9% per annum
Upfront Fee: 1% (USD 1 million)
Hedging Cost: 2% per annum (forward contract to hedge USD/INR risk)
All-In-Cost: 9% + (1% ÷ 5 years) + 2% = 11.2% per annum

Comparison with Domestic Loan:
- ECB AIC: 11.2%
- Domestic Rupee Loan: 12.5%
- Savings: 1.3% per annum (₹13 lakh per ₹10 crore)
```

### 3.3 ECB End-Use Restrictions

**Permitted End-Uses**:
- Import of capital goods, equipment
- New projects (greenfield), expansion (brownfield)
- Overseas acquisition (M&A)
- Refinancing of existing ECB

**Prohibited End-Uses**:
- Real estate (except affordable housing, SEZ infrastructure)
- Speculation (stock market, commodity trading)
- On-lending (cannot lend ECB proceeds to other companies)
- Working capital (except trade credit)

**Example - ECB for Capex**:
```
Company: Steel Ltd (listed, manufacturing)
ECB: USD 200 million (₹1,650 crore @ ₹82.5/USD) from Deutsche Bank
Tenor: 7 years
Interest Rate: SOFR (5%) + 4% = 9% per annum
All-In-Cost: 10% per annum (including hedging)

End-Use: Import of blast furnace equipment from Germany (₹1,200 crore), expansion of plant (₹450 crore)

Compliance:
✓ Automatic route limit: USD 750 million > USD 200 million ✓
✓ End-use permitted: Capital goods import + expansion ✓
✓ AIC within ceiling: 10% vs ceiling ~10.5% ✓

Forex Risk Management:
- Forward contract: Lock USD/INR rate at ₹84/USD for 7 years (hedge principal repayment)
- Currency swap: Swap USD interest for INR interest (hedge interest payments)
- Result: USD loan converted to synthetic INR loan (10% effective rate)
```

---

## 4. INTER-CORPORATE DEPOSITS (ICD)

### 4.1 ICD Regulations

**Definition**: Unsecured deposit/loan from one company to another (short-term, typically 3-6 months).

**RBI Regulations (Directions 1975)**:
- **Maximum Tenure**: 6 months (cannot exceed)
- **Rate of Interest**: No ceiling (market-determined, typically 10-13% for creditworthy companies)
- **Restrictions**: Non-banking companies cannot accept ICDs from public (only from other companies)

**Section 186 Limits (Lending Company)**:
```
Section 186(2): Company cannot give loans/guarantees >60% of (Paid-up Capital + Free Reserves + Securities Premium)

Exception: Loans to wholly-owned subsidiaries, banking/finance companies (no limit)
```

**Example - ICD Limits**:
```
Company: Parent Ltd
Paid-up Capital: ₹100 crore
Free Reserves: ₹200 crore
Securities Premium: ₹50 crore

Maximum ICD Lending: 60% of (₹100 + ₹200 + ₹50) = ₹210 crore

Current ICDs Given:
- Subsidiary A (wholly-owned): ₹80 crore (exempt from limit)
- Subsidiary B (60% owned): ₹50 crore (counted)
- Unrelated Co C: ₹30 crore (counted)
- Total counted: ₹80 crore

Available Capacity: ₹210 crore - ₹80 crore = ₹130 crore (can lend more ICDs)
```

### 4.2 ICD vs Related Party Transaction

**If ICD to Related Party**: Section 188 approval required (Audit Committee, Board, Shareholders if threshold exceeded).

**Arms-Length Pricing**: ICD interest rate should be market rate (not preferential rate to related party).

**Example - ICD to Related Party**:
```
Company: ABC Ltd (lender)
Related Party: XYZ Ltd (borrower, director of ABC is director and 40% shareholder in XYZ)
ICD: ₹20 crore for 6 months at 8% per annum

Market Rate: 11-12% for similar creditworthiness

Issue: 8% is below market rate (11-12%) → NOT arms-length

Audit Committee Review:
- ICD interest should be ≥11% (market rate)
- If 8% rate used, transaction is preferential (benefits related party at ABC's expense)
- Recommendation: Revise rate to 11% or reject ICD

Revised ICD: ₹20 crore at 11% per annum for 6 months
Interest: ₹20 cr × 11% × 6/12 = ₹1.1 crore (vs ₹0.8 crore at 8% → ₹30 lakh higher, arms-length ✓)
```

---

## 5. BOARD APPROVALS AND LIMITS (Section 180)

### 5.1 Borrowing Powers of Board (Section 180(1)(c))

**Section 180(1)(c)**: Board cannot borrow money (other than temporary loans from banks) if aggregate borrowing exceeds paid-up capital + free reserves + securities premium, UNLESS authorized by shareholders (special resolution).

**Formula**:
```
Borrowing Limit (without shareholder approval) = Paid-up Capital + Free Reserves + Securities Premium

If Borrowing > Limit → Special Resolution required (75% majority)
```

**"Temporary Loans from Banks"**: Excluded from limit (working capital facilities like cash credit, overdraft).

**Example - Borrowing Limit**:
```
Company: Infrastructure Ltd
Paid-up Capital: ₹500 crore
Free Reserves: ₹800 crore
Securities Premium: ₹200 crore

Board Borrowing Limit: ₹500 + ₹800 + ₹200 = ₹1,500 crore

Current Borrowings:
- Term Loan A: ₹600 crore (counted)
- Term Loan B: ₹400 crore (counted)
- Cash Credit: ₹200 crore (excluded - temporary loan from bank)
- Total counted: ₹1,000 crore

Available Capacity: ₹1,500 crore - ₹1,000 crore = ₹500 crore (Board can approve up to ₹500 crore more without shareholder approval)

New Term Loan C: ₹700 crore (proposed)
- Exceeds available capacity (₹700 cr > ₹500 cr)
- Special resolution required at EGM/AGM

Shareholder Approval:
- Special resolution: "RESOLVED THAT Board be authorized to borrow up to ₹2,500 crore (in addition to temporary loans from banks)"
- If passed (75% majority), Board can approve Term Loan C
```

### 5.2 Board Resolution for Borrowing

**Typical Board Resolution Contents**:
```
RESOLVED THAT the Board approves borrowing of ₹[Amount] from [Lender] on the following terms:
1. Amount: ₹[Principal Amount]
2. Interest Rate: [X]% per annum (floating/fixed)
3. Tenure: [Y] years
4. Repayment: [Quarterly/Monthly] installments of ₹[Amount]
5. Security: [Hypothecation/Mortgage of specified assets]
6. Guarantee: [Personal guarantee by promoters / Corporate guarantee by holding company]
7. Covenants: [DSCR ≥1.5x, Debt-Equity ≤2:1, etc.]

RESOLVED FURTHER THAT [MD/CEO/CFO] be authorized to execute loan agreements, security documents, and all related documents and do all acts necessary to give effect to this resolution.
```

---

## 6. SECURITY AND COLLATERAL

### 6.1 Types of Security

**1. Hypothecation** (Section 2(21), SARFAESI Act):
- **Charge over Movable Property**: Machinery, inventory, receivables, vehicles
- **Possession**: Borrower retains possession (continues using assets)
- **Creation**: Hypothecation deed + CERSAI registration (within 30 days)
- **Enforcement**: Section 13 notice (60 days) → Possession → Sale

**2. Mortgage** (Transfer of Property Act, Section 58):
- **Charge over Immovable Property**: Land, building, factory
- **Types**:
  - **Simple Mortgage**: Borrower retains possession, personal liability for debt
  - **Mortgage by Deposit of Title Deeds**: Deposit title deeds with lender (equitable mortgage), possession with borrower
- **Registration**: Mortgage deed registered with Sub-Registrar
- **Enforcement**: Section 13 notice → Possession → Sale OR Civil suit (mortgage suit)

**3. Pledge** (Indian Contract Act, Section 172):
- **Physical Possession**: Asset delivered to lender (shares, bonds, gold)
- **Enforcement**: Lender sells pledged asset (no court process required)
- **Example**: Promoter pledges 10 lakh shares (worth ₹50 crore) for ₹30 crore loan → If default, bank sells shares

**4. Guarantee** (Indian Contract Act, Section 126):
- **Personal Guarantee**: Promoter/director personally guarantees company's loan (personal assets liable)
- **Corporate Guarantee**: Holding company/group company guarantees subsidiary's loan
- **Enforcement**: Sue guarantor for debt recovery

**Example - Security Structure**:
```
Loan: ₹200 crore term loan for manufacturing plant
Borrower: Manufacturing Ltd

Primary Security:
1. Hypothecation: Plant and machinery (₹280 crore) + Inventory (₹50 crore) = ₹330 crore (1.65x coverage)
2. Mortgage: Factory land and building (₹120 crore) - Equitable mortgage (deposit title deeds)

Collateral Security:
3. Personal Guarantee: MD and 2 promoters (₹200 crore guarantee)
4. Corporate Guarantee: Holding company (₹200 crore guarantee)
5. Pledge: Promoter pledges 20 lakh shares in listed group company (₹80 crore market value)

Total Security: ₹530 crore charged assets + ₹200 crore personal guarantee + ₹80 crore pledged shares = 4.05x loan amount (strong security coverage)
```

### 6.2 CERSAI Registration

**CERSAI** (Central Registry of Securitisation Asset Reconstruction and Security Interest):
- **Online registry** for recording charges (hypothecation, mortgage)
- **Timeline**: Register within 30 days of charge creation (else penalty ₹10,000)
- **Purpose**: Public notice (prevents fraudulent multiple charges on same asset), priority determination (first-registered charge has priority)

**Registration Process**:
1. Execute hypothecation/mortgage deed
2. File charge details on CERSAI portal (lender files online)
3. Upload documents (hypothecation deed, board resolution)
4. Pay fee (₹50-500 depending on loan amount)
5. CERSAI issues Unique Charge ID (charge registered)

**Priority**:
```
If company creates multiple charges on same asset:
- Charge A: Registered on Jan 1, 2024 (SBI loan ₹50 crore)
- Charge B: Registered on June 1, 2024 (ICICI loan ₹30 crore)

Priority: SBI has first charge (earlier registration date), ICICI has second charge
Enforcement: If default, SBI sells asset first (recovers ₹50 crore), ICICI gets residual (if any)
```

---

## 7. DEBT COVENANTS

### 7.1 Financial Covenants

**Common Financial Covenants**:

**1. Debt Service Coverage Ratio (DSCR)**:
```
DSCR = EBITDA ÷ (Principal Repayment + Interest)

Covenant: Maintain DSCR ≥1.5x

Example:
EBITDA: ₹60 crore
Annual Principal: ₹30 crore
Annual Interest: ₹10 crore
DSCR: ₹60 cr ÷ (₹30 cr + ₹10 cr) = 1.5x ✓ (covenant met)

If EBITDA falls to ₹50 crore:
DSCR: ₹50 cr ÷ ₹40 cr = 1.25x ✗ (covenant breached)
→ Lender can recall loan, invoke security
```

**2. Debt-Equity Ratio**:
```
Debt-Equity Ratio = Total Debt ÷ Shareholders' Equity

Covenant: Maintain Debt-Equity ≤2:1

Example:
Total Debt: ₹300 crore
Shareholders' Equity: ₹200 crore
Debt-Equity: ₹300 cr ÷ ₹200 cr = 1.5:1 ✓ (covenant met)

If company takes additional ₹150 crore debt (total debt ₹450 crore):
Debt-Equity: ₹450 cr ÷ ₹200 cr = 2.25:1 ✗ (covenant breached)
→ Company must infuse equity (₹25 crore to bring D/E to 2:1) OR seek lender waiver
```

**3. Interest Coverage Ratio (ICR)**:
```
ICR = EBIT ÷ Interest Expense

Covenant: Maintain ICR ≥3x

Example:
EBIT: ₹90 crore
Interest Expense: ₹25 crore
ICR: ₹90 cr ÷ ₹25 cr = 3.6x ✓ (covenant met)
```

### 7.2 Non-Financial Covenants

**Positive Covenants** (must do):
- Submit quarterly financials within 45 days of quarter-end
- Maintain insurance on charged assets (property, plant, machinery, key man)
- Pay statutory dues (taxes, PF, ESI) on time
- Maintain books of accounts as per Companies Act

**Negative Covenants** (must not do):
- **Negative Pledge**: Do not create additional charge on charged assets (no second mortgage without lender consent)
- Do not sell/transfer charged assets without lender consent
- Do not change nature of business (e.g., manufacturing to real estate)
- Do not merge/amalgamate without lender consent
- Do not pay dividends if DSCR <1.5x (cash conservation)

**Example - Negative Pledge Clause**:
```
Clause: "The Borrower shall not create any charge, lien, or encumbrance on the hypothecated assets (machinery) without prior written consent of the Lender."

Scenario: Company wants to obtain additional ₹50 crore loan from HDFC Bank, using same machinery as security.

Action Required:
1. Request SBI consent (existing lender with first charge on machinery)
2. SBI evaluates: Security coverage sufficient? (Machinery worth ₹280 cr, existing loan ₹200 cr, new loan ₹50 cr → Total ₹250 cr < ₹280 cr ✓)
3. SBI grants consent (HDFC gets second charge on machinery)
4. Execute inter-creditor agreement (SBI first charge, HDFC second charge)
```

### 7.3 Covenant Breach and Waivers

**Breach Consequences**:
- **Event of Default**: Covenant breach triggers Event of Default (EoD)
- **Lender Rights**: Recall loan (demand immediate repayment), invoke security, appoint nominee director, initiate CIRP (IBC)

**Waiver**:
- Company can request waiver (temporary relaxation of covenant)
- Lender evaluates: Temporary vs permanent issue? Management action plan?
- Waiver granted (typically 6-12 months, with corrective action milestones)

**Example - Covenant Breach and Waiver**:
```
Covenant: Maintain DSCR ≥1.5x

FY 2023-24 Q3: DSCR 1.2x (breach due to temporary revenue dip from delayed project)

Company Action:
1. Notify lender immediately (within 7 days of breach per loan agreement)
2. Provide explanation: Project delay (2 months), revenue to normalize in Q4
3. Request waiver: 6-month waiver, commit to DSCR 1.5x by Q2 FY 2024-25
4. Remedial action: Reduce capex (₹20 crore postponed), cost reduction (₹10 crore savings)

Lender Decision:
- Assess credibility: Management track record, industry outlook, project pipeline
- Waiver granted: 6 months (till September 2024), conditions:
  (a) Submit monthly financials (vs quarterly)
  (b) No dividend payment till DSCR 1.5x restored
  (c) Reduce capex as committed
- If DSCR not restored by September 2024 → Recall loan

Result: Q2 FY 2024-25 DSCR 1.6x ✓ (project delivered, revenue normalized, covenant restored)
```

---

## 8. DEFAULT AND REMEDIES

### 8.1 Events of Default (EoD)

**Typical EoDs in Loan Agreement**:
```
1. Non-payment: Principal or interest overdue >30 days
2. Covenant Breach: Financial covenants (DSCR, D/E) or non-financial covenants breached
3. Cross-Default: Default in any other loan (triggers default in this loan too)
4. Insolvency: Company admits inability to pay debts, CIRP initiated
5. Material Adverse Change (MAC): Business materially affected (regulatory ban, loss of key customer/license)
6. Misrepresentation: Material misrepresentation in loan application (fraud)
```

**Example - Cross-Default**:
```
Company: Auto Ltd
Loan A: ₹100 crore from SBI (Clause: Cross-default if any loan default)
Loan B: ₹50 crore from ICICI

Scenario: Auto Ltd defaults on Loan B (missed ₹2 crore interest payment to ICICI, 45 days overdue)

Cross-Default Trigger:
- Loan B default automatically triggers default in Loan A (per cross-default clause)
- SBI can recall Loan A (even though Auto Ltd never defaulted on SBI payments)

Rationale: Default on one loan signals financial distress (risk to all lenders)

Company Action:
- Cure Loan B default immediately (pay ₹2 crore to ICICI + default interest)
- Notify SBI that default cured (provide ICICI payment proof)
- SBI satisfied, does not recall Loan A
```

### 8.2 Lender Remedies

**Step 1: Demand Notice (Section 13(2), SARFAESI Act)**:
- Lender issues 60-day notice to borrower (demand full payment of outstanding loan)
- Notice sent via registered post, email (to registered office, directors, promoters)

**Step 2: Symbolic Possession (if borrower doesn't pay)**:
- Lender takes symbolic possession of secured assets (affixes possession notice)
- Actual physical possession (if borrower resists, lender can request DM assistance)

**Step 3: Sale of Assets (Section 13(4))**:
- Lender can sell secured assets (30 days public notice)
- Sale via auction, e-auction (highest bidder)
- Sale proceeds: Recover principal + interest + costs, surplus returned to borrower

**Timeline**: 60 days notice + 30 days possession + 30 days sale = ~120 days (4 months) from notice to recovery.

**Example - SARFAESI Enforcement**:
```
Loan: ₹80 crore term loan (secured by hypothecation of machinery worth ₹120 crore)
Default: Principal ₹10 crore overdue (3 months past due date)

Day 1: SBI issues Section 13(2) notice (60-day demand notice)
- Outstanding: ₹80 crore principal + ₹3 crore interest + ₹1 crore penal interest = ₹84 crore

Day 60: Borrower fails to pay (requests restructuring, SBI rejects)

Day 65: SBI takes symbolic possession (affixes notice on factory gate, machinery)

Day 75: SBI publishes sale notice (30-day public notice in newspapers, online portals)
- Machinery to be sold via e-auction on Day 105

Day 105: E-auction held
- 5 bidders participate
- Highest bid: ₹95 crore (79% of ₹120 crore value - distress sale discount)

Day 110: Sale completed
- SBI recovers: ₹84 crore (outstanding loan)
- Surplus: ₹95 cr - ₹84 cr = ₹11 crore returned to borrower

Borrower rights: Can approach DRT (Debt Recovery Tribunal) within 60 days of notice (challenge securitization, seek injunction)
```

### 8.3 Insolvency and Bankruptcy Code (IBC)

**Financial Creditor's Right (Section 7, IBC)**:
```
If default ≥₹1 crore:
- Financial creditor (bank, bondholder, debentureholder) can file application with NCLT
- NCLT admits application → CIRP (Corporate Insolvency Resolution Process) initiated
- 180 days (extendable to 330 days) to find resolution plan (or liquidation)
```

**Process**:
1. **Financial Creditor files Section 7 application** (NCLT)
2. **NCLT admits** (14 days, if default and debt >₹1 crore proved)
3. **Moratorium declared** (no legal proceedings against company, no asset transfer)
4. **Resolution Professional (RP) appointed** (takes over management from directors)
5. **Committee of Creditors (CoC) formed** (financial creditors only, voting based on debt share)
6. **Resolution plans invited** (potential investors submit plans)
7. **CoC votes** (66% majority required to approve plan)
8. **NCLT approves plan** → Company taken over by resolution applicant
9. **If no plan approved** → Liquidation (assets sold, creditors paid in waterfall priority)

**Example - IBC Case**:
```
Company: Steel Ltd (default on ₹300 crore loan to consortium of 5 banks)
Default Amount: ₹300 crore principal + ₹40 crore interest = ₹340 crore

Day 1: SBI (lead bank) files Section 7 application with NCLT
Day 14: NCLT admits application (default proved, debt >₹1 crore)
Day 15: Moratorium declared, RP appointed (takes over Steel Ltd management)
Day 30: CoC formed (5 banks, voting share based on debt: SBI 40%, ICICI 25%, HDFC 20%, Axis 10%, Kotak 5%)
Day 90: 3 resolution plans received (from Tata Steel, JSW Steel, ArcelorMittal)
Day 150: CoC votes - ArcelorMittal plan approved (70% approval: SBI, ICICI, HDFC voted YES; Axis, Kotak voted NO)
Day 180: NCLT approves ArcelorMittal plan
- ArcelorMittal pays ₹250 crore to creditors (₹340 crore debt → 74% recovery)
- Steel Ltd becomes wholly-owned subsidiary of ArcelorMittal

Alternative (no plan approved): Day 330 → Liquidation → Assets sold for ₹180 crore → 53% recovery
```

---

## 9. DEBT RESTRUCTURING

### 9.1 Types of Restructuring

**1. Tenure Extension**:
- Extend repayment period (5 years → 7 years)
- Reduces quarterly installment (cash flow relief)

**2. Moratorium**:
- 6-12 month moratorium on principal (interest continues)
- Company uses cash for business stabilization

**3. Interest Rate Reduction**:
- Reduce rate (12% → 10%)
- Reduce interest burden

**4. Debt-Equity Conversion**:
- Convert part of debt to equity (₹50 crore debt → 10% equity)
- Reduces debt burden, but dilutes existing shareholders

**Example - Debt Restructuring**:
```
Original Loan: ₹100 crore, 5 years, 12% interest, quarterly installments ₹5 crore principal + ₹3 crore interest = ₹8 crore per quarter
Company Situation: Temporary revenue dip, DSCR 0.8x (cannot service ₹8 crore quarterly)

Restructuring Request:
- Extend tenure from 5 years to 7 years
- 1-year moratorium on principal (only interest for Year 1)
- Reduce rate from 12% to 10%

Restructured Loan:
- Tenure: 7 years
- Moratorium: Year 1 (only ₹2.5 crore interest per quarter, no principal)
- Installments Year 2-7: ₹4.17 crore principal + ₹2 crore interest = ₹6.17 crore per quarter

Cash Flow Relief: ₹8 crore → ₹2.5 crore (Year 1) → ₹6.17 crore (Year 2-7) - Manageable with projected revenue recovery
```

### 9.2 RBI Prudential Norms

**Standard Asset**: Loan performing (no overdue >90 days), provision 0.4% of loan.
**NPA (Non-Performing Asset)**: Overdue >90 days, classified as Sub-Standard (provision 15%), Doubtful (provision 25-100%), Loss (provision 100%).

**Restructuring Impact**:
- Restructured loan: Downgraded to NPA (even if performing), provision 5% (for 1 year "restructured standard")
- After 1 year: If performing post-restructuring, upgraded to Standard

---

## COMPLIANCE CHECKLIST

**Before Borrowing**:
- [ ] Check borrowing limit (Section 180: Paid-up + Free Reserves + Securities Premium)
- [ ] If limit exceeded, pass special resolution at EGM/AGM
- [ ] Board resolution approving loan (amount, terms, security, authorized signatories)

**Loan Documentation**:
- [ ] Execute loan agreement (borrower, lender, terms, covenants, EoDs)
- [ ] Execute security documents (hypothecation/mortgage deed)
- [ ] Register charge with CERSAI (within 30 days, penalty ₹10,000 if late)
- [ ] File Form CHG-1 with ROC (within 30 days of charge creation)

**Ongoing Compliance**:
- [ ] Submit quarterly financials to lender (within 45 days)
- [ ] Submit annual audited financials (within 6 months of FYE)
- [ ] Maintain financial covenants (DSCR, Debt-Equity, ICR)
- [ ] Comply with negative covenants (no additional charge, no asset sale, no business change)
- [ ] Renew insurance policies (property, plant, key man) annually
- [ ] Pay interest and principal on due dates (no default)

**If Covenant Breach**:
- [ ] Notify lender immediately (within 7 days per loan agreement)
- [ ] Provide explanation and remedial action plan
- [ ] Request waiver (temporary covenant relaxation)
- [ ] Implement corrective actions within waiver period

---

## LEGAL DISCLAIMER

This protocol provides information on debt financing methods and regulations under Indian law. It is for informational purposes only and does not constitute legal, financial, or investment advice. Companies should consult qualified bankers, corporate lawyers, company secretaries, and chartered accountants for specific debt financing matters. Legal provisions, RBI regulations, and lending policies are subject to change. Interest rates, loan terms, and lender appetite vary based on company creditworthiness and market conditions.

---

**Last Updated**: December 5, 2025
**Version**: 1.0.0
**Protocol ID**: IL-CORP-DEBT-FINANCING
