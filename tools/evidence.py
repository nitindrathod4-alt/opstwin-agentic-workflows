"""Evidence primitives used by the advanced investigator."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    source: str
    timestamp: str
    signal: str
    detail: str
    supports: tuple[str, ...] = ()
    contradicts: tuple[str, ...] = ()
