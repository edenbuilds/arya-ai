---
name: nclt-section-241-242-petition-draft
description: Draft a Petition before the National Company Law Tribunal under Sections 241 and 242 of the Companies Act 2013 (oppression and mismanagement) read with Section 244 (eligibility threshold) and Rules 81 to 89 of the NCLT Rules 2016. For a shareholder (or group of shareholders) seeking relief against the conduct of the affairs of the company in a manner prejudicial / oppressive to any member or in a manner prejudicial to public interest. Encodes the Section 244 threshold (not less than 100 members OR one-tenth of total members OR one-tenth of issued share capital — whichever is less; Section 244(1) proviso waiver power) and the wide-ranging Section 242 reliefs (regulation of conduct of affairs, share-purchase orders, supersession of Board, removal of directors, regulation of dividend policy, winding-up regulation). Auto-fires on "draft Section 241 petition", "draft 241-242 petition", "draft oppression and mismanagement petition", "draft NCLT oppression petition", and similar trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# NCLT Section 241-242 Oppression and Mismanagement Petition Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_company_drafting_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: PETITION UNDER SECTIONS 241 AND 242 OF THE COMPANIES ACT 2013 READ WITH SECTION 244 THEREOF
case_short_code: NCLT_241_242
case_number_prefix: C.P.
pleading_type: Company Petition (Oppression and Mismanagement)
typical_forum: National Company Law Tribunal of competent territorial jurisdiction (the NCLT within whose territorial jurisdiction the registered office of the Respondent Company is situated, per Rule 18 of the NCLT Rules 2016)
typical_parties: Petitioner Member(s) / Shareholder(s) / Central Government (in public-interest cases under Section 241(2)) + Respondent Company + Respondent Directors / Controlling Shareholders / KMP
statutory_opening: "This Petition is filed under Sections 241 and 242 of the Companies Act 2013 read with Section 244 thereof and the National Company Law Tribunal Rules 2016 (in particular Rules 81 to 89), by the Petitioner / Petitioners against the Respondents, seeking relief against (a) the conduct of the affairs of the Respondent Company in a manner prejudicial or oppressive to the Petitioner / any other member; and (b) the conduct of the affairs of the Respondent Company in a manner prejudicial to public interest, and further seeking such of the reliefs enumerated in Section 242 as the Tribunal may consider just and equitable in the facts and circumstances of the present case."
ground_clauses:
  - "Authority of the Tribunal — the National Company Law Tribunal has exclusive jurisdiction under Sections 241 and 242 of the Companies Act 2013 to grant the reliefs sought herein; the Company Law Board jurisdiction under the erstwhile Sections 397 and 398 of the Companies Act 1956 stood transferred to the NCLT with effect from 1 June 2016."
  - "Jurisdictional anchor — the Tribunal has territorial jurisdiction under Rule 18 of the NCLT Rules 2016, as the registered office of the Respondent Company is situated within the local limits of this Bench."
  - "Section 244 threshold satisfied — the Petitioner / Petitioners hold not less than [one-tenth of the issued share capital / one-tenth of the total number of members / not less than 100 members] of the Respondent Company, satisfying the eligibility threshold under Section 244(1) of the Companies Act 2013. [Where below threshold: the Petitioner respectfully invokes the proviso to Section 244(1) and prays for waiver of the threshold by way of the accompanying application.]"
  - "Oppression made out — the Respondents have conducted the affairs of the Respondent Company in a manner prejudicial and oppressive to the Petitioner / to other members, particularised in paragraphs ___ to ___ hereinabove and supported by Exhibits ___ to ___."
  - "Mismanagement made out — the Respondents have conducted the affairs of the Respondent Company in a manner prejudicial to the interests of the Respondent Company / to public interest, particularised in paragraphs ___ to ___ and supported by Exhibits ___ to ___."
  - "Just and equitable to grant relief — the conduct complained of is continuing and incapable of being remedied except by the intervention of this Tribunal; alternative remedies (derivative suit / civil suit / arbitration) are inadequate; oppression / mismanagement matters are NON-ARBITRABLE per Vidya Drolia v. Durga Trading Corporation (2021) 2 SCC 1."
  - "Limitation — the present Petition is filed within the residual limitation under Article 137 of the Schedule to the Limitation Act 1963 (3 years from the date when the right to apply accrues); the continuing nature of the oppressive / mismanagement conduct keeps the limitation alive."
prayer_clauses:
  - "(a) Issue an order under Section 242(2)(a) of the Companies Act 2013 regulating the conduct of the affairs of the Respondent Company in future;"
  - "(b) Issue an order under Section 242(2)(b) of the Companies Act 2013 directing the purchase of the shares of any member of the Respondent Company by other members thereof or by the Respondent Company / direct the consequent reduction of share capital of the Respondent Company;"
  - "(c) Issue an order under Section 242(2)(d) of the Companies Act 2013 setting aside the resolution(s) dated ____ / the transfer(s) dated ____ / the agreement(s) dated ____ entered into by the Respondent Company contrary to law / contrary to the Articles of Association / fraudulent / preferential / contrary to the interests of the members;"
  - "(d) Issue an order under Section 242(2)(f) of the Companies Act 2013 removing the Respondent No. ___ from the directorship of the Respondent Company / superseding the Board of Directors;"
  - "(e) Issue an order under Section 242(2)(k) of the Companies Act 2013 directing the Respondent Company to act in accordance with the directions of this Tribunal in respect of the future conduct of business;"
  - "(f) Grant ad-interim ex-parte injunction restraining the Respondents from (i) altering the share capital of the Respondent Company; (ii) issuing fresh shares / convertibles; (iii) reconstituting the Board; (iv) declaring any dividend / bonus / buy-back; (v) selling / encumbering / disposing of any of the principal assets of the Respondent Company, pending disposal of this Petition;"
