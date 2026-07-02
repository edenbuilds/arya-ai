# IL-CORP-SHAREHOLDER-AGREEMENTS
## Shareholder Agreements (SHA) for Investor Protection

---
id: IL-CORP-SHAREHOLDER-AGREEMENTS
version: 1.0.0
category: corporate_law
subcategory: company_formation
sections:
  - SHA vs AOA Distinction
  - Key SHA Clauses
  - Pre-emptive Rights and ROFR
  - Tag-Along and Drag-Along Rights
  - Anti-Dilution Protection
  - Exit Rights and Liquidity
  - Governance and Control Provisions
  - Dispute Resolution
dependencies:
  - IL-CORP-MOA-AOA (AOA vs SHA relationship)
  - IL-CORP-SHAREHOLDERS-RIGHTS (Statutory shareholder rights)
  - IL-CORP-SHARE-CAPITAL (Share types and transfers)
related_protocols:
  foundation:
    - IL-CORP-EQUITY-FINANCING (Fundraising and term sheets)
    - IL-CORP-PRIVATE-EQUITY-VC (PE/VC investment structures)
  procedural:
    - IL-CONTRACT-LAW (Contract enforceability, breach remedies)
landmark_cases:
  - Vodafone v. Union of India AIR 2012 SC 1179 (SHA validity, taxation)
  - Ruchi Soya Industries v. ICICI Bank AIR 2016 Bom 203 (SHA vs AOA primacy)
  - Nirma Chemical Works v. Vijay Chemicals AIR 1980 Guj 86 (SHA enforceability)
---

## Overview

**Shareholder Agreement (SHA)** = Contract between shareholders (and often company) governing their rights, obligations, and relationship beyond statutory AOA provisions.

**Purpose**:
- Investor protection (especially PE/VC investors)
- Governance control (board composition, reserved matters)
- Exit mechanisms (liquidity events, drag/tag-along)
- Dispute resolution (deadlock resolution, arbitration)

**Legal Status**:
- SHA is **contractual** (governed by Indian Contract Act 1872)
- AOA is **statutory** (governed by Companies Act 2013)
- SHA binds only signatory shareholders (not third parties)
- AOA binds company + all shareholders (public document)

---

## SHA vs AOA Distinction

### Legal Differences

| Aspect | Shareholder Agreement (SHA) | Articles of Association (AOA) |
|--------|---------------------------|-------------------------------|
| **Nature** | Private contract | Public constitutional document |
| **Governed By** | Contract Act 1872 | Companies Act 2013 |
| **Parties** | Shareholders (signatories only) | Company + All shareholders |
| **Amendments** | Requires consent of all parties (or as per SHA amendment clause) | Special resolution (75% majority) |
| **Disclosure** | Confidential (not filed with ROC) | Public document (filed with ROC, searchable) |
| **Enforceability** | Specific performance OR damages (breach of contract) | Company law remedies (oppression, NCLT) |
| **Duration** | Can be perpetual OR time-bound (e.g., till IPO) | Perpetual (till company exists) |
| **Third Party Rights** | No third party rights (privity of contract) | Binds all shareholders (including future shareholders if AOA incorporated) |

---

### Conflict Resolution: SHA vs AOA

**General Rule**: SHA provisions cannot override Companies Act provisions (statute prevails over contract).

**SHA Cannot Override** (Void Provisions):
❌ Minimum statutory quorum for board/general meetings (Section 174, 103)
❌ Special resolution requirement (Section 114)
❌ Alteration of MOA/AOA procedure (Section 13, 14)
❌ Mandatory disclosures to ROC (Section 92, 137)

**SHA Can Supplement** (Valid Provisions):
✅ Higher quorum than statutory minimum (e.g., 3 directors quorum vs statutory 2)
✅ Reserved matters requiring investor approval (beyond special resolution requirements)
✅ Board composition (investor nominee directors)
✅ Share transfer restrictions (ROFR, lock-in)
✅ Exit rights (tag-along, drag-along, put/call options)
✅ Anti-dilution adjustments
✅ Non-compete, confidentiality obligations

