---
name: _company_drafting_base
description: Universal Indian company-law tribunal pleading skeleton. Shared base for all 10 case-type drafting skills in this plugin. Holds the standard structure (Cause Title in correct NCLT-bench / NCLAT nomenclature -> Parties block -> Statutory Opening invoking the operative section of the Companies Act 2013 or the IBC 2016 -> Prelude -> Facts -> Grounds -> Prayer -> Verification -> Affidavit-in-support -> Index -> List of Documents -> accompanying applications). Encodes the Companies Act 1956 -> 2013 transition discipline, the Section 244 threshold computation for Section 241-242 pleadings, the Section 245 class-action thresholds, the Section 230(2) scheme-disclosure obligations, the Section 66 creditor-protection regime, the Section 252 limitation regimes (3-year / 20-year), the Section 213 maintainability thresholds, the Section 8 IBC demand-notice ingredient discipline (Mobilox), the Section 10(3) special-resolution discipline, the CIRP timeline (Section 12 IBC), the Innoventive admission framework, the Section 421(3) Companies Act and Section 61(2) IBC appellate limitation, and the SS-1 / SS-2 compliance check. NOT invoked directly — extended by every case-type skill in this plugin.
allowed-tools: Read
---

# `_company_drafting_base` — universal Indian company-law-tribunal pleading skeleton

This base skill defines the **structural shape** of any company-law-tribunal pleading drafted by the plugin (NCLT first-instance under the Companies Act 2013 / IBC 2016 — and NCLAT appellate under Section 421 Companies Act / Section 61 IBC). Case-type skills extend this base with case-type-specific statutory openings, fact-sequences, grounds, prayer clauses, and accompanying applications.

## Universal skeleton

