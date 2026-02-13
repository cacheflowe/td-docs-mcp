# VS Code + GitHub Copilot Setup

VS Code natively supports MCP servers through GitHub Copilot. This guide covers configuring TD-MCP for use in VS Code.

## Configuration

Create a `.vscode/mcp.json` file in your project root:

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

Replace `/path/to/td-mcp` with the actual path to your cloned td-mcp repository.

### Windows Example

```json
{
  "servers": {
    "td-mcp": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "C:\\Users\\you\\projects\\td-mcp", "run", "td-mcp"]
    }
  }
}
```

### Custom Docs Directory

If your documentation is in a non-default location, pass the path via an environment variable:

```json
{
  "servers": {
    "td-mcp": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "/path/to/td-mcp", "run", "td-mcp"],
      "env": {
        "TD_MCP_DOCS_DIR": "/path/to/your/td_docs"
      }
    }
  }
}
```

## Using TD-MCP in Copilot Chat

Once configured, TD-MCP tools are available in Copilot's agent mode:

1. Open Copilot Chat in VS Code
2. Switch to **Agent** mode (if not already active)
3. Click the "Configure tools" button next to the model seletor. Find td-mcp in the list and refresh the tools. Once completed, it should list all available TD-MCP tools.
4. Ask TouchDesigner questions directly — Copilot will automatically invoke TD-MCP tools as needed. You may need to allow permissions for the tools to run on first use.
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

To make TD-MCP available across all VS Code projects (not just one workspace), use the **MCP: Open User Configuration** command from the VS Code command palette. This stores the server config globally rather than in a per-project `.vscode/mcp.json`.

## Additional Resources

- [VS Code MCP Server Documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- [MCP Specification](https://modelcontextprotocol.io)
