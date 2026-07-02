---
name: nclt-section-252-revival-struck-off-company-draft
description: Draft an Appeal under Section 252(1) or an Application under Section 252(3) of the Companies Act 2013 for restoration of the name of a company struck off the Register of Companies under Section 248 by the Registrar of Companies. Encodes the Section 252(1) 3-year appeal limitation for the company and the Section 252(3) 20-year application limitation for the company / any member / creditor / workman, with discipline on documentary evidence of the company "carrying on business or in operation" at the time of strike-off. Auto-fires on "draft Section 252 revival", "draft restoration of company", "draft restoration petition", "draft revive struck off company", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# NCLT Section 252 Revival / Restoration of Struck-Off Company Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: APPEAL / APPLICATION UNDER SECTION 252 OF THE COMPANIES ACT 2013 READ WITH RULE 87A OF THE NCLT RULES 2016 AND RULE 11 OF THE COMPANIES (REMOVAL OF NAMES OF COMPANIES FROM THE REGISTER OF COMPANIES) RULES 2016
case_short_code: NCLT_252
case_number_prefix: C.P.
pleading_type: Appeal under Section 252(1) / Application under Section 252(3)
typical_forum: NCLT of competent territorial jurisdiction (registered office of the struck-off company as it stood prior to strike-off)
typical_parties: Petitioner Company / Member / Creditor / Workman + Respondent Registrar of Companies (and the Central Government where the strike-off was on the application of the company)

statutory_opening_252_1: "This Appeal is filed under Section 252(1) of the Companies Act 2013, by the Petitioner Company against the order dated ____ passed by the Respondent Registrar of Companies under Section 248(5) of the Companies Act 2013 striking off the name of the Petitioner Company from the Register of Companies, and consequent publication in the Official Gazette dated ____, on the ground that the said order is not justified in the facts and circumstances of the case."
statutory_opening_252_3: "This Application is filed under Section 252(3) of the Companies Act 2013 read with Rule 87A of the NCLT Rules 2016 and Rule 11 of the Companies (Removal of Names of Companies from the Register of Companies) Rules 2016, by the Petitioner [Company / Member / Creditor / Workman] seeking restoration of the name of the [name of company] (CIN: ____) to the Register of Companies maintained by the Respondent Registrar of Companies on the ground that the said Company was, at the time of its name being struck off, carrying on business or in operation / on the ground that it is otherwise just that the name of the Company be restored."

ground_clauses:
  - "Authority of the Tribunal — Section 252 of the Companies Act 2013 vests jurisdiction in the National Company Law Tribunal to direct restoration of a struck-off company; the erstwhile High Court jurisdiction under Section 560(6) of the Companies Act 1956 stood transferred to the NCLT with effect from 15 December 2016."
  - "Jurisdictional anchor — the registered office of the [name of company] was situated within the territorial limits of this Bench at the time the name was struck off (Rule 18 of the NCLT Rules 2016)."
  - "Standing — the Petitioner is [the Company itself through its directors / a member of the Company / a creditor of the Company / a workman of the Company], having locus to bring the present [Appeal / Application] under Section 252."
  - "Limitation — [the Appeal is filed within 3 years from the date of the strike-off order under Section 252(1) / the Application is filed within 20 years from the publication of the strike-off notice in the Official Gazette under Section 252(3)]."
  - "Evidence of carrying on business or in operation — at the time of strike-off, the Company was carrying on business / was in operation, as evidenced by: (i) bank statements of the Company's bank accounts during the period prior to strike-off (Exhibit ___); (ii) GST returns filed by the Company (Exhibit ___); (iii) income-tax returns filed by the Company (Exhibit ___); (iv) statutory filings under Sections 92 and 137 of the Companies Act 2013 — annual return and financial statements (Exhibit ___); (v) statutory filings of provident fund / ESI / employer-statutory dues (Exhibit ___); (vi) lease deeds / service contracts in operation (Exhibit ___); (vii) employer-employee payroll records (Exhibit ___)."
  - "Just to restore — even where evidence of operation is limited, it is just and equitable to restore the Company's name to enable [recovery of outstanding receivables / completion of pending statutory obligations / enforcement of pre-strike-off contracts / continuation of statutory proceedings to which the Company is a party]."
  - "Willingness to remedy default — the Company / its directors undertake to file all overdue statutory returns within such period as the Tribunal may direct, and to pay all statutory dues including ROC filing fees, additional fees, late-filing fees, and any other dues as the Tribunal may determine."

