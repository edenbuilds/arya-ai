---
name: nclt-section-245-class-action-draft
description: Draft a Class Action Application before the National Company Law Tribunal under Section 245 of the Companies Act 2013 read with Rule 84 of the NCLT Rules 2016. For a class of members or depositors of a company seeking class-relief restraining the company from ultra vires acts, declaring a resolution void, restraining a fraudulent or unlawful act by directors, claiming damages or compensation, or other suitable Section 245 reliefs. Encodes the Section 245(3) threshold for class action (not less than 100 members / depositors or one-tenth holding — whichever is less) and the Section 245(4) admission-factors discipline. Auto-fires on "draft class action", "draft Section 245 application", "draft NCLT class action", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# NCLT Section 245 Class Action Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: APPLICATION UNDER SECTION 245 OF THE COMPANIES ACT 2013 READ WITH RULE 84 OF THE NCLT RULES 2016
case_short_code: NCLT_245
case_number_prefix: C.A.
pleading_type: Class Action Application
typical_forum: NCLT of competent territorial jurisdiction (registered office of the Respondent Company)
typical_parties: Applicant Members / Depositors (as a class) + Respondent Company + Respondent Directors / Officers / Auditors / Consultants / Advisors implicated
statutory_opening: "This Application is filed under Section 245 of the Companies Act 2013 read with Rule 84 of the National Company Law Tribunal Rules 2016, by the Applicants as a class of [members / depositors] of the Respondent Company, seeking the reliefs enumerated in Section 245(1) on the ground that the management or conduct of the affairs of the Respondent Company is being conducted in a manner prejudicial to the interests of the Respondent Company / its members / its depositors."
ground_clauses:
  - "Authority of the Tribunal — Section 245 of the Companies Act 2013 vests exclusive jurisdiction in the National Company Law Tribunal to entertain class actions by members / depositors."
  - "Jurisdictional anchor — the registered office of the Respondent Company is within the territorial limits of this Bench (Rule 18 of the NCLT Rules 2016)."
  - "Section 245(3) class-threshold satisfied — the Applicants are [not less than 100 members / depositors / not less than one-tenth of total members / depositors / members holding not less than one-tenth of issued share capital / depositors holding not less than one-tenth of total deposits] of the Respondent Company, satisfying the eligibility threshold under Section 245(3) read with Rule 84(3) of the NCLT Rules 2016."
  - "Section 245(4) factors satisfied — (i) the Applicants are acting in good faith in making the Application; (ii) the cause of action is one that they could pursue in their own right; (iii) the alleged-acts are likely to be authorised / ratified only by the company / its members / its directors in breach of statutory duty; (iv) the views of all other class members will be effectively represented in the proceedings."
  - "Class commonality — every Applicant has the same interest in the cause of action, and the impugned conduct affects the class uniformly."
  - "Limitation — the present Application is filed within the residual limitation under Article 137 of the Schedule to the Limitation Act 1963 (3 years from the date when the right to apply accrues)."
prayer_clauses:
  - "(a) Issue an order under Section 245(1)(a) of the Companies Act 2013 restraining the Respondent Company from committing the act of [ultra vires the Articles / Memorandum / the Companies Act 2013];"
  - "(b) Issue an order under Section 245(1)(b) of the Companies Act 2013 restraining the Respondent Company from acting on the resolution dated ____ on the ground that the resolution was passed by suppression of material facts / by misstatement / in a manner contrary to the Companies Act 2013;"
  - "(c) Issue an order under Section 245(1)(c) of the Companies Act 2013 declaring the resolution dated ____ as void;"
  - "(d) Issue an order under Section 245(1)(d) of the Companies Act 2013 restraining the Respondent Directors / Officers from acting on the resolution dated ____ / from doing the act complained of;"
  - "(e) Issue an order under Section 245(1)(e) of the Companies Act 2013 restraining the Respondent Company / Directors from doing the act which is ultra vires the Articles / Memorandum / Companies Act 2013;"
  - "(f) Award compensation under Section 245(1)(g) of the Companies Act 2013 to the Applicant-class members / depositors;"
  - "(g) Direct publication of the present Application in such manner as the Tribunal may consider proper to bring the class action to the notice of similarly placed members / depositors who are not parties to the Application;"
mandatory_exhibits:
  - memorandum_of_association_and_articles_of_association
  - certificate_of_incorporation
  - latest_annual_return_mgt_7
  - register_of_members_or_register_of_deposit_holders_under_section_88_or_section_73
  - list_of_class_applicants_with_shareholding_or_deposit_holding
  - impugned_resolution_or_act_documentary_anchor
  - correspondence_or_communications_demonstrating_pre_application_efforts
  - board_minutes_general_meeting_minutes_for_impugned_period
accompanying_applications:
  - "I.A. for advertisement / publication directions under Section 245(5) (manner of intimating the class)"
  - "I.A. for ad-interim relief restraining the impugned act pending hearing"
  - "I.A. for consolidation of class applications (where multiple Section 245 applications on the same facts are pending)"
  - "I.A. for urgent listing"
filing_fee: "Fee under the Schedule of Fees of the NCLT Rules 2016 (verify against latest schedule)."
limitation: "Residual under Article 137 of the Schedule to the Limitation Act 1963 — 3 years from accrual."
```

## Section 245(4) factors — admission discipline

Before admitting a Section 245 application, the NCLT must consider the factors under Section 245(4):

- Whether the member / depositor is acting in good faith
- Any evidence before it as to the involvement of any person other than directors or officers of the company on any of the matters provided in clauses (a) to (f) of Section 245(1)
- Whether the cause of action is one which the member / depositor could pursue in his own right rather than through an order under Section 245
- Any evidence before it as to the views of the members / depositors of the company who have no personal interest, direct or indirect, in the matter being proceeded under Section 245
- Where the cause of action is an act / omission that is yet to occur, whether the act / omission could be (i) authorised by the company before it occurs, or (ii) ratified by the company after it occurs
- Where the cause of action is an act / omission that has already occurred, whether the act / omission could be ratified by the company

The Drafter pleads positively to each of these factors so the Tribunal is satisfied at admission.

## Section 245(5) advertisement / publication

Where the Tribunal admits a Section 245 application, it shall give public notice to all the members / depositors of the class in the prescribed manner. The applicant typically prays for directions on the manner of publication; the costs are borne as the Tribunal may direct.

## Section 245(7) sanction against frivolous applications

A frivolous or vexatious Section 245 application attracts dismissal with costs of at least ₹1 lakh and not more than such amount as may be prescribed. The Drafter ensures the application is well-particularised and supported by documentary anchors to avoid the Section 245(7) sanction surface.

## Cross-reference to Section 241-242

Section 245 is not mutually exclusive with Section 241-242 — the same conduct may simultaneously give rise to oppression-and-mismanagement individual relief under Section 241 and to class relief under Section 245. The Drafter chooses the forum based on the relief most adequate to the wrong; both forums may run in parallel.