**Vodafone v. Union of India (2012) - SHA Validity**

**Facts**:
- Vodafone acquired 67% stake in Hutchison Essar (Indian telecom company)
- Transaction structured via acquisition of Cayman Islands holding company (which owned Indian subsidiary)
- Shareholders had SHA governing their rights
- Tax department argued SHA is "real" transaction (taxable in India), share purchase was form

**Issue**: Whether SHA creates taxable rights in India?

**Held**:
- SHA is valid contract between shareholders
- SHA provisions (call option, put option, ROFR) are **contractual rights**, not property rights
- No capital gains tax on SHA rights (only on share transfer)
- **Principle**: SHA is valid, enforceable contract. SHA rights are contractual (not property).

**Impact**: Upheld SHA validity, PE/VC investment structures commonly use SHAs for investor protection.

---

## Key SHA Clauses

### 1. Definitions

**Purpose**: Define key terms used throughout SHA (avoid ambiguity).

**Common Definitions**:
- **Investors**: Series A/B/C investors (preferential shareholders)
- **Founder Shareholders**: Promoters, founding team
- **Company**: [Company name]
- **Equity Shares**: Ordinary equity shares
- **Preference Shares**: CCPS (Compulsorily Convertible Preference Shares) held by investors
- **Board**: Board of directors of company
- **Reserved Matters**: Actions requiring investor approval (defined in Governance clause)
- **Liquidity Event**: IPO, M&A, liquidation
- **Drag-Along Notice**: Notice triggering drag-along rights
- **Tag-Along Offer**: Notice triggering tag-along rights

---

### 2. Parties and Recitals

**Parties**:
- Company (as confirming party)
- Founders (equity shareholders)
- Investors (preference shareholders)

**Recitals** (Background):
- Company incorporated on [date]
- Founders hold [X]% equity
- Investors investing ₹[Y] crore via CCPS subscription
- Parties desire to govern their rights via SHA

---

## Pre-emptive Rights and ROFR

### 3. Pre-emptive Rights (New Issuance)

**Definition**: Right of existing shareholders to subscribe to new shares **pro rata to their shareholding** before company offers to third parties.

**Clause Example**:
```
3.1 Pre-emptive Rights on New Issuance
If the Company proposes to issue new shares (equity or preference), the Company shall first offer such shares to existing shareholders in proportion to their shareholding.

3.2 Offer Notice
Company shall send written notice to shareholders stating:
(a) Number of shares offered
(b) Price per share
(c) Terms of issuance
(d) Last date to accept (minimum 15 days)

3.3 Acceptance/Waiver
Shareholder may accept offer (subscribe pro rata) OR waive pre-emptive rights (written waiver).
If shareholder doesn't respond within 15 days, deemed waiver.

3.4 Unsubscribed Shares
If shareholders don't subscribe to entire offer, Company may offer unsubscribed shares to third parties (at price not less than offer price).

3.5 Exceptions
Pre-emptive rights do not apply to:
(a) ESOP issuance (10% ESOP pool pre-approved)
(b) Bonus shares
(c) Shares issued to vendors/underwriters for non-cash consideration
```

**Strategic Purpose**:
- **Investor Protection**: Prevent dilution (maintain ownership %)
- **Founder Protection**: Maintain control by subscribing to new shares

---

### 4. Right of First Refusal (ROFR) (Share Transfer)

**Definition**: Right of existing shareholders to buy shares that another shareholder proposes to sell to third party.

