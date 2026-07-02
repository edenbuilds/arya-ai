---
id: IL-CORP-DEMERGER-SCHEMES
version: 1.0.0
category: corporate_law
subcategory: mergers_restructuring
sections:
  - Demerger Overview
  - Types of Demergers
  - NCLT Demerger Process
  - Valuation and Share Allocation
  - Tax-Neutral Demerger
  - Accounting Treatment
  - Regulatory Approvals
  - Post-Demerger Integration
  - Strategic Considerations
  - Best Practices
dependencies:
  - IL-CORP-MERGER-PROCESS-NCLT (NCLT scheme process, shareholder approvals)
  - IL-CORP-SHAREHOLDERS-RIGHTS (Shareholder voting, dissenting rights)
  - IL-CORP-SHARE-CAPITAL (Share issuance in resulting company)
related_protocols:
  foundation:
    - IL-COMPANIES-ACT (Companies Act 2013, Sections 230-232)
    - IL-CORP-BOARD-MEETINGS (Board approval for demerger scheme)
  procedural:
    - IL-CORP-SLUMP-SALE (Alternative to demerger, asset sale)
landmark_cases:
  - Bombay Dyeing v. State of Bombay AIR 1958 SC 328 (Division of assets in demerger)
  - Sterlite Industries v. SEBI (2013) (Mirror principle in demerger share allocation)
---

# DEMERGER SCHEMES - INDIAN CORPORATE LAW

## OVERVIEW

A demerger (or de-merger, spin-off) is a corporate restructuring where a company splits into two or more entities by transferring one or more undertakings to a separate company. The demerged company (transferor) transfers a business division/undertaking to the resulting company (transferee/new company), and shareholders of the demerged company receive shares in the resulting company in proportion to their existing shareholding (mirror principle).

**DEMERGER vs MERGER**:

| Parameter | Demerger | Merger |
|---|---|---|
| **Direction** | Company splits (1 → 2+) | Companies combine (2+ → 1) |
| **Purpose** | Unlock value, focus on core business | Synergies, economies of scale |
| **Transferor** | Continues to exist (retains remaining business) | Ceases to exist (dissolved) |
| **Consideration** | Shares issued by resulting company to demerged company shareholders | Shares issued by transferee to transferor shareholders |
| **Example** | Reliance Industries demerges Financial Services → Reliance Capital | HDFC Ltd merges into HDFC Bank |

**LEGAL DEFINITION (Section 2(19AA))**:
```
"Demerger" means transfer of one or more undertakings by demerged company to resulting company such that:
(a) ALL assets and liabilities of undertaking transferred
(b) Resulting company issues shares to shareholders of demerged company (on proportionate basis)
(c) Shareholders holding ≥75% shares in demerged undertaking become shareholders in resulting company
(d) Transfer is on "going concern" basis (business continues uninterrupted)
(e) Demerger is in accordance with Section 230-232 (scheme of arrangement)
```

**LEGAL FRAMEWORK**:
- **Companies Act 2013**: Sections 230-232 (Scheme of Arrangement), Section 2(19AA) (Definition)
- **Income Tax Act 1961**: Section 2(19AA) (Tax-neutral demerger conditions)
- **SEBI (LODR) Regulations 2015**: Listed company demerger disclosures, mirror principle
- **Competition Act 2002**: CCI approval (if thresholds crossed)

---

## 1. TYPES OF DEMERGERS

### 1.1 Full Demerger vs Partial Demerger

**Full Demerger (Complete Spin-Off)**:
```
Structure: Demerged company transfers entire business to resulting company, then liquidates
Result: Demerged company ceases to exist (like merger, but split not combine)
Rare in India (most demergers are partial)
```

**Partial Demerger (Standard)**:
```
Structure: Demerged company transfers one/some undertakings, retains core business
Result: Both demerged and resulting companies continue (2 listed companies post-demerger if demerged listed)
Example: Reliance Industries demerged Financial Services (resulting = Reliance Capital), retained Petrochemicals/Refining
```

### 1.2 Vertical vs Horizontal Demerger

**Vertical Demerger**:
```
Separate different stages of value chain
Example: Manufacturing + Retail → Manufacturing Co + Retail Co (separate upstream and downstream)
```

**Horizontal Demerger**:
```
Separate similar businesses/product lines
Example: Pharma (APIs + Formulations) → API Co + Formulations Co (separate product lines)
```

