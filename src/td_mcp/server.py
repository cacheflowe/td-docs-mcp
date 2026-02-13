"""
TD-MCP Server

MCP server that provides TouchDesigner documentation to AI coding assistants.
Implements tools for searching and retrieving documentation.
"""

import asyncio
import os
import re
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from thefuzz import fuzz, process

# Maximum content length to return (to stay within context limits)
MAX_CONTENT_LENGTH = 30000

# Fuzzy match threshold (0-100)
FUZZY_THRESHOLD = 50

# Default docs directory (relative to project root)
DEFAULT_DOCS_DIR = Path(__file__).parent.parent.parent / "td_docs"


def get_docs_dir() -> Path:
    """Get the documentation directory path."""
    # Check environment variable first
    env_path = os.environ.get("TD_MCP_DOCS_DIR")
    if env_path:
        return Path(env_path)
    return DEFAULT_DOCS_DIR


def list_all_docs() -> list[tuple[str, Path]]:
    """List all documentation files with their category."""
    docs_dir = get_docs_dir()
    docs = []

    if not docs_dir.exists():
        return docs

    for category_dir in docs_dir.iterdir():
        if category_dir.is_dir():
            category = category_dir.name
            for doc_file in category_dir.glob("*.md"):
                docs.append((category, doc_file))

    return docs


def extract_title(file_path: Path) -> str:
    """Extract the title from a markdown file's frontmatter or filename."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(500)  # Read just the beginning

        # Try to extract from frontmatter
        if content.startswith('---'):
            match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
            if match:
                return match.group(1).strip()

        # Fall back to filename
        return file_path.stem.replace('_', ' ')
    except Exception:
        return file_path.stem.replace('_', ' ')


def search_docs(query: str, limit: int = 10) -> list[dict]:
    """
    Search documentation using fuzzy matching.

    Returns a list of matches with scores.
    """
    docs = list_all_docs()

    if not docs:
        return []

    # Build a list of (searchable_text, (category, path)) tuples
    searchable = []
    for category, path in docs:
        title = extract_title(path)
        # Create searchable text combining title and category
        search_text = f"{title} {category}"
        searchable.append((search_text, (category, path, title)))

    # Use thefuzz to find best matches
    results = []
    for search_text, (category, path, title) in searchable:
        # Calculate multiple fuzzy scores
        partial_score = fuzz.partial_ratio(query.lower(), search_text.lower())
        token_score = fuzz.token_set_ratio(query.lower(), search_text.lower())
        # Use the best score
        score = max(partial_score, token_score)

        if score >= FUZZY_THRESHOLD:
            results.append({
                "title": title,
                "category": category,
                "path": str(path.relative_to(get_docs_dir())),
                "score": score
            })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:limit]


def read_doc(relative_path: str) -> str | None:
    """
    Read a documentation file by relative path.

    Returns the content or None if not found.
    Includes path traversal protection.
    """
    docs_dir = get_docs_dir()

    # Security: Resolve the path and ensure it's within docs_dir
    try:
        requested_path = (docs_dir / relative_path).resolve()

        # Check that the resolved path is within docs_dir
        if not str(requested_path).startswith(str(docs_dir.resolve())):
            return None

        if not requested_path.exists() or not requested_path.is_file():
            return None

        with open(requested_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Truncate if too long
        if len(content) > MAX_CONTENT_LENGTH:
            content = content[:MAX_CONTENT_LENGTH]
            content += f"\n\n[Content truncated at {MAX_CONTENT_LENGTH} characters]"

        return content

    except Exception:
        return None


def list_categories() -> list[dict]:
    """List all available documentation categories."""
    docs_dir = get_docs_dir()
    categories = []

    if not docs_dir.exists():
        return categories

    for category_dir in docs_dir.iterdir():
        if category_dir.is_dir():
            doc_count = len(list(category_dir.glob("*.md")))
            if doc_count > 0:
                categories.append({
                    "name": category_dir.name,
                    "doc_count": doc_count
                })

    return sorted(categories, key=lambda x: x["name"])


def get_python_class(class_name: str) -> str | None:
    """
    Get Python class documentation by class name.

    Searches in the Python documentation directories.
    """
    docs_dir = get_docs_dir()

    # Search patterns for Python classes
    patterns = [
        f"{class_name}_Class.md",
        f"{class_name}.md",
        f"td.{class_name}.md",
    ]

    # Search in Python directories
    python_dirs = ["Python", "Python_Experimental"]

    for python_dir in python_dirs:
        dir_path = docs_dir / python_dir
        if not dir_path.exists():
            continue

        for pattern in patterns:
            file_path = dir_path / pattern
            if file_path.exists():
                return read_doc(str(file_path.relative_to(docs_dir)))

        # Also try fuzzy matching within Python docs
        for doc_file in dir_path.glob("*.md"):
            if class_name.lower() in doc_file.stem.lower():
                return read_doc(str(doc_file.relative_to(docs_dir)))

    return None


# Create the MCP server
server = Server("td-mcp")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="search_touchdesigner_docs",
            description=(
                "Search TouchDesigner documentation using fuzzy matching. "
                "Returns a list of matching documents with relevance scores. "
                "Use this to find documentation about operators, Python classes, "
                "or any TouchDesigner concept."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query (e.g., 'Noise TOP', 'moviefileinTOP', 'Python OP class')"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 10)",
                        "default": 10
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="read_operator_doc",
            description=(
                "Read a specific TouchDesigner documentation file by path. "
                "Use the path returned from search_touchdesigner_docs."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Relative path to the documentation file (e.g., 'TOPs/Noise_TOP.md')"
                    }
                },
                "required": ["path"]
            }
        ),
        Tool(
            name="list_categories",
            description=(
                "List all available TouchDesigner documentation categories "
                "with the number of documents in each. Categories include "
                "TOPs, CHOPs, DATs, SOPs, MATs, COMPs, and Python."
            ),
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_python_class",
            description=(
                "Get documentation for a specific TouchDesigner Python class. "
                "This is a shortcut for finding Python API documentation. "
                "Examples: 'OP', 'TOP', 'CHOP', 'Par', 'Cell', 'Matrix', 'Position'"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "class_name": {
                        "type": "string",
                        "description": "Name of the Python class (e.g., 'OP', 'TOP', 'moviefileinTOP')"
                    }
                },
                "required": ["class_name"]
            }
        ),
        Tool(
            name="help",
            description=(
                "Show a summary of all available TD-MCP tools with usage examples."
            ),
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
    ]


HELP_TEXT = """\
TD-MCP — TouchDesigner Documentation Server

