---
name: nclat-appeal-section-421-draft
description: Draft a Memorandum of Appeal before the National Company Law Appellate Tribunal under Section 421 of the Companies Act 2013 (and Section 422 disposal-timelines) read with the NCLAT Rules 2016, from an order of the National Company Law Tribunal in a non-IBC matter (oppression and mismanagement under Sections 241-242 / scheme under Sections 230-232 / reduction under Section 66 / restoration under Section 252 / investigation under Section 213 / class action under Section 245 / or any other matter under the Companies Act 2013). Encodes the Section 421(3) limitation regime (45 days from receipt of the NCLT order, extendable on sufficient cause to a further 45 days), Section 421(4) NCLAT remedial scope, and the NCLAT Rules 2016 procedural discipline. Auto-fires on "draft Section 421 appeal", "draft NCLAT appeal Companies Act", "draft NCLAT Companies Act appeal", "draft appeal from NCLT order Companies Act", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# NCLAT Section 421 Companies Act Appeal Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: APPEAL UNDER SECTION 421 OF THE COMPANIES ACT 2013 BEFORE THE NATIONAL COMPANY LAW APPELLATE TRIBUNAL
case_short_code: NCLAT_421
case_number_prefix: Company Appeal (AT)
pleading_type: Memorandum of Appeal (Companies Act 2013)
typical_forum: National Company Law Appellate Tribunal, Principal Bench, New Delhi (the NCLAT Chennai Bench was constituted for IBC appeals primarily; non-IBC Companies-Act appeals from all NCLT benches typically lie before the NCLAT Principal Bench unless specifically allocated otherwise — verify allocation notification)
typical_parties: Appellant (any person aggrieved by the impugned NCLT order) + Respondent(s) (parties to the NCLT proceedings below in whose favour the impugned order was passed or who would be affected by its modification)

statutory_opening: "This Appeal is filed under Section 421 of the Companies Act 2013 read with the NCLAT Rules 2016, by the Appellant, being a person aggrieved by the order dated ____ passed by the [Member Judicial / Member Technical / Two-Member-Bench, as the case may be] of the National Company Law Tribunal, [Bench-Name], in [Case-Number-Below — e.g. C.P. (CAA) No. ____ of ____ / C.A. No. ____ of ____ / C.P. No. ____ of ____], by which the Tribunal [outcome — e.g. allowed / dismissed / partly allowed / passed directions / made an interim order]."

ground_clauses:
  - "Authority of the Appellate Tribunal — the National Company Law Appellate Tribunal has been constituted under Section 410 of the Companies Act 2013 to hear appeals against orders of the NCLT and certain other authorities; Section 421 of the Companies Act 2013 confers the right of appeal on any person aggrieved by an order of the NCLT."
  - "Section 421(3) limitation satisfied — the impugned NCLT order was received by the Appellant on ____; the present Appeal is filed within 45 days from the date of receipt, satisfying the limitation prescribed under Section 421(3). [Where filed beyond 45 days but within the extended 45 days on sufficient cause: a separate I.A. for condonation of delay is filed along with this Appeal, pleading the sufficient cause that prevented filing within the original 45 days.]"
  - "Section 421(1) standing — the Appellant is a person aggrieved by the impugned order within the meaning of Section 421(1) of the Companies Act 2013, in that [pleading of aggrievement — direct adverse effect / loss of right / imposition of liability / denial of relief]."
  - "Grounds of appeal (specimen, to be tailored per case):"
  - "  - The NCLT erred in law in [(a) misconstruing the operative provision of the Companies Act 2013; (b) applying an erroneous standard; (c) overlooking a binding precedent of the NCLAT / Supreme Court]."
  - "  - The NCLT erred in fact in [(a) appreciating the documentary evidence; (b) drawing inferences inconsistent with the record; (c) recording findings unsupported by the evidence on record]."
  - "  - The NCLT acted in breach of natural justice in [(a) not affording adequate hearing on a material issue; (b) deciding on grounds not put to the Appellant; (c) failing to consider the Appellant's submissions on a critical issue]."
  - "  - The NCLT acted in excess of jurisdiction in [(a) granting reliefs not pleaded; (b) traversing beyond the issues; (c) exercising a power not vested in it by the operative provision]."
  - "  - The NCLT failed to consider material on record — paragraphs ___ of the Appellant's pleadings and Exhibits ___ to ___ filed below are not addressed in the impugned order."
  - "  - [Case-type-specific grounds — e.g. Section 244 threshold misconstrued in a Section 241-242 appeal; Section 230(2) disclosure standard misapplied in a Section 230 scheme appeal; Section 66 creditor-protection regime misapplied in a Section 66 capital-reduction appeal; Section 252 limitation misconstrued in a Section 252 revival appeal]."

prayer_clauses:
  - "(a) Set aside / Modify / Quash the impugned order dated ____ passed by the National Company Law Tribunal, [Bench-Name], in [Case-Number-Below];"
  - "(b) Pass such order in the matter as the Appellate Tribunal considers appropriate under Section 421(4) of the Companies Act 2013, including [substantive directions sought];"
  - "(c) Direct the Respondents to pay the costs of this Appeal and of the proceedings below to the Appellant;"

