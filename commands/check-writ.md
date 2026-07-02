---
description: Comprehensive writ petition viability analysis tool that assesses whether filing a writ petition (mandamus, certiorari, prohibition, habeas corpus, quo warranto) under Article 226 (High Court) or Article 32 (Supreme Court) is appropriate for your case.
---

# /check-writ - Writ Petition Viability Checker

## Command Purpose
Comprehensive writ petition viability analysis tool that assesses whether filing a writ petition (mandamus, certiorari, prohibition, habeas corpus, quo warranto) under Article 226 (High Court) or Article 32 (Supreme Court) is appropriate for your case.

## How It Works
This command launches the `writ-petition-analyzer` skill through an interactive Q&A session that systematically evaluates:
1. Whether respondent is "State" (Article 12)
2. Your locus standi (standing to file)
3. Alternative remedy requirements
4. Grounds for judicial review
5. Appropriate writ type
6. Likelihood of success
7. Strategic recommendations

## When to Use
- Government authority denied your application/permission
- Government order you want to challenge
- Government refusing to perform mandatory duty
- Illegal detention by authorities
- Unauthorized person holding public office
- Need urgent judicial intervention against government action

## Usage

```
/check-writ
```

OR with case context:

```
/check-writ Municipality denied my building permission without valid reason
```

```
/check-writ Passport approved but not issued for 60 days
```

## Workflow

When you invoke `/check-writ`, I will conduct systematic legal analysis:

### Step 1: Case Facts Gathering

I'll ask you structured questions:

**Q1: What is the government action/inaction you want to challenge?**
- Order passed (denying permission, rejecting application, etc.)?
- Inaction (duty not performed, service not delivered)?
- Detention?
- Appointment to public office?

**Q2: Which authority is involved?**
- Central/State Government department?
- Local body (municipality, panchayat)?
- PSU, statutory corporation?
- Private entity?

**Q3: When did this happen?**
- Date of impugned order (if challenging an order)
- Date when duty should have been performed
- How long ago? (Check for laches/delay)

**Q4: What did you do before approaching court?**
- Filed application/representation?
- Pursued departmental appeal/tribunal?
- Filed RTI, CPGRAMS grievance?
- Sent legal notice?

**Q5: What relief do you seek?**
- Quash an order?
- Compel authority to do something (issue license, grant permission)?
- Declare action unconstitutional?
- Secure release (if detention)?
- Challenge office appointment?

### Step 2: Viability Analysis (7-Point Framework)

I'll analyze your case through systematic legal framework:

**Analysis 1: Respondent Classification**
- Is respondent "State" under Article 12?
- Test: Government entity / PSU with state control / Private entity?
- **Output**: Writ maintainable (if State) OR Not maintainable (if private - suggest civil suit)

**Analysis 2: Locus Standi**
- Are you directly affected (aggrieved person)?
- OR filing PIL (public interest) - bonafide assessment
- **Output**: Strong/Moderate/Weak standing

**Analysis 3: Alternative Remedy**
- Is tribunal/departmental appeal available?
- Does exception apply (jurisdictional error, natural justice violation, etc.)?
- **Output**: Exhaust remedy first OR Direct writ maintainable

**Analysis 4: Grounds for Judicial Review**
- Illegality (action beyond jurisdiction, contrary to law)
- Irrationality (arbitrary, unreasonable)
- Procedural impropriety (natural justice violated)
- Malafide (improper purpose)
- Constitutional violation (Article 14, 19, 21)
- **Output**: Strong/Moderate/Weak grounds identified

**Analysis 5: Writ Type Selection**
- **Mandamus**: If seeking to compel duty
- **Certiorari**: If seeking to quash order
- **Prohibition**: If seeking to stop ongoing proceedings
- **Habeas Corpus**: If challenging detention
- **Quo Warranto**: If challenging office appointment
- **Output**: Appropriate writ type with relief formula

**Analysis 6: Delay/Laches**
- Time elapsed since cause of action
- Risk of dismissal on delay grounds
- **Output**: Low/Moderate/High laches risk + explanation strategy

**Analysis 7: Forum Selection**
- High Court (Article 226) - for any legal right, local issues
- Supreme Court (Article 32) - only fundamental rights, national importance
- **Output**: Recommended forum with reasoning

### Step 3: Success Likelihood Assessment

I'll provide overall assessment:

**Strong Case (70-90% success likelihood)**:
- Clear statutory violation
- Mandatory duty not performed
- Natural justice violated
- Fundamental right clearly violated
- No alternative remedy

**Moderate Case (40-70% success likelihood)**:
- Arguable violation
- Some discretion involved but arbitrary
- Alternative remedy exists but exception arguable
- Some delay (explainable)

**Weak Case (10-40% success likelihood)**:
- Policy decision (court reluctant)
- Discretionary action
- Alternative remedy not exhausted
- Significant unexplained delay

### Step 4: Strategic Recommendations

I'll provide actionable strategy:

