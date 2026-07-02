---
name: ibc-section-9-operational-creditor-application-draft
description: Draft an Application under Section 9 of the Insolvency and Bankruptcy Code 2016 by an Operational Creditor for initiation of the Corporate Insolvency Resolution Process against a Corporate Debtor before the National Company Law Tribunal. Encodes Section 8 demand-notice ingredient discipline (Form 3 / Form 4 service + 10-day reply window + no notice of pre-existing dispute) with Mobilox Innovations v. Kirusa Software (2018) 1 SCC 353 pre-existing-dispute pre-emption, Section 4 default threshold (currently ₹1 crore), Section 5(20) Operational-Creditor definition, Section 5(21) Operational-Debt definition, Section 14 moratorium, Section 60(1) territorial jurisdiction, Section 10A suspension-window check (25 March 2020 - 24 March 2021), the Innoventive Industries (2018) admission framework adapted to Section 9, and the IBBI (Application to Adjudicating Authority) Rules 2016 Form 5 filing discipline. Auto-fires on "draft Section 9 IBC", "draft operational creditor application", "draft IBC operational creditor", "draft NCLT operational creditor CIRP", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# IBC Section 9 Operational Creditor Application Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: APPLICATION UNDER SECTION 9 OF THE INSOLVENCY AND BANKRUPTCY CODE 2016 FOR INITIATION OF THE CORPORATE INSOLVENCY RESOLUTION PROCESS
case_short_code: IBC_9
case_number_prefix: C.P. (IB)
pleading_type: Company Petition (Insolvency — Operational Creditor)
typical_forum: National Company Law Tribunal of competent territorial jurisdiction under Section 60(1) IBC (NCLT within whose territorial jurisdiction the registered office of the Corporate Debtor is situated)
typical_parties: Applicant Operational Creditor (supplier / service provider / employee / contractor / workman / government department for statutory dues) + Respondent Corporate Debtor
filing_form: Form 5 of the IBBI (Application to Adjudicating Authority) Rules 2016 — supported by Part I (Particulars of Applicant), Part II (Particulars of Corporate Debtor), Part III (Particulars of Proposed Interim Resolution Professional — optional under Section 9), Part IV (Particulars of Operational Debt), Part V (Particulars of Operational-Debt-evidence documents), Part VI (Documents attached to prove the existence of operational debt and the amount in default)

statutory_opening: "This Application is filed under Section 9 of the Insolvency and Bankruptcy Code 2016 read with Rule 6 of the Insolvency and Bankruptcy Board of India (Application to Adjudicating Authority) Rules 2016, by the Applicant Operational Creditor against the Respondent Corporate Debtor, for initiation of the Corporate Insolvency Resolution Process on account of default by the Corporate Debtor in payment of an operational debt of ₹ ___ which is in excess of the threshold prescribed under Section 4 of the Code (currently ₹1 crore per Section 4 notification dated 24 March 2020). The Applicant has duly served a demand notice under Section 8 of the Code on the Respondent Corporate Debtor in Form 3 / Form 4 dated ____, the 10-day reply period whereunder expired on ____ without payment of the unpaid operational debt and without notice of pre-existing dispute."

