---
id: IL-CORP-PRIVATE-EQUITY-VC
version: 1.0.0
category: corporate_law
subcategory: corporate_finance
sections:
  - PE/VC Overview
  - Investment Structures
  - Term Sheet Negotiation
  - Shareholder Agreements (SHA)
  - Liquidation Preferences
  - Anti-Dilution Protection
  - Governance Rights
  - Exit Mechanisms
  - Valuation and Pricing
  - SEBI Regulations
dependencies:
  - IL-CORP-SHAREHOLDER-AGREEMENTS (SHA clauses, tag-along, drag-along)
  - IL-CORP-EQUITY-FINANCING (Preferential allotment, private placement)
  - IL-CORP-SHARE-CAPITAL (Preference shares, CCPS)
related_protocols:
  foundation:
    - IL-COMPANIES-ACT (Companies Act 2013, Section 42, 62)
    - IL-CORP-SHAREHOLDERS-RIGHTS (Pre-emptive rights, shareholder approvals)
  procedural:
    - IL-CORP-RELATED-PARTY-TRANSACTIONS (RPT if investor becomes related party)
landmark_cases:
  - Vodafone International Holdings v. Union of India (2012) 6 SCC 613 (Indirect transfer, SHA enforceability)
  - WestBridge Ventures v. Flipkart (2020) (Investor protection, SHA enforcement)
---

# PRIVATE EQUITY AND VENTURE CAPITAL - INDIAN CORPORATE LAW

## OVERVIEW

Private Equity (PE) and Venture Capital (VC) are forms of equity financing where institutional investors (PE/VC funds) invest in private companies in exchange for equity ownership. PE/VC investors provide not just capital but also strategic guidance, operational expertise, and network access to help companies scale. Unlike public equity (stock market), PE/VC investments are illiquid, long-term (5-10 years), and require sophisticated investor protections via Shareholder Agreements (SHA).

**PE vs VC**:

| Parameter | Private Equity (PE) | Venture Capital (VC) |
|---|---|---|
| **Stage** | Growth/mature companies (established) | Early-stage startups (seed, Series A/B) |
| **Investment Size** | ₹50 crore - ₹1,000+ crore | ₹5 crore - ₹100 crore |
| **Equity Stake** | Majority (>51%) or significant minority (25-49%) | Minority (<25%) |
| **Risk** | Moderate (proven business model) | High (unproven, high failure rate) |
| **Return Expectation** | 2-3x return (IRR 15-25%) | 5-10x return (IRR 30-50%+) |
| **Investment Instrument** | Equity, CCPS, debt | Equity, CCPS |
| **Holding Period** | 5-7 years | 7-10 years |
| **Exit** | Strategic sale, IPO, buyback | IPO, strategic sale, secondary sale |

**LEGAL FRAMEWORK**:
- **Companies Act 2013**: Section 42 (Private placement), Section 62 (Preferential allotment)
- **SEBI (AIF) Regulations 2012**: Regulation of VC/PE funds as Alternative Investment Funds
- **FEMA (Foreign Exchange Management Act) 1999**: Foreign VC/PE investment in Indian companies
- **Income Tax Act 1961**: Section 56(2)(viib) (Angel Tax), Section 112A (LTCG on listed equity)

---

## 1. INVESTMENT STRUCTURES

### 1.1 Equity Shares

**Structure**: Investor subscribes to equity shares (same class as founders).

**Advantages**:
- Simple structure (no complex preferences)
- Same economic rights as founders (pro-rata dividends, liquidation proceeds)
- Suitable for early-stage/seed (when downside protection less critical)

**Disadvantages**:
- No liquidation preference (investor loses money if exit valuation <investment valuation)
- No downside protection (ranks pari passu with founders in liquidation)

**Example**:
```
Company: SaaS Startup (pre-money valuation ₹50 crore, founders own 100%)
VC Investment: ₹20 crore for equity shares

Post-Money Valuation: ₹50 cr + ₹20 cr = ₹70 crore
VC Ownership: ₹20 cr ÷ ₹70 cr = 28.6%
Founder Ownership: 71.4%

Exit Scenario 1 (IPO at ₹200 crore valuation):
- VC Proceeds: 28.6% × ₹200 cr = ₹57.2 crore (2.86x return)

Exit Scenario 2 (Distress Sale at ₹30 crore):
- VC Proceeds: 28.6% × ₹30 cr = ₹8.58 crore (0.43x return, 57% loss)
- Founder Proceeds: 71.4% × ₹30 cr = ₹21.42 crore (also lose)
```