**Evidence to Gather**:
- Impugned order copy
- Correspondence with authority
- RTI responses (government's admission)
- Statutory provisions proving mandatory duty
- Similar precedents

**Procedural Strategy**:
- Direct writ OR Exhaust tribunal first?
- Seek interim relief (stay order)?
- Engage advocate (experience level needed)

**Timeline & Costs**:
- Filing to admission: 2-4 weeks
- Admission to disposal: 6 months - 3 years
- **Costs**: ₹30,000 - ₹2,50,000+ (court fee + advocate fee)

**Alternative Approaches**:
- If writ weak: RTI → Representation → Escalation → Then writ
- If alternative remedy required: Tribunal → Then writ if unsuccessful

### Step 5: Comprehensive Report

I'll deliver detailed viability report:

```markdown
# Writ Petition Viability Analysis Report

## Your Case Summary
[Brief description of your issue]

## Viability Assessment

### 1. Respondent: [State ✓ / Not State ✗]
[Analysis and reasoning]

### 2. Locus Standi: [Strong/Moderate/Weak]
[Your standing assessment]

### 3. Alternative Remedy: [Required/Not Required/Exception Applies]
[Recommendation on exhausting remedy]

### 4. Grounds for Review: [List applicable grounds]
- Illegality: [Details]
- Natural Justice: [Details]
- Article 14/21: [Details]

### 5. Appropriate Writ: [Mandamus/Certiorari/etc.]
Relief: "Issue writ of [X] directing respondent to [Y]"

### 6. Delay Analysis: [X months delay - Low/Moderate/High risk]
[Explanation strategy if delayed]

### 7. Forum: [High Court of [State] / Supreme Court]
[Reasoning for forum choice]

## Overall Assessment

**Success Likelihood**: [70-90% Strong / 40-70% Moderate / 10-40% Weak]

**Strengths**:
1. [Clear violation of law]
2. [Fundamental right engaged]

**Weaknesses**:
1. [Some delay - must explain]
2. [Discretionary element]

**Recommendation**:
[Strongly recommend writ / Viable but engage experienced advocate / Consider alternatives before writ]

## Strategic Guidance

**Evidence Needed**: [List]

**Procedural Path**: [Direct writ / Tribunal first / RTI + writ]

**Interim Relief**: [Strong/Moderate/Weak case for stay]

**Advocate Engagement**: [Strongly recommended - administrative law specialist]

**Timeline**: 6 months - 2 years

**Estimated Costs**: ₹35,000 - ₹2,50,000+

---

**NEXT STEPS**:
[If Strong: Engage advocate, gather evidence, file writ]
[If Moderate: Strengthen evidence, consider RTI for government admission, then file]
[If Weak: Pursue alternative remedies (RTI, representation, tribunal) before court]
```

## Example Interactions

**Example 1: Service Delay**
```
User: /check-writ Passport application approved 60 days ago, not issued despite approval

Analysis Output:
- Respondent: Ministry of External Affairs (State ✓)
- Standing: Aggrieved person (Strong)
- Alternative Remedy: None (no tribunal for passport delays)
- Ground: Illegality (Citizens Charter violated - 30 day timeline)
- Writ Type: Mandamus (compel issuance)
- Delay: 60 days (Low laches risk)
- Forum: High Court
- Success: Strong (70-90%)
- Recommendation: File mandamus petition immediately
```

**Example 2: Building Permission Denial**
```
User: /check-writ Municipality denied building plan approval citing vague reasons, plan complies with all bylaws

Analysis Output:
- Respondent: Municipality (State ✓)
- Standing: Aggrieved person (Strong)
- Alternative Remedy: Municipal appeal (if provided) - check state law
- Ground: Illegality (denial without valid reason), Article 14 (arbitrary)
- Writ Type: Mandamus (compel approval) / Certiorari (quash denial)
- Forum: High Court
- Success: Strong if plan complies, Moderate if discretionary element
- Recommendation: File municipal appeal first (if available), then writ if unsuccessful. OR direct writ if no appeal forum.
```

**Example 3: Weak Case**
```
User: /check-writ Government rejected my proposal for new scheme, I think it's a good idea

Analysis Output:
- Respondent: Government (State ✓)
- Standing: Weak (no legal right to have proposal accepted)
- Ground: Weak (policy decision - court won't interfere with government's discretion to accept/reject proposals)
- Success: Weak (10-20%)
- Recommendation: Writ not appropriate. This is policy/discretionary decision. Alternative: Representation to Minister, public campaign, but not legal remedy.
```

## Integration

This command integrates:
- **writ-petition-analyzer** skill (for systematic analysis)
- **admin-law-specialist** agent (for expert assessment)
- **CIVIC-WRIT-BASICS**, **CIVIC-WRIT-TYPES** protocols (for legal framework)

## Important Disclaimers

**This analysis is for informational purposes only and does NOT constitute legal advice.**

**Key Points**:
- Writ viability analysis is preliminary assessment
- Actual litigation requires qualified advocate
- Court outcomes depend on evidence, arguments, judicial discretion
- Costs and timelines are estimates (vary by case complexity, HC backlog)
- Always consult experienced advocate before filing writ petition

**Writ petitions are powerful constitutional remedies. This command ensures you approach courts only with viable cases.**

---

**Related Commands**:
- `/file-rti` - Gather evidence via RTI before filing writ
- `/pil-viability` - For public interest litigation assessment
- `/civic-query` - General civic law guidance
