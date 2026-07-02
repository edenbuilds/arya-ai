---
id: IL-CORP-EMPLOYEE-STOCK-OPTIONS
version: 1.0.0
category: corporate_law
subcategory: corporate_finance
sections:
  - ESOP Overview
  - ESOP Schemes and Plans
  - Stock Options vs RSUs
  - Grant, Vesting, Exercise
  - Taxation of ESOPs
  - Accounting Treatment
  - SEBI SBEB Regulations
  - ESOP Pool Dilution
  - Exit and Liquidity
  - Best Practices
dependencies:
  - IL-CORP-SHARE-CAPITAL (Equity shares, authorized capital)
  - IL-CORP-EQUITY-FINANCING (Private placement, preferential allotment)
  - IL-CORP-SHAREHOLDERS-RIGHTS (Shareholder approvals for ESOP schemes)
related_protocols:
  foundation:
    - IL-COMPANIES-ACT (Companies Act 2013, Section 62)
    - IL-CORP-BOARD-MEETINGS (Board approval for ESOP grants)
  procedural:
    - IL-CORP-RELATED-PARTY-TRANSACTIONS (ESOP grants to directors/relatives)
landmark_cases:
  - Commissioner of Income Tax v. Infosys Technologies Ltd (2008) (ESOP taxation timing)
  - SEBI v. Sahara (2012) (ESOP cannot be used to circumvent public offer norms)
---

# EMPLOYEE STOCK OPTIONS (ESOPs) - INDIAN CORPORATE LAW

## OVERVIEW

Employee Stock Option Plans (ESOPs) are equity compensation tools used by companies to attract, retain, and incentivize employees by offering them the opportunity to own equity in the company. ESOPs align employee interests with shareholder interests (wealth creation through equity appreciation) and are particularly popular in startups and growth companies where cash compensation may be constrained.

**ESOP Mechanism**:
```
Grant → Vesting (time-based/milestone-based) → Exercise → Shareholding

Example Timeline:
Day 0: Grant 10,000 options at ₹10/share (fair market value)
Year 1-4: 25% vest each year (cliff vesting after Year 1)
Year 1+: Employee can exercise 2,500 vested options (pay ₹25,000, receive 2,500 shares)
Exit (IPO/Sale): Employee sells shares at ₹500/share → ₹12.5 lakh proceeds (50x return)
```

**LEGAL FRAMEWORK**:
- **Companies Act 2013**: Section 62(1)(b) (Issue of shares under ESOP)
- **Companies (Share Capital and Debentures) Rules 2014**: Rule 12 (ESOP regulations)
- **SEBI (Share Based Employee Benefits) Regulations 2014**: Detailed ESOP norms for listed companies
- **Income Tax Act 1961**: Section 17(2)(vi) (ESOP taxation as perquisite)
- **Accounting Standards**: Ind AS 102 (Share-Based Payments)

---

## 1. ESOP vs RSU vs SAR

### 1.1 Comparison of Equity Compensation Tools

| Parameter | Stock Options | Restricted Stock Units (RSUs) | Stock Appreciation Rights (SARs) |
|---|---|---|---|
| **Grant** | Option to buy shares (not shares) | Promise of shares (not actual shares) | Right to cash equivalent of share appreciation |
| **Vesting** | Time-based or milestone-based | Time-based or milestone-based | Time-based |
| **Exercise** | Employee pays exercise price | No payment (shares granted free on vesting) | No payment, no shares (cash payout only) |
| **Upfront Cost** | No (option is free at grant) | No (RSUs granted free) | No (SAR is free) |
| **Exercise Cost** | Yes (employee must pay exercise price) | No (free shares on vesting) | No (cash payout) |
| **Taxation** | At exercise + at sale (double taxation) | At vesting (as perquisite) + at sale | At cash payout (as perquisite) |
| **Dilution** | Yes (new shares issued) | Yes (new shares issued) | No (cash-settled, no dilution) |
| **Liquidity Risk** | High (may not recover exercise cost if share price falls) | Moderate (shares have value even if price falls) | Low (cash payout, no illiquidity) |