### 1.2 Compulsorily Convertible Preference Shares (CCPS)

**Structure**: Investor subscribes to CCPS (preference shares that convert to equity at future date/milestone).

**Advantages**:
- **Liquidation Preference**: CCPS holders paid before equity in liquidation (downside protection)
- **Participation Rights**: Can participate in residual proceeds after preference paid (participating CCPS)
- **Cumulative Dividend**: Entitled to fixed dividend (typically 0.01% non-cumulative or 8% cumulative)
- **Conversion Ratio**: Fixed or variable (based on valuation adjustments)

**Disadvantages**:
- More complex (requires valuation, conversion mechanics in SHA)
- Tax implications (dividend taxable if cumulative)

**Example**:
```
Company: E-commerce Startup (pre-money ₹100 crore)
PE Investment: ₹50 crore for CCPS (1x liquidation preference, non-participating)

Post-Money Valuation: ₹150 crore
PE Ownership (as-converted): ₹50 cr ÷ ₹150 cr = 33.3%

Exit Scenario 1 (IPO at ₹500 crore):
CCPS converts to equity at IPO (all preference rights extinguish)
PE Proceeds: 33.3% × ₹500 cr = ₹166.5 crore (3.33x return)

Exit Scenario 2 (Distress Sale at ₹80 crore):
Liquidation Waterfall:
1. CCPS Holders (1x preference): ₹50 crore (paid first)
2. Residual to Equity: ₹30 crore (₹80 cr - ₹50 cr)
3. Founder Proceeds: 66.7% × ₹30 cr = ₹20 crore

PE Downside Protection: ₹50 crore (100% capital back despite distress valuation)
Founder Downside: ₹20 crore (vs ₹66.7 crore invested if calculated pro-rata)

If Participating CCPS:
PE gets ₹50 cr (preference) + 33.3% × ₹30 cr (participation) = ₹60 crore
Founders get ₹20 crore (worse off than non-participating)
```

### 1.3 Optionally Convertible Debentures (OCDs) / Convertible Notes

**Structure**: Investor provides loan (debenture) that can convert to equity at investor's option.

**Advantages**:
- **Bridge Financing**: Quick capital (no valuation negotiation upfront)
- **Interest Income**: Investor earns interest till conversion (8-12% typical)
- **Valuation Discount**: Converts at discount to next round valuation (15-25% discount typical)

**Disadvantages**:
- Debt on balance sheet (affects debt-equity ratio)
- Interest obligation (even if unprofitable)
- Tax risk (SEBI v. Sahara - OCDs may be deemed equity if marketed widely)

**Example**:
```
Company: Fintech Startup (raising Series A but need immediate capital)
Investor: Angel investor provides ₹2 crore via Convertible Note

Terms:
- Interest: 10% per annum
- Conversion Discount: 20% to next round valuation
- Maturity: 18 months (convert or redeem)

Scenario 1: Series A in 12 months at ₹100 crore pre-money
- Convertible Note converts at 20% discount: ₹80 crore effective valuation
- Investment: ₹2 crore + ₹0.2 crore accrued interest = ₹2.2 crore
- Ownership: ₹2.2 cr ÷ (₹80 cr + Series A amount) (calculated post-Series A)

If Series A is ₹20 crore:
- Post-Money: ₹80 cr + ₹20 cr + ₹2.2 cr (convertible note) = ₹102.2 crore
- Angel Ownership: ₹2.2 cr ÷ ₹102.2 cr = 2.15%
- Series A Ownership: ₹20 cr ÷ ₹102.2 cr = 19.6%
- Founder Ownership: 78.25%

Scenario 2: No Series A raised (18 months elapse)
- Angel exercises redemption (maturity)
- Company repays ₹2 crore principal + ₹0.3 crore interest (10% × 18/12) = ₹2.3 crore
```

---

## 2. TERM SHEET NEGOTIATION

### 2.1 Term Sheet Overview

**Term Sheet**: Non-binding memorandum of understanding outlining key commercial terms of investment.

