# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Call", "Participant"]


class Participant(BaseModel):
    id: str
    """Unique identifier for the object."""

    phone: str
    """The E.164 formatted phone number of the participant."""

    role: Literal["caller", "callee", "other"]
    """The role of the participant in the call. Can be `caller`, `callee`, or `other`."""

    type: Literal["participant"]
    """String representing the object’s type. Always `participant` for this object."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""


class Call(BaseModel):
    id: str
    """Unique identifier for the object."""

    direction: Literal["incoming", "outgoing"]
    """The direction of the call, either `incoming` or `outgoing`."""

    participants: List[Participant]
    """The participants involved in the call."""

    provider: str
    """The name of the phone provider that handled the call."""

    provider_id: str
    """The unique identifier for the call from the provider's system."""

    start_at: datetime
    """The time the call started, as an RFC 3339 timestamp."""

    status: Literal[
        "queued",
        "initiated",
        "ringing",
        "in_progress",
        "completed",
        "busy",
        "failed",
        "no_answer",
        "canceled",
        "missed",
        "answered",
        "forwarded",
        "abandoned",
    ]
    """The current status of the call."""

    type: Literal["call"]
    """String representing the object’s type. Always `call` for this object."""

    answered_at: Optional[datetime] = None
    """The time the call was answered, if available, as an RFC 3339 timestamp."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    end_at: Optional[datetime] = None
    """The time the call ended, if available, as an RFC 3339 timestamp."""

    provider_metadata: Optional[Dict[str, object]] = None
    """A hash of additional metadata from the provider."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
