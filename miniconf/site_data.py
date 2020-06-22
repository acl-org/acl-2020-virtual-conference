from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Paper:
    uid: str
    title: str
    authors: List[str]
    abstract: str
    keywords: List[str]
    track: str
    paper_type: str


@dataclass(frozen=True)
class CommitteeMember:
    role: str
    name: str
    aff: str
    im: Optional[str]
    tw: Optional[str]
