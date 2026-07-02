# IL-CORP-SHARE-CAPITAL
## Share Capital Structure, Types, and Operations

---
id: IL-CORP-SHARE-CAPITAL
version: 1.0.0
category: corporate_law
subcategory: company_formation
sections:
  - Types of Share Capital
  - Types of Shares
  - Share Allotment Procedure
  - Share Transfer and Transmission
  - Share Buyback
  - Capital Reduction
  - Forfeiture and Surrender of Shares
dependencies:
  - IL-CORP-MOA-AOA (Capital clause in MOA)
  - IL-COMPANIES-ACT (Companies Act 2013 provisions)
related_protocols:
  foundation:
    - IL-CORP-INCORPORATION-PROCESS (Initial capital structure)
    - IL-CORP-SHAREHOLDERS-RIGHTS (Shareholder rights attached to shares)
  procedural:
    - IL-CORP-EQUITY-FINANCING (Share issuance for fundraising)
    - IL-CORP-BOARD-MEETINGS (Board approval for share allotment)
landmark_cases:
  - Trevor v. Whitworth (1887) 12 AC 409 (Share buyback principles)
  - Ooregum Gold Mining Co v. Roper [1892] AC 125 (Capital reduction)
  - National Westminster Bank v. IRC [1995] 1 AC 119 (Share capital maintenance)
---

## Overview

**Share Capital** = Total capital raised by company through issuance of shares.

**Legal Framework**:
- Companies Act 2013: Sections 39-68 (Share Capital and Debentures)
- Companies (Share Capital and Debentures) Rules 2014
- SEBI (Issue of Capital and Disclosure Requirements) Regulations 2018 (for listed companies)

**Key Principle**: **Capital Maintenance Doctrine** - Company must maintain its capital for creditor protection. Cannot return capital to shareholders except via legal procedures (buyback, capital reduction, dividends from profits).

---

## Types of Share Capital

### 1. Authorized Share Capital (Nominal Capital)

**Definition**: Maximum capital company is authorized to raise as per MOA capital clause.

**Example**:
- MOA: "Authorized Capital ₹10,00,000 divided into 1,00,000 equity shares of ₹10 each"
- Company authorized to issue up to 1 lakh shares (max capital = ₹10 lakh)

**Characteristics**:
- Fixed in MOA (cannot be exceeded without alteration)
- Stamp duty payable on authorized capital (at incorporation + on increase)
- No obligation to issue entire authorized capital

**Increase Procedure** (Section 61):
- Ordinary resolution in general meeting
- Alter MOA capital clause
- File Form SH-7 with ROC (within 30 days)
- Pay stamp duty (state-wise variation: ₹500 - ₹2,000 per ₹1 lakh increase)

---

### 2. Issued Capital

**Definition**: Part of authorized capital actually offered for subscription (issued to shareholders).

**Example**:
- Authorized Capital: ₹10 lakh (1 lakh shares × ₹10)
- Issued Capital: ₹5 lakh (50,000 shares issued to shareholders)
- Unissued: ₹5 lakh (50,000 shares available for future issuance)

**Characteristics**:
- Issued Capital ≤ Authorized Capital
- Company can issue remaining capital later (via rights issue, preferential allotment, public issue)

---

### 3. Subscribed Capital

**Definition**: Part of issued capital that shareholders have agreed to subscribe (buy).

**Example**:
- Issued Capital: ₹5 lakh (50,000 shares offered)
- Subscribed Capital: ₹4 lakh (40,000 shares subscribed by shareholders)
- Unsubscribed: ₹1 lakh (10,000 shares not subscribed)

**Note**: In private placements (most startups), Issued = Subscribed (all offered shares are subscribed).

---

### 4. Paid-Up Capital (Paid-In Capital)

**Definition**: Part of subscribed capital actually paid by shareholders.

