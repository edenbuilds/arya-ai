"""arya-ai — Indian legal research and drafting MCP server.

Local-first tools for Indian lawyers: protocol search, prompt retrieval,
drafting templates, and company-law/NCLT/NCLAT/IBC drafting workflows.
"""

from __future__ import annotations

import re
import subprocess
from datetime import datetime
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

DEFAULT_DRAFTS_ROOT = Path.home() / "Downloads" / "arya-ai-Drafts"
ALLOWED_ARTIFACT_NAMES = {
    "case-facts.md",
    "format-shell.md",
    "draft-v1.md",
    "draft-v1.docx",
    "verification-report.md",
    "draft-v2.md",
    "draft-v2.docx",
    "opposing-notes.md",
    "final-draft.md",
}

mcp = FastMCP("arya-ai")

BUNDLE_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = BUNDLE_ROOT / "skills"
AGENTS_DIR = BUNDLE_ROOT / "agents"
PIPELINE_AGENTS_DIR = BUNDLE_ROOT / "company-drafting-agents"
MH_DIR = BUNDLE_ROOT / "maharashtra"
MH_FORUMS_DIR = MH_DIR / "forum-config" / "exemplars"
MH_TEMPLATES_DIR = MH_DIR / "templates"
MH_REFERENCES_DIR = MH_DIR / "references"
COMMANDS_DIR = BUNDLE_ROOT / "commands"
PROTOCOLS_DIR = BUNDLE_ROOT / "protocols"
TEMPLATES_DIR = SKILLS_DIR / "indian-legal-drafting" / "assets" / "templates"
PLEADING_BASE_DIR = SKILLS_DIR / "_company_drafting_base"

CASE_TYPES: list[str] = [
    "nclt-section-241-242-petition",
    "nclt-scheme-of-arrangement",
    "nclt-section-66-reduction-of-capital",
    "nclt-section-252-revival-struck-off-company",
    "nclt-section-213-investigation",
    "nclt-section-245-class-action",
    "nclat-appeal-section-421",
    "nclat-appeal-section-61-ibc",
    "ibc-section-9-operational-creditor-application",
    "ibc-section-10-corporate-applicant",
]

CASE_TYPE_DESCRIPTIONS: dict[str, str] = {
    "nclt-section-241-242-petition": "NCLT oppression and mismanagement petition under Sections 241-242 Companies Act 2013",
    "nclt-scheme-of-arrangement": "NCLT scheme of arrangement / amalgamation under Sections 230-232",
    "nclt-section-66-reduction-of-capital": "NCLT capital reduction petition under Section 66",
    "nclt-section-252-revival-struck-off-company": "NCLT revival of struck-off company under Section 252",
    "nclt-section-213-investigation": "NCLT investigation petition under Section 213 / 214",
    "nclt-section-245-class-action": "NCLT class action under Section 245",
    "nclat-appeal-section-421": "NCLAT appeal under Section 421 Companies Act",
    "nclat-appeal-section-61-ibc": "NCLAT appeal under Section 61 IBC",
    "ibc-section-9-operational-creditor-application": "IBC Section 9 operational creditor application",
    "ibc-section-10-corporate-applicant": "IBC Section 10 corporate applicant initiation",
}



