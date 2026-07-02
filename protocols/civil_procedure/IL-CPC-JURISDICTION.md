# Protocol: Jurisdiction of Civil Courts (India)

**Protocol ID**: IL-CPC-JURISDICTION  
**Domain**: Civil Procedure  
**Subdomain**: Jurisdiction and Court Hierarchy  
**Version**: 1.0.0  
**Last Updated**: 2025-12-06

## Purpose

This protocol provides systematic guidance on determining which civil court has jurisdiction to entertain a suit, covering pecuniary, territorial, and subject matter jurisdiction under the Code of Civil Procedure 1908 (CPC).

## Activation Triggers

- User asks "Which court has jurisdiction to file my suit?"
- Need to determine appropriate court for civil litigation
- Jurisdiction challenge or objection raised
- Transfer of case requested
- Multiple defendants in different jurisdictions
- Property located in different jurisdictions
- Cause of action arose in multiple places

## Core Principles

### 1. Three Types of Jurisdiction (All Must Be Satisfied)

```
For a court to entertain a suit, it must have:

1. PECUNIARY Jurisdiction (value-based)
   → Can this court try suits of this value?

2. TERRITORIAL Jurisdiction (geography-based)
   → Does this court have jurisdiction over the area where defendant/property/cause of action is?

3. SUBJECT MATTER Jurisdiction (topic-based)
   → Is this court competent to try this type of case?

Rule: ALL THREE must be satisfied. If even one lacking → Court CANNOT try suit.
```

### 2. Fundamental Rule - Section 15

```
Section 15: Every suit shall be instituted in the court of the lowest grade 
competent to try it.

Meaning:
- Start at LOWEST court that has all three jurisdictions
- Cannot directly file in High Court if District Court competent
- Prevents forum shopping to higher courts

Example:
Suit value: Rs. 5 lakhs
District Court: Can try suits up to Rs. 3 crores
High Court: Original jurisdiction unlimited

→ File in District Court (lowest competent court)
✗ Cannot directly file in High Court (though it has jurisdiction)
```

## Jurisdiction Framework

### I. PECUNIARY JURISDICTION (Value-Based)

**Rule**: Court can only try suits within its monetary limits set by State Government.

#### Court Hierarchy and Pecuniary Limits:

```
Supreme Court:
- Article 131-132: Special original jurisdiction
- Appeals: No monetary limit

High Court (Original Side):
- Varies by state notification
- Example (Bombay): Rs. 2 lakhs and above
- Some High Courts: No original civil jurisdiction (only appellate)

District Court:
- Varies by state
- Typical: Up to Rs. 3 crores
- No upper limit if state notification says so

Subordinate Courts:
Civil Judge (Senior Division): Rs. 5 lakhs to Rs. 50 lakhs (varies by state)
Civil Judge (Junior Division): Up to Rs. 5 lakhs (varies by state)

Small Causes Court (Section 15 Provincial Small Cause Courts Act 1887):
- Urban areas only
- Typically: Up to Rs. 20,000-50,000
- Speedy procedure, no appeal on facts
```

#### Determination of "Value of Suit" (Sections 7-11 Court Fees Act 1870):

```
**Immovable Property**:
Market value at suit institution

**Movable Property**:
Market value at suit institution

**Debt/Money Claim**:
Principal amount + interest due (not future interest)

**Declaration of Title**:
Market value of property

**Injunction**:
Value of property affected

**Specific Performance**:
Amount of consideration

**Partition**:
Share of plaintiff (not whole property)

**Multiple Reliefs**:
Value of relief which gives jurisdiction (not aggregate)

Example:
Suit for Rs. 10 lakhs + specific performance of land worth Rs. 50 lakhs
→ Value = Rs. 50 lakhs (higher relief)
```

### II. TERRITORIAL JURISDICTION (Section 16-20)

**General Rule - Section 20**: 

```
"Every suit shall be instituted in a court within the local limits of whose 
jurisdiction:
(a) The defendant, or each of defendants where more than one, at time of 
    commencement of suit, actually and voluntarily resides, or carries on 
    business, or personally works for gain; OR
(b) Any defendants, where more than one, at time of commencement of suit 
    actually and voluntarily resides, or carries on business, or personally 
    works for gain, PROVIDED leave of court obtained; OR
(c) Cause of action, wholly or in part, arises."
```