**Binding Clauses**: Exclusivity (no-shop), confidentiality, governing law.

**Non-Binding Clauses**: Valuation, investment amount, liquidation preference, governance (finalized in SHA).

**Key Sections**:
1. **Investment Structure**: Amount, instrument (CCPS/equity), valuation (pre-money, post-money)
2. **Liquidation Preference**: 1x/2x, participating/non-participating
3. **Anti-Dilution**: Full ratchet, weighted average (broad-based/narrow-based)
4. **Governance**: Board seats, observer rights, reserved matters (investor veto)
5. **Exit Rights**: Tag-along, drag-along, IPO rights, redemption
6. **Conditions Precedent**: Due diligence, legal documentation

### 2.2 Valuation Negotiation

**Pre-Money vs Post-Money Valuation**:
```
Pre-Money Valuation: Company value BEFORE investment
Post-Money Valuation: Company value AFTER investment

Formula: Post-Money = Pre-Money + Investment Amount

Investor Ownership = Investment ÷ Post-Money

Example:
Pre-Money: ₹80 crore
Investment: ₹20 crore
Post-Money: ₹100 crore
Investor Ownership: 20%
```

**Valuation Methods**:
1. **Comparable Company Analysis**: Peer multiples (EV/Revenue, EV/EBITDA, P/E)
2. **Discounted Cash Flow (DCF)**: Present value of projected cash flows
3. **Venture Capital Method**: Exit value ÷ (1 + Required Return)^Years

**Example - VC Method**:
```
Startup: AI SaaS (ARR ₹10 crore, growing 100% YoY)
Projected ARR Year 5: ₹160 crore (CAGR 100%)
Exit Multiple: 10x ARR (SaaS industry standard)
Exit Value: ₹1,600 crore

VC Required Return: 10x in 5 years (58% IRR)
Pre-Money Valuation: ₹1,600 cr ÷ 10 = ₹160 crore

Investment: ₹40 crore
Post-Money: ₹200 crore
VC Ownership: 20%

Exit Check: 20% × ₹1,600 cr = ₹320 crore (₹40 cr × 8x = 320 cr, but required 10x, so negotiation may lower valuation)

Revised Valuation:
If VC insists on 10x return (₹400 crore exit proceeds):
Required Ownership: ₹400 cr ÷ ₹1,600 cr = 25%
Pre-Money: (₹40 cr ÷ 0.25) - ₹40 cr = ₹120 crore (25% lower)
```

---

## 3. LIQUIDATION PREFERENCES

### 3.1 Types of Liquidation Preferences

**1x Non-Participating Preference** (Most Common, Balanced):
```
Investor gets HIGHER of:
(a) 1x invested capital, OR
(b) Pro-rata share of proceeds (as-converted ownership %)

Example:
Investment: ₹50 crore for 25% (as-converted)
Exit at ₹300 crore:
Option (a): 1x = ₹50 crore
Option (b): 25% × ₹300 cr = ₹75 crore
Investor chooses (b): ₹75 crore (higher)

Exit at ₹150 crore:
Option (a): 1x = ₹50 crore
Option (b): 25% × ₹150 cr = ₹37.5 crore
Investor chooses (a): ₹50 crore (higher, downside protection)
```

**1x Participating Preference** (Investor-Friendly, "Double-Dip"):
```
Investor gets:
(a) 1x invested capital FIRST, THEN
(b) Pro-rata share of REMAINING proceeds

Example:
Investment: ₹50 crore for 25%
Exit at ₹300 crore:
Step 1: Investor gets ₹50 crore (1x preference)
Step 2: Remaining ₹250 crore split pro-rata (investor 25%, founders 75%)
Step 3: Investor gets 25% × ₹250 cr = ₹62.5 crore
Total Investor Proceeds: ₹50 cr + ₹62.5 cr = ₹112.5 crore
Founder Proceeds: ₹187.5 crore

Investor Return: ₹112.5 cr ÷ ₹50 cr = 2.25x (vs 1.5x non-participating)
```

