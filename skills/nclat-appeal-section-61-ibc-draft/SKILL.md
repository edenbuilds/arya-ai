---
name: nclat-appeal-section-61-ibc-draft
description: Draft a Memorandum of Appeal before the National Company Law Appellate Tribunal under Section 61 of the Insolvency and Bankruptcy Code 2016 read with the NCLAT Rules 2016, from an order of the National Company Law Tribunal made under the IBC (admission / rejection of Section 7 / 9 / 10 application, approval of resolution plan under Section 31, liquidation order under Section 33, IRP / RP / liquidator-related disputes, voidable-transaction orders under Sections 43-51, avoidance-transaction orders, personal-guarantor IRP orders under Section 100, distribution of liquidation proceeds, or any other NCLT order under the IBC). Encodes the Section 61(2) limitation regime (30 days from the date of the NCLT order, extendable on sufficient cause to a further 15 days; 45 days hard stop), the Section 61(3) grounds for admission-order appeals, the Section 61(4) grounds for resolution-plan-approval appeals, the Section 62 further-appeal-to-Supreme-Court framework, Section 64 expeditious-disposal endeavour (30 days, extendable to 90 days), and the Innoventive Industries (2018) admission framework as the lens for appellate review. Auto-fires on "draft Section 61 appeal", "draft NCLAT appeal IBC", "draft NCLAT IBC appeal", "draft appeal from NCLT IBC order", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# NCLAT Section 61 IBC Appeal Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: APPEAL UNDER SECTION 61 OF THE INSOLVENCY AND BANKRUPTCY CODE 2016 BEFORE THE NATIONAL COMPANY LAW APPELLATE TRIBUNAL
case_short_code: NCLAT_61_IBC
case_number_prefix_principal_bench: Company Appeal (AT) (Insolvency)
case_number_prefix_chennai_bench: Company Appeal (AT) (CH) (Insolvency)
pleading_type: Memorandum of Appeal (IBC 2016)
typical_forum: National Company Law Appellate Tribunal — Principal Bench at New Delhi for appeals from NCLT benches generally; NCLAT Chennai Bench for appeals from NCLT benches falling within its territorial assignment (NCLT Chennai / NCLT Bengaluru / NCLT Hyderabad / NCLT Amaravati / NCLT Kochi / verify against the current allocation notification of the NCLAT)
typical_parties: Appellant (any person aggrieved by the impugned NCLT order under the IBC) + Respondent(s) (Corporate Debtor / Resolution Professional / Liquidator / Committee of Creditors / successful Resolution Applicant / objecting creditor / personal guarantor / any other party to the proceedings below)

statutory_opening: "This Appeal is filed under Section 61 of the Insolvency and Bankruptcy Code 2016 read with the NCLAT Rules 2016, by the Appellant, being a person aggrieved by the order dated ____ passed by the [Member Judicial / Member Technical / Two-Member-Bench, as the case may be] of the National Company Law Tribunal, [Bench-Name], in [Case-Number-Below — e.g. C.P. (IB) No. ____ of ____ / I.A. No. ____ of ____ in C.P. (IB) No. ____ of ____], by which the Tribunal [outcome — e.g. admitted a Section 7 / Section 9 / Section 10 application; approved a resolution plan under Section 31; passed a liquidation order under Section 33; allowed / dismissed an application under Sections 43 / 45 / 47 / 49 / 50; passed an order under Section 60(5) IBC residual jurisdiction; admitted / rejected a personal-guarantor application under Section 100; passed an order in the course of CIRP / liquidation]."