**Example**:
```
Employee A (Stock Option): Grant 1,000 options at ₹100/share
- Vests Year 1: 250 options
- Exercise: Pay ₹25,000 (250 × ₹100), receive 250 shares
- Current FMV: ₹500/share → Perquisite ₹100,000 (₹500 - ₹100) × 250 = taxable
- Sale at ₹1,000/share: ₹250,000 proceeds - ₹25,000 cost = ₹225,000 gain

Employee B (RSU): Grant 1,000 RSUs
- Vests Year 1: 250 RSUs → 250 shares granted (no payment)
- Current FMV: ₹500/share → Perquisite ₹125,000 (₹500 × 250) = taxable
- Sale at ₹1,000/share: ₹250,000 proceeds - ₹0 cost = ₹250,000 gain (vs ₹225,000 for option)

Employee C (SAR): Grant 1,000 SARs at ₹100/share
- Vests Year 1: 250 SARs
- Exercise: Receive cash = (₹500 - ₹100) × 250 = ₹100,000 (no shares issued)
- Perquisite: ₹100,000 (taxable)
- No dilution to existing shareholders (cash-settled from company profits)
```

---

## 2. ESOP SCHEME FRAMEWORK

### 2.1 ESOP Pool Creation

**ESOP Pool**: Reserved shares set aside for future grants (typically 5-15% of post-dilution equity).

**Authorization**:
```
Step 1: Increase authorized capital (if required) - Shareholder special resolution
Step 2: Create ESOP pool - Shareholder special resolution under Section 62(1)(b)
Step 3: Adopt ESOP scheme - Shareholder approval (explanatory statement with scheme details)
```

**Example - ESOP Pool Creation**:
```
Company: SaaS Startup (pre-ESOP: 10 crore shares, founders 70%, investors 30%)
ESOP Pool: 1.5 crore shares (10% post-dilution pool)

Calculation:
- Post-ESOP shares: 10 cr ÷ (1 - 0.10) = 11.11 crore shares
- ESOP pool: 1.11 crore shares (10% of 11.11 cr)

Dilution:
- Founders: 7 cr ÷ 11.11 cr = 63% (vs 70% pre-ESOP, 7% dilution)
- Investors: 3 cr ÷ 11.11 cr = 27% (vs 30% pre-ESOP, 3% dilution)
- ESOP Pool: 1.11 cr ÷ 11.11 cr = 10%

Investor Protection: Investors negotiate ESOP pool carved out BEFORE their investment (avoid further dilution)
```

### 2.2 ESOP Scheme Contents (Rule 12)

**Mandatory Clauses in ESOP Scheme**:
```
1. TOTAL OPTIONS: Maximum number of options under scheme (tied to ESOP pool)

2. ELIGIBILITY:
   - Employees (full-time, permanent)
   - Directors (executive directors, not independent directors)
   - Exclusions: Promoters with >10% equity, directors with >10% equity

3. VESTING:
   - Vesting schedule (e.g., 4 years, 25% per year, 1-year cliff)
   - Vesting conditions (time-based OR performance-based)
   - Minimum vesting period: 1 year from grant date

4. EXERCISE PRICE:
   - Listed companies: ≥Fair Market Value (FMV) on grant date (no discount without shareholder approval)
   - Unlisted companies: Determined by Compensation Committee (typically FMV or ≥face value)

5. EXERCISE PERIOD:
   - Window for exercise after vesting (e.g., 5-10 years from vesting)
   - Expiry: Options lapse if not exercised within exercise period

6. LOCK-IN:
   - Listed companies: Minimum 1 year lock-in from exercise date (SEBI)
   - Unlisted companies: Negotiable (often 1-3 years)

7. TERMINATION PROVISIONS:
   - Resignation: Unvested options lapse, vested options exercisable within 3-6 months
   - Termination for cause: All options lapse (vested + unvested)
   - Death/disability: Unvested options accelerate (vest immediately), exercise within 12 months
   - Retirement: Unvested options may vest pro-rata

8. CORPORATE ACTIONS:
   - Stock split, bonus, rights issue: Adjustment to option quantity/price (maintain economic value)
   - Merger/demerger: Options adjusted or substituted by acquiring company options

9. ADMINISTRATION:
   - Compensation Committee (min 3 non-executive directors) administers scheme
   - Board approves individual grants (within scheme limits)
```

