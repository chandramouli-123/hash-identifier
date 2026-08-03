"""Compatibility wrapper for running the project from the repository root.

This keeps ``python cli.py`` working while the implementation lives in
``src/hash_identifier``.
"""

from __future__ import annotations

import sys
from pathlib import Path


_ROOT = Path(__file__).resolve().parent
_SRC = _ROOT / "src"

if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from hash_identifier.cli import main


if __name__ == "__main__":
    raise SystemExit(main())