**2x Non-Participating Preference** (Rare, High-Risk Deals):
```
Investor gets HIGHER of:
(a) 2x invested capital, OR
(b) Pro-rata share of proceeds

Example:
Investment: ₹50 crore for 25%
Exit at ₹300 crore:
Option (a): 2x = ₹100 crore
Option (b): 25% × ₹300 cr = ₹75 crore
Investor chooses (a): ₹100 crore

Exit at ₹500 crore:
Option (a): 2x = ₹100 crore
Option (b): 25% × ₹500 cr = ₹125 crore
Investor chooses (b): ₹125 crore (converts to common, higher return)
```

### 3.2 Participation Cap

**Capped Participating Preference** (Compromise between Non-Participating and Participating):
```
Investor gets:
(a) 1x preference + participation, BUT
(b) Capped at 3x invested capital (cap limits upside)

Example:
Investment: ₹50 crore for 25%
Exit at ₹800 crore:
Participating: ₹50 cr + (25% × ₹750 cr) = ₹237.5 crore
Cap: 3x = ₹150 crore
Investor gets: ₹150 crore (capped, converts to common for excess ₹87.5 cr)

Without Cap:
Investor would get ₹237.5 crore (4.75x return vs 3x capped)
Founders benefit from cap on large exits
```

---

## 4. ANTI-DILUTION PROTECTION

### 4.1 Down-Round Protection

**Down-Round**: Subsequent funding round at LOWER valuation than previous round (dilutes existing investors).

**Anti-Dilution Mechanisms**:

**1. Full Ratchet** (Investor-Friendly, Extremely Dilutive to Founders):
```
Investor's conversion price resets to lower round price (ignoring amount raised)

Example:
Series A: ₹100/share (investor owns 2 million shares, ₹200 crore invested)
Series B (Down-Round): ₹50/share (50% lower)

Full Ratchet:
- Investor's price resets from ₹100 to ₹50
- Investor's shares: ₹200 cr ÷ ₹50 = 4 million shares (DOUBLED)
- Founder dilution: Massive (founder ownership halved)

Pre-Series B: Investor 20%, Founders 80%
Post-Series B (Full Ratchet): Investor 33%, Founders 67% (founder ownership drops 13% despite no new Series B investor)
```

**2. Weighted Average Broad-Based** (Balanced, Standard in India):
```
Formula:
New Price = Old Price × [(Old Shares + New Shares at Old Price) ÷ (Old Shares + New Shares Issued)]

Example:
Series A: ₹100/share, 2 million shares, ₹200 crore invested
Total Shares Pre-Series B: 10 million (founders 8M, investor 2M)
Series B (Down-Round): ₹50/share, ₹100 crore raised = 2 million shares

New Price = ₹100 × [(10M + (₹100 cr ÷ ₹100)) ÷ (10M + 2M)]
           = ₹100 × [(10M + 1M) ÷ 12M]
           = ₹100 × (11M ÷ 12M)
           = ₹91.67

Investor's New Shares: ₹200 cr ÷ ₹91.67 = 2.18 million shares (9% increase vs 100% under full ratchet)

Post-Series B: Investor 18.2%, Founders 66.7%, Series B 16.7%
```

**3. Weighted Average Narrow-Based** (More Dilutive than Broad-Based):
```
Same formula but "Old Shares" includes only Common Stock (excludes ESOP pool, warrants)
→ Higher dilution to founders (smaller denominator)
```

**4. Pay-to-Play** (Founder-Friendly, Penalizes Non-Participating Investors):
```
Anti-dilution protection ONLY for investors who participate pro-rata in down-round
Non-participating investors: Lose anti-dilution (or convert to common)

Example:
Series B down-round: Investor A participates pro-rata (gets anti-dilution ✓)
Investor B does not participate (loses anti-dilution, stuck at ₹100/share)
```

---

## 5. GOVERNANCE RIGHTS

### 5.1 Board Representation

**Typical Board Composition**:
```
5-Director Board:
- 2 Founder Directors (CEO, CTO)
- 2 Investor Nominees (1 PE, 1 VC)
- 1 Independent Director (mutually agreed)

7-Director Board (Larger Company):
- 3 Founder/Executive Directors
- 3 Investor Nominees (proportional to ownership)
- 1 Independent Director
```

**Observer Rights**:
- Non-voting participant in board meetings
- Receives all board papers, attends meetings, but cannot vote
- Useful for minority investors (<10% ownership)