#### A. Defendant's Residence/Business (Section 20(a))

**Single Defendant**:
```
File where defendant:
- Actually resides (not mere temporary stay)
- Voluntarily resides (not under arrest/detention)
- Carries on business (has office/regular business activity)
- Personally works for gain (employment/profession)

Example:
Defendant company: Registered office in Mumbai, branch in Delhi
→ Plaintiff can sue in Mumbai (registered office) OR Delhi (branch - carries on business)
```

**Multiple Defendants** (Section 20(a)):
```
If suing multiple defendants:
- Court must have jurisdiction over ALL defendants (conjunctive), OR
- Court must have jurisdiction over at least ONE defendant + get leave (Section 20(b))

Example:
Defendant 1: Resides in Mumbai
Defendant 2: Resides in Delhi
Defendant 3: Resides in Kolkata

Option 1: Find common jurisdiction (where all carry on business - unlikely)
Option 2: Sue in Mumbai (D1's residence) + get leave to add D2 and D3 (Section 20(b))
```

#### B. Cause of Action (Section 20(c))

**Definition**: 
```
"Cause of action" = Bundle of facts which give plaintiff right to sue

Must include:
1. Facts showing plaintiff's right
2. Facts showing defendant's infringement of that right
3. Facts showing consequent damage

Accrues when: All facts necessary for suit come into existence
```

**"Wholly or in Part" Arises**:
```
If cause of action arises in multiple places → Plaintiff can choose ANY place 
where any part of cause of action arose

Example (Debt Recovery):
Contract signed: Mumbai
Goods delivered: Delhi
Payment due: Bangalore
Default occurred: Bangalore

Cause of action arose in: Mumbai (contract) + Delhi (delivery) + Bangalore (default)
→ Plaintiff can file in ANY of these three places
```

**Continuing Cause of Action**:
```
If wrong is continuous (e.g., nuisance, defamation on website):
→ Cause of action arises wherever the wrong continues
→ Plaintiff can sue in any jurisdiction where wrong persists

Example:
Defamatory content on website accessible nationwide
→ Cause of action arises wherever website accessed
→ Plaintiff can sue in ANY jurisdiction in India (BUT recent SC judgments limiting this)
```

#### C. Special Territorial Jurisdiction Rules

**1. Immovable Property (Section 16)**:
```
Section 16: Suits for recovery of immovable property, partition, foreclosure, 
sale, rent, profits, etc. → MUST be filed where property is situated

Exception: No exception. Mandatory jurisdiction.

Example:
Land located: Mumbai
Plaintiff resides: Delhi
Defendant resides: Bangalore

→ Suit MUST be filed in Mumbai (where property situated)
✗ Cannot file in Delhi or Bangalore
```

**2. Compensation for Wrongs to Immovable Property (Section 16 Explanation)**:
```
If suit is ONLY for compensation (not recovery/partition):
→ Can file where property situated OR where defendant resides

Example:
Trespass on land in Mumbai; Defendant in Delhi
Relief: Only damages (not injunction/possession)

→ Can file in Mumbai OR Delhi
```

**3. Suit Against Vessel (Section 17)**:
```
Admiralty jurisdiction:
File where voyage began/ended OR where defendant resides
```

**4. Negotiable Instruments (Section 20 + NI Act Section 142)**:
```
Section 138 NI Act dishonor cases:
Can file where:
- Cheque presented for payment (bank branch), OR
- Payee/holder resides, OR
- Cause of action arose

Note: Restricted by Bridhi Chand v. Surajmull (not unlimited jurisdiction)
```

**5. Compensation for Wrongs to Person or Movables (Section 20)**:
```
File where:
- Wrong committed (tort occurred), OR
- Defendant resides, OR
- Plaintiff resides (if defendant carries on business there)
```

### III. SUBJECT MATTER JURISDICTION

**Rule**: Courts have jurisdiction over types of cases assigned by statute/constitution.

#### Categories:

```
Civil Courts (General):
- All civil matters NOT exclusively assigned elsewhere
- Section 9 CPC: Courts have jurisdiction to try all civil suits EXCEPT expressly/impliedly barred

Tribunals/Special Courts (Exclusive):
- Family Courts: Matrimonial disputes, guardianship
- Consumer Forums: Consumer complaints
- Debt Recovery Tribunals: Bank debt recovery
- NCLT: Company law matters
- Labour Courts: Industrial disputes
- Rent Control Courts: Landlord-tenant (in states with Rent Control Acts)

Rule: If matter assigned exclusively to tribunal → Civil court CANNOT try
```

**Section 9 CPC - Courts to Try All Civil Suits**:
```
"The Courts shall (subject to the provisions herein contained) have 
jurisdiction to try all suits of a civil nature excepting suits of which 
their cognizance is either expressly or impliedly barred."

Civil Nature Test:
✓ Civil: Private rights (property, contract, tort)
✗ Not Civil: Criminal acts, revenue matters, political questions

Expressly Barred:
- Statute says "no civil court shall have jurisdiction"
- Example: Rent Control Act bars civil court for rent disputes

Impliedly Barred:
- Comprehensive code with dispute resolution mechanism
- Example: Industrial Disputes Act creates labour tribunals → Civil courts impliedly barred
```

## Transfer of Cases

### Section 24 - Transfer from Court Lacking Jurisdiction

```
If court finds it lacks jurisdiction → Transfer to competent court

Procedure:
1. Court determines lack of jurisdiction (pecuniary/territorial/subject matter)
2. Passes order transferring to competent court
3. Evidence recorded in transferring court → Valid in receiving court

Effect:
- Suit deemed filed in receiving court from original institution date (for limitation)
- Filing fees paid in first court → Adjusted
```

### Section 25 - Transfer from Supreme Court or High Court

```
Supreme Court/High Court can transfer any case:
FROM: Any court subordinate to it
TO: Any other subordinate court

Grounds (Discretionary):
1. Convenience of parties
2. Ends of justice
3. Important questions of law involved
4. Multiplicity of proceedings

Procedure:
- Application by party OR suo motu by HC/SC
- Notice to opposite party
- Hearing
- Transfer order
```

## Jurisdiction Clauses in Contracts

### Validity and Effect:

```
Parties CAN agree on jurisdiction BY CONTRACT (Section 20 Explanation)

Valid Clause Example:
"All disputes arising from this contract shall be subject to exclusive 
jurisdiction of courts at Mumbai."

Effect:
✓ Creates additional ground for jurisdiction (beyond Section 20)
✓ Can confer jurisdiction where none existed
✗ CANNOT oust jurisdiction of court otherwise competent
✗ CANNOT violate Section 16 (immovable property mandatory jurisdiction)

Case Law - ABC Laminart v. AP Agencies (SC):
"Jurisdiction clause is an additional right; does not take away other 
jurisdictions under Section 20."

Result:
If clause says "Mumbai courts", plaintiff can ALSO sue where Section 20 allows.
To make EXCLUSIVE → Must explicitly say "EXCLUSIVE jurisdiction" + defendant must not object.
```

## Jurisdiction Objections

### When to Raise (Order VII Rule 10, 11):

```
Defendant must raise jurisdiction objection:
EARLIEST OPPORTUNITY (ideally with written statement)

Consequence of Delay:
If defendant participates in proceedings without objection → WAIVER of territorial 
jurisdiction objection

Exception:
- Pecuniary jurisdiction: CANNOT be waived (goes to court's competence)
- Subject matter jurisdiction: CANNOT be waived (goes to court's existence of power)
- Territorial jurisdiction: CAN be waived by conduct
```

### Procedure to Challenge:

```
1. File APPLICATION under Order VII Rule 10 (before written statement)
   OR raise in WRITTEN STATEMENT (Order VIII Rule 1)

2. Court decides jurisdiction AS PRELIMINARY ISSUE

3. Options:
   - Dismiss suit (if lacks jurisdiction + not transferable)
   - Transfer suit (Section 24 if competent court identifiable)
   - Return plaint for presentation to proper court (Order VII Rule 10)

4. Appeal:
   - Against rejection of jurisdiction challenge → Appeal/revision available
   - Against transfer order → Usually no appeal (but revision under Section 115 possible)
```