```
1. CAUSE TITLE
   {{forum.name}} {{forum.bench}}
   {{case_type.case_number_prefix}} No. ____ of {{year}}

   {{party_block_template}}
   {{petitioner_or_applicant_or_appellant_party}} ... {{party_role}}
                                  Versus
   {{respondent_party}} ... {{respondent_role}}

2. STATUTORY OPENING
   {{case_type.statutory_opening}}

3. PRELUDE
   (Short paragraph identifying the Petitioner's / Applicant's / Appellant's
   status — member / depositor / company / operational creditor / corporate
   debtor / ROC / Central Government / any person aggrieved — with the
   authorisation reference (Board Resolution / Power-of-Attorney / member-list
   under Section 88 / IBBI registration for proposed IRP) and the
   registration / address particulars.)

4. FACTS (numbered narrative paragraphs)
   4.1 Incorporation and constitution of the Respondent / Applicant Company
       — date of incorporation, CIN, registered office, current authorised
       and paid-up share capital, principal objects per Memorandum, current
       Articles of Association (refer Exhibit / Annexure A — MOA and AOA).
   4.2 Shareholding pattern / capital structure — categorisation of equity
       holders, promoter and non-promoter classification, the Petitioner's /
       Applicant's / Appellant's shareholding (refer Exhibits / Annexures
       B — D, including register of members under Section 88 of the
       Companies Act 2013 and the latest Annual Return MGT-7).
   4.3 Board composition + Key Managerial Personnel — Directors with DINs,
       date of appointment, current portfolios, KMP under Section 203
       (refer Exhibit / Annexure E).
   4.4 Section 244 threshold compliance (Section 241-242 pleadings) /
       Section 245(3) class threshold (Section 245 pleadings) / Section
       213(a) member-count or Section 213(b) prima-facie material (Section
       213 pleadings) — pleaded with arithmetic.
   4.5 Impugned conduct / scheme particulars / capital-reduction arithmetic
       / strike-off history / investigation grounds / operational-debt
       particulars / corporate-applicant financial-distress / NCLT order
       being appealed (case-type-specific — see case-type SKILL.md).
   4.6 Cause of action for the present pleading — the specific event that
       has crystallised the present cause of action (e.g. the latest
       oppressive act under Section 241-242; the alleged-class-injury under
       Section 245; the special resolution dated ____ approving the scheme
       / capital reduction; the ROC's strike-off order; the expiry of the
       10-day Section 8 IBC notice window; the date of the NCLT order being
       appealed).
   4.7 Limitation — applicable Article of the Limitation Act 1963 (residual
       Article 137 for Companies Act 2013 first-instance pleadings unless
       otherwise specified), or the special limitation regimes — Section
       252(1) / 252(3) for strike-off revival, Section 421(3) Companies
       Act for NCLAT appeals from Companies-Act orders, Section 61(2) IBC
       for NCLAT appeals from IBC orders — pleaded with date of accrual,
       date of filing, and days within limitation.
   4.8 Jurisdiction — territorial jurisdiction of the NCLT / NCLAT bench,
       with statutory anchor (Section 60(1) IBC for IBC matters / Rule 18
       NCLT Rules 2016 for Companies Act matters / NCLAT Rules 2016 for
       appellate matters).
   4.9 Filing fee — amount + applicable schedule (NCLT Rules 2016 Schedule
       of Fees / IBBI (AAA) Rules 2016 Schedule / NCLAT Rules 2016).

5. GROUNDS (numbered)
   5.1 {{case_type.ground_1}}
   5.2 {{case_type.ground_2}}
   5.3 {{case_type.ground_3}}
   ...
   (Grounds anchor each prayer clause; every ground cites the operative
   provision of the Companies Act 2013 / IBC 2016 and the document
   supporting the ground; SS-1 / SS-2 compliance asserted where the ground
   relies on a board / general-meeting record.)

6. PRAYER
   {{case_type.prayer_clauses}}

   And for such further and other reliefs as this Hon'ble Tribunal /
   Appellate Tribunal may deem fit and proper.

7. VERIFICATION
   I, [Name of Authorised Signatory / Member-Petitioner / Applicant], being
   the duly authorised signatory of the Petitioner / Applicant / Appellant
   herein, do hereby verify that the contents of paragraphs ___ to ___ of
   the {{case_type.pleading_type}} are true to my personal knowledge and
   the contents of paragraphs ___ to ___ are true on the basis of
   information received and believed to be true. No part of this
   verification is false and nothing material has been concealed therefrom.

   Verified at [Place] on this __ day of [Month, Year].

                                       [Authorised Signatory /
                                        Petitioner-Member]
                                       [Designation]

8. AFFIDAVIT-IN-SUPPORT
   I, [Name of Authorised Signatory / Petitioner-Member], aged ___ years,
   occupation [Designation / Occupation], having office / residence at
   [Address], do hereby solemnly affirm on oath and state as under:
   1. That I am the duly authorised signatory / Petitioner-Member of the
      Petitioner / Applicant / Appellant herein under [Board Resolution /
      member-list under Section 88 / IBBI registration / capacity-anchor]
      dated ____ (Exhibit / Annexure ___), and am acquainted with the
      facts and circumstances of the case from the records maintained by
      the Petitioner / Applicant / Appellant in the ordinary course of
      business / from my own personal knowledge as a member.
   2. That I have read and understood the contents of the
      {{case_type.pleading_type}} comprising paragraphs 1 to ___ and the
      same are true and correct.
   3. That the documents annexed are true copies / certified true copies /
      true print-outs of the originals available with the Petitioner /
      Applicant / Appellant.

   Affirmed at [Place] on this __ day of [Month, Year].

                                       [Authorised Signatory /
                                        Petitioner-Member]
                                       [Designation / Capacity]

   Solemnly affirmed before me on solemn affirmation under the Bharatiya
   Sakshya Adhiniyam 2023.

                                       [Notary Public / Oath
                                        Commissioner / Tribunal Officer]

9. INDEX
   (Running paragraph-anchored index — paragraph numbers, content summary,
   exhibit references.)

10. LIST OF DOCUMENTS / EXHIBITS / ANNEXURES
    Exhibit / Annexure A — Memorandum of Association and Articles of
                          Association of the Respondent Company
    Exhibit / Annexure B — Certificate of incorporation
    Exhibit / Annexure C — Latest Annual Return MGT-7
    Exhibit / Annexure D — Register of Members under Section 88
    Exhibit / Annexure E — Latest audited financial statements
    Exhibit / Annexure F — Board minutes (impugned period)
    Exhibit / Annexure G — General-Meeting minutes (impugned period)
    Exhibit / Annexure H — Special Resolution dated ____ (for scheme /
                          Section 66 reduction / Section 10 IBC)
    Exhibit / Annexure I — Auditor's certificate (for scheme / Section 66)
    Exhibit / Annexure J — Valuation report (for scheme)
    Exhibit / Annexure K — Section 8 IBC demand notice with proof of
                          service (for Section 9)
    Exhibit / Annexure L — Proposed IRP's Form 2 consent + IBBI
                          registration (for Section 9 / 10)
    Exhibit / Annexure M — NCLT Order being appealed (for Section 421 /
                          Section 61)
    Exhibit / Annexure N — Board Resolution authorising the litigation
    Exhibit / Annexure O — Power-of-Attorney in favour of the authorised
                          signatory (where applicable)
    ... (further case-type-specific exhibits)

11. ACCOMPANYING APPLICATIONS
    {{case_type.accompanying_applications}}
    (Common examples — case-type-specific:
     · Section 244(1) proviso waiver application (for Section 241-242
       where Petitioner falls below threshold)
     · Application for dispensation of meetings (for Section 230-232 where
       90% creditor consent obtained per the Rules)
     · Application for newspaper-publication directions (for Section
       230-232 / Section 66)
     · Application for creditor-objection directions (for Section 66)
     · Application for ad-interim ex-parte injunction (restraining
       alteration of share capital / dilution / board reconstitution
       pending Section 241-242 Petition; preserving books of account
       pending Section 213 Application)
     · Application for ad-interim moratorium pending hearing (for Section
       9 / Section 10 IBC — though admission ordinarily triggers Section
       14 moratorium automatically)
     · Application for stay of operation of the NCLT order (for Section
       421 / Section 61 appeal)
     · Application for condonation of delay (for Section 421(3) Companies
       Act / Section 61(2) IBC beyond the prescribed period)
     · Application for urgent listing
     · Application for substituted service)
```

