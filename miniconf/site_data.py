from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Paper:
    uid: str
    title: str
    authors: List[str]
    abstract: str
    keywords: List[str]
    track: str
    paper_type: str