### 1.3 Equity Carve-Out vs Pure Spin-Off

**Equity Carve-Out (IPO of Subsidiary)**:
```
Structure: Resulting company lists via IPO, public owns minority, demerged company retains majority
Example: Reliance Retail IPO (Reliance Industries retains 70%, public 30%)
Not technically demerger (Reliance remains shareholder, shareholders don't receive shares directly)
```

**Pure Spin-Off (Demerger)**:
```
Structure: Resulting company shares distributed to demerged company shareholders (mirror principle)
Example: ITC demerges Hotels business → ITC shareholders receive ITC Hotels shares pro-rata
ITC shareholding: 0% in ITC Hotels (shareholders own both ITC + ITC Hotels separately)
```

**Example - Partial Demerger Structure**:
```
Before Demerger:
Company A (Conglomerate):
- Business 1: FMCG (₹500 cr revenue, ₹100 cr EBITDA)
- Business 2: Hotels (₹300 cr revenue, ₹50 cr EBITDA)
- Business 3: IT Services (₹200 cr revenue, ₹40 cr EBITDA)

Demerger:
- Hotels + IT Services transferred to Resulting Co (New Co)
- FMCG retained by Company A (Demerged Co)

After Demerger:
Company A (Demerged): FMCG only (₹500 cr revenue, ₹100 cr EBITDA)
New Co (Resulting): Hotels + IT Services (₹500 cr revenue, ₹90 cr EBITDA)

Shareholders: Own both A + New Co shares (proportionately)
```

---

## 2. NCLT DEMERGER PROCESS (Sections 230-232)

### 2.1 Pre-Scheme Preparation

**Step 1: Identify Undertaking**:
```
"Undertaking" = Business division capable of operating independently (Section 2(19AA))
Must have:
- Identifiable assets (plant, machinery, inventory, receivables)
- Identifiable liabilities (loans, payables specific to undertaking)
- Separate operations (distinct products/services/customers)
- Going concern (viable standalone business)

Example:
Company A: FMCG + Hotels
Undertaking (Hotels): Separate hotels, staff, brand, customers, suppliers, loans (identified) → Valid undertaking ✓

Not Undertaking: Corporate treasury function (not independent business, supports other divisions) → Invalid ✗
```

**Step 2: Valuation**:
```
Registered valuer prepares valuation of:
(a) Demerged Company (pre-demerger consolidated value)
(b) Demerged Undertaking (value of business being transferred)
(c) Resulting Company (value of undertaking on standalone basis)

Methods: DCF, NAV, Market Multiples
```

**Step 3: Share Allocation Ratio**:
```
Mirror Principle (SEBI): Resulting company shares issued to demerged company shareholders in SAME PROPORTION as demerged company shareholding

Formula: Shareholding % in Resulting Company = Shareholding % in Demerged Company (exactly mirrors)

Example:
Shareholder A: Owns 25% of Demerged Company
Post-Demerger: A owns 25% of Resulting Company (mirror shareholding)
```

**Step 4: Scheme Drafting**:
```
Demerger Scheme includes:
- Undertaking description (assets, liabilities, employees, contracts)
- Appointed Date (date from which undertaking deemed transferred, retrospective accounting)
- Effective Date (date NCLT order becomes operative)
- Share allocation (resulting company shares to demerged shareholders, exchange ratio)
- Employees (transfer on existing terms, continuity of service)
- Contracts (assignment to resulting company, consent from counterparties if required)
- Liabilities (specified liabilities transferred, demerged company indemnifies if any missed)
```

### 2.2 NCLT Process (Same as Merger, 270-365 days)

**Process identical to merger** (see IL-CORP-MERGER-PROCESS-NCLT):
1. Board approval (demerged + resulting companies)
2. NCLT application (Form NCLT-1)
3. NCLT directions (convene shareholder/creditor meetings)
4. Meetings (75% in value + 50% in number approval)
5. Regulatory approvals (ROC, IT, SEBI, Stock Exchanges, CCI)
6. Final NCLT hearing (scheme sanction)
7. ROC filing (Form INC-28)
8. Implementation (shares issued, assets/liabilities transferred)

**Key Difference**: Resulting company may be newly incorporated (vs merger where transferee already exists).

