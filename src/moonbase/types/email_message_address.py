# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .item_pointer import ItemPointer

__all__ = ["EmailMessageAddress"]


class EmailMessageAddress(BaseModel):
    """The EmailMessageAddress object represents a recipient or sender of a message.

    It contains an email address and can be linked to a person and an organization in your collections.
    """

    id: str
    """Unique identifier for the object."""

    email: str
    """The email address."""

    role: Literal["from", "reply_to", "to", "cc", "bcc"]
    """The role of the address in the message.

    Can be `from`, `reply_to`, `to`, `cc`, or `bcc`.
    """

    type: Literal["email_message_address"]
    """String representing the object’s type.

    Always `message_address` for this object.
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
