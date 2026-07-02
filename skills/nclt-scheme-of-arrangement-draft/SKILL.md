---
name: nclt-scheme-of-arrangement-draft
description: Draft a Scheme of Arrangement / Compromise / Amalgamation / Merger / Demerger Application before the National Company Law Tribunal under Sections 230, 231 and 232 of the Companies Act 2013 read with the Companies (Compromises, Arrangements and Amalgamations) Rules 2016. Two-stage procedure — First-Motion Application for direction to convene meetings under Section 230(1), then Second-Motion Petition for sanction under Section 230(6) / Section 232(3). Encodes the Section 230(2) disclosure obligations, Section 230(3) valuation-report requirement, Section 230(5) regulator-notice requirement (Central Government / RBI / SEBI / CCI / Income-tax / ROC / Official Liquidator / stock exchanges), and the Section 232 merger / amalgamation framework including cross-border merger under Section 234. Auto-fires on "draft scheme of arrangement", "draft Section 230 scheme", "draft merger application", "draft amalgamation petition", "draft demerger application", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# NCLT Scheme of Arrangement Draft Skill (Sections 230 - 232 Companies Act 2013)

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: APPLICATION / PETITION UNDER SECTIONS 230 TO 232 OF THE COMPANIES ACT 2013 READ WITH THE COMPANIES (COMPROMISES, ARRANGEMENTS AND AMALGAMATIONS) RULES 2016
case_short_code: NCLT_230_232
case_number_prefix_first_motion: C.A. (CAA)
case_number_prefix_second_motion: C.P. (CAA)
pleading_type: Application (First Motion) / Petition (Second Motion / Sanction)
typical_forum: NCLT of competent territorial jurisdiction (registered office of each company that is party to the scheme; consolidated where possible)
typical_parties: Applicant Company / Companies (Transferor + Transferee in amalgamation / merger / demerger; Demerging + Resulting in demerger; the Scheme-promoting company in a Section 230 compromise with creditors) + creditors / members served notice pursuant to Section 230(1) directions

statutory_opening_first_motion: "This Application is filed under Section 230(1) of the Companies Act 2013 read with Rule 3 of the Companies (Compromises, Arrangements and Amalgamations) Rules 2016, by the Applicant Company / Companies, seeking directions of this Tribunal for convening meetings of [equity shareholders / preference shareholders / secured creditors / unsecured creditors / class-as-applicable] for the purpose of considering and, if thought fit, approving the proposed Scheme of [Arrangement / Compromise / Amalgamation / Merger / Demerger / Capital-Reduction-cum-Buy-Back] annexed hereto."
statutory_opening_second_motion: "This Petition is filed under Section 230(6) / Section 232(3) of the Companies Act 2013 read with Rule 15 of the Companies (Compromises, Arrangements and Amalgamations) Rules 2016, for sanction of the Scheme of [Arrangement / etc.] annexed hereto, which has been approved by the [majority in number representing 3/4ths in value] of the [creditors / class of creditors / members / class of members] of the Applicant Company / Companies at the meetings convened pursuant to the order of this Tribunal dated ____ in C.A. (CAA) No. ____ of ____."