**Example**:
```
Company: Fintech Startup (post-Series B)
Ownership: Founders 60%, PE 25%, VC 15%

Board: 5 directors
- Founder Directors: 2 (CEO, COO)
- PE Nominee: 1 (senior partner from PE fund)
- VC Observer: 1 (cannot vote, attends meetings)
- Independent Director: 1 (ex-banker with fintech expertise)

PE negotiates voting director (25% ownership justifies 1 seat = 20% board representation)
VC accepts observer (15% ownership insufficient for voting seat in 5-member board)
```

### 5.2 Reserved Matters (Investor Veto Rights)

**Reserved Matters** requiring investor approval (typically 75% preference shareholder votes OR specific investor veto):

```
CATEGORY A: CAPITAL STRUCTURE
1. Issuance of new shares (except ESOP within approved pool)
2. Buyback, capital reduction
3. Alteration of MOA/AOA (capital, objects clauses)
4. Liquidation, winding up

CATEGORY B: M&A AND ASSET SALES
5. Merger, amalgamation, demerger, scheme of arrangement
6. Sale of business/undertaking (asset sale >10% of book value)
7. Acquisition of business/company (consideration >₹10 crore)

CATEGORY C: DEBT AND ENCUMBRANCES
8. Borrowing >₹50 crore
9. Creating security on assets (except working capital hypothecation)
10. Guarantees for third parties >₹25 crore

CATEGORY D: RELATED PARTY TRANSACTIONS
11. RPT with founders/directors/relatives (except salary/sitting fees as per policy)
12. Loans to directors/relatives

CATEGORY E: MANAGEMENT AND OPERATIONS
13. Appointment/removal of CEO, CFO, CTO (C-suite)
14. CEO/CFO compensation increase >20% per annum
15. Entering new line of business (material deviation from approved business plan)
16. Annual budget approval (capex, opex, hiring plan)

CATEGORY F: ESOP AND COMPENSATION
17. ESOP pool increase (beyond approved 10%)
18. Granting ESOPs to any individual >1% of issued capital

CATEGORY G: EXITS AND LIQUIDITY
19. IPO (timing, pricing, OFS by investors)
20. Sale to strategic buyer (approval of buyer, valuation, terms)

CATEGORY H: SHA AMENDMENTS
21. Amendment of SHA/voting agreement
22. Admission of new investors (except in approved funding rounds)
```

**Example - Reserved Matter in Action**:
```
Company: SaaS Startup (Founders 65%, PE 25%, VC 10%)
Proposed Action: Acquire competitor for ₹30 crore (strategic M&A)

Reserved Matter: Acquisition >₹10 crore requires investor approval (75% preference shareholders OR affirmative vote of PE)

Process:
1. Board Meeting: Management presents acquisition rationale
   - Competitor has 5,000 customers, ₹15 crore ARR
   - Synergy: Consolidate market, eliminate competition, upsell/cross-sell
   - Valuation: 2x ARR (market rate for SaaS acquisitions)
2. Board Votes:
   - Founders (2 directors): YES
   - PE (1 director): YES (supports growth via M&A)
   - Independent (1 director): YES
   - VC (Observer): Cannot vote
3. Reserved Matter Vote (Preference Shareholders):
   - PE (25%): YES (affirmative investor vote ✓)
   - VC (10%): YES (supportive but PE vote alone sufficient)
4. Result: Acquisition APPROVED ✓

Alternative Scenario (PE votes NO):
- PE believes ₹30 crore overvalued (should be 1.5x ARR = ₹22.5 crore)
- PE exercises veto (reserved matter)
- Result: Acquisition REJECTED (even though 3/4 board directors voted YES)
- Management must renegotiate price or abandon deal
```

---

## 6. EXIT MECHANISMS

### 6.1 Tag-Along Rights

**Tag-Along (Co-Sale Rights)**: If founder sells shares, minority investors can "tag along" (sell proportionately at same price).

**Purpose**: Protect minority investors from being left in illiquid company after founder exits.

**Mechanism**:
```
1. Founder receives offer to sell shares (e.g., strategic buyer offers to buy founder's 60% stake)
2. Founder must notify investors (tag-along trigger)
3. Investors have 15-30 days to elect to tag along
4. Buyer must purchase investors' shares at same per-share price as founder
5. If buyer refuses to buy investors' shares, founder sale reduced proportionately
```