def _frontmatter_description(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines()[1:10]:
        if line.startswith("description:"):
            return line.removeprefix("description:").strip()
    return ""


# Maharashtra court and tribunal case types come from the skills/*-draft folders
# merged in from the Maharashtra drafting pack (vikram-shah-archive companion).
MH_CASE_TYPES: list[str] = sorted(
    d.name.removesuffix("-draft")
    for d in SKILLS_DIR.glob("*-draft")
    if (d / "SKILL.md").is_file() and d.name.removesuffix("-draft") not in CASE_TYPES
)
CASE_TYPE_DESCRIPTIONS.update({c: _frontmatter_description(SKILLS_DIR / f"{c}-draft" / "SKILL.md") for c in MH_CASE_TYPES})
CASE_TYPES = CASE_TYPES + MH_CASE_TYPES

AGENT_NAMES: list[str] = ["reader", "format", "drafter", "verifier", "refiner", "overseer"]

# The user's acronym decides the case type. APL is quashing, not ABA; MAT is the
# Administrative Tribunal, not a matrimonial matter.
ACRONYM_TO_CASE_TYPE: dict[str, str] = {
    "APL": "application-482",
    "ABA": "anticipatory-bail",
    "BA": "bail",
    "WP": "civil-wp",
    "CrWP": "criminal-wp",
    "PIL": "pil",
    "FA": "first-appeal",
    "SA": "second-appeal",
    "MAT OA": "mat-oa",
    "OA (DRT)": "drt-oa",
    "SA (SARFAESI s.17)": "sarfaesi-17",
    "CP (Company Petition 241-242)": "nclt-section-241-242-petition",
    "CP (IB) s.7": "ibc-section-7",
    "CP (IB) s.9": "ibc-section-9-operational-creditor-application",
    "CP (IB) s.10": "ibc-section-10-corporate-applicant",
}

# Bombay High Court seat by district, from maharashtra/references/territorial-jurisdiction.md.
HC_BENCH_DISTRICTS: dict[str, list[str]] = {
    "bombay-hc-mumbai": ["mumbai", "mumbai city", "mumbai suburban", "thane", "palghar", "nashik", "pune", "raigad"],
    "bombay-hc-kolhapur": ["satara", "sangli", "solapur", "kolhapur", "ratnagiri", "sindhudurg"],
    "bombay-hc-nagpur": ["nagpur", "akola", "amravati", "bhandara", "buldhana", "chandrapur", "wardha", "yavatmal", "gondia", "gadchiroli", "washim"],
    "bombay-hc-aurangabad": ["aurangabad", "chhatrapati sambhajinagar", "ahmednagar", "ahilyanagar", "beed", "dhule", "jalna", "jalgaon", "latur", "nanded", "osmanabad", "dharashiv", "parbhani", "nandurbar", "hingoli"],
}


def _safe_slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]", "-", value.strip()).strip(".-_")


def _read_text_file(path: Path, max_chars: int | None = None) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    return text if max_chars is None else text[:max_chars]


def _relative_file_under(root: Path, relative_path: str) -> Path:
    rel = Path(relative_path)
    if rel.is_absolute() or any(part == ".." for part in rel.parts):
        raise ValueError("path must be relative and must not contain '..'")
    target = (root / rel).resolve()
    target.relative_to(root.resolve())
    if not target.is_file():
        raise FileNotFoundError(relative_path)
    return target


def _first_heading_or_line(path: Path) -> str:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip().lstrip("#").strip()
        if stripped and not stripped.startswith("---") and ":" not in stripped[:24]:
            return stripped[:160]
    return path.stem.replace("-", " ").title()


