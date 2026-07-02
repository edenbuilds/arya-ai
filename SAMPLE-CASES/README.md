# Sample Cases — Reviewer Examples

Three anonymised fact patterns. All party names are placeholders.

## Example 1 — nclt-section-241-242-petition

> *"Use the connector to draft a nclt section 241 242 petition (NCLT oppression and mismanagement petition under Sections 241-242 Companies Act 2013). Use anonymised placeholders for party names and figures."*

Tool sequence: list_case_types → get_case_type_format("nclt-section-241-242-petition") → get_pleading_base → draft → save_draft_as_docx

## Example 2 — nclt-scheme-of-arrangement

> *"Use the connector to draft a nclt scheme of arrangement (NCLT scheme of arrangement / amalgamation under Sections 230-232). Use anonymised placeholders for party names and figures."*

Tool sequence: list_case_types → get_case_type_format("nclt-scheme-of-arrangement") → get_pleading_base → draft → save_draft_as_docx

## Example 3 — nclt-section-66-reduction-of-capital

> *"Use the connector to draft a nclt section 66 reduction of capital (NCLT capital reduction petition under Section 66). Use anonymised placeholders for party names and figures."*

Tool sequence: list_case_types → get_case_type_format("nclt-section-66-reduction-of-capital") → get_pleading_base → draft → save_draft_as_docx

## Notes for the reviewer

- All examples use placeholders.
- No external API keys / accounts required.
- `save_draft_as_docx` requires `pandoc`.
- Three-layer privacy firewall applies throughout.

---

## Synthetic case folder for Anthropic reviewer

A fully-fictional, AAAK-pseudonymised case folder is bundled at:

`SAMPLE-CASES/synthetic-nclt-oppression-section-241-242/`

It contains 3 source documents (.docx) plus a `case-facts-background.md` narrative.

**To exercise the pipeline end-to-end**, point `read_case_folder(path)` at this folder and follow the orchestration script returned by `get_agent_instructions()`. The Reader stage will extract facts, the Format stage will load the case-type SKILL.md template, and the remaining four agents (Drafter → Verifier → Refiner → Overseer) will produce `final-draft.docx`.

All identifiers in the bundled documents are structural placeholders. The Pseudonymisation Gateway is therefore exercising against pre-pseudonymised content; reviewers seeking to test re-substitution may replace placeholders with their own fictional values before invoking the pipeline.

