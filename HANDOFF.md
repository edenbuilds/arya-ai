# arya-ai: handoff

Indian-law plugin for advocates (Claude Code plugin, Codex plugin, MCPB for Claude Desktop, local MCP server).
Repo: https://github.com/edenbuilds/arya-ai (public). Local: `~/arya-ai` (moved from `~/.tmp/arya-ai` on 01-11-2026).

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
- `npx @anthropic-ai/mcpb validate manifest.json` passes. `dist/arya-ai-1.1.0.mcpb` built (2.9 MB, 544 files).
- MCP over stdio: 22 tools listed. `resolve_bench("Chandrapur")` returns `bombay-hc-nagpur`. `create_case_folder("anticipatory-bail")` works.
  `get_agent_instructions()` returns the combined script.

## Not verified

- An install inside Claude Code (`/plugin marketplace add edenbuilds/arya-ai`): the headless CLI returned 401 in the agent sandbox.
- DOCX export: pandoc is not installed on this Mac.
- The Kolhapur circuit, DRT and MAT territorial lists, fees and pecuniary limits are from the pack's notes and carry VERIFY tags.

## Next prompt (paste-ready)

> In ~/arya-ai, install the plugin in Claude Code with `/plugin marketplace add edenbuilds/arya-ai` then
> `/plugin install arya-ai@arya-ai`, restart, and ask "ABA before the Nagpur Bench in an FIR from Chandrapur under BNS 118".
> Confirm it calls get_agent_instructions, resolve_bench and get_forum_config, and that the case folder lands in
> ~/Downloads/arya-ai-Drafts. `brew install pandoc` first so the DOCX step runs. Fix anything that breaks, bump the
> patch version in the three manifests and pyproject, rebuild dist/*.mcpb, then commit and push.