ground_clauses:
  - "Authority of the Appellate Tribunal — the National Company Law Appellate Tribunal has been constituted under Section 410 of the Companies Act 2013 to hear appeals against orders of the NCLT, and Section 61 of the IBC 2016 confers the right of appeal on any person aggrieved by an order of the NCLT made under the IBC."
  - "Section 61(2) limitation satisfied — the impugned NCLT order was passed on ____; the present Appeal is filed within 30 days from the date of the order, satisfying the limitation prescribed under Section 61(2) of the Code. [Where filed beyond 30 days but within the extended 15 days on sufficient cause: a separate I.A. for condonation of delay is filed along with this Appeal, pleading the sufficient cause that prevented filing within the original 30 days. Beyond 45 days total, the Appeal is barred per consistent NCLAT and Supreme Court authority.]"
  - "Section 61(1) standing — the Appellant is a person aggrieved by the impugned order within the meaning of Section 61(1), in that [pleading of aggrievement]."
  - "Grounds of appeal (case-type-specific) —"
  - "  [For Section 61(3) appeals — admission-order appeals from Section 7 / 9 / 10 admission orders]"
  - "  - The NCLT erred in admitting the application as the alleged default has not occurred / the alleged default amount is below the threshold under Section 4 of the Code / the debt is not due and payable / the alleged default falls within the Section 10A suspension window (25 March 2020 — 24 March 2021)."
  - "  - The NCLT erred in admitting the application as the application is not complete / the form / format requirements under the IBBI (AAA) Rules 2016 are not satisfied / the proposed IRP is disqualified."
  - "  - [Section 9-specific] The NCLT erred in admitting the application as a pre-existing dispute existed within the meaning of Mobilox Innovations v. Kirusa Software (2018) 1 SCC 353; the dispute is real, not spurious, supported by material, and was raised before receipt of the Section 8 demand notice."
  - "  - [Section 10-specific] The NCLT erred in admitting the application as the Applicant is ineligible under Section 11 / the Application is fraudulent / malicious within Section 65."
  - "  - The admission was procured by material irregularity / fraud (Section 61(3)(i) read with Section 61(3)(ii))."
  - "  [For Section 61(4) appeals — resolution-plan-approval appeals]"
  - "  - The approved resolution plan is in contravention of Section 30(2) of the Code (does not conform to the priorities under Section 53 / does not provide for management of the corporate debtor after approval / does not contemplate adequate means for supervising the implementation of the plan / does not address the interests of all stakeholders)."
  - "  - The approved resolution plan violates Section 29A — the Resolution Applicant is a disqualified person."
  - "  - The CoC commercial wisdom was exercised without due application of mind / on extraneous considerations / in breach of the duty owed to operational and dissenting creditors."
  - "  - Material irregularity in the conduct of CIRP — public-announcement defects / claim-verification defects / CoC-constitution defects / voting-share computation defects / Section 30(4) compliance defects."
  - "  [For other Section 61 appeals — liquidation orders, Section 60(5) residual orders, Section 43-51 voidable-transaction orders, Section 100 personal-guarantor admission orders]"
  - "  - [Case-specific grounds as applicable, addressing the operative provisions of the impugned order and the relevant case-law line.]"
  - "Innoventive admission framework — at admission stage the NCLT is required to examine only (a) default, (b) completeness, and (c) IRP eligibility per Innoventive Industries v. ICICI Bank (2018) 1 SCC 407. [Where the Appellant challenges admission:] the impugned order goes BEYOND the Innoventive framework / fails to apply the Innoventive framework correctly. [Where the Appellant defends admission against an opposing appeal:] the impugned order correctly applied the Innoventive framework and the appeal seeks impermissible merits re-adjudication."

prayer_clauses:
  - "(a) Set aside / Modify the impugned order dated ____ passed by the National Company Law Tribunal, [Bench-Name], in [Case-Number-Below];"
  - "(b) [Case-specific consequential prayer — e.g. quash the admission of CIRP and direct refund of fees; reject the resolution plan and direct fresh CoC consideration; set aside the liquidation order and remit to NCLT for further consideration; modify the Section 43 voidable-transaction direction]"
  - "(c) Pass such order in the matter as the Appellate Tribunal considers appropriate under Section 61 of the Code;"
  - "(d) Direct the Respondents to pay the costs of this Appeal and of the proceedings below to the Appellant;"

mandatory_exhibits:
  - certified_copy_of_the_impugned_nclt_order
  - proof_of_date_of_the_nclt_order_or_proof_of_uploading_on_nclt_portal
  - complete_paper_book_of_the_proceedings_below_pleadings_replies_rejoinders
  - complete_paper_book_of_orders_passed_during_pendency_of_proceedings_below
  - public_announcement_form_a_published_pursuant_to_section_13_1_where_admission_being_appealed
  - claim_filings_and_irp_or_rp_verification_records_where_relevant
  - committee_of_creditors_minutes_where_relevant
  - resolution_plan_approved_by_coc_and_submitted_to_nclt_where_section_61_4_appeal
  - rp_certificate_under_section_30_2_where_section_61_4_appeal
  - liquidator_or_resolution_professional_reports_where_relevant
  - vakalatnama_or_authorisation_in_favour_of_the_advocate_for_the_appellant
  - board_resolution_authorising_the_appeal_where_appellant_is_corporate

accompanying_applications:
  - "I.A. for stay of operation of the impugned NCLT order pending the Appeal"
  - "I.A. for condonation of delay under Section 61(2) proviso (where appeal is filed beyond 30 days but within the extended 15 days)"
  - "I.A. for ad-interim direction (e.g. status-quo on disposal of assets of the Corporate Debtor / continuation of essential supplies under Section 14(2A) / specific stay on implementation of the approved plan pending appeal)"
  - "I.A. for early disposal under Section 64 (which mandates the NCLAT to endeavour to dispose of the appeal within 30 days, extendable to 90 days)"
  - "I.A. for permission to be added as Appellant / Respondent where impleadment is necessary"
  - "I.A. for substituted service on the Respondents"
  - "I.A. for exemption from filing certified copies of voluminous CoC records / claim records (where available with the IRP / RP / Liquidator)"

filing_fee: "Fee under the NCLAT Rules 2016 / IBBI Rules for Section 61 IBC appeals (verify against latest schedule)."

