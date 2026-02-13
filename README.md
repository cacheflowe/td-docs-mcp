# TD-MCP

An MCP (Model Context Protocol) server that provides TouchDesigner documentation to AI coding assistants. This enables better Python scripting suggestions and UI recommendations for TouchDesigner projects.

## Features

- **Full Documentation Access**: Scraped documentation from docs.derivative.ca including all operator types (TOPs, CHOPs, DATs, SOPs, MATs, COMPs), Python base classes, and operator-specific Python classes (e.g., `BlurTOP_Class`, `ScriptCHOP_Class`)
- **Fuzzy Search**: Find relevant documentation even with imprecise queries
- **Python Class Lookup**: Quick access to TouchDesigner Python API documentation
- **MCP Integration**: Works with Claude Code, Claude Desktop, VS Code + Copilot, Cursor, and other MCP-compatible tools

## Using MCP effectively with VS Code + Copilot

The MCP tools are reactive — Copilot calls them when it thinks they're relevant. To get the most out of them:

- Be explicit in your prompts about TouchDesigner context. Instead of "how do I blur an image", say "I'm working in a TouchDesigner DAT execute script and need to change the size parameter on a Blur TOP via Python." This triggers Copilot to search the docs rather than hallucinate.
- Ask it to look things up before writing code. Something like "Look up the Blur TOP parameters and its Python class, then write a script that..." forces two MCP calls before any code generation.
- Key use cases where the docs prevent hallucination:
  - Parameter names — TD parameters have specific identifiers (moviefilein1.par.file not .filename). The docs have every ParamName `identifier` listed.
  - Python class methods — knowing what's on scriptCHOP_Class vs CHOP_Class vs OP_Class prevents invented method names
  - Callback signatures — DAT execute, CHOP execute, Panel execute all have specific callback signatures that AI tools frequently get wrong
  - Node wiring — which operators accept which inputs, and how many, is documented in "Operator Inputs/Outputs" sections
  - Cooking behavior — when things cook, time slicing, etc. — stuff AI models confidently fabricate

## Quick Start

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended) or pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/td-mcp.git
   cd td-mcp
   ```

2. Install dependencies with uv:
   ```bash
   uv sync
   ```

3. Crawl the TouchDesigner documentation:
   ```bash
   uv run python -m td_mcp.crawler
   ```
   This creates a `td_docs/` folder with all documentation as markdown files.

4. Configure your MCP client (see [Configuration](#configuration) below)

## Configuration

### Claude Code

Add to `~/.claude.json`:

```json
{
  "mcpServers": {
    "td-mcp": {
      "command": "uv",
      "args": ["--directory", "/path/to/td-mcp", "run", "td-mcp"]
    }
  }
}
```

### Claude Desktop

Add to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "td-mcp": {
      "command": "uv",
      "args": ["--directory", "/path/to/td-mcp", "run", "td-mcp"]
    }
  }
}
```

### Cursor / Windsurf

See [config/cursor.md](config/cursor.md) for Cursor and Windsurf configuration.

### VS Code with GitHub Copilot

VS Code natively supports MCP servers. Create `.vscode/mcp.json` in your project:

```json
{
  "servers": {
    "td-mcp": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "/path/to/td-mcp", "run", "td-mcp"]
    }
  }
}
```

See [config/vscode_copilot.md](config/vscode_copilot.md) for detailed setup including Windows paths, environment variables, and usage tips.

## Usage

Once configured, your AI assistant will have access to these tools:

### search_touchdesigner_docs

Search across all TouchDesigner documentation:

```
"How do I use a Noise TOP?"
"What parameters does Movie File In have?"
"Python OP class methods"
```

### read_operator_doc

Read specific documentation files (usually after a search):

```
"Read the full documentation for TOPs/Noise_TOP.md"
```

### list_categories

List available documentation categories:

```
"What TouchDesigner documentation categories are available?"
```

### get_python_class

Quick lookup for Python class documentation:

```
"Show me the TOP Python class documentation"
"What methods does the OP class have?"
```

## Example Queries