**Example - ESOP Scheme Extract**:
```
ESOP SCHEME 2024 - ABC PRIVATE LIMITED

1. POOL: 1,00,00,000 options (representing 10% of post-dilution equity)

2. ELIGIBILITY: All full-time employees, excluding:
   (a) Promoters holding >10% equity
   (b) Directors holding >10% equity
   (c) Consultants, advisors, part-time employees

3. VESTING: 4-year vesting (1-year cliff, then 25% each year)
   - Year 1: 0% vest (cliff period)
   - Year 2: 25% vest (25% cumulative)
   - Year 3: 25% vest (50% cumulative)
   - Year 4: 25% vest (75% cumulative)
   - Year 5: 25% vest (100% cumulative)

4. EXERCISE PRICE: ₹10 per share (face value ₹10, current FMV ₹100 - 90% discount approved by shareholders)

5. EXERCISE PERIOD: 7 years from vesting date (options expire if not exercised)

6. LOCK-IN: 1 year from exercise date (shares cannot be sold/transferred)

7. TERMINATION:
   - Resignation: Unvested lapse, vested exercisable within 90 days
   - Termination for cause (fraud, misconduct): All options lapse
   - Death/disability: 100% accelerated vesting, exercise within 12 months by nominee/legal heir

8. STOCK SPLIT: If 1:10 stock split (₹10 FV → ₹1 FV):
   - Options: 1,00,000 options × 10 = 10,00,000 options
   - Exercise Price: ₹10 ÷ 10 = ₹1 per share
   - (Economic value unchanged: 1,00,000 × ₹10 = 10,00,000 × ₹1)
```

---

## 3. GRANT, VESTING, EXERCISE

### 3.1 Grant Process

**Board Approval**:
```
Compensation Committee recommends grants → Board approves

Grant Letter to Employee:
- Number of options granted (e.g., 10,000 options)
- Exercise price (₹10/share)
- Vesting schedule (4 years, 25% per year, 1-year cliff)
- Exercise period (7 years from vesting)
- Terms & conditions (termination provisions, lock-in, corporate action adjustments)
```

**Example - Grant Letter**:
```
ESOP GRANT LETTER

To: Mr. A (Employee ID: 12345, Designation: Senior Engineer)
Date: January 1, 2024

Subject: Grant of Stock Options under ESOP Scheme 2024

The Board of Directors, based on Compensation Committee recommendation, has approved grant of 10,000 (Ten Thousand) stock options to you under the ESOP Scheme 2024.

GRANT DETAILS:
- Number of Options: 10,000
- Exercise Price: ₹10 per share (face value)
- Current Fair Market Value: ₹150 per share (valuation dated December 31, 2023)
- Vesting Schedule: 4 years (1-year cliff, then 25% per year)
  - January 1, 2025: 2,500 options vest
  - January 1, 2026: 2,500 options vest
  - January 1, 2027: 2,500 options vest
  - January 1, 2028: 2,500 options vest
- Exercise Period: 7 years from vesting date
- Lock-in: 1 year from exercise date

CONDITIONS:
- Continued employment required for vesting (resignation → unvested options lapse)
- Options subject to ESOP Scheme 2024 terms
- Acceptance: Sign and return within 30 days (else grant lapses)

Signed:
CEO, ABC Private Limited

ACCEPTANCE:
I accept the above grant subject to ESOP Scheme 2024 terms.

Signed: _____________
Mr. A
Date: _______________
```

