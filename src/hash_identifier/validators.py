_HEX_CHARS = frozenset("0123456789abcdefABCDEF")


def _is_hex(text: str) -> bool:
    return all(character in _HEX_CHARS for character in text)