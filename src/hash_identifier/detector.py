from .models import HashCandidate
from .rules import HEX_LENGTH_RULES, PREFIX_RULES
from .validators import _is_hex
from .models import Rule
import re

def identify(text: str):
    result = []

    for rule in PREFIX_RULES:
        is_match = False
        if rule.regex:
            is_match = bool(re.fullmatch(rule.regex, text))
            if is_match and rule.length is not None:
                is_match = (len(text) == rule.length)
        elif rule.prefix:
            is_match = text.startswith(rule.prefix)
            if is_match and rule.length is not None:
                is_match = (len(text) == rule.length)

        if is_match:
            return [
                HashCandidate(
                    algorithm=rule.algorithm,
                    detail=rule.detail,
                    confidence=rule.confidence,
                    reason=rule.reason,
                )
            ]

    hash_len = len(text)

    if _is_hex(text) and hash_len in HEX_LENGTH_RULES:
        for algo, detail in HEX_LENGTH_RULES[hash_len]:
            result.append(
                HashCandidate(
                    algo,
                    detail,
                    50,
                    "Length matches and contains only hexadecimal values",
                )
            )

    return result