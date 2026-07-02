---
description: Provide step-by-step self-representation guidance across ALL law domains (labour, consumer, civil, property, writ petitions, IP, criminal) for litigants who cannot afford lawyers. Automatically detects legal domain and provides domain-specific filing guides, court etiquette, cost savings analysis, and success strategies.
argument-hint: [describe your legal situation in plain English]
---

# Command: Universal Self-Representation Guide

## Purpose
Provide step-by-step self-representation guidance across ALL law domains (labour, consumer, civil, property, writ petitions, IP, criminal) for litigants who cannot afford lawyers. Automatically detects legal domain and provides domain-specific filing guides, court etiquette, cost savings analysis, and success strategies.

## Usage
```
/self-represent [describe your legal situation in plain English]
```

## What This Command Does

### 1. Domain Auto-Detection
Analyzes your situation description to identify which area of law applies:
- **Labour Law**: Wrongful termination, retrenchment, statutory dues (PF, ESI, Gratuity)
- **Consumer Law**: RERA complaints (builder delays), defective products, service deficiency
- **Civil Law**: Contract breaches, property disputes, specific performance
- **Writ Petitions**: Government license denials, administrative action challenges
- **Property Law**: Title disputes, encroachment, adverse possession
- **IP Law**: Trademark opposition, patent infringement (limited self-rep feasibility)
- **Criminal Law**: Bail applications, FIR quashing (HIGH RISK - lawyer strongly recommended)

### 2. Cost-Benefit Analysis
Compares self-representation costs vs hiring lawyer:
- **Self-Representation**: ₹1,000-10,000 (court fees, photocopies, travel)
- **Hiring Lawyer**: ₹30,000-₹5,00,000 (depending on case complexity)
- **Savings**: ₹29,000-₹4,90,000

### 3. Domain-Specific Package
Provides complete self-representation package tailored to your legal domain:
- **Step-by-step filing guides** (conciliation, tribunal, court)
- **Sample forms and templates** (complaint, plaint, affidavit, application)
- **Court etiquette guidance** (how to address judge, stand, respond, object)
- **Timeline tracking** (filing deadlines, hearing dates, limitation periods)
- **Success strategies** (what to say, what NOT to say, common mistakes)
- **Alternative remedies** (mediation, arbitration, settlement)

### 4. Agent Delegation
Routes to appropriate specialist agent based on domain detected:
- Labour → `labour-dispute-strategist`
- Consumer → `consumer-protection-specialist`
- Civil → `civil-litigation-strategist`
- Writ → `india-civic-law-specialist`
- Property → `property-due-diligence-agent`

---

## Example Usage

### Example 1: Labour Dispute (Wrongful Termination)

**Input**:
```
/self-represent I was terminated without domestic enquiry after 8 years service as factory worker. Salary ₹25,000/month. Cannot afford lawyer.
```

**Domain Detected**: Labour Law

**Agent**: labour-dispute-strategist

**Output Provided**:

#### Cost-Benefit Analysis
- **Self-Representation**: ₹2,000-6,000 (conciliation free, labour court fees ₹100-500)
- **Hiring Lawyer**: ₹30,000-75,000
- **Savings**: ₹24,000-73,000

#### Phase 1: Conciliation (Mandatory First Step - FREE)
```markdown
**Step 1: Draft Conciliation Complaint**

To: The Conciliation Officer
Labour Department, [Your District]

COMPLAINT UNDER INDUSTRIAL DISPUTES ACT 1947 (Section 12)

Complainant: [Your Name]
Address: [Your Full Address]
Occupation: Factory Worker

Respondent: [Company Name]
Address: [Company Address]

Nature of Dispute:
I was employed as factory worker from [Date] to [Termination Date] (8 years service).

On [Termination Date], I was terminated without:
1. Issuing charge sheet
2. Conducting domestic enquiry
3. Giving notice
4. Stating any reason

This is illegal termination violating principles of natural justice and Section 11A of Industrial Disputes Act 1947.

Relief Sought:
1. Reinstatement to service
2. Back wages from termination date
3. Statutory dues: PF ₹4,50,000, Gratuity ₹1,15,385, Notice Pay ₹25,000

I request conciliation under Industrial Disputes Act.

Date: [DD/MM/YYYY]
[Your Signature]
[Your Name]

**Step 2: File at Labour Office**
- Visit Labour Commissioner's office (district headquarters)
- Submit 2 copies of complaint
- NO FEES (conciliation is free)
- Get acknowledgment with case number

**Step 3: Attend Conciliation Meeting**
- Conciliation Officer calls both parties within 21 days
- Discuss settlement (employer may offer ₹2-5 lakhs settlement)
- If settlement reached → Sign settlement deed (legally binding)
- If settlement fails → Get "Failure of Conciliation" report

**Timeline**: 21 days (conciliation must complete within this period)
```