mandatory_exhibits:
  - memorandum_of_association_and_articles_of_association
  - certificate_of_incorporation
  - latest_annual_return_mgt_7
  - register_of_members_under_section_88
  - share_certificates_or_demat_holding_statement_of_petitioner
  - latest_audited_financial_statements_three_years
  - board_minutes_for_impugned_period
  - general_meeting_minutes_for_impugned_period
  - alleged_oppressive_resolutions_or_agreements_or_transfers
  - correspondence_petitioner_to_board_or_management
  - board_resolution_authorising_filing_where_petitioner_is_corporate_shareholder
accompanying_applications:
  - "I.A. for waiver of the Section 244 threshold under the proviso to Section 244(1) (where Petitioner falls below the threshold)"
  - "I.A. for ad-interim ex-parte injunction restraining alteration of share capital / dilution / board reconstitution / dividend declaration pending the Petition"
  - "I.A. for production of statutory registers and books of account (Section 128, Section 88, Section 92 — Section 92(3)) by the Respondent Company"
  - "I.A. for appointment of an independent administrator / observer pending the Petition (where Section 242 supersession of Board is sought)"
  - "I.A. for urgent listing"
filing_fee: "Fee under the Schedule of Fees of the NCLT Rules 2016 for Section 241-242 petitions (verify against latest schedule); typically a fixed fee."
limitation: "Residual limitation under Article 137 of the Schedule to the Limitation Act 1963 — 3 years from the date when the right to apply accrues. Continuing-conduct oppression keeps limitation alive."
```

## Section 244 threshold computation

Under Section 244 of the Companies Act 2013, a member is eligible to apply if he satisfies one of (whichever is less):

- Not less than **100 members** of the company OR
- **One-tenth of the total number of members** of the company OR
- Members holding not less than **one-tenth of the issued share capital** of the company (provided all calls / other sums due have been paid)

Where the Petitioner falls below the threshold, the proviso to Section 244(1) empowers the Tribunal, "if in the opinion of the Tribunal circumstances so justify," to waive the requirement. A separate I.A. for waiver MUST accompany the Petition, pleading the circumstances justifying waiver (small-shareholder oppression of disproportionate severity, fraud against minority, public-interest dimension, etc.).

## Section 241(2) public-interest standing

Under Section 241(2), the Central Government may itself apply to the Tribunal where it considers that the affairs of the company are being conducted in a manner prejudicial to public interest. Where the Petitioner is the Central Government, the public-interest dimension must be pleaded with particularity.

## Section 242 reliefs — the menu

Section 242(2) enumerates the reliefs the Tribunal may grant on a finding of oppression / mismanagement, including but not limited to:

- (a) regulation of the conduct of affairs of the company in future
- (b) purchase of shares / interests of any members by other members or by the company itself
- (c) consequent reduction of share capital
- (d) restrictions on transfer / allotment of shares
- (e) termination, setting aside or modification of any agreement between the company and its directors / MD / manager (subject to Section 188 related-party-transaction discipline)
- (f) termination, setting aside or modification of any agreement between the company and any person (with notice and opportunity to that person)
- (g) setting aside of any transfer / delivery of goods / payment / execution / other act made within 3 months prior to the application
- (h) removal of the MD / manager / director of the company
- (i) recovery of undue gains made by any MD / manager / director and the manner of utilisation of the recovery
- (j) the manner in which the MD / manager / director may be appointed in succession
- (k) appointment of such number of persons as directors as may be required by the Tribunal
- (l) imposition of costs
- (m) any other matter for which it is just and equitable that provision should be made

## Vidya Drolia non-arbitrability

Per *Vidya Drolia v. Durga Trading Corporation* (2021) 2 SCC 1 — oppression and mismanagement matters are NON-ARBITRABLE. Any arbitration clause in shareholders' agreement / Articles is unenforceable to the extent it purports to oust the Tribunal's Section 241-242 jurisdiction. The Drafter pre-empts any Section 8 A&C 1996 reference application by the Respondents.

## Tata Consultancy Services / Cyrus Investments — limited reference

The 2021 Supreme Court decision in *Tata Consultancy Services Ltd. v. Cyrus Investments Pvt. Ltd.* (2021) 9 SCC 449 sets out the contemporary contours of Section 241-242 review at the Supreme Court — used here as a limited reference for the proposition that Section 242 reliefs are wide but discretionary, and the Tribunal does not rewrite the corporate constitution at the instance of a defeated shareholder. The Drafter does NOT lean on Cyrus Investments as a precedent for the merits of any individual case; the precedential weight is contextual.