**Clause Example**:
```
4.1 ROFR on Transfer
If any shareholder ("Selling Shareholder") proposes to transfer shares to third party ("Proposed Transferee"), Selling Shareholder shall first offer shares to:
(a) Company (if permitted by law, e.g., buyback)
(b) Other shareholders (pro rata to their shareholding)

4.2 ROFR Notice
Selling Shareholder shall send ROFR Notice to Company + shareholders stating:
(a) Number of shares offered
(b) Proposed purchase price
(c) Identity of Proposed Transferee
(d) Material terms of proposed sale

4.3 Acceptance Period (30 days)
Shareholders may accept ROFR offer within 30 days by written notice.
If multiple shareholders accept, shares allocated pro rata.

4.4 Pricing
Shareholders exercising ROFR shall purchase at **same price** as offered to Proposed Transferee.

4.5 Failure to Exercise ROFR
If shareholders don't exercise ROFR within 30 days, Selling Shareholder may sell to Proposed Transferee at same terms within next 90 days.
If sale not completed within 90 days, ROFR process restarts.

4.6 Exceptions (Permitted Transfers)
ROFR does not apply to transfers:
(a) To founder's family members or family trust (intra-family transfers)
(b) To investor's affiliate funds (intra-fund transfers)
(c) As per drag-along rights (Section 6)
```

**Strategic Purpose**:
- **Investor Protection**: Prevent entry of undesirable third parties (maintain cap table control)
- **Liquidity Opportunity**: Existing shareholders can buy shares at market price (increase stake)

---

## Tag-Along and Drag-Along Rights

### 5. Tag-Along Rights (Co-Sale Rights)

**Definition**: If **majority shareholder** sells shares to third party, **minority shareholders** have right to "tag along" and sell proportionate shares to same buyer at same terms.

**Scenario**:
- Founder (60% shareholding) receives offer from acquirer to sell their shares at ₹100/share
- Minority investors (40% shareholding) want to exit with founder (not remain in company with new controlling shareholder)
- Tag-along clause: Founder can sell ONLY if acquirer agrees to buy minority investors' shares **at same price (₹100/share)**

**Clause Example**:
```
5.1 Tag-Along Right
If Founder Shareholders propose to sell ≥25% of company's equity to third party ("Tag Buyer"), each Investor shall have right to "tag along" and sell:
(a) Proportionate number of shares (Investor shareholding % × total shares being sold by Founder)
(b) At same price per share as Founder
(c) On same terms and conditions as Founder's sale

5.2 Tag-Along Notice (30 days before closing)
Founder shall send Tag-Along Notice to Investors stating:
(a) Number of shares Founder proposes to sell
(b) Identity of Tag Buyer
(c) Purchase price per share
(d) Material terms of sale
(e) Closing date

5.3 Investor Acceptance (15 days)
Investor may elect to tag along by written notice within 15 days.
Investor shall specify number of shares to sell (up to proportionate entitlement).

5.4 Reduction of Founder's Sale
If Tag Buyer unwilling to purchase Investors' shares:
- Founder's sale shall be reduced proportionately
- Example: Founder proposes to sell 60% stake. Investors (holding 40%) tag along.
  - Tag Buyer willing to buy only 70% total.
  - Allocation: Founder 42% (60% × 70/100), Investors 28% (40% × 70/100)

5.5 Tag-Along Failure = Sale Void
If Tag Buyer refuses to purchase Investors' tagged shares, Founder's entire sale transaction is void (Founder cannot sell without Investors getting exit).
```

**Strategic Purpose**:
- **Minority Protection**: Minority investors get exit opportunity when founder exits (avoid being "stuck" with new controlling shareholder)
- **Equal Treatment**: Minority gets same price as founder (no discriminatory pricing)

---

### 6. Drag-Along Rights (Forced Sale)

**Definition**: If **majority shareholders** approve sale of company, they can "drag along" **minority shareholders** to sell their shares to buyer (forced exit).

**Scenario**:
- Founder (60%) + Investor A (20%) = 80% shareholders approve acquisition offer at ₹100/share
- Investor B (20%) opposes acquisition (wants to hold shares)
- Drag-along clause: Investor B **forced to sell** at ₹100/share (cannot block deal)

