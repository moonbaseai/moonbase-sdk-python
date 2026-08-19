# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .item_pointer import ItemPointer

__all__ = ["SlackMessageAddress", "SlackMessageChannelAddress", "SlackMessageUserAddress"]


class SlackMessageChannelAddress(BaseModel):
    """
    The SlackMessageChannelAddress object represents a Slack channels address on a message. It contains a Slack Channel ID and can be linked to a person and an organization in your collections.
    """

    id: str
    """Unique identifier for the object."""

    provider_id: str
    """The Slack Channel ID."""

    role: Literal["from", "to", "cc", "bcc"]
    """The role of the address in the message.

    Can be `from`, `reply_to`, `to`, `cc`, or `bcc`.
    """

    type: Literal["slack_message_channel_address"]
    """String representing the object’s type.

    Always `slack_message_channel_address` for this object.
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


class SlackMessageUserAddress(BaseModel):
    """The SlackMessageUserAddress object represents a Slack user address on a message.

    It contains a Slack User ID  and can be linked to a person and an organization in your collections.
    """

    id: str
    """Unique identifier for the object."""

    provider_id: str
    """The Slack User ID"""

    role: Literal["from", "to", "cc", "bcc"]
    """The role of the address in the message.

    Can be `from`, `reply_to`, `to`, `cc`, or `bcc`.
    """

    type: Literal["slack_message_user_address"]
    """String representing the object’s type.

    Always `slack_message_user_address` for this object.
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


SlackMessageAddress: TypeAlias = Annotated[
    Union[SlackMessageChannelAddress, SlackMessageUserAddress], PropertyInfo(discriminator="type")
]