**Example**:
- Subscribed Capital: ₹4 lakh (40,000 shares × ₹10)
- **Scenario 1 (Fully Paid)**: Shareholders paid ₹10 per share → Paid-up = ₹4 lakh
- **Scenario 2 (Partly Paid)**: Shareholders paid ₹6 per share → Paid-up = ₹2.4 lakh (unpaid ₹4 per share = calls in arrears)

**Characteristics**:
- Paid-up Capital ≤ Subscribed Capital
- Partly paid shares: Company can make "calls" (demand remaining amount) later
- Shareholder liability = Unpaid amount on shares

---

### 5. Called-Up Capital

**Definition**: Part of subscribed capital that company has demanded (called) from shareholders.

**Example**:
- Subscribed Capital: 10,000 shares × ₹10 = ₹1 lakh
- **Call 1**: Company calls ₹4 per share → Called-up = ₹40,000
- **Call 2**: Company calls ₹3 per share → Called-up = ₹70,000 (cumulative)
- **Uncalled**: ₹3 per share (company hasn't called yet)

---

### 6. Reserve Capital

**Definition**: Uncalled capital that company (via special resolution) reserves to be called only in winding up.

**Purpose**: Creditor protection (assurance that this capital available for creditors if company wound up)

**Example**:
- Subscribed Capital: 10,000 shares × ₹10 = ₹1 lakh
- Paid-up: ₹6 per share (₹60,000)
- Reserve Capital: ₹2 per share (special resolution reserves for winding up)
- Uncalled (can be called anytime): ₹2 per share

**Characteristics**:
- Cannot be called except in winding up
- Irrevocable (once set as reserve capital, cannot be changed)
- Rare in modern practice (used historically for creditor assurance)

---

## Types of Shares

### 1. Equity Shares (Ordinary Shares)

**Definition** (Section 43): Shares with voting rights, entitled to residual profits (after preference dividend).

**Rights**:
✅ Voting rights (1 share = 1 vote)
✅ Dividend rights (declared out of profits, no fixed rate)
✅ Right to participate in residual assets on winding up (after preference shareholders)
✅ Pre-emptive rights (Section 62): Right to subscribe to new shares before outsiders

**Risk-Return**:
- **Risk**: Higher (no fixed dividend, residual claimants in liquidation)
- **Return**: Unlimited upside (share price appreciation + dividends)

**Use Case**: Common for founders, employees (ESOP), growth-oriented investors

---

### 2. Preference Shares (Section 43)

**Definition**: Shares with preferential rights regarding:
1. **Dividend**: Fixed dividend rate (e.g., 8% per annum)
2. **Repayment of Capital**: Priority in winding up (before equity shareholders)

**Types of Preference Shares**:

#### a. Cumulative vs Non-Cumulative

**Cumulative Preference Shares**:
- If dividend not paid in a year (due to insufficient profits), it **accumulates**
- Arrears must be paid before equity dividend declared
- Example: 8% cumulative preference shares, ₹100 face value, 3 years no profit
  - Year 1: ₹8 dividend not paid (arrears ₹8)
  - Year 2: ₹8 dividend not paid (arrears ₹16)
  - Year 3: ₹8 dividend not paid (arrears ₹24)
  - Year 4: Company has profit, must pay ₹32 (₹24 arrears + ₹8 current) to preference shareholders before equity dividend

**Non-Cumulative Preference Shares**:
- If dividend not paid in a year, it **lapses** (no accumulation)
- Only current year dividend payable

---

#### b. Participating vs Non-Participating

**Participating Preference Shares**:
- After receiving fixed dividend (8%), participate in **surplus profits** with equity shareholders
- Example: Company declares ₹100 profit, preference dividend ₹20 (8% of ₹250 preference capital)
  - Remaining ₹80 distributed to preference (25%) + equity (75%) pro rata to shareholding

**Non-Participating Preference Shares** (Most Common):
- Only receive fixed dividend (8%), no participation in surplus

---

#### c. Redeemable vs Irredeemable

**Redeemable Preference Shares** (Section 55):
- Can be redeemed (bought back) by company after specified period
- **Maximum Tenure**: 20 years from date of issue
- **Redemption Sources**: Profits OR fresh issue of shares
- **Example**: Company issues ₹10 lakh redeemable preference shares (10-year tenure)
  - After 10 years, company redeems (buys back) at face value OR premium

**Irredeemable Preference Shares**:
- **Prohibited** u/s 55(1) (cannot issue preference shares without redemption date)
- Exception: Government companies (with Central Government approval)

---

#### d. Convertible vs Non-Convertible

**Convertible Preference Shares**:
- Can be converted into equity shares after specified period
- **CCPS** (Compulsorily Convertible Preference Shares): Auto-converts on specified date/event
- **OCPS** (Optionally Convertible): Shareholder has option to convert OR retain as preference

**Use Case**: PE/VC investments (CCPS gives downside protection via dividend + upside via conversion to equity)

**Example**:
- Investor subscribes 10,000 CCPS at ₹100 per share (₹10 lakh investment)
- 8% dividend per annum for 3 years
- Auto-converts to equity shares at Series A valuation after 3 years

**Non-Convertible Preference Shares**:
- Remain as preference shares, cannot convert to equity

---

### 3. DVR Shares (Differential Voting Rights Shares)

**Definition** (Section 43): Shares with differential rights regarding voting, dividend, or otherwise.

**Types**:
1. **DVR with Lesser Voting Rights** (e.g., 1 share = 0.1 vote OR no voting rights)
2. **DVR with Higher Dividend** (e.g., 15% dividend vs 10% for equity)

**Purpose**: Founder control retention while raising capital
- Founders hold equity (1 share = 1 vote) → Voting control
- Investors hold DVR (1 share = 0.1 vote, but 15% dividend) → Economic return

**Restrictions** (Rule 4 of Companies (Share Capital and Debentures) Rules):
❌ Cannot issue DVR with superior voting rights (only lesser voting OR higher dividend)
❌ DVR cannot exceed 26% of total issued equity capital
❌ Cannot issue DVR if company in default (dividends, annual return, financial statements)

**Example**:
- Founder: 1 million equity shares (1 share = 1 vote) = 1 million votes (66.7% voting)
- Investor: 500,000 DVR shares (1 share = 0.1 vote, 15% dividend) = 50,000 votes (3.3% voting)
- Total: Founder retains 95% voting control despite 66.7% economic ownership

**Landmark Case**: **Tata Motors** issued DVR shares ('A' ordinary shares with 1/10th voting rights but 5% higher dividend)

---

## Share Allotment Procedure

### Private Placement (Section 42)

**Definition**: Offer/invitation to subscribe shares to selected persons (not public, max 200 persons).

**Procedure**:

**Step 1: Board Resolution**
- Board approves share allotment (number of shares, face value, price, allottees)
- Documents: Board resolution, valuation report (if issued at premium to non-residents)

**Step 2: Private Placement Offer Letter** (at least 3 days before allotment)
- Offer letter to proposed allottees with:
  - Company details, business, financials
  - Number of shares offered, price, payment terms
  - Risk factors
  - Application form

**Step 3: Application + Payment**
- Allottees submit application form + payment
- Bank account: Separate designated bank account for private placement (until allotment)

**Step 4: Board Meeting for Allotment**
- Board allots shares (within 60 days of receipt of application money)
- Return unsubscribed money (if shares not allotted within 60 days + 15 days interest @ 12%)

**Step 5: ROC Filing** (within 30 days of allotment)
- **Form PAS-3**: Return of allotment
- Documents: List of allottees, offer letter, board resolution, valuation report (if applicable)

**Step 6: Issue Share Certificates** (within 60 days of allotment)
- Physical certificate OR Demat (electronic form)

---

### Rights Issue (Section 62)

**Definition**: Offer of new shares to **existing shareholders** in proportion to their current shareholding.

**Pre-emptive Rights** (Section 62(1)(a)):
- Existing equity shareholders have first right to subscribe to new shares
- Proportion: Pro rata to existing shareholding
- Example: Shareholder holds 10% equity → Entitled to 10% of new shares issued

**Procedure**:

**Step 1: Board Resolution + Shareholders' Special Resolution**
- Board recommends rights issue
- Shareholders approve via special resolution (75% majority)

**Step 2: Rights Entitlement**
- Determine "record date" (shareholders on record date eligible)
- Calculate entitlement: (Existing shares held / Total shares) × New shares

**Step 3: Rights Offer Letter** (at least 3 days before opening)
- Offer letter with subscription form, payment details, last date
- **Renunciation**: Shareholder can renounce (transfer) rights to others

**Step 4: Subscription Period**
- Minimum: 15 days (cannot be less)
- Shareholders subscribe + pay

**Step 5: Allotment + ROC Filing**
- Board allots shares
- File Form PAS-3 (within 30 days)

---

### Preferential Allotment (Section 62(1)(c))

**Definition**: Issue of shares to selected persons (identified persons) via special resolution.

**Use Case**: Strategic investors, promoters, employees (ESOP exercise)

**Procedure**:
- Special resolution in general meeting (75% majority)
- Price: Cannot be less than fair value (determined by registered valuer)
- Lock-in: 1 year from date of allotment (for non-promoters)
- Filing: Form PAS-3 (within 30 days)

---

### Bonus Shares (Section 63)

**Definition**: Issue of free shares to existing shareholders (capitalization of reserves/profits).

**Example**:
- Company has ₹10 lakh accumulated reserves
- Decides to issue bonus shares (1:1 ratio)
- Existing shareholder holds 100 shares → Receives 100 bonus shares (total 200 shares)
- Capital structure after bonus:
  - Share capital increases by ₹10 lakh
  - Reserves decrease by ₹10 lakh
  - **Net effect**: No change in company's net worth (only reclassification)

**Purpose**:
- Reward shareholders (without cash outflow)
- Improve liquidity (more shares traded)
- Capitalize reserves (convert reserves to share capital)

**Procedure**:
- Board resolution
- AOA permits bonus issue (if not, alter AOA first)
- Issue fully paid-up bonus shares (no payment required from shareholders)
- File Form PAS-3 (within 30 days)

**Restrictions**:
❌ Cannot issue bonus shares if company hasn't paid preference dividend arrears
❌ Cannot issue bonus shares partly paid-up (must be fully paid)

---

## Share Transfer and Transmission

### Share Transfer (Section 56)

**Definition**: Voluntary transfer of shares by shareholder (sale, gift, exchange).

**Procedure**:

**Step 1: Share Transfer Form (SH-4)**
- Transferor (seller) signs SH-4
- Transferee (buyer) receives shares

**Step 2: Stamp Duty**
- Payable by transferor (state-wise: 0.015% - 0.25% of consideration)
- Example: ₹1 lakh share sale, Maharashtra stamp duty 0.25% = ₹250

**Step 3: Submit to Company**
- SH-4 + share certificate (if physical) + stamp duty proof submitted to company

**Step 4: Board Approval** (for private companies with transfer restrictions)
- Board can refuse transfer (if AOA permits)
- Reasons: Non-payment of calls, ROFR (Right of First Refusal) not complied, transferee not approved
- If refused, company must send refusal notice within 30 days

**Step 5: Register Transfer + Issue New Certificate**
- Company registers transfer in Register of Members
- Cancels old certificate, issues new certificate to transferee (within 60 days)

---

### Share Transmission (Section 56)

**Definition**: Involuntary transfer by operation of law (death, insolvency, court order).

**Procedure** (Death of Shareholder):

**Step 1: Nominee/Legal Heir Intimates Company**
- Submit: Death certificate + Succession certificate OR Will + Legal heir certificate

**Step 2: Company Verifies Documents**
- Board meeting for transmission approval (formality, cannot refuse)

**Step 3: Register Transmission + Issue Certificate**
- Register transmission in Register of Members
- Issue share certificate to nominee/legal heir

**Difference from Transfer**:
- Transfer: Voluntary (sale), requires transferor signature, stamp duty
- Transmission: Involuntary (death), no signature needed, no stamp duty

---

## Share Buyback (Section 68)

**Definition**: Company purchases its own shares from shareholders (capital reduction method).

**Purpose**:
- Return excess capital to shareholders
- Increase promoter holding % (by reducing total shares)
- Improve financial ratios (EPS, ROE increase)
- Support share price (demand created by buyback)

**Landmark Case: Trevor v. Whitworth (1887)**
**Facts**: Company bought back its own shares and resold them.
**Held**: Buyback violates capital maintenance doctrine. Company cannot traffic in its own shares (creditor protection requires capital to remain intact).
**Principle**: Buyback allowed ONLY if done from:
1. Free reserves, OR
2. Securities premium account, OR
3. Proceeds of fresh issue (for buying back existing shares)

---

### Buyback Restrictions (Section 68)

**Maximum Buyback Limit**:
- **25% of paid-up capital + free reserves** in a financial year
- Example: Paid-up capital ₹10 lakh + Free reserves ₹5 lakh = ₹15 lakh
  - Max buyback = 25% × ₹15 lakh = ₹3.75 lakh in a year

**Debt-Equity Ratio**:
- After buyback, debt-equity ratio must not exceed 2:1
- Example: If debt ₹20 lakh, equity (after buyback) must be ≥₹10 lakh

**Source of Funds**:
✅ Free reserves (not tied up)
✅ Securities premium account
✅ Proceeds of fresh issue (for buying back existing shares, e.g., issue equity to buy back preference shares)

❌ Proceeds of earlier buyback
❌ Proceeds of issue of preference shares/debentures

**Timing**:
- Cannot buyback within 1 year of previous buyback
- Exception: Buyback of preference shares per terms of issue

---

### Buyback Procedure

**Step 1: Board Resolution**
- Board recommends buyback (number of shares, price, source of funds)

**Step 2: Shareholders' Special Resolution**
- 75% majority approval in general meeting
- Explanatory statement: Purpose, price, source, impact on capital

**Step 3: File e-Form SH-8** (within 7 days of special resolution)
- Declaration of solvency (company can pay debts after buyback)

**Step 4: Public Announcement** (if listed company)
- Newspaper advertisement, stock exchange filing
- Offer period: Minimum 15 days

**Step 5: Buyback Execution**
- Pay shareholders for shares tendered
- Transfer buyback amount to Capital Redemption Reserve (CRR)

**Step 6: Extinguish Shares** (within 7 days of buyback completion)
- Physical certificates destroyed
- Demat shares extinguished
- File Form SH-11 with ROC

---

## Capital Reduction (Section 66)

**Definition**: Reduction of share capital (authorized/issued/paid-up capital).

**Methods**:
1. **Cancel Unpaid Capital**: Cancel calls in arrears (partly paid shares become fully paid at reduced value)
2. **Cancel Paid-Up Capital**: Return capital to shareholders (exceeds requirement)
3. **Write Off Lost Capital**: Adjust share capital to reflect losses (balance sheet cleanup)

**Example** (Write Off Losses):
- Company: Paid-up capital ₹10 lakh, accumulated losses ₹6 lakh → Net worth ₹4 lakh
- Capital reduction: Reduce paid-up capital by ₹6 lakh (write off losses)
- Result: Paid-up capital ₹4 lakh, losses NIL → Net worth ₹4 lakh (cleaner balance sheet)

---

### Capital Reduction Procedure (Section 66)

**Step 1: Board Resolution**
- Board recommends capital reduction

**Step 2: Shareholders' Special Resolution**
- 75% majority approval
- Explanatory statement: Method, amount, reasons

**Step 3: File Application with NCLT** (National Company Law Tribunal)
- Form: NCLT application (Misc. Application)
- Documents: Board resolution, special resolution, scheme of reduction, list of creditors

**Step 4: NCLT Notice to Creditors**
- NCLT orders notice to creditors (if reduction involves capital return to shareholders)
- Creditors can object (if debts unpaid)

**Step 5: NCLT Hearing + Order**
- NCLT ensures:
  - Creditors not prejudiced
  - Reduction fair and equitable to shareholders
  - Company solvent after reduction
- NCLT passes order sanctioning reduction

**Step 6: File NCLT Order with ROC** (within 30 days)
- Form INC-28 (order certified copy)
- Reduction effective from NCLT order date

**Timeline**: 6-12 months (NCLT process)

---

## Forfeiture and Surrender of Shares

### Forfeiture (Section 56)

**Definition**: Company forfeits shares due to non-payment of calls (shareholder didn't pay call money).

**Procedure**:
- AOA must permit forfeiture
- Company serves notice to shareholder (14 days to pay call + interest)
- If not paid, board passes resolution forfeiting shares
- Forfeited shares become property of company (can be reissued at discount)

**Example**:
- Shareholder holds 100 shares, face value ₹10, paid ₹6, call ₹4 pending
- Shareholder doesn't pay ₹4 call despite notice
- Company forfeits 100 shares
- Forfeited shares reissued at ₹8 (₹2 discount, max discount = ₹4 originally unpaid)

---

### Surrender

**Definition**: Shareholder voluntarily returns shares to company (to avoid forfeiture).

**Conditions**:
- Surrender accepted only if shares liable to forfeiture (call unpaid)
- Company can accept surrender instead of forfeiture (less adversarial)

---

## Conclusion

Share capital structure is foundational to corporate finance. Key principles:

1. ✅ **Capital Maintenance**: Company cannot return capital to shareholders except via legal procedures (buyback, reduction, dividends from profits)
2. ✅ **Pre-emptive Rights**: Existing shareholders have first right to subscribe to new shares (Section 62)
3. ✅ **Types**: Equity (voting, variable dividend) vs Preference (fixed dividend, priority) vs DVR (differential voting/dividend)
4. ✅ **Buyback Limits**: Max 25% of paid-up capital + free reserves per year, debt-equity ≤2:1 after buyback
5. ✅ **Capital Reduction**: Requires NCLT approval (creditor protection)

**Strategic Considerations**:
- **Startups**: Equity for founders/employees, CCPS for investors (downside protection + upside participation)
- **Mature Companies**: Buyback for capital return (vs dividend, more tax-efficient), bonus shares for liquidity
- **Founder Control**: DVR shares (investors get economic return, founders retain voting control)

---

**Next Protocols to Consult**:
- **IL-CORP-SHAREHOLDERS-RIGHTS**: Voting rights, dividends, oppression/mismanagement
- **IL-CORP-SHAREHOLDER-AGREEMENTS**: SHA clauses for investor protection
- **IL-CORP-EQUITY-FINANCING**: Fundraising rounds, term sheets, valuation
- **IL-CORP-PRIVATE-EQUITY-VC**: PE/VC investment structures, CCPS, exit mechanisms

---

**Legal Disclaimer**: This protocol provides informational guidance on share capital in India. It is NOT legal advice. For specific capital structuring, share allotment, or buyback, engage a qualified Chartered Accountant or Company Secretary. Legal validity depends on compliance with Companies Act 2013, SEBI regulations, and NCLT procedures.

---

**End of Protocol: IL-CORP-SHARE-CAPITAL**