**Example - Timeline**:
```
Day 0: Board approves demerger scheme
Day 30: Incorporate Resulting Co (new company, if not existing)
Day 60: NCLT application filed (demerged company jurisdiction)
Day 90: NCLT first hearing (directions for meetings)
Day 150: Shareholder/creditor meetings (75% approval achieved)
Day 240: Regulatory approvals obtained (ROC, IT, SEBI, Stock Exchange)
Day 300: NCLT final hearing (scheme sanctioned, effective date specified)
Day 330: Implementation (resulting company shares issued to demerged shareholders, assets/liabilities transferred)
```

---

## 3. MIRROR PRINCIPLE (SEBI)

### 3.1 Proportionate Share Allocation

**SEBI Requirement (Sterlite Industries case)**: Resulting company shares must be issued to demerged company shareholders in EXACT SAME PROPORTION as their shareholding in demerged company.

**Rationale**: Prevent wealth transfer between shareholders (if disproportionate, some shareholders gain, others lose).

**Formula**:
```
Shareholding % in Resulting Co = Shareholding % in Demerged Co

OR

Shares received in Resulting Co ÷ Total Resulting Co shares = Shares held in Demerged Co ÷ Total Demerged Co shares
```

**Example - Mirror Principle Application**:
```
Demerged Company A (10 crore shares):
- Promoter: 6 crore shares (60%)
- PE Investor: 2 crore shares (20%)
- Public: 2 crore shares (20%)

Demerger: Hotels division transferred to Resulting Company B
Resulting Company B issues: 5 crore shares

Mirror Allocation:
- Promoter: 60% × 5 crore = 3 crore B shares (owns 60% of B)
- PE Investor: 20% × 5 crore = 1 crore B shares (owns 20% of B)
- Public: 20% × 5 crore = 1 crore B shares (owns 20% of B)

Check: Each shareholder's % ownership in B = % ownership in A (mirror maintained ✓)

Post-Demerger Holdings:
- Promoter: 6 crore A shares (60% of A) + 3 crore B shares (60% of B)
- PE Investor: 2 crore A shares (20% of A) + 1 crore B shares (20% of B)
- Public: 2 crore A shares (20% of A) + 1 crore B shares (20% of B)
```

### 3.2 Violations and Consequences

**Non-Proportionate Allocation = Violation**:
```
Example (Violation):
Demerger Company: Promoter 60%, Public 40%
Resulting Company (incorrect): Promoter 70%, Public 30%

Issue: Promoter receives disproportionately more shares (wealth transfer from public to promoter)

SEBI Action:
- Reject scheme (scheme approval withheld)
- Require rectification (adjust allocation to 60:40 mirror)
```

**Exceptions (Rare)**:
- ESOP shares in resulting company (not mirror, allocated to employees)
- Preferential issue in resulting company (new investor subscribes, dilutes mirror slightly - requires separate shareholder approval)

---

## 4. VALUATION AND SHARE EXCHANGE RATIO

### 4.1 Valuation Methodology

**Demerged Company Valuation (Pre-Demerger)**:
```
Sum-of-Parts Valuation:
Business 1 (retained): ₹1,000 crore (DCF valuation)
Business 2 (demerged): ₹500 crore (DCF valuation)
Corporate costs: (₹50 crore) (allocated to retained business)
Total: ₹1,450 crore

Per Share Value: ₹1,450 cr ÷ 10 cr shares = ₹145/share
```

**Post-Demerger Valuation**:
```
Demerged Company (retained business): ₹950 crore (₹1,000 cr - ₹50 cr corporate costs)
Resulting Company (demerged business): ₹500 crore

Check: ₹950 cr + ₹500 cr = ₹1,450 crore (pre-demerger value preserved ✓)
```

**Share Allocation**:
```
Resulting Company: Issues 2 crore shares (decided by scheme)
Per Share Value: ₹500 cr ÷ 2 cr = ₹250/share

Shareholder A (owns 1 crore shares in Demerged Company = 10%):
Receives: 10% × 2 cr = 20 lakh Resulting Company shares

Shareholder A Pre-Demerger Wealth:
1 cr shares × ₹145/share = ₹145 crore

Shareholder A Post-Demerger Wealth:
Demerged Co: 1 cr shares × ₹95/share = ₹95 crore (₹950 cr ÷ 10 cr shares)
Resulting Co: 20 lakh shares × ₹250/share = ₹50 crore
Total: ₹95 cr + ₹50 cr = ₹145 crore (wealth preserved ✓)
```

