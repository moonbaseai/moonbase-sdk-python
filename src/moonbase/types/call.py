# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .note import Note
from .._models import BaseModel
from .shared.tag import Tag
from .call_transcript import CallTranscript
from .call_participant import CallParticipant

__all__ = ["Call"]


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

    participants: List[CallParticipant]
    """The participants involved in the call."""

    provider: Literal["openphone", "user", "zoom_phone"]
    """The name of the phone provider that handled the call."""

    provider_id: str
    """The unique identifier for the call from the provider's system."""

    provider_status: str
    """The current status of the call."""

    start_at: datetime
    """The time the call started, as an ISO 8601 timestamp in UTC."""

    tags: List[Tag]
    """The tags currently applied to this call."""

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

    transcript: Optional[CallTranscript] = None
