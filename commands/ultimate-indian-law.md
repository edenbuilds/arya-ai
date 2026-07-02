---
description: Comprehensive Indian legal assistance command providing expert guidance across all domains of Indian law including constitutional, criminal, civil, corporate, cyber, IP, tax, family, and property law. Powered by 160+ protocols, 18 specialized agents, and integrated knowledge graph.
argument-hint: "Can government restrict my freedom of speech online?"
---

# /ultimate-indian-law Command

**Command Name**: `/ultimate-indian-law`
**Version**: 1.0.0
**Domain**: Indian Law (Complete Legal Knowledge System)
**Invokes**: indian-law-master-orchestrator

---

## Purpose

Comprehensive Indian legal assistance command providing expert guidance across all domains of Indian law including constitutional, criminal, civil, corporate, cyber, IP, tax, family, and property law. Powered by 160+ protocols, 18 specialized agents, and integrated knowledge graph.

---

## Syntax

```bash
/ultimate-indian-law [query] [options]
```

---

## Parameters

### Required
- `[query]`: Legal question, case analysis request, or procedural guidance needed

### Optional Flags

**Domain Specification**:
- `--domain <domain>`: Direct routing to specific legal domain
  - Options: `constitutional` `criminal` `civil` `corporate` `cyber` `ip` `tax` `family` `property`
  - Example: `/ultimate-indian-law "Can FIR be quashed?" --domain criminal`

**Jurisdiction**:
- `--jurisdiction <court>`: Specify applicable jurisdiction
  - Options: `supreme-court` `delhi-hc` `bombay-hc` `madras-hc` `calcutta-hc` etc.
  - Example: `/ultimate-indian-law "Patent infringement remedy" --jurisdiction delhi-hc`

**Temporal Context**:
- `--law-version <old|new>`: Specify old (IPC/Evidence Act) vs. new (BNS/BSA) law
  - Options: `old` `new` `both`
  - Default: Auto-detect based on context
  - Example: `/ultimate-indian-law "Section 420 punishment" --law-version old`

**Output Format**:
- `--format <type>`: Desired output format
  - Options: `summary` `detailed` `step-by-step` `comparison`
  - Default: `detailed`
  - Example: `/ultimate-indian-law "How to file writ petition" --format step-by-step`

**Case Analysis**:
- `--analyze-case`: Request comprehensive case analysis
  - Includes: Facts, issues, applicable law, precedents, strategy
  - Example: `/ultimate-indian-law "Client arrested for fraud" --analyze-case`

**Multi-Domain**:
- `--multi-domain`: Force multi-domain analysis
  - Useful when query spans multiple areas
  - Example: `/ultimate-indian-law "Director liability in company fraud" --multi-domain`

---

## Usage Examples

### Example 1: Constitutional Rights Query
```bash
/ultimate-indian-law "Can government restrict my freedom of speech online?"
```

**Process**:
1. Routes to: constitutional-law-specialist + cyber-law-specialist
2. Analyzes: Article 19(1)(a), Article 19(2), IT Act Section 69A
3. Provides: Comprehensive answer on constitutional limits + IT Act provisions

**Output**:
```
LEGAL ANALYSIS - Constitutional & Cyber Law

Domain: Constitutional Law (Article 19) + Cyber Law (IT Act)
Applicable Law: Constitution Article 19, IT Act Section 69A

Summary:
Government can impose reasonable restrictions on freedom of speech under Article 19(2)
on grounds of sovereignty, security, public order, decency, morality, contempt of court,
defamation, or incitement. IT Act Section 69A allows content blocking with due process.

[Detailed analysis follows...]
```

---

### Example 2: Criminal Procedure Question
```bash
/ultimate-indian-law "What is the procedure for filing FIR?" --format step-by-step
```

**Process**:
1. Routes to: criminal-procedure-specialist
2. Retrieves: Section 154 CrPC protocol
3. Formats: Step-by-step procedural guidance

**Output**:
```
STEP-BY-STEP: Filing FIR under Section 154 CrPC

Step 1: Visit Police Station
- Go to police station having jurisdiction over offense location
- Cognizable offense can be reported at any police station (Section 156)

Step 2: Provide Information
- Give oral or written information about cognizable offense
- Information can be given by anyone (not just victim)

[Steps 3-8 continue...]
```