mandatory_exhibits:
  - certified_copy_of_the_impugned_nclt_order
  - proof_of_date_of_receipt_of_the_nclt_order_or_proof_of_uploading_on_nclt_portal
  - complete_paper_book_of_the_proceedings_below_pleadings_replies_rejoinders_documents_exhibits
  - complete_paper_book_of_orders_passed_during_pendency_of_proceedings_below
  - any_subsequent_application_filed_before_the_nclt_referenced_in_the_impugned_order
  - vakalatnama_or_authorisation_in_favour_of_the_advocate_for_the_appellant
  - board_resolution_authorising_the_appeal_where_appellant_is_corporate

accompanying_applications:
  - "I.A. for stay of operation of the impugned NCLT order pending the Appeal"
  - "I.A. for condonation of delay under the proviso to Section 421(3) (where appeal is filed beyond 45 days)"
  - "I.A. for exemption from filing certified copies of certain documents (where unavailable from the NCLT registry)"
  - "I.A. for urgent listing (where irreversible consequences may follow the impugned order — e.g. operation of a Section 232 sanction order, alteration of share capital, removal of director, etc.)"
  - "I.A. for substituted service on the Respondents (where regular service has been frustrated)"
  - "I.A. for early disposal under Section 422 (which mandates the NCLAT to endeavour to dispose of the appeal within 6 months)"

filing_fee: "Fee under the NCLAT Rules 2016 for Section 421 Companies Act appeals (verify against latest schedule)."

limitation: "45 days from the date of receipt of the order of the NCLT (Section 421(3)). Extendable by the NCLAT on sufficient cause shown to a further 45 days. Beyond 90 days total, the appeal is barred."
```

## Section 421(4) — NCLAT's remedial powers

Section 421(4) empowers the NCLAT, after giving the parties to the appeal a reasonable opportunity of being heard, to "pass such orders thereon as it thinks fit, confirming, modifying or setting aside the order appealed against." The Drafter's prayer reflects this remedial scope — the Appellate Tribunal may CONFIRM, MODIFY, or SET ASIDE; substitution of NCLT's findings is permissible.

## Section 422 — expeditious disposal endeavour

Section 422 mandates that every appeal preferred under Section 421 shall be dealt with by the NCLAT as expeditiously as possible and endeavour shall be made to dispose of the appeal finally within six months from the date of receipt of the appeal. The Drafter pleads the Section 422 expectation in the I.A. for early disposal where applicable.

## Distinction from Section 61 IBC appeal (separate skill)

| Feature | Section 421 (this skill) | Section 61 IBC (separate skill) |
|---|---|---|
| Source of NCLT order | Companies Act 2013 jurisdiction | IBC 2016 jurisdiction |
| Limitation — original | 45 days | 30 days |
| Limitation — extension | 45 days (total 90) | 15 days (total 45) |
| Disposal endeavour | 6 months (Section 422) | 30 days, extendable to 90 days (Section 64) |
| Grounds-specificity | General appeal heads | Section 61(3) / Section 61(4) statutory heads |
| Case-number prefix at NCLAT | Company Appeal (AT) | Company Appeal (AT) (Insolvency) / Company Appeal (AT) (CH) (Insolvency) |

The Drafter does NOT conflate the two routes. A Section 421 appeal against a Companies-Act-2013 NCLT order is filed under THIS skill; a Section 61 IBC appeal against an IBC NCLT order is filed under the `nclat-appeal-section-61-ibc-draft` skill.

## Stay-application discipline

Filing an appeal under Section 421 does NOT operate as an automatic stay of the impugned NCLT order. The Appellant must specifically pray for stay in an I.A. accompanying the appeal. The stay-application pleads:

- Prima-facie case in favour of the Appellant (Grounds of appeal applied to the facts)
- Balance of convenience favouring stay (irreversible consequences if the impugned order operates)
- Irreparable injury to the Appellant absent stay
- Public-interest dimension (where applicable, particularly for scheme / capital-reduction / restoration appeals affecting stakeholders other than the parties)

## Further appeal under Section 423

Section 423 provides for further appeal to the Supreme Court from any order of the NCLAT, on questions of law arising out of such order — within 60 days of the order. The Drafter notes Section 423 for client-advice purposes but does NOT plead it in the NCLAT memo.

## Companies Act 1956 → 2013 transition lens

Even at NCLAT, residual 1956-Act citations may surface in older case-laws cited in the impugned order or in the parties' pleadings below. The Drafter notes the transition (Section 397/398 → 241/242; Section 391-394 → 230-232; Section 100-102 → 66; Section 235/237 → 213; Section 560 → 248-252) but does NOT re-cite the 1956 provisions in the NCLAT memo — only the 2013-Act successor sections appear in the operative paragraphs.