### 4.2 Dissenting Shareholders

**Same as Merger**: Shareholders who vote against scheme can object at NCLT final hearing.

**Common Objections**:
- Undervaluation of demerged undertaking (shareholders lose value)
- Inappropriate allocation of corporate costs/debts (demerged undertaking burdened with excessive liabilities)
- Non-mirror allocation (some shareholders receive disproportionate shares)

**NCLT Powers**: Modify scheme (adjust valuation, share allocation, cost/debt allocation) or reject scheme.

---

## 5. TAX-NEUTRAL DEMERGER (Section 2(19AA), Income Tax Act)

### 5.1 Conditions for Tax Neutrality

**Section 2(19AA) Definition** (Tax-neutral demerger conditions):
```
1. Transfer of undertaking on "going concern" basis (business continues uninterrupted)
2. ALL assets and liabilities of undertaking transferred (cannot cherry-pick)
3. Resulting company issues shares worth ≥75% of net worth of demerged undertaking
4. Shareholders holding ≥75% of demerged company shares become shareholders of resulting company
5. No consideration other than shares (no cash payment to demerged company or its shareholders)
6. Demerger pursuant to court-approved scheme (NCLT/NCLT approval)
```

**If Conditions Met**:
- **Demerged Company**: No capital gains tax on undertaking transfer (Section 47(vib))
- **Resulting Company**: Inherits tax attributes of demerged undertaking (carry-forward losses, MAT credit - proportionate) (Section 72A(5))
- **Shareholders**: No capital gains tax on share receipt (Section 47(vii))
  - Cost of acquisition split: Original cost allocated between demerged shares (retained) and resulting shares (received) based on Net Asset Value ratio

**Example - Tax-Neutral Demerger**:
```
Demerged Company A:
- Undertaking (Hotels): Assets ₹800 cr (book value), ₹1,200 cr (fair value)
- Capital gain if sold: ₹400 cr (taxable @ 25% = ₹100 cr tax)

Tax-Neutral Demerger:
- Hotels transferred to Resulting Company B (Section 2(19AA) conditions satisfied)
- Section 47(vib): Transfer exempt from capital gains tax (₹0 tax vs ₹100 cr if sold)
- Section 72A(5): B inherits A's carry-forward losses (proportionate, e.g., ₹200 cr losses allocated to hotels undertaking)

Shareholder X:
- Original Cost: 1 lakh A shares @ ₹50/share = ₹50 lakh
- Receives: 10,000 B shares (mirror allocation)

Cost Allocation (NAV method):
- A NAV post-demerger: ₹80/share (retained business)
- B NAV: ₹120/share (demerged undertaking)
- Ratio: 80:120 = 40:60

Cost Allocation:
- A shares (retained): ₹50 lakh × 40% = ₹20 lakh (₹20 cost per A share)
- B shares (received): ₹50 lakh × 60% = ₹30 lakh (₹300 cost per B share)

Future Sale of B shares @ ₹500/share:
Capital Gain: (₹500 - ₹300) × 10,000 = ₹20 lakh (taxable when sold, not at demerger)
```

### 5.2 Non-Tax-Neutral Demerger

**If Section 2(19AA) conditions NOT met** (e.g., cash consideration paid, <75% shareholding continuity):
- Demerged company: Capital gains tax on undertaking transfer (fair value - book value taxable)
- Shareholders: Tax on share receipt (value of shares received taxable as dividend)

**Example - Non-Tax-Neutral**:
```
Demerger with Cash Component:
- Hotels undertaking transferred to Resulting Co (₹500 cr fair value)
- Resulting Co issues: ₹300 cr shares + ₹200 cr cash to Demerged Co

Issue: Cash consideration paid → Violates Section 2(19AA) condition (no consideration other than shares)

Tax Consequences:
- Demerged Co: Capital gains tax on ₹500 cr (fair value) - ₹300 cr (book value) = ₹200 cr gain (₹50 cr tax @ 25%)
- Shareholders: ₹200 cr cash distributed treated as dividend (taxed in hands of Demerged Co @ 30%+ as dividend distribution tax)
```

---

## 6. ACCOUNTING TREATMENT (Ind AS)

### 6.1 Demerged Company Accounting