---

### Example 3: Multi-Domain Corporate-Criminal Query
```bash
/ultimate-indian-law "Our company director was arrested for cheating customers. What are the implications?" --multi-domain --analyze-case
```

**Process**:
1. Routes to: criminal-law-specialist, criminal-procedure-specialist, corporate-law-specialist
2. Analyzes:
   - Criminal liability (IPC/BNS cheating provisions)
   - Arrest and bail procedures
   - Director disqualification (Companies Act Section 164)
   - Company reputation and ongoing contracts

**Output**:
```
COMPREHENSIVE CASE ANALYSIS - Criminal + Corporate Law

FACTS ANALYSIS:
- Director arrested for cheating under IPC Section 420 / BNS equivalent
- Criminal proceedings initiated
- Company facing reputational risk

LEGAL ISSUES:
1. Criminal liability of director
2. Bail and procedural rights
3. Director disqualification under Companies Act
4. Company's ability to continue operations

APPLICABLE LAW:
Criminal: IPC/BNS Section 420 (Cheating), CrPC arrest/bail provisions
Corporate: Companies Act Section 164 (Disqualification)

[Detailed multi-domain analysis continues...]
```

---

### Example 4: Transitional Law Query
```bash
/ultimate-indian-law "I was charged under IPC Section 379 in June 2024. Will I be tried under BNS now?" --law-version both
```

**Process**:
1. Identifies: Transitional provisions question
2. Routes to: criminal-law-specialist with temporal analysis
3. Compares: IPC (old) vs. BNS (new) application

**Output**:
```
TRANSITIONAL LAW ANALYSIS - IPC to BNS

Your Situation:
- Offense date: June 2024 (before BNS effective date July 1, 2024)
- Charged under: IPC Section 379 (Theft)
- BNS Status: Effective from July 1, 2024

ANSWER: You will be tried under IPC Section 379, NOT BNS.

Reason:
Per transitional provisions, offenses committed before July 1, 2024 continue
to be governed by IPC and prosecuted under old law, even though BNS is now
in force.

[Detailed transitional analysis continues...]
```

---

### Example 5: Data Protection Compliance
```bash
/ultimate-indian-law "How do I ensure DPDP Act 2023 compliance for my startup?" --domain cyber --format detailed
```

**Process**:
1. Routes to: cyber-law-specialist
2. Analyzes: DPDP Act 2023 requirements
3. Provides: Compliance checklist and implementation guidance

**Output**:
```
DPDP ACT 2023 COMPLIANCE GUIDE - Startups

[Comprehensive compliance framework with data fiduciary obligations,
consent mechanisms, data principal rights, technical measures, etc.]
```

---

## Output Structure

### Standard Format

```markdown
## LEGAL ANALYSIS

**Domain**: [Legal domains involved]
**Applicable Law**: [Statutes + Sections]
**Jurisdiction**: [SC / Specific HC / All India]
**Query Type**: [Advisory / Procedural / Litigation / Compliance]

### Summary
[2-3 sentence executive summary]

### Detailed Analysis
[Comprehensive legal analysis with subsections]

### Relevant Statutory Provisions
- [Statute, Section]: [Brief description]
- [Statute, Section]: [Brief description]

### Applicable Case Law
- [Case citation]: [Principle established]
- [Case citation]: [Principle established]

### Practical Guidance
[Step-by-step actionable advice]

### Important Considerations
- [Critical points, deadlines, risks]
- [Procedural requirements]
- [Documentation needed]

### Next Steps
1. [Immediate action]
2. [Short-term action]
3. [Long-term strategy]

---

**Agents Consulted**: [Sub-agents used]
**Protocols Referenced**: [Protocol IDs]
**Sources**: [Statutes, judgments, authorities]
**Last Updated**: [Date]
**Confidence Level**: [High / Medium / Low - based on clarity of law]
```

---

## Capabilities Matrix