ground_clauses:
  - "Authority of the Tribunal — Sections 230 to 232 of the Companies Act 2013 vest jurisdiction in the National Company Law Tribunal to direct meetings under Section 230(1) and to sanction schemes under Section 230(6) / Section 232(3); the erstwhile High Court jurisdiction under Sections 391 to 394 of the Companies Act 1956 stood transferred to the NCLT with effect from 15 December 2016."
  - "Jurisdictional anchor — the registered office of each Applicant Company is within the territorial limits of this Bench (Rule 18 of the NCLT Rules 2016)."
  - "Section 230(2) disclosures made — the Applicant Company / Companies have disclosed by affidavit: (i) all material facts relating to the company including latest financial position, latest auditor's report, pendency of any investigation or proceedings against the company; (ii) reduction of share capital, if any, included in the Scheme; (iii) any scheme of corporate debt restructuring consented to by not less than 75% of the secured creditors in value, with the prescribed statements; (iv) valuation report by a registered valuer under Section 230(3); (v) notices issued to the regulators under Section 230(5)."
  - "Section 230(5) regulator-notices issued — notices have been served on the Central Government, RBI (where applicable), SEBI (where applicable), Registrar of Companies, Income-tax authorities, Competition Commission of India (where applicable — threshold under Section 5 of the Competition Act 2002), Official Liquidator (where applicable), and the stock exchanges (where applicable), each with 30 days to make their representations."
  - "Scheme is bona fide and not contrary to public policy — the Scheme is a genuine commercial arrangement supported by valuation, fairness opinion (where applicable), and the requisite Board approvals of each Applicant Company; the Scheme does not have the effect of evading any statutory obligation."
  - "Limitation — there is no statutory limitation on first-motion / second-motion applications under Section 230-232; the Application is filed contemporaneously with the commercial readiness of the Scheme."

prayer_clauses_first_motion:
  - "(a) Direct the convening of separate meetings of the [equity shareholders / preference shareholders / secured creditors / unsecured creditors / class-as-applicable] of the Applicant Company / Companies for the purpose of considering and, if thought fit, approving the Scheme annexed hereto;"
  - "(b) Appoint a Chairperson and an Alternate Chairperson for each meeting, and a Scrutinizer to assist the Chairperson with the conduct of voting;"
  - "(c) Direct that notice of the meetings, along with the Scheme, the explanatory statement under Section 230(3), the valuation report, and the requisite annexures, be sent by post / electronic mode to every member / creditor entitled to attend, and be published in two newspapers (one English and one vernacular circulating in the district where the registered office of the Applicant Company is situated);"
  - "(d) Dispense with the meetings of [class of creditors / members] from whom written consents in the prescribed form representing not less than 90% in value have been obtained (where applicable per Rule 6(3) of the 2016 Rules);"
  - "(e) Direct service of the Scheme + notice on the regulators under Section 230(5) — Central Government / RBI / SEBI / ROC / Income-tax / CCI / Official Liquidator / stock exchanges as applicable;"

prayer_clauses_second_motion:
  - "(a) Sanction the Scheme of [Arrangement / etc.] annexed hereto, with such modifications as this Tribunal may consider necessary, with effect from the Appointed Date specified in the Scheme;"
  - "(b) Direct that the Order of sanction be filed with the Registrar of Companies in Form INC-28 within the prescribed period;"
  - "(c) Direct that all property, rights, liabilities, and obligations of the Transferor Company / Demerging Company shall stand transferred to and vested in the Transferee Company / Resulting Company in accordance with the Scheme and Section 232(3);"
  - "(d) Direct that all proceedings pending by or against the Transferor Company / Demerging Company be continued by or against the Transferee Company / Resulting Company;"
  - "(e) Order dissolution without winding-up of the Transferor Company / Demerging Company under Section 232(3)(d) (where applicable);"

mandatory_exhibits:
  - memorandum_of_association_and_articles_of_association_of_each_applicant_company
  - certificate_of_incorporation_of_each_applicant_company
  - latest_audited_financial_statements_three_years_of_each_applicant_company
  - latest_annual_return_mgt_7_of_each_applicant_company
  - the_scheme_of_arrangement_or_compromise_or_amalgamation_or_merger_or_demerger
  - explanatory_statement_under_section_230_3
  - valuation_report_by_registered_valuer_under_section_230_3
  - fairness_opinion_where_applicable
  - auditor_certificate_on_accounting_treatment_under_indas
  - board_resolutions_of_each_applicant_company_approving_the_scheme
  - share_exchange_ratio_workings_for_amalgamation_or_demerger
  - statement_of_assets_and_liabilities_of_each_applicant_company_pre_scheme
  - list_of_creditors_with_consents_or_unsatisfied_creditors_under_section_66_where_capital_reduction_included
  - notice_to_regulators_under_section_230_5

