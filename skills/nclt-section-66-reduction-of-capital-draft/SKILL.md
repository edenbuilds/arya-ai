---
name: nclt-section-66-reduction-of-capital-draft
description: Draft a Petition before the National Company Law Tribunal for confirmation of a reduction of share capital under Section 66 of the Companies Act 2013 read with the NCLT (Procedure for Reduction of Share Capital of Company) Rules 2016. Encodes Section 66(1) requirements (special resolution + Tribunal confirmation), Section 66(2) creditor-protection regime (auditor's certificate on absence of arrears of deposit repayment; list of creditors with consents / unsatisfied creditors with proposed settlement), Section 66(3) public-notice and creditor-objection regime, Section 66(5) order of confirmation, and Section 66(6) registration of the order with the Registrar of Companies. Auto-fires on "draft Section 66 reduction", "draft capital reduction petition", "draft reduction of share capital", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# NCLT Section 66 Reduction of Share Capital Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: PETITION UNDER SECTION 66 OF THE COMPANIES ACT 2013 READ WITH THE NCLT (PROCEDURE FOR REDUCTION OF SHARE CAPITAL OF COMPANY) RULES 2016
case_short_code: NCLT_66
case_number_prefix: C.P.
pleading_type: Company Petition (Reduction of Share Capital)
typical_forum: NCLT of competent territorial jurisdiction (registered office of the Petitioner Company)
typical_parties: Petitioner Company (the company resolving to reduce its share capital) + Respondent Registrar of Companies + creditors served notice pursuant to Section 66(4)

statutory_opening: "This Petition is filed under Section 66 of the Companies Act 2013 read with the NCLT (Procedure for Reduction of Share Capital of Company) Rules 2016, by the Petitioner Company seeking confirmation of the special resolution dated ____ reducing the paid-up share capital of the Petitioner Company from ₹ ___ to ₹ ___ in the manner specified in the Scheme of Reduction annexed hereto."

ground_clauses:
  - "Authority of the Tribunal — Section 66 of the Companies Act 2013 vests jurisdiction in the National Company Law Tribunal to confirm a reduction of share capital; the erstwhile High Court jurisdiction under Sections 100 to 102 of the Companies Act 1956 stood transferred to the NCLT with effect from 15 December 2016."
  - "Jurisdictional anchor — the registered office of the Petitioner Company is within the territorial limits of this Bench (Rule 18 of the NCLT Rules 2016)."
  - "Articles permit reduction — Article ____ of the Articles of Association of the Petitioner Company expressly authorises reduction of share capital; alternatively, the Articles do not prohibit reduction and the Section 66 procedure has been complied with."
  - "Special resolution under Section 66(1) passed — the Petitioner Company, in its [Annual / Extraordinary] General Meeting held on ____, passed a special resolution under Section 66(1) of the Companies Act 2013 read with Section 114(2), approving the reduction of share capital in the manner set out in the Scheme of Reduction (Exhibit ___); the explanatory statement under Section 102 disclosed all material facts."
  - "Mode of reduction — the reduction is by [extinguishing or reducing the liability on shares not paid-up / cancelling paid-up capital lost or unrepresented by available assets / paying off paid-up capital in excess of the company's wants] in accordance with Section 66(1)(b)."
  - "Section 66(2)(b) auditor's certificate — the Petitioner Company is not in arrears of repayment of any deposits accepted by it under Chapter V of the Companies Act 2013 or under the Companies Act 1956 (where applicable) before commencement, or of the interest payable thereon, as certified by the auditor (Exhibit ___)."
  - "Section 66(2)(c) list of creditors — the Petitioner Company has filed a list of creditors as on the relevant date, disclosing the name, address and nature of debt of each creditor (Exhibit ___); written consents from creditors representing [percentage] of the total claims have been obtained (Exhibit ___); the remaining creditors have been provided for in the proposed settlement."
  - "Section 66(4) public notice — the Tribunal is requested to direct publication of notice of the reduction in two newspapers (one English, one vernacular) circulating in the district of the registered office, inviting creditor objections within the prescribed period of 3 months."
  - "Limitation — no statutory limitation applies; the Petition is filed contemporaneously with the passing of the special resolution and the auditor's certificate."

prayer_clauses:
  - "(a) Confirm the special resolution dated ____ of the Petitioner Company reducing the paid-up share capital from ₹ ___ to ₹ ___ in the manner specified in the Scheme of Reduction;"
  - "(b) Direct publication of notice of the proposed reduction in two newspapers (one English, one vernacular) circulating in the district of the registered office of the Petitioner Company, inviting creditor objections within the prescribed period;"
  - "(c) Direct notice of the proposed reduction to the Central Government, the Registrar of Companies, the Securities and Exchange Board of India (where applicable to a listed company), and the creditors of the Petitioner Company as required by Section 66(2);"
  - "(d) Settle / cause to be settled the list of creditors of the Petitioner Company, and where any creditor has not consented to the reduction, secure / cause to be secured the payment of his debt;"
  - "(e) Direct that the minute approved by the Tribunal showing (i) the amount of share capital, (ii) the number of shares into which it is divided, (iii) the amount of each share, and (iv) the amount, if any, deemed to be paid-up on each share at the date of registration of the minute, shall be registered with the Registrar of Companies under Section 66(6);"
  - "(f) Direct that the words 'and reduced' (where required by the Tribunal under Section 66(7)) shall be added to the name of the Petitioner Company for such period as the Tribunal may direct, and that a copy of the order be published in such manner as the Tribunal may direct;"

mandatory_exhibits:
  - memorandum_of_association_and_articles_of_association
  - certificate_of_incorporation
  - latest_annual_return_mgt_7
  - latest_audited_financial_statements_three_years
  - special_resolution_dated_under_section_66_1
  - notice_of_general_meeting_with_explanatory_statement_under_section_102
  - scheme_of_reduction_setting_out_pre_reduction_and_post_reduction_capital_structure
  - auditors_certificate_under_section_66_2_b_on_absence_of_arrears_of_deposit_repayment
  - auditors_report_on_accounting_treatment_under_indas
  - list_of_creditors_as_on_relevant_date
  - written_consents_of_creditors_where_obtained
  - statement_of_proposed_settlement_of_unsatisfied_creditors
  - board_resolution_authorising_the_petition

accompanying_applications:
  - "I.A. for newspaper publication directions"
  - "I.A. for creditor-objection directions and disposal"
  - "I.A. for confidentiality directions (where settlement particulars are commercially sensitive)"
  - "I.A. for urgent listing"

filing_fee: "Fee under the Schedule of Fees of the NCLT Rules 2016 for Section 66 petitions (verify against latest schedule)."

limitation: "No specific limitation; filed contemporaneously with the special resolution and the auditor's certificate."
```

## Section 66(1)(b) — modes of reduction

Section 66(1)(b) of the Companies Act 2013 contemplates three modes of reduction:

1. **Extinguishing or reducing the liability on any of its shares in respect of share capital not paid-up** — applicable to partly paid-up shares
2. **Cancelling any paid-up share capital which is lost or is unrepresented by available assets** — applicable where accumulated losses have eroded paid-up capital (the 'wipe-out' route)
3. **Paying off any paid-up share capital which is in excess of the wants of the company** — applicable where excess capital is returned to shareholders

The Petitioner specifies the mode in the Scheme of Reduction. The arithmetic of the reduction (pre-reduction paid-up capital / amount written off or paid off / post-reduction paid-up capital / treatment of the share-premium / securities premium / capital-redemption-reserve account) is pleaded with particularity.

## Section 66(2) — preconditions

- **Section 66(2)(a)** — no application shall be sanctioned by the Tribunal unless the accounting treatment proposed by the company is in conformity with the accounting standards specified in Section 133 of the Companies Act 2013 read with a certificate of the auditor to that effect
- **Section 66(2)(b)** — no application shall be sanctioned if the company is in arrears in the repayment of any deposits accepted by it under Chapter V of the 2013 Act or under the corresponding provisions of the 1956 Act or interest payable thereon
- **Section 66(2)(c)** — protection of creditors as set out above

The Drafter pleads each of these positively in the petition body.

## Section 66(3) — special resolution and Tribunal confirmation

The reduction of share capital is a two-step process: (i) special resolution of the members in general meeting under Section 66(1) read with Section 114(2); (ii) confirmation by the Tribunal under Section 66(5). Either step alone does not effect the reduction. The Petition is filed AFTER the special resolution has been passed.

## Section 66(4) — public notice and creditor objections

The Tribunal directs publication of notice of the proposed reduction in such manner as it considers proper, calling upon any creditor who objects to the reduction to file his objection within the prescribed period. Every creditor whose debt is not discharged or determined and who does not consent to the reduction must be secured. The Drafter pleads positively to creditor-protection.

## Section 66(6) — registration of order with ROC

On confirmation, a minute approved by the Tribunal setting out (i) the amount of share capital as altered, (ii) the number of shares into which it is to be divided, (iii) the amount of each share, (iv) the amount, if any, at the date of registration deemed to be paid-up on each share, must be registered with the Registrar of Companies. The Drafter prays for the consequential direction.

## Section 66(7) — "and reduced" addition (Tribunal discretion)

Where the Tribunal so directs, the words *"and reduced"* may be added to the name of the company for such period as the Tribunal thinks expedient. Modern practice: this is rarely directed for going-concern reductions; the Drafter does not pray for it but flags it as a Tribunal discretion.

## Cross-reference to Section 230 (scheme involving capital reduction)

Where the reduction is part of a Section 230 compromise / arrangement scheme, separate Section 66 filing is NOT required — the Section 230(2)(c) single-window sanction subsumes the Section 66 compliance, provided the Section 66 creditor-protection particulars are pleaded within the Section 230 application body. The advocate is to choose the appropriate route at the design stage and not file in parallel.

## Cross-reference to Section 68 (buy-back of securities)

Buy-back of equity / preference shares is governed by Section 68 (board-level for up to 10%; shareholder-level for up to 25%), NOT by Section 66. The Drafter does not conflate Section 68 buy-back with Section 66 reduction.