## Companies Act 1956 → 2013 transition discipline

Every pleading filed today MUST cite the operative provisions of the **Companies Act 2013**. The plugin's Verifier enforces the following 1956 → 2013 transition rules:

| 1956 Act | 2013 Act Successor |
|---|---|
| Section 397 / 398 (oppression and mismanagement) | **Sections 241 and 242** |
| Section 399 (eligibility threshold) | **Section 244** |
| Section 100 / 102 (reduction of share capital) | **Section 66** |
| Sections 391 — 394 (compromise / arrangement / amalgamation) | **Sections 230 — 232** (Section 233 fast-track merger) |
| Sections 235 / 237 (investigation) | **Section 213** |
| Section 560 (strike-off) | **Sections 248 — 252** |
| Section 433 (winding-up by Court) | **Sections 271 — 272** read with the IBC 2016 for insolvency-led winding-up |
| Section 70 (Statement in lieu of prospectus) | **OBSOLETE — removed from 2013 Act in its 1956 form.** Replaced by Chapter III (Public Offer / Private Placement) of the 2013 Act |
| Companies (Court) Rules 1959 | **NCLT Rules 2016 / NCLAT Rules 2016 / Companies (Compromises, Arrangements and Amalgamations) Rules 2016 / NCLT (Procedure for Reduction of Share Capital) Rules 2016 / Companies (Removal of Names of Companies from the ROC) Rules 2016 / Companies (Inspection, Investigation and Inquiry) Rules 2014** (case-type specific) |
| Company Law Board | **National Company Law Tribunal** (NCLT — operative since 1 June 2016) |
| Court (in Court-sanction language) | **NCLT / NCLAT** as the case may be |

## Section 244 threshold computation (Section 241-242 pleadings)

A member shall have the right to apply under Section 241 if he satisfies one of the following thresholds (whichever is less):

- **Not less than 100 members** of the company OR
- **One-tenth of the total number of members** of the company OR
- **Members holding not less than one-tenth of the issued share capital** of the company (provided all calls and other sums due have been paid)

For a company **not having share capital**, not less than one-fifth of the total number of members.

Where the Petitioner falls below the threshold, a Section 244(1) proviso waiver application accompanies the Petition, pleading the Tribunal's discretion to waive the threshold "if in the opinion of the Tribunal circumstances so justify."

## Section 245(3) class-action thresholds

Applicants under Section 245 must satisfy one of (whichever is less):

- Not less than **100 members** or **100 depositors**, OR
- Such percentage of the total number of members / depositors, OR
- Members holding such percentage of issued share capital of the company (where the company has share capital), OR
- Depositors holding such percentage of total deposits, AS MAY BE PRESCRIBED (currently 1/10th per Rule 84 sub-rule (3) of the NCLT Rules 2016 — verify against the latest amendment).