**Clause Example**:
```
6.1 Drag-Along Right
If shareholders holding ≥75% equity ("Dragging Shareholders") approve sale of company to third party ("Drag Buyer"), Dragging Shareholders may require minority shareholders ("Dragged Shareholders") to sell their shares on same terms.

6.2 Conditions for Drag-Along
Drag-along applies if:
(a) Sale is for 100% of company's equity (full exit, not partial)
(b) Price ≥ [Minimum Price Floor, e.g., 1.5x invested capital for investors]
(c) Drag Buyer agrees to same terms for all shareholders (no discrimination)

6.3 Drag-Along Notice (30 days before closing)
Dragging Shareholders shall send Drag-Along Notice to Dragged Shareholders stating:
(a) Drag Buyer identity
(b) Purchase price per share
(c) Material terms of sale agreement
(d) Closing date

6.4 Obligations of Dragged Shareholders
Dragged Shareholders shall:
(a) Sell all their shares to Drag Buyer
(b) Execute sale agreements, transfer forms
(c) Provide representations and warranties (limited to title, capacity, authority)
(d) Cooperate with closing formalities

6.5 Indemnity Cap for Dragged Shareholders
Dragged Shareholders' liability for representations/warranties capped at their sale proceeds (Dragged Shareholders not liable beyond what they receive).

6.6 Exceptions (No Drag-Along)
Drag-along does not apply if:
(a) Sale price < Minimum Price Floor
(b) Payment terms unreasonable (e.g., deferred payment >3 years without security)
(c) Drag Buyer imposes discriminatory terms on Dragged Shareholders
```

**Strategic Purpose**:
- **Majority Protection**: Prevent minority from blocking exit (company sale needs 100% shareholding transfer)
- **Facilitates M&A**: Acquirers prefer 100% ownership (drag-along ensures no minority holdouts)

---

## Anti-Dilution Protection

### 7. Anti-Dilution Clause

**Definition**: If company raises future funding round at **lower valuation** ("down-round"), existing investors' shares automatically adjust (increase number of shares OR reduce price) to protect against dilution.

**Types**:

#### a. Full Ratchet Anti-Dilution

**Mechanism**: If down-round occurs, investor's original purchase price **reset to lower price** (as if investor paid lower price from beginning).

**Example**:
- Investor A: Invested ₹10 crore at ₹100/share = 10 lakh shares (Series A)
- Company raises Series B at ₹50/share (down-round, 50% lower)
- **Full Ratchet**: Investor A's price reset to ₹50/share
  - New shares: ₹10 crore / ₹50 = 20 lakh shares (doubled)
  - Investor A now holds 20 lakh shares (instead of 10 lakh)

