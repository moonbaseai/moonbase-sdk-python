# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .note import Note
from .._models import BaseModel
from .shared.pointer import Pointer

__all__ = ["Call", "Participant", "Transcript", "TranscriptCue", "TranscriptCueSpeaker"]


class Participant(BaseModel):
    """Represents a participant in a call."""

    id: str
    """Unique identifier for the object."""

    phone: str
    """The E.164 formatted phone number of the participant."""

    role: Literal["caller", "callee", "other"]
    """The role of the participant in the call. Can be `caller`, `callee`, or `other`."""

    type: Literal["call_participant"]
    """String representing the object’s type.

    Always `call_participant` for this object.
    """

    organization: Optional[Pointer] = None
    """A lightweight reference to another resource."""

    person: Optional[Pointer] = None
    """A lightweight reference to another resource."""


class TranscriptCueSpeaker(BaseModel):
    attendee_id: Optional[str] = None

    label: Optional[str] = None


class TranscriptCue(BaseModel):
    from_: float = FieldInfo(alias="from")

    speaker: TranscriptCueSpeaker

    text: str

    to: float


class Transcript(BaseModel):
    cues: List[TranscriptCue]


class Call(BaseModel):
    """The Call object represents a phone call that has been logged in the system.

    It contains details about the participants, timing, and outcome of the call.
    """

    id: str
    """Unique identifier for the object."""

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    direction: Literal["incoming", "outgoing"]
    """The direction of the call, either `incoming` or `outgoing`."""

    participants: List[Participant]
    """The participants involved in the call."""

    provider: str
    """The name of the phone provider that handled the call."""

    provider_id: str
    """The unique identifier for the call from the provider's system."""

    provider_status: str
    """The current status of the call."""

    start_at: datetime
    """The time the call started, as an ISO 8601 timestamp in UTC."""

    type: Literal["call"]
    """String representing the object’s type. Always `call` for this object."""

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""

    answered_at: Optional[datetime] = None
    """The time the call was answered, if available, as an ISO 8601 timestamp in UTC."""

    end_at: Optional[datetime] = None
    """The time the call ended, if available, as an ISO 8601 timestamp in UTC."""

    note: Optional[Note] = None
    """
    The Note object represents a block of text content, often used for meeting notes
    or summaries.
    """

    provider_metadata: Optional[Dict[str, object]] = None
    """A hash of additional metadata from the provider."""

    summary: Optional[Note] = None
    """
    The Note object represents a block of text content, often used for meeting notes
    or summaries.
    """

    transcript: Optional[Transcript] = None
