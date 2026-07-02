# Case Facts Background — NCLT § 241-242 oppression and mismanagement petition

All party names, CIN, addresses, monetary figures, and ancillary dates are fictional placeholders.

## Parties

- **Petitioner:** [Director-Min-1] — Director and 25% pre-allotment shareholder of M/s [Company-A] Pvt Ltd. Now diluted to [Post-Min-1-%] by the impugned allotment.
- **Respondent No. 1:** M/s [Company-A] Private Limited, CIN [CIN-Placeholder], registered office at [Registered-Office-Placeholder].
- **Respondent No. 2:** [Director-Maj-1] — Majority Promoter Director (35% → [Post-Maj-1-%] post allotment).
- **Respondent No. 3:** [Director-Maj-2] — Promoter Director (30% → [Post-Maj-2-%] post allotment).
- **Respondent No. 4 (Proper party):** [Director-Min-2] — co-minority director (10% → [Post-Min-2-%]).

## Section 244 eligibility

- Section 244(1)(a) Companies Act 2013 — petitioner needs at least 1/10th of the issued share capital OR 100 members (whichever lesser). Petitioner holds 25% pre-allotment and [Post-Min-1-%] post-allotment — well above the threshold. Maintainable on Petitioner's own holding without seeking waiver.

## Acts of oppression and mismanagement (skeleton)

1. **Inadequate notice of Board meeting** — petitioner served notice less than 24 hours before; [Director-Min-2] not served at all. Violation of Section 173(3) and Articles of Association.
2. **Substantive agenda not circulated** — preferential allotment not on circulated agenda; raised on the floor in violation of disclosure norms.
3. **Allotment at par despite valuation** — fair value Rs. [Valuation-FV-Placeholder]/- per share; allotment at Rs. 10/- per share; resulting transfer of value of Rs. [Transfer-Value-Placeholder]/- to the majority block.
4. **No pre-emption offer / rights issue** to existing shareholders — direct preferential allotment to majority insiders.
5. **False working-capital urgency claim** — Company had Rs. [Retained-Earnings-Placeholder]/- retained earnings and Rs. [Operating-CF-Placeholder]/- operating cash flow.
6. **Dilution of minority** — Petitioner from 25% → [Post-Min-1-%]; [Director-Min-2] from 10% → [Post-Min-2-%]. Loss of veto rights and statutory rights (Section 244, Section 230(6), etc.).

## Reliefs sought (Section 242)

1. Declaration that the Board resolution dated 28 November 2025 and the consequent preferential allotment are void and oppressive.
2. Cancellation of the allotment and consequent restoration of pre-allotment shareholding pattern.
3. In the alternative, direction to the Respondents Nos. 2 and 3 to purchase the Petitioner's shareholding at fair value calculated per the valuation report dated [Valuation-Date-Placeholder], with interest from the date of impugned allotment till payment.
4. Reconstitution of the Board with appointment of an independent director nominated by the Petitioner.
5. Investigation under Section 213 if warranted.
6. Costs and incidental reliefs.

## Forum and case type

- **Forum:** National Company Law Tribunal (NCLT), [NCLT-Bench-Placeholder] Bench.
- **Case type:** `nclt-section-241-242-petition`.
- **Statutory anchor:** Sections 241–244 + 246 + 401 of the Companies Act 2013.
- **Procedure:** NCLT Rules 2016 (Rule 81 — Form NCLT-1).
- **Limitation:** Acts of oppression are continuing wrongs; no fixed limitation. Petition filed within reasonable time of latest act.

## How to use this fixture

1. Point `read_case_folder(path)` at this directory.
2. Reader extracts facts from the 3 `.docx` files plus this `case-facts-background.md`.
3. Call `get_case_type_format("nclt-section-241-242-petition")` for the NCLT § 241-242 template.
4. The remaining 5 agents (Format → Drafter → Verifier → Refiner → Overseer) run end-to-end to produce `final-draft.docx` containing the NCLT petition (NCLT-1) + Statement of Particulars + List of Authorities + Affidavit verifying.
