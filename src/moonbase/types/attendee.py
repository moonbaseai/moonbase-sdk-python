# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.pointer import Pointer

__all__ = ["Attendee"]


class Attendee(BaseModel):
    """The Attendee object represents a participant in a meeting.

    It includes their email address and links to associated `Person` and `Organization` items, if they exist in your collections.
    """

    id: str
    """Unique identifier for the object."""

    email: str
    """The email address of the attendee."""

    type: Literal["meeting_attendee"]
    """String representing the object’s type.

    Always `meeting_attendee` for this object.
    """

    organization: Optional[Pointer] = None
    """A lightweight reference to another resource."""

    person: Optional[Pointer] = None
    """A lightweight reference to another resource."""