## Section 230(2) scheme-disclosure obligations

For any Section 230-232 application, the company shall disclose by affidavit:

- All material facts relating to the company (latest financial position, latest auditor's report on accounts, pendency of any investigation or proceedings against the company)
- Reduction of share capital, if any, included in the compromise or arrangement
- Any scheme of corporate debt restructuring consented to by not less than 75 percent of the secured creditors in value, including (i) a creditor's responsibility statement in the prescribed form; (ii) safeguards for protection of other secured and unsecured creditors; (iii) report by the auditor that the fund requirements of the company will conform to the liquidity test based on the estimates provided to them by the Board; (iv) where the company proposes to adopt the corporate debt restructuring guidelines specified by the Reserve Bank of India, a statement to that effect; (v) a valuation report in respect of the shares and the property and all assets, tangible and intangible, movable and immovable, of the company by a registered valuer
- Valuation report by a registered valuer (Section 230(3))
- Notice to the Central Government, RBI, SEBI, Registrar of Companies, Income-tax authorities, CCI, Official Liquidator, and the stock exchanges (Section 230(5)) as applicable

## Section 66 creditor-protection regime

For any Section 66 reduction of share capital, the following are mandatory:

- Special resolution under Section 66(1) (3/4 majority)
- Auditor's certificate on absence of arrears of deposit repayment / interest on deposits under Section 66(2)(b)
- List of creditors as on the relevant date with consents / unsatisfied creditors with proposed settlement under Section 66(2)(c)
- Public notice / newspaper publication under Section 66(4) inviting creditor objections within the prescribed period
- Order of confirmation under Section 66(5) and registration with the ROC under Section 66(6)

## Section 252 limitation regimes

- **Section 252(1) Appeal** by the company — within **3 years** from the date of the strike-off order by the ROC under Section 248
- **Section 252(3) Application** by the company / a member / a creditor / a workman — within **20 years** from the publication of the strike-off notice, on the ground that the company was carrying on business or in operation, or on any other ground that the NCLT considers just to restore the name

Evidence of "carrying on business or in operation" pleaded with documentary anchors — bank statements, GST returns, income-tax returns, statutory filings under Sections 92 / 137 of the Companies Act 2013, employer's PF / ESI returns, lease deeds / service contracts in operation.

## Section 213 maintainability

- **Section 213(a)**: not less than 100 members OR members holding not less than 1/10th of the total voting power
- **Section 213(b)**: any person on prima-facie material satisfying the Tribunal of (i) intent to defraud creditors / members / others; (ii) fraudulent or unlawful purpose; (iii) fraud / misfeasance / other misconduct by management; (iv) non-disclosure to members of information they were reasonably entitled to

## Section 8 IBC demand-notice ingredient discipline (Mobilox)

For any Section 9 Operational Creditor application, the following ingredients of the Section 8 demand-notice regime must be pleaded:

- Notice in **Form 3** (claim with default amount, supported by documentary evidence) or **Form 4** (claim with invoices, supported by copies of invoices) served on the Corporate Debtor at registered office
- **10-day reply window** expired
- **No notice of pre-existing dispute** received from the Corporate Debtor during the window
- Where any reply / dispute notice was received: pre-emption by the Applicant — the dispute is not "pre-existing" within *Mobilox Innovations Pvt. Ltd. v. Kirusa Software Pvt. Ltd.* (2018) 1 SCC 353 (i.e., the dispute is not plausible, is unsupported by some material, was raised only after receipt of the Section 8 notice)
- **Proof of service** of the Section 8 notice (postal receipt / dispatch register / email-delivery proof / registered-post acknowledgement)

## Section 10(3) special-resolution discipline

For any Section 10 Corporate Applicant application:

- **Special resolution of members under Section 10(3)(c)** of the IBC read with Section 114(2) of the Companies Act 2013 (3/4 majority), OR
- **For an LLP** — resolution of not less than 3/4 of the total number of partners

The Applicant pleads the date of the special resolution, the MCA / ROC filing reference, and exhibits the certified copy of the resolution. The proposed IRP's Form 2 consent and IBBI registration are mandatory annexures.

## CIRP timeline — Section 12 IBC

CIRP must be completed within **180 days** from CIRP commencement, extendable to **330 days** in aggregate (including any time taken in legal proceedings). The Drafter pleads the timeline awareness in prayer-clauses of Section 9 / Section 10 applications and in appellate grounds for Section 61 appeals challenging admission / plan-approval / liquidation.

## Innoventive admission framework

*Innoventive Industries Ltd. v. ICICI Bank* (2018) 1 SCC 407 — at IBC admission stage only:

- (a) Default has occurred,
- (b) Application is complete in all respects, and
- (c) No disciplinary proceedings are pending against the proposed IRP

are examined. The merits of any dispute about the debt are not the subject of inquiry at the admission stage. Drafters of Section 9 / Section 10 applications draft accordingly; Drafters of Section 61 appeals against admission orders draft within this lens.

## Section 421(3) / Section 61(2) appellate limitation discipline

- **Section 421(3) Companies Act NCLAT appeal**: **45 days** from receipt of NCLT order; extendable on sufficient cause to a further **45 days**
- **Section 61(2) IBC NCLAT appeal**: **30 days** from the date of the NCLT order; extendable on sufficient cause to a further **15 days** (hard stop at 45 days)

Beyond the prescribed period a condonation application accompanies the appeal memo; absent sufficient cause, the appeal is barred.

## SS-1 / SS-2 compliance check

Any board / general-meeting record relied on (board minutes for board resolutions; AGM / EGM minutes for special resolutions) must comply with **Secretarial Standard 1 (Meetings of the Board of Directors)** and **Secretarial Standard 2 (General Meetings)** issued by the Institute of Company Secretaries of India under Section 118(10) of the Companies Act 2013 — notice period, quorum, recording of minutes, signed minutes, attendance register. Defects flagged for the Refiner / surfaced for the Overseer.

## Statute references the plugin handles

- Companies Act 2013 (principal — Sections 2, 88, 92, 102, 114, 118, 137, 196 — 205, 213, 230 — 232, 233, 241 — 246, 247, 248 — 252, 271 — 272, 421 — 422, 447, 452, the Schedules)
- Insolvency and Bankruptcy Code 2016 (Sections 3, 4, 5, 6, 7, 9, 10, 10A, 11, 12, 13, 14, 17 — 19, 21, 29A, 30 — 33, 43 — 51, 60, 61, 62, 64, 65, 78 — 100, 218 — 220)
- NCLT Rules 2016
- NCLAT Rules 2016
- Companies (Compromises, Arrangements and Amalgamations) Rules 2016
- NCLT (Procedure for Reduction of Share Capital of Company) Rules 2016
- Companies (Removal of Names of Companies from the Register of Companies) Rules 2016
- Companies (Inspection, Investigation and Inquiry) Rules 2014
- IBBI (Application to Adjudicating Authority) Rules 2016
- IBBI (Insolvency Resolution Process for Corporate Persons) Regulations 2016
- IBBI (Liquidation Process) Regulations 2016
- IBBI (Voluntary Liquidation Process) Regulations 2017
- IBBI (Insolvency Professionals) Regulations 2016
- Secretarial Standard 1 (Meetings of the Board of Directors) and Secretarial Standard 2 (General Meetings) issued by ICSI under Section 118(10) of the Companies Act 2013
- Companies Act 1956 — referenced only for legacy-transition discipline (NEVER as operative authority in a new pleading)
- Bharatiya Nagarik Suraksha Sanhita 2023 (for cross-references in Section 447 / Section 452 criminal complaints arising from company-law context)
- Bharatiya Sakshya Adhiniyam 2023 (for electronic-records admissibility — MCA-21 portal printouts, DEMAT records — under Section 63 BSA)
- Limitation Act 1963 (Schedule I, Article 137 as residual; special regimes under Section 252 Companies Act, Section 421(3) Companies Act, Section 61(2) IBC)
- Indian Contract Act 1872 (Sections 124 — 147 on indemnity, guarantee, surety — for corporate-guarantee / personal-guarantor cross-references)
- Transfer of Property Act 1882 (for share-pledge cross-references)
- Indian Stamp Act 1899 + applicable State Stamp Acts (for scheme-of-arrangement stamp-duty computation)
- Applicable State Court-Fees Acts (where any NCLT bench-specific filing-fee schedule cross-references the State Act)


---

## v0.2.1 RENDER DISCIPLINE (load-bearing — Drafter must follow)

**Pandoc + reference.docx + post-pandoc fix script.** The Drafter writes Markdown using the heading discipline below. Pandoc converts the Markdown to `.docx` using the SHIPPED reference.docx at `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/reference.docx` — pre-customised with locked Word styles matching the filing-grade Bombay HC convention (extracted from an actual filed Second Appeal pleading):

- **Body (Normal)** — TNR 14pt, 1.5 line spacing, justified, 0.5cm first-line indent
- **Heading 1** — TNR 14pt **bold + centered** (NOT underlined) — for the Court / Forum / Tribunal header line and the case-number line
- **Heading 2** — TNR 14pt **bold + UNDERLINED + centered + letter-spacing** — for spaced section headers (`F A C T S`, `G R O U N D S`, `P R A Y E R`, `I N D E X`, `S Y N O P S I S`, `L I S T   O F   A N N E X U R E S`, `V E R I F I C A T I O N`)
- **Heading 3** — TNR 14pt **bold + UNDERLINED + centered** — for unspaced section headers (`SUBSTANTIAL QUESTIONS OF LAW`, `ACTS & RULES`, `CITATIONS`) and statutory opening (`WRIT PETITION UNDER ARTICLE 226 …`)
- **Heading 4** — TNR 14pt **bold + UNDERLINED + left-aligned** — for left-anchored bold-underlined headings (`MOST RESPECTFULLY SHEWETH:`)
- **Tables** — `tblLayout = fixed`; first row bold centered; cell margins locked

### Markdown heading mapping

| Markdown | Rendered as | Used for |
|---|---|---|
| `# Heading 1` | Bold centered (no underline) | Court header line; case-number line; cover-page anchors |
| `## Heading 2` | Bold centered UNDERLINED with letter-spacing | Spaced section headers (`## F A C T S`, `## G R O U N D S`, `## P R A Y E R`, `## I N D E X`, `## S Y N O P S I S`, `## L I S T   O F   A N N E X U R E S`, `## V E R I F I C A T I O N`) |
| `### Heading 3` | Bold centered UNDERLINED | Unspaced section headers + statutory opening |
| `#### Heading 4` | Bold left UNDERLINED | `#### MOST RESPECTFULLY SHEWETH:` |
| Body paragraph | TNR 14pt justified 1.5 spacing 0.5cm first-line indent | Everything else |
| `**Bold inline**` | Bold | Property descriptors / annexure markers / key terms inline within Facts narrative |

### Bold-number paragraph convention

Facts and Grounds paragraphs use **BOLD NUMBERS**: `**1.**`, `**2.**`, `**3.**` followed by a tab + body. Renders as the gold-standard pleading layout.

### Two-step pandoc command (Step 2 is NON-NEGOTIABLE)

```bash
# Step 1 — pandoc → .docx with locked Word styles
pandoc draft-v1.md -o draft-v1.docx \
  --reference-doc="${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/reference.docx" \
  --from=markdown+pipe_tables+raw_tex

# Step 2 — force table column widths
python3 "${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/fix_docx_tables.py" draft-v1.docx
```

Step 2 forces column widths on every table — 5-col (Sr.No / Annx / Particulars / Date / Pgs) = 8/8/60/14/10; 4-col = 10/10/65/15; 3-col = 10/75/15; 2-col Dates–Events = 18/82. Locks first-row bold + centered + vertically-centered cells. **Skipping the fix script reproduces the v0.2.0 Index-table defect (Sr.No / Annx columns stacking vertically).**

Do NOT auto-generate a fresh reference.docx in the case folder. Use the shipped one or a `<case-folder>/reference.docx` override.

### Cover-page discipline

INDEX, SYNOPSIS, LIST OF ANNEXURES each begin on a new page (`\newpage` in Markdown) and carry ONLY: forum header (`#`) + case-number line (`#`) + short cause-title (Petitioner short name `///VERSUS///` Respondent short name) + section header (`##`) + table + Counsel block. DO NOT repeat the full party address block on cover pages.

### Pipeline-optionality (advocate-cost discipline)

The full 6-agent pipeline (Reader → Format → Drafter → Verifier → Refiner → Overseer) is **NOT** mandatory. Only the first three stages are required to produce a filing-grade draft. Stages 4–6 are OPTIONAL QC layers the advocate explicitly invokes. Default exit point is here, after Drafter (~280K tokens). Full pipeline ~600K tokens — disproportionate for routine pleadings.

When `draft-v1.docx` is written, the Drafter's job is complete. The advocate decides whether to invoke the QC stages.
