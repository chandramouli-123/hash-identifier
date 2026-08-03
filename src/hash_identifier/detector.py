from .models import HashCandidate
from .rules import HEX_LENGTH_RULES, PREFIX_RULES
from .validators import _is_hex


def identify(text: str):
    result = []

    for prefix, algorithm, detail in PREFIX_RULES:
        if text.startswith(prefix):
            return [HashCandidate(algorithm, detail, "High", "Matches Prefix")]

    hash_len = len(text)

    if _is_hex(text) and hash_len in HEX_LENGTH_RULES:
        for algo, detail in HEX_LENGTH_RULES[hash_len]:
            result.append(
                HashCandidate(
                    algo,
                    detail,
                    "Medium",
                    "Length matches and contains only hexadecimal values",
                )
            )

    return result