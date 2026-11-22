<!-- mcp-name: CSOAI-ORG/regex-ai-mcp -->
[![MCP Scorecard: 74/100](https://img.shields.io/badge/proofof.ai-74%2F100-5b21b6)](https://proofof.ai/scorecard/regex-ai-mcp.html)

> **Scorecard provenance:** This linked ProofOf.ai badge is a publisher-supplied assessment, **not independent certification, external adoption or a GSPC measurement**. The GSPC badge below explicitly remains UNMEASURED.
>
> **Local execution disclosure:** `auth_middleware.py` writes day-level usage counters keyed by a truncated hash of the supplied API key (or an anonymous marker) to `~/.meok/usage.json`. The current regex tools compute user-supplied patterns locally; there is no active remote meter in `server.py`. The package is not side-effect-free.

# Regex Ai MCP

[![MEOK AI Labs](https://img.shields.io/badge/MEOK-AI%20Labs-667eea)](https://meok.ai)
[![GSPC](https://img.shields.io/badge/GSPC-UNMEASURED-9ca3af)](https://councilof.ai/api/gspc)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-Install-3775a9)](https://pypi.org/project/regex_ai_mcp/)

> regex-ai-mcp — deterministic regular-expression helper tools exposed through MCP.

This repository provides regex pattern construction, matching and explanation utilities under the MIT licence. It is not a model evaluation, regulatory control, or compliance certification.

---

## 🚀 Quick Start

```bash
# Install via pip
pip install regex_ai_mcp

# Or install via Smithery
npx -y @smithery/cli@latest install regex-ai-mcp --client claude
```

## ✨ Features

- MCP interface for regex helpers (verify client/SDK compatibility before deployment)
- Installable open-source Python package
- Pattern construction, matching and explanation
- Local daily access counters (see disclosure above)
- Not independently assessed for production security or regulatory compliance

## 📖 Documentation

- [Full Documentation](https://docs.meok.ai/regex-ai-mcp)
- [API Reference](https://api.meok.ai)
- [EU AI Act Compliance Guide](https://councilof.ai/compliance)

## 🛡️ Regulatory scope and limitations

This is a regex utility; **it does not implement, verify, or certify compliance with the EU AI Act**. In particular it is not an Article 9 risk management system, Article 13 transparency assessment, Article 15 accuracy/robustness assessment, Article 26 fundamental-rights impact assessment, or Article 50 watermarking mechanism. Such obligations require separate documented measures, technical and legal evaluation, and where applicable competent human review.

A regex match must not be presented as a GSPC score, a regulatory determination or proof of an independent assessment.

## How MEOK charges

For current commercial terms, see <https://meok.ai/pricing>. This open-source server's bundled `auth_middleware.py` currently enforces local daily access tiers; those code-level tier names do not establish a commercial subscription, price or paid-service entitlement.

This repository's source is MIT-licensed and free to self-host.

## 🤝 Part of the MEOK Ecosystem

This server is part of the **[MEOK AI Labs](https://meok.ai)** ecosystem — 300+ MCP servers for sovereign AI governance.

| Domain | Purpose |
|--------|---------|
| [councilof.ai](https://councilof.ai) | EU AI Act compliance marketplace |
| [safetyof.ai](https://safetyof.ai) | AI safety & monitoring |
| [meok.ai](https://meok.ai) | Sovereign AI platform |
| [cobolbridge.ai](https://cobolbridge.ai) | Legacy modernization |

## 📜 License

MIT © [CSOAI-ORG](https://github.com/CSOAI-ORG)

---

<p align="center">
  <sub>Built with 💜 by <a href="https://meok.ai">MEOK AI Labs</a> · UK Companies House 16939677</sub>
</p>
MIT © [MEOK AI Labs](https://meok.ai)

<!-- meok-moat-footer-v1 -->
---

## Pairs with MEOK Governance Suite

The wider MEOK ecosystem lists additional governance tools. Their presence does not establish regulatory compliance; check each tool's published capabilities, license, evidence and limitations before any deployment or reliance.

```bash
# One-shot install of the governance pack
npx meok-setup --pack governance
```


→ Full catalogue: [councilof.ai](https://councilof.ai)
→ MEOK AI Labs: [meok.ai](https://meok.ai)




## Configuration

Add to your `claude_desktop_config.json` (Claude Desktop) or your MCP client config:

```json
{
  "mcpServers": {
    "regex-ai-mcp": {
      "command": "uvx",
      "args": ["regex-ai-mcp"]
    }
  }
}
```

Or: `pip install regex-ai-mcp` then run the `regex-ai-mcp` command (stdio transport).

## Examples

Once configured, ask your assistant, for example:
- "Use `build_regex` to …"
- "Use `test_regex` to …"
- "Use `explain_regex` to …"
