---
description: Assess viability of filing Public Interest Litigation (PIL) for social justice causes, environmental protection, corruption exposure, or enforcement of diffused/collective rights. Evaluates bonafide intent, public interest element, evidence strength, and strategic litigation approach.
---

# /pil-viability - Public Interest Litigation Assessment

## Command Purpose
Assess viability of filing Public Interest Litigation (PIL) for social justice causes, environmental protection, corruption exposure, or enforcement of diffused/collective rights. Evaluates bonafide intent, public interest element, evidence strength, and strategic litigation approach.

## How It Works
This command invokes the `pil-environmental-specialist` agent to:
1. Distinguish PIL from private writ (public vs. individual interest)
2. Assess petitioner's bonafide intent and credibility
3. Evaluate public interest magnitude
4. Recommend PIL vs. alternative remedies (SPCB, NGT, RTI, etc.)
5. Provide evidence gathering strategy
6. Assess likelihood of admission and success

## When to Use
- **Environmental violations** (pollution, illegal construction in forests, mining)
- **Rights of marginalized groups** (slum dwellers, bonded laborers, prisoners, tribals)
- **Corruption in public projects** (tender irregularities, misuse of public funds)
- **Systemic violations** (government school infrastructure, public health, sanitation)
- **Government inaction** affecting large population
- **Transparency** issues (denial of public information systemically)

## When NOT to Use (Private Writ, Not PIL)
- Your own passport delay (personal issue)
- Your property dispute (private matter)
- Your employment termination (service matter - CAT)
- Single individual affected (not public/large group)

## Usage

```
/pil-viability
```

OR with cause context:

```
/pil-viability Industrial pollution affecting entire village
```

```
/pil-viability Government schools lack toilets for girl students across district
```

## Workflow

When you invoke `/pil-viability`, I will:

### Step 1: Issue Classification - PIL or Private Remedy?

I'll ask you targeted questions:

**Q1: What is the issue?**
- Describe the problem/violation

**Q2: Who is affected?**
- Just you (individual)?
- Large section of public / Community / Marginalized group?
- How many people affected? (Approx.)

**Q3: Can affected persons approach court themselves?**
- Are they poor, illiterate, fearful of retaliation?
- OR they can but haven't (raises question - why PIL needed?)