Available tools:

1. search_touchdesigner_docs(query, limit?)
   Fuzzy search across all documentation.
   Examples:
     query: "Noise TOP"
     query: "moviefileinTOP"
     query: "Python OP class"

2. read_operator_doc(path)
   Read a specific doc file by its relative path (from search results).
   Example:
     path: "TOPs/Noise_TOP.md"

3. list_categories()
   List all documentation categories with document counts.

4. get_python_class(class_name)
   Quick lookup for a Python class doc.
   Examples:
     class_name: "OP"
     class_name: "TOP"
     class_name: "moviefileinTOP"

5. help()
   Show this message.

Typical workflow:
  1. search_touchdesigner_docs to find relevant docs
  2. read_operator_doc to read the full content
  3. get_python_class for quick Python API lookups
"""


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""

    if name == "search_touchdesigner_docs":
        query = arguments.get("query", "")
        limit = arguments.get("limit", 10)

        results = search_docs(query, limit)

        if not results:
            return [TextContent(
                type="text",
                text=f"No documentation found matching '{query}'. "
                     "Try a different search term or check if documentation has been crawled."
            )]

        # Format results
        output_lines = [f"Found {len(results)} results for '{query}':\n"]
        for i, result in enumerate(results, 1):
            output_lines.append(
                f"{i}. [{result['category']}] {result['title']} "
                f"(score: {result['score']}) - path: {result['path']}"
            )

        return [TextContent(type="text", text="\n".join(output_lines))]

    elif name == "read_operator_doc":
        path = arguments.get("path", "")

        content = read_doc(path)

        if content is None:
            return [TextContent(
                type="text",
                text=f"Documentation file not found: {path}"
            )]

        return [TextContent(type="text", text=content)]

    elif name == "list_categories":
        categories = list_categories()

        if not categories:
            return [TextContent(
                type="text",
                text="No documentation categories found. "
                     "Run the crawler first: python -m td_mcp.crawler"
            )]

        output_lines = ["Available TouchDesigner documentation categories:\n"]
        for cat in categories:
            output_lines.append(f"- {cat['name']}: {cat['doc_count']} documents")

        return [TextContent(type="text", text="\n".join(output_lines))]

    elif name == "get_python_class":
        class_name = arguments.get("class_name", "")

        content = get_python_class(class_name)

        if content is None:
            return [TextContent(
                type="text",
                text=f"Python class documentation not found for: {class_name}. "
                     f"Try searching with search_touchdesigner_docs instead."
            )]

        return [TextContent(type="text", text=content)]

    elif name == "help":
        return [TextContent(type="text", text=HELP_TEXT)]

    else:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]


def main():
    """Main entry point for the MCP server."""
    async def run():
        async with stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                server.create_initialization_options()
            )

    asyncio.run(run())


if __name__ == "__main__":
    main()