## Common Scenarios

### Scenario 1: Loan Default

```
Facts:
- Loan agreement signed: Bangalore
- Lender: Mumbai
- Borrower: Delhi
- Payment place: Bangalore
- Default: Borrower stopped paying

Cause of Action Arose:
- Bangalore (contract signed + payment place + default occurred)
- Mumbai (lender's loss suffered there)

Jurisdictions Available (Section 20):
1. Delhi (defendant resides) - Section 20(a)
2. Bangalore (cause of action arose) - Section 20(c)
3. Mumbai (if lender proves part of cause of action arose - arguable)

Cannot File:
- Any other city (no jurisdictional connection)
```

### Scenario 2: Breach of Contract for Sale of Goods

```
Facts:
- Seller: Kolkata
- Buyer: Chennai
- Contract signed: Mumbai (neutral place)
- Goods to be delivered: Chennai
- Payment: Bank transfer to Kolkata
- Breach: Goods not delivered

Cause of Action:
- Mumbai (contract signed)
- Chennai (delivery place - breach occurred here)
- Kolkata (seller's place - from where goods should have been dispatched)

Seller Suing Buyer (for non-payment):
- Kolkata (seller resides) - Section 20(a)
- Chennai (buyer resides) - Section 20(a)
- Mumbai, Chennai, Kolkata (cause of action) - Section 20(c)

Buyer Suing Seller (for non-delivery):
- Chennai (buyer resides) - Section 20(a)
- Kolkata (seller resides) - Section 20(a)
- Mumbai, Chennai, Kolkata (cause of action) - Section 20(c)
```

### Scenario 3: Partition of Ancestral Property

```
Facts:
- Ancestral house: Jaipur
- Co-owner 1: Jaipur
- Co-owner 2: Pune
- Co-owner 3: Bangalore

Mandatory Jurisdiction (Section 16):
MUST file in Jaipur (where immovable property situated)

Irrelevant:
- Where co-owners reside
- Where family originally from
- Where cause of action arose

Exception: NONE. Section 16 is absolute for immovable property suits.
```

### Scenario 4: Defamation (Tort)

```
Facts:
- Defamatory article published: In Delhi newspaper
- Article written: Mumbai
- Plaintiff: Lives in Bangalore
- Defendant: Lives in Delhi
- Article circulated: All India

Traditional Rule (Section 20):
- Delhi (defendant resides + wrong committed)
- Mumbai (cause of action partly arose)
- Bangalore (plaintiff resides + wrong suffered there)

Recent Restriction (SC in Banyan Tree Holdings):
For online defamation/media:
Plaintiff should sue where:
- Defendant resides, OR
- Plaintiff resides AND suffers "significant" reputational harm there

Not: Every place where accessible (prevents forum shopping)
```

### Scenario 5: Specific Performance of Contract for Land Sale

```
Facts:
- Land: Mumbai
- Seller: Delhi
- Buyer: Bangalore
- Contract signed: Mumbai
- Breach: Seller refuses to convey

Applicable Sections:
- Section 16: Immovable property suit → MUST file where property situated
- Relief: Specific performance (relates to immovable property)

Mandatory Jurisdiction:
Mumbai (where land situated)

Cannot File:
- Delhi (seller's residence) - Section 16 overrides Section 20
- Bangalore (buyer's residence)
```

### Scenario 6: Multiple Defendants in Different States

```
Facts:
- Plaintiff: Sues D1 (Mumbai) + D2 (Delhi) + D3 (Kolkata)
- Contract: Joint liability of all three

Options (Section 20):

Option 1: Section 20(a)
Find court where ALL defendants reside/carry business → Difficult if individual defendants

Option 2: Section 20(b)
File where ANY ONE defendant resides + get LEAVE to add others
Example: File in Mumbai (D1's residence) + seek leave to add D2, D3

Option 3: Section 20(c)
File where cause of action arose (if common cause of action against all)

Practical:
Option 2 most common (file where one defendant + get leave)
Court grants leave if:
- Causes of action connected
- Convenient for all parties
- Prevents multiplicity of suits
```

## Jurisdiction Over Corporations

### Registered Office (Section 20 + Companies Act):