**Example**:
```
Company: E-commerce Startup
Ownership: Founder 60%, PE 30%, VC 10%
Strategic Buyer Offer: Buy Founder's 60% stake at ₹500 crore (₹833/share × 60M shares)

Tag-Along Exercise:
- PE elects to tag along (30% = 30M shares)
- VC elects to tag along (10% = 10M shares)
- Total tag-along: 40M shares (PE + VC)

Scenario 1 (Buyer accepts tag-along):
- Buyer purchases: Founder 60M + PE 30M + VC 10M = 100M shares (100% acquisition)
- Total consideration: 100M shares × ₹833/share = ₹833 crore
- Founder proceeds: ₹500 crore
- PE proceeds: ₹250 crore
- VC proceeds: ₹83 crore

Scenario 2 (Buyer only wants 60% stake, refuses full tag-along):
- Buyer will buy only 60M shares total (not 100M)
- Tag-along pro-rata reduction:
  - Founder: 60% ÷ (60% + 30% + 10%) = 60% of 60M = 36M shares sold (24M retained)
  - PE: 30% ÷ 100% = 30% of 60M = 18M shares sold (12M retained)
  - VC: 10% ÷ 100% = 10% of 60M = 6M shares sold (4M retained)
- Result: All stakeholders sell proportionately, maintain relative ownership in remaining company
```

### 6.2 Drag-Along Rights

**Drag-Along**: If majority investors approve sale, minority investors (including founders) must sell on same terms (forced exit).

**Purpose**: Enable clean 100% acquisition (buyer wants full control, not minority holdouts).

**Threshold**: Typically 75% shareholders (or 75% preference + founder approval).

**Mechanism**:
```
1. Buyer offers to acquire 100% company
2. Majority investors (75%+ shareholders) approve sale
3. Drag-along triggered: Minority shareholders MUST sell (no veto)
4. Minority receives same per-share price as majority
```

**Example**:
```
Company: Logistics Startup (mature, profitable)
Ownership: Founder 40%, PE 45%, VC 15%
Strategic Buyer Offer: Acquire 100% for ₹1,000 crore

Drag-Along Exercise:
- PE (45%) + VC (15%) = 60% (insufficient for 75% threshold)
- PE + VC seek Founder consent: Founder initially resists (wants to continue building)
- PE/VC invoke drag-along clause (75% shareholders = PE 45% + VC 15% + need 15% more)

Negotiation:
- Founder negotiates: Retention bonus (₹20 crore paid 1 year post-acquisition if Founder stays)
- Founder agrees to drag-along
- Result: 100% sale approved (85% voted YES = Founder 40% + PE 45%, dragging along dissenting VC minority if any)

Distribution:
- Founder: 40% × ₹1,000 cr = ₹400 crore + ₹20 cr retention = ₹420 crore
- PE: 45% × ₹1,000 cr = ₹450 crore
- VC: 15% × ₹1,000 cr = ₹150 crore

VC had no choice (drag-along forced sale) but received fair price (same ₹/share as majority)
```

### 6.3 Redemption (Put Option)

**Redemption Rights**: Investor can demand company buy back shares after holding period (typically 5-7 years).

**Trigger**: No IPO, no strategic sale, investor wants liquidity.

**Redemption Price**: Higher of (a) 1.2x invested capital OR (b) Fair market value (FMV).

**Example**:
```
Investment: ₹100 crore for 25% (Year 0)
Redemption: After 7 years (no exit materialized)

Year 7 Company Value:
- FMV: ₹300 crore (25% = ₹75 crore)
- 1.2x Investment: ₹120 crore

Redemption Price: ₹120 crore (higher of ₹75 cr or ₹120 cr)

Company Obligation:
- Pay ₹120 crore to investor (redeem 25% shares)
- Funding: Raise debt, use cash reserves, or find replacement investor

If company cannot pay (insolvency risk):
- Liquidation drag-along: If 75% preference shareholders vote, force liquidation
- Investor recovers via liquidation preference (1x or 2x)
```

---

## 7. SEBI REGULATIONS

### 7.1 SEBI (AIF) Regulations 2012

**Alternative Investment Funds (AIFs)**: VC/PE funds registered with SEBI.

