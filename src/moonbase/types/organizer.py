# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .item_pointer import ItemPointer

__all__ = ["Organizer"]


class Organizer(BaseModel):
    """Represents the organizer of a meeting."""

    id: str
    """Unique identifier for the object."""

    email: str
    """The email address of the organizer."""

    type: Literal["meeting_organizer"]
    """String representing the object’s type.

    Always `meeting_organizer` for this object.
    """

    organization: Optional[ItemPointer] = None
    """
    A reference to an `Item` within a specific `Collection`, providing the context
    needed to locate the item.
    """

    person: Optional[ItemPointer] = None
    """
    A reference to an `Item` within a specific `Collection`, providing the context
    needed to locate the item.
    """
