# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .item_pointer import ItemPointer

__all__ = ["CallParticipant"]


class CallParticipant(BaseModel):
    """Represents a participant in a call."""

    id: str
    """Unique identifier for the object."""

    phone: str
    """The E.164 formatted phone number of the participant."""

    role: Literal["caller", "callee", "other"]
    """The role of the participant in the call. Can be `caller`, `callee`, or `other`."""

    type: Literal["call_participant"]
    """String representing the object’s type.

    Always `call_participant` for this object.
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
