---
id: IL-CORP-DEBENTURES
version: 1.0.0
category: corporate_law
subcategory: corporate_finance
sections:
  - Debentures Overview
  - Types of Debentures
  - Issuance Process
  - Debenture Trustee
  - Security and Charge
  - Redemption and Conversion
  - Debenture Holders' Rights
  - Default and Enforcement
  - Listed vs Unlisted Debentures
  - SEBI Regulations
dependencies:
  - IL-CORP-DEBT-FINANCING (Debt financing fundamentals)
  - IL-CORP-BOARD-MEETINGS (Board approval for debenture issue)
  - IL-CORP-SHARE-CAPITAL (Convertible debentures conversion to equity)
related_protocols:
  foundation:
    - IL-COMPANIES-ACT (Companies Act 2013, Sections 71, 117)
    - IL-CORP-PRIVATE-PLACEMENT (Private placement of debentures)
  procedural:
    - IL-CORP-AUDIT-COMMITTEE (Debenture issue approval)
landmark_cases:
  - SEBI v. Sahara India Real Estate Corporation (2013) 1 SCC 1 (OFCD deemed public offer)
  - Privy Council in Webb v. Whiffin (1872) LR 5 HL 711 (Debenture holders' priority)
---

# DEBENTURES - INDIAN CORPORATE LAW

## OVERVIEW

A debenture is a debt instrument issued by a company acknowledging indebtedness and containing terms of repayment of principal and interest. Debenture holders are creditors (not owners), have priority over shareholders in liquidation, but no voting rights. Companies issue debentures to raise long-term capital (5-30 years typical) without diluting equity.

**DEBENTURE vs EQUITY vs LOAN**:

| Parameter | Debenture | Equity | Bank Loan |
|---|---|---|---|
| **Nature** | Debt (tradable security) | Ownership | Debt (non-tradable) |
| **Voting Rights** | No | Yes | No |
| **Return** | Fixed interest (coupon) | Dividend (variable) | Fixed interest |
| **Tradability** | Tradable (if listed) | Tradable (if listed) | Non-tradable |
| **Security** | Secured or unsecured | N/A | Secured |
| **Tenure** | 5-30 years | Perpetual | 1-10 years |
| **Priority in Liquidation** | Before equity, after secured creditors | Last (residual claimants) | Secured creditors first |

**LEGAL DEFINITION (Section 2(30))**:
```
"Debenture" includes:
- Debenture stock
- Bonds
- Any other instrument of a company evidencing a debt (whether secured or not)

Excludes: Equity shares, preference shares (not debt)
```

**LEGAL FRAMEWORK**:
- **Companies Act 2013**: Section 71 (Debenture issue), Section 117 (Debenture register), Section 71A-71H (Debenture trustee)
- **SEBI (Issue and Listing of Debt Securities) Regulations 2021**: Listed debentures
- **SEBI (Issue and Listing of Non-Convertible Securities) Regulations 2021**: NCDs, bonds
- **Companies (Share Capital and Debentures) Rules 2014**: Debenture issuance procedures

---

## 1. TYPES OF DEBENTURES

### 1.1 Classification by Security

**1. Secured Debentures**:
- Backed by charge on company's assets (fixed or floating charge)
- Debenture holders have priority claim on charged assets
- Lower risk → Lower interest rate (9-11%)
- Example: Mortgage debenture (charge on specific property)

**2. Unsecured Debentures (Naked Debentures)**:
- No charge on assets (only company's general creditworthiness)
- Higher risk → Higher interest rate (12-15%)
- Rank below secured creditors in liquidation

**Example - Secured vs Unsecured**:
```
Company: Real Estate Ltd
Assets: Land & Building (₹500 cr), Inventory (₹200 cr), Cash (₹50 cr)
Total Assets: ₹750 crore

Issuance:
- Secured Debentures: ₹300 crore at 10% (secured by mortgage on land & building worth ₹500 cr)
- Unsecured Debentures: ₹100 crore at 13% (no security)

Liquidation Scenario (Assets sold for ₹600 crore):
1. Secured Debenture Holders: ₹300 crore (paid in full from sale of land & building)
2. Unsecured Debenture Holders: ₹100 crore (paid from residual ₹300 crore)
3. Equity Shareholders: ₹200 crore (residual)

If Assets sold for ₹350 crore only:
1. Secured Debenture Holders: ₹300 crore (paid in full)
2. Unsecured Debenture Holders: ₹50 crore (50% recovery, ₹50 crore loss)
3. Equity Shareholders: ₹0 (nothing left)
```

### 1.2 Classification by Convertibility

**1. Non-Convertible Debentures (NCDs)**:
- Cannot be converted into equity
- Remain debt till maturity (then redeemed)
- Most common type (90%+ of corporate debentures)

**2. Fully Convertible Debentures (FCDs)**:
- 100% converted into equity shares at predetermined date/ratio
- Effectively delayed equity (no redemption, just conversion)
- Example: ₹1,000 FCD converted to 10 shares at ₹100/share after 3 years

**3. Partly Convertible Debentures (PCDs)**:
- Partial conversion (e.g., 60% converted to equity, 40% redeemed in cash)
- Hybrid: Part debt, part equity
- Example: ₹1,000 PCD → ₹600 converted to 6 shares at ₹100/share + ₹400 redeemed in cash

**4. Optionally Convertible Debentures (OCDs)**:
- Debenture holder has OPTION to convert (or remain as debt till maturity)
- Flexibility for investor (convert if share price rises, redeem if share price falls)
- **SEBI v. Sahara case**: OCDs treated as equity-like (if marketed to large public, deemed public offer)

**Example - Conversion Mechanics**:
```
Company: Software Ltd (current share price ₹80, pre-issue 1 crore shares)
Issue: ₹200 crore Fully Convertible Debentures (₹1,000 face value, 20 lakh FCDs)
Conversion Terms: Each FCD converts to 10 shares at ₹100/share after 3 years

At Conversion (Year 3):
- 20 lakh FCDs × 10 shares = 2 crore new shares issued
- Pre-issue equity: 1 crore shares
- Post-conversion equity: 1 crore + 2 crore = 3 crore shares
- Existing shareholder dilution: 1 crore ÷ 3 crore = 33.3% (vs 100% pre-issue, 66.7% dilution)

If Share Price at Conversion = ₹150 (higher than conversion price ₹100):
- Debenture holders benefit: Get shares worth ₹150 for ₹100 (50% gain)
- Existing shareholders diluted at below-market price

If Share Price at Conversion = ₹60 (lower than conversion price ₹100):
- Debenture holders lose: Get shares worth ₹60 for ₹100 (40% loss)
- Had it been OCD, holder would choose redemption (₹1,000 cash) over conversion
```

### 1.3 Classification by Redemption

**1. Redeemable Debentures**:
- Redeemed (repaid) at maturity or earlier as per terms
- Tenure: 5-30 years typical
- Redemption: At par (₹1,000 → ₹1,000) or at premium (₹1,000 → ₹1,100)

**2. Irredeemable/Perpetual Debentures**:
- No fixed maturity (perpetual debt)
- Interest paid perpetually, no principal redemption
- Rare in India (prohibited under Section 71(1) - all debentures must specify redemption terms)

**3. Call Option Debentures**:
- Company has option to redeem before maturity (issuer call)
- Example: 10-year debenture, callable after 5 years (company can redeem early if interest rates fall)

**4. Put Option Debentures**:
- Debenture holder has option to demand early redemption (investor put)
- Example: 10-year debenture, puttable after 7 years (investor can demand redemption if needing liquidity)

**Example - Call Option Exercise**:
```
Issue: ₹500 crore 10-year debentures at 12% coupon, callable after 5 years at 102 (₹1,020 per ₹1,000 face value)

Year 5: Interest rates fallen to 8% (market rate)
Company Decision: Exercise call option
- Redeem ₹500 crore at 102 = ₹510 crore (₹10 crore call premium paid)
- Reissue new ₹500 crore debentures at 8% (market rate)
- Savings: (12% - 8%) × ₹500 cr × 5 years = ₹100 crore interest savings (vs ₹10 cr call premium)
- Net Benefit: ₹90 crore over 5 years

Debenture Holder Impact:
- Receives ₹1,020 per debenture (par + 2% premium)
- Must reinvest at lower prevailing rate (8% vs original 12%)
- Reinvestment risk (lower returns going forward)
```

### 1.4 Classification by Registration

**1. Registered Debentures**:
- Debenture holder's name registered in company's debenture register
- Transfer requires execution of transfer deed + registration with company
- Interest/principal paid directly to registered holder

**2. Bearer Debentures**:
- Transferable by delivery (like cash, no registration required)
- Interest paid to bearer (whoever presents coupon)
- **Prohibited in India** (Companies Act 2013, Section 71(3) - all debentures must be registered)

---

## 2. ISSUANCE PROCESS (Section 71)

### 2.1 Board and Shareholder Approval

**Board Approval (Section 180(1)(c))**:
```
Board can issue debentures within borrowing limit:
Limit = Paid-up Capital + Free Reserves + Securities Premium

If debenture issue exceeds limit → Shareholder approval (special resolution) required
```

**Example - Approval Requirement**:
```
Company: Manufacturing Ltd
Paid-up Capital: ₹200 crore
Free Reserves: ₹300 crore
Securities Premium: ₹50 crore

Board Borrowing Limit: ₹200 + ₹300 + ₹50 = ₹550 crore

Current Borrowings:
- Bank Loans: ₹300 crore (counted)
- Existing Debentures: ₹100 crore (counted)
- Total: ₹400 crore

Proposed New Debenture Issue: ₹200 crore

Check: ₹400 cr (existing) + ₹200 cr (new) = ₹600 crore > ₹550 crore limit
→ EXCEEDS LIMIT → Special resolution required at EGM/AGM

Shareholder Resolution: "RESOLVED THAT Board be authorized to borrow up to ₹800 crore (including debentures)"
```

### 2.2 Public Issue vs Private Placement

**Public Issue (Section 23)**:
- Offer to public (>200 persons)
- Requires prospectus (SEBI approval)
- Timeline: 6-9 months
- Cost: 2-3% of issue size
- Listing mandatory

**Private Placement (Section 42)**:
- Offer to <200 persons (identified investors)
- Offer letter (no prospectus)
- Timeline: 30-60 days
- Cost: 0.5-1% of issue size
- Listing optional

**Example - Public Issue Process**:
```
Company: Power Ltd
Issue: ₹1,000 crore 7-year NCDs at 10.5% coupon

Public Issue Process:
Day -180: Appoint merchant bankers, trustees, legal advisors
Day -120: Draft prospectus (200-300 pages)
Day -90: File draft prospectus with SEBI
Day -60: SEBI observations, company responds
Day -30: File final prospectus, publish in newspapers
Day 0: Issue Opens (3-day subscription period)
Day 3: Issue Closes (Subscription: 2.5x oversubscribed)
Day 5: Allotment (pro-rata basis, each applicant gets 40% of application)
Day 10: Listing on NSE/BSE (debentures tradable)

Costs:
- Merchant Banker Fees: ₹15 crore (1.5%)
- Legal, Audit, Trustee: ₹5 crore (0.5%)
- Listing, Printing, Ads: ₹5 crore (0.5%)
- Total: ₹25 crore (2.5% of ₹1,000 crore)

Net Proceeds: ₹975 crore (₹1,000 cr - ₹25 cr costs)
```

### 2.3 Credit Rating (Section 71(2))

**Mandatory Credit Rating**:
```
Section 71(2): All public issues of debentures MUST obtain credit rating from at least 1 credit rating agency

Credit Rating Agencies (SEBI-registered):
- CRISIL, ICRA, CARE, India Ratings, Brickwork Ratings

Rating Scale:
- AAA: Highest safety (top-tier companies, government PSUs)
- AA: High safety
- A: Adequate safety
- BBB: Moderate safety (investment grade minimum)
- BB, B: Speculative grade (junk bonds)
- C, D: High risk, default

Interest Rate Correlation:
- AAA: 8-9.5%
- AA: 9.5-11%
- A: 11-13%
- BBB: 13-15%
- Below BBB: 15-20% (if marketable at all)
```

**Example - Credit Rating Impact**:
```
Company A (AAA-rated): Issues ₹500 crore NCDs at 9% coupon
Company B (A-rated): Issues ₹500 crore NCDs at 12% coupon (same tenure, similar business)

Interest Cost Difference:
- Company A: ₹500 cr × 9% = ₹45 crore per annum
- Company B: ₹500 cr × 12% = ₹60 crore per annum
- Company B pays ₹15 crore MORE per year (33% higher) due to lower rating

Over 7-year tenure:
- Company B pays ₹105 crore extra interest (₹15 cr × 7 years)

Credit Rating Value: Strong rating (AAA vs A) saves ₹105 crore on ₹500 crore issue
```

---

## 3. DEBENTURE TRUSTEE (Section 71A-71H)

### 3.1 Mandatory Appointment

**Section 71A**: Every company issuing debentures (secured or unsecured) to public or >500 persons must appoint debenture trustee.

**Who Can Be Trustee**:
- Scheduled banks, public financial institutions, insurance companies, NBFCs
- Cannot be: Director, KMP, employee, shareholder (>2% equity), related party

**Trustee's Role**:
- Represent debenture holders' collective interests
- Monitor company compliance with debenture terms
- Ensure security (if secured debentures) created and maintained
- Take action if company defaults (enforce security, file CIRP)

**Example - Trustee Appointment**:
```
Company: Infrastructure Ltd
Issue: ₹800 crore secured NCDs (offered to 5,000 retail investors)

Debenture Trustee: IDBI Trusteeship Services Ltd
Trustee Fee: 0.1% per annum (₹80 lakh per year for ₹800 crore issue)

Trustee's Duties:
1. Verify creation of security (mortgage on toll road assets worth ₹1,200 crore)
2. Monitor compliance:
   - DSCR ≥1.5x (verify quarterly)
   - Debt-Equity ≤2:1 (verify quarterly)
   - Timely payment of interest/principal
3. Attend company board meetings (when invited)
4. If default: Issue notice to company (30 days to cure), if not cured → File CIRP with NCLT

Debenture Holders' Benefit:
- Individual investors (5,000 holders) cannot monitor company individually
- Trustee acts as collective representative (economies of scale)
- Ensures security maintained, covenants enforced, defaults remedied
```

### 3.2 Trustee's Powers and Duties

**Section 71B - Trustee's Duties**:
```
1. Ensure issue proceeds utilized for stated objects
2. Call debenture holders' meeting if 10% holders request (or if company defaults)
3. Appoint nominee director (if company defaults)
4. Enforce security (if secured debentures, company defaults)
5. File suit for recovery of principal/interest (on behalf of debenture holders)
6. Take any action to protect debenture holders' interests
```

**Section 71C - Trustee's Liability**:
- Liable for breach of trust (negligence, fraud)
- Liable to debenture holders (for losses caused by trustee's breach)
- Indemnified by company for reasonable expenses

**Example - Trustee Enforcement**:
```
Company: Real Estate Ltd (₹500 crore secured NCDs, secured by mortgage on 10 properties)
Default: Missed 2 consecutive interest payments (₹25 crore each, total ₹50 crore overdue)

Trustee Action (IDBI Trusteeship):
Day 1: Issue default notice to company (30 days to cure)
Day 30: Company fails to cure (unable to pay due to cash flow stress)
Day 35: Trustee calls debenture holders' meeting (75% debenture holders vote to enforce security)
Day 40: Trustee files SARFAESI notice (Section 13(2)) - demand ₹500 crore principal + ₹50 crore interest = ₹550 crore
Day 100: Take possession of 10 properties (symbolic possession)
Day 130: Auction 10 properties (sale proceeds ₹620 crore)

Distribution:
- Debenture Holders: ₹550 crore (principal + interest)
- Trustee Fee (enforcement): ₹5 crore
- Surplus to Company: ₹65 crore (₹620 cr - ₹555 cr)

Result: Debenture holders recover 100% (security adequate)
```

---

## 4. SECURITY AND CHARGE CREATION

### 4.1 Types of Charges

**1. Fixed Charge**:
- Charge on specific identified assets (land, building, specific machinery)
- Asset cannot be sold without lender/trustee consent
- Example: Mortgage on factory land (₹200 crore debentures secured by factory worth ₹300 crore)

**2. Floating Charge**:
- Charge on class of assets (inventory, receivables, "all current assets")
- Company can trade assets in ordinary course (sell inventory, collect receivables)
- Charge "crystallizes" (becomes fixed) on default
- Example: Floating charge on inventory (₹100 crore debentures secured by inventory worth ₹150 crore, company can sell inventory and buy new inventory)

**Priority**:
```
If same asset has multiple charges:
1. Fixed Charge (specific asset) has priority over Floating Charge (class of assets)
2. Among multiple fixed charges: First-registered charge (CERSAI registration date)
```

**Example - Fixed vs Floating Charge**:
```
Company: Manufacturing Ltd
Assets: Factory land & building (₹500 cr), Machinery (₹300 cr), Inventory (₹100 cr)

Issue 1: ₹400 crore Secured NCDs (Series A)
Security: Fixed charge on factory land & building (₹500 crore)

Issue 2: ₹150 crore Secured NCDs (Series B)
Security: Floating charge on inventory (₹100 crore) + Floating charge on receivables (₹80 crore)

Liquidation Scenario (Assets sold: Factory ₹450 cr, Machinery ₹200 cr, Inventory ₹80 cr, Receivables ₹60 cr):

Priority:
1. Series A (Fixed Charge on Factory): ₹400 crore (paid from factory sale ₹450 cr)
2. Secured Creditors (Machinery): ₹50 crore (assumed other secured loan)
3. Series B (Floating Charge on Inventory + Receivables): ₹140 crore (paid from inventory ₹80 cr + receivables ₹60 cr)

Series B Recovery: ₹140 crore out of ₹150 crore = 93% recovery (₹10 crore loss)
```

### 4.2 Charge Registration (Section 77)

**Section 77**: Company must file particulars of charge with ROC within 30 days of creation.

**Form CHG-1**: Details of charge (amount, property, chargee, debenture trustee).

**Penalty**:
- Non-registration within 30 days: Charge void (unenforceable against liquidator, other creditors)
- Company: Fine up to ₹10 lakh
- Officers in default: Fine up to ₹1 lakh

**CERSAI Registration**: Also register with CERSAI (for hypothecation, mortgage) for public notice.

**Example - Charge Registration Timeline**:
```
Debenture Issue: ₹600 crore secured NCDs (mortgage on properties worth ₹900 crore)

Day 0: Debentures issued, mortgage deed executed
Day 5: Mortgage registered with Sub-Registrar (immovable property registration)
Day 10: File Form CHG-1 with ROC (charge particulars: ₹600 crore, properties, trustee IDBI Trusteeship)
Day 12: File charge details on CERSAI portal (online registration)
Day 15: ROC approves Form CHG-1 (charge registered)

Result: Charge valid, enforceable (registered within 30 days ✓)

If registered on Day 35 (late):
- Charge void against liquidator (if company liquidates, debenture holders lose priority)
- Debenture holders become unsecured creditors (rank below secured creditors)
- Penalty: Company ₹10 lakh, Directors ₹1 lakh each
```

---

## 5. REDEMPTION OF DEBENTURES (Section 71(4))

### 5.1 Debenture Redemption Reserve (DRR)

**Section 71(4)**: Company issuing debentures MUST create Debenture Redemption Reserve (DRR) before redemption.

**DRR Requirement**:
```
Listed Companies: 25% of debenture value
Unlisted Companies: 25% of debenture value (if issue to public), 100% (if private placement to <100 persons)

Exception: Infrastructure companies, NBFCs, housing finance companies (exempt from DRR)
```

**Creation**:
- Transfer from profits (P&L reserves) to DRR
- Cannot be distributed as dividend (earmarked for debenture redemption)
- Must be created before redemption commences (or latest by date of redemption)

**Example - DRR Creation**:
```
Company: FMCG Ltd (listed)
Debentures: ₹800 crore 7-year NCDs (redemption starts Year 6)

DRR Requirement: 25% of ₹800 crore = ₹200 crore

Timeline:
- End of Year 5: Transfer ₹200 crore from P&L reserves to DRR (before redemption commences)
- Year 6: Redeem ₹200 crore (25% of debentures)
- Year 7: Redeem ₹600 crore (75% of debentures)
- After full redemption: Transfer ₹200 crore from DRR back to general reserves (DRR no longer required)

Journal Entries:
Year 5: Profit & Loss A/c Dr. ₹200 cr
         To DRR A/c Cr. ₹200 cr
Year 7 (after full redemption): DRR A/c Dr. ₹200 cr
                                  To General Reserve A/c Cr. ₹200 cr
```

### 5.2 Redemption Methods

**1. Lump Sum Redemption**:
- Entire principal redeemed at maturity
- Example: ₹500 crore NCDs mature in Year 7 → Pay ₹500 crore on maturity date

**2. Serial Redemption (Installments)**:
- Principal redeemed in installments (annual, semi-annual)
- Example: ₹500 crore NCDs, 5-year tenure, annual redemption → ₹100 crore per year

**3. Sinking Fund Method**:
- Company invests in sinking fund (liquid investments) over debenture tenure
- At maturity, liquidate sinking fund to redeem debentures
- Example: ₹500 crore NCDs, 10-year tenure → Invest ₹50 crore per year in sinking fund (10 years × ₹50 cr = ₹500 cr at maturity)

**4. Conversion Method**:
- Debentures converted to equity (no cash redemption)
- Only for convertible debentures (FCDs, PCDs, OCDs)

**Example - Serial Redemption**:
```
Issue: ₹1,000 crore 10-year NCDs at 10% coupon
Redemption: Annual installments starting Year 6 (₹200 crore per year for 5 years)

Cash Flow (Coupon + Principal):
Year 1-5: ₹100 crore interest only (₹1,000 cr × 10%)
Year 6: ₹100 crore interest + ₹200 crore principal = ₹300 crore
Year 7: ₹80 crore interest (₹800 cr × 10%) + ₹200 crore principal = ₹280 crore
Year 8: ₹60 crore interest (₹600 cr × 10%) + ₹200 crore principal = ₹260 crore
Year 9: ₹40 crore interest (₹400 cr × 10%) + ₹200 crore principal = ₹240 crore
Year 10: ₹20 crore interest (₹200 cr × 10%) + ₹200 crore principal = ₹220 crore

Total Interest Paid: ₹1,000 crore (₹100 cr × 5 years + ₹80 + ₹60 + ₹40 + ₹20 = ₹700 crore interest vs ₹1,000 crore if lump sum redemption)

Advantage: Lower interest cost (average outstanding reduces as principal repaid)
```

---

## 6. DEBENTURE HOLDERS' RIGHTS

### 6.1 Statutory Rights

**1. Right to Interest**:
- Debenture holders entitled to interest as per debenture terms (coupon rate)
- Interest payment: Annual, semi-annual, or quarterly (as specified)
- Non-payment: Default (debenture trustee can enforce)

**2. Right to Redemption**:
- Debenture holders entitled to principal repayment at maturity (or as per redemption schedule)
- Non-payment: Default (trustee enforces security or files CIRP)

**3. Right to Inspect Register (Section 117(3))**:
- Debenture holders can inspect debenture register at registered office (during business hours)
- Can obtain copy of register (₹50 per page)

**4. Right to Call Meeting (Section 71G)**:
- 10% debenture holders (by value) can request trustee to call meeting
- Trustee must call meeting within 21 days (or debenture holders can call directly)

**5. Right to Vote at Meeting**:
- Debenture holders vote at debenture holders' meeting (resolutions affecting rights)
- Voting: 1 debenture = 1 vote (proportional to value)
- **No voting at shareholders' meeting** (debenture holders are creditors, not owners)

**6. Right to Enforce Security** (via trustee):
- If secured debentures, debenture holders (via trustee) can enforce security on default
- Priority over unsecured creditors, equity shareholders

**Example - Debenture Holders' Meeting**:
```
Company: Steel Ltd (₹500 crore NCDs outstanding)
Issue: Company proposes to extend maturity by 2 years (original maturity Year 7 → proposed Year 9)

Debenture Holders' Meeting:
- Called by Trustee (at company's request)
- Agenda: Approve maturity extension
- Voting: 1 debenture (₹1,000 face value) = 1 vote → 5 lakh votes total

Present: Debenture holders representing 60% (₹300 crore, 3 lakh votes)
Resolution: Approve maturity extension
Votes: YES (2.5 lakh votes = 83%), NO (0.5 lakh votes = 17%)
Result: Resolution PASSED (75% majority required for modifying debenture terms)

Effect: Maturity extended to Year 9 (all debenture holders bound, even those who voted NO or did not attend)
```

### 6.2 Priority in Liquidation (Webb v. Whiffin, 1872)

**Privy Council in Webb v. Whiffin**:
```
Priority Order (Liquidation/Winding Up):
1. Secured Creditors (including secured debenture holders) - Paid from secured assets
2. Liquidation Expenses (insolvency professional fees, legal costs)
3. Workmen's Dues (wages for 12 months prior to liquidation, max ₹24,000 per employee)
4. Secured Creditors (if secured assets insufficient) - Become unsecured for shortfall
5. Unsecured Debenture Holders - Pari passu with other unsecured creditors
6. Preference Shareholders - Paid capital + unpaid cumulative dividends
7. Equity Shareholders - Residual (if anything left)

Principle: Debenture holders (secured) have priority over equity shareholders but may rank below workmen's dues (social security policy)
```

**Example - Liquidation Distribution**:
```
Company: Real Estate Ltd (in liquidation)
Assets: ₹800 crore (after sale)

Claims:
1. Secured Debenture Holders (₹500 crore, secured by mortgage worth ₹600 crore before liquidation)
2. Workmen's Dues (₹5 crore, 200 workers × ₹24,000 average × 12 months)
3. Unsecured Debenture Holders (₹200 crore)
4. Unsecured Trade Creditors (₹150 crore)
5. Preference Shareholders (₹50 crore capital + ₹5 crore unpaid cumulative dividends)
6. Equity Shareholders (₹100 crore capital)

Distribution:
1. Secured Debenture Holders: ₹500 crore (paid from mortgaged assets, assume realized ₹600 crore) ✓
2. Liquidation Expenses: ₹10 crore (IRP fees, legal) (paid from residual ₹300 crore)
3. Workmen's Dues: ₹5 crore (paid from residual ₹290 crore) ✓
4. Unsecured Creditors (Debentures ₹200 cr + Trade ₹150 cr = ₹350 crore):
   - Available: ₹285 crore (₹290 cr - ₹5 cr workmen)
   - Recovery: ₹285 cr ÷ ₹350 cr = 81.4% (each unsecured creditor gets 81.4%)
   - Unsecured Debenture Holders: ₹162.8 crore (81.4% of ₹200 crore)
   - Trade Creditors: ₹122.2 crore (81.4% of ₹150 crore)
5. Preference Shareholders: ₹0 (nothing left)
6. Equity Shareholders: ₹0 (nothing left)

Result: Secured debenture holders 100%, Unsecured debenture holders 81.4%, Equity shareholders 0%
```

---

## 7. DEFAULT AND ENFORCEMENT

### 7.1 Events of Default

**Typical EoDs in Debenture Trust Deed**:
```
1. Non-Payment: Interest or principal overdue >30 days
2. Covenant Breach: Financial covenants (DSCR, D/E) breached
3. Cross-Default: Default in any other loan/debenture
4. Insolvency: CIRP initiated, company admits inability to pay
5. Security Impairment: Security value fallen below threshold (e.g., <1.2x debenture value)
6. Material Adverse Change: Business/financials materially worsened
```

### 7.2 Trustee's Enforcement Actions

**Step 1: Default Notice** (30 days cure period):
- Trustee issues notice to company (demand payment of principal + interest)

**Step 2: Debenture Holders' Meeting** (if company doesn't cure):
- Trustee calls meeting, seeks approval for enforcement (75% majority required)

**Step 3: Enforcement of Security** (if secured):
- Trustee files SARFAESI notice (Section 13(2), 60 days demand)
- Takes possession of charged assets
- Sells assets, distributes proceeds to debenture holders

**Step 4: CIRP Filing** (if unsecured or security insufficient):
- Trustee files CIRP application with NCLT (Section 7, IBC)
- Represents debenture holders in Committee of Creditors (CoC)

**Example - Enforcement Process**:
```
Company: Infrastructure Ltd (₹600 crore NCDs, secured by toll road assets)
Default: Missed 2 interest payments (₹30 crore each, total ₹60 crore overdue)

Day 1: Trustee issues default notice (30 days to cure ₹60 crore interest default)
Day 30: Company unable to cure (cash flow stress due to low toll collections)
Day 35: Trustee calls debenture holders' meeting (80% debenture holders vote to enforce security)
Day 40: Trustee files SARFAESI notice (demand ₹600 crore principal + ₹60 crore interest = ₹660 crore)
Day 100: Trustee takes possession of toll road (appoints operator to collect tolls)
Day 120: Toll road sold to Infra Acquisition Co for ₹720 crore (via auction)

Distribution:
- Debenture Holders: ₹660 crore (100% recovery)
- Trustee Enforcement Fee: ₹5 crore
- Surplus to Company: ₹55 crore

Result: Debenture holders recover 100% (security adequate)

Alternative (if unsecured or security insufficient):
- Trustee files CIRP with NCLT (Section 7)
- Resolution plan may offer 60-80% recovery (vs 100% with adequate security)
```

---

## 8. LISTED VS UNLISTED DEBENTURES

### 8.1 Comparison

| Parameter | Listed Debentures | Unlisted Debentures |
|---|---|---|
| **Tradability** | Traded on stock exchange (NSE, BSE) | Not traded (hold till maturity) |
| **Liquidity** | High (can sell anytime) | Low (cannot sell, except bilateral transfer) |
| **Investor Base** | Retail + institutional (broad participation) | Institutional / HNIs (narrow participation) |
| **Disclosure** | Quarterly results, annual report (public) | Private (only to debenture holders) |
| **Listing Fee** | ₹10-50 lakh (annual listing fee) | None |
| **Credit Rating** | Mandatory (Section 71(2)) | Mandatory for public issue, optional for private |
| **Pricing** | Market-determined (traded price) | Fixed (hold-to-maturity yield) |

**Example - Listed Debenture Trading**:
```
Issue: HDFC Bank ₹5,000 crore NCDs at 8.5% coupon, 7-year maturity, listed on NSE

Investor A: Buys ₹10 lakh (10 debentures @ ₹1 lakh each) at issue (Year 0)
Receives: ₹85,000 interest per year (8.5% of ₹10 lakh)

Year 3: Interest rates risen to 10% (new NCDs issue at 10%)
Market Price of Investor A's debentures: ₹92,000 per debenture (trades below par, as 8.5% coupon < 10% market)

Investor A decides to sell (needs liquidity):
- Sells 10 debentures @ ₹92,000 each = ₹9.2 lakh (8% capital loss)
- Total Return: ₹85,000 × 3 years interest + ₹9.2 lakh sale proceeds - ₹10 lakh invested = ₹455,000 (4.55% annual return vs 8.5% if held to maturity)

Investor B (buyer):
- Buys 10 debentures @ ₹92,000 each = ₹9.2 lakh
- Holds till maturity (4 years remaining)
- Receives: ₹85,000 × 4 years interest + ₹10 lakh redemption = ₹11.4 lakh
- Return: (₹11.4 lakh - ₹9.2 lakh) ÷ ₹9.2 lakh ÷ 4 years = 5.98% annual return

Benefit of Listing:
- Investor A: Liquidity (exited early despite capital loss)
- Investor B: Higher yield (10.5% YTM vs 8.5% coupon, bought at discount)
```

### 8.2 SEBI Listing Regulations

**SEBI (Issue and Listing of Debt Securities) Regulations 2021**:

**Minimum Issue Size**: ₹500 crore (listed NCDs)

**Credit Rating**: At least 2 ratings from SEBI-registered rating agencies (both must be investment grade ≥BBB)

**Minimum Application**: ₹10,000 per investor (demat form only)

**Disclosure**:
- Quarterly financials (within 45 days)
- Annual audited financials (within 60 days)
- Material events (within 24 hours)

**Investor Protection**:
- Debenture trustee mandatory (represent all debenture holders)
- Default intimation (immediate disclosure to stock exchange)

---

## 9. BEST PRACTICES

### 9.1 For Issuers

**Optimize Tenure and Coupon**:
- Longer tenure = Lower redemption pressure but higher coupon
- Match tenure to project cash flows (if funding specific project)

**Maintain Security Coverage**:
- Security value ≥1.5x debenture value (1.5x coverage ratio)
- If security value falls, top up security (prevent trustee enforcement)

**Covenant Compliance**:
- Monitor DSCR, Debt-Equity quarterly (proactive management)
- If breach anticipated, seek waiver before breach (better negotiation position)

**DRR Planning**:
- Build DRR gradually (transfer 25% over 3-5 years vs lump sum before redemption)
- Avoid strain on P&L reserves in single year

### 9.2 For Investors

**Credit Rating Review**:
- Invest only in investment-grade (≥BBB-) debentures
- Monitor rating changes (downgrades signal deteriorating credit)

**Security Analysis**:
- Verify security (CERSAI search, property valuation)
- Ensure security coverage ≥1.5x (adequate protection)

**Diversification**:
- Spread across multiple issuers (avoid concentration risk)
- Limit single-issuer exposure to 10-15% of debt portfolio

**Maturity Matching**:
- Match debenture maturity to investment horizon (avoid forced sale)
- Ladder maturities (reduce reinvestment risk)

---

## COMPLIANCE CHECKLIST

**Before Issue**:
- [ ] Board resolution approving debenture issue (amount, terms, security)
- [ ] Shareholder special resolution (if borrowing limit exceeded)
- [ ] Appoint debenture trustee (if public issue or >500 holders)
- [ ] Obtain credit rating from 2 agencies (if listed NCDs)
- [ ] Draft trust deed (debenture terms, security, covenants, trustee powers)

**At Issue**:
- [ ] Execute debenture certificates (registered to debenture holders)
- [ ] Create security (mortgage deed, hypothecation deed)
- [ ] File Form CHG-1 with ROC (within 30 days of charge creation)
- [ ] Register charge with CERSAI (within 30 days)
- [ ] Maintain debenture register (Section 117 - details of all debenture holders)

**Ongoing Compliance**:
- [ ] Pay interest on due dates (quarterly/semi-annual/annual as per terms)
- [ ] Create DRR (25% for listed, 25-100% for unlisted, before redemption)
- [ ] Submit quarterly financials to trustee (verify covenant compliance)
- [ ] Maintain security (ensure value ≥1.5x debenture outstanding)
- [ ] Renew insurance on secured assets (property, plant, machinery)
- [ ] File annual return (disclose debenture details in Form MGT-7)

**At Redemption**:
- [ ] Transfer funds to DRR (if not already done)
- [ ] Pay principal to debenture holders on redemption date
- [ ] Cancel debentures (strike off from register)
- [ ] Satisfy charge with ROC (Form CHG-4 within 30 days of redemption)
- [ ] Transfer surplus DRR to general reserves (after full redemption)

---

## LEGAL DISCLAIMER

This protocol provides information on debentures under Indian corporate law. It is for informational purposes only and does not constitute legal, financial, or investment advice. Companies should consult qualified merchant bankers, corporate lawyers, company secretaries, chartered accountants, and credit rating agencies for specific debenture issuance matters. Investors should conduct independent due diligence before investing in debentures. Legal provisions and SEBI regulations are subject to amendments.

---

**Last Updated**: December 5, 2025
**Version**: 1.0.0
**Protocol ID**: IL-CORP-DEBENTURES
