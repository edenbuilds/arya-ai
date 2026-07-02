---
description: Critique legal arguments, strategies, and written submissions across ALL legal domains (labour, consumer, civil, writ, criminal, property, IP, corporate). Provides detailed feedback on structure, persuasiveness, legal accuracy, case law mastery, and logical coherence with actionable improvement suggestions.
argument-hint: [paste your argument or describe your strategy]
---

# Command: Universal Legal Argument Critique

## Purpose
Critique legal arguments, strategies, and written submissions across ALL legal domains (labour, consumer, civil, writ, criminal, property, IP, corporate). Provides detailed feedback on structure, persuasiveness, legal accuracy, case law mastery, and logical coherence with actionable improvement suggestions.

## Usage
```
/critique-lawyer [paste your argument or describe your strategy]
```

## What This Command Does

### 1. Domain Auto-Detection
Analyzes your argument to identify legal domain:
- Labour law arguments (domestic enquiry, retrenchment, statutory dues)
- Consumer law arguments (RERA, product defects, service deficiency)
- Civil law arguments (contract breach, specific performance, injunctions)
- Writ petitions (Mandamus, Certiorari, Habeas Corpus, constitutional grounds)
- Criminal defense arguments (bail, acquittal, evidence challenges)

### 2. Multi-Dimensional Evaluation
Scores argument on 5 dimensions (1-10 scale each):

**1. Structure (20% weight)**:
- IRAC framework compliance (Issue-Rule-Application-Conclusion)
- Logical flow (does each point build on previous?)
- Opening strength (hook, roadmap, theme)
- Closing impact (summary, call to action)

**2. Persuasiveness (25% weight)**:
- Rhetorical effectiveness (ethos, pathos, logos)
- Storytelling quality (narrative arc, humanizing facts)
- Emotional appeal (appropriate vs manipulative)
- Counterargument handling (anticipate and rebut opposing points)

**3. Legal Accuracy (30% weight)**:
- Statutory citations (correct section numbers, act names)
- Case law relevance (landmark vs obscure, binding vs persuasive)
- Legal principle application (does case law support your point?)
- Factual accuracy (do facts match legal claims?)

**4. Case Law Mastery (15% weight)**:
- Citation quality (party names, year, court, judgment reference)
- Ratio decidendi vs obiter dicta (binding principle vs passing remarks)
- Distinguishing adverse precedents (how well did you differentiate?)
- Precedent hierarchy (Supreme Court > High Court > Tribunal)

**5. Logical Coherence (10% weight)**:
- Premise-conclusion validity (does conclusion follow from premises?)
- Internal consistency (do your points contradict each other?)
- Evidence support (do you have facts backing each claim?)
- Fallacy detection (ad hominem, straw man, slippery slope)

### 3. Domain-Specific Standards
Applies court/tribunal-specific criteria:
- **Labour Court**: Worker-friendly interpretation, domestic enquiry compliance, statutory dues calculation accuracy
- **Consumer Forum**: Deficiency in service proof, contributory negligence rebuttal
- **High Court (Writ)**: Constitutional grounds (Articles 14, 19, 21), locus standi, alternative remedy doctrine
- **Civil Court**: Cause of action clarity, limitation period compliance, pleading specificity

### 4. Improvement Suggestions
Provides actionable feedback:
- Alternative phrasing (stronger word choices)
- Missing case law (more relevant precedents you should cite)
- Stronger transitions (connecting paragraphs logically)
- Theme development (unifying narrative thread)
- Conciseness (cut unnecessary words)

---

## Example Usage

### Example 1: Labour Court Argument Critique

**Input**:
```
/critique-lawyer

Your Honour, this is a case of gross injustice. My client worked for 8 years and was thrown out like garbage. The employer is greedy and doesn't care about workers' rights. I demand reinstatement and ₹10 lakhs compensation immediately.
```

**Output**:

