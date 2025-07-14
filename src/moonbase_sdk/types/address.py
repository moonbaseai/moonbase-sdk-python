# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Address", "Links"]


class Links(BaseModel):
    organization: Optional[str] = None
    """A link to the associated `Organization` item."""

    person: Optional[str] = None
    """A link to the associated `Person` item."""


class Address(BaseModel):
    id: str
    """Unique identifier for the object."""

    email: str
    """The email address."""

    links: Links
    """A hash of related links."""

    type: Literal["address"]
    """String representing the object’s type. Always `address` for this object."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    role: Optional[Literal["from", "reply_to", "to", "cc", "bcc"]] = None
    """The role of the address in the message.

    Can be `from`, `reply_to`, `to`, `cc`, or `bcc`.
    """

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