limitation: "30 days from the date of the order of the NCLT (Section 61(2) — note: from DATE OF ORDER, not date of receipt, per the consistent NCLAT and Supreme Court authority). Extendable by the NCLAT on sufficient cause shown by a further 15 days. Beyond 45 days total, the appeal is barred — this is a HARD STOP per consistent appellate authority."
```

## Section 61(3) — grounds for appeals against admission orders

Section 61(3) IBC specifies the grounds on which an appeal against an order of admission under Section 7 / 9 / 10 may be filed:

- **Section 61(3)(i)** — the approved resolution plan is in contravention of the provisions of any law for the time being in force (relevant for Section 31 plan-approval appeals)
- **Section 61(3)(ii)** — there has been material irregularity in exercise of the powers by the resolution professional during the corporate insolvency resolution period
- **Section 61(3)(iii)** — the debts owed to operational creditors of the corporate debtor have not been provided for in the resolution plan in the manner specified by the Board (CIRP Regulations on minimum recovery for operational creditors)
- **Section 61(3)(iv)** — the insolvency resolution process costs have not been provided for repayment in priority to all other debts
- **Section 61(3)(v)** — the resolution plan does not comply with any other criteria specified by the Board

These grounds primarily apply to Section 61(4) plan-approval appeals; for Section 61 appeals from admission orders generally, the standard grounds (default not occurred / threshold not met / Mobilox dispute / Section 11 / Section 65 / Innoventive overreach) apply.

## Section 61(4) — grounds for appeals against resolution-plan-approval orders

Section 61(4) — an appeal against an order approving a resolution plan under Section 31 may be filed on any of the grounds in Section 61(3) above. The Section 61(4) appellate review is NARROWER than general appellate review — the NCLAT does NOT re-adjudicate the commercial wisdom of the Committee of Creditors per *K. Sashidhar v. Indian Overseas Bank* (2019) 12 SCC 150 and *CoC of Essar Steel v. Satish Kumar Gupta* (2020) 8 SCC 531. The grounds are confined to the statutory heads.

## Section 62 — further appeal to the Supreme Court

Section 62 IBC permits a further appeal to the Supreme Court from an order of the NCLAT on a question of law arising out of such order under the IBC, within 45 days from the date of receipt of the NCLAT order. The Supreme Court may extend the period by a further 15 days on sufficient cause. The Drafter notes Section 62 for client-advice purposes but does NOT plead it in the NCLAT memo.

## Section 64 — expeditious disposal

Section 64 mandates the NCLAT to dispose of the appeal within 30 days from receipt of the appeal, extendable on sufficient cause to 90 days. The Drafter pleads the Section 64 expectation in the I.A. for early disposal where the CIRP timeline pressure is acute.

## Hard-stop limitation per consistent appellate authority

The Supreme Court has consistently held (*K. Sashidhar* line; *V. Nagarajan v. SKS Ispat & Power Ltd.* (2022) 2 SCC 244) that the maximum extension under Section 61(2) is 15 days, totalling 45 days from the date of the NCLT order. The Drafter MUST verify the date of the impugned order (not date of receipt) and ensure filing within 30 days; beyond, file with a vigorous condonation application supported by sufficient-cause documentation; beyond 45 days total, the appeal is incompetent regardless of cause.

## Innoventive framework as the appellate lens

Where the Appellant challenges an admission order, the framework is: did the NCLT confine its inquiry to (a) default + (b) completeness + (c) IRP eligibility? If yes, the admission stands; if the NCLT overshot into merits-of-debt adjudication, that is appealable. Where the Appellant defends an admission order against an opposing appeal, the framework cuts the other way — the appeal cannot seek a merits re-look that the admission stage itself excludes.

## CIRP timeline pressure

The Section 12 IBC timeline (180 days extendable to 330 days) is the appellate decision-making backdrop. Resisting interim stay of the NCLT admission order is harder when an approved plan is days from implementation; resisting stay of a plan-approval order is harder when the Corporate Debtor's value is depleting. The Drafter pleads CIRP-timeline awareness in the stay-application discipline.

## Distinction from Section 421 Companies Act appeal (separate skill)

| Feature | Section 61 IBC (this skill) | Section 421 Companies Act (separate skill) |
|---|---|---|
| Source of NCLT order | IBC 2016 jurisdiction | Companies Act 2013 jurisdiction |
| Limitation — original | 30 days from order date | 45 days from receipt of order |
| Limitation — extension | 15 days (HARD STOP at 45) | 45 days (total 90) |
| Disposal endeavour | 30 days, extendable to 90 days | 6 months |
| Grounds-specificity | Section 61(3) / (4) statutory heads + Innoventive | General appeal heads |
| Case-number prefix | Company Appeal (AT) (Insolvency) | Company Appeal (AT) |

The Drafter does NOT conflate the two routes. An IBC NCLT order is appealed under THIS skill; a Companies-Act-2013 NCLT order is appealed under `nclat-appeal-section-421-draft`.