```
Company "resides" where:
1. Registered office (Section 12 Companies Act 2013)
2. Subordinate office where "carries on business"

"Carries on business":
- Has office/branch
- Regular business activity (not one-off transaction)
- Employees/agents present
- Continuous operations

Example:
ABC Ltd: Registered office Mumbai
Branches: Delhi, Bangalore, Chennai

Plaintiff can sue ABC Ltd in:
- Mumbai (registered office) - Section 20(a)
- Delhi, Bangalore, Chennai (carries on business) - Section 20(a)
- Anywhere cause of action arose - Section 20(c)
```

### Service on Company (Order XXIX Rule 2):

```
Service on company valid if served at:
- Registered office, OR
- Principal place of business, OR
- Secretary/director/managing agent
```

## Jurisdiction Over Government (Section 79-82, Order XXVII)

### Union of India:

```
Defendant: Union of India
Jurisdiction: Where cause of action arose (Section 79 + Order XXVII Rule 3)

Service:
- Secretary of concerned department (Central), OR
- Section 80 notice mandatory (2 months prior)
```

### State Government:

```
Defendant: State Government
Jurisdiction: Where cause of action arose (within that state)

Service:
- Chief Secretary OR Secretary of concerned department
- Section 80 notice mandatory (2 months prior)
```

## Summary Chart

```
PECUNIARY JURISDICTION (Value):
Court Fees Act 1870 (Sections 7-11) → Determine value
State notification → Check court's monetary limit
File in LOWEST competent court (Section 15)

TERRITORIAL JURISDICTION (Place):
Section 16: Immovable property → MANDATORY (where property situated)
Section 20(a): Defendant's residence/business
Section 20(c): Cause of action (wholly or in part)
Jurisdiction clause: Additional (not exclusive unless explicit)

SUBJECT MATTER JURISDICTION (Type):
Section 9 CPC: Civil courts try all civil suits UNLESS barred
Expressly barred: Statute says so
Impliedly barred: Tribunal with exclusive jurisdiction

TRANSFER:
Section 24: Transfer if lacking jurisdiction
Section 25: HC/SC transfer for convenience/justice

OBJECTIONS:
Raise earliest (with written statement)
Pecuniary/subject matter: Cannot waive
Territorial: Can waive by conduct
```

## Common Mistakes

### Mistake 1: Filing in Higher Court Directly
```
❌ Wrong: Suit worth Rs. 10 lakhs filed directly in High Court
✓ Correct: File in District/Civil Court (lowest competent - Section 15)

Exception: High Court's original jurisdiction if state notification permits
```

### Mistake 2: Ignoring Section 16 Mandatory Jurisdiction
```
❌ Wrong: Partition suit for land in Jaipur filed in Delhi (where all parties reside)
✓ Correct: MUST file in Jaipur (Section 16 absolute)

No exception even if all parties agree to Delhi jurisdiction.
```

### Mistake 3: Assuming Jurisdiction Clause is Exclusive
```
❌ Wrong: Contract says "Mumbai jurisdiction" → Plaintiff thinks can ONLY sue in Mumbai
✓ Correct: Mumbai is ADDITIONAL jurisdiction; can also sue under Section 20

To make exclusive: Must say "EXCLUSIVE jurisdiction" + defendant must not object
```

### Mistake 4: Valuing Suit Incorrectly
```
❌ Wrong: Suit for Rs. 5 lakhs + Rs. 10 lakhs land → Value Rs. 15 lakhs (added)
✓ Correct: Value = Rs. 10 lakhs (highest relief; not aggregate)

Court Fees Act Section 7-11: Value is of relief sought (not cumulative)
```

### Mistake 5: Not Raising Jurisdiction Objection Timely
```
❌ Wrong: Defendant files written statement, appears in court, then raises jurisdiction
✓ Correct: Raise jurisdiction in written statement OR preliminary application (earliest)

Delay → Waiver of territorial jurisdiction (not pecuniary/subject matter)
```

### Mistake 6: Thinking Online Defamation Gives Nationwide Jurisdiction
```
❌ Wrong: Defamatory post on website → Sue anywhere in India
✓ Correct: Sue where defendant resides OR where significant harm to reputation (SC restriction)

Banyan Tree Holdings: Cannot sue in every jurisdiction where accessible
```

