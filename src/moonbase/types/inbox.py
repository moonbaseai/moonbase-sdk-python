# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .tagset import Tagset
from .._models import BaseModel

__all__ = ["Inbox", "Links"]


class Links(BaseModel):
    self: str
    """The canonical URL for this object."""

    tagset: Optional[str] = None
    """A link to the `Tagset` for this inbox."""


class Inbox(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: Links

    name: str
    """The display name of the inbox."""

    type: Literal["inbox"]
    """String representing the object’s type. Always `inbox` for this object."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    tagset: Optional[Tagset] = None
    """
    The `Tagset` associated with this inbox, which defines the tags available for
    its conversations.
    """

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