```markdown
## ARGUMENT CRITIQUE REPORT

**Argument Domain Detected**: Labour Law
**Court Type**: Labour Court
**Argument Type**: Opening Statement

---

### OVERALL SCORE: 25/100 (F - FAILING)

**Grade**: F (Failing - Fundamental issues, requires extensive revision)

**Verdict**: This argument is WEAK and will likely FAIL. Major structural, legal, and persuasiveness defects.

---

### DIMENSION-WISE BREAKDOWN

**1. STRUCTURE (20%)**: Score: 2/10

**Assessment**:
❌ **No IRAC framework**: Missing Issue, Rule, Application
❌ **No legal basis stated**: No section, no case law, no statute cited
❌ **No roadmap**: Didn't tell judge what your 3 points will be
❌ **Vague relief**: "₹10 lakhs compensation" - no breakdown (PF? Gratuity? Back wages?)

**IRAC Compliance**:
- Issue: ❌ Not framed ("What is the legal question?")
- Rule: ❌ Not stated (No Section 11A ID Act, no case law)
- Application: ❌ Not done (How does law apply to facts?)
- Conclusion: ⚠️ Stated ("reinstatement") but not supported

---

**2. PERSUASIVENESS (25%)**: Score: 3/10

**Assessment**:
❌ **Excessive emotion**: "Thrown out like garbage", "greedy employer" - too emotional, lacks legal basis
❌ **No narrative**: Facts missing (When? Why? How?)
❌ **No credibility establishment**: No case law cited (establishes legal authority)
⚠️ **Pathos present but overdone**: Worker's plight mentioned but no legal grounding

**Rhetorical Devices**:
- Ethos (Credibility): ❌ None (no case law, no statutory basis)
- Pathos (Emotion): ⚠️ Present but excessive (\"garbage\", \"greedy\")
- Logos (Logic): ❌ None (no cause-effect reasoning)

**Theme**: ❌ No theme present

---

**3. LEGAL ACCURACY (30%)**: Score: 0/10

**Assessment**:
❌ **NO statutory citations**: Didn't mention Section 11A Industrial Disputes Act
❌ **NO case law**: Didn't cite *Bharat Forge v. Uttam Manohar Nakate* (2005) or any precedent
❌ **Incorrect relief**: "₹10 lakhs compensation" - not how labour law works (should be reinstatement + back wages)
❌ **No legal grounds stated**: What law was violated? (Domestic enquiry? Natural justice?)

**Missing Legal Framework**:
- Industrial Disputes Act, Section 11A (reinstatement with back wages)
- Principles of natural justice (audi alteram partem - hear other side)
- *Bharat Forge* case (landmark on domestic enquiry defects)

---

**4. CASE LAW MASTERY (15%)**: Score: 0/10

**Assessment**:
❌ **ZERO case law cited**: No precedents mentioned
❌ **No ratio decidendi**: No binding principle stated
❌ **No precedent hierarchy**: Didn't cite Supreme Court ruling (mandatory in labour cases)

**Missing Cases**:
- *Bharat Forge Co. Ltd. v. Uttam Manohar Nakate* (2005) 2 SCC 489 (defective enquiry = reinstatement)
- *Siemens Ltd. v. Union of India* (1976) (enquiry officer must be independent)
- *Workmen of Firestone Tyre v. Firestone Tyre* (1973) (burden of proof on employer)

---

**5. LOGICAL COHERENCE (10%)**: Score: 4/10

**Assessment**:
❌ **Weak premise**: "Employer is greedy" - allegation, not legal argument
❌ **No evidence support**: "8 years" mentioned but no details (appointment letter? salary slips?)
✅ **Basic logic present**: If terminated unjustly → reinstatement warranted (valid but unsupported)

**Fallacies Detected**:
- **Ad hominem**: Attacking employer's character ("greedy") instead of arguing facts
- **Appeal to emotion**: "Thrown out like garbage" (emotion overrides legal argument)

---

### STRENGTHS (Very Few)

1. ✅ **Service duration mentioned**: "8 years" is relevant (establishes workman status)
2. ✅ **Relief clearly stated**: "Reinstatement" is appropriate remedy (though ₹10L compensation is wrong)

---

### WEAKNESSES (Critical)

1. ❌ **NO LEGAL BASIS**: Didn't cite ANY law (section, act, case)
2. ❌ **EXCESSIVE EMOTION**: "Garbage", "greedy" - unprofessional, judge will ignore
3. ❌ **NO FACTS**: What happened? When? Why terminated? Was enquiry conducted?
4. ❌ **ARGUMENTATIVE TONE**: "I demand" - improper (should be "I pray" or "I respectfully submit")
5. ❌ **WRONG RELIEF**: "₹10 lakhs compensation" - labour law doesn't work this way (reinstatement + back wages calculated, not arbitrary lump sum)
6. ❌ **NO ROADMAP**: Didn't tell judge what your 3 points will be

---

### SUGGESTED IMPROVEMENTS

**COMPLETE REWRITE NEEDED**. Here's how it SHOULD be argued:

```markdown
**IMPROVED VERSION** (Score would be: 85/100):

