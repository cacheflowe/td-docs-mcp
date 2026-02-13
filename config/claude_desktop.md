# Claude Desktop Configuration

This guide explains how to configure TD-MCP with Claude Desktop.

## Setup

1. First, ensure you've installed TD-MCP and crawled the documentation:
   ```bash
   cd /path/to/td-mcp
   uv sync
   uv run python -m td_mcp.crawler
   ```

2. Locate your Claude Desktop configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

3. Add the MCP server configuration:

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

   **Windows users**: Use forward slashes or escaped backslashes:
   ```json
   {
     "mcpServers": {
       "td-mcp": {
         "command": "uv",
         "args": ["--directory", "C:/Users/you/td-mcp", "run", "td-mcp"]
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
       "td-mcp": {
         "command": "C:/Users/you/.cargo/bin/uv.exe",
         "args": ["--directory", "C:/Users/you/td-mcp", "run", "td-mcp"]
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
2. Verify the path is correct and td-mcp is properly installed
3. Test the server manually: `uv --directory /path/to/td-mcp run td-mcp`
