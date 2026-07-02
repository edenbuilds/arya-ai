---
description: Interactive mock court practice across ALL legal domains (labour, consumer, civil, writ petitions, criminal) with AI judge, opposing counsel, and witnesses. Provides realistic court simulations, performance feedback, and skill development for lawyers, law students, and aspiring litigators.
argument-hint: [domain] [case-type] [difficulty]
---

# Command: Universal Litigation Practice Simulator

## Purpose
Interactive mock court practice across ALL legal domains (labour, consumer, civil, writ petitions, criminal) with AI judge, opposing counsel, and witnesses. Provides realistic court simulations, performance feedback, and skill development for lawyers, law students, and aspiring litigators.

## Usage
```
/practice-lawyer [domain] [case-type] [difficulty]
```

**Parameters**:
- `domain`: labour | consumer | civil | writ | criminal | property
- `case-type`: Specific case within domain (e.g., wrongful-termination, rera-complaint, mandamus)
- `difficulty`: easy (70% win rate) | medium (50% win rate) | hard (30% win rate)

## What This Command Does

### 1. Generates Realistic Case Scenario
Creates fact pattern with:
- Background facts (employment details, transaction details, dispute history)
- Legal issues (what needs to be proven/defended)
- Evidence available (documents, witnesses)
- Procedural posture (first hearing, evidence stage, arguments stage)
- Your role (applicant's counsel OR respondent's counsel)

### 2. AI Court Simulation
**AI Judge**: Adapts behavior to court type
- Labour Court: Patient, worker-friendly, less formal ("Your Honour")
- Consumer Forum: Semi-formal, pro-consumer bias
- High Court: Very formal, strict, interventionist ("My Lord")
- Civil Court: Moderately formal, neutral

**AI Opposing Counsel**: Domain-appropriate strategies
- Labour: Employer's lawyer (attacks worker credibility, claims misconduct proven)
- Consumer: Company's lawyer (claims no deficiency, buyer's contributory negligence)
- Writ: Government's lawyer (cites alternative remedy, questions locus standi)
- Civil: Defendant's lawyer (denies breach, claims force majeure)

