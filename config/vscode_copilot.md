# VS Code + GitHub Copilot Setup

VS Code natively supports MCP servers through GitHub Copilot. This guide covers configuring TD-DOCS-MCP for use in VS Code.

## Configuration

Create a `.vscode/mcp.json` file in your project root:

```json
{
  "servers": {
    "td-docs-mcp": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "/path/to/td-docs-mcp", "run", "td-docs-mcp"]
    }
  }
}
```

Replace `/path/to/td-docs-mcp` with the actual path to your cloned td-docs-mcp repository.

### Windows Example

```json
{
  "servers": {
    "td-docs-mcp": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "C:\\Users\\you\\projects\\td-docs-mcp", "run", "td-docs-mcp"]
    }
  }
}
```

### Custom Docs Directory

If your documentation is in a non-default location, pass the path via an environment variable:

```json
{
  "servers": {
    "td-docs-mcp": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "/path/to/td-docs-mcp", "run", "td-docs-mcp"],
      "env": {
        "TD_DOCS_MCP_DOCS_DIR": "/path/to/your/td_docs"
      }
    }
  }
}
```

## Using TD-DOCS-MCP in Copilot Chat

Once configured, TD-DOCS-MCP tools are available in Copilot's agent mode:

1. Open Copilot Chat in VS Code
2. Switch to **Agent** mode (if not already active)
3. Click the "Configure tools" button next to the model seletor. Find td-docs-mcp in the list and refresh the tools. Once completed, it should list all available TD-DOCS-MCP tools.
4. Ask TouchDesigner questions directly — Copilot will automatically invoke TD-DOCS-MCP tools as needed. You may need to allow permissions for the tools to run on first use.
   1. `/search_touchdesigner_docs scriptCHOP` — Search for documentation related to `scriptCHOP`
      1. `/search_touchdesigner_docs scriptCHOP_class` — Search for documentation related to `scriptCHOP` python class
   2. `/read_operator_doc scriptCHOP` — Get the full documentation for `scriptCHOP`
   3. `/list_categories` — List all documentation categories available
   4. `/get_python_class tdu` — Look up the `tdu` Python class documentation

You can also reference specific tools by typing `#` followed by the tool name in the chat prompt.

### Available Tools

- `search_touchdesigner_docs` — Search across all TD documentation
- `read_operator_doc` — Read a specific operator's full documentation
- `list_categories` — List available documentation categories
- `get_python_class` — Look up Python class documentation

## Global Configuration

To make TD-DOCS-MCP available across all VS Code projects (not just one workspace), use the **MCP: Open User Configuration** command from the VS Code command palette. This stores the server config globally rather than in a per-project `.vscode/mcp.json`.

## Additional Resources

- [VS Code MCP Server Documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- [MCP Specification](https://modelcontextprotocol.io)