### 3.2 Vesting Mechanisms

**Time-Based Vesting** (Most Common):
```
Standard: 4 years, 25% per year, 1-year cliff
- Year 1: 0% (cliff, employee must complete 1 year for any vesting)
- Year 2: 25% vest (cumulative 25%)
- Year 3: 25% vest (cumulative 50%)
- Year 4: 25% vest (cumulative 75%)
- Year 5: 25% vest (cumulative 100%)

Alternate: 4 years monthly vesting (1/48th each month after 1-year cliff)
- Year 1: 0% (cliff)
- Months 13-48: 1/48 = 2.08% per month

Example:
10,000 options granted
Month 12 (Year 1 complete): 0 vest (cliff not crossed)
Month 13: 10,000 × 1/48 = 208 options vest
Month 24: 10,000 × 12/48 = 2,500 options vested cumulative
Month 48: 10,000 × 36/48 = 7,500 options vested cumulative (+ 2,500 from Year 1 cliff if monthly = 10,000 total)
```

**Milestone-Based/Performance Vesting**:
```
Vest only if performance milestones achieved

Example:
10,000 options, 4-year performance vesting
- Year 1 (Company ARR ≥₹50 crore): 2,500 vest
- Year 2 (Company ARR ≥₹100 crore): 2,500 vest
- Year 3 (Company ARR ≥₹200 crore): 2,500 vest
- Year 4 (IPO completed): 2,500 vest

Risk: If milestones not achieved, options don't vest (vs time-based where vesting certain if employed)
```

**Accelerated Vesting** (Exit Events):
```
Full vesting on:
- IPO (all unvested options vest immediately)
- Change of control (strategic sale/acquisition - "double-trigger" acceleration)
  - Single-trigger: Vesting on sale alone
  - Double-trigger: Vesting only if sale + termination within 12 months (protects acquirer from mass vesting)

Example (Double-Trigger):
10,000 options, 25% vested (2 years elapsed)
Company acquired by Buyer Corp
Employee terminated 6 months post-acquisition
Result: Remaining 75% (7,500 options) vest immediately (double-trigger: sale + termination)
```

### 3.3 Exercise Process

**Exercise Window**:
```
Employee can exercise anytime after vesting (within exercise period, e.g., 7 years)

Factors Influencing Exercise Timing:
1. Immediate exercise (if expecting share price rise): Lock in low FMV for taxation
2. Delay exercise (if uncertain about liquidity): Avoid upfront cash outlay, tax liability
3. Pre-exit exercise (if IPO/sale imminent): Exercise before exit, sell immediately post-exit
```

**Exercise Mechanics**:
```
Step 1: Employee submits exercise form (number of vested options to exercise)
Step 2: Employee pays exercise price (₹10/share × quantity)
Step 3: Company issues shares (credited to employee's demat account)
Step 4: Shares subject to lock-in (1 year for listed, 1-3 years for unlisted)
```

**Example - Exercise**:
```
Employee: Mr. B (10,000 options vested, exercise price ₹10/share, current FMV ₹500/share)

Exercise Decision:
- Exercise all 10,000: Pay ₹1,00,000 (10,000 × ₹10)
- Receive 10,000 shares (worth ₹50 lakh at current FMV)
- Taxable perquisite: (₹500 - ₹10) × 10,000 = ₹49 lakh (taxed at 30%+ = ₹15 lakh tax)

Total Cash Outflow: ₹1 lakh (exercise) + ₹15 lakh (tax) = ₹16 lakh

Liquidity: Shares locked in for 1 year (cannot sell immediately to recover tax)

Alternative (Partial Exercise):
- Exercise 2,000 options: Pay ₹20,000
- Perquisite: (₹500 - ₹10) × 2,000 = ₹9.8 lakh (₹3 lakh tax)
- Cash outflow: ₹20,000 + ₹3 lakh = ₹3.2 lakh (more manageable)
```