prayer_clauses:
  - "(a) [Set aside / quash] the order dated ____ of the Respondent Registrar of Companies striking off the name of the [name of company] from the Register of Companies under Section 248(5), and direct restoration of the name of the [name of company] (CIN: ____) to the Register of Companies (under Section 252(1)) / Restore the name of the [name of company] (CIN: ____) to the Register of Companies (under Section 252(3));"
  - "(b) Direct the Respondent Registrar of Companies to publish the Order of restoration in the Official Gazette under Section 252(3) proviso;"
  - "(c) Direct the Company to file all overdue Annual Returns under Section 92 and Financial Statements under Section 137 of the Companies Act 2013 within such period as this Tribunal may direct, on payment of the applicable additional fees and late-filing fees;"
  - "(d) Direct that on restoration, the Company shall be deemed never to have had its name struck off, and any acts done by or on behalf of the Company in the interim period shall be deemed to have been validly done;"
  - "(e) Direct payment of such costs as this Tribunal may determine to the Respondent Registrar of Companies for the procedural inconvenience occasioned by the strike-off and restoration cycle;"

mandatory_exhibits:
  - certificate_of_incorporation_of_the_struck_off_company
  - memorandum_of_association_and_articles_of_association
  - registrar_of_companies_strike_off_order_under_section_248_5
  - official_gazette_publication_of_strike_off
  - latest_annual_return_mgt_7_pre_strike_off
  - latest_audited_financial_statements_pre_strike_off
  - bank_statements_of_the_company_during_period_prior_to_strike_off
  - gst_returns_filed_during_period_prior_to_strike_off
  - income_tax_returns_filed_during_period_prior_to_strike_off
  - provident_fund_or_esi_returns_during_period_prior_to_strike_off
  - lease_deeds_or_service_contracts_in_operation
  - board_resolution_authorising_the_petition_where_petitioner_is_the_company
  - proof_of_locus_where_petitioner_is_member_or_creditor_or_workman

accompanying_applications:
  - "I.A. for condonation of delay (where Appeal under Section 252(1) is filed beyond 3 years OR Application under Section 252(3) is filed within 20 years but with unexplained gaps; the Tribunal's discretion under Article 137 / Section 5 Limitation Act considerations apply)"
  - "I.A. for urgent listing (where restoration is sought to defend a recovery action / enforce a contract within time-limits)"
  - "I.A. for directions to the Respondent Registrar to permit filing of overdue returns on the strength of the restoration order"

filing_fee: "Fee under the Schedule of Fees of the NCLT Rules 2016 for Section 252 appeals / applications (verify against latest schedule)."

limitation: "Section 252(1) Appeal by the Company — 3 years from the date of the strike-off order by the ROC under Section 248. Section 252(3) Application by the Company / a member / a creditor / a workman — 20 years from the publication of the strike-off notice in the Official Gazette."
```

## Section 248 — strike-off background (context for the Verifier)

The ROC strikes off the name of a company under Section 248 of the Companies Act 2013 in two circumstances:

- **Section 248(1)** — suo motu strike-off by the ROC where the ROC has reasonable cause to believe that (a) the company has failed to commence its business within one year of its incorporation; or (b) the company is not carrying on any business or operation for a period of two immediately preceding financial years and has not made any application within such period for obtaining the status of a dormant company under Section 455
- **Section 248(2)** — strike-off on the application of the company itself (the voluntary strike-off / 'fast-track exit' under the 2016 Rules)

Section 252 restoration is available against BOTH categories of strike-off, subject to the respective limitation regimes.

## Section 252(1) vs Section 252(3) — choice of route

| Branch | Petitioner | Limitation | Standard | Reliefs |
|---|---|---|---|---|
| Section 252(1) | Only the Company (through its directors) | 3 years from strike-off order | "Not justified in the facts and circumstances" | Setting aside of strike-off + restoration |
| Section 252(3) | Company / member / creditor / workman | 20 years from Gazette publication | "Carrying on business or in operation at the time of strike-off" OR "just to restore" | Restoration |

The Drafter chooses the branch based on (i) who the Petitioner is (Section 252(1) is restricted to the Company; Section 252(3) is open to a wider class), (ii) the time elapsed since strike-off, and (iii) the strength of the "carrying on business" evidence.

## Section 252 — restoration consequences

On a Section 252 restoration order, the company is deemed to have continued in existence as if its name had not been struck off (Section 252(3) proviso). All acts done by or on behalf of the company in the interim period are deemed validly done. Statutory filings overdue from the strike-off period must be regularised within the period directed by the Tribunal, with additional fees and late-filing fees as applicable.

## Documentary anchoring is the heart of the case

The Tribunal grants restoration on the strength of documentary evidence of operation. The advocate's craft is in producing a chronologically-anchored set of bank statements, GST returns, income-tax returns, statutory filings, payroll records, lease agreements, and customer / vendor correspondence covering the period prior to the strike-off. Bare assertions of operation, unaccompanied by documentary anchors, will not satisfy Section 252.

## Where the Company is wound up / under CIRP

Where the company is in voluntary winding-up or under CIRP, Section 252 restoration is not the appropriate route — those processes have their own statutory closure mechanisms. The Drafter ensures Section 252 is invoked only for genuine strike-off-to-be-reversed scenarios, not as a workaround for other corporate-closure issues.
