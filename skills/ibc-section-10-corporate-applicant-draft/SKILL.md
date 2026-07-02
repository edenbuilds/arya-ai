---
name: ibc-section-10-corporate-applicant-draft
description: Draft an Application under Section 10 of the Insolvency and Bankruptcy Code 2016 by a Corporate Applicant / Corporate Debtor for self-initiation of the Corporate Insolvency Resolution Process against itself before the National Company Law Tribunal. Encodes Section 10(3) authorisation discipline (special resolution of members under Section 10(3)(c) read with Section 114(2) Companies Act 2013 — 3/4 majority; or 3/4 of partners for an LLP), Section 10(3)(a) particulars of debt and default, Section 10(3)(b) proposed IRP with written consent in Form 2, Section 10(4) admission framework, Section 11 ineligibility regime, Section 65 fraudulent / malicious initiation pre-emption, Section 4 default threshold (currently ₹1 crore), Section 14 moratorium, and Form 6 filing discipline under the IBBI (Application to Adjudicating Authority) Rules 2016. Auto-fires on "draft Section 10 IBC", "draft corporate applicant CIRP", "draft self-initiation CIRP", "draft NCLT corporate applicant", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# IBC Section 10 Corporate Applicant Self-Initiation Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: APPLICATION UNDER SECTION 10 OF THE INSOLVENCY AND BANKRUPTCY CODE 2016 BY A CORPORATE APPLICANT FOR INITIATION OF THE CORPORATE INSOLVENCY RESOLUTION PROCESS
case_short_code: IBC_10
case_number_prefix: C.P. (IB)
pleading_type: Company Petition (Insolvency — Corporate Applicant)
typical_forum: National Company Law Tribunal of competent territorial jurisdiction under Section 60(1) IBC (NCLT within whose territorial jurisdiction the registered office of the Corporate Applicant is situated)
typical_parties: Applicant Corporate Applicant / Corporate Debtor (the company itself, through its authorised signatory pursuant to the special resolution under Section 10(3)(c))
filing_form: Form 6 of the IBBI (Application to Adjudicating Authority) Rules 2016 — supported by Part I (Particulars of the Corporate Applicant), Part II (Particulars of the Proposed Interim Resolution Professional), Part III (Particulars of Debt — schedule of financial debt, operational debt, employee dues, statutory dues), Part IV (Documents in support — including special resolution / partners' resolution, audited financial statements, list of creditors with debt schedule, Form 2 consent of proposed IRP, IBBI registration certificate of proposed IRP)

statutory_opening: "This Application is filed under Section 10 of the Insolvency and Bankruptcy Code 2016 read with Rule 7 of the IBBI (Application to Adjudicating Authority) Rules 2016, by the Applicant Corporate Applicant / Corporate Debtor, supported by the special resolution of the members dated ____ passed under Section 10(3)(c) of the Code read with Section 114(2) of the Companies Act 2013, for initiation of the Corporate Insolvency Resolution Process in respect of the Applicant itself, on account of default by the Applicant in payment of a debt of ₹ ___ which is in excess of the threshold prescribed under Section 4 of the Code (currently ₹1 crore per Section 4 notification dated 24 March 2020)."

ground_clauses:
  - "Authority of the Tribunal — Section 10 of the Insolvency and Bankruptcy Code 2016 read with Rule 7 of the IBBI (Application to Adjudicating Authority) Rules 2016 vests jurisdiction in the National Company Law Tribunal to admit a Corporate Applicant's self-initiation of CIRP."
  - "Jurisdictional anchor — the registered office of the Applicant is within the territorial limits of this Bench under Section 60(1) IBC."
  - "Section 10(3)(c) authorisation duly passed — the Applicant's members, in an Extraordinary General Meeting held on ____, passed a special resolution under Section 10(3)(c) of the Code read with Section 114(2) of the Companies Act 2013, authorising the Applicant to initiate CIRP under Section 10 against itself; certified copy of the resolution along with the explanatory statement under Section 102 of the Companies Act 2013 is at Exhibit ___. [Where the Applicant is an LLP, the resolution of three-fourths of the partners under Section 10(3)(c) proviso is at Exhibit ___.]"
  - "Section 10(3)(a) particulars of debt and default — particulars of the financial debt, operational debt, employee dues, and statutory dues of the Applicant, the dates of default, and the aggregate amount in default (₹ ___) are set out in Part III of Form 6 and supported by the audited financial statements at Exhibit ___ and the list of creditors at Exhibit ___."
  - "Section 10(3)(b) proposed IRP — the Applicant proposes [Proposed-IRP-Name], registered with IBBI under registration No. [Registration-Placeholder], who has furnished written consent in Form 2 of the IBBI (CIRP for Corporate Persons) Regulations 2016 to act as Interim Resolution Professional (Exhibit ___); the proposed IRP has no disciplinary proceedings pending and is otherwise eligible to be appointed."
  - "Section 11 ineligibility does not apply — the Applicant positively pleads that: (a) the Applicant is not undergoing a CIRP under the Code, nor is it the subject of any liquidation order, nor has a resolution plan in respect of the Applicant been approved under Section 31 in the 12 months immediately preceding the date of this Application; (b) the Applicant has not defaulted under any resolution plan approved in the past; (c) the Applicant is not a wilful defaulter under Section 29A read with the RBI Master Circular on Wilful Defaulters; (d) the Applicant is not otherwise disqualified under Section 11 IBC."
  - "Section 65 IBC pre-emption — the present Application is filed bona fide, in the interest of all stakeholders of the Applicant, and is not initiated fraudulently or with malicious intent for any purpose other than the resolution of insolvency. The Applicant disclaims any intent to misuse the IBC process to defeat creditor remedies under any other law; the present Application is the considered commercial judgment of the Board and the members."
  - "Default has occurred — the Applicant has committed a default within the meaning of Section 3(12) IBC, by failing to make payment of the debt on the date of default being ____. The aggregate amount in default is ₹ ___, which is in excess of the threshold of ₹1 crore prescribed under Section 4 IBC."
  - "Section 10A bar inapplicable — the default did not occur during the Section 10A suspension window (25 March 2020 — 24 March 2021); the present cause of action is post-suspension."
  - "Limitation — the Application is filed contemporaneously with the crystallisation of the default and the passing of the special resolution; no extended limitation issues arise."

prayer_clauses:
  - "(a) Admit this Application under Section 10(4) IBC and pass an order initiating the Corporate Insolvency Resolution Process in respect of the Applicant;"
  - "(b) Declare moratorium under Section 14 IBC in respect of the Applicant with effect from the date of admission;"
  - "(c) Appoint [Proposed IRP] as the Interim Resolution Professional with such directions as this Tribunal may consider appropriate, including directions for the public announcement under Section 13(1) IBC and the constitution of the Committee of Creditors under Section 21 IBC;"
  - "(d) Direct the management and Directors of the Applicant to extend all assistance to the Interim Resolution Professional in accordance with Sections 17, 18, and 19 IBC, including (i) handing over of books of account / records / control of business; (ii) full disclosure of assets / liabilities / receivables / contracts; (iii) cooperation in the public announcement and the call for claims;"

mandatory_exhibits:
  - memorandum_of_association_and_articles_of_association
  - certificate_of_incorporation
  - latest_audited_financial_statements_three_years
  - latest_annual_return_mgt_7
  - register_of_charges_under_section_85
  - special_resolution_under_section_10_3_c_with_explanatory_statement_under_section_102
  - notice_of_egm_at_which_special_resolution_was_passed
  - certified_minutes_of_egm
  - mca_or_roc_filing_reference_of_the_special_resolution_form_mgt_14
  - list_of_creditors_with_full_particulars_including_financial_operational_employee_statutory
  - statement_of_debt_default_with_arithmetic
  - written_consent_in_form_2_from_proposed_irp
  - registration_certificate_of_proposed_irp_with_ibbi
  - section_29a_declaration_from_proposed_irp_re_disqualification
  - declaration_under_section_11_that_section_11_disqualifications_do_not_apply
  - declaration_under_section_65_that_the_application_is_bona_fide
  - fee_receipt_under_schedule_to_ibbi_aaa_rules_2016

accompanying_applications:
  - "I.A. for ad-interim moratorium pending hearing"
  - "I.A. for urgent listing (where the financial distress is acute and protection from creditor actions is urgent)"
  - "I.A. for confidentiality directions on commercial-sensitive information in the application record"
  - "I.A. for any specific direction relating to handover of records / books / control to the IRP"

filing_fee: "Fee under the Schedule to the IBBI (Application to Adjudicating Authority) Rules 2016 — ₹25,000 for a Section 10 application by a Corporate Applicant (verify current schedule before filing). Paid through the NCLT's online portal / by demand draft as required by the bench."

limitation: "Section 10 applications are filed contemporaneously with the crystallisation of default and the special resolution; no specific limitation arises as in Section 7 / Section 9, but the application must be brought in good faith without inordinate delay between default and filing (delay attracts Section 65 scrutiny)."
```

## Section 10(3) — authorisation requirements

Section 10(3) lays out three documentary requirements that the Corporate Applicant MUST file along with the Application:

- **Section 10(3)(a)** — its books of account and such other documents relating to such period as may be specified
- **Section 10(3)(b)** — the name of the resolution professional proposed to be appointed as an interim resolution professional (with the proposed IRP's written consent in Form 2 of the CIRP Regulations 2016)
- **Section 10(3)(c)** — a special resolution passed by shareholders of the corporate debtor or the resolution passed by at least three-fourths of the total number of partners of the corporate debtor, as the case may be, approving the filing of the application

The Drafter verifies each is filed in original / certified copy.

## Section 10(4) — admission framework

The NCLT under Section 10(4) shall, within fourteen days of the receipt of the application, by an order:

- **Admit** the application, if it is complete and no disciplinary proceeding is pending against the proposed IRP; OR
- **Reject** the application, if it is incomplete or any disciplinary proceeding is pending against the proposed IRP

Before rejection, the NCLT shall give a notice to the applicant to rectify the defects in his application within seven days from the date of receipt of such notice from the NCLT.

The admission threshold mirrors Section 7 / Section 9 (Innoventive framework) — only completeness + IRP eligibility, not merits of debt-dispute.

## Section 11 — ineligibility regime

Section 11 IBC disqualifies certain persons from filing CIRP applications:

- **Section 11(a)** — a corporate debtor undergoing a corporate insolvency resolution process
- **Section 11(b)** — a corporate debtor having completed corporate insolvency resolution process twelve months preceding the date of making of the application
- **Section 11(c)** — a corporate debtor or a financial creditor who has violated any of the terms of resolution plan which was approved twelve months before the date of making of an application under this Chapter
- **Section 11(d)** — a corporate debtor in respect of whom a liquidation order has been made

The Drafter pleads positively that the Applicant is NOT within any Section 11 disqualification. A false Section 11 declaration attracts Section 65 + penal consequences.

## Section 65 — pre-emption of malicious / fraudulent initiation

Section 65 IBC penalises any person who initiates the insolvency resolution process or liquidation proceedings fraudulently or with malicious intent for any purpose other than the resolution of insolvency or liquidation, as the case may be — with a fine ranging from ₹1 lakh to ₹1 crore. The Drafter pre-empts Section 65 by positively pleading the bona fide nature of the Application — financial distress is real, default has crystallised, all stakeholders' interests are served by CIRP, and there is no intent to misuse the IBC to defeat creditor actions under SARFAESI / DRT / recovery suits.

Common Section 65 attack vectors the Overseer surfaces:
- Filing Section 10 while a creditor's Section 7 / Section 9 is pending or imminent (forum-shopping suspicion)
- Filing Section 10 in proximity to enforcement actions under SARFAESI (defeating-creditor suspicion)
- Pattern of repeated Section 10 attempts with prior dismissals
- Disproportionate gap between default-date and filing-date without explanation

## Section 29A and the corporate-applicant context

Section 29A IBC disqualifies certain persons from being eligible to submit a resolution plan. While Section 29A primarily applies to RP-stage plan submission, its shadow falls on Section 10 — promoters of a corporate applicant who would themselves be Section 29A-disqualified from re-acquiring the debtor through CIRP should think twice before initiating Section 10, as the resolution plan they hope for may exclude them. The Drafter does NOT advise on the Section 29A merits in the pleading body but ensures the Section 10 application does not preview any plan-strategy that would be Section 29A-defeated.

## CIRP timeline awareness — Section 12 IBC

Once admitted, CIRP must be completed within 180 days from CIRP commencement, extendable to 330 days (Section 12 read with the 2019 amendment). The Drafter's awareness of the timeline informs the prayer-clause structure (no relief that conflicts with the statutory cadence) and informs the proposed-IRP's resource-readiness verification.