**Q4: Why are YOU filing (if you're not personally affected)?**
- Are you an NGO working in this field?
- Public-spirited citizen with credibility?
- What's your interest in this cause?

**Classification Output**:
```
**PIL Appropriate**: [Yes / No / Borderline]

**Reasoning**:
- [Issue affects X people / large public / marginalized group]
- [Affected persons unable to approach court because: poverty/fear/illiteracy]
- [You have bonafide interest as: NGO/activist/affected person representing group]

OR

- [This is individual issue, not public - Recommend private writ/consumer complaint]
- [You appear to be busybody / have vested interest - PIL likely to be dismissed]
```

### Step 2: Bonafide Intent Assessment

Critical for PIL admission. Courts dismiss publicity PILs, politician PILs, busybody PILs.

I'll assess:

**Bonafide Indicators** (Strong PIL):
- NGO with track record in relevant field (education NGO for school PIL, environmental NGO for pollution PIL)
- Journalist/activist exposing violations
- Affected person representing larger affected group
- No vested interest (not competitor filing against rival's project)
- Genuine public welfare motive

**Red Flags** (Weak PIL - Likely Dismissal):
- Politician seeking publicity
- Lawyer offering to withdraw if engaged
- Person with no connection to issue (busybody)
- Competitor masking private rivalry as PIL
- First-time filer with no credibility in field

**Assessment Output**:
```
**Bonafide Assessment**: [Strong / Moderate / Weak]

**Strengths**:
- [You are NGO working in education for 10 years - credible]
- [You are affected villager representing 500 families - genuine]

OR

**Weaknesses / Red Flags**:
- [You have no prior engagement in this cause - why now?]
- [This appears to be private business rivalry, not public interest]

**Admission Likelihood on Bonafide**: [High / Moderate / Low]
```

### Step 3: Public Interest Magnitude Assessment

**How significant is the public interest?**

I'll analyze:

**Strong Public Interest**:
- Affects large population (thousands, entire village/district)
- Concerns fundamental rights (Article 21 - life, health, clean environment)
- Systemic violation (not isolated incident)
- Public funds misuse (taxpayer money wasted)

**Moderate Public Interest**:
- Affects moderate number (hundreds)
- Local issue (one locality, one institution)
- Important but not life-threatening

**Weak Public Interest**:
- Affects few people (could file individually)
- Private dispute in disguise
- Not of public importance

**Assessment Output**:
```
**Public Interest Magnitude**: [High / Moderate / Low]

**Analysis**:
- **Affected Population**: [500 families / Entire district / 50 students]
- **Nature of Right**: [Fundamental right (Article 21 - health from pollution) / Statutory right (education)]
- **Systemic vs. Isolated**: [Systemic - affects all government schools in district / Isolated - one school]

**Public Importance Score**: [Strong case for PIL / Moderate - borderline / Weak - private remedy better]
```

### Step 4: Evidence Assessment

PIL succeeds on STRONG EVIDENCE, not just allegations.

I'll guide you on evidence needed:

**Essential Evidence for Environmental PIL**:
- **Ground Reality**: Photos/videos of pollution, illegal activity (timestamped, geotagged)
- **Government Data**: RTI responses showing violations, inspection reports
- **Expert Reports**: Pollution test results (SPCB or independent lab), health impact studies
- **Affected Persons**: Affidavits from villagers, medical reports
- **Statutory Violations**: Cite specific law/rule violated (EPA, Forest Act, EIA Notification)

**Essential Evidence for Corruption PIL**:
- **RTI Responses**: Tender documents, contract details
- **Comparison**: Show irregularities (lowest bidder not selected, inflated rates, etc.)
- **Media Reports**: News coverage of alleged corruption
- **Whistleblower Documents**: If available

**Essential Evidence for Social Justice PIL** (Education, Health, Sanitation):
- **Inspection**: Photos of school without toilets, hospital without doctors, garbage accumulation
- **RTI Data**: Budget allocated vs. actual spending, beneficiary lists
- **Comparative**: Violations of Citizens Charter, government norms
- **Affected Persons**: Affidavits, testimonials

**Evidence Strength Output**:
```
**Evidence Currently Available**: [List what you have]

**Evidence Gaps**: [What's missing]

**Evidence Gathering Strategy**:
1. **RTI**: File RTI to [Department] for [specific information]
2. **Ground Documentation**: [Photos needed of X, Y]
3. **Expert Reports**: [If pollution, get water/air samples tested]
4. **Affected Persons**: [Collect affidavits from X number of people]

**Evidence Strength for PIL**: [Strong - Ready to file / Moderate - Need more evidence / Weak - Insufficient for PIL]

**Timeline to Gather Evidence**: [2 weeks for RTI + documentation / 1-2 months for expert reports]
```

### Step 5: Alternative Remedies Assessment

PIL is **extraordinary remedy**. Courts prefer petitioner exhaust alternative remedies first.

I'll recommend whether to pursue alternatives before PIL:

**For Environmental Pollution**:
- **Alternative**: Complaint to SPCB → RTI if SPCB inactive → NGT Application
- **When PIL Instead**: If SPCB systemically inactive, need HC's comprehensive directions, or NGT jurisdiction doesn't cover

**For Government Service Deficiency**:
- **Alternative**: CPGRAMS grievance → RTI → Departmental escalation
- **When PIL Instead**: If systemic (affects large population), department unresponsive to grievances

**For Corruption**:
- **Alternative**: Complaint to CVC/Lokayukta → RTI for information
- **When PIL Instead**: If corruption systemic, need judicial investigation/monitoring

**Recommendation Output**:
```
**Alternative Remedies Available**:
1. [SPCB complaint for pollution]
2. [NGT application (faster than PIL, specialized environmental forum)]
3. [RTI to gather evidence]

**Should Alternatives Be Exhausted First?**: [Yes / No / Parallel Track]

**Strategic Recommendation**:
- [If Yes: File SPCB complaint → Wait 1-2 months → If no action, then PIL]
- [If No: Direct PIL because... (systemic issue / alternative inadequate / urgency)]
- [If Parallel: File SPCB complaint + RTI + Prepare PIL simultaneously]

**PIL Timing**: [File immediately / After exhausting alternatives / After gathering more evidence]
```

### Step 6: PIL Strategy & Relief

I'll provide PIL filing strategy:

**Forum Selection**:
- **High Court** (Article 226): Local/state issue, faster, cheaper
- **Supreme Court** (Article 32): National importance, policy-level violation

**Relief to Seek in PIL**:
Based on your issue, I'll recommend appropriate prayers:

**Environmental PIL**:
1. Direct SPCB to inspect and take action
2. Close polluting factory till compliance
3. Appoint expert committee (pollution assessment)
4. Compensation to affected villagers (Polluter Pays Principle)
5. Monitoring committee

**Corruption PIL**:
1. Direct CBI/ACB investigation
2. Audit of project expenditure
3. Blacklist erring contractors
4. Recover misused public funds

**Social Justice PIL** (Education, Health):
1. Direct government to provide infrastructure (toilets, doctors, etc.)
2. Allocate budget for deficiencies
3. Monitoring committee (government + NGO + experts)
4. Periodic compliance reports

**Strategic Guidance Output**:
```
**Recommended Forum**: [High Court of [State] / Supreme Court]

**PIL Prayers** (Recommended Relief):
1. [Direct [Authority] to [specific action]]
2. [Appoint fact-finding/expert committee]
3. [Compensation: ₹[amount] (Polluter Pays / for victims)]
4. [Monitoring committee (composition: [officials + NGO + experts])]
5. [Continuing jurisdiction - court monitors implementation]

**Interim Relief** (Urgent if needed):
- [Stop pollution immediately]
- [Preserve status quo (no tree-cutting, no demolition)]
- [Temporary water tanker supply (if water contamination)]

**PIL Draft Structure**: [I'll provide framework - actual drafting needs advocate]
```

### Step 7: Success Likelihood & Costs

**PIL Admission & Success Assessment**:

**Strong PIL** (70-90% admission + success):
- Clear public interest (large affected population)
- Bonafide petitioner (NGO/credible activist)
- Strong evidence (photos, RTI, expert reports)
- Systemic violation (government duty clearly not performed)
- Alternatives exhausted OR inadequate

**Moderate PIL** (40-70%):
- Public interest present but moderate scale
- Petitioner credible but not well-known
- Some evidence, needs strengthening
- Alternatives partially exhausted

**Weak PIL** (10-40% - Likely Dismissal):
- Public interest questionable (small affected group)
- Bonafide doubtful (busybody, vested interest)
- Weak evidence (only allegations)
- Alternative remedies not attempted
- Private interest masquerading as PIL

**Timeline & Costs**:
- **Filing to Admission**: 4-8 weeks (HC scrutiny - is it genuine PIL?)
- **Admission to Disposal**: 1-3 years (PIL often takes long - monitoring, multiple hearings)
- **Continuing Jurisdiction**: Some PILs monitored for 5-10+ years

**Costs**:
- **Court Fee**: Nil to ₹1,000 (PIL often low/no fee)
- **Advocate Fee**: ₹50,000 - ₹5,00,000+ (depends on PIL complexity, advocate seniority)
- **Evidence Gathering**: ₹10,000-50,000 (RTI, expert reports, documentation)
- **Total**: ₹60,000 - ₹6,00,000+

**Assessment Output**:
```
**PIL Admission Likelihood**: [High 70-90% / Moderate 40-70% / Low 10-40%]

**Success Likelihood** (if admitted): [High / Moderate / Low]

**Strengths**:
1. [Strong public interest - 500 families affected]
2. [Clear Article 21 violation]
3. [You are credible NGO]

**Weaknesses**:
1. [Need more evidence - RTI pending]
2. [Alternative remedy (SPCB) not yet attempted]

**Recommendation**:
- [If High: File PIL immediately - strong case]
- [If Moderate: Strengthen evidence (RTI, expert report), then file]
- [If Low: Reconsider - Pursue alternative remedies / Refocus as private writ if you're personally affected]

**Timeline**: 1-3 years for disposal, possible long-term monitoring

**Estimated Costs**: ₹60,000 - ₹6,00,000+ (court fee + advocate + evidence)

**Advocate Engagement**: Strongly recommended - PIL requires experienced advocate in public interest litigation
```

### Step 8: Comprehensive PIL Viability Report

I'll deliver detailed report:

```markdown
# Public Interest Litigation Viability Report

## Your Cause (Summary)
[Brief description of issue and affected population]

---

## PIL Viability Assessment

### 1. PIL vs. Private Remedy
**Classification**: [PIL Appropriate / Private Remedy Better]
**Affected**: [500 families / Entire district / Marginalized group]
**Public Interest**: [High / Moderate / Low]

### 2. Bonafide Intent
**Petitioner**: [NGO / Affected person / Activist / Politician]
**Credibility**: [Strong - 10 year track record / Moderate / Weak - no prior engagement]
**Bonafide Score**: [High / Moderate / Low]

### 3. Evidence Strength
**Available**: [Photos, RTI responses, affidavits]
**Gaps**: [Need expert report, more RTI data]
**Evidence Score**: [Strong / Moderate / Weak]

### 4. Alternative Remedies
**Available**: [SPCB, NGT, CPGRAMS, RTI]
**Recommendation**: [Exhaust first / Parallel track / Direct PIL]

### 5. PIL Strategy
**Forum**: [High Court of [State] / Supreme Court]
**Relief**: [List of prayers]
**Interim Relief**: [If urgent - stop pollution / preserve status quo]

---

## Overall Assessment

**PIL Admission Likelihood**: [70-90% High / 40-70% Moderate / 10-40% Low]

**Success Likelihood**: [High / Moderate / Low]

**Strengths**: [List]

**Weaknesses**: [List]

**RECOMMENDATION**:
[File PIL immediately / Gather more evidence first / Exhaust alternatives / Reconsider - private remedy better]

---

## Action Plan

**Immediate Next Steps**:
1. [File RTI to [Department] for [information]]
2. [Get pollution samples tested / Document ground reality]
3. [Collect affidavits from affected persons]

**Evidence Gathering Timeline**: [2 weeks / 1-2 months]

**PIL Filing Timeline**: [After evidence complete - [Month]]

**Engage Advocate**: [Experienced in PIL / Environmental law / Social justice litigation]

**Estimated Costs**: ₹60,000 - ₹6,00,000+

**Timeline to Disposal**: 1-3 years

---

**IMPORTANT NOTES**:
- PIL is for genuine public causes, not personal grievances
- Courts strictly scrutinize bonafide intent (dismiss publicity PILs)
- Strong evidence is critical - allocations alone don't suffice
- PIL often requires long-term engagement (monitoring, compliance verification)
- Consider alternative remedies (often faster than PIL)

**Related Protocols**:
- CIVIC-PIL-BASICS (PIL fundamentals, locus standi)
- CIVIC-ENVIRONMENTAL-LAW (for pollution PILs)
- CIVIC-NGT (NGT as alternative to PIL for environment)
```

---

## Example Interactions

**Example 1: Environmental PIL (Strong)**
```
User: /pil-viability Chemical factory polluting river, 500 families affected, I'm environmental NGO

Analysis:
- PIL Appropriate: Yes (large affected population)
- Bonafide: Strong (NGO credible)
- Evidence: Moderate (need water test report, RTI to SPCB)
- Alternative: File SPCB complaint first, then NGT or PIL if inactive
- Success: High (70-90%)
- Recommendation: File SPCB complaint + RTI → If no action in 60 days → NGT (faster than PIL) OR PIL to HC
```

**Example 2: Social Justice PIL (Moderate)**
```
User: /pil-viability 20 government schools in district lack toilets for girls

Analysis:
- PIL Appropriate: Yes (systemic, affects large student population)
- Bonafide: Moderate (are you NGO or individual? If individual, build credibility via RTI, media)
- Evidence: Need RTI (school-wise data), photos, girl students' affidavits
- Alternative: CPGRAMS → RTI → Then PIL
- Success: Moderate (40-70%)
- Recommendation: Gather evidence (RTI, documentation) → File PIL with strong evidence package
```

**Example 3: Weak PIL (Private Interest)**
```
User: /pil-viability My competitor got government contract unfairly, I want investigation

Analysis:
- PIL Appropriate: No (Private business rivalry, not public interest)
- Bonafide: Weak (Vested interest - you're competitor)
- Success: Very Low (10-20% - Likely dismissal as private dispute)
- Recommendation: NOT PIL. If contract irregularities exist, file representation to vigilance / Use RTI for tender details / But don't disguise private rivalry as PIL
```

---

## Disclaimer

**This assessment is for informational purposes only and does NOT constitute legal advice.**

**PIL is a powerful tool for social justice - use responsibly. Courts dismiss abuse of PIL process (publicity stunts, private interests, busybody litigation).**

**Consult experienced advocate specializing in public interest litigation before filing PIL.**

---

**Related Commands**:
- `/file-rti` - Gather evidence via RTI before PIL
- `/check-writ` - If issue is individual (not public), check private writ viability
- `/civic-query` - General civic law guidance
