from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class SessionInfo:
    """The session information for a paper."""

    session_name: str
    start_time: datetime
    end_time: datetime
    zoom_link: str

    @property
    def time_string(self) -> str:
        return "({}-{} GMT)".format(
            self.start_time.strftime("%H:%M"), self.end_time.strftime("%H:%M")
        )

    @property
    def start_time_string(self) -> str:
        return self.start_time.strftime("%Y-%m-%dT%H:%M:%S")

    @property
    def end_time_string(self) -> str:
        return self.end_time.strftime("%Y-%m-%dT%H:%M:%S")

    @property
    def session(self) -> str:
        start_date = f'{self.start_time.strftime("%b")} {self.start_time.day}'
        if self.session_name.startswith("D"):
            # demo sessions
            return f"Demo Session {self.session_name[1:]}: {start_date}"
        if self.session_name.startswith("P-"):
            # plenary sessions
            return f"{self.session_name[2:]}: {start_date}"
        if self.session_name.startswith("S-"):
            # social event sessions
            return f"{self.session_name[2:]}: {start_date}"
        if self.session_name.startswith("W-"):
            # workshop sessions
            return f"{self.session_name[2:]}: {start_date}"
        return f"Session {self.session_name}: {start_date}"


@dataclass(frozen=True)
class PaperContent:
    """The content of a paper.

    Needs to be synced with static/js/papers.js and static/js/paper_vis.js.
    """

    # needs to be synced with
    title: str
    authors: List[str]
    track: str
    paper_type: str
    abstract: str
    tldr: str
    keywords: List[str]
    pdf_url: Optional[str]
    demo_url: Optional[str]
    sessions: List[SessionInfo]
    similar_paper_uids: List[str]

    def __post_init__(self):
        assert self.track, self
        if self.pdf_url:
            assert self.pdf_url.startswith("https://"), self.pdf_url
        if self.demo_url:
            assert self.demo_url.startswith("https://") or self.demo_url.startswith(
                "http://"
            ), self.demo_url
        assert self.paper_type[0].isupper(), self


@dataclass(frozen=True)
class Paper:
    """The paper dataclass.

    This corresponds to an entry in the `papers.json`.
    See the `start()` method in static/js/papers.js.
    """

    id: str
    forum: str
    card_image_path: str
    presentation_id: str
    content: PaperContent

    @property
    def rocketchat_channel(self) -> str:
        return f"paper-{self.id.replace('.', '-')}"


@dataclass(frozen=True)
class PlenaryVideo:
    id: str
    title: str
    speakers: str
    presentation_id: Optional[str]


@dataclass(frozen=True)
class PlenarySession:
    id: str
    title: str
    image: str
    date: str
    day: str
    sessions: List[SessionInfo]
    presenter: Optional[str]
    institution: Optional[str]
    abstract: Optional[str]
    bio: Optional[str]
    # SlidesLive presentation ID
    presentation_id: Optional[str]
    rocketchat_channel: Optional[str]
    videos: List[PlenaryVideo]


@dataclass(frozen=True)
class CommitteeMember:
    role: str
    name: str
    aff: str
    im: Optional[str]
    tw: Optional[str]


@dataclass(frozen=True)
class TutorialSessionInfo:
    """The session information for a tutorial."""

    session_name: str
    start_time: datetime
    end_time: datetime
    livestream_id: str
    zoom_link: str

    @property
    def time_string(self) -> str:
        return "({}-{} GMT)".format(
            self.start_time.strftime("%H:%M"), self.end_time.strftime("%H:%M")
        )

    @property
    def start_time_string(self) -> str:
        return self.start_time.strftime("%Y-%m-%dT%H:%M:%S")

    @property
    def end_time_string(self) -> str:
        return self.end_time.strftime("%Y-%m-%dT%H:%M:%S")

    @property
    def session(self) -> str:
        start_date = f'{self.start_time.strftime("%b")} {self.start_time.day}'
        return f"{self.session_name}: {start_date}"


@dataclass(frozen=True)
class Tutorial:
    id: str
    title: str
    organizers: List[str]
    abstract: str
    website: Optional[str]
    material: Optional[str]
    slides: Optional[str]
    prerecorded: Optional[str]
    rocketchat_channel: str
    sessions: List[TutorialSessionInfo]
    virtual_format_description: str


@dataclass(frozen=True)
class WorkshopPaper:
    id: str
    title: str
    speakers: str
    presentation_id: Optional[str]


@dataclass(frozen=True)
class Workshop:
    id: str
    title: str
    day: str
    organizers: List[str]
    abstract: str
    website: str
    livestream: Optional[str]
    papers: List[WorkshopPaper]
    schedule: List[Dict[str, Any]]
    rocketchat_channel: str
    sessions: List[SessionInfo]


@dataclass(frozen=True)
class SocialEventOrganizers:
    members: List[str]
    website: str


@dataclass(frozen=True)
class SocialEvent:
    id: str
    name: str
    description: str
    image: str
    organizers: SocialEventOrganizers
    sessions: List[SessionInfo]
    rocketchat_channel: str
    website: str
