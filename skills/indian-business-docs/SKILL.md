---
name: indian-business-docs
description: >
  Draft and review common Indian legal and business documents from plain-language requirements.
  Use whenever the user needs to create, review, or understand an Indian contract or legal document:
  rental/lease agreements, NDAs, employment offer letters, founder/co-founder agreements, freelance
  or consulting contracts, vendor MSAs, DPDPA 2023 privacy notices, terms of service, cease and
  desist letters, legal notices, MoUs, or partnership deeds. Triggers on "draft a rent agreement",
  "review this NDA", "make an employment contract", "founder agreement with vesting", "privacy
  policy for my app", "is this clause fair", or when the user pastes an agreement and asks what's
  risky in it. Built for Indian law and Indian business context, not US/UK templates.
---

# Indian Legal Documents Skill

Draft and review common Indian business and legal documents. Built for the Indian legal context
(Indian Contract Act 1872, DPDPA 2023, state stamp duty rules, Indian employment norms).

**This skill produces drafts and highlights issues. It is not a substitute for a licensed advocate.**
Always tell the user to have high-stakes documents reviewed by a lawyer before signing.

---

## Core principle

Most people don't need a 40-page contract. They need a clear, enforceable document that covers the
few things that actually cause disputes. Focus on the clauses that matter, written in language a
non-lawyer can understand, and flag where professional review is genuinely needed.

---

## Workflow

### Step 1: Identify the document and gather essentials

Ask only for what you actually need. For every document you need the parties, the core commercial
terms, and the jurisdiction. Don't over-interrogate - infer sensible defaults and state them.

Minimum inputs by document type:

| Document | Must-have inputs |
|---|---|
| Rent/Lease agreement | Landlord, tenant, property address, rent, deposit, term, city (for stamp duty) |
| NDA | Disclosing party, receiving party, purpose, mutual or one-way, duration |
| Employment offer | Employer, employee, role, CTC, joining date, notice period, location |
| Founder agreement | Founders, equity split, vesting schedule, roles, IP assignment |
| Freelance/consulting | Client, contractor, scope, fee, payment terms, IP ownership |
| Privacy notice (DPDPA) | Entity name, data collected, purpose, contact for grievances |

### Step 2: Draft using the clause library

Every document should include the essential clauses for its type (see references/clause-library.md).
Use plain English. Number clauses. Keep sentences short.

### Step 3: Flag the risk points

After drafting, add a short "Points to review" section that flags:
- Any blank the user must fill (stamp duty amount, specific dates)
- Any clause that is commercially significant and worth negotiating
- Any place where a lawyer's review is genuinely warranted
- Stamp duty and registration requirements for that state

---

## Document standards for India

**Stamp duty:** Most agreements need stamping to be admissible as evidence. Rates vary by state.
Rent agreements over 11 months usually require registration. Always flag this - never claim a
document is "ready to sign" without noting stamping/registration needs.

**Governing law and jurisdiction:** Default to Indian law with courts of a specific city having
jurisdiction. Ask which city if unclear.

**Notice period:** Indian employment norm is 30-90 days for salaried roles. Probation typically
3-6 months.

**Vesting (founder/ESOP):** Standard is 4-year vesting with a 1-year cliff. Flag if the user
proposes something unusual.

**DPDPA 2023:** India's Digital Personal Data Protection Act. Any app/website collecting personal
data of Indian users needs a privacy notice covering: what data, why, how long, user rights
(access, correction, erasure, grievance redressal), and Data Protection Officer / grievance
contact. This is now legally required, not optional.

**Non-compete:** Post-employment non-competes are largely unenforceable in India (Section 27,
Indian Contract Act). Non-solicitation and confidentiality survive; blanket non-competes usually
don't. Flag this if a user asks for one - don't draft something unenforceable and call it protection.

---

## Review mode

When the user pastes an existing document and asks you to review it, structure your response:

```
## Summary
[2-3 sentences: what this document is and its overall fairness]

## Red flags (things that could hurt you)
[Specific clauses that are one-sided, missing, or risky - quote the clause number]

## Missing clauses
[Standard protections that should be here but aren't]

## Negotiation points
[Where you have leverage to ask for better terms]

## Get a lawyer for
[The specific parts where professional review is genuinely worth the money]
```

Be direct about who a clause favours. If a contract is heavily one-sided against the user, say so
plainly. People paste contracts because they want honesty, not reassurance.

---

## Hard rules

- Never claim a document is legally bulletproof or guaranteed enforceable. Indian courts interpret
  facts case by case.
- Always flag stamp duty and registration requirements.
- For anything involving significant money, property, or equity, explicitly recommend a licensed
  advocate review before signing.
- Never draft something designed to deceive or defraud a counterparty.
- Don't invent specific statutory section numbers unless certain - describe the legal principle instead.

---

## Reference files

- `references/clause-library.md` - Standard clauses for each document type, ready to adapt
- `references/stamp-duty-guide.md` - State-wise stamp duty and registration overview


---

Vendored from mnbresearch/mnb-claude-skills (`indian-legal-docs`), MIT licence, see `LICENSE.txt`. For court pleadings use `indian-legal-drafting` or `maharashtra-courts-drafting` instead; run `ai-practice-safeguards` before anything leaves the chambers.
