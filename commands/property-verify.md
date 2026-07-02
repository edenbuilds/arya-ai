---
description: Conduct comprehensive property title verification, due diligence analysis, encumbrance review, and risk assessment for immovable property transactions (sale, mortgage, lease, gift) under Transfer of Property Act and Registration Act.
argument-hint: <property-details> <transaction-type>
---

# Slash Command: /property-verify - Property Title Verification and Due Diligence

## Purpose
Conduct comprehensive property title verification, due diligence analysis, encumbrance review, and risk assessment for immovable property transactions (sale, mortgage, lease, gift) under Transfer of Property Act and Registration Act.

## Usage
```
/property-verify <property-details> <transaction-type>
```

## What This Command Does

When you invoke `/property-verify`, I will systematically:

1. **Title Chain Analysis:**
   - Examine property ownership chain (minimum 30 years recommended)
   - Verify each transaction link (sale, inheritance, gift, partition)
   - Identify breaks in chain or missing documents
   - Assess root of title validity

2. **Registration Compliance:**
   - Verify mandatory registration (Section 17 Registration Act)
   - Check stamp duty payment adequacy
   - Validate document execution (signatures, witnesses)
   - Assess unregistered documents (void as to transfer - Section 49)

3. **Encumbrance Analysis:**
   - Review Encumbrance Certificate (13-15 years)
   - Identify mortgages, charges, liens
   - Detect court attachments or litigation
   - Verify tax dues and clearances

4. **Legal Search:**
   - Civil litigation search (partition, specific performance, injunction)
   - Criminal cases (fraud, cheating related to property)
   - Revenue court disputes

5. **Physical Verification Guidance:**
   - Site inspection protocol (boundary verification)
   - Encroachment identification
   - Occupancy status (vacant, tenant, owner-occupied)
   - Municipal records verification (Khata, property tax)

6. **Risk Assessment:**
   - Categorize risks (High/Medium/Low)
   - Identify title defects and marketability issues
   - Recommend mitigation strategies (indemnity, escrow, price reduction)

7. **Transaction Structuring:**
   - Payment milestone recommendations
   - Escrow arrangements for disputed amounts
   - Registration timeline and compliance
   - Post-registration obligations (mutation, tax transfer)

8. **Stamp Duty Calculation:**
   - State-wise stamp duty rates
   - Registration fee estimation
   - Total transaction cost projection

## Example Usage

### Example: Apartment Purchase Verification
```
/property-verify I want to purchase Flat 503, Tower A, Prestige Gardens, Bangalore. Seller bought it in 2015 for Rs. 60 lakhs, now selling for Rs. 1.2 crores. Society is 15 years old. I have the sale agreement and EC from 2010. Transaction: Sale.
```