---

## 4. TAXATION OF ESOPs (Section 17(2)(vi))

### 4.1 Double Taxation Structure

**Stage 1: At Exercise** (Perquisite Tax):
```
Taxable Perquisite = (FMV on exercise date - Exercise Price) × Quantity exercised

Taxed as "Salary Income" (Section 17(2)(vi))
Tax Rate: Applicable slab rate (30% for income >₹15 lakh)
TDS: Employer must deduct TDS on perquisite (included in Form 16)
```

**Stage 2: At Sale** (Capital Gains Tax):
```
Listed Shares:
- Holding >1 year: Long-Term Capital Gains (LTCG) @ 10% on gains >₹1 lakh (Section 112A)
- Holding ≤1 year: Short-Term Capital Gains (STCG) @ 15% (Section 111A)

Unlisted Shares:
- Holding >24 months: LTCG @ 20% with indexation (Section 112)
- Holding ≤24 months: STCG at slab rate (30%)

Capital Gain = Sale Price - (FMV on exercise date)
(Not Sale Price - Exercise Price, as exercise perquisite already taxed)
```

**Example - Complete Taxation**:
```
Employee: Ms. C (Software Engineer, ₹20 lakh salary slab = 30% tax rate)
Grant: 5,000 options at ₹10 exercise price (Year 0)
Vesting: 1,250 options vest each year (Year 1-4)

YEAR 2 (Exercise):
- Vested: 2,500 options (Year 1 + Year 2 vesting)
- FMV on exercise: ₹300/share
- Exercise: Pay ₹25,000 (2,500 × ₹10)
- Perquisite: (₹300 - ₹10) × 2,500 = ₹7.25 lakh
- Tax: 30% × ₹7.25 lakh = ₹2.18 lakh (added to salary TDS)
- Total Cash Outflow: ₹25,000 (exercise) + ₹2.18 lakh (tax) = ₹2.43 lakh

YEAR 3 (IPO + Lock-in Expires):
- Shares held for 13 months (>1 year = LTCG for listed)
- Sale Price: ₹800/share (IPO listing price)
- Sale Proceeds: 2,500 × ₹800 = ₹20 lakh
- Capital Gain: (₹800 - ₹300) × 2,500 = ₹12.5 lakh
- LTCG Tax: 10% × (₹12.5 lakh - ₹1 lakh exemption) = ₹1.15 lakh

TOTAL TAX: ₹2.18 lakh (perquisite) + ₹1.15 lakh (LTCG) = ₹3.33 lakh
NET PROCEEDS: ₹20 lakh - ₹25,000 (exercise) - ₹3.33 lakh (tax) = ₹16.42 lakh

Return on ₹25,000 investment: 65.7x (₹16.42 lakh ÷ ₹25,000)
```

### 4.2 Taxation Timing Optimization

**Strategy 1: Exercise Close to Exit**:
```
If IPO/Sale expected in 6-12 months:
- Exercise immediately before exit (FMV = Exit Price, minimal perquisite)
- Sell shares post-exit (minimal capital gains)

Example:
Pre-IPO: Exercise at ₹450 FMV (vs ₹10 exercise price) → Perquisite ₹440/share
IPO: Share price ₹500 → Sell immediately post-lock-in → Capital gain ₹50/share

vs

Early Exercise: Exercise at ₹300 FMV (2 years before IPO) → Perquisite ₹290/share
IPO: Share price ₹500 → Sell → Capital gain ₹200/share (but tax cash outflow 2 years earlier)
```

**Strategy 2: Delay Exercise (Conserve Cash)**:
```
If uncertain about exit timeline or lack cash for tax:
- Don't exercise (keep as option)
- Exercise when exit imminent (liquidity to pay tax from sale proceeds)
```

---

## 5. ACCOUNTING TREATMENT (Ind AS 102)

### 5.1 Fair Value Measurement