**Categories**:
```
Category I (Social/Early-Stage):
- Venture Capital Funds (VCFs)
- Angel Funds
- SME Funds
- Exemption: Pass-through tax status (tax at investor level, not fund level)

Category II (PE/Debt Funds):
- Private Equity Funds
- Debt Funds
- Fund of Funds
- No specific incentives, no leverage

Category III (Hedge Funds):
- Hedge Funds
- PIPE (Private Investment in Public Equity)
- Can use leverage, derivatives
```

**Minimum Investment**: ₹1 crore per investor (₹25 lakh for employees/directors of AIF).

**Minimum Corpus**: ₹20 crore (must be raised within 12 months of first close).

**Example - AIF Structure**:
```
AIF: XYZ Venture Fund (Category I VCF)
Corpus: ₹500 crore (50 investors × ₹10 crore average)

Fund Structure:
- General Partner (GP): Fund manager (XYZ Ventures LLP, 2% management fee + 20% carried interest)
- Limited Partners (LPs): Investors (HNIs, family offices, corporates, institutions)

Investment Portfolio:
- 15 startups (average ₹33 crore per startup)
- Stage: Series A/B (early growth stage)
- Holding Period: 7-10 years
- Target IRR: 30%+

Fee Structure:
- Management Fee: 2% per annum on committed capital (₹500 cr × 2% = ₹10 cr/year for 10 years)
- Carried Interest: 20% of profits above 8% hurdle rate

Exit Scenario (Year 10):
- Portfolio Value: ₹2,500 crore (5x return)
- Profit: ₹2,500 cr - ₹500 cr = ₹2,000 crore
- Hurdle Amount: ₹500 cr × (1.08)^10 = ₹1,079 crore
- Profit above hurdle: ₹2,500 cr - ₹1,079 cr = ₹1,421 crore
- GP Carried Interest: 20% × ₹1,421 cr = ₹284 crore
- LP Proceeds: ₹2,500 cr - ₹284 cr = ₹2,216 crore (4.4x net return to LPs)
```

### 7.2 Angel Tax (Section 56(2)(viib), Income Tax Act)

**Angel Tax**: Tax on startups receiving funding at valuation higher than Fair Market Value (FMV).

**Trigger**: Startup issues shares to resident angel investor at premium >FMV → Excess premium taxed as "Income from Other Sources" (30% tax).

**Exemption** (as of 2023):
- DPIIT-recognized startups: Exempt from Angel Tax (up to ₹25 crore aggregate funding)
- Funding from Category I/II AIFs, listed companies, government: Exempt

**Example**:
```
Startup: AI SaaS (pre-revenue, 1 year old)
Angel Investment: ₹5 crore for 10% equity
Implied Valuation: ₹50 crore post-money

FMV (per Income Tax DCF method): ₹20 crore (discounted for pre-revenue stage, execution risk)
Share Premium: ₹4.5 crore (₹5 cr investment - ₹0.5 cr face value)
FMV Share Premium: ₹1.8 crore (10% × ₹20 cr - ₹0.5 cr face value)

Excess Premium: ₹4.5 cr - ₹1.8 cr = ₹2.7 crore
Angel Tax: 30% × ₹2.7 cr = ₹81 lakh

Exemption:
- If startup is DPIIT-recognized (incorporation <10 years, turnover <₹100 cr, innovative business)
- Angel Tax: ₹0 (exempt)

OR

- If angel invests via Category I AIF (not direct investment)
- Angel Tax: ₹0 (exempt under Section 56(2)(viib) proviso)
```

---

## 8. DUE DILIGENCE

### 8.1 Due Diligence Checklist

**Legal DD**:
- Incorporation documents (MOA, AOA, Certificate of Incorporation)
- Shareholding pattern, cap table (verify founder ownership, ESOP grants, past investors)
- SHA, voting agreements, side letters (identify investor rights, obligations)
- Material contracts (customer/supplier contracts >₹1 crore, exclusivity agreements)
- Litigation (pending/threatened, regulatory notices, IP disputes)
- Intellectual Property (patents, trademarks, copyrights, domain names - ownership, validity, infringement risk)
- Employee agreements (founder service agreements, key employee contracts, non-compete, IP assignment)
- Compliance (statutory filings, ROC filings, tax returns, PF/ESI, POSH)

