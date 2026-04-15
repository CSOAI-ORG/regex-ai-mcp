# Regex Ai

> By [MEOK AI Labs](https://meok.ai) — MEOK AI Labs MCP Server

Regex AI MCP Server — Regular expression helper tools.

## Installation

```bash
pip install regex-ai-mcp
```

## Usage

```bash
# Run standalone
python server.py

# Or via MCP
mcp install regex-ai-mcp
```

## Tools

### `build_regex`
Build common regex patterns. Types: email, url, phone, ipv4, date_iso, hex_color, credit_card, ssn, zip_us, uuid. Or describe a custom pattern.

**Parameters:**
- `pattern_type` (str)
- `custom_options` (str)

### `test_regex`
Test a regex pattern against a string. Flags: i(gnorecase), m(ultiline), s(dotall).

**Parameters:**
- `pattern` (str)
- `test_string` (str)
- `flags` (str)

### `explain_regex`
Explain a regex pattern in plain English.

**Parameters:**
- `pattern` (str)

### `extract_matches`
Extract all matches of a pattern from text. group=0 for full match, 1+ for capture groups.

**Parameters:**
- `pattern` (str)
- `text` (str)
- `group` (int)


## Authentication

Free tier: 15 calls/day. Upgrade at [meok.ai/pricing](https://meok.ai/pricing) for unlimited access.

## Links

- **Website**: [meok.ai](https://meok.ai)
- **GitHub**: [CSOAI-ORG/regex-ai-mcp](https://github.com/CSOAI-ORG/regex-ai-mcp)
- **PyPI**: [pypi.org/project/regex-ai-mcp](https://pypi.org/project/regex-ai-mcp/)

## License

MIT — MEOK AI Labs