accompanying_applications:
  - "I.A. for dispensation of meetings (per Rule 6(3) where 90% creditor consent obtained)"
  - "I.A. for directions on advertisement / publication of meeting notices"
  - "I.A. for issuance of notice to regulators under Section 230(5)"
  - "I.A. for confidentiality directions (where sensitive commercial information is part of the scheme record)"
  - "I.A. for short-notice meeting (where time-criticality of the scheme is demonstrated)"
  - "I.A. for urgent listing of the second-motion petition post completion of meetings"

filing_fee: "Fee under the Schedule of Fees of the NCLT Rules 2016 for first-motion and second-motion applications / petitions (verify against latest schedule). Stamp duty on the Scheme order under the applicable State Stamp Act for transferor / transferee where immovable property is included in the scheme assets."

limitation: "No specific limitation; the application is filed contemporaneously with the commercial readiness of the scheme. The second-motion petition is filed after the meetings ordered at first motion have approved the Scheme (typically within 7 days of receipt of the meeting Chairperson's report per Rule 14 of the 2016 Rules)."
```

## Section 232 — merger / amalgamation specific discipline

For schemes under Section 232 (merger / amalgamation between two or more companies), additional disclosures and protections:

- Draft scheme of merger / amalgamation must be approved by the Board of each company
- Auditor's certificate on accounting treatment in accordance with the Indian Accounting Standards (Ind AS)
- Section 232(3)(c) — provisions for transfer of employees of the Transferor Company to the Transferee Company on terms not less favourable
- Section 232(3)(d) — dissolution without winding-up of the Transferor Company
- Section 232(3)(e) — incidents to facilitate the merger including (where applicable) any necessary modifications to the Memorandum / Articles of the Transferee Company
- Section 232(6) — Appointed Date for the merger to take effect

## Section 233 — fast-track merger

Where the scheme involves merger between two or more small companies / between a holding company and its wholly-owned subsidiary / such other class of companies as may be prescribed, Section 233 permits a fast-track merger before the Regional Director (not the NCLT). The fast-track route is OUTSIDE the scope of this skill — the present skill covers the regular Section 230-232 route. Where the parties qualify for Section 233, the appropriate filing is a Section 233 application before the Regional Director, not a Section 230 application before the NCLT.

## Section 234 — cross-border merger

Cross-border mergers (Indian company merging with foreign company / foreign company merging with Indian company) are governed by Section 234 of the Companies Act 2013 read with the Companies (Compromises, Arrangements and Amalgamations) Rules 2016 (Rule 25A in particular) and the FEMA (Cross Border Merger) Regulations 2018 of the RBI. The Drafter pleads the Section 234 / Rule 25A / FEMA framework where the scheme is cross-border.

## Schemes involving capital reduction within Section 230

Where the Scheme includes a reduction of share capital, Section 230(2)(c) requires the Section 66 compliance to be subsumed into the Section 230 Scheme (single-window sanction). The Drafter pleads the Section 66 creditor-protection particulars within the Section 230 application — separate Section 66 filing is not required where the reduction is part of an approved Section 230 Scheme.

## Schemes involving SEBI-listed companies

Where one or more Applicant Companies are listed on a stock exchange, the SEBI (Listing Obligations and Disclosure Requirements) Regulations 2015 (LODR — Regulation 37 and Master Circular on Schemes of Arrangement by Listed Entities) apply. The stock exchange / SEBI must issue a no-objection letter under the LODR before the second-motion sanction. The Drafter ensures the LODR no-objection is exhibited.

## Innoventive moratorium does not bar Section 230

Section 230-232 is COMPANY-INITIATED; the moratorium under Section 14 IBC does not bar the company from approaching the NCLT under Section 230 even where CIRP is pending. However, Section 30 IBC permits resolution plans that may include compromise / arrangement features functionally similar to Section 230 — the Drafter checks for forum-coherence before proceeding with a parallel Section 230 application.
