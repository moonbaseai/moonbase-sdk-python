# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .tagset_pointer import TagsetPointer

__all__ = ["Inbox"]


class Inbox(BaseModel):
    """The Inbox object represents a shared inbox for receiving and sending messages."""

    id: str
    """Unique identifier for the object."""

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    name: str
    """The display name of the inbox."""

    tagsets: List[TagsetPointer]
    """
    A list of `TagsetPointer` objects referring to the Tagsets associated with this
    inbox, which defines the tags available for its conversations.
    """

    type: Literal["inbox"]
    """String representing the object’s type. Always `inbox` for this object."""

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""

    can_read: Optional[bool] = None
