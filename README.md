# arya-ai

arya-ai is a comprehensive Indian-law plugin and local MCP server for lawyers. It combines specialist legal agents, reusable drafting skills, command prompts, protocol references, NCLT/NCLAT/IBC drafting workflows, legal templates, and local document tools into one portable repository.

It is designed to work across Claude, Claude Code, ChatGPT/Codex, Gemini, Cursor, and any MCP-compatible assistant.

## What It Does

arya-ai helps with:

- Indian legal research and issue spotting.
- Legal notices, civil suits, criminal complaints, affidavits, opinions, RTI applications, writ/PIL workflows, and contract review.
- Bombay High Court (Mumbai, Nagpur, Aurangabad, Kolhapur) and Maharashtra tribunal pleadings: writs, APL, ABA, bail, appeals, MAT, MACT, consumer, DRT/DRAT, SARFAESI, NI 138, ULP, MahaRERA, family court, civil suits, written statements, reply affidavits and deeds.
- Business documents: rent, NDA, employment, founder, freelance, MSA, DPDPA notices, terms, cease and desist, MoU, partnership.
- AI-practice safeguards: anonymisation, hallucination checks, a pre-filing checklist, matter briefs, four-tier contract review.
- NCLT/NCLAT/IBC/company-law pleadings using a six-stage Reader, Format, Drafter, Verifier, Refiner, and Overseer workflow.
- Limitation analysis, jurisdiction checks, trial preparation, appeal strategy, and evidence review.
- Protocol-backed analysis across contract, criminal, civil procedure, corporate, labour, property, IP, consumer, RERA, RTI, PIL, writ, ADR, cyber, and civic-law domains.
- Local case-folder creation and DOCX export using Pandoc.
- Local PDF workflow guidance for tribunal/court annexures and extracted text review.

## Contents

| Area | Count | Location |
|---|---:|---|
| Specialist legal agents | 32 | `agents/` |
| Command workflows | 32 | `commands/` |
| Skills and drafting workflows | 67 | `skills/` |
| Protocol reference files | 235 | `protocols/` |
| Maharashtra court and tribunal case types | 36 | `skills/<case-type>-draft/` |
| Company-law drafting case types | 10 | `skills/nclt-*`, `skills/ibc-*`, `skills/nclat-*` |
| Maharashtra forum configs (Bombay HC seats, tribunals) | 20 | `maharashtra/forum-config/exemplars/` |
| Long-form drafting templates | 50 | `maharashtra/templates/`, `skills/indian-legal-drafting/assets/templates/` |
| Local MCP server | 1 | `server/main.py` |

## Covered Domains

- Contract law and specific relief.
- Criminal law, BNS/BNSS/BSA transition, bail, FIR, trial, evidence, and appeals.
- Civil procedure, jurisdiction, pleadings, trial, execution, appeals, and revision.
- Corporate law, Companies Act compliance, shareholder disputes, board processes, schemes, and IBC.
- NCLT, NCLAT, company bench, oppression/mismanagement, schemes, capital reduction, revival, investigation, class action, and IBC applications.
- Labour and employment law, gratuity, bonus, EPF/ESIC, termination, retrenchment, settlements, and industrial disputes.
- Property transfers, leases, mortgages, registration, due diligence, and RERA/consumer remedies.
- Intellectual property, patents, trademarks, copyright, designs, GI, licensing, and enforcement.
- Constitutional/civic remedies: writs, RTI, PIL, NGT, local governance, tribunals, and public grievance.
- ADR: arbitration, mediation, and conciliation.

## Universal Rules

All platforms should start with:

```text
Read skills/arya-ai-orchestrator/SKILL.md first and follow it for routing, legal safety, drafting, and verification.
```

Core rules:

- Do not invent citations, statutes, court rules, dates, or facts.
- Mark uncertain law as needing verification.
- Check current primary sources when law, filing requirements, fees, or limitation periods may have changed.
- Treat client materials as confidential.
- Keep every draft traceable to user-provided facts or explicit assumptions.
- Always include a final verification checklist for filing-sensitive work.

## Install and Use

### Codex / ChatGPT Codex

This repo includes a Codex plugin manifest:

```text
.codex-plugin/plugin.json
```

Use the repo as a local plugin folder or copy it into your plugin marketplace/workspace. The key entry points are:

- `skills/arya-ai-orchestrator/SKILL.md`
- `.mcp.json`
- `server/main.py`

### Claude Code

Install from GitHub:

```text
/plugin marketplace add edenbuilds/arya-ai
/plugin install arya-ai@arya-ai
```

Or load a local clone:

```bash
claude --plugin-dir /path/to/arya-ai
```

The MCP server needs `uv` on the PATH. Install pandoc for DOCX export.

Claude-specific metadata is in:

```text
.claude-plugin/plugin.json
CLAUDE.md
```

### Claude Desktop MCP

Install as an MCPB-style local extension using `manifest.json`, or add this server config manually:

```json
{
  "mcpServers": {
    "arya-ai": {
      "command": "uv",
      "args": ["--directory", "/absolute/path/to/arya-ai", "run", "server/main.py"]
    }
  }
}
```

Requirements:

- Python 3.10+
- `uv`
- Optional: `pandoc` for DOCX export
- Optional: `pdftotext` for PDF text extraction

### Cursor

Cursor rules are in:

