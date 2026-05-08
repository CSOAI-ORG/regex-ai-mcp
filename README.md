<div align="center">

# Regex Ai MCP

**Regex AI MCP Server — Regular expression helper tools.**

[![PyPI](https://img.shields.io/pypi/v/meok-regex-ai-mcp)](https://pypi.org/project/meok-regex-ai-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-MCP_Server-purple)](https://meok.ai)

</div>

## Overview

Regex AI MCP Server — Regular expression helper tools.

## Tools

| Tool | Description |
|------|-------------|
| `build_regex` | Build common regex patterns. Types: email, url, phone, ipv4, date_iso, hex_color |
| `test_regex` | Test a regex pattern against a string. Flags: i(gnorecase), m(ultiline), s(dotal |
| `explain_regex` | Explain a regex pattern in plain English. |
| `extract_matches` | Extract all matches of a pattern from text. group=0 for full match, 1+ for captu |

## Installation

```bash
pip install meok-regex-ai-mcp
```

## Usage with Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "regex-ai": {
      "command": "python",
      "args": ["-m", "meok_regex_ai_mcp.server"]
    }
  }
}
```

## Usage with FastMCP

```python
from mcp.server.fastmcp import FastMCP

# This server exposes 4 tool(s) via MCP
# See server.py for full implementation
```

## License

MIT © [MEOK AI Labs](https://meok.ai)