| Legal Domain | Agent | Sample Queries |
|-------------|-------|----------------|
| **Constitutional Law** | constitutional-law-specialist | Fundamental rights, writ petitions, constitutional validity |
| **Supreme Court Practice** | supreme-court-litigation-specialist | SLPs, appeals, constitutional benches |
| **Public Interest Litigation** | public-interest-litigation-specialist | PIL filing, locus standi, social justice |
| **Criminal Law (Substantive)** | criminal-law-specialist | IPC/BNS offenses, defenses, liability |
| **Criminal Procedure** | criminal-procedure-specialist | FIR, investigation, trial, bail, appeals |
| **Criminal Defense** | criminal-defense-strategist | Defense strategies, evidence, cross-examination |
| **Civil Procedure** | civil-procedure-specialist | Suits, appeals, injunctions, execution |
| **Contract Law** | contract-law-specialist | Formation, breach, remedies, specific performance |
| **Tort Law** | tort-law-specialist | Negligence, defamation, consumer protection |
| **Corporate Law** | corporate-law-specialist | Companies Act, governance, M&A, compliance |
| **Insolvency** | insolvency-resolution-specialist | IBC, NCLT, resolution, liquidation |
| **Commercial Disputes** | commercial-litigation-specialist | Arbitration, commercial recovery |
| **Property Law** | property-law-specialist | Transfer, registration, title, disputes |
| **Family Law** | family-law-specialist | Marriage, divorce, custody, succession |
| **Cyber Law** | cyber-law-specialist | IT Act, DPDP Act, cybercrimes, data protection |
| **Intellectual Property** | intellectual-property-specialist | Patents, trademarks, copyright, enforcement |
| **Tax Law** | tax-law-specialist | Income tax, GST, tax litigation |
| **Labor & Employment** | labor-employment-law-specialist | Labor laws, employment contracts, disputes |

---

## Knowledge Base

### Protocols
- **160+ protocols** across all Indian law domains
- Regular updates tracking Supreme Court and High Court judgments
- Transitional protocols for IPC→BNS, Evidence Act→BSA

### Statute Coverage
- Constitution of India (complete)
- IPC 1860 + BNS 2023/2024
- CrPC 1973 + BNSS 2023/2024 (when effective)
- Indian Contract Act 1872
- Evidence Act 1872 + BSA 2023/2024
- CPC 1908
- Companies Act 2013
- IBC 2016
- IT Act 2000 + DPDP Act 2023
- All major commercial, tax, IP, property, family law statutes

### Case Law
- Supreme Court judgments (1950-2024)
- High Court precedents (24 High Courts)
- Integrated via Indian Kanoon database

---

## Best Practices

### For Users
1. **Be specific** in queries - mention jurisdiction, time period, specific facts
2. **Use flags** to direct routing and output format
3. **Request multi-domain analysis** when query spans multiple areas
4. **Mention urgency** if time-sensitive (bail, injunction)
5. **Provide context** - pending litigation, advisory, compliance, etc.

### For Complex Matters
1. Break down into sub-queries if needed
2. Request step-by-step procedural guidance
3. Ask for case law analysis
4. Request comparison between old and new law
5. Seek practical timelines and documentation requirements

---

## Limitations & Disclaimers

⚠️ **This is NOT a substitute for professional legal advice from a qualified lawyer**

**Limitations**:
- General guidance based on statutes and precedents
- Cannot account for all factual nuances of specific cases
- State-specific variations may exist
- Recent judgments (within last week) may not be reflected
- Does not constitute attorney-client relationship

**Always Consult**:
- Qualified advocate for litigation
- Legal expert for compliance matters
- Specialist for complex transactions

---

## Update Frequency

- **Protocols**: Updated monthly
- **Case Law**: Integrated weekly from Indian Kanoon
- **Statutes**: Updated upon amendments/notifications
- **Agents**: Enhanced quarterly based on emerging legal areas

---

## Related Commands

- `/learn-domain Indian-Law`: Refresh and expand knowledge base
- `/synthesize-protocols`: Create unified protocols for specific topics

---

## Support & Feedback

For issues, improvements, or new legal domain coverage requests, please provide feedback to improve this legal knowledge system.

---

## Version History

- **v1.0.0** (2025-12-04): Initial release with 160+ protocols, 18 agents, comprehensive Indian law coverage

---

## Keywords

`indian law` `legal advice` `constitutional law` `criminal law` `civil law` `corporate law` `supreme court` `high court` `legal research` `case analysis` `statutory interpretation` `legal procedure`