**AI Witnesses**: Realistic responses
- Evasive witnesses (\"I don't remember\")
- Hostile witnesses (defensive, argumentative)
- Cooperative witnesses (answer clearly)
- Expert witnesses (technical testimony)

### 3. Interactive Practice Modes
- **Cross-Examination Practice**: Question opposing party's witnesses
- **Examination-in-Chief Practice**: Elicit testimony from your client
- **Argument Practice**: Opening statements, final arguments, rebuttals
- **Objection Handling**: Respond to opposing counsel's objections
- **Settlement Negotiation**: Practice mediation, conciliation

### 4. Performance Feedback
**Real-Time Feedback** (during practice):
- ✅ Good question - establishes key fact
- ⚠️ Could improve - question too vague
- ❌ Avoid - argumentative question (judge will sustain objection)

**Comprehensive Report** (after practice):
- Overall Score: X/100
- Grade: A+ to F
- Dimension-wise breakdown (cross-examination, arguments, case law, objections)
- Strengths: What you did well
- Weaknesses: What needs improvement
- Suggested practice areas

---

## Example Usage

### Example 1: Labour Court Practice (Medium Difficulty)

**Input**:
```
/practice-lawyer labour wrongful-termination medium
```

**Output**:

#### Case Scenario Generated
```markdown
## MOCK CASE - LABOUR COURT PRACTICE

**Ref. No.**: R.A. 456/2024 (Simulated)
**Before**: Labour Court, Mumbai (AI Simulation)

**Your Role**: Counsel for Applicant (Worker)

**Applicant (Your Client)**: Rajesh Kumar, Factory Worker
**Respondent (Employer)**: ABC Manufacturing Ltd.

**Background Facts**:
- Employment: 7 years (2017-2024) as Machine Operator
- Salary: ₹22,000/month
- Termination Date: 15th September 2024
- Reason Stated: "Misconduct - Damaged machinery worth ₹50,000"

**Domestic Enquiry Conducted**:
- Enquiry Officer: Mr. Sharma (Production Manager - Rajesh's REPORTING MANAGER)
- Charge Sheet: Issued 1 day before enquiry (14th Sept)
- Enquiry Date: 10th September 2024
- Finding: Guilty (dismissed for willful damage)

**Your Strategy**: Prove enquiry defective due to bias (enquiry officer = reporting manager with prior conflict)

**Evidence Available**:
1. Appointment letter (proves 7-year service)
2. March 2024 leave warning letter (proves prior conflict with Mr. Sharma)
3. Salary slips (last 3 months)
4. Termination order

**Difficulty**: Medium (50% win rate - valid enquiry conducted but bias issue exists)

**Your Objective**: Cross-examine enquiry officer (Mr. Sharma) to expose bias
```

---

#### Interactive Cross-Examination

```markdown
## CROSS-EXAMINATION PRACTICE

**AI JUDGE**: "Counsel for Applicant, you may cross-examine the witness."

**AI WITNESS** (Mr. Sharma): "I am ready, Your Honour."

---

**YOU** (first question): "Mr. Sharma, you are the Production Manager at ABC Manufacturing, correct?"

**AI SHARMA**: "Yes."

✅ **FEEDBACK**: Good foundational question - establishing identity

---

**YOU**: "And Mr. Rajesh Kumar, the Applicant, worked under your supervision for 7 years?"

**AI SHARMA**: "Yes, he reported to me."

✅ **FEEDBACK**: Establishing reporting relationship (bias foundation)

---

**YOU**: "So you were his REPORTING MANAGER for 7 years?"

**AI SHARMA**: "Yes."

**YOU**: "And who appointed you as the Enquiry Officer in this case?"

**AI SHARMA**: "The HR department appointed me."

✅ **EXCELLENT**: Key admission - reporting manager appointed as enquiry officer

---

**YOU**: "Mr. Sharma, did you have any prior disagreements with Mr. Rajesh?"

**AI OPPOSING COUNSEL** (Employer's Lawyer): "Objection, Your Honour! Irrelevant!"

**AI JUDGE**: "Objection OVERRULED. Bias is relevant. Counsel may continue."

✅ **JUDGE RULING**: Your line of questioning upheld

---

**YOU**: "Mr. Sharma, in March 2024, did you issue a written warning to Mr. Rajesh for taking leave?"

**AI SHARMA** (hesitates): "...Yes, for unauthorized absence."

**YOU**: "And did Mr. Rajesh CHALLENGE that warning by complaining to HR?"

**AI SHARMA** (defensive): "He did complain, yes, but it was baseless."

✅ **POWERFUL**: Exposed prior conflict (strengthens bias argument)

---

**YOU**: "Who WITNESSED the machinery damage incident on 9th September?"

**AI SHARMA**: "I witnessed it myself."

**YOU**: "So you are the SOLE witness to the alleged misconduct?"

**AI SHARMA**: "Yes, I was the only one present."

**YOU**: "And you are ALSO the person who filed the complaint against Mr. Rajesh?"

**AI SHARMA**: "Yes, as Production Manager, it was my duty."

**YOU**: "So, Mr. Sharma, you were:
1. The COMPLAINANT (filed report about damage)
2. The WITNESS (only person who saw incident)
3. The ENQUIRY OFFICER (conducted enquiry)

Is that correct?"

**AI SHARMA** (admits): "...Technically, yes."

✅ **DEVASTATING**: Triple role established (complainant + witness + judge)

---

**AI OPPOSING COUNSEL**: "Your Honour, I object! Counsel is arguing, not questioning!"

**AI JUDGE**: "Objection SUSTAINED. Counsel, just ask questions, don't argue yet. Save arguments for final submissions."

⚠️ **FEEDBACK**: Last question was argumentative. Rephrase as separate questions, not combined statement.

---

**YOU** (rephrased): "Thank you, Your Honour. Mr. Sharma, you filed the complaint, correct?"

**AI SHARMA**: "Yes."

**YOU**: "You witnessed the incident, correct?"

**AI SHARMA**: "Yes."

**YOU**: "And you conducted the enquiry, correct?"

**AI SHARMA**: "Yes."

**YOU**: "No further questions, Your Honour."

✅ **RECOVERED WELL**: Separated questions, achieved same impact

---

## CROSS-EXAMINATION COMPLETE

**AI JUDGE** (private feedback to you):

**Performance Score**: 85/100 (EXCELLENT - B+ Grade)

**What You Did Well**:
✅ Established reporting relationship (bias foundation)
✅ Exposed prior conflict (March warning letter)
✅ Extracted triple role admission (complainant + witness + enquiry officer)
✅ Controlled witness (didn't let him ramble)
✅ Recovered well from sustained objection

**What to Improve**:
⚠️ One question was argumentative (judge sustained objection)
⚠️ Could have asked: "Did you recommend to HR that a neutral officer conduct enquiry?"
⚠️ Could have asked: "Were you aware that being reporting manager + complainant creates conflict?"

**Success Probability (Based on Cross-Examination)**: 75%

**Why**: You established FATAL flaw in enquiry (same person = complainant + witness + judge). Employer will struggle to defend this in arguments.

**Next Step**: Practice final arguments (emphasize bias + cite *Siemens v. Union of India* case on enquiry officer independence)
```

---

### Example 2: Consumer Forum Practice (Easy Difficulty)

**Input**:
```
/practice-lawyer consumer defective-product easy
```

**Output**:

#### Case Scenario
```markdown
## MOCK CASE - CONSUMER FORUM PRACTICE

**Before**: District Consumer Disputes Redressal Commission

**Your Role**: Counsel for Complainant (Buyer)

**Complainant (Your Client)**: Mrs. Anjali Patel
**Opposite Party (Seller)**: XYZ Electronics Ltd.

**Facts**:
- Purchased washing machine on 1st March 2024 (₹25,000)
- Machine malfunctioned within 1 month (drum stopped rotating)
- Complained to seller - sent for "repair" (not replacement)
- Repaired machine malfunctioned again within 15 days
- Seller refusing refund OR replacement

**Deficiency in Service**: Repeated malfunction within warranty period = inherent defect

**Relief Sought**:
1. Replacement with new machine OR Refund ₹25,000
2. Compensation for mental harassment: ₹10,000
3. Total: ₹35,000

**Evidence**:
- Purchase invoice (dated 1-March-2024)
- Warranty card (1 year warranty)
- Complaint emails (3 emails sent to seller)
- Repair invoice (dated 5-April-2024)

**Difficulty**: Easy (70% win rate - clear defect within warranty, seller non-responsive)
```

---

#### Mock Hearing

```markdown
**AI CONSUMER FORUM PRESIDENT**: "Both parties present?"

**YOU**: "Yes, Madam. I appear for the Complainant."

**AI OPPOSITE PARTY LAWYER**: "Yes, Madam. I appear for XYZ Electronics."

**AI PRESIDENT**: "Complainant's counsel, briefly state your case."

---

**YOU** (opening statement):
"Madam President, this is a clear case of defective product and deficiency in service.

My client purchased washing machine for ₹25,000 on 1st March 2024. Within 1 month, machine malfunctioned. Seller took it for repair instead of replacement (despite being within warranty).

Repaired machine malfunctioned AGAIN within 15 days. This proves INHERENT DEFECT.

Under Consumer Protection Act 2019 Section 2(11), this is 'deficiency in service.' Seller must replace OR refund.

I rely on *Bangalore Development Authority v. R. Purushothama* (2010) - if goods inherently defective, consumer entitled to replacement OR refund at his choice.

I seek replacement with new machine OR refund ₹25,000 + compensation ₹10,000 for mental harassment."

✅ **FEEDBACK**: Excellent opening - concise, cited facts, cited law, stated relief clearly

---

**AI OPPOSITE PARTY LAWYER**: "Madam President, there is no defect. Complainant misused the machine (overloading). Warranty doesn't cover misuse."

**AI PRESIDENT** (to you): "Counsel, how do you respond to allegation of misuse?"

**YOU**: "Madam, misuse is an ALLEGATION. Opposite party has provided NO evidence (no engineer report, no technical assessment).

Moreover, machine malfunctioned TWICE within 2 months. If it was misuse, why did it work initially?

Repeated malfunction = inherent defect (burden on opposite party to prove no defect - Section 2(34) Consumer Protection Act)."

✅ **STRONG REBUTTAL**: Shifted burden of proof to opposite party

---

**AI PRESIDENT**: "Opposite party, do you have any evidence of misuse?"

**AI OPPOSITE PARTY LAWYER**: "...No, Madam. But generally, overloading causes this issue."

**AI PRESIDENT**: "General allegations are not evidence. Order reserved."

## JUDGMENT (Next Hearing)

**AI PRESIDENT** (delivers order):

"After hearing both sides, we find:
1. Washing machine malfunctioned TWICE within 2 months
2. This indicates INHERENT DEFECT in product
3. Opposite party failed to prove misuse (no technical evidence)
4. Consumer Protection Act Section 2(11) - This is deficiency in service

ORDER: Complaint ALLOWED.
Opposite party directed to:
1. Refund ₹25,000 to Complainant within 30 days
2. Pay compensation ₹10,000 for mental harassment
3. Pay litigation costs ₹5,000

**YOU WIN**: 90% score

---

## PERFORMANCE REPORT

**Overall Score**: 88/100 (EXCELLENT - A- Grade)

**Strengths**:
✅ Excellent opening statement (facts + law + relief in 2 minutes)
✅ Strong rebuttal (shifted burden of proof to opposite party)
✅ Cited correct case law (*Bangalore Development Authority*)
✅ Stayed focused on key issue (inherent defect)

**Weaknesses**:
⚠️ Could have mentioned Consumer Protection Act Section 2(34) definition of "product" earlier
⚠️ Could have asked for HIGHER compensation (₹10k is low for 2-month harassment)

**Recommended Next Practice**:
Try MEDIUM difficulty (service deficiency with contributory negligence by consumer - more challenging)
```

---

### Example 3: High Court Writ Petition Practice (Hard Difficulty)

**Input**:
```
/practice-lawyer writ mandamus hard
```

**Output**:

#### Case Scenario
```markdown
## MOCK CASE - HIGH COURT WRIT PRACTICE

**Before**: High Court of [State] (AI Simulation)

**Your Role**: Petitioner's Counsel

**Petitioner (Your Client)**: Mr. Vikram Singh, Business Owner
**Respondents**: 1. State Government, 2. Licensing Authority

**Facts**:
- Applied for liquor license on 1st January 2024
- Meets all statutory requirements (premises, character certificate, fee paid)
- License denied on 30th June 2024 citing \"public interest\"
- No SPECIFIC reasons given (just \"public interest\" - vague)

**Challenges**:
1. Respondent has filed COUNTER-AFFIDAVIT stating: \"Local residents objected (50 signatures collected)\"
2. Alternative Remedy exists: Appeal to Excise Commissioner (under Excise Act Section 25)
3. Petitioner did NOT exhaust alternative remedy (filed writ directly)

**Legal Issues**:
1. Is writ maintainable despite alternative remedy?
2. Is \"public interest\" based on local objections valid ground?
3. Did authority violate natural justice (no hearing given to petitioner)?

**Difficulty**: Hard (30% win rate - alternative remedy not exhausted, local objections exist)

**Your Strategy**: Argue alternative remedy inadequate + natural justice violation
```

---

#### Mock Hearing (Admission Stage)

```markdown
**AI HIGH COURT JUDGE**: "Writ petition no. 123/2025. Counsel for petitioner?"

**YOU** (stand, bow): "My Lord, [Your Name] for the Petitioner."

**AI JUDGE**: "Counsel for respondent?"

**AI GOVERNMENT COUNSEL**: "My Lord, [Name] for the State Government."

---

**AI JUDGE** (to you): "Why have you approached this Court under Article 226 when there is alternative remedy under Section 25 of Excise Act? Appeal to Excise Commissioner is available."

⚠️ **CRITICAL QUESTION**: Judge questioning maintainability (alternative remedy objection)

**YOU**: "My Lord, I have TWO submissions:

**First**, alternative remedy under Section 25 is INADEQUATE because:
1. Excise Commissioner is part of same executive (not independent authority)
2. Appeal timeline is 60 days, but license denial causes daily business loss (₹10,000/day)
3. Commissioner has NO power to examine natural justice violation (only reviews factual correctness)

**Second**, this Court has held in *Whirlpool Corporation v. Registrar of Trademarks* (1998) that writ is maintainable despite alternative remedy if:
- Jurisdictional error exists OR
- Natural justice violated OR
- Order perverse

Here, natural justice was VIOLATED - no hearing given before denial despite adverse local objections.

I rely on *Maneka Gandhi v. Union of India* (1978) - Right to be heard is part of Article 21 (life and personal liberty includes livelihood)."

✅ **STRONG RESPONSE**: Cited exceptions to alternative remedy doctrine + case law

---

**AI GOVERNMENT COUNSEL** (responds):
"My Lord, in *L. Chandra Kumar v. Union of India* (1997), Supreme Court held alternative remedy must be exhausted. Petitioner cannot bypass statutory appeal just because it's inconvenient."

**AI JUDGE** (to you): "Counsel, how do you distinguish *L. Chandra Kumar* case?"

**YOU**: "My Lord, *L. Chandra Kumar* held alternative remedy must be exhausted UNLESS exception applies.

Here, EXCEPTION applies - natural justice violation (no hearing given).

In *State of UP v. Mohammad Nooh* (1958), Supreme Court held: If administrative order violates natural justice, writ is maintainable despite alternative remedy.

Petitioner was denied hearing before adverse decision based on local objections. This is CLASSIC natural justice violation."

✅ **EXCELLENT DISTINCTION**: Showed exception to L. Chandra Kumar rule

---

**AI JUDGE**: "Alright. Prima facie, there appears to be natural justice violation. Issue notice to respondents. Counter-affidavit to be filed in 4 weeks. List after 4 weeks."

**YOU**: "My Lord, may I request interim relief? Petitioner is suffering daily business loss of ₹10,000."

**AI JUDGE**: "What interim relief do you seek?"

**YOU**: "My Lord, interim direction to respondent to grant TEMPORARY license till petition disposal, subject to petitioner complying with all safety norms."

**AI GOVERNMENT COUNSEL**: "My Lord, liquor license cannot be granted as interim measure. Public interest involved."

**AI JUDGE**: "Interim relief REJECTED. However, respondents are directed to decide appeal under Section 25 within 30 days if petitioner files appeal. List after 4 weeks."

⚠️ **PARTIAL SUCCESS**: Writ admitted but interim relief denied

---

## PERFORMANCE REPORT

**Overall Score**: 72/100 (GOOD - B Grade)

**Strengths**:
✅ Responded well to alternative remedy objection (cited *Whirlpool* case)
✅ Distinguished opponent's case law (*L. Chandra Kumar*)
✅ Cited natural justice violation (*Maneka Gandhi*, *Mohammad Nooh*)
✅ Requested interim relief (shows litigation awareness)

**Weaknesses**:
⚠️ Could have ANTICIPATED alternative remedy objection in opening (pre-emptively addressed)
⚠️ Interim relief request was weak (temporary license unlikely in liquor cases - public interest)
⚠️ Could have cited *Harinagar Sugar Mills v. Shyam Sunder* (1961) - natural justice in licensing

**Success Probability**: 50%

**Why Uncertain**: Writ admitted (good), but judge seems inclined to direct petitioner to exhaust appeal first. Outcome depends on strength of natural justice argument.

**Recommended Practice**:
1. Practice anticipating procedural objections (alternative remedy, locus standi, delay)
2. Study more constitutional law cases (writ petitions are heavily case-law dependent)
3. Try MEDIUM difficulty next to build confidence
```

---

## Supported Practice Modes

### Mode 1: Cross-Examination Practice
**Focus**: Question opposing party's witnesses
- Hostile witness (defensive, evasive)
- Expert witness (technical testimony)
- Eyewitness (fact testimony)

### Mode 2: Examination-in-Chief Practice
**Focus**: Elicit testimony from your own witness
- Leading question detection (AI judge sustains objections)
- Smooth testimony flow
- Document marking (Exhibit A, B, C)

### Mode 3: Argument Practice
**Focus**: Opening statements, final arguments, rebuttals
- 2-minute opening (hook + roadmap + theme)
- 10-minute final arguments (IRAC structure)
- 3-minute rebuttal (respond to opponent's points)

### Mode 4: Objection Handling
**Focus**: Make and respond to objections
- Common objections: Hearsay, Leading, Irrelevant, Argumentative
- When to object vs when to let it go
- How to phrase objections ("Objection, Your Honour. [Reason].")

### Mode 5: Settlement Negotiation
**Focus**: Mediation, conciliation practice
- Opening position, reservation price
- Concessions strategy (what to give, what to get)
- Deadlock resolution

---

## Court Types Supported

| Court Type | Formality | Judge Style | Opposing Counsel | Success Metric |
|------------|-----------|-------------|------------------|----------------|
| **Labour Court** | Moderate | Patient, pro-worker | Employer's lawyer (attacks credibility) | Reinstatement granted |
| **Consumer Forum** | Semi-formal | Pro-consumer | Company's lawyer (claims no deficiency) | Compensation awarded |
| **Civil Court** | Formal | Neutral | Defendant's lawyer (denies liability) | Decree passed |
| **High Court (Writ)** | Very formal | Strict, interventionist | Government's lawyer (technical objections) | Notice issued |
| **Criminal Court** | Very formal | Cautious (liberty issues) | Public Prosecutor (proves guilt) | Bail granted / Acquittal |

---

## Protocols Utilized

- `IL-LABOUR-INDUSTRIAL-DISPUTES.md` (labour court practice)
- `IL-CONSUMER-PROTECTION-ACT.md` (consumer forum practice)
- `IL-CPC-TRIAL-PROCEDURE.md` (civil court practice)
- `CIVIC-WRIT-BASICS.md`, `CIVIC-WRIT-TYPES.md` (writ petition practice)
- `IL-CRPC-TRIAL-PROCEDURE.md` (criminal court practice)

## Agent Utilized

- `mock-court-simulator` (AI judge + opposing counsel + witnesses)

## Skills Utilized

- `court-etiquette-guide` (court-specific behavior)
- `argument-analyzer` (performance feedback)
- `evidence_evaluator` (evidence admissibility)

---

**Version**: 1.0
**Last Updated**: December 2025
**Coverage**: ALL litigation domains (Labour, Consumer, Civil, Writ, Criminal, Property)
**Replaces**: `/practice-labour-case` (deprecated - use this universal command instead)
