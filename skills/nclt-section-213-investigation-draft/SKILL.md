---
name: nclt-section-213-investigation-draft
description: Draft an Application before the National Company Law Tribunal under Section 213 of the Companies Act 2013 read with the Companies (Inspection, Investigation and Inquiry) Rules 2014, seeking an order directing the Central Government to investigate the affairs of a company. Encodes the dual maintainability standards — Section 213(a) member-threshold (not less than 100 members OR members holding 1/10th of the total voting power) and Section 213(b) prima-facie-material standard (any person on the ground of fraud / misfeasance / unlawful purpose / non-disclosure to members). Auto-fires on "draft Section 213 investigation", "draft NCLT investigation application", "draft investigation petition", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# NCLT Section 213 Investigation Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: APPLICATION UNDER SECTION 213 OF THE COMPANIES ACT 2013 READ WITH THE COMPANIES (INSPECTION, INVESTIGATION AND INQUIRY) RULES 2014
case_short_code: NCLT_213
case_number_prefix: C.P.
pleading_type: Application for Investigation
typical_forum: NCLT of competent territorial jurisdiction (registered office of the Respondent Company)
typical_parties: Applicants (members under Section 213(a) / any person under Section 213(b)) + Respondent Company + Respondent Directors / KMP / Officers implicated + Central Government (as a necessary party to whom the investigation will be directed)

statutory_opening_213_a: "This Application is filed under Section 213(a) of the Companies Act 2013 read with the Companies (Inspection, Investigation and Inquiry) Rules 2014, by the Applicants being [not less than 100 members of the Respondent Company / members of the Respondent Company holding not less than one-tenth of the total voting power], seeking an order of this Tribunal directing the Central Government to investigate the affairs of the Respondent Company in accordance with Section 213."
statutory_opening_213_b: "This Application is filed under Section 213(b) of the Companies Act 2013 read with the Companies (Inspection, Investigation and Inquiry) Rules 2014, by the Applicant on the ground that the affairs of the Respondent Company are being conducted with intent to defraud creditors / members / others / for any fraudulent or unlawful purpose / in a manner oppressive to any member / for a fraudulent or unlawful purpose, and seeking an order of this Tribunal directing the Central Government to investigate the affairs of the Respondent Company in accordance with Section 213."

ground_clauses:
  - "Authority of the Tribunal — Section 213 of the Companies Act 2013 vests jurisdiction in the National Company Law Tribunal to direct the Central Government to investigate the affairs of a company; the erstwhile Company Law Board / High Court jurisdiction under Sections 235 and 237 of the Companies Act 1956 stood transferred to the NCLT with effect from 1 June 2016."
  - "Jurisdictional anchor — the registered office of the Respondent Company is within the territorial limits of this Bench (Rule 18 of the NCLT Rules 2016)."
  - "[For Section 213(a) applications] Member-threshold satisfied — the Applicants are [not less than 100 members / members holding not less than one-tenth of the total voting power] of the Respondent Company, as evidenced by the Register of Members under Section 88 (Exhibit ___) and the share-certificate / DEMAT holding statements of the Applicants (Exhibit ___)."
  - "[For Section 213(b) applications] Prima-facie material on the existence of one or more of the Section 213(b)(i) to (iv) grounds — particularly: (i) intent to defraud creditors / members / others (the documentary anchors at Exhibits ___ to ___ disclose [particulars]); OR (ii) a fraudulent or unlawful purpose underlying corporate transactions (the documentary anchors at Exhibits ___ to ___ disclose [particulars]); OR (iii) misfeasance or other misconduct by management (the documentary anchors at Exhibits ___ to ___ disclose [particulars]); OR (iv) non-disclosure to members of information they were reasonably entitled to (the documentary anchors at Exhibits ___ to ___ disclose [particulars])."
  - "Less-invasive remedies inadequate — a Section 206 / Section 207 inspection by the Registrar of Companies has either (i) been undertaken and proved inadequate; OR (ii) cannot realistically be expected to surface the depth of investigation that the present grounds necessitate, given the implications of the alleged fraud / misfeasance / unlawful purpose."
  - "Limitation — the present Application is filed within the residual limitation under Article 137 of the Schedule to the Limitation Act 1963; continuing fraud / mismanagement keeps limitation alive."

