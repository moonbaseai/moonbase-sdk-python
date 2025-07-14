# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Attendee", "Links"]


class Links(BaseModel):
    organization: str
    """A link to the associated `Organization` item."""

    person: str
    """A link to the associated `Person` item."""


class Attendee(BaseModel):
    id: str
    """Unique identifier for the object."""

    email: str
    """The email address of the attendee."""

    links: Links
    """A hash of related links."""

    type: Literal["attendee"]
    """String representing the object’s type. Always `attendee` for this object."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
