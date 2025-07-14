# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .attendee import Attendee
from .organizer import Organizer

__all__ = ["Meeting", "Links"]


class Links(BaseModel):
    self: str
    """The canonical URL for this object."""

    note: Optional[str] = None
    """A link to an associated `Note` object."""

    recording_url: Optional[str] = None
    """A temporary, signed URL to download the meeting recording.

    The URL expires after one hour.
    """

    summary: Optional[str] = None
    """A link to a long-form summary of the meeting."""

    transcript_url: Optional[str] = None
    """A temporary, signed URL to download the meeting transcript.

    The URL expires after one hour.
    """


class Meeting(BaseModel):
    id: str
    """Unique identifier for the object."""

    end_at: datetime
    """The end time of the meeting, as an RFC 3339 timestamp."""

    i_cal_uid: str
    """The globally unique iCalendar UID for the meeting event."""

    links: Links

    provider_id: str
    """
    The unique identifier for the meeting from the external calendar provider (e.g.,
    Google Calendar).
    """

    start_at: datetime
    """The start time of the meeting, as an RFC 3339 timestamp."""

    time_zone: str
    """
    The IANA time zone in which the meeting is scheduled (e.g.,
    `America/Los_Angeles`).
    """

    type: Literal["meeting"]
    """String representing the object’s type. Always `meeting` for this object."""

    attendees: Optional[List[Attendee]] = None
    """A list of `Attendee` objects for the meeting."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    description: Optional[str] = None
    """A detailed description or agenda for the meeting."""

    duration: Optional[float] = None
    """The duration of the meeting in seconds."""

    location: Optional[str] = None
    """The physical or virtual location of the meeting."""

    organizer: Optional[Organizer] = None
    """The `Organizer` of the meeting."""

    provider_uri: Optional[str] = None
    """A URL to access the meeting in the external provider's system."""

    summary_ante: Optional[str] = None
    """A summary or notes generated before the meeting."""

    summary_post: Optional[str] = None
    """A summary or notes generated after the meeting."""

    title: Optional[str] = None
    """The title or subject of the meeting."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