**Agent Response:**
```markdown
## Property Due Diligence Report: Flat 503, Prestige Gardens, Bangalore

### Property Overview
- **Location:** Flat 503, Tower A, Prestige Gardens, Bangalore
- **Transaction Type:** SALE (Purchase)
- **Seller's Acquisition:** 2015 (Rs. 60 lakhs)
- **Current Offer:** Rs. 1.2 crores
- **Building Age:** 15 years (approx 2010 construction)
- **EC Period Provided:** 2010 onwards

### Due Diligence Checklist

**Critical Documents (REQUEST IMMEDIATELY):**

**MANDATORY:**
- [ ] Title deeds from 2000/1995 (30-year chain - EC starts 2010, need earlier deeds)
  - **Gap Identified:** Need title documents from project inception (~2008-2010)
- [ ] Encumbrance Certificate 2008-2024 (15 years minimum)
  - **Current:** 2010-2024 provided (INSUFFICIENT - need from project approval ~2008)
- [ ] Registered Sale Deed (Seller's purchase in 2015)
  - Document No., Registration Date required
- [ ] Approved Building Plan + Occupancy Certificate
  - Verify legal construction, no unauthorized additions
- [ ] Property Tax Receipts (last 5 years)
  - Verify no dues, current Khata in seller's name
- [ ] Society Share Certificate in Seller's Name
  - Proof of society membership
- [ ] Society NOC for Sale
  - Mandatory for sale completion

**IMPORTANT:**
- [ ] Power of Attorney (if seller executing through POA - verify GPA validity)
- [ ] Apartment Possession Letter (from builder to seller - 2015)
- [ ] Original Builder-Seller Sale Agreement (2015)
- [ ] Loan Closure Certificate (if seller's flat was mortgaged - verify mortgage released)

### Title Chain Analysis

**Required Chain:**
1. **Root of Title:** Builder's land acquisition (typically 20-30 years before project)
2. **Development:** Builder developed Prestige Gardens (2008-2010 approx)
3. **First Sale:** Builder → Original Buyer (2010-2012)
4. **Second Sale:** Original Buyer → Current Seller (2015)
5. **Proposed Sale:** Current Seller → YOU (2024)

**Current Gap:**
- **Missing:** Title from builder's land acquisition to seller's purchase (2015)
- **Risk:** Cannot verify builder had clear title to sell in 2015
- **Recommendation:** Obtain:
  - Builder's title documents (land purchase deed, development agreement)
  - Khata extract showing building approval
  - Completion certificate (building legally constructed)

**Verification Steps:**
1. **Request from Seller:**
   - Copy of builder's original title (if available)
   - Certified copy of approved building plan
   - Occupancy Certificate (OC) - CRITICAL (no OC = illegal construction)

2. **BBMP Records Search:**
   - Khata extract (shows ownership progression)
   - Property tax payment history (establishes continuous ownership)
   - Building plan approval records

3. **Society Records:**
   - Builder-Society handover documents
   - Allotment of flat to first buyer
   - Transfer to current seller (2015)

### Encumbrance Certificate Analysis

**EC Period Provided:** 2010-2024

**What to Look For in EC:**
1. **Mortgages:** Any bank loans on property (should be NIL or released)
2. **Court Orders:** Attachment, injunction (should be NIL)
3. **Revenue Entries:** Acquisition, betterment charges (should be NIL)
4. **Tax Dues:** Outstanding property tax (should be paid)

**Common Red Flags (CHECK):**
- Unreleased mortgage (seller's loan not closed)
- Court attachment order (litigation pending)
- "Subject to conditions" entries (investigate further)
- Multiple sale entries (indicates chain - verify each)

**Action Items:**
1. Obtain fresh EC from 2008 (not just 2010 - cover project inception)
2. Verify each transaction in EC matches title documents
3. Check for unreleased mortgages (if seller took home loan in 2015, verify closure)

**Example EC Entry to Verify:**
```
Year: 2015
Document No.: 12345/2015
Type: Sale Deed
Parties: Mr. X (Seller) to Mr. Current Seller (Buyer)
Consideration: Rs. 60 lakhs
```
- **Verify:** Does this match seller's title deed? Same document number? Same parties?

### Legal and Litigation Search

**Civil Court Search (Bangalore City Civil Court):**
- Search party name: Current Seller + Previous owners
- Case types: Partition, Specific Performance, Injunction, Declaration
- **Action:** Visit court record room OR engage advocate for search
- **Timeline:** 1-2 weeks

**High Court Search (Karnataka HC):**
- Writ petitions, appeals related to property
- Search by property description (Survey No. if available)

**Revenue Court (Tahsildar/DC Court):**
- Land disputes, mutation challenges
- Verify no disputes over land on which building stands

**Criminal Court Search:**
- Cheating, fraud, forgery cases related to property sale
- Search current seller's name

**Recommendation:**
- If seller provides "No Litigation Certificate" from advocate, verify independently
- Budget: Rs. 10,000-20,000 for comprehensive search (worth the investment for Rs. 1.2 crore property)

### Society Verification (CRITICAL for Apartments)

**Society Records to Verify:**

1. **Share Certificate:**
   - Is it in current seller's name?
   - Share No., Certificate No. match society records?

2. **Maintenance Dues:**
   - Any outstanding? (seller must clear before sale)
   - Obtain "No Dues Certificate" from society

3. **Society NOC for Sale:**
   - Most societies require NOC before sale registration
   - NOC conditions (right of first refusal to society members?)
   - Processing time: 15-30 days (apply early)

4. **Society Bye-Laws:**
   - Any restriction on sale? (rare, but check)
   - Transfer fee payable to society? (typically Rs. 5,000-25,000)

5. **Builder-Society Handover:**
   - Has builder handed over maintenance to society?
   - If not, may indicate incomplete project (common areas not finished)

**Red Flag:** If society records show disputes with builder (pending maintenance handover, incomplete facilities), investigate further.

### Physical Verification Protocol

**Site Inspection (MANDATORY - Never skip):**

**Day Visit:**
1. **Boundary Verification:**
   - Flat matches description (carpet area, rooms as per agreement)
   - Verify against approved plan (no unauthorized modifications)

2. **Encroachment Check:**
   - Balconies, terraces not encroaching on common area
   - No boundary disputes with neighbors

3. **Structural Condition:**
   - Visible cracks, seepage, water damage?
   - If yes, document (photos/videos) - negotiate repair OR price reduction

4. **Occupancy:**
   - Who is occupying? (Seller, tenant, vacant?)
   - If tenant-occupied, rent agreement status (rent control act applicability?)

5. **Common Areas:**
   - Lifts, staircases, parking functional?
   - Any major pending repairs/redevelopment?

**Municipal Records (BBMP Office):**
1. **Khata Extract:**
   - Current Khata in seller's name? (proof of tax-paying owner)
   - Khata type: A Khata (legal) OR B Khata (illegal - avoid B Khata properties)

2. **Property Tax:**
   - Paid up to date? (last 5 years receipts)
   - Annual tax amount (you will continue paying post-purchase)

3. **Building Plan Approval:**
   - Approved plan on record (matches constructed building?)
   - Occupancy Certificate issued?

**Utility Connections:**
- Electricity: BESCOM connection (meter in seller's name? transfer needed)
- Water: BWSSB/Borewell supply
- Gas pipeline (if applicable)

### Risk Assessment

**Risk Matrix:**

| Risk Factor | Level | Impact | Mitigation |
|-------------|-------|--------|------------|
| **Missing title documents (pre-2010)** | HIGH | Cannot verify builder's title, risk of invalid sale | Demand builder's title OR reduce price for risk OR avoid |
| **No Occupancy Certificate** | HIGH | Building illegal, demolition risk (rare but catastrophic) | MUST obtain OC OR avoid transaction |
| **Unreleased mortgage (if seller's loan)** | MEDIUM | Cannot get clear title until released | Seller must provide loan closure certificate |
| **Litigation pending (if found)** | MEDIUM-HIGH | Disputed ownership, sale may be challenged | Obtain litigation details, assess merit, seek indemnity |
| **Society NOC delay** | LOW | Registration delayed by 30 days | Plan timeline with buffer |
| **Property tax dues** | LOW | Buyer may inherit dues (up to 3 years backlog) | Deduct from sale consideration OR seller clears |

**Marketability Assessment:**

**CLEAR TITLE (Proceed):**
- Complete 30-year chain with all registered documents
- Occupancy Certificate obtained
- No litigation, mortgages released
- Society NOC available

**DOUBTFUL TITLE (Proceed with Conditions):**
- Minor gaps in chain (seller can rectify - obtain missing documents)
- Encumbrance found but clearable (e.g., seller's loan - obtain closure certificate)
- **Conditions:** Escrow, indemnity, price reduction

**UNMARKETABLE TITLE (AVOID):**
- Major breaks in chain (cannot trace ownership)
- No Occupancy Certificate (illegal construction)
- Active litigation with injunction order
- Multiple claimants to property

### Recommendations

**IMMEDIATE ACTIONS (Before Proceeding):**

1. **Request Missing Documents (Week 1):**
   - Builder's title (land purchase to development)
   - Occupancy Certificate (CRITICAL - non-negotiable)
   - Fresh EC from 2008-2024 (not just 2010)

2. **Society Verification (Week 1-2):**
   - Verify share certificate
   - Apply for NOC (may take 30 days)
   - Obtain no-dues certificate

3. **Litigation Search (Week 2):**
   - Engage advocate for comprehensive search (Rs. 15,000-20,000)

4. **Physical Verification (Week 2):**
   - Site visit with building expert/engineer (if 15-year-old building, check structural soundness)
   - Municipal records verification (Khata in seller's name, tax paid)

**CONDITIONAL PROCEED (After Verification):**

**If OC Available + Clear Title:**
- Proceed with sale
- Structure payment: 10% advance → 40% on document signing → 50% on registration

**If OC NOT Available:**
- **Red Alert:** Illegal construction risk
- **Options:**
  1. Avoid transaction (safest)
  2. If building has been occupied 15+ years without demolition, risk may be low (but still exists)
  3. Significant price reduction (30-40%) to compensate risk
  4. Obtain indemnity from seller + builder (if available)

**If Title Gaps Found:**
- Seller must rectify (obtain missing documents, release mortgages)
- Hold 20-30% payment in escrow until rectification
- Set deadline: 60 days to cure defects

### Transaction Structuring

**Payment Schedule (If Proceeding):**

| Milestone | Amount (% of Rs. 1.2 Cr) | Condition |
|-----------|--------------------------|-----------|
| Token Advance (MOU signing) | Rs. 1 lakh (1%) | Refundable if title defects found |
| On Title Clearance | Rs. 12 lakhs (10%) | After due diligence complete, clear title confirmed |
| On Agreement Execution | Rs. 36 lakhs (30%) | Registered sale agreement signed |
| Balance on Registration | Rs. 71 lakhs (59%) | Registered sale deed + possession handover |

**Total:** Rs. 1.2 crores

**Escrow Provision:**
- If unresolved issues (e.g., seller's mortgage release pending): Hold Rs. 10-20 lakhs in escrow
- Release on mortgage closure certificate submission

**Indemnity Clause (in Sale Agreement):**
- Seller indemnifies buyer against:
  - Undisclosed liabilities (tax dues, society dues)
  - Undisclosed litigation
  - Title defects not disclosed
  - Encumbrances not disclosed

**Possession:**
- Vacant possession OR tenant-protected possession (with rent agreement transfer)
- Handover: Physical keys + society entry update within 7 days of registration

### Stamp Duty and Registration (Karnataka - Example)

**Calculation:**
- Property Value: Rs. 1.2 crores
- **Stamp Duty:** 5% (female buyer) / 5% (male buyer if < Rs. 45 lakhs guideline value, else graduated)
  - Assuming 5%: Rs. 1.2 cr × 5% = Rs. 6 lakhs
  - Cess: 1% = Rs. 1.2 lakhs
  - **Total Stamp Duty:** Rs. 7.2 lakhs (approx, verify current rates)
- **Registration Fee:** Rs. 1% = Rs. 1.2 lakhs (max cap Rs. 2 lakhs in some states)
- **Society Transfer Fee:** Rs. 10,000-25,000 (estimate)

**Total Transaction Cost (Buyer's Side):** Rs. 1.2 cr (price) + Rs. 7.2 lakhs (stamp) + Rs. 1.2 lakhs (reg) + Rs. 20,000 (misc) = **Rs. 1.29 crores**

**Seller's Cost:**
- Capital Gains Tax (if applicable - LTCG 20% with indexation OR STCG as per slab)
- Society clearance: No-dues certificate cost (Rs. 1,000-5,000)

### Registration Process (Karnataka)

**Online Registration (Kaveri Portal):**
1. Upload documents (ID proofs, sale agreement draft, EC, property docs)
2. Pay stamp duty online (GRAS portal)
3. Book appointment at Sub-Registrar office
4. Slot timing: 30-minute window
5. All parties + 2 witnesses present
6. Biometric verification + document execution
7. Registered deed issued same day OR within 7 days

**Timeline:** 15-30 days (from slot booking to registration)

**Post-Registration (Within 30 days):**
- Khata mutation (transfer property tax account to your name)
- Society share certificate transfer
- Utility connections transfer (electricity, water)

### Final Recommendation

**PROCEED WITH CAUTION - Subject to:**

1. **Obtain Occupancy Certificate:** Non-negotiable (if unavailable, AVOID)
2. **Complete Title Chain:** Demand builder's title + 30-year chain
3. **Clear Litigation Search:** No pending cases
4. **Society NOC:** Obtained before registration
5. **Mortgage Release:** If seller's flat mortgaged, loan closure certificate mandatory

**Estimated Timeline (if all clear):**
- Due diligence: 3-4 weeks
- Society NOC: 2-4 weeks
- Registration: 2 weeks
- **Total:** 8-10 weeks (2.5 months) from offer to possession

**Probability Assessment:**
- **If OC Available + Clear Chain:** 80% (PROCEED)
- **If OC Unavailable:** 20% (HIGH RISK - avoid unless significant price reduction)
- **If Title Gaps but Rectifiable:** 60% (CONDITIONAL - demand rectification)

**Would you like me to:**
1. Draft the due diligence checklist for your advocate?
2. Prepare the sale agreement with protective clauses?
3. Calculate exact stamp duty for your state?
4. Draft the indemnity clause for title defects?
5. Provide litigation search template for advocate?
```

## Protocols Utilized

- IL-PROPERTY-TRANSFER-BASICS.md - TPA fundamentals, transfer validity
- IL-PROPERTY-SALE.md - Sale deed requirements, Section 54 compliance
- IL-REGISTRATION-ACT.md - Mandatory registration, Section 17, Section 49 consequences
- IL-RERA-ACT.md - Occupancy certificate, building approvals (if under-construction)
- IL-CPC-EXECUTION.md - Court sale properties (if auction purchase)
- IL-CONTRACT-LAW.md - Sale agreements, breach remedies

## Agent Used

**Primary Agent:** property-due-diligence-agent

## Output Format

Comprehensive due diligence report with:
- Document checklist (critical vs important)
- Title chain verification roadmap
- Encumbrance analysis framework
- Legal search protocols
- Risk matrix (high/medium/low)
- Transaction structuring recommendations
- Stamp duty calculations
- Registration compliance guidance
- Timeline and cost estimates
- Conditional proceed/avoid recommendations

---

**Version:** 1.0  
**Last Updated:** December 2025  
**Domain:** Property Law (Transfer of Property Act 1882, Registration Act 1908)
