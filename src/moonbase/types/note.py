# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .item_pointer import ItemPointer
from .shared.formatted_text import FormattedText
from .note_association_pointer import NoteAssociationPointer

__all__ = ["Note"]


class Note(BaseModel):
    """
    The Note object represents a block of text content, often used for meeting notes or summaries.
    """

    id: str
    """Unique identifier for the object."""

    associations: List[NoteAssociationPointer]
    """A list of items, meetings or calls this note is associated with."""

    body: FormattedText
    """The main content of the note."""

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    lock_version: int
    """The current lock version of the note for optimistic concurrency control."""

    type: Literal["note"]
    """String representing the object’s type. Always `note` for this object."""

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""

    creator: Optional[ItemPointer] = None
    """
    A reference to an `Item` within a specific `Collection`, providing the context
    needed to locate the item.
    """

    summary: Optional[str] = None
    """A short, system-generated summary of the note's content."""

    title: Optional[str] = None
    """An optional title for the note."""