**Impact**: Extremely dilutive to founders (founders' % ownership significantly reduced)

---

#### b. Weighted Average Anti-Dilution (Broad-Based)

**Mechanism**: Investor's price adjusted using weighted average formula (considers amount raised, price differential).

**Formula**:
```
New Price = Old Price × [(Old Shares + New Shares at Old Price) / (Old Shares + New Shares Issued)]

Where:
Old Shares = Total shares outstanding before new round
New Shares Issued = Shares issued in new round
New Shares at Old Price = (Amount raised in new round) / (Old Price)
```

**Example** (Same Scenario):
- Investor A: ₹10 crore at ₹100/share = 10 lakh shares (Series A)
- Total shares before Series B: 1 crore shares
- Series B: ₹5 crore raised at ₹50/share = 10 lakh new shares issued

**Calculation**:
- Old Shares = 1 crore
- New Shares at Old Price = ₹5 crore / ₹100 = 5 lakh shares
- New Shares Issued = 10 lakh shares
- New Price for Investor A = ₹100 × [(1 crore + 5 lakh) / (1 crore + 10 lakh)]
  - New Price = ₹100 × (1.05 crore / 1.10 crore) = ₹95.45/share

- Investor A's new shares = ₹10 crore / ₹95.45 = 10.48 lakh shares (vs original 10 lakh)
- **Increase**: 4.8% more shares (vs 100% under full ratchet)

**Impact**: Less dilutive to founders than full ratchet (considers amount raised, not just price drop).

---

**Clause Example** (Weighted Average):
```
7.1 Anti-Dilution Adjustment
If Company issues shares ("New Shares") at price per share < Series A Issue Price ("Down-Round"), Series A Issue Price shall be adjusted using weighted average formula (broad-based).

7.2 Formula
New Issue Price = Old Issue Price × [(A + B) / (A + C)]

Where:
A = Total shares outstanding immediately before New Shares issuance
B = (Aggregate consideration for New Shares) / (Old Issue Price)
C = Number of New Shares issued

7.3 Automatic Adjustment
Within 10 days of New Shares issuance, Company shall:
(a) Calculate New Issue Price
(b) Issue additional shares to Series A Investors (to adjust their holding to New Issue Price)
(c) Notify all shareholders of adjustment

7.4 Exceptions (No Anti-Dilution)
Anti-dilution does not apply to:
(a) ESOP issuance (10% pool pre-approved)
(b) Stock splits, bonus shares, dividends
(c) Conversion of preference shares to equity (per terms)
(d) Shares issued as consideration for M&A (not for cash)
```

**Strategic Purpose**:
- **Investor Protection**: Protect against dilution in down-rounds (maintain ownership %, economic value)
- **Founder Alignment**: Incentivize founders to raise at higher valuations (avoid triggering anti-dilution)

---

## Exit Rights and Liquidity

### 8. Redemption Rights (Put Option)

**Definition**: Investor's right to require company to **buy back their shares** after specified period (if no liquidity event occurs).

**Clause Example**:
```
8.1 Redemption Right (Put Option)
If no Liquidity Event occurs within [5 years] from Series A Closing Date, each Investor may require Company to redeem (buy back) their Preference Shares by written notice ("Redemption Notice").

8.2 Redemption Price
Higher of:
(a) 1.2x invested capital (20% IRR for 5 years), OR
(b) Fair market value (determined by independent registered valuer)

8.3 Redemption Timeline
Company shall redeem shares within [18 months] of Redemption Notice.
Payment in installments allowed (if company lacks funds):
- First installment: 50% within 6 months
- Second installment: 50% within 18 months

8.4 Source of Funds
Redemption funded from:
(a) Company's free reserves, OR
(b) Proceeds of fresh equity issuance (specifically for redemption)

8.5 Redemption Failure = Liquidation Trigger
If Company fails to redeem within 18 months, Investors may initiate liquidation/winding up of Company (as per Section 9).
```

**Strategic Purpose**:
- **Investor Protection**: Guaranteed exit if company doesn't achieve liquidity event (IPO/M&A) within timeframe
- **Downside Protection**: Minimum return (1.2x invested capital) even if company underperforms

**Legal Risk**: Redemption must comply with Section 68 (buyback provisions) - Source of funds, debt-equity ratio, solvency.

---

### 9. Drag-Along for Liquidation

**Clause Example**:
```
9.1 Liquidation Drag-Along
If shareholders holding ≥75% Preference Shares approve liquidation/winding up of Company, they may require all shareholders to vote in favor of winding up resolution (drag-along for liquidation).

9.2 Distribution Priority (on Liquidation)
Per Section 53 Insolvency & Bankruptcy Code 2016:
(a) Secured creditors
(b) Workmen dues
(c) Unsecured creditors
(d) Preference shareholders: 1x invested capital + arrears of dividend
(e) Equity shareholders: Residual assets
```

---

## Governance and Control Provisions

### 10. Board Composition

**Clause Example**:
```
10.1 Board Size and Composition
Company's Board shall have [7] directors:
(a) [3] directors nominated by Founder Shareholders
(b) [2] directors nominated by Series A Investors
(c) [2] independent directors (mutually agreed by Founder and Investors)

10.2 Nomination Rights
- Series A Investors entitled to nominate [2] directors so long as they hold ≥10% equity
- If Investor shareholding falls below 10%, nomination rights reduced to [1] director

10.3 Appointment Procedure
Company shall convene board meeting/general meeting to appoint/remove directors as per shareholder nominations.

10.4 Removal and Replacement
Nominating shareholder may remove/replace their nominee director at any time by written notice.
Company shall effect such removal/replacement within 15 days.
```

---

### 11. Reserved Matters (Investor Veto Rights)

**Definition**: List of actions that require **investor approval** (beyond board/shareholders' ordinary/special resolution).

**Clause Example**:
```
11.1 Reserved Matters Requiring Investor Approval
Company shall not undertake following actions without prior written approval of Investors holding ≥75% Preference Shares:

(a) Mergers & Acquisitions:
- Acquisition of any company/business (if consideration >₹1 crore)
- Merger, amalgamation, demerger, restructuring

(b) Capital Structure:
- Issue of new shares (except ESOP within approved 10% pool, except per pre-emptive rights)
- Buyback, redemption, capital reduction

(c) Debt & Security:
- Borrowing >₹50 lakh (aggregate across all debts)
- Creating security interest over company assets (>₹50 lakh)

(d) Related Party Transactions:
- Any transaction with Founder/Director/their relatives (>₹10 lakh per transaction)

(e) Capex & Opex:
- Capital expenditure >₹25 lakh per transaction
- Operating expenditure >₹50 lakh per annum (beyond approved budget)

(f) Dividend & Distributions:
- Declaration of dividend (except mandatory preference dividend)
- Any distribution to shareholders

(g) Management & Key Persons:
- Appointment/removal of CEO, CFO, CTO
- Change in CEO/CFO compensation (if increase >20%)

(h) Business Plan:
- Material deviation from approved annual business plan/budget
- Entry into new line of business (not in objects clause)

(i) Legal & Compliance:
- Voluntary winding up, liquidation
- Admission of liability >₹25 lakh (litigation settlement)
- Initiation of arbitration/litigation (where claim >₹25 lakh)

(j) Amendments:
- Alteration of MOA/AOA (except as necessary for compliance)
- Amendment of SHA
```

**Strategic Purpose**:
- **Investor Control**: Prevent founder from taking unilateral decisions that affect investor interests (dilution, related party transactions, excessive borrowing)
- **Risk Mitigation**: Ensure investor input on material decisions

---

### 12. Information Rights

**Clause Example**:
```
12.1 Financial Statements
Company shall provide to Investors:
(a) Unaudited quarterly financials (within 30 days of quarter end)
(b) Audited annual financial statements (within 90 days of FY end)
(c) Annual budget (45 days before FY start)

12.2 Board Meeting Materials
Company shall provide Investor-nominated directors:
(a) Board meeting agenda (7 days prior)
(b) Board meeting materials (3 days prior)
(c) Minutes of board meeting (within 15 days)

12.3 Inspection Rights
Investors may inspect company's books of account, statutory registers during business hours (upon reasonable notice).

12.4 Investor Meetings
Company shall hold quarterly meetings with Investors to review:
- Business performance vs budget
- Key operational metrics (revenue, burn rate, runway)
- Material developments, risks
```

---

## Dispute Resolution

### 13. Arbitration Clause

**Clause Example**:
```
13.1 Arbitration
Any dispute arising out of or in connection with this Agreement shall be resolved by arbitration per Arbitration and Conciliation Act 1996.

13.2 Arbitration Procedure
(a) Number of arbitrators: [3] (each party appoints 1, third arbitrator appointed by first two arbitrators)
(b) Seat of arbitration: [City]
(c) Language: English
(d) Governing law: Laws of India

13.3 Award Binding
Arbitral award shall be final and binding on parties.
Parties waive right to appeal arbitral award (except on grounds in Section 34 Arbitration Act).

13.4 Injunctive Relief
Notwithstanding arbitration clause, parties may seek interim injunctive relief from courts (to prevent irreparable harm pending arbitration).
```

---

### 14. Deadlock Resolution

**Clause Example**:
```
14.1 Deadlock Definition
Deadlock = Situation where:
(a) Board unable to pass resolution due to lack of quorum/majority for [2 consecutive meetings], OR
(b) Shareholders unable to pass special resolution (due to 50-50 deadlock)

14.2 Deadlock Resolution Procedure
Step 1: CEOs of disputing parties meet to resolve (30 days)
Step 2: If unresolved, escalate to senior management/board chairs (30 days)
Step 3: If still unresolved, trigger Buy-Sell Clause (Section 14.3)

14.3 Buy-Sell Clause (Russian Roulette)
If deadlock persists after Step 2:
(a) Either party ("Offeror") may offer to buy other party's shares at specified price
(b) Other party ("Offeree") has [60 days] to either:
    - Accept offer (sell shares to Offeror at offered price), OR
    - Reverse the transaction (buy Offeror's shares at **same price**)
(c) Offeree must choose one option (cannot reject both)

Purpose: Forces parties to make fair offer (if Offeror lowballs, Offeree buys at lowball price; if Offeror overpays, Offeree sells at high price).
```

---

## Best Practices

### For Investors (PE/VC)

✅ **Board Seats**: Secure at least 1-2 board seats (board observer rights if shareholding <10%)
✅ **Reserved Matters**: Define veto rights on material decisions (M&A, capex >₹1 crore, related party transactions, new fundraising)
✅ **Anti-Dilution**: Weighted average (broad-based) preferred over full ratchet (founder-friendly but still protective)
✅ **Tag-Along**: Ensure tag-along on any founder sale >25% (proportionate exit opportunity)
✅ **Redemption Rights**: 5-7 year horizon, 1.2-1.5x invested capital (downside protection)
✅ **Information Rights**: Quarterly financials, board materials, inspection rights (transparency)

---

### For Founders

✅ **Drag-Along**: Secure drag-along rights (prevent minority from blocking exit)
✅ **ROFR Exceptions**: Exclude intra-family transfers from ROFR (founder can gift shares to spouse/children without investor approval)
✅ **Anti-Dilution Cap**: Negotiate cap on anti-dilution adjustment (e.g., max 2x adjustment even in severe down-round)
✅ **Redemption Timeline**: Longer timeline (7 years vs 5 years), installment payments (reduce cash outflow burden)
✅ **Reserved Matters Thresholds**: Higher thresholds (capex >₹50 lakh vs ₹10 lakh), avoid veto on operational decisions
✅ **Founder Liquidity**: Secondary sale rights (founders can sell 10-20% shares in future rounds to generate personal liquidity)

---

## Conclusion

**Shareholder Agreements (SHA)** are critical for investor-founder alignment, especially in PE/VC-funded startups.

**Key Takeaways**:

1. ✅ **SHA vs AOA**: SHA is private contract (binds signatories), AOA is public document (binds company + all shareholders)
2. ✅ **Investor Protection**: Reserved matters, board seats, anti-dilution, tag-along, redemption rights
3. ✅ **Founder Protection**: Drag-along, ROFR exceptions, longer redemption timelines
4. ✅ **Exit Mechanisms**: Tag-along (minority exit with majority), drag-along (majority forces minority exit), redemption (investor put option)
5. ✅ **Dispute Resolution**: Arbitration, buy-sell clause (deadlock resolution)

**Strategic Advice**:

- **For Investors**: Focus on control (board seats, veto rights), downside protection (redemption, anti-dilution), exit (tag/drag, IPO/M&A clauses)
- **For Founders**: Balance control dilution (give board seats but retain majority), accept standard protections (tag-along, anti-dilution weighted average), negotiate operational freedom (higher reserved matters thresholds)
- **For Both**: Clear dispute resolution (arbitration, buy-sell), transparency (information rights), alignment (liquidation preference 1x-2x, not 3x+ which misaligns incentives)

---

**Next Protocols to Consult**:
- **IL-CORP-EQUITY-FINANCING**: Fundraising rounds, term sheets, valuation
- **IL-CORP-PRIVATE-EQUITY-VC**: PE/VC investment structures, CCPS, exit mechanisms
- **IL-CONTRACT-LAW**: Contract enforceability, breach remedies, specific performance
- **IL-CORP-BOARD-MEETINGS**: Board governance, director duties

---

**Legal Disclaimer**: This protocol provides informational guidance on shareholder agreements in India. It is NOT legal advice. For specific SHA drafting or negotiation, engage a qualified Corporate Lawyer with experience in PE/VC transactions. SHA enforceability depends on contract law principles, compliance with Companies Act, and commercial reasonableness.

---

**End of Protocol: IL-CORP-SHAREHOLDER-AGREEMENTS**
