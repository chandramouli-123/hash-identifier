from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HashCandidate:
    algorithm: str
    detail: str
    confidence: int
    reason: str


@dataclass(frozen=True,slots=True)
class Rule:
    algorithm : str
    detail : str
    confidence : int
    reason : str
    regex : Optional[str] = None
    prefix : Optional[str] = None
    suffix : Optional[str] = None    
    length : Optional[int]=None