"Your Honour, this is a reference application under Section 10A of the Industrial Disputes Act for wrongful termination.

My client, Mr. [Name], was employed as a factory worker for 8 years with an unblemished record. On [Date], he was terminated for alleged misconduct WITHOUT any domestic enquiry, in direct violation of principles of natural justice established by the Supreme Court in *Bharat Forge v. Uttam Manohar Nakate* (2005) 2 SCC 489.

I will establish THREE propositions:

**First**, NO charge sheet was issued to my client (violation of standing orders).

**Second**, NO opportunity to defend was provided (violation of audi alteram partem principle - *Maneka Gandhi v. Union of India*, 1978).

**Third**, the termination is therefore ILLEGAL and VOID, entitling my client to reinstatement with back wages.

Under Section 11A Industrial Disputes Act, when termination is found illegal, reinstatement is the rule, not the exception.

I pray for:
1. Reinstatement to service
2. Back wages: ₹25,000/month × [X months] = ₹[calculated amount]
3. Statutory dues: PF ₹4,50,000, Gratuity ₹1,15,385

Thank you, Your Honour."
```

**Why This is Better**:
✅ Cites law (Section 10A, Section 11A, *Bharat Forge*, *Maneka Gandhi*)
✅ States facts precisely (8 years service, no enquiry)
✅ Roadmap (three propositions)
✅ Professional tone (no "greedy", no "garbage")
✅ Clear relief (calculated back wages, not arbitrary ₹10L)
✅ IRAC structure (Issue: wrongful termination, Rule: Section 11A + case law, Application: no enquiry, Conclusion: reinstatement)

**Revised Score**: 85/100 ✓

---

### PRACTICE RECOMMENDATIONS

**Based on this analysis, you MUST**:
1. **Study Labour Law Basics**: Read Industrial Disputes Act 1947 (Sections 2(s), 10A, 11A, 25F)
2. **Read 5 Landmark Cases**:
   - *Bharat Forge v. Uttam Manohar Nakate* (2005)
   - *Siemens Ltd. v. Union of India* (1976)
   - *Workmen of Firestone Tyre* (1973)
   - *Maneka Gandhi v. Union of India* (1978)
   - *ECIL v. Karunakar* (1994)
3. **Practice IRAC Structure**: Every argument must have Issue → Rule → Application → Conclusion
4. **Remove Emotional Language**: Replace "garbage", "greedy" with legal terms
5. **Calculate Relief Precisely**: PF = 12% × capped salary × years, Gratuity = (Salary × 15 days × Years) / 26

**Next Practice**: Try writing final arguments again, then use `/critique-lawyer` to check improvement

---

## FINAL GRADE: F (25/100)

**Recommendation**: REJECT this argument. Complete rewrite required. Use improved version above as template.
```

---

### Example 2: Writ Petition Argument Critique (Better Quality)

**Input**:
```
/critique-lawyer

My Lord, this is a writ petition under Article 226 challenging denial of trade license by Municipal Corporation.

My client applied for license on 1st January 2024, meeting all requirements under Municipal Act Section 52. License was denied on 30th June 2024 citing "public interest" without specific reasons.

This violates Article 14 (arbitrary action) and Article 19(1)(g) (right to occupation).

I rely on *Maneka Gandhi v. Union of India* (1978) - right to be heard is part of Article 21.

I pray for writ of Mandamus directing Municipal Commissioner to grant license.
```