```text
.cursor/rules/arya-ai.mdc
```

Attach this repo to your workspace and reference `skills/arya-ai-orchestrator/SKILL.md` before Indian-law tasks.

### Gemini

Use `GEMINI.md` as the platform entry file. If your Gemini environment supports MCP, load `.mcp.json`.

### Any MCP Client

Run the server:

```bash
uv --directory /absolute/path/to/arya-ai run server/main.py
```

Then use the `arya-ai` MCP server tools.

## MCP Tools

arya-ai exposes these local tools:

- `list_arya_ai_capabilities`
- `list_legal_domains`
- `list_commands`
- `get_command_prompt`
- `list_specialist_agents`
- `get_specialist_agent`
- `search_protocols`
- `get_protocol`
- `list_drafting_templates`
- `get_drafting_template`
- `list_case_types`
- `get_case_type_format`
- `get_agent_instructions`
- `get_pleading_base`
- `list_forums`
- `get_forum_config`
- `resolve_bench`
- `get_reference_note`
- `read_case_folder`
- `create_case_folder`
- `save_artifact`
- `save_draft_as_docx`

## Drafting Pipeline

For any pleading (Maharashtra courts and tribunals, or NCLT/NCLAT/IBC), call `get_agent_instructions()` first. For a Maharashtra matter it also routes through `resolve_bench`, `get_forum_config` and the long-form template. The required workflow is:

1. Create a case folder.
2. Save source documents.
3. Load the case-type skill.
4. Load pleading base.
5. Reader extracts and pseudonymises facts.
6. Format maps facts to the forum structure.
7. Drafter creates draft v1.
8. Verifier checks facts, citations, annexures, and unsupported assertions.
9. Refiner fixes and polishes.
10. Overseer reviews as opposing counsel and hardens the final draft.
11. Save final DOCX locally.

Maharashtra case types: anticipatory-bail, application-482, bail, civil-suit, civil-wp, consumer-appeal-41, consumer-district-35, consumer-state-47, contempt-petition, criminal-appeal, criminal-revision, criminal-wp, drat-appeal, drt-oa, family-court-petition, first-appeal, gift-deed, ibc-section-7, labour-court-claim, mact-appeal-173, mact-claim-166, maharera-complaint, mat-oa, matrimonial-appeal, mortgage-deed, mrtu-pulp-complaint, ni-138-complaint, ni-138-reply-notice, partition-deed, pil, sale-deed-mh, sarfaesi-13-2-notice, sarfaesi-14, sarfaesi-17, second-appeal, title-investigation.

Supported company-law case types:

- `nclt-section-241-242-petition`
- `nclt-scheme-of-arrangement`
- `nclt-section-66-reduction-of-capital`
- `nclt-section-252-revival-struck-off-company`
- `nclt-section-213-investigation`
- `nclt-section-245-class-action`
- `nclat-appeal-section-421`
- `nclat-appeal-section-61-ibc`
- `ibc-section-9-operational-creditor-application`
- `ibc-section-10-corporate-applicant`

## Example Prompts

```text
Draft a legal notice for breach of a software services agreement under Indian law. Use placeholders where facts are missing.
```

```text
Check limitation, forum, and maintainability for this proposed civil suit.
```

```text
Search arya-ai protocols for Section 65B digital evidence and prepare a trial checklist.
```

```text
Draft an NCLT Section 241-242 oppression and mismanagement petition from these facts and documents.
```

```text
ABA before the Nagpur Bench in an FIR from Chandrapur under BNS 118.
```

```text
Draft the affidavit in reply to this writ petition for the respondent Municipal Corporation, Thane.
```

```text
Run the pre-filing checklist on this draft before I file it.
```

```text
Prepare an RTI application and first appeal strategy for non-disclosure by a public authority.
```

## Repository Layout

```text
arya-ai/
├── .codex-plugin/          Codex plugin manifest
├── .claude-plugin/         Claude-style plugin metadata
├── .cursor/rules/          Cursor rules
├── agents/                 Specialist legal agents
├── commands/               Legal command workflows
├── company-drafting-agents/ Six-agent company-law pipeline personas
├── docs/                   Licensing and documentation
├── maharashtra/            Forum configs, long-form templates, practice notes, pipeline notes
├── protocols/              Indian-law protocol reference library
├── server/                 Local MCP server
├── skills/                 Skills, templates, and drafting workflows
├── AGENTS.md               Generic agent instructions
├── CLAUDE.md               Claude entry instructions
├── GEMINI.md               Gemini entry instructions
├── manifest.json           MCPB-style manifest
└── pyproject.toml          Python/MCP runtime metadata
```

## Legal and Professional Disclaimer

arya-ai is a legal drafting and research aid. It does not replace an advocate's professional judgment. Every output must be checked by a qualified lawyer before filing, sending, or relying on it. Verify statutes, rules, limitation, citations, court fees, forum-specific practice directions, annexures, affidavits, authorisations, and procedural requirements from current primary sources.

## Licensing

The arya-ai integration code and original wrapper materials are MIT licensed. Bundled source materials retain their original licenses and notices in `docs/source-licenses/`.

Important: the supplied `NCLT-Skills-main.zip` archive contained proprietary restrictions that prohibit redistribution. Its files are not included here. arya-ai includes an original `skills/nclt-pdf-workflow/SKILL.md` replacement for local PDF and tribunal annexure workflows.
