from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HashCandidate:
    algorithm: str
    detail: str
    confidence: str
    reason: str
