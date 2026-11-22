"""Fail closed if the MCP server misstates its issuer or runtime side effects."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class TrustTransparencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = (ROOT / "server.py").read_text()
        cls.auth = (ROOT / "auth_middleware.py").read_text()
        cls.readme = (ROOT / "README.md").read_text()

    def test_no_unused_phone_home_function_or_credential_forwarder(self):
        self.assertNotIn("_server_meter_check", self.server)
        self.assertNotIn("_METER_URL", self.server)
        self.assertNotIn("proofof.ai/verify", self.server)

    def test_local_side_effect_truth_in_docs(self):
        self.assertIn("_save_json(USAGE_FILE, usage)", self.auth)
        self.assertIn("~/.meok/usage.json", self.server)
        self.assertIn("~/.meok/usage.json", self.readme)
        self.assertNotIn("no side effects", self.server.lower())
        self.assertNotIn("fully idempotent", self.server.lower())
        self.assertNotIn("read-only and stateless", self.server.lower())

    def test_no_unsupported_paid_or_certification_claim(self):
        self.assertIn("publisher-supplied assessment", self.readme)
        self.assertIn("not independent certification", self.readme)
        self.assertIn("GSPC-UNMEASURED", self.readme)
        self.assertNotIn("Pro tier: unlimited calls", self.server)
        self.assertNotIn("No tiers. Jobs are quoted", self.server)

    def test_regulatory_scope_is_not_misrepresented(self):
        self.assertIn("does not implement, verify, or certify compliance", self.readme)
        self.assertNotIn("EU AI Act compliance** built-in", self.readme)
        self.assertNotIn("Production-ready", self.readme)
        self.assertNotIn("✅ Article 50", self.readme)

if __name__ == "__main__":
    unittest.main()
