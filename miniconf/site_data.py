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
class Keynote:
    id: str
    speaker: str
    slides_link: str
    qa_link: str
    title: str
    image: str
    institution: str
    day: str
    time: str
    zoom: str
    abstract: str
    bio: str


@dataclass(frozen=True)
class CommitteeMember:
    role: str
    name: str
    aff: str
    im: Optional[str]
    tw: Optional[str]


@dataclass(frozen=True)
class Tutorial:
    id: str
    title: str
    organizers: List[str]
    abstract: str
    material: str


@dataclass(frozen=True)
class Workshop:
    id: str
    title: str
    organizers: List[str]
    abstract: str
    material: str