**Ind AS 102**: ESOPs expensed over vesting period based on fair value of options granted.

**Fair Value (Black-Scholes Model)**:
```
Inputs:
- Exercise Price (₹10)
- Share Price on Grant Date (₹150)
- Expected Volatility (50% for startup)
- Risk-Free Rate (7% for 4-year govt bond)
- Expected Life (6 years = vesting 4 years + exercise window 2 years average)
- Dividend Yield (0% for startup)

Black-Scholes Formula: Fair Value = ₹142/option (illustrative)

Accounting Entry (Grant of 10,000 options):
Total Expense: 10,000 × ₹142 = ₹14.2 lakh (spread over 4-year vesting)
Annual Expense: ₹14.2 lakh ÷ 4 = ₹3.55 lakh per year
```

**Journal Entries**:
```
Year 1 (25% vest):
Dr. Employee Compensation Expense ₹3.55 lakh
Cr. Employee Stock Option Outstanding (Equity Reserve) ₹3.55 lakh

Year 2-4: Same entry each year (₹3.55 lakh per year)

At Exercise (2,500 options exercised at ₹10):
Dr. Bank ₹25,000 (exercise price paid)
Dr. Employee Stock Option Outstanding ₹3.55 lakh (transferred from reserve)
Cr. Share Capital ₹25,000 (face value ₹10 × 2,500)
Cr. Securities Premium ₹3.55 lakh (excess)

Impact on Financials:
- P&L: ₹14.2 lakh expense over 4 years (reduces profit)
- Balance Sheet: ₹14.2 lakh in equity reserves (increases net worth, offsetting P&L expense)
```

---

## 6. SEBI (SBEB) REGULATIONS 2014

### 6.1 Listed Company Requirements

**Disclosure**:
- Quarterly disclosure of ESOP grants, vesting, exercises (published on stock exchange)
- Annual disclosures: Dilution %, options outstanding, exercise price range

**Pricing**:
- Exercise price ≥FMV on grant date (unless discount approved by shareholders)
- FMV = Market price on grant date (listed companies)

**Lock-in**:
- Minimum 1 year lock-in from exercise date (cannot sell shares for 1 year)

**Vesting**:
- Minimum 1 year vesting period from grant date

**Scheme Approval**:
- Shareholder approval (special resolution) for ESOP scheme
- Disclosure in notice: Maximum options, eligible employees, vesting/exercise terms

**Example - SEBI Compliance**:
```
Company: Tech Services Ltd (listed on NSE, share price ₹1,200)
ESOP Grant: 1 lakh options to 50 employees

Compliance:
1. Exercise Price: ₹1,200 (≥market price ✓)
2. Vesting: 4 years (≥1 year ✓)
3. Lock-in: 1 year from exercise ✓
4. Shareholder Approval: Special resolution passed at AGM (85% voted YES) ✓
5. Disclosure: Filed scheme details with NSE/BSE within 15 days ✓

Quarterly Disclosure (Q1 FY 2024-25):
- Options granted: 1 lakh
- Options vested: 0 (cliff not crossed)
- Options exercised: 0
- Options outstanding: 1 lakh
- Dilution: 1 lakh ÷ (10 crore shares + 1 lakh) = 1% post-dilution
```

---

## 7. ESOP POOL DILUTION MANAGEMENT

### 7.1 Dilution Impact

**Founder Dilution**:
```
Scenario: Startup (100% founder-owned, 10 crore shares)
ESOP Pool: 1.11 crore shares (10% post-dilution)

Founder Ownership: 10 cr ÷ (10 cr + 1.11 cr) = 90%

Series A: ₹50 crore at ₹100 crore pre-money (33% to investor)
Post-A: Founders 60%, Investor 30%, ESOP 10%

Series B: ₹100 crore at ₹300 crore pre-money (25% to investor)
Post-B: Founders 45%, Series A 22.5%, Series B 25%, ESOP 7.5%

ESOP Pool Top-Up: Increase ESOP to 10% (add 0.28 crore shares)
Post-Top-Up: Founders 42.9%, Series A 21.4%, Series B 23.8%, ESOP 10%

Founder Dilution from ESOP: 100% → 42.9% (15.9% dilution from ESOP across funding rounds)
```

