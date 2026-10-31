---
name: maharashtra-courts-drafting
description: Draft official Maharashtra pleadings for the Bombay High Court (Mumbai, Nagpur, Aurangabad, Kolhapur circuit) and State tribunals including MAT, MACT, Consumer Commissions, DRT DRAT, NCLT Mumbai, Labour and Industrial Courts, MahaRERA and Family Courts. Use when the user asks for a writ, APL, ABA, bail, appeal, MACT claim, consumer complaint, DRT OA, SARFAESI, NI 138, MAT OA, ULP, RERA or a Maharashtra deed.
---

# Maharashtra Courts Drafting

Draft in the forum's own register. This skill is Maharashtra-only.

## Load first

Read as needed from `${CLAUDE_PLUGIN_ROOT}/maharashtra/references/` (or `get_reference_note`):

- `territorial-jurisdiction.md` — district → Bombay bench / MAT / DRT
- `acronyms.md` — APL is not ABA; MAT is the Administrative Tribunal
- `court-fees-stamp.md`
- `efiling.md`

## Before drafting

Ask two things and wait for the answers:
1. Which instrument and forum (take the advocate's acronym as given; see `acronyms.md`).
2. Whether there is a reference draft to follow. If there is, follow its structure, headings, cause title, numbering and register, and take nothing factual from it about this matter.

Facts come from the matter's own papers or from the advocate. Where a fact, fee, date, limitation article or citation is missing, leave a bracketed blank and say what must be supplied.

When drafting a named instrument, load in this order:
1. `maharashtra/forum-config/exemplars/` (or `get_forum_config`, `resolve_bench`) for the bench or tribunal
2. `maharashtra/templates/` (or `get_drafting_template`) long-form official form (writ, reply affidavit, rejoinder, stay, MACT, consumer, DRT, deeds)
3. matching `skills/<case-type>-draft/SKILL.md` if it exists

Opposite-side drafts are first-class. A writ reply is `maharashtra/templates/high-court/affidavit-in-reply-writ.md`. A rejoinder is `maharashtra/templates/high-court/rejoinder-affidavit-writ.md`. Do not invent a short form when a long-form template exists.

## Pipeline

Reader (privacy firewall + fact ledger) → Format (forum header + skeleton) → Drafter → Verifier (no invented citations) → Refiner (strip model-voice) → Overseer (opposing-counsel notes) → filing-grade markdown / docx.

## House style — Bombay High Court

- `IN THE HIGH COURT OF JUDICATURE AT BOMBAY.` at the Principal Seat.
- `IN THE HIGH COURT OF JUDICATURE AT BOMBAY BENCH AT NAGPUR.` (or AURANGABAD / KOLHAPUR) at a bench.
- Appeals prefer `///VERSUS///`.
- Annexures `ANNEXURE-A`. A4, Times New Roman 14, 1.5, left margin ~4 cm.
- Court fees cite the Bombay Court-Fees Act, 1959. Deeds cite the Maharashtra Stamp Act, 1958.

## Routing

- State service matters → Maharashtra Administrative Tribunal, not a writ in the first instance.
- Unfair labour practice / union recognition → Industrial Court under MRTU and PULP Act, 1971.
- IBC first instance → NCLT Mumbai, not the High Court.
- s.173 MV appeal follows the High Court bench of the MACT district.
- Kolhapur circuit districts — confirm the circuit is sitting; otherwise Principal Seat.

## Never

- Invent a reported citation, fee, or limitation article.
- Treat APL as anticipatory bail.
- File a Maharashtra district matter at the Goa Bench.
- Restore real identifiers until the final local render.
- Advertise legal services or guarantee Registry acceptance.

Every draft is a starting point for a practising advocate.