**At Appointed Date** (retrospective accounting):
```
Journal Entry (Demerged Company A):
Dr. Resulting Company B (Investment) ₹500 cr (value of undertaking transferred)
Cr. Net Assets (Undertaking) ₹500 cr (eliminate assets/liabilities transferred)

Post-Demerger:
- A retains investment in B: ₹500 cr (shown as investment if A holds B shares)
- OR
- A distributes B shares to shareholders: Eliminate investment, reduce reserves ₹500 cr (if mirror distribution)
```

**Example**:
```
Demerged Company A (Pre-Demerger Balance Sheet):
Assets: ₹1,500 cr (FMCG ₹1,000 cr + Hotels ₹500 cr)
Liabilities: ₹600 cr (FMCG ₹400 cr + Hotels ₹200 cr)
Net Assets: ₹900 cr
Equity: ₹900 cr (10 cr shares @ ₹90/share)

Demerger (Hotels transferred to Resulting Company B):
Assets transferred: ₹500 cr
Liabilities transferred: ₹200 cr
Net Assets transferred: ₹300 cr

Journal Entry:
Dr. Investment in B ₹300 cr
Dr. Liabilities (Hotels) ₹200 cr
Cr. Assets (Hotels) ₹500 cr

A's Balance Sheet Post-Demerger:
Assets: ₹1,000 cr (FMCG retained) + ₹300 cr (investment in B) = ₹1,300 cr
Liabilities: ₹400 cr (FMCG)
Net Assets: ₹900 cr (unchanged)
Equity: ₹900 cr

OR (if B shares distributed to shareholders immediately):
Dr. Reserves ₹300 cr
Cr. Investment in B ₹300 cr
(A's equity reduces to ₹600 cr, shareholders now own A + B separately)
```

### 6.2 Resulting Company Accounting

**At Incorporation**:
```
Resulting Company B receives:
- Assets: ₹500 cr (at book value from A)
- Liabilities: ₹200 cr (from A)
- Net Assets: ₹300 cr

B issues shares: 2 cr shares (₹10 face value = ₹20 cr, balance ₹280 cr to reserves)

B's Balance Sheet (Day 1):
Assets: ₹500 cr
Liabilities: ₹200 cr
Share Capital: ₹20 cr (2 cr shares @ ₹10 face value)
Reserves: ₹280 cr
Total Equity: ₹300 cr
```

---

## 7. REGULATORY APPROVALS

### 7.1 SEBI and Stock Exchange Approvals (Listed Companies)

**SEBI Observation Letter**:
- SEBI reviews: Mirror principle compliance, valuation fairness, disclosure adequacy
- SEBI may require: Independent valuation, fairness opinion by merchant banker, enhanced disclosures

**Stock Exchange In-Principle Approval**:
- Resulting company listing: If demerged company listed, resulting company also lists (automatic listing)
- Listing requirements: Minimum public shareholding (25%), market capitalization (₹500 cr for main board)

**Example**:
```
Demerged Company: Listed on NSE (market cap ₹5,000 cr, promoter 55%, public 45%)
Resulting Company: Hotels division (estimated market cap ₹2,000 cr)

Listing Compliance:
- Public shareholding: 45% (mirrors demerged company, ≥25% required ✓)
- Market cap: ₹2,000 cr (≥₹500 cr main board requirement ✓)
- Result: Resulting company eligible for NSE main board listing ✓

Stock Exchange In-Principle Approval:
- NSE grants approval (subject to scheme sanction by NCLT)
- Trading begins: Post-NCLT order + ROC filing (typically 30 days after NCLT)
```

### 7.2 CCI Approval (Competition Commission)

**Same thresholds as merger** (see IL-CORP-MERGER-PROCESS-NCLT):
- Combined assets >₹2,000 cr OR Combined turnover >₹6,000 cr
- OR Target assets >₹750 cr OR Target turnover >₹2,250 cr

**Demerger Specific**: Usually NO CCI approval required (demerger splits business, reduces market concentration, unlikely to create competition concerns).

**Exception**: If demerger creates dominant player (e.g., all hotel assets consolidated into one resulting company while competitors remain fragmented).

---

## 8. POST-DEMERGER INTEGRATION

### 8.1 Operational Separation

**Day 1-30 (Transition Services Agreement)**:
```
Issue: Resulting company may depend on demerged company for shared services (IT, HR, Finance, Legal)
Solution: Transition Services Agreement (TSA) - Demerged company provides services for 6-12 months (fee-based)

Example:
Hotels demerged from FMCG conglomerate
TSA: FMCG provides IT support, payroll processing, legal services to Hotels for 12 months (₹2 cr/month fee)
Timeline: Hotels builds standalone IT/HR/Legal within 12 months, then TSA terminates
```

