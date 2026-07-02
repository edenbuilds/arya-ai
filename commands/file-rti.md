---
description: file rti
---

# /file-rti - RTI Application Assistant

## Command Purpose
Interactive RTI (Right to Information) application assistant that guides users through filing RTI applications under RTI Act 2005, drafts complete applications, and provides submission guidance.

## How It Works
This command launches an interactive workflow that:
1. Asks targeted questions to understand information needs
2. Helps refine vague requests into specific information points
3. Identifies correct Public Information Officer (PIO)
4. Drafts complete RTI application using `rti-application-drafter` skill
5. Provides submission instructions and follow-up timeline

## When to Use
- Filing RTI to Central/State Government departments
- Seeking information from PSUs, local bodies
- Following up on applications/services
- Gathering evidence for litigation (writ, consumer complaint, PIL)
- Transparency/accountability on government decisions

## Usage

```
/file-rti
```

OR with topic context:

```
/file-rti property tax assessment details
```

```
/file-rti passport application status
```

## Workflow

When you invoke `/file-rti`, I will:

### Step 1: Understand Your Information Need

I'll ask you:

**Q1: What information do you need?**
- What topic/subject? (e.g., government tender, scheme beneficiaries, approval orders, etc.)
- Why do you need it? (Helps refine request)

**Q2: From which public authority?**
- Central Government ministry/department?
- State Government department?
- PSU (ONGC, LIC, Railways, etc.)?
- Local body (municipality, panchayat)?

**Q3: Timeframe?**
- Specific period (FY 2023-24, Jan-Dec 2023)?
- Current status (as on date)?
- Specific date/event?

### Step 2: Refine Information Request

I'll help you make your request **SPECIFIC** (critical for RTI success):

**If your request is vague**, I'll suggest specific information points:

Example:
- ❌ You: "Information about X scheme"
- ✅ I suggest: "Number of beneficiaries of X scheme in [district] during [year], total amount disbursed, selection criteria applied"

### Step 3: PIO Identification

I'll identify the correct Public Information Officer:
- Check department/ministry responsible
- Provide PIO address (if available in knowledge base)
- If unknown, guide you to find PIO on department website

### Step 4: Additional Parameters

I'll ask:

**Q4: Are you a BPL (Below Poverty Line) applicant?**
- If YES → Fee exempted (need to attach BPL certificate)
- If NO → ₹10 fee (Central) or state-specific fee

**Q5: Does this concern life or liberty?**
- If YES → 48-hour response timeline (Section 7(1) proviso)
- If NO → Standard 30-day timeline

**Q6: How do you want information?**
- Certified copies (default)
- Photocopies
- Inspection of records
- Electronic form (email/CD)

### Step 5: Draft RTI Application

I'll invoke the `rti-application-drafter` skill to generate your complete RTI application with:
- Specific information points (numbered)
- Correct PIO address
- Fee clause (with exemption if BPL)
- Timeline invocation (30 days or 48 hours)
- Section 6(3) transfer clause (if PIO not correct)
- Section 11 third-party clause (if applicable)

### Step 6: Submission Guidance

I'll provide you with:

**Submission Checklist**:
- [ ] Print and sign RTI application
- [ ] Attach fee (IPO/DD/Stamp) OR BPL certificate
- [ ] Address envelope to PIO
- [ ] Send by Registered Post / Submit in person
- [ ] **KEEP COPY + POSTAL RECEIPT** (critical for appeals)

**Timeline Tracker**:
- Day 0: Submit RTI
- Day 30 (or 48 hrs): PIO must respond
- Day 31-45: File First Appeal if no response
- Day 60: FAA must decide appeal

**Follow-Up Actions**:
- Week 2-3: Check status (if online RTI portal available)
- Day 30: If no response, file First Appeal
- Day 60: If FAA doesn't respond, file Second Appeal to CIC/SIC

**Appeal Format** (for reference if needed later):
I'll also provide sample First Appeal format so you're prepared if PIO denies/delays.

## Example Interaction

```
User: /file-rti