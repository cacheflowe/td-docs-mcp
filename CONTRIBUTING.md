# Contributing to TD-MCP

Thank you for your interest in contributing to TD-MCP! This document provides guidelines and information for contributors.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/td-mcp.git
   cd td-mcp
   ```
3. Install development dependencies:
   ```bash
   uv sync --dev
   ```

## Development Setup

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- A local copy of TouchDesigner documentation (run the crawler)

### Running the Crawler

```bash
# Full crawl
uv run python -m td_mcp.crawler

# Quick test (limit pages)
uv run python -m td_mcp.crawler --limit 5
```

### Testing the MCP Server

```bash
# With MCP Inspector
npx @modelcontextprotocol/inspector uv --directory . run td-mcp

# Unit tests
uv run pytest
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints where practical
- Keep functions focused and well-documented
- Write docstrings for public functions and classes

## Making Changes

### Branching

- Create a feature branch from `main`:
  ```bash
  git checkout -b feature/your-feature-name
  ```

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove, etc.)
- Keep the first line under 72 characters

Examples:
```
Add fuzzy search for operator documentation
Fix path traversal vulnerability in read_doc
Update crawler to handle rate limiting
```

### Pull Requests

1. Ensure your code passes all tests
2. Update documentation if needed
3. Create a pull request with a clear description
4. Link any related issues

## Areas for Contribution

### High Priority

- **Crawler improvements**: Better parsing, more robust error handling
- **Search quality**: Improved fuzzy matching algorithms
- **Documentation**: Better examples, tutorials, troubleshooting guides

### Nice to Have

- **Caching**: Implement caching for frequently accessed docs
- **Indexing**: Pre-build search index for faster queries
- **Additional tools**: New MCP tools for specific TouchDesigner tasks

### Documentation

- Fix typos or unclear explanations
- Add examples for common use cases
- Improve configuration guides for different platforms

## Testing

### Running Tests

```bash
uv run pytest
```

### Writing Tests

- Add tests for new features
- Place tests in a `tests/` directory
- Use pytest fixtures for common setup

## Reporting Issues

When reporting bugs:

1. Check existing issues first
2. Include your environment (OS, Python version, TD-MCP version)
3. Provide steps to reproduce
4. Include error messages and logs

## Questions?

- Open an issue for questions about the codebase
- Check existing documentation first
- Be patient - maintainers may have limited time

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