### Mistake 7: Not Getting Leave for Multiple Defendants (Section 20(b))
```
❌ Wrong: File suit against D1 (Mumbai) + D2 (Delhi) in Mumbai without leave
✓ Correct: File in Mumbai + seek LEAVE to add D2 (Section 20(b))

Court must grant leave (otherwise suit against D2 liable to be dismissed)
```

## Case Law

### 1. RSA Industries v. Abhishek Khanna (SC 2020)
```
Facts: Jurisdiction clause in contract; defendant raised jurisdiction objection
Held: 
- Jurisdiction clause gives ADDITIONAL forum (not exclusive)
- To be exclusive: Must explicitly state + parties' intent clear
- Defendant must object timely; silence → Submission to jurisdiction
```

### 2. ABC Laminart v. AP Agencies (SC 1989)
```
Facts: Contract had "Bombay jurisdiction" clause; suit filed in Bombay
Held:
- Jurisdiction clause DOES NOT oust other courts' jurisdiction under Section 20
- Plaintiff can sue where Section 20 allows EVEN IF jurisdiction clause exists
- Clause creates CONCURRENT jurisdiction (not exclusive)
```

### 3. Swastik Gases v. Indian Oil Corporation (SC 2013)
```
Facts: Multiple defendants in different states; suit filed where one defendant resides
Held:
- Section 20(b): Can sue where ONE defendant resides + get leave for others
- Leave should be granted if:
  * Causes of action connected
  * Prevents multiplicity
  * Not oppressive to other defendants
```

### 4. Kusum Ingots v. Union of India (SC 2004)
```
Facts: Continuing cause of action in multiple jurisdictions
Held:
- "Cause of action" = Bundle of facts giving right to sue
- "Wholly or in part" → Plaintiff can choose ANY place where any part arose
- BUT should not be purely for convenience/forum shopping
```

### 5. Banyan Tree Holdings v. A Murali Krishna Reddy (SC 2009)
```
Facts: Defamation on website; plaintiff sued in his own jurisdiction
Held:
- For online content: Jurisdiction where plaintiff resides + suffers SIGNIFICANT harm
- Not every place where content accessible (prevents unlimited jurisdiction)
- Must show real and substantial connection to forum
```

### 6. New Moga Transport Co. v. United India Insurance (SC 2004)
```
Facts: Jurisdiction clause in insurance policy; accident occurred elsewhere
Held:
- Jurisdiction clause valid but NOT exclusive unless so stated
- Can sue where accident occurred (Section 20(c) - cause of action)
- Clause gives ADDITIONAL option (not ONLY option)
```

### 7. Hakam Singh v. Gammon (SC 1971)
```
Facts: Whether suit for compensation for wrong to immovable property falls under Section 16
Held:
- Section 16: Recovery, partition, foreclosure, rent → MUST file where property situated
- ONLY compensation: Can file where property situated OR where defendant resides (Explanation)
- If mixed relief (compensation + injunction) → Section 16 mandatory
```

## Limitation Period

```
Jurisdiction objections:
- No specific limitation
- Must raise at EARLIEST OPPORTUNITY
- Ideally: With written statement (Order VIII)
- Latest: Before leading evidence

Delay consequences:
- Territorial jurisdiction → WAIVED if not raised timely
- Pecuniary/subject matter → Can raise ANYTIME (even in appeal)
```

## Integration Points

- **IL-CPC-COURT-HIERARCHY**: Court structure, appeals
- **IL-CPC-PLAINT-WRITTEN-STATEMENT**: Pleadings, jurisdiction objections
- **IL-CPC-SUMMONS-SERVICE**: Service requirements
- **IL-CONTRACT-FORMATION**: Jurisdiction clauses in contracts
- **IL-CPC-APPEALS-REVISION**: Challenging jurisdiction orders

## Version History

- **1.0.0** (2025-12-06): Initial protocol creation

---

**Authority**: Code of Civil Procedure 1908 (Sections 9, 15-25), Court Fees Act 1870, Companies Act 2013  
**Jurisdiction**: All India (Civil Courts)  
**Type**: Civil Procedure