#### Phase 2: Labour Court Filing (If Conciliation Fails)
```markdown
**Document: Reference Application**

To: The Presiding Officer
Labour Court, [Your City]

REFERENCE APPLICATION UNDER SECTION 10A
INDUSTRIAL DISPUTES ACT 1947

Applicant (Worker): [Your Name]
Respondent (Employer): [Company Name]

FACTS:
1. I worked 8 years (2016-2024) as Factory Worker
2. Terminated on [Date] WITHOUT domestic enquiry
3. No charge sheet, no hearing, no reasons given
4. Conciliation failed (Report dated [Date])

LEGAL GROUNDS:
1. Termination violates principles of natural justice (no enquiry, no hearing)
2. Section 11A Industrial Disputes Act: Employer must prove misconduct after fair enquiry
3. Supreme Court in *Bharat Forge v. Uttam Manohar Nakate* (2005): Defective enquiry = reinstatement

RELIEF SOUGHT:
1. Reinstatement with back wages (₹25,000/month × [months] = ₹[total])
2. Statutory dues:
   - PF: ₹4,50,000 (12% × ₹15,000 capped × 8 years × 12 months)
   - Gratuity: ₹1,15,385 (₹25,000 × 15 days × 8 years / 26)
   - Notice Pay: ₹25,000 (1 month as per Standing Orders)

VERIFICATION:
I verify that contents are true to my knowledge.

Date: [DD/MM/YYYY]
[Your Signature]
[Your Name]

**Filing Checklist**:
✓ Reference Application (3 copies - court, employer, yourself)
✓ Conciliation Failure Report (certified copy)
✓ Appointment letter (proof of employment)
✓ Salary slips (last 3 months)
✓ Termination letter
✓ Affidavit verifying application
✓ Court fee: ₹100-500 (varies by state)

**Where to File**: Labour Court registry, [Your City]
```

#### Court Etiquette Guide
```markdown
## Labour Court Appearance

**What to Wear**:
- Men: Shirt + Trousers (NOT jeans) + Formal shoes
- Women: Saree OR Salwar Kameez (plain colors)
- Avoid: Jeans, t-shirts, flashy jewelry

**How to Address Judge**:
- "Your Honour" (most common in labour court)
- "Sir" / "Madam" (acceptable)
- NOT "My Lord" (only for High Court/Supreme Court)

**When Your Case is Called**:
Court Clerk: "R.A. No. 123/2024"
You: Stand up, say "Present, Your Honour. I am [Name], the Applicant, appearing in person."

Judge: "Do you have a lawyer?"
You: "No, Your Honour. I am representing myself."

Judge: "What is your case?"
You: "Your Honour, I was terminated without domestic enquiry. I have filed reference application for reinstatement with back wages."

Judge: "Okay. Matter adjourned to [Next Date] for employer to file written statement."
You: [Note the date], say "Thank you, Your Honour."

**Common Mistakes to Avoid**:
❌ Don't argue with judge
❌ Don't interrupt employer's lawyer
❌ Don't lose temper (even if provoked)
❌ Don't volunteer extra information
❌ Bring mobile on silent (or switch off)

✅ Stay calm
✅ Speak slowly and clearly
✅ Answer only what is asked
✅ Stand when judge enters/leaves
```

#### Success Rate & Timeline
- **Success Rate**: 70-80% (if termination clearly illegal - no enquiry)
- **Timeline**: 1-2 years (6-12 hearings)
- **Settlement Probability**: 50% (employer may settle for ₹3-8 lakhs to avoid reinstatement)

---

### Example 2: RERA Complaint (Builder Delayed Flat)

**Input**:
```
/self-represent Builder delayed my flat by 3 years. Paid ₹50 lakhs. No possession. RERA complaint needed. Cannot afford lawyer.
```

**Domain Detected**: Consumer Law (RERA)

**Agent**: consumer-protection-specialist

**Output Provided**:

#### Cost-Benefit Analysis
- **Self-Representation**: ₹5,000-15,000 (RERA fees 1% of claim, max ₹5,000)
- **Hiring Lawyer**: ₹50,000-₹2,00,000 (RERA cases - complex)
- **Savings**: ₹35,000-₹1,85,000

