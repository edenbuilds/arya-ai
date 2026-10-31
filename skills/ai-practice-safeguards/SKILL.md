---
name: ai-practice-safeguards
description: Professional safeguards for using AI in Indian legal practice. Use before any AI-assisted draft, memo, opinion or letter leaves the chambers, when the user pastes client material, asks to "verify", "check before filing", "is this citation real", wants a pre-filing checklist, a matter brief, a contract review in tiers, or a devil's-advocate pass. Covers anonymisation, the five ways AI gets Indian law wrong, the pre-filing checklist, and the matter-brief format.
---

# AI practice safeguards

The advocate signs the document, so the advocate answers for every line of it. The AI having written a line is no defence. This skill sets the checks that make a draft safe to use.

## 1. Before any client material goes in

- Replace names, addresses, phone numbers, PAN/Aadhaar/CIN/DIN, account numbers, FIR and case numbers with role placeholders (`Client A`, `Builder X`, `[FIR-1]`). Keep the key on the advocate's machine. The drafting pipeline's Reader stage does this for pleadings.
- Real identifiers go back in only at the final local render (`save_draft_as_docx`).
- If the client has not agreed to AI-assisted work, say so and suggest a line for the engagement letter. Client confidentiality duties under the Advocates Act, 1961 and the BCI Rules apply. Under the DPDPA, 2023 the chambers is the data fiduciary for client data. [VERIFY: current BCI guidance and DPDP Rules notification status]

## 2. Five ways AI gets Indian law wrong

| Failure | Guard while drafting | Check before use |
|---|---|---|
| Invented case | State the principle without a case name unless the case was supplied or verified. Never complete a half-remembered citation. | Find the judgment on Indian Kanoon / SCC Online / Manupatra, read the paragraph relied on, check it is not overruled, note the bench strength. |
| Wrong section | Quote the opening words of the section next to the number. | Match against India Code (indiacode.nic.in), "as amended" version. |
| Superseded law | Say which code applies. Offences and procedure on or after 1 July 2024 are BNS / BNSS / BSA. Earlier ones stay IPC / CrPC / IEA. Labour Codes: confirm the state and industry notification. | Check commencement and transition provisions for the trigger date. |
| Foreign rule passed off as Indian | Apply Indian law and flag where it differs from UK/US. A post-employment non-compete is void under s.27 Contract Act, 1872. | Ask whether an Indian authority actually says this. |
| Confident wrong figure | Put `[VERIFY: source]` against every rate, fee, threshold, limitation period and interest figure. | Court-fees schedule of the state, Limitation Act article, SBI MCLR on the date, forum's pecuniary notification. |

Add this to any drafting instruction: *"Do not invent case names, citations, section numbers, dates, fees or figures. Where unsure, write the principle and mark [VERIFY]."*

Use `legal-citation-validator` for format checks. It cannot prove a judgment exists. Only a database search does that.

## 3. Pre-filing checklist

Run it on every AI-assisted document before it is filed, sent or signed. Report each line as PASS, FAIL or OPEN.

**Citations**
- Every case found in a database. Its holding read, not just the headnote.
- Citation format right: (Year) Vol SCC Page / AIR / SCR. Bench strength noted.
- Not overruled or doubted by a larger bench.
- No authority the draft hedges on ("I believe", "approximately").

**Statutes**
- Every section checked against the official text.
- Correct code for the trigger date (BNS/BNSS/BSA vs IPC/CrPC/IEA).
- State law right for the state: rent, shops and establishments, stamp, court fees. In Maharashtra that means the Maharashtra Stamp Act, 1958 and the Bombay Court-Fees Act, 1959.

**Figures and time**
- Limitation: right article, trigger date, computation shown, condonation needed or not.
- Statutory windows recomputed by hand, e.g. NI Act s.138: return memo, then the demand notice, then the payment period, then the complaint window. [VERIFY each against the section]
- Interest and compensation formulas recomputed, with the rate source dated.
- Court fee computed from the state schedule.

**Forum and form**
- Pecuniary and territorial jurisdiction confirmed. Consumer: District / State / National limits. [VERIFY: latest notification] Maharashtra bench via `resolve_bench`.
- Pre-litigation steps done or excused. Commercial Courts Act s.12A pre-institution mediation for suits without urgent interim relief. CPC s.80 notice before suing government, or leave sought.
- Plaint has the Order VII Rule 1 particulars. Verification and affidavit match the forum.
- Annexures all referenced, marked and present. Index, synopsis and list of dates where the forum requires them.

**Client data and ethics**
- Placeholders restored only in the local final file.
- Nothing promises an outcome. Nothing in the draft solicits or advertises.
- The advocate has read the whole document.

## 4. Writing the instruction (for any drafting or research task)

Give the model six things: **role** (who it is drafting as), **jurisdiction** (court, state, code version), **facts** (anonymised, dated), **task** (one instrument or question), **format** (forum's form, length, headings), **constraints** (no invented authority, mark VERIFY, cite only supplied cases). For analysis, ask for Issue, Rule, Application, Conclusion.

## 5. Matter brief (keep one per matter)

```
MATTER: [reference]            UPDATED: [DD-MM-YYYY]
CLIENT ROLE: [petitioner / accused / buyer ...]   OPPONENT ROLE: [...]
FORUM: [court, bench, case no. if filed]
STATUS: [pre-litigation / pending - next date / advisory / transaction]
KEY DATES: [next hearing, limitation expiry, compliance dates]
FACTS: [numbered, dated, each with its source document]
ISSUES: [numbered]
OUR POSITION / THEIR POSITION: [one paragraph each]
AUTHORITIES VERIFIED: [citation - paragraph - date checked]
DO NOT: [things the client has asked be kept out, settlement limits]
```

## 6. Contract review in four tiers

Mark every clause **ACCEPT**, **NEGOTIATE** (state the ask), **REJECT** (state why and give a replacement) or **MISSING** (give the clause). Lead with the REJECT and MISSING items. For foreign-law contracts, list what changes when Indian law governs: s.27 restraint, s.74 penalty vs liquidated damages, stamp duty, seat and venue under the Arbitration and Conciliation Act, 1996.

## 7. Devil's-advocate pass

Before finalising a pleading or opinion, write the other side's three strongest points and the forum's likely objections (maintainability, limitation, alternative remedy, suppression, delay). Answer each in the draft or flag it to the advocate. The drafting pipeline's Overseer stage does this for pleadings.

## 8. When to re-check the templates

Templates go stale with the legal calendar. Re-check:
- **After each RBI policy meeting** (about Feb, Apr, Jun, Aug, Oct, Dec): SBI MCLR used in RERA interest.
- **February to April**: Union Budget changes to tax and GST templates, then anything that says "current financial year".
- **1 July**: the BNS / BNSS / BSA section numbers in the criminal templates, and new Supreme Court guidance.
- **Any time**: state notifications of the Labour Codes, DPDP Rules, revised consumer pecuniary limits, and court-fee or stamp amendments in Maharashtra.

## 9. A one-page chambers AI policy

Cover: which AI tools and plans are allowed, anonymisation before upload, the pre-filing checklist before anything leaves, the advocate reading the whole document, the engagement-letter disclosure line, and who updates the policy each quarter.

## 10. Knowledge that compounds

Keep, per chambers: verified judgment notes (citation, ratio in one line, the paragraphs relied on, date checked), a tested clause library, a register of AI errors caught (what it said, what was true, which check caught it), and plain-language client FAQs by matter type. Review the templates against amendments every quarter.

---

Structure informed by the LLM Advocates course (learn.llmadvocates.com). No course text is reproduced. Every figure and rule above must be verified against primary sources before use.
