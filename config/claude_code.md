# Claude Code Configuration

This guide explains how to configure TD-MCP with Claude Code.

## Setup

1. First, ensure you've installed TD-MCP and crawled the documentation:
   ```bash
   cd /path/to/td-mcp
   uv sync
   uv run python -m td_mcp.crawler
   ```

2. Add the MCP server to your Claude Code configuration at `~/.claude.json`:

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

   Replace `/path/to/td-mcp` with the actual path to your td-mcp installation.

3. Restart Claude Code to load the new configuration.

## Verification

After restarting, verify the server is loaded:

1. Ask Claude: "What MCP tools do you have available?"
2. You should see `search_touchdesigner_docs`, `read_operator_doc`, `list_categories`, and `get_python_class`

## Example Usage

Try these prompts to verify everything works:

- "Search the TouchDesigner docs for Noise TOP"
- "How do I use Python to change a parameter in TouchDesigner?"
- "What's the difference between .par.value and .eval() in TouchDesigner?"

## Optional: Custom Docs Path

If your documentation is in a non-standard location, set the environment variable:

```json
{
  "mcpServers": {
    "td-mcp": {
      "command": "uv",
      "args": ["--directory", "/path/to/td-mcp", "run", "td-mcp"],
      "env": {
        "TD_MCP_DOCS_DIR": "/custom/path/to/td_docs"
      }
    }
  }
}
```

## Troubleshooting

### Server not appearing

- Check that the path in `--directory` is correct
- Ensure `uv` is in your PATH
- Try running `uv --directory /path/to/td-mcp run td-mcp` manually to see any errors

### No search results

- Make sure you ran the crawler: `uv run python -m td_mcp.crawler`
- Check that `td_docs/` folder exists and contains markdown files

### Permission errors

- On macOS/Linux, ensure the script has execute permissions
- Check file permissions on the td_docs folder
