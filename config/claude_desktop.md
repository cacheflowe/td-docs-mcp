# Claude Desktop Configuration

This guide explains how to configure TD-DOCS-MCP with Claude Desktop.

## Setup

1. First, ensure you've installed TD-DOCS-MCP and crawled the documentation:
   ```bash
   cd /path/to/td-docs-mcp
   uv sync
   uv run python -m td_docs_mcp.crawler
   ```

2. Locate your Claude Desktop configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

3. Add the MCP server configuration:

   ```json
   {
     "mcpServers": {
       "td-docs-mcp": {
         "command": "uv",
         "args": ["--directory", "/path/to/td-docs-mcp", "run", "td-docs-mcp"]
       }
     }
   }
   ```

   Replace `/path/to/td-docs-mcp` with the actual path to your td-docs-mcp installation.

   **Windows users**: Use forward slashes or escaped backslashes:
   ```json
   {
     "mcpServers": {
       "td-docs-mcp": {
         "command": "uv",
         "args": ["--directory", "C:/Users/you/td-docs-mcp", "run", "td-docs-mcp"]
       }
     }
   }
   ```

4. Restart Claude Desktop to load the new configuration.

## Verification

1. Open Claude Desktop
2. Start a new conversation
3. Look for the MCP tools indicator or ask: "What tools do you have access to?"
4. You should see TouchDesigner documentation tools available

## Example Prompts

Test the integration with these prompts:

- "Search TouchDesigner docs for Movie File In TOP"
- "Show me the Python documentation for the OP class"
- "List all TouchDesigner documentation categories"

## Windows-Specific Notes

On Windows, you may need to:

1. Ensure `uv` is installed and in your PATH
2. Use the full path to `uv.exe` if it's not in PATH:
   ```json
   {
     "mcpServers": {
       "td-docs-mcp": {
         "command": "C:/Users/you/.cargo/bin/uv.exe",
         "args": ["--directory", "C:/Users/you/td-docs-mcp", "run", "td-docs-mcp"]
       }
     }
   }
   ```

## Troubleshooting

### Configuration file doesn't exist

Create the configuration directory and file:

**macOS**:
```bash
mkdir -p ~/Library/Application\ Support/Claude
echo '{"mcpServers":{}}' > ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Windows** (PowerShell):
```powershell
New-Item -ItemType Directory -Force -Path "$env:APPDATA\Claude"
'{"mcpServers":{}}' | Out-File "$env:APPDATA\Claude\claude_desktop_config.json" -Encoding UTF8
```

### Tools not appearing

1. Check Claude Desktop logs for errors
2. Verify the path is correct and td-docs-mcp is properly installed
3. Test the server manually: `uv --directory /path/to/td-docs-mcp run td-docs-mcp`