ground_clauses:
  - "Applicant is an Operational Creditor — within the meaning of Section 5(20) IBC; the debt owed by the Corporate Debtor is an Operational Debt within the meaning of Section 5(21) IBC, being a claim in respect of provision of goods or services including employment or a debt in respect of payment of dues arising under any law for the time being in force and payable to the Central / State Government / local authority."
  - "Existence and quantum of operational debt — particulars of the supply of goods / services / employment / statutory dues, the invoices raised, the accrued debt, and the present default, are set out in Part IV of Form 5 and supported by the documents at Part V and Part VI (purchase orders / service agreements / employment contracts at Exhibit ___; invoices at Exhibit ___; statement of account at Exhibit ___; default-intimation correspondence at Exhibit ___)."
  - "Section 8 demand notice duly served — the Applicant has, on ____, served the demand notice in Form 3 / Form 4 on the Corporate Debtor at the registered office and at the address of the Corporate Debtor on record, by [registered post AD / speed post / courier / hand-delivery against acknowledgement / email-to-official-email-id]; proof of service is at Exhibit ___. The 10-day reply period whereunder expired on ____."
  - "No notice of pre-existing dispute received — within the 10-day reply window, the Corporate Debtor [(i) did not respond to the Section 8 demand notice / (ii) responded but without bringing to the notice of the Applicant any existence of a dispute, if any, and a record of the pendency of a suit or arbitration proceeding filed before the receipt of the demand notice in relation to the dispute (Section 8(2)(a))]; the alleged dispute [if pleaded] is not a pre-existing dispute within Mobilox Innovations Pvt. Ltd. v. Kirusa Software Pvt. Ltd. (2018) 1 SCC 353, as it is unsupported by any material, was raised only after receipt of the Section 8 notice, and is a sham defence not satisfying the 'plausible contention requiring further investigation' test."
  - "Default has occurred — the Corporate Debtor has committed a default within the meaning of Section 3(12) IBC, by failing to make payment of the Operational Debt on the date of default being ____. The aggregate amount in default is ₹ ___, which is in excess of the threshold of ₹1 crore prescribed under Section 4 IBC."
  - "Innoventive admission framework — under Innoventive Industries v. ICICI Bank (2018) 1 SCC 407, the NCLT at admission is required to satisfy itself only that (a) default has occurred, (b) the application is complete, and (c) no disciplinary proceedings are pending against the proposed IRP (where one is proposed). Merits of any dispute about the operational debt are not the subject of inquiry at the admission stage."
  - "Section 10A bar inapplicable — the default did not occur during the Section 10A suspension window (25 March 2020 — 24 March 2021); the present cause of action is post-suspension."
  - "Limitation — the Application is filed within three years from the date of default per Article 137 of the Schedule to the Limitation Act 1963; for operational debt the limitation runs from the date of default (i.e., the date of expiry of the credit period for the relevant invoice / the date the relevant statutory due fell due / the date the last salary became payable), not from the invoice-date in isolation."
  - "Proposed Interim Resolution Professional (where proposed) — the Applicant proposes [Proposed-IRP-Name], registered with IBBI under registration No. [Registration-Placeholder], who has furnished a written communication in Form 2 of the IBBI (CIRP for Corporate Persons) Regulations 2016 consenting to act as Interim Resolution Professional (Exhibit ___). [Where IRP is NOT proposed by the Operational Creditor — as is permissible under Section 9(4) — the Applicant prays for direction to IBBI to nominate an IRP from its panel.]"

prayer_clauses:
  - "(a) Admit this Application under Section 9(5)(i) IBC and pass an order initiating the Corporate Insolvency Resolution Process in respect of the Corporate Debtor;"
  - "(b) Declare moratorium under Section 14 IBC in respect of the Corporate Debtor with effect from the date of admission;"
  - "(c) [Where IRP proposed] Appoint [Proposed IRP] as the Interim Resolution Professional with such directions as this Tribunal may consider appropriate, including directions for the public announcement under Section 13(1) IBC and the constitution of the Committee of Creditors under Section 21 IBC; / [Where no IRP proposed] Direct the IBBI to recommend the name of an Insolvency Professional from its panel to be appointed as the Interim Resolution Professional;"
  - "(d) Direct that the Corporate Debtor shall extend all assistance to the Interim Resolution Professional in accordance with Sections 17, 18, and 19 IBC."

mandatory_exhibits:
  - purchase_order_or_service_agreement_or_employment_contract_or_statutory_due_basis
  - invoices_raised_on_the_corporate_debtor_with_dates
  - statement_of_account_showing_outstanding_operational_debt
  - default_intimation_correspondence_or_reminder_letters
  - section_8_demand_notice_in_form_3_or_form_4
  - proof_of_service_of_section_8_demand_notice_postal_courier_email
  - corporate_debtor_response_to_section_8_notice_if_any
  - certified_master_data_of_corporate_debtor_from_mca
  - written_consent_in_form_2_from_proposed_irp_where_applicable
  - registration_certificate_of_proposed_irp_with_ibbi_where_applicable
  - fee_receipt_under_schedule_to_ibbi_aaa_rules_2016
  - board_resolution_or_power_of_attorney_authorising_the_applicant_to_file_the_application

accompanying_applications:
  - "I.A. for ad-interim moratorium pending hearing (admission ordinarily triggers Section 14 moratorium automatically; this I.A. is filed where the gap between filing and admission is expected to be long and urgent protection is needed)"
  - "I.A. for urgent listing"
  - "I.A. for direction to IBBI to nominate an IRP (where no IRP proposed in Part III of Form 5)"
  - "I.A. for any specific direction (e.g. directions to the Corporate Debtor to hand over books of account / records to the IRP)"

filing_fee: "Fee under the Schedule to the IBBI (Application to Adjudicating Authority) Rules 2016 — ₹25,000 for a Section 9 application by an Operational Creditor (verify current schedule before filing). Paid through the NCLT's online portal / by demand draft as required by the bench."

