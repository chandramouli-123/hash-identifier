import sys
from pathlib import Path
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hash_identifier.detector import identify
from hash_identifier.models import HashCandidate


class DetectorTests(unittest.TestCase):
    def test_prefix_match_returns_high_confidence_candidate(self):
        self.assertEqual(
            identify("$2b$12$" + "a" * 53),
            [HashCandidate("bcrypt", "Current bcrypt variant", 100, "Matches Prefix")],
        )

    def test_hex_length_match_returns_all_candidates_for_length(self):
        candidates = identify("5f4dcc3b5aa765d61d8327deb882cf99")

        self.assertEqual(len(candidates), 4)
        self.assertEqual(candidates[0].algorithm, "MD5")
        self.assertEqual(candidates[0].confidence, 50)


if __name__ == "__main__":
    unittest.main()