# Cursor / Windsurf Configuration

This guide explains how to configure TD-MCP with Cursor and Windsurf editors.

## Cursor Setup

Cursor has experimental MCP support. Configuration may vary by version.

### Method 1: Project-level configuration

Create a `.cursor/mcp.json` file in your project root:

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

### Method 2: Global configuration

Check Cursor's settings for MCP server configuration options. The location varies by operating system and Cursor version.

## Windsurf Setup

Windsurf uses a similar configuration approach:

1. Open Windsurf Settings
2. Navigate to the MCP or Extensions section
3. Add the TD-MCP server configuration:

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

## Prerequisites

Before configuring either editor:

1. Install TD-MCP:
   ```bash
   cd /path/to/td-mcp
   uv sync
   ```

2. Crawl the documentation:
   ```bash
   uv run python -m td_mcp.crawler
   ```

3. Ensure `uv` is in your system PATH

## Verification

After configuration:

1. Restart the editor
2. Open a TouchDesigner-related project or Python file
3. Ask the AI assistant about TouchDesigner (e.g., "How do I use a Noise TOP?")
4. The assistant should use the TD-MCP tools to search documentation

## Using the Skills File

For better context, you can also point the editor to the skills file:

1. Add `skills/TD_SKILLS.md` to your project
2. Reference it in AI prompts: "Using the TD skills guide, help me with..."

Or configure it as a context file in your editor's AI settings.

## Troubleshooting

### MCP features not available

- MCP support in Cursor/Windsurf may be experimental
- Check for updates to the editor
- Consult the editor's documentation for current MCP configuration options

### Path issues on Windows

Use forward slashes in paths:
```json
"args": ["--directory", "C:/Users/you/td-mcp", "run", "td-mcp"]
```

### uv not found

Specify the full path to uv:
```json
"command": "/full/path/to/uv"
```
