"""Regex AI MCP Server — Regular expression helper tools."""

import sys, os
sys.path.insert(0, os.path.expanduser('~/clawd/meok-labs-engine/shared'))
from auth_middleware import check_access

import re
import time
from typing import Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("regex-ai", instructions="MEOK AI Labs MCP Server")
_calls: dict[str, list[float]] = {}
DAILY_LIMIT = 50

def _rate_check(tool: str) -> bool:
    now = time.time()
    _calls.setdefault(tool, [])
    _calls[tool] = [t for t in _calls[tool] if t > now - 86400]
    if len(_calls[tool]) >= DAILY_LIMIT:
        return False
    _calls[tool].append(now)
    return True

COMMON_PATTERNS = {
    "email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "url": r'https?://[^\s<>"{}|\\^`\[\]]+',
    "phone": r'[\+]?[(]?[0-9]{1,4}[)]?[-\s\./0-9]{7,15}',
    "ipv4": r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    "date_iso": r'\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])',
    "hex_color": r'#(?:[0-9a-fA-F]{3}){1,2}\b',
    "credit_card": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
    "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
    "zip_us": r'\b\d{5}(?:-\d{4})?\b',
    "uuid": r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
}

@mcp.tool()
def build_regex(pattern_type: str, custom_options: str = "", api_key: str = "") -> dict[str, Any]:
    """Build common regex patterns. Types: email, url, phone, ipv4, date_iso, hex_color, credit_card, ssn, zip_us, uuid. Or describe a custom pattern."""
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return {"error": msg, "upgrade_url": "https://meok.ai/pricing"}

    if not _rate_check("build_regex"):
        return {"error": "Rate limit exceeded (50/day)"}
    if pattern_type in COMMON_PATTERNS:
        pat = COMMON_PATTERNS[pattern_type]
        return {"pattern": pat, "type": pattern_type, "python": f"re.compile(r'{pat}')", "description": f"Matches {pattern_type} patterns"}
    suggestions = {k: v for k, v in COMMON_PATTERNS.items() if pattern_type.lower() in k}
    if suggestions:
        return {"suggestions": suggestions, "hint": "Use one of the suggested pattern types"}
    return {"available_types": list(COMMON_PATTERNS.keys()), "error": f"Unknown pattern type: {pattern_type}"}

@mcp.tool()
def test_regex(pattern: str, test_string: str, flags: str = "", api_key: str = "") -> dict[str, Any]:
    """Test a regex pattern against a string. Flags: i(gnorecase), m(ultiline), s(dotall)."""
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return {"error": msg, "upgrade_url": "https://meok.ai/pricing"}

    if not _rate_check("test_regex"):
        return {"error": "Rate limit exceeded (50/day)"}
    flag_map = {"i": re.IGNORECASE, "m": re.MULTILINE, "s": re.DOTALL}
    combined = 0
    for f in flags:
        if f in flag_map:
            combined |= flag_map[f]
    try:
        compiled = re.compile(pattern, combined)
    except re.error as e:
        return {"error": f"Invalid regex: {e}", "pattern": pattern}
    matches = []
    for m in compiled.finditer(test_string):
        match_info = {"match": m.group(), "start": m.start(), "end": m.end(), "groups": list(m.groups())}
        if m.groupdict():
            match_info["named_groups"] = m.groupdict()
        matches.append(match_info)
    return {"pattern": pattern, "test_string": test_string, "matches": matches, "match_count": len(matches), "is_match": len(matches) > 0}

@mcp.tool()
def explain_regex(pattern: str, api_key: str = "") -> dict[str, Any]:
    """Explain a regex pattern in plain English."""
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return {"error": msg, "upgrade_url": "https://meok.ai/pricing"}

    if not _rate_check("explain_regex"):
        return {"error": "Rate limit exceeded (50/day)"}
    explanations = []
    tokens = {
        r'\d': "digit (0-9)", r'\D': "non-digit", r'\w': "word character (a-z, A-Z, 0-9, _)",
        r'\W': "non-word character", r'\s': "whitespace", r'\S': "non-whitespace",
        r'\b': "word boundary", r'\B': "non-word boundary", '.': "any character",
        '^': "start of string/line", '$': "end of string/line",
        '*': "zero or more times", '+': "one or more times", '?': "zero or one time",
    }
    i = 0
    while i < len(pattern):
        matched = False
        for tok, desc in sorted(tokens.items(), key=lambda x: -len(x[0])):
            if pattern[i:i+len(tok)] == tok:
                explanations.append({"token": tok, "meaning": desc, "position": i})
                i += len(tok)
                matched = True
                break
        if not matched:
            if pattern[i] == '[':
                end = pattern.find(']', i)
                if end > i:
                    charset = pattern[i:end+1]
                    explanations.append({"token": charset, "meaning": f"character class: one of {charset[1:-1]}", "position": i})
                    i = end + 1
                    continue
            if pattern[i] == '(':
                explanations.append({"token": "(", "meaning": "start of capture group", "position": i})
            elif pattern[i] == ')':
                explanations.append({"token": ")", "meaning": "end of capture group", "position": i})
            elif pattern[i] == '{':
                end = pattern.find('}', i)
                if end > i:
                    quant = pattern[i:end+1]
                    explanations.append({"token": quant, "meaning": f"repeat {quant[1:-1]} times", "position": i})
                    i = end + 1
                    continue
            else:
                explanations.append({"token": pattern[i], "meaning": f"literal '{pattern[i]}'", "position": i})
            i += 1
    try:
        re.compile(pattern)
        valid = True
    except re.error as e:
        valid = False
        explanations.append({"error": str(e)})
    return {"pattern": pattern, "is_valid": valid, "explanation": explanations, "token_count": len(explanations)}

@mcp.tool()
def extract_matches(pattern: str, text: str, group: int = 0, api_key: str = "") -> dict[str, Any]:
    """Extract all matches of a pattern from text. group=0 for full match, 1+ for capture groups."""
    allowed, msg, tier = check_access(api_key)
    if not allowed:
        return {"error": msg, "upgrade_url": "https://meok.ai/pricing"}

    if not _rate_check("extract_matches"):
        return {"error": "Rate limit exceeded (50/day)"}
    try:
        compiled = re.compile(pattern)
    except re.error as e:
        return {"error": f"Invalid regex: {e}"}
    matches = []
    for m in compiled.finditer(text):
        try:
            matches.append(m.group(group))
        except IndexError:
            return {"error": f"Group {group} does not exist in pattern"}
    unique = list(set(matches))
    return {"pattern": pattern, "matches": matches, "unique": unique, "total": len(matches), "unique_count": len(unique)}

if __name__ == "__main__":
    mcp.run()