**Investor Protection**:
```
Investors negotiate: "ESOP pool created PRE-investment" (ESOP dilution borne by founders, not investors)

Example:
Scenario 1 (ESOP Pre-Investment):
- Pre-money: ₹100 cr (includes 10% ESOP)
- Founders: 90% pre-money
- Investment: ₹50 cr for 33%
- Post-money: Founders 60%, Investor 30%, ESOP 10%

Scenario 2 (ESOP Post-Investment):
- Pre-money: ₹100 cr (100% founders, no ESOP)
- Investment: ₹50 cr for 33%
- Post-money: Founders 66.7%, Investor 33.3%
- ESOP Created: 10% post-investment
- Final: Founders 60%, Investor 30%, ESOP 10%

Result: Same dilution outcome, but Pre-Investment ESOP protects investor from surprise post-investment ESOP pool increases
```

---

## 8. EXIT AND LIQUIDITY

### 8.1 Liquidity Events

**IPO**:
```
1. Options convert to shares (employees exercise pre-IPO or at IPO)
2. Lock-in: 1 year from exercise (SEBI) OR 1 year from IPO (for pre-IPO exercised shares)
3. Post-lock-in: Shares freely tradable (employees sell on stock exchange)
```

**Strategic Sale/Acquisition**:
```
1. Buyer acquires 100% company (drag-along)
2. Employee options:
   - Accelerated vesting (single/double-trigger)
   - Cash-out: Buyer pays (Exit Price - Exercise Price) × Options to employees (no share issuance)
   OR
   - Substitute options: Employee receives buyer company options (rollover)

Example (Cash-Out):
Employee: 5,000 options at ₹10 exercise price
Exit Price: ₹800/share
Cash-Out: (₹800 - ₹10) × 5,000 = ₹39.5 lakh (taxed as perquisite)
```

**Secondary Sale**:
```
1. Employees sell shares to secondary buyer (PE/VC, founder buyback, company buyback)
2. Pricing: Negotiated (typically at discount to last funding round, e.g., 20-30% discount)
3. Liquidity: Provides partial liquidity pre-exit (especially for early employees who exercised years ago)

Example:
Employee exercised 10,000 shares @ ₹10 (5 years ago, FMV ₹50 then)
Last funding round: ₹500/share (Series C)
Secondary Sale: ₹350/share (30% discount to Series C)
Proceeds: ₹35 lakh
Capital Gains: (₹350 - ₹50) × 10,000 = ₹30 lakh (LTCG @ 20% = ₹6 lakh tax)
Net Proceeds: ₹35 lakh - ₹6 lakh = ₹29 lakh
```

### 8.2 Buyback Programs

**Company Buyback (Section 68)**:
```
Purpose: Provide liquidity to employees (especially if no exit imminent)
Limits: Max 25% of paid-up capital + free reserves per year
Pricing: FMV (fair market value as per registered valuer)
```

**Example**:
```
Company: Profitable SaaS Company (no IPO plans for 5 years)
Buyback: ₹10 crore annual buyback for employee shares

Year 1: 50 employees sell 2 lakh shares @ ₹500 FMV = ₹10 crore
Year 2: 60 employees sell 2 lakh shares @ ₹600 FMV = ₹12 crore (exceeds ₹10 cr limit → pro-rata allocation)

Employee A (wants to sell 10,000 shares):
- Requested: 10,000 shares
- Pro-rata allocation: (₹10 cr ÷ ₹12 cr) × 10,000 = 8,333 shares accepted
- Proceeds: 8,333 × ₹600 = ₹50 lakh
```

---

## 9. BEST PRACTICES

### 9.1 For Companies