Here are some example queries your AI assistant can now handle better:

1. **Basic operator usage**:
   > "How do I create a noise pattern with a Noise TOP?"

2. **Python scripting**:
   > "How do I change parameters with Python in TouchDesigner?"

3. **Complex tasks**:
   > "I am working with a Movie File In TOP. I need to do two things using Python:
   > 1. Script a change to the 'file' parameter to load a new video.
   > 2. Get the actual width and height of the loaded video in pixels.
   > How do I write this code?"

## Crawler Options

The crawler runs in three stages:

1. **Operator categories** — crawls index pages for TOPs, CHOPs, DATs, SOPs, POPs, MATs, and COMPs
2. **Python reference** — crawls base classes (OP_Class, TOP_Class, etc.) from the TouchDesigner_Python_Classes index
3. **Operator Python classes** — scans saved operator docs for links to operator-specific class pages (e.g., `BlurTOP_Class`, `ScriptCHOP_Class`) and crawls each into its matching category directory alongside the operator doc that references it

All stages have resume capability — files already on disk are skipped automatically.

```bash
# Crawl all documentation (all three stages)
uv run python -m td_mcp.crawler

# Crawl specific categories only
uv run python -m td_mcp.crawler -c TOPs CHOPs Python

# Limit pages per category/stage (for testing)
uv run python -m td_mcp.crawler --limit 5

# Only crawl operator Python class pages (stage 3 only, requires existing operator docs)
uv run python -m td_mcp.crawler --classes-only

# Skip the operator Python class crawl (stages 1 & 2 only)
uv run python -m td_mcp.crawler --skip-classes

# Re-crawl pages that previously returned 403/error content
uv run python -m td_mcp.crawler --retry-failed

# Custom output directory
uv run python -m td_mcp.crawler -o /path/to/docs
```

## Markdown Cleaner

After every crawl (full, single-category, `--classes-only`, or `--retry-failed`), run the cleaner to post-process the raw Crawl4AI markdown output:

```bash
# Clean all docs
uv run python -m td_mcp.cleaner

# Clean a single file
uv run python -m td_mcp.cleaner -f td_docs/TOPs/Blur_TOP.md

# Preview changes without writing (dry run)
uv run python -m td_mcp.cleaner --dry-run
```

The cleaner applies these fixes:

- Removes wiki artifacts (`From Derivative`, `[edit]` links, `Jump to navigation`, empty headers)
- Strips the `## Contents` TOC section
- Fixes section headers that lost their `##` prefix during conversion
- Converts same-page absolute anchor links to relative `#fragment` links for local markdown navigation
- Cleans up blockquote formatting in Python class docs
- Removes the redundant operator family footer (link lists and glossary)
- Formats parameter lines as proper markdown bullet lists
- Relocates general wiki pages (glossary, tutorials, etc.) into a shared `General/` directory
- Contracts excessive blank lines and trims trailing whitespace

## Testing

### Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector uv --directory . run td-mcp
```

### Run unit tests

```bash
uv run pytest
```

## Project Structure

```
td-mcp/
├── pyproject.toml              # Project configuration
├── README.md                   # This file
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
├── src/
│   └── td_mcp/
│       ├── __init__.py
│       ├── server.py           # MCP server implementation
│       ├── crawler.py          # Documentation scraper
│       └── cleaner.py          # Post-crawl markdown cleanup
├── td_docs/                    # Scraped docs (gitignored)
├── skills/
│   └── TD_SKILLS.md            # Best practices context
└── config/
    ├── claude_code.md          # Claude Code setup
    ├── claude_desktop.md       # Claude Desktop setup
    ├── cursor.md               # Cursor/Windsurf setup
    └── vscode_copilot.md       # VS Code notes
```

## Environment Variables

- `TD_MCP_DOCS_DIR`: Custom path to documentation directory (defaults to `td_docs/` in project root)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- [TouchDesigner](https://derivative.ca) by Derivative
- [Model Context Protocol](https://modelcontextprotocol.io) by Anthropic
- [Crawl4AI](https://github.com/unclecode/crawl4ai) for web scraping