#### RERA Complaint Filing
```markdown
**Document: RERA Complaint Format**

To: The Member/Chairperson
Real Estate Regulatory Authority, [State]

COMPLAINT UNDER SECTION 31
REAL ESTATE (REGULATION AND DEVELOPMENT) ACT 2016

Complainant (Buyer): [Your Name]
Respondent (Builder): [Builder Company Name]

FACTS:
1. Booked flat on [Date] at [Project Name]
2. Agreement for Sale dated [Date]
3. Total amount paid: ₹50,00,000
4. Possession promised: [Date - 3 years ago]
5. Possession NOT delivered till date

VIOLATIONS:
1. Section 18 RERA: Builder must deliver within time OR pay interest + compensation
2. Delay: 3 years (36 months × MCLR + 2% interest)
3. No occupancy certificate obtained (illegal to give possession)

RELIEF SOUGHT:
1. Immediate possession with occupancy certificate
2. Interest on delayed possession: ₹50,00,000 × 10% × 3 years = ₹15,00,000
3. Compensation for mental harassment: ₹2,00,000
4. Total: Possession + ₹17,00,000

Date: [DD/MM/YYYY]
[Your Signature]

**Filing Procedure**:
1. Visit RERA website: [state].rera.gov.in
2. Register as complainant
3. Upload documents online:
   - Agreement for Sale
   - Payment receipts (all installments)
   - Correspondence with builder (emails, letters)
   - RERA registration certificate of project
4. Pay fee: 1% of claim (₹17,00,000 × 1% = ₹17,000, capped at ₹5,000)
5. Get acknowledgment with complaint number

**Timeline**: 60 days for first hearing
```

#### RERA Hearing Etiquette
```markdown
**RERA Tribunal is SEMI-FORMAL** (more formal than consumer forum, less than court)

**Address Authority as**: "Sir" / "Madam" (RERA members are not judges)

**Typical Hearing**:
Member: "Both parties present?"
You: "Yes, Sir. I am the complainant, appearing in person."
Builder's Lawyer: "Yes, Sir. I appear for the builder."

Member: "What is the status of possession?"
You: "Sir, possession not given. 3 years delay. I seek interest + compensation."
Builder's Lawyer: "Sir, project delayed due to pandemic. Force majeure applies."
You: "Sir, delay started BEFORE pandemic (2021). Pandemic cannot excuse 3-year delay."

**Success Rate**: 80-90% (RERA strongly pro-buyer)
**Timeline**: 6 months - 1 year
**Settlement**: Builder may offer possession + partial interest (₹5-10 lakhs)
```

---

### Example 3: Writ Petition (License Denial)

**Input**:
```
/self-represent Municipal corporation denied my trade license without reasons. I meet all requirements. Can I file writ petition myself?
```

**Domain Detected**: Administrative Law (Writ Petition)

**Agent**: india-civic-law-specialist

**Output Provided**:

#### Feasibility Warning
```markdown
⚠️ **WRIT PETITIONS - COMPLEX PROCEDURE**

**Self-Representation Feasibility**: MODERATE (possible but challenging)

**Why Challenging**:
- High Court procedure very formal
- Judges expect legal precision
- Opponent (government) will have experienced lawyers
- Technical objections common (jurisdiction, locus standi, alternative remedy)

**Recommendation**:
- If claim value < ₹50,000: Self-represent (lawyer costs ₹10k-50k exceed benefit)
- If claim value > ₹1,00,000: Hire lawyer (complex constitutional law issues)
- Middle ground (₹50k-1L): Try self-rep, engage lawyer if dismissed at admission stage

**Success Rate (Self-Representing)**: 40-50% (vs 70-80% with lawyer)
```

#### Cost-Benefit Analysis
- **Self-Representation**: ₹2,000-5,000 (court fees ₹500-2,000, drafting ₹0)
- **Hiring Lawyer**: ₹10,000-₹50,000 (simple writ petition)
- **Savings**: ₹5,000-48,000

#### Writ Petition Format
```markdown
**IN THE HIGH COURT OF [STATE] AT [CITY]**
**WRIT PETITION NO. _____ OF 2025**

**IN THE MATTER OF ARTICLE 226 OF CONSTITUTION OF INDIA**

**[Your Name]** ... Petitioner

Versus

**1. Municipal Commissioner, [City]**
**2. Licensing Officer, [Department]** ... Respondents

**PETITION UNDER ARTICLE 226 OF CONSTITUTION OF INDIA**

Petitioner seeks writ of Mandamus directing Respondents to grant trade license.

**FACTS**:
1. Petitioner applied for trade license on [Date]
2. Application complete, all documents submitted
3. Petitioner meets ALL requirements under Municipal Act Section [X]
4. License arbitrarily denied on [Date] without reasons
5. Denial violates Article 14 (equality) and Article 19(1)(g) (right to trade)

**LEGAL GROUNDS**:
1. **Arbitrary Action**: Denial without reasons violates Article 14
2. **Legal Duty**: Municipal Corporation has DUTY to grant license if conditions met
3. **Fundamental Right**: Denial violates Article 19(1)(g) (right to occupation)
4. **Mandamus Appropriate**: Court can compel public authority to perform legal duty

**ALTERNATIVE REMEDY**:
No effective alternative remedy available. Municipal Act does not provide appeal.

**PRAYERS**:
1. Issue writ of Mandamus directing Municipal Commissioner to grant trade license
2. Costs

VERIFICATION:
I verify contents are true.

Date: [DD/MM/YYYY]
[Your Signature]
[Your Name]

**Annexures**:
A-1: Trade license application
A-2: Acknowledgment receipt
A-3: All documents submitted (NOC, rent agreement, etc.)
A-4: Denial letter (if received) OR statement that no response received
```