**Output**:

```markdown
## ARGUMENT CRITIQUE REPORT

**Argument Domain Detected**: Administrative Law (Writ Petition)
**Court Type**: High Court (Article 226)
**Argument Type**: Opening Statement

---

### OVERALL SCORE: 72/100 (B - Good, Needs Minor Improvements)

**Grade**: B (Good - Competent argument, minor improvements needed)

**Verdict**: This argument is GOOD and will likely SUCCEED, but can be strengthened with minor additions.

---

### DIMENSION-WISE BREAKDOWN

**1. STRUCTURE (20%)**: Score: 8/10

**Assessment**:
✅ **IRAC mostly present**:
  - Issue: ✅ Identified (license denial)
  - Rule: ✅ Stated (Article 14, 19(1)(g), Article 21)
  - Application: ⚠️ Weak (didn't explain HOW Articles apply)
  - Conclusion: ✅ Clear (Mandamus for license grant)
✅ **Facts stated**: Date of application, denial, reason
✅ **Relief clear**: Mandamus for license grant

**Missing**:
⚠️ No roadmap (didn't state "I will establish 3 propositions")
⚠️ No opening hook or theme

---

**2. PERSUASIVENESS (25%)**: Score: 7/10

**Assessment**:
✅ **Professional tone**: No excessive emotion, respectful
✅ **Facts organized chronologically**: Application → Denial → Grounds
⚠️ **No narrative**: Could humanize facts (e.g., "My client, a small business owner...")
⚠️ **No counterargument anticipation**: Opponent will cite "public interest" - pre-emptively rebut

**Missing**:
- Theme (e.g., "No person shall be denied livelihood without fair hearing")
- Emotional grounding (why this matters - livelihood, family)

---

**3. LEGAL ACCURACY (30%)**: Score: 7/10

**Assessment**:
✅ **Correct Articles cited**: 14 (equality), 19(1)(g) (occupation), 21 (procedure)
✅ **Mandamus appropriate**: Correct writ type (compel public duty)
✅ **Municipal Act cited**: Section 52 (statutory basis)
⚠️ **Incomplete *Maneka Gandhi* citation**: Year (1978) mentioned but no specific holding explained
⚠️ **Alternative remedy not addressed**: Did you exhaust Municipal Act appeals?

**Missing Case Law**:
- *Whirlpool Corporation v. Registrar of Trademarks* (1998) - natural justice in licensing
- *Mohinder Singh Gill v. CEC* (1978) - reasons must be given for administrative action

---

**4. CASE LAW MASTERY (15%)**: Score: 6/10

**Assessment**:
✅ **Cited *Maneka Gandhi***: Landmark constitutional case (good)
⚠️ **Incomplete citation**: Didn't explain WHAT *Maneka Gandhi* held (right to be heard)
⚠️ **Only 1 case cited**: For writ petition, should cite 2-3 cases
❌ **No ratio decidendi**: Didn't state binding principle from case

**Suggested Additional Cases**:
- *Ridge v. Baldwin* (1964) - natural justice in licensing (foreign but persuasive)
- *Maneka Gandhi* (expand): "Procedure under Article 21 must be fair, just, reasonable"
- *State of UP v. Mohammad Nooh* (1958) - no man condemned unheard

---

**5. LOGICAL COHERENCE (10%)**: Score: 8/10

**Assessment**:
✅ **Valid logic**: If (1) license eligibility + (2) arbitrary denial → Mandamus warranted
✅ **Internal consistency**: No contradictions
✅ **Evidence support**: Application date, denial date, statute section (factually grounded)
⚠️ **Weak cause-effect**: "Public interest" reason not analyzed (why is it arbitrary?)

---

### STRENGTHS

1. ✅ **Professional tone**: No excessive emotion or rhetoric
2. ✅ **Correct writ type**: Mandamus (compel public duty)
3. ✅ **Constitutional grounds**: Articles 14, 19(1)(g), 21 cited
4. ✅ **Statutory basis**: Municipal Act Section 52 referenced
5. ✅ **Case law cited**: *Maneka Gandhi* (landmark)

---

### WEAKNESSES

1. ⚠️ **Incomplete *Maneka Gandhi* citation**: State holding ("procedure must be fair + reasonable")
2. ⚠️ **No counterargument anticipation**: Opponent will argue "public interest" valid - pre-empt this
3. ⚠️ **Alternative remedy not addressed**: If Municipal Act provides appeal, writ may be dismissed
4. ⚠️ **No theme**: Add unifying thread (e.g., "Fair hearing before denying livelihood")
5. ⚠️ **Missing case law**: Add *Whirlpool*, *Mohammad Nooh* for natural justice

---

### SUGGESTED IMPROVEMENTS

**Improvement 1: Expand *Maneka Gandhi* Citation**

**Current**:
> "I rely on *Maneka Gandhi v. Union of India* (1978) - right to be heard is part of Article 21."

**Suggested**:
> "I rely on *Maneka Gandhi v. Union of India* (1978) AIR 597 SC, where the Supreme Court held that 'procedure established by law' under Article 21 must be FAIR, JUST, and REASONABLE. Right to be heard is integral. Here, license denied without hearing - violates Article 21."

**Why Better**: Explains WHAT case held + HOW it applies to facts

---

**Improvement 2: Address Alternative Remedy**

**Add before prayers**:
> "My Lord, Municipal Act does not provide appeal against license denial. Even if appeal existed, it would be inadequate because (1) Licensing Authority is part of same executive, (2) Daily business loss (₹10,000/day), (3) Appeal takes 6 months. I rely on *Whirlpool Corporation* (1998) - writ maintainable if alternative remedy inadequate."

**Why Better**: Pre-emptively handles judge's likely question

---

**Improvement 3: Rebut \"Public Interest\" Ground**

**Add after facts**:
> "My Lord, denial citing 'public interest' is VAGUE and ARBITRARY. No specific reasons given. What public interest? No local objections on record. No environmental issue. No safety concern. *Mohinder Singh Gill v. CEC* (1978) held reasons must be SPECIFIC, not general. 'Public interest' without specifics = arbitrary (violates Article 14)."

**Why Better**: Attacks weakness in opponent's case

---

**Revised Score (With Improvements)**: 88/100 (A-)

---

### PRACTICE RECOMMENDATIONS

1. **Case Law Depth**: Read 5 more natural justice cases (*Whirlpool*, *Mohammad Nooh*, *Ridge v. Baldwin*)
2. **Anticipate Objections**: Before arguing, list 3 objections opponent will make → prepare counter for each
3. **Theme Development**: Add unifying theme ("No livelihood denial without fair hearing")
4. **Conciseness**: Current argument is good length - don't expand unnecessarily

**Next Practice**: Try civil suit argument (contract breach) to test IRAC in different domain

---

## FINAL GRADE: B (72/100)

**Recommendation**: GOOD argument, likely to succeed in High Court. With suggested improvements, could reach A- (88/100).
```

---

## Protocols Utilized

- `argument-analyzer.md` (evaluation framework)
- Domain-specific protocols (auto-detected):
  - Labour: `IL-LABOUR-INDUSTRIAL-DISPUTES.md`
  - Consumer: `IL-CONSUMER-PROTECTION-ACT.md`
  - Writ: `CIVIC-WRIT-BASICS.md`, `CIVIC-WRIT-TYPES.md`
  - Civil: `IL-CPC-PLAINT.md`, `IL-CPC-TRIAL-PROCEDURE.md`
  - Criminal: `IL-CRPC-BAIL.md`, `IL-CRPC-TRIAL-PROCEDURE.md`

## Skills Utilized

- `argument-analyzer` (structure, persuasiveness, coherence evaluation)
- `evidence_evaluator` (evidence support assessment)
- Domain-specific calculators (if argument includes relief calculation)

---

**Version**: 1.0
**Last Updated**: December 2025
**Coverage**: ALL argument types across 9 legal domains
**Replaces**: N/A (new functionality - no previous equivalent)