@mcp.tool(annotations=ToolAnnotations(title="List arya-ai Capabilities", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def list_arya_ai_capabilities() -> dict:
    """Return a high-level inventory of bundled arya-ai assets."""
    skill_count = len(list(SKILLS_DIR.glob("*/SKILL.md")))
    return {
        "name": "arya-ai",
        "summary": "Indian legal assistant for research, drafting, litigation strategy, Bombay High Court and Maharashtra tribunal pleadings, NCLT/NCLAT/IBC pleadings, and local document workflows.",
        "counts": {
            "specialist_agents": len(list(AGENTS_DIR.glob("*.md"))),
            "commands": len(list(COMMANDS_DIR.glob("*.md"))),
            "skills": skill_count,
            "protocols": len(list(PROTOCOLS_DIR.rglob("*.md"))),
            "drafting_case_types": len(CASE_TYPES),
            "maharashtra_case_types": len(MH_CASE_TYPES),
            "maharashtra_forums": len(list(MH_FORUMS_DIR.glob("*.md"))),
            "drafting_templates": len(_template_paths()),
        },
        "domains": [
            "contract law",
            "criminal law",
            "civil procedure",
            "corporate law",
            "Bombay High Court and Maharashtra tribunals",
            "NCLT/NCLAT",
            "IBC",
            "labour law",
            "property law",
            "intellectual property",
            "consumer and RERA",
            "RTI, PIL, writs, civic remedies",
            "ADR",
            "PDF/document workflows",
        ],
        "start_here": "Use skills/arya-ai-orchestrator/SKILL.md or call search_protocols(), list_commands(), list_specialist_agents(), and list_case_types().",
    }


@mcp.tool(annotations=ToolAnnotations(title="List Legal Domains", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def list_legal_domains() -> dict:
    """List protocol directories and the number of reference files in each."""
    domains: dict[str, int] = {}
    if PROTOCOLS_DIR.exists():
        for folder in sorted(p for p in PROTOCOLS_DIR.iterdir() if p.is_dir()):
            domains[folder.name] = len(list(folder.rglob("*.md")))
    return {"domains": domains}


@mcp.tool(annotations=ToolAnnotations(title="List arya-ai Commands", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def list_commands() -> dict:
    """List command prompts available in the command pack."""
    commands = []
    for path in sorted(COMMANDS_DIR.glob("*.md")):
        commands.append({"name": path.stem, "path": path.relative_to(BUNDLE_ROOT).as_posix(), "title": _first_heading_or_line(path)})
    return {"commands": commands, "count": len(commands)}


@mcp.tool(annotations=ToolAnnotations(title="Get Command Prompt", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_command_prompt(command_name: str) -> dict:
    """Return a command prompt by name, for example 'draft-contract'."""
    name = _safe_slug(command_name.removesuffix(".md"))
    path = COMMANDS_DIR / f"{name}.md"
    if not path.is_file():
        return {"error": f"unknown command '{command_name}'", "available": [p.stem for p in sorted(COMMANDS_DIR.glob("*.md"))]}
    return {"name": name, "path": path.relative_to(BUNDLE_ROOT).as_posix(), "content": _read_text_file(path)}


@mcp.tool(annotations=ToolAnnotations(title="List Specialist Agents", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def list_specialist_agents() -> dict:
    """List legal specialist personas bundled with arya-ai."""
    agents = []
    for path in sorted(AGENTS_DIR.glob("*.md")):
        agents.append({"name": path.stem, "path": path.relative_to(BUNDLE_ROOT).as_posix(), "title": _first_heading_or_line(path)})
    return {"agents": agents, "count": len(agents)}


@mcp.tool(annotations=ToolAnnotations(title="Get Specialist Agent", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_specialist_agent(agent_name: str) -> dict:
    """Return a specialist agent persona by name."""
    name = _safe_slug(agent_name.removesuffix(".md"))
    path = AGENTS_DIR / f"{name}.md"
    if not path.is_file():
        return {"error": f"unknown agent '{agent_name}'", "available": [p.stem for p in sorted(AGENTS_DIR.glob("*.md"))]}
    return {"name": name, "path": path.relative_to(BUNDLE_ROOT).as_posix(), "content": _read_text_file(path)}


@mcp.tool(annotations=ToolAnnotations(title="Search Legal Protocols", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def search_protocols(query: str, domain: str = "", limit: int = 12) -> dict:
    """Search bundled Indian-law protocol references by filename and content.

    Args:
        query: Search terms, for example 'specific performance' or 'section 65b'.
        domain: Optional top-level protocol domain such as 'contract_law'.
        limit: Maximum results, capped at 30.
    """
    terms = [t.lower() for t in re.findall(r"[a-zA-Z0-9]+", query)]
    if not terms:
        return {"error": "query must contain at least one alphanumeric term", "results": []}
    root = PROTOCOLS_DIR / domain if domain else PROTOCOLS_DIR
    if not root.exists():
        return {"error": f"unknown protocol domain '{domain}'", "results": []}
    results = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(PROTOCOLS_DIR).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        haystack = f"{rel}\n{text}".lower()
        score = sum(haystack.count(term) for term in terms)
        if score <= 0:
            continue
        first_index = min((haystack.find(term) for term in terms if haystack.find(term) >= 0), default=0)
        start = max(0, first_index - 160)
        end = min(len(text), first_index + 360)
        snippet = " ".join(text[start:end].split())
        results.append({"path": rel, "score": score, "snippet": snippet[:500]})
    results.sort(key=lambda item: (-item["score"], item["path"]))
    capped = max(1, min(int(limit), 30))
    return {"query": query, "domain": domain or "all", "results": results[:capped], "count": len(results)}


@mcp.tool(annotations=ToolAnnotations(title="Get Legal Protocol", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_protocol(relative_path: str) -> dict:
    """Return a protocol markdown file by path relative to protocols/."""
    try:
        path = _relative_file_under(PROTOCOLS_DIR, relative_path)
    except (ValueError, FileNotFoundError) as exc:
        return {"error": str(exc)}
    return {"path": path.relative_to(PROTOCOLS_DIR).as_posix(), "content": _read_text_file(path)}


@mcp.tool(annotations=ToolAnnotations(title="List Drafting Templates", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def list_drafting_templates() -> dict:
    """List drafting templates: general Indian forms plus Maharashtra long-form pleadings.

    Maharashtra templates are grouped (high-court, tribunals, applications, trial,
    conveyancing) and include opposite-side drafts such as a writ reply affidavit.
    """
    templates = [
        {"name": path.stem, "group": "general" if path.parent == TEMPLATES_DIR else path.parent.name, "path": path.relative_to(BUNDLE_ROOT).as_posix(), "title": _first_heading_or_line(path)}
        for path in _template_paths()
    ]
    return {"templates": templates, "count": len(templates)}


# Short names the Maharashtra pack's README and USAGE use.
TEMPLATE_ALIASES = {
    "civil-wp": "civil-writ-petition",
    "criminal-wp": "criminal-writ-petition",
    "wp-reply-affidavit": "affidavit-in-reply-writ",
    "wp-rejoinder": "rejoinder-affidavit-writ",
    "aba": "anticipatory-bail",
    "apl": "application-528-bnss",
}


def _template_paths() -> list[Path]:
    general = sorted(TEMPLATES_DIR.glob("*.md")) if TEMPLATES_DIR.exists() else []
    mh = sorted(p for p in MH_TEMPLATES_DIR.glob("*/*.md")) if MH_TEMPLATES_DIR.exists() else []
    return general + mh


@mcp.tool(annotations=ToolAnnotations(title="Get Drafting Template", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_drafting_template(template_name: str) -> dict:
    """Return a general drafting template such as legal_notice or civil_suit."""
    name = _safe_slug(template_name.removesuffix(".md")).lower()
    name = TEMPLATE_ALIASES.get(name, name)
    paths = _template_paths()
    path = next((p for p in paths if _safe_slug(p.stem) == name), None)
    if path is None:
        # ponytail: substring match so "civil-wp" finds civil-writ-petition; ambiguity is reported, not guessed.
        hits = [p for p in paths if all(tok in _safe_slug(p.stem) for tok in name.split("-") if tok)]
        if len(hits) != 1:
            return {"error": f"unknown or ambiguous template '{template_name}'", "matches": [p.stem for p in hits], "available": [p.stem for p in paths]}
        path = hits[0]
    return {"name": path.stem, "path": path.relative_to(BUNDLE_ROOT).as_posix(), "content": _read_text_file(path)}


@mcp.tool(annotations=ToolAnnotations(title="List Maharashtra Forums", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def list_forums() -> dict:
    """List Bombay High Court seats and Maharashtra tribunals that have a forum-config."""
    forums = [{"forum_id": p.stem, "title": _first_heading_or_line(p)} for p in sorted(MH_FORUMS_DIR.glob("*.md"))]
    return {"forums": forums, "count": len(forums), "note": "Call get_forum_config(forum_id) for the header, cause-title, annexure and paper rules."}


@mcp.tool(annotations=ToolAnnotations(title="Get Forum Config", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_forum_config(forum_id: str) -> dict:
    """Return the forum-config (court header, house style, annexure prefix, fees note) for one forum."""
    path = MH_FORUMS_DIR / f"{_safe_slug(forum_id)}.md"
    if not path.is_file():
        return {"error": f"unknown forum '{forum_id}'", "available": [p.stem for p in sorted(MH_FORUMS_DIR.glob("*.md"))]}
    return {"forum_id": path.stem, "content": _read_text_file(path)}


@mcp.tool(annotations=ToolAnnotations(title="Resolve Bombay High Court Bench", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def resolve_bench(district: str, forum_class: str = "high-court") -> dict:
    """Map a Maharashtra district to its Bombay High Court seat.

    For tribunals (MAT, DRT, consumer, MACT, NCLT, labour) the territorial note is
    returned instead, because their limits change by notification.
    """
    key = district.strip().lower().removesuffix(" district")
    note = _read_text_file(MH_REFERENCES_DIR / "territorial-jurisdiction.md")
    if forum_class != "high-court":
        return {"district": district, "forum_class": forum_class, "territorial_note": note}
    for forum_id, districts in HC_BENCH_DISTRICTS.items():
        if key in districts:
            result = {"district": district, "forum_id": forum_id, "verify": "Confirm the sitting notification on bombayhighcourt.nic.in before filing."}
            if forum_id == "bombay-hc-kolhapur":
                result["caveat"] = "Kolhapur circuit: if it is not sitting for the cause-list week, these districts stay with the Principal Seat (bombay-hc-mumbai)."
            return result
    return {"district": district, "error": "district not in the Bombay High Court map; it may be outside Maharashtra or spelled differently", "territorial_note": note}


@mcp.tool(annotations=ToolAnnotations(title="Get Maharashtra Reference Note", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_reference_note(name: str) -> dict:
    """Return a Maharashtra practice note: territorial-jurisdiction, acronyms, court-fees-stamp or efiling."""
    path = MH_REFERENCES_DIR / f"{_safe_slug(name.removesuffix('.md'))}.md"
    if not path.is_file():
        return {"error": f"unknown note '{name}'", "available": [p.stem for p in sorted(MH_REFERENCES_DIR.glob("*.md"))]}
    return {"name": path.stem, "content": _read_text_file(path)}


FULL_ORCHESTRATION_SCRIPT = """# arya-ai — DRAFTING · FULL ORCHESTRATION SCRIPT
# Company-law forums (NCLT / NCLAT / IBC) and Maharashtra courts and tribunals
# (Bombay High Court seats, MAT, MACT, Consumer, DRT/DRAT, Labour/Industrial, MahaRERA, Family, trial courts)

**YOU MUST execute every step below in order. DO NOT skip steps. DO NOT write
standalone python-docx, JavaScript, or shell scripts to generate output —
invoke the tools listed at each step.**

## BEFORE STEP 0 — ASK ADV. ARYA, THEN WAIT

Call `intake_questions(case_type)` and put those questions to the advocate as one numbered list.
Skip what she has already told you. STOP and wait for her answers; do not start STEP 0 until she replies.
If she has a reference draft, follow its structure, headings, cause title, numbering and register,
and take nothing factual from it about this matter.

## STEP 0 — CREATE THE CASE FOLDER

Call `create_case_folder(case_type)` with a slug from `list_case_types()`.

For a Maharashtra case type, also:
- `resolve_bench(district)` for a High Court matter, or `get_reference_note("territorial-jurisdiction")` for a tribunal;
- `get_forum_config(forum_id)` for the header and house style;
- `get_drafting_template(...)` for the long-form official form (writ, reply affidavit, rejoinder, MACT, consumer, DRT, deeds).

The tool returns `case_folder` — an absolute path. **Use this path in every
subsequent save_artifact and save_draft_as_docx call.**

## STEP 1 — MATERIALIZE THE USER'S INPUT DOCUMENTS

Every source document the user attached to this conversation must be saved to
disk before the Reader can run. For each attachment:

Call `save_artifact(case_folder, "inputs/source-document.txt", <extracted-text>)`

## STEP 2 — LOAD THE CASE-TYPE SKILL

Call `get_case_type_format(case_type)`. Read the returned SKILL.md carefully.

## STEP 3 — LOAD THE PLEADING BASE

Call `get_pleading_base(case_type)`. Read the universal skeleton + common drafting
discipline (citation rules, AI-fabricated-citation risk per HC cautions).

## STEP 4 — RUN THE READER AGENT (APPLIES PRIVACY FIREWALL)

Call `get_agent_instructions("reader")` to load the Reader persona. The Reader
applies the privacy firewall — substitutes party names, addresses, identifying
numbers, financial figures, statutory-notice references with structural
placeholders BEFORE any downstream agent processes the facts.

Save the output via `save_artifact(case_folder, "case-facts.md", <content>)`.

## STEP 5 — RUN THE FORMAT AGENT

Call `get_agent_instructions("format")`. Map case-facts.md (already privacy-
firewalled) into the SKILL.md placeholders.

Save via `save_artifact(case_folder, "format-shell.md", <content>)`.

## STEP 6 — RUN THE DRAFTER AGENT

Call `get_agent_instructions("drafter")`. Write the first complete draft using
format-shell.md as scaffold and case-facts.md as ground-truth.

Save markdown via `save_artifact(case_folder, "draft-v1.md", <content>)`. Then
`save_draft_as_docx(<markdown>, f"{case_folder}/draft-v1.docx")`.

## STEP 7 — RUN THE VERIFIER AGENT (ANTI-HALLUCINATION FIREWALL — DO NOT SKIP)

Call `get_agent_instructions("verifier")`. Compare draft-v1.md against
case-facts.md fact-by-fact. Flag every hallucinated date, fabricated citation,
unsupported assertion, orphan annexure marker, missing factual basis.

Save via `save_artifact(case_folder, "verification-report.md", <content>)`.

## STEP 8 — RUN THE REFINER AGENT

Call `get_agent_instructions("refiner")`. Apply every Verifier flag. Polish
language. Enforce Registry formatting.

Save via `save_artifact(case_folder, "draft-v2.md", <content>)` and
`save_draft_as_docx(<markdown>, f"{case_folder}/draft-v2.docx")`.

## STEP 9 — RUN THE OVERSEER AGENT (OPPOSING-COUNSEL LENS — DO NOT SKIP)

Call `get_agent_instructions("overseer")`. Read draft-v2.md with opposing-
counsel lens. Find weak prayers, contradictory facts, attackable defects.

Save via `save_artifact(case_folder, "opposing-notes.md", <content>)`. Then
apply hardening to produce final draft. Save via
`save_artifact(case_folder, "final-draft.md", <content>)` and
`save_draft_as_docx(<markdown>, f"{case_folder}/final-draft.docx")`.

## STEP 10 — REPORT TO THE USER

Return the absolute path to `final-draft.docx` and a one-paragraph summary.

---

**FALSIFICATION CHECK:** the case folder must contain at minimum:
1. case-facts.md
2. format-shell.md
3. draft-v1.docx (or draft-v1.md)
4. verification-report.md
5. draft-v2.docx (or draft-v2.md)
6. final-draft.docx

If any are missing, return to the matching STEP and produce it.

**REMINDER:** YOU MUST NOT write a standalone python-docx generator, a
JavaScript script, or any one-shot drafting program. The MCPB exposes every
required tool. Use them.
"""

@mcp.tool(annotations=ToolAnnotations(title="Get Intake Questions", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def intake_questions(case_type: str = "") -> str:
    """Questions to ask the advocate before any work starts. Call this first, ask, then wait for answers.

    With a case_type from list_case_types(), the instrument's own "facts the user
    must supply" list is appended to the general intake.
    """
    text = (SKILLS_DIR / "arya-intake" / "SKILL.md").read_text(encoding="utf-8")
    extra = SKILLS_DIR / f"{case_type}-draft" / "format-from-user.md"
    if case_type and extra.is_file():
        text += "\n\n---\n\n" + extra.read_text(encoding="utf-8")
    return text


@mcp.tool(annotations=ToolAnnotations(title="List Available Case Types", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def list_case_types() -> dict:
    """List all case types this connector can draft.

    Returns a dict with the list of case types, a short description of each,
    AND an acronym disambiguation map (Indian advocacy acronyms / Form
    references / statutory section references -> case_type).

    CRITICAL: the user's acronym IS the source of truth for case_type
    classification. Do not infer case_type from input-document content.
    """
    return {
        "case_types": CASE_TYPES,
        "descriptions": CASE_TYPE_DESCRIPTIONS,
        "acronym_to_case_type": ACRONYM_TO_CASE_TYPE,
        "note": "Call get_case_type_format(case_type) for the full drafting skill.",
    }


@mcp.tool(annotations=ToolAnnotations(title="Get Case Type Drafting Format", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_case_type_format(case_type: str) -> str:
    """Get the drafting format SKILL.md for a given case type.

    Returns the full SKILL.md content for the case type, including statutory
    anchors, format placeholders, and the drafting checklist. Also appends
    format-from-user.md if present in the same skill folder.

    Args:
        case_type: One of the slugs returned by list_case_types().
    """
    if case_type not in CASE_TYPES:
        return (
            f"Error: unknown case_type '{case_type}'. "
            f"Available: {', '.join(CASE_TYPES)}. "
            "Call list_case_types() for descriptions."
        )

    skill_dir = SKILLS_DIR / f"{case_type}-draft"
    skill_md = skill_dir / "SKILL.md"
    format_from_user = skill_dir / "format-from-user.md"

    if not skill_md.exists():
        return f"Error: skill file not found for case_type '{case_type}'."

    parts = ["# Case-type skill: " + case_type, "", skill_md.read_text(encoding="utf-8")]
    if format_from_user.exists():
        parts.extend(
            [
                "",
                "---",
                "",
                "# Format expected from user (case-type checklist)",
                "",
                format_from_user.read_text(encoding="utf-8"),
            ]
        )
    return "\n".join(parts)



@mcp.tool(annotations=ToolAnnotations(title="Get Pipeline Agent Instructions", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_agent_instructions(agent_name: str = "") -> str:
    """Get the instructions for the drafting pipeline.

    Default mode (no agent_name, or agent_name=""): returns the FULL orchestration
    script enumerating every step and tool call from case-folder creation through
    final-draft.docx. THIS IS THE MANDATORY FIRST CALL when the user asks you to
    draft anything.

    Single-agent mode (agent_name ∈ {reader, format, drafter, verifier, refiner,
    overseer}): returns that agent's persona instructions only.
    """
    if not agent_name or agent_name == "full":
        return FULL_ORCHESTRATION_SCRIPT
    if agent_name not in AGENT_NAMES:
        return (
            f"Error: unknown agent_name '{agent_name}'. "
            f"Available: {', '.join(AGENT_NAMES)}. "
            "Call with no arguments to receive the full orchestration script."
        )
    agent_md = PIPELINE_AGENTS_DIR / agent_name / f"{agent_name}.md"
    if not agent_md.exists():
        return f"Error: agent file not found for '{agent_name}'."
    text = agent_md.read_text(encoding="utf-8")
    mh_md = MH_DIR / "agents" / agent_name / f"{agent_name}.md"
    if mh_md.exists():
        text += "\n\n---\n\n# Maharashtra courts and tribunals (apply for non-company case types)\n\n" + mh_md.read_text(encoding="utf-8")
    return text


@mcp.tool(annotations=ToolAnnotations(title="Get Pleading Base Structure", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_pleading_base(case_type: str = "") -> str:
    """Get the shared pleading skeleton and common drafting discipline.

    Pass a Maharashtra case_type (writ, bail, MACT, consumer, DRT and so on) to get
    the Maharashtra pleading base; otherwise the company-law base is returned.
    """
    if case_type in MH_CASE_TYPES:
        return "\n\n---\n\n".join(
            (MH_DIR / name).read_text(encoding="utf-8") for name in ("pleading-base.md", "drafting-common.md")
        )
    common_md = SKILLS_DIR / "_drafting_common" / "SKILL.md"
    parts: list[str] = []
    if PLEADING_BASE_DIR.exists():
        for md_file in sorted(PLEADING_BASE_DIR.glob("*.md")):
            parts.extend([f"# {md_file.stem}", "", md_file.read_text(encoding="utf-8"), "", "---", ""])
    if common_md.exists():
        parts.extend(["# Common Drafting Discipline", "", common_md.read_text(encoding="utf-8")])
    return "\n".join(parts)



@mcp.tool(annotations=ToolAnnotations(title="Read Case Folder Files", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def read_case_folder(path: str) -> dict:
    """Read all files in a case folder.

    Args:
        path: Absolute or relative path to the case folder.
    """
    folder = Path(path).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        return {"error": f"Path '{path}' is not a valid directory.", "files": {}, "warnings": [], "file_count": 0}
    files: dict[str, str] = {}
    warnings: list[str] = []
    for f in sorted(folder.rglob("*")):
        if not f.is_file() or any(p.startswith(".") for p in f.relative_to(folder).parts):
            continue
        rel = f.relative_to(folder).as_posix()
        ext = f.suffix.lower()
        try:
            if ext in (".md", ".txt"):
                files[rel] = f.read_text(encoding="utf-8", errors="replace")
            elif ext == ".pdf":
                try:
                    r = subprocess.run(["pdftotext", str(f), "-"], capture_output=True, text=True, timeout=30)
                    files[rel] = r.stdout if r.returncode == 0 else f"[PDF at {rel} — extract failed]"
                    if r.returncode != 0:
                        warnings.append(f"pdftotext failed on {rel}")
                except FileNotFoundError:
                    warnings.append("pdftotext not installed")
                    files[rel] = f"[PDF at {rel} — pdftotext not installed]"
                except subprocess.TimeoutExpired:
                    warnings.append(f"pdftotext timed out on {rel}")
            elif ext == ".docx":
                try:
                    r = subprocess.run(["pandoc", "-f", "docx", "-t", "markdown", str(f)], capture_output=True, text=True, timeout=30)
                    files[rel] = r.stdout if r.returncode == 0 else f"[DOCX at {rel} — extract failed]"
                    if r.returncode != 0:
                        warnings.append(f"pandoc failed on {rel}")
                except FileNotFoundError:
                    warnings.append("pandoc not installed")
                    files[rel] = f"[DOCX at {rel} — pandoc not installed]"
                except subprocess.TimeoutExpired:
                    warnings.append(f"pandoc timed out on {rel}")
            else:
                warnings.append(f"Skipped unsupported file type: {rel}")
        except Exception as exc:
            warnings.append(f"Error reading {rel}: {exc}")
    return {"folder": str(folder), "files": files, "warnings": warnings, "file_count": len(files)}


@mcp.tool(annotations=ToolAnnotations(title="Save Draft as Filing-Grade DOCX", readOnlyHint=False, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def save_draft_as_docx(markdown_text: str, output_path: str) -> dict:
    """Save markdown draft as filing-grade .docx using pandoc.

    Args:
        markdown_text: Draft content in markdown.
        output_path: Where to save the .docx file.
    """
    output = Path(output_path).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    reference_docx = PLEADING_BASE_DIR / "reference.docx" if (PLEADING_BASE_DIR / "reference.docx").exists() else None
    temp_md = output.parent / f".{output.stem}.tmp.md"
    temp_md.write_text(markdown_text, encoding="utf-8")
    cmd = ["pandoc", str(temp_md), "-o", str(output)]
    if reference_docx:
        cmd.extend(["--reference-doc", str(reference_docx)])
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        temp_md.unlink(missing_ok=True)
        if r.returncode != 0:
            return {"success": False, "error": r.stderr.strip()[:500], "output_path": str(output)}
        return {"success": True, "output_path": str(output), "file_size_bytes": output.stat().st_size, "reference_docx_applied": reference_docx is not None}
    except FileNotFoundError:
        temp_md.unlink(missing_ok=True)
        return {"success": False, "error": "pandoc not installed.", "output_path": str(output)}
    except subprocess.TimeoutExpired:
        temp_md.unlink(missing_ok=True)
        return {"success": False, "error": "pandoc conversion timed out after 60s.", "output_path": str(output)}


def _sanitise_path_component(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9._-]", "-", value.strip())
    cleaned = cleaned.strip(".-_") or "untitled"
    return cleaned[:80]


@mcp.tool(annotations=ToolAnnotations(title="Create Case Folder", readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=False))
def create_case_folder(case_type: str, base_dir: str = "") -> dict:
    """Create the case folder for a drafting session on the user's machine.

    Creates a timestamped folder under ~/Downloads/arya-ai-Drafts/ (or the
    base_dir if supplied) named <case-type>-<YYYYMMDD-HHMMSS>/, with an inputs/
    subfolder for source documents. Cross-platform (macOS / Windows / Linux).
    """
    if case_type not in CASE_TYPES:
        return {"error": f"unknown case_type '{case_type}'. Available: {', '.join(CASE_TYPES)}."}
    parent = Path(base_dir).expanduser().resolve() if base_dir else DEFAULT_DRAFTS_ROOT
    parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    folder_name = f"{_sanitise_path_component(case_type)}-{timestamp}"
    case_folder = parent / folder_name
    inputs_folder = case_folder / "inputs"
    inputs_folder.mkdir(parents=True, exist_ok=True)
    readme = case_folder / "README.md"
    readme.write_text(
        f"# arya-ai Drafting Case Folder\n\n"
        f"- Case type: {case_type}\n"
        f"- Created: {datetime.now().isoformat(timespec='seconds')}\n\n"
        f"## Artifacts (pipeline output)\n"
        f"- `inputs/` — source documents\n"
        f"- `case-facts.md` — Reader output (privacy-firewalled)\n"
        f"- `format-shell.md` — Format output\n"
        f"- `draft-v1.docx` — Drafter output\n"
        f"- `verification-report.md` — Verifier output\n"
        f"- `draft-v2.docx` — Refiner output\n"
        f"- `opposing-notes.md` — Overseer output\n"
        f"- `final-draft.docx` — Final filing-grade output\n",
        encoding="utf-8",
    )
    return {
        "case_folder": str(case_folder),
        "inputs_folder": str(inputs_folder),
        "case_type": case_type,
        "timestamp": timestamp,
        "next_step": (
            "Save every source document the user attached to this conversation "
            f"into '{inputs_folder}' via save_artifact, then proceed to STEP 2 "
            "of the orchestration script (get_case_type_format)."
        ),
    }


@mcp.tool(annotations=ToolAnnotations(title="Save Pipeline Artifact", readOnlyHint=False, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def save_artifact(case_folder: str, relative_path: str, content: str) -> dict:
    """Save a pipeline artifact or input document into the case folder.

    Required at the end of every agent step. Pipeline artifact names accepted at
    the root: case-facts.md, format-shell.md, draft-v1.md, draft-v1.docx,
    verification-report.md, draft-v2.md, draft-v2.docx, opposing-notes.md,
    final-draft.md. Input documents go under inputs/ (e.g.,
    'inputs/source-document.txt').
    """
    case_dir = Path(case_folder).expanduser().resolve()
    if not case_dir.exists() or not case_dir.is_dir():
        return {"success": False, "error": f"case_folder '{case_folder}' does not exist. Call create_case_folder first."}
    rel = Path(relative_path)
    if rel.is_absolute():
        return {"success": False, "error": "relative_path must not be absolute."}
    if any(part == ".." for part in rel.parts):
        return {"success": False, "error": "relative_path must not contain '..'."}
    is_root_artifact = len(rel.parts) == 1
    if is_root_artifact and rel.name not in ALLOWED_ARTIFACT_NAMES:
        return {"success": False, "error": f"'{rel.name}' is not a recognised root-level artifact. Allowed: {', '.join(sorted(ALLOWED_ARTIFACT_NAMES))}. Input documents must go under inputs/."}
    target = (case_dir / rel).resolve()
    try:
        target.relative_to(case_dir)
    except ValueError:
        return {"success": False, "error": "resolved path escapes the case_folder."}
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return {"success": True, "path": str(target), "file_size_bytes": target.stat().st_size, "relative_path": rel.as_posix()}


if __name__ == "__main__":
    mcp.run()