**ESOP Pool Sizing**:
- Startups: 10-15% pool (attract talent, compensate for lower cash salaries)
- Growth companies: 5-10% pool (balance dilution vs retention)
- Refresh pool: Top-up ESOP pool every 2-3 years (retain senior employees)

**Vesting Structure**:
- Standard 4-year vesting, 1-year cliff (industry standard, predictable)
- Monthly vesting post-cliff (smoother retention vs annual)
- Performance vesting for key roles (CTO, sales head - tie to deliverables)

**Exercise Window**:
- Long window (7-10 years from vesting) - employee-friendly (flexibility to exercise)
- Short window (90 days post-termination) increases forfeiture (company recovers options)

**Communication**:
- ESOP orientation (educate employees on grant, vesting, exercise, taxation)
- Annual ESOP statements (vested options, unvested, FMV, potential value)
- Exit projections (illustrative scenarios: IPO at ₹X, sale at ₹Y → employee proceeds)

### 9.2 For Employees

**Diversification**:
- Don't hold >50% net worth in company stock (concentration risk)
- Exercise and sell gradually (if liquidity available) vs holding for home-run exit

**Tax Planning**:
- Exercise when FMV low (minimize perquisite tax)
- Hold >1 year post-exercise for LTCG benefit (10% vs 30% STCG)
- Consult CA for tax optimization (especially large grants >₹50 lakh perquisite)

**Negotiate Grant**:
- Joining: Negotiate upfront grant (1-2% for senior hires in early-stage)
- Promotion/Retention: Request refresh grants (vest performance, loyalty)
- Exit: Negotiate accelerated vesting (if leaving for competitor, may forfeit)

---

## COMPLIANCE CHECKLIST

**ESOP Scheme Creation**:
- [ ] Board approves ESOP scheme (quantum, eligibility, vesting, exercise terms)
- [ ] Shareholder special resolution (75% majority) approving scheme
- [ ] File explanatory statement with notice (scheme details disclosed to shareholders)
- [ ] Increase authorized capital (if required) - Shareholder special resolution + Form SH-7
- [ ] Constitute Compensation Committee (min 3 non-executive directors)

**Grant**:
- [ ] Compensation Committee recommends grants (individual allocations)
- [ ] Board approves grants based on committee recommendation
- [ ] Grant letters issued to employees (options, exercise price, vesting, terms)
- [ ] Update ESOP register (maintain record of grants, vesting, exercise)
- [ ] Disclosure (for listed companies): File grant details with stock exchange within 15 days

**Vesting & Exercise**:
- [ ] Track vesting (automated system preferred, manual prone to errors)
- [ ] Issue exercise notices to employees (when options vest)
- [ ] Process exercise requests (collect exercise price, verify vesting)
- [ ] Issue shares (credit to employee's demat account)
- [ ] File Form PAS-3 (Return of Allotment within 30 days of exercise)
- [ ] Apply lock-in (1 year for listed, as per scheme for unlisted)

**Annual Compliance**:
- [ ] Board's Report: Disclose ESOP details (grants, vesting, exercise, outstanding)
- [ ] Accounting: Expense ESOPs as per Ind AS 102 (fair value over vesting period)
- [ ] TDS: Deduct TDS on perquisite at exercise (include in Form 16)
- [ ] Shareholder approval: If scheme modifications (increase pool, extend exercise period)

---

## LEGAL DISCLAIMER

This protocol provides information on Employee Stock Option Plans under Indian law. It is for informational purposes only and does not constitute legal, financial, tax, or investment advice. Companies should consult qualified corporate lawyers, chartered accountants, company secretaries, and valuation experts for ESOP scheme design and implementation. Employees should consult tax advisors for ESOP taxation planning. Tax laws, SEBI regulations, and accounting standards are subject to amendments.

---

**Last Updated**: December 5, 2025
**Version**: 1.0.0
**Protocol ID**: IL-CORP-EMPLOYEE-STOCK-OPTIONS