**Day 1-100 (Operational Independence)**:
- **Employees**: Transfer employment contracts (hotels staff to Resulting Co), continuity of service
- **Contracts**: Assign customer/supplier contracts (consent required if contracts have non-assignment clauses)
- **Licenses**: Transfer regulatory licenses (hotel licenses, trade licenses, GST registration)
- **IP**: Assign trademarks, brands (hotels brand to Resulting Co)
- **Real Estate**: Transfer property titles (hotel properties to Resulting Co)
- **IT Systems**: Separate ERP, email, intranet (build standalone or subscribe to new systems)

### 8.2 Listing and Trading

**Resulting Company Listing** (if demerged listed):
```
Timeline:
- NCLT order: Day 300
- ROC filing: Day 310
- Shares credited to shareholders: Day 320 (demat account, ISIN allotted)
- Trading begins: Day 330 (NSE/BSE trading commences)

Shareholder Impact:
- Pre-demerger: Owns 1 lakh A shares (worth ₹145 lakh at ₹145/share)
- Post-demerger: Owns 1 lakh A shares (₹95/share) + 10,000 B shares (₹250/share)
- Total value: ₹95 lakh + ₹25 lakh = ₹120 lakh (Day 1 trading may be volatile, ₹145 lakh pre-demerger value not guaranteed)

Lock-in: No lock-in for public shareholders (freely tradable from Day 1)
Promoter lock-in: If promoter holding increases post-demerger (due to rounding), excess locked in for 1 year
```

---

## 9. STRATEGIC RATIONALE FOR DEMERGERS

### 9.1 Unlock Conglomerate Discount

**Conglomerate Discount**: Diversified companies trade at discount vs sum-of-parts (market difficulty valuing unrelated businesses).

**Example**:
```
Conglomerate A (FMCG + Hotels):
- FMCG value (standalone): ₹1,000 cr (10x EBITDA)
- Hotels value (standalone): ₹500 cr (10x EBITDA)
- Sum-of-parts: ₹1,500 cr
- Actual market cap (conglomerate): ₹1,200 cr (20% discount)

Demerger:
- FMCG Co: ₹1,000 cr (post-demerger market cap, pure-play FMCG valued at 10x)
- Hotels Co: ₹500 cr (post-demerger market cap, pure-play hotels valued at 10x)
- Total value: ₹1,500 cr (conglomerate discount eliminated, 25% value creation)

Shareholder Benefit: ₹1,500 cr ÷ 10 cr shares = ₹150/share (vs ₹120/share pre-demerger, 25% gain)
```

### 9.2 Management Focus

**Issue**: Conglomerate management distracted by unrelated businesses (FMCG CEO managing hotels, suboptimal).

**Solution**: Demerger creates focused management teams (FMCG CEO focuses on FMCG, Hotels CEO focuses on hotels).

**Result**: Better operational performance (focused strategy, specialized expertise, faster decision-making).

### 9.3 Fundraising and M&A

**Separate Capital Allocation**:
- Hotels (capital-intensive): Raises debt for hotel acquisitions (optimal leverage for hotels)
- FMCG (working capital-intensive): Raises equity for brand expansion (optimal leverage for FMCG)
- Pre-demerger: Single balance sheet, suboptimal leverage for both (FMCG wants less debt, hotels want more debt)

**M&A Flexibility**:
- Resulting company can be sold separately (strategic buyer interested in hotels, not FMCG)
- Pre-demerger: Must sell entire conglomerate (fewer buyers, lower valuation)

---

## 10. BEST PRACTICES

### 10.1 Undertaking Definition

**Clear Boundaries**: Define undertaking with precision (assets, liabilities, employees, contracts listed in schedule).

**Avoid Disputes**:
- Shared assets: Allocate clearly (office building shared → allocate floors, or sell and distribute proceeds)
- Shared contracts: Assign or duplicate (group insurance policy → separate policies for each entity)
- Corporate costs: Allocate based on usage (IT costs → allocate based on employee count)

