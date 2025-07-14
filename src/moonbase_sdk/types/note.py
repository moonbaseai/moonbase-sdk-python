# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Note", "Links"]


class Links(BaseModel):
    self: str
    """The canonical URL for this object."""


class Note(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: Links

    type: Literal["note"]
    """String representing the object’s type. Always `note` for this object."""

    body: Optional[str] = None
    """The main content of the note."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    summary: Optional[str] = None
    """A short, system-generated summary of the note's content."""

    title: Optional[str] = None
    """An optional title for the note."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
