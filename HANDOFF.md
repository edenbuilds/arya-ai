# arya-ai: handoff

Indian-law plugin for advocates (Claude Code plugin, Codex plugin, MCPB for Claude Desktop, local MCP server).
Repo: https://github.com/edenbuilds/arya-ai (public). Local: `~/arya-ai` (moved from `~/.tmp/arya-ai` on 01-11-2026).

## State at 1.2.0 (01-11-2026)

- Intake first: `skills/arya-intake/` plus the MCP tool `intake_questions(case_type)`. The orchestrator, the drafting
  orchestration script, CLAUDE.md, AGENTS.md and GEMINI.md all require asking Adv. Arya and waiting for her answers
  before any work. Per-instrument question sets cover bail, ABA, APL, s.138, writ, replies, RERA/consumer/MACT, contracts,
  memos, letters and deeds. For pipeline case types the skill's `format-from-user.md` is appended.
- `INSTALL.md`: uv and pandoc prerequisites, then Claude Code plugin, Claude Desktop `.mcpb`, and Codex/Cursor/Gemini/MCP.
- `ai-practice-safeguards` gained the template re-check calendar and a one-page chambers AI policy outline (from the course's
  Bonus module, in my own words).
- Not committed: `~/Downloads/LLM_Advocates_Complete_Study_Guide.md`. It is a full copy of the LLM Advocates course and
  the repo is public. Its useful frameworks are already in `arya-intake` and `ai-practice-safeguards`.
  `~/Downloads/indian-legal-ai-claude-SKILL.md` was folded into `arya-intake` (IRAC frame, code-selection rule,
  escalation list) as intake questions, with no prompt text copied.

## State at 1.1.0 (01-11-2026)

- Maharashtra courts drafting merged in from `~/vikram-shah-archive/companion/drafting/maharashtra-courts-drafting`:
  36 case-type skills in `skills/<case-type>-draft/`, plus `maharashtra/` (20 forum configs, 46 long-form templates,
  4 practice notes, short pipeline notes). Entry skill: `skills/maharashtra-courts-drafting/`.
  The companion copy is still the source for Case Companion's MCP. Edit there and recopy, or keep both in step.
- New MCP tools in `server/main.py`: `list_forums`, `get_forum_config`, `resolve_bench` (district to Bombay HC seat),
  `get_reference_note`. `list_drafting_templates` and `get_drafting_template` now include the Maharashtra templates
  (aliases such as `civil-wp`, `wp-reply-affidavit`, `APL`). The case types are discovered from the skill folders.
- Fixed: `get_agent_instructions(<stage>)` pointed at `agents/` and always failed. It now reads `company-drafting-agents/`
  and appends the Maharashtra stage notes.
- Fixed: 17 agents and several commands had YAML frontmatter that did not parse, so they loaded with no description.
- `skills/indian-business-docs/`: vendored from mnbresearch/mnb-claude-skills (MIT).
- `skills/ai-practice-safeguards/`: original text, structured after the LLM Advocates course. Covers anonymisation,
  five hallucination types, the pre-filing checklist, the matter brief, four-tier contract review and the
  devil's-advocate pass. No course text was copied, and the course's "Drafting Skill Library" is paid and was not used.

## Verified

- `claude plugin validate` passes (one warning: CLAUDE.md at the root is not loaded by Claude Code).
- `npx @anthropic-ai/mcpb validate manifest.json` passes. `dist/arya-ai-1.2.0.mcpb` built (547 files) and attached to the GitHub release.
- MCP over stdio: 23 tools listed. `intake_questions("anticipatory-bail")` returns the general and instrument questions. `resolve_bench("Chandrapur")` returns `bombay-hc-nagpur`. `create_case_folder("anticipatory-bail")` works.
  `get_agent_instructions()` returns the combined script.
- DOCX export (01-11-2026, pandoc 3.13): the ABA long-form template rendered through `save_draft_as_docx` with
  `reference.docx` applied. A4, Times New Roman 14, 1.5 line spacing, 4 cm left margin, matching Bombay HC house style.
- `.mcp.json` uses `${CLAUDE_PLUGIN_ROOT:-.}` so the server also starts when the repo is opened as a project (it failed
  with "Connection closed" before). Project-mode start still needs the one-time server approval in `claude`.

## Not verified

- An install inside Claude Code (`/plugin marketplace add edenbuilds/arya-ai`): the headless CLI returned 401 in the agent sandbox.
- The Kolhapur circuit, DRT and MAT territorial lists, fees and pecuniary limits are from the pack's notes and carry VERIFY tags.

## Next prompt (paste-ready)

> In ~/arya-ai, install the plugin in Claude Code with `/plugin marketplace add edenbuilds/arya-ai` then
> `/plugin install arya-ai@arya-ai`, restart, and ask "ABA before the Nagpur Bench in an FIR from Chandrapur under BNS 118".
> Confirm it first asks the intake questions and waits, then calls get_agent_instructions, resolve_bench and get_forum_config, and that the case folder lands in
> ~/Downloads/arya-ai-Drafts. Fix anything that breaks, bump the
> patch version in plugin.json, marketplace.json, .codex-plugin/plugin.json, manifest.json and pyproject.toml, rebuild dist/*.mcpb, then commit and push.
