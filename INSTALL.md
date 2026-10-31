# Installing arya-ai

Pick the route that matches how you use Claude. The plugin route gives you everything: skills, commands, specialist agents and the drafting tools. The Desktop extension gives you the drafting and research tools inside a normal Claude chat.

## Before you start (once per computer)

arya-ai's tools run on your own computer. They need two free programs:

**Mac** (open Terminal and paste each line):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
brew install pandoc
```

No Homebrew? Download pandoc from https://pandoc.org/installing.html instead.

**Windows** (open PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then install pandoc from https://pandoc.org/installing.html.

Close and reopen Claude after installing these.

## Option 1: Claude Code or the Claude desktop app's Code tab (recommended)

In a Claude Code session, type:

```text
/plugin marketplace add edenbuilds/arya-ai
```

```text
/plugin install arya-ai@arya-ai
```

Restart the session. To check it worked, ask: *"What can arya-ai do?"* It should list the skills and the drafting tools.

To update later:

```text
/plugin marketplace update arya-ai
```

## Option 2: Claude Desktop extension (tools inside a normal chat)

1. Download `arya-ai-<version>.mcpb` from https://github.com/edenbuilds/arya-ai/releases/latest
2. Double-click it. Claude Desktop opens the install screen. Click **Install**.
3. Open a new chat and ask: *"Use arya-ai to list the Maharashtra forums."*

To update, download the newer `.mcpb` and install it the same way.

## Option 3: Codex, Cursor, Gemini or any MCP client

```bash
git clone https://github.com/edenbuilds/arya-ai.git
```

- **Codex:** use the folder as a local plugin (`.codex-plugin/plugin.json`).
- **Cursor:** open the folder. The rules in `.cursor/rules/` load on their own.
- **Gemini CLI:** start from `GEMINI.md`.
- **Any MCP client:** add this server, using the folder's full path:

```json
{
  "mcpServers": {
    "arya-ai": {
      "command": "uv",
      "args": ["--directory", "/full/path/to/arya-ai", "run", "server/main.py"]
    }
  }
}
```

## Where your drafts go

Each drafting job gets its own folder under `Downloads/arya-ai-Drafts/` on your computer. The folder holds the case facts, each draft version, the verification report and the final `.docx`. Nothing is uploaded anywhere by these tools.

## First use

Start with what you need in plain words, for example *"ABA before the Nagpur Bench, FIR from Chandrapur under BNS 118"*. arya-ai asks you its questions first and waits for your answers before it drafts anything.

## If something does not work

- **"uv not found" or the tools do not appear:** install uv as shown above, then quit and reopen Claude fully.
- **No `.docx` produced:** pandoc is missing. Install it, then ask again for the DOCX.
- **Plugin not found:** check that the first command was typed exactly as `/plugin marketplace add edenbuilds/arya-ai`.

Every draft is a starting point for the advocate. Verify citations, sections, fees and limitation against primary sources before filing.