prayer_clauses:
  - "(a) Direct the Central Government to investigate the affairs of the Respondent Company in accordance with Section 213 of the Companies Act 2013;"
  - "(b) Direct that the Central Government may appoint such Inspectors as it considers necessary, with such terms of reference as may be specified, to inquire into and report on the matters set out in the present Application;"
  - "(c) Pending the investigation, direct the Respondent Company and its Directors / Officers to preserve all books of account, registers, records, minutes, accounting records, electronic records, share-transfer records, and any other documents relevant to the matters being investigated, and to make them available to the Inspectors when called upon;"
  - "(d) Direct that the Inspectors' report, when received, be placed before this Tribunal for further directions;"
  - "(e) Restrain the Respondent Directors / Officers from disposing of / alienating / encumbering any of the assets of the Respondent Company pending the investigation;"

mandatory_exhibits:
  - memorandum_of_association_and_articles_of_association
  - certificate_of_incorporation
  - latest_annual_return_mgt_7
  - latest_audited_financial_statements_three_years
  - register_of_members_under_section_88_with_share_holding_workings_for_threshold
  - share_certificates_or_demat_holding_statements_of_applicants
  - board_minutes_for_impugned_period
  - general_meeting_minutes_for_impugned_period
  - documentary_anchors_for_alleged_fraud_or_misfeasance_or_unlawful_purpose
  - correspondence_evidencing_pre_application_efforts_to_secure_information
  - any_prior_section_206_or_section_207_inspection_report_or_order
  - police_complaint_or_first_information_report_or_other_criminal_action_where_relevant

accompanying_applications:
  - "I.A. for interim directions preserving books of account / records pending the investigation"
  - "I.A. for restraint on the Respondent Directors / Officers from disposing of assets of the Respondent Company"
  - "I.A. for confidentiality directions on sensitive material filed with the Application"
  - "I.A. for urgent listing (where the threat of evidence destruction is imminent)"

filing_fee: "Fee under the Schedule of Fees of the NCLT Rules 2016 for Section 213 applications (verify against latest schedule)."

limitation: "Residual under Article 137 of the Schedule to the Limitation Act 1963 — 3 years from accrual; continuing wrongs keep limitation alive."
```

## Section 213(a) vs Section 213(b) — choice of branch

The branch chosen determines (i) who can be the Applicant, (ii) the maintainability threshold, and (iii) the standard of pleading.

| Branch | Applicant | Threshold | Standard |
|---|---|---|---|
| Section 213(a) | Members | Not less than 100 OR holding 1/10th of total voting power | No special standard; member-status + threshold = locus |
| Section 213(b) | Any person | None | Prima-facie material on Section 213(b)(i) — (iv) grounds satisfying the Tribunal |

For Section 213(a), the Drafter pleads member-status and threshold arithmetic with particularity. For Section 213(b), the Drafter pleads the prima-facie material with documentary anchors — the application stands or falls on the quality of the material, NOT on the rhetoric.

## Tribunal's power on a Section 213 finding (Section 213 second proviso + Section 214)

After hearing the parties and finding circumstances warranting an investigation, the Tribunal "shall pass an order directing the Central Government to investigate the affairs of the company." The Central Government may, after considering the order, appoint Inspectors under Section 216 and the Inspectors investigate under Sections 217 — 219. The Tribunal's role at this stage ends with directing the investigation; the Tribunal does not itself conduct the investigation.

## Section 215 — security for costs

The Tribunal may require the Applicant to give security for an amount not exceeding the prescribed amount as security for payment of the costs of the investigation. The Drafter pre-empts the Section 215 issue with willingness to furnish security commensurate with the scope of the investigation sought.

## Less-invasive remedy framework

Before invoking Section 213, the Applicant should consider whether the lesser-impact remedies under Section 206 (power of the Registrar to call for information / inspection) or Section 207 (conduct of inspection / inquiry by the Registrar) would adequately serve the purpose. Where they would, Section 213 is disproportionate. The Drafter pleads positively to the inadequacy of the less-invasive remedies — this is the key persuasion point for the Tribunal.

## Section 213 vs SFIO investigation under Section 212

Investigation by the Serious Fraud Investigation Office (SFIO) under Section 212 is a separate, more invasive route. SFIO investigations are typically ordered by the Central Government (not the NCLT) on its own assessment of public interest. The Drafter does NOT pray for an SFIO investigation under a Section 213 application; if the grounds warrant SFIO involvement, the Applicant typically routes a separate representation to the Ministry of Corporate Affairs, not a Tribunal application.
