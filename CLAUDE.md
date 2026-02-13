# TD-MCP Project Instructions

## Overview

TD-MCP is an MCP (Model Context Protocol) server that provides AI assistants with searchable access to TouchDesigner documentation. The docs are scraped from `docs.derivative.ca`, converted to markdown, cleaned up, and served via MCP tools.

## Project Structure

```
src/td_mcp/
  crawler.py    # Scrapes docs.derivative.ca -> raw markdown files
  cleaner.py    # Post-processes markdown for quality and consistency
  server.py     # MCP server exposing search and read tools
td_docs/        # Generated markdown output (not hand-edited)
  CHOPs/  TOPs/  SOPs/  DATs/  POPs/  MATs/  COMPs/  Python/  General/
```

## Documentation Pipeline

### Step 1: Crawl (`crawler.py`)

Uses **Crawl4AI** (headless browser) to fetch pages from `docs.derivative.ca` and convert HTML to markdown via Crawl4AI's built-in converter.

```bash
python -m src.td_mcp.crawler                     # Full crawl
python -m src.td_mcp.crawler -c TOPs CHOPs       # Specific categories
python -m src.td_mcp.crawler --retry-failed       # Re-crawl 403/error pages
```

**Key behaviors:**
- Fetches category index pages, extracts operator links, crawls each one
- Adds YAML frontmatter (url, category, title) to each file
- Resume capability: skips files that already exist on disk
- Retry with exponential backoff (5s/10s/20s) for 403s and empty responses
- General/meta pages (glossary, tutorials, etc.) are redirected to `General/` directory
- Rate limited at 0.5s between requests

### Step 2: Clean (`cleaner.py`)

Post-processes the raw Crawl4AI markdown output to fix formatting issues.

```bash
python -m src.td_mcp.cleaner                     # Clean all docs
python -m src.td_mcp.cleaner -f path/to/file.md  # Clean single file
python -m src.td_mcp.cleaner --dry-run            # Preview changes
```

**Processing order within `clean_td_markdown()`:**
1. Line-by-line pass (frontmatter preservation, junk removal, header fixing)
2. Python-specific blockquote cleaning (for `_Class.md` files)
3. Operator family footer removal
4. Parameter bullet formatting
5. Blank line contraction (max 2 consecutive)
6. Trailing whitespace removal

## Cleaning Rules Reference

Rules are applied in the order listed. When adding new rules, consider where in the pipeline they should run.

### Line-by-line rules (main loop in `clean_td_markdown`)

| Rule | What it does |
|------|-------------|
| **Remove "From Derivative"** | Drops the wiki byline |
| **Remove wikieditor lines** | Drops MediaWiki editor metadata |
| **Remove "Jump to" links** | Drops navigation/search jump links |
| **Remove `[edit]` links** | Strips `[[edit](...)]` and standalone edit links |
| **Remove empty `##` headers** | Drops bare `##` lines (MediaWiki artifact) |
| **Strip `>>` double blockquote** | Strips `>> ` prefix from any line starting with `>>` — double-blockquote formatting artifact |
| **Skip Contents/TOC section** | Removes `## Contents` and the indented numbered list below it |
| **Remove PythonIcon image links** | Strips `[![PythonIcon.png](...)](...)` markup |
| **Fix missing section headers** | Detects plain-text lines matching known header patterns (Summary, Parameters, Operator Inputs, etc.) and adds `## ` prefix |

### Post-processing rules (separate functions)

| Rule | Function | What it does |
|------|----------|-------------|
| **Python blockquote cleanup** | `clean_python_blockquotes()` | Removes `> ` prefix from description lines in Python class docs; preserves code blocks; adds spacing before member definitions |
| **Self-anchor link conversion** | `convert_self_anchor_links()` | Converts absolute anchor links that point to the same page (matched via frontmatter `title`) to relative `#fragment` links so TOC entries and self-references work in local markdown viewers |
| **Blockquote spacing** | `ensure_blockquote_spacing()` | Ensures blank lines before and after `>` blockquote lines (or blocks of consecutive `>` lines) for proper markdown rendering. Skips code-fenced regions |
| **Operator family footer removal** | `remove_operator_family_footer()` | Detects a bare family name line (CHOPs/TOPs/etc.) followed by `---`, and truncates everything from there to EOF. Removes the redundant link list and glossary definitions |
| **Page footer removal** | `remove_page_footer()` | Keeps `__setstate__()` and its description line, discards all glossary/boilerplate after. Falls back to truncating at "TouchDesigner Build" if no `__setstate__` is found |
| **Parameter bullet formatting** | `format_parameter_bullets()` | Inside `## Parameters` sections: prefixes top-level param lines matching `ParamName \`id\` - description` with `- `. Removes blank lines between consecutive sub-bullet (`* `) items for tight nested lists |

### File organization rules

| Rule | Where | What it does |
|------|-------|-------------|
| **General page relocation** | `relocate_general_files()` in cleaner, `crawl_page()` in crawler | Pages in `GENERAL_PAGE_FILENAMES` are saved to / moved to `General/` instead of per-category dirs. Duplicates are deleted. List is maintained in both `crawler.py` and `cleaner.py` (kept in sync manually) |

### Constants to keep in sync

The general page filename list exists in two places:
- `crawler.py`: `GENERAL_PAGE_FILENAMES` set (used during crawl)
- `cleaner.py`: `general_filenames` set inside `relocate_general_files()` (used during clean)

When adding/removing general pages, update both.

## Adding New Cleaning Rules

1. **Decide scope**: Does it apply to all files, only certain categories, or only within specific sections?
2. **Decide placement**: Line-by-line rules go in the main loop of `clean_td_markdown()`. Section-aware or multi-line rules should be separate functions called from the post-processing section.
3. **Pattern**: New functions should take `content: str` and return `content: str` for composability.
4. **Update this doc**: Add the rule to the appropriate table above.
5. **Test**: Run `python -m src.td_mcp.cleaner --dry-run` and spot-check affected files.

## Common Commands

```bash
# Full re-crawl of a category (delete dir first to force fresh crawl)
rm -rf td_docs/TOPs && python -m src.td_mcp.crawler -c TOPs

# Re-crawl only 403/failed pages
python -m src.td_mcp.crawler --retry-failed

# Clean all docs (also relocates general files)
python -m src.td_mcp.cleaner

# Run MCP server
uv run td-mcp
```
