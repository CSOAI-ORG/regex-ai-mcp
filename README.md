# regex-ai-mcp

MCP server for regular expression helper tools.

## Tools

- **build_regex** — Build common regex patterns (email, URL, phone, etc.)
- **test_regex** — Test patterns against strings with flag support
- **explain_regex** — Explain regex patterns in plain English
- **extract_matches** — Extract all pattern matches from text

## Usage

```bash
pip install mcp
python server.py
```

## Rate Limits

50 calls/day per tool (free tier).