#### High Court Etiquette (VERY FORMAL)
```markdown
**Address Judge as**: "My Lord" / "Your Lordship" (High Court/Supreme Court)

**Standing Protocol**:
✅ Stand when judge enters (everyone rises, bow slightly)
✅ Stand while addressing court (don't sit while arguing)
✅ Stand when judge asks question

**Dress Code**:
- Formal wear mandatory (shirt + trousers for men, saree/formal for women)
- Advocates wear black coat + gown + bands (you don't need gown if self-representing)

**When Case is Called**:
Clerk: "W.P. No. 123/2025"
You: Stand, say "My Lord, I am the Petitioner, appearing in person."

Judge: "Petitioner-in-person? What is your grievance?"
You: "My Lord, Municipal Corporation denied trade license without reasons. I seek Mandamus to compel grant of license. I meet all statutory requirements under Municipal Act Section [X]."

Judge: "Have you filed all documents?"
You: "Yes, My Lord. Annexures A-1 to A-4 filed."

Judge: "Issue notice to respondents. Returnable in 4 weeks."
You: "As Your Lordship pleases. Thank you, My Lord."

**Timeline**: 6 months - 2 years (depends on High Court backlog)
**Success Rate (Self-Representing)**: 40-50% (judges may be lenient to self-representing litigants)
```

---

## Domain-Specific Success Rates (Self-Representation)

| Legal Domain | Feasibility | Success Rate | Lawyer Cost | Self-Rep Cost | Savings |
|--------------|-------------|--------------|-------------|---------------|---------|
| **Labour Court** | HIGH | 70-80% | ₹30k-75k | ₹2k-6k | ₹24k-73k |
| **Consumer Forum** | HIGH | 75-85% | ₹20k-50k | ₹1k-5k | ₹15k-49k |
| **RERA Tribunal** | MODERATE | 60-70% | ₹50k-2L | ₹5k-15k | ₹35k-1.85L |
| **Civil Court** | MODERATE | 50-60% | ₹50k-3L | ₹10k-30k | ₹20k-2.7L |
| **Writ Petition (HC)** | MODERATE | 40-50% | ₹10k-50k | ₹2k-5k | ₹5k-48k |
| **Criminal Defense** | LOW | 20-30% | ₹50k-5L | N/A | ❌ HIRE LAWYER |

**Recommendation**:
- ✅ **Self-Represent**: Labour, Consumer, RERA (high success rates, simple procedures)
- ⚠️ **Proceed with Caution**: Civil suits, Writ petitions (complex, but feasible)
- ❌ **Hire Lawyer**: Criminal cases (liberty at stake - NOT worth risk)

---

## Protocols Utilized

This command integrates ALL 144 protocols across 9 law domains:
- **Labour Law**: IL-LABOUR-INDUSTRIAL-DISPUTES, IL-LABOUR-EPF-ESIC, IL-LABOUR-GRATUITY
- **Consumer Law**: IL-CONSUMER-PROTECTION-ACT, IL-RERA-ACT
- **Civil Procedure**: IL-CPC-BASICS, IL-CPC-PLAINT, IL-CPC-TRIAL-PROCEDURE
- **Writ Jurisdiction**: CIVIC-WRIT-BASICS, CIVIC-WRIT-TYPES
- **Property Law**: IL-PROPERTY-TRANSFER-BASICS, IL-PROPERTY-SALE
- **Limitation**: IL-LIMITATION-ACT (filing deadlines)

## Agents Utilized

- `labour-dispute-strategist` (labour disputes)
- `consumer-protection-specialist` (RERA, consumer complaints)
- `civil-litigation-strategist` (civil suits, contract breaches)
- `india-civic-law-specialist` (writ petitions, RTI, PIL)
- `property-due-diligence-agent` (property title disputes)

## Skills Utilized

- `court-etiquette-guide` (universal court behavior)
- `limitation-calculator` (filing deadlines)
- `forum-selector` (which court/tribunal)
- `labour-law-calculator` (PF, Gratuity, ESI calculation)
- `document-drafter` (sample forms)

---

**Version**: 1.0
**Last Updated**: December 2025
**Coverage**: ALL 9 law domains (Labour, Consumer, Civil, Property, IP, Writ, Criminal, Contract, Corporate)
**Replaces**: `/self-represent-labour` (deprecated - use this universal command instead)