**Example - Shared Asset Allocation**:
```
Head Office Building: 10 floors (₹100 cr value)
- FMCG uses 7 floors
- Hotels uses 3 floors

Option 1 (Physical Division):
- FMCG retains 7 floors (₹70 cr value)
- Hotels gets 3 floors (₹30 cr value transferred to Resulting Co)

Option 2 (Sell and Distribute):
- Sell building for ₹100 cr
- FMCG gets ₹70 cr (buys new office)
- Hotels gets ₹30 cr (buys new office)
- Clean separation, no shared asset post-demerger
```

### 10.2 Employee Communication

**Uncertainty**: Employees uncertain about employment continuity, compensation, career prospects post-demerger.

**Communication Plan**:
- Announce demerger rationale (strategic focus, unlock value, growth prospects)
- Employee town halls (Q&A with leadership, address concerns)
- One-on-one meetings (affected employees, discuss transfer, role, compensation)
- Retention bonuses (key employees, prevent attrition during uncertainty)

**Continuity of Service**: Section 230-232 schemes preserve employee rights (service continuity, PF, gratuity).

---

## STRATEGIC CONSIDERATIONS

### When to Choose Demerger vs Asset Sale (Slump Sale)

**Choose Demerger When**:
- Tax-neutral treatment required (preserve tax attributes, avoid capital gains tax)
- Shareholders want to own both businesses (participate in upside of both entities)
- Resulting company needs listing (automatic listing if demerged company listed)
- Long-term strategic separation (both businesses continue independently)

**Choose Asset Sale (Slump Sale) When**:
- Speed critical (2-4 months vs 9-12 months for demerger)
- Buyer wants 100% ownership (demerger = distributed to shareholders, buyer must make separate offer)
- Tax-neutral not required (can absorb capital gains tax)
- Demerged company wants cash (asset sale = cash proceeds, demerger = no cash to company)

---

## COMPLIANCE CHECKLIST

**Pre-Application**:
- [ ] Board approval (demerged company, resulting company if existing)
- [ ] Incorporate resulting company (if new entity, capital ₹5 lakh typical)
- [ ] Due diligence (undertaking identification, asset/liability listing)
- [ ] Valuation (registered valuer, demerged company + undertaking + resulting company)
- [ ] Draft scheme (comprehensive, mirror principle, appointed date, effective date)

**NCLT Application**:
- [ ] File Form NCLT-1 (demerged company jurisdiction)
- [ ] Attach scheme, board resolutions, valuation, financials (3 years), shareholder/creditor lists
- [ ] Pay NCLT fees (₹5-10 lakh)
- [ ] First hearing (NCLT directions for meetings)

**Meetings**:
- [ ] Convene shareholder meeting (demerged company, 21-day notice, 75% in value + 50% in number)
- [ ] Convene creditor meeting (demerged company, same threshold)
- [ ] File meeting results (Form CA-4 within 7 days)

**Regulatory Approvals**:
- [ ] ROC no-objection (demerged + resulting companies)
- [ ] Income Tax clearance (Section 2(19AA) tax-neutral conditions verified)
- [ ] SEBI observation letter (if listed, mirror principle compliance)
- [ ] Stock exchange in-principle approval (resulting company listing)
- [ ] CCI approval (if thresholds crossed, rare for demergers)

**Final NCLT Hearing**:
- [ ] File regulatory approvals with NCLT
- [ ] Respond to objections (dissenting shareholders)
- [ ] NCLT passes order (scheme sanctioned, effective date)

**Implementation**:
- [ ] ROC filing (Form INC-28, both companies)
- [ ] Issue shares (resulting company shares to demerged shareholders, mirror allocation)
- [ ] Transfer assets/liabilities (deed of conveyance, assignment)
- [ ] Transfer employees (employment contracts, PF transfer, service continuity)
- [ ] Update licenses, contracts (resulting company replaces demerged company)
- [ ] List resulting company (if demerged listed, trading begins)

---

## LEGAL DISCLAIMER

This protocol provides information on demerger schemes under Indian law. It is for informational purposes only and does not constitute legal, financial, tax, or investment advice. Companies should consult qualified corporate lawyers, chartered accountants, company secretaries, registered valuers, and merchant bankers for demerger transactions. NCLT procedures, tax treatment, SEBI regulations, and listing requirements are subject to change. Demerger timelines and costs vary based on transaction complexity.

---

**Last Updated**: December 5, 2025
**Version**: 1.0.0
**Protocol ID**: IL-CORP-DEMERGER-SCHEMES