**Financial DD**:
- Audited financials (3 years), management accounts (current FY)
- Revenue recognition (quality of revenue, customer concentration, churn)
- Unit economics (CAC, LTV, gross margin, contribution margin)
- Cash flow (burn rate, runway, working capital)
- Projections (revenue, EBITDA, cash flow for 5 years - reasonableness, assumptions)

**Commercial DD**:
- Business model (scalability, defensibility, competitive advantage)
- Market size (TAM, SAM, SOM), growth rate
- Competition (market share, differentiation, pricing power)
- Customer analysis (top 10 customers, retention, NPS)
- Product/technology (product-market fit, tech stack, scalability)

**Management DD**:
- Founder background (education, prior experience, domain expertise)
- Key employees (CTO, CFO, sales head - retention risk)
- Culture, values (founder integrity, team dynamics)
- References (prior investors, customers, ex-employees)

### 8.2 Red Flags

**Fatal Red Flags** (Deal-Breakers):
- Founder integrity issues (fraud, misrepresentation, criminal record)
- IP not owned by company (founders/employees own key IP, licensing disputes)
- Material litigation (₹10 crore+ exposure, adverse judgment likely)
- Regulatory non-compliance (unlicensed operations, show cause notices)
- Customer concentration (>50% revenue from 1 customer, churn risk)

**Moderate Red Flags** (Fixable with Conditions):
- Missing ROC filings (can be rectified with compounding fees)
- ESOP grants without board approval (can be ratified)
- Related party transactions without proper approvals (can be regularized)
- Founder shareholding pledged (can be released pre-investment)

---

## COMPLIANCE CHECKLIST

**Pre-Investment**:
- [ ] Execute term sheet (binding: exclusivity, confidentiality; non-binding: commercial terms)
- [ ] Conduct due diligence (legal, financial, commercial, management) - 60-90 days
- [ ] Negotiate and finalize SHA (incorporate investor protections, governance rights)
- [ ] Obtain board approval (investee company) for private placement/preferential allotment
- [ ] Obtain shareholder approval (special resolution if required under Section 180)

**At Investment Closing**:
- [ ] Execute subscription agreement (investor subscribes to CCPS/equity)
- [ ] Execute SHA (all shareholders sign, including founders, existing investors)
- [ ] Execute voting agreement (if applicable, for board/shareholder matters)
- [ ] Investor pays subscription amount (₹X crore transferred to company bank account)
- [ ] Company issues shares/CCPS to investor (share certificates, demat credit)
- [ ] File Form PAS-3 with ROC (Return of Allotment within 30 days)
- [ ] Update MOA (if authorized capital increased), file Form SH-7 with ROC

**Post-Investment Compliance**:
- [ ] Quarterly board meetings (investor nominee director attends, reviews financials)
- [ ] Annual general meeting (investor attends, approves accounts, dividends)
- [ ] Quarterly/monthly MIS (financial statements, KPIs shared with investor per SHA)
- [ ] Reserved matters approval (seek investor consent for M&A, capex >threshold, new debt)
- [ ] ESOP grants (within approved pool, investor notified)
- [ ] Fundraising (investor right of first refusal on next funding round, pro-rata participation)

**At Exit**:
- [ ] Board approval for exit transaction (IPO/strategic sale/buyback)
- [ ] Investor approval (reserved matter, typically requires 75% preference shareholders)
- [ ] Execute exit documents (share purchase agreement for strategic sale, OFS for IPO)
- [ ] Investor sells shares (receives exit proceeds per liquidation preference/as-converted)
- [ ] File Form SH-4 with ROC (notice of transfer/transmission of shares)
- [ ] Close CCPS (if CCPS converts to equity at IPO, file conversion details with ROC)

---

## LEGAL DISCLAIMER

This protocol provides information on private equity and venture capital transactions under Indian law. It is for informational purposes only and does not constitute legal, financial, or investment advice. Companies and investors should consult qualified corporate lawyers, chartered accountants, merchant bankers, and financial advisors for specific PE/VC transactions. Term sheets, shareholder agreements, and investment structures vary significantly based on negotiation. Legal provisions and SEBI regulations are subject to amendments.

---

**Last Updated**: December 5, 2025
**Version**: 1.0.0
**Protocol ID**: IL-CORP-PRIVATE-EQUITY-VC