limitation: "Three years from the date of default per Article 137 Limitation Act 1963. For operational debt the date of default is the date of expiry of the credit period on the relevant invoice / the date the statutory due fell due / the date the last salary became payable. Section 18 Limitation Act acknowledgement may extend limitation; the Drafter pleads any such acknowledgement with documentary anchor."
```

## Section 8 demand-notice discipline (Mobilox-style)

Section 8 of the IBC requires the Operational Creditor to deliver a demand notice in Form 3 (claim with default amount supported by documentary evidence) or Form 4 (claim with invoices) to the Corporate Debtor at the registered office, demanding payment of the unpaid operational debt within 10 days. The 10-day reply window is the **statutory firewall** within which the Corporate Debtor may bring to the notice of the Operational Creditor:

- **Existence of a dispute, if any** (with record of pendency of a suit / arbitration before receipt of the demand notice in relation to such dispute) — Section 8(2)(a), OR
- **The payment of the unpaid operational debt** (by sending an attested copy of the record of electronic transfer / sending an attested copy of record that the operational creditor has encashed a cheque) — Section 8(2)(b)

If neither is received within the 10-day window, the Operational Creditor may file the Section 9 application. The Drafter pleads positively to: (i) the Form 3 / Form 4 compliance; (ii) the service mode and date; (iii) the expiry of the 10-day window without payment AND without notice of pre-existing dispute.

## Mobilox Innovations — pre-existing-dispute test

*Mobilox Innovations Pvt. Ltd. v. Kirusa Software Pvt. Ltd.* (2018) 1 SCC 353 — the test for "existence of dispute" under Section 8(2)(a) is whether the dispute truly exists in fact and is not spurious, hypothetical, or illusory; the merits of the dispute are not adjudicated at admission stage.

The Drafter pre-empts the *Mobilox* defence by positively pleading on the record:

- No reply to the Section 8 notice (where applicable); OR
- The reply does not raise any pre-existing dispute supported by material; OR
- The alleged dispute is illusory / hypothetical / raised only after receipt of the Section 8 notice (with documentary anchor showing absence of any prior dispute on the same matter); OR
- The alleged dispute is unsupported by any pending suit / arbitration filed before receipt of the demand notice

Quantum of the dispute is not the question — even a small but genuinely pre-existing dispute defeats Section 9 admission per *Mobilox*. Hence the heart of the Drafter's work is anchoring the absence of prior dispute, NOT the magnitude of the operational debt.

## Section 9(4) — IRP proposal is optional for Operational Creditor

Unlike Section 7 (Financial Creditor — IRP proposal is mandatory under Section 7(3)(b)), under Section 9 the Operational Creditor MAY but is NOT required to propose an IRP. Where no IRP is proposed, the NCLT shall direct the IBBI to recommend the name of an Insolvency Professional from its panel within the prescribed period. The Drafter chooses the route based on the applicant's commercial position (proposing an IRP signals seriousness and accelerates the timeline; leaving the IRP to IBBI is administratively simpler).

## Section 10A — suspension window check

Section 10A IBC bars the filing of any Section 7 / Section 9 / Section 10 application in respect of any default arising during the period **25 March 2020 to 24 March 2021**. The Drafter pleads positively that the date of default is outside the Section 10A window. Where the relevant invoice falls within the window but earlier defaults / later defaults on the same continuing course of dealing fall outside, the Drafter anchors the application on the outside-window default with arithmetic support.

## Default-threshold discipline

The current default threshold under Section 4 IBC is ₹1 crore (per the notification dated 24 March 2020). The Drafter pleads the threshold compliance with specificity — the aggregate operational debt in default must equal or exceed ₹1 crore. Aggregation across multiple invoices / accounts of the same Operational Creditor against the same Corporate Debtor is permissible; aggregation across different Operational Creditors is not.

## Distinction from Section 7 IBC (lives in the banking plugin)

| Feature | Section 7 (Banking plugin) | Section 9 (This plugin) |
|---|---|---|
| Applicant | Financial Creditor | Operational Creditor |
| Debt type | Financial debt (Section 5(8)) | Operational debt (Section 5(21)) |
| IRP proposal | Mandatory | Optional |
| Demand-notice precondition | None | Section 8 demand notice mandatory |
| Pre-existing-dispute defence | Limited (Innoventive only) | Available + powerful (Mobilox) |
| Form | Form 1 | Form 5 |

The Drafter does NOT conflate the two routes. Financial debts (bank loans / NBFC facilities / debentures / financial guarantees) belong to Section 7 and are drafted via the banking plugin. Operational debts (supplies / services / employment / statutory dues) belong to Section 9 and are drafted via this skill.
