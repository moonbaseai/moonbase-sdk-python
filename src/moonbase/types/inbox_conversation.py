# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .address import Address
from .._models import BaseModel

__all__ = ["InboxConversation", "Links", "Tag"]


class Links(BaseModel):
    inbox: str
    """A link to the `Inbox` this conversation belongs to."""

    messages: str
    """A link to the list of `Message` objects in this conversation."""

    self: str
    """The canonical URL for this object."""


class Tag(BaseModel):
    id: str
    """Unique identifier for the object."""

    name: str
    """The name of the tag."""

    type: Literal["tag"]
    """String representing the object’s type. Always `tag` for this object."""


class InboxConversation(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: Links

    type: Literal["inbox_conversation"]
    """String representing the object’s type.

    Always `inbox_conversation` for this object.
    """

    addresses: Optional[List[Address]] = None
    """A list of `Address` objects (participants) in this conversation."""

    bulk: Optional[bool] = None
    """`true` if the conversation appears to be part of a bulk mailing."""

    closed: Optional[bool] = None
    """`true` if the conversation is currently closed."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    follow_up: Optional[bool] = None
    """Whether the conversation is marked for follow-up."""

    new_draft_conversation: Optional[bool] = None
    """`true` if a new draft reply to this conversation has been started."""

    open: Optional[bool] = None
    """`true` if the conversation is currently open."""

    spam: Optional[bool] = None
    """`true` if the conversation is marked as spam."""

    subject: Optional[str] = None
    """The subject line of the conversation."""

    tags: Optional[List[Tag]] = None
    """A list of `Tag` objects applied to this conversation."""

    timestamp: Optional[str] = None
    """
    The time of the most recent activity in the conversation, as an RFC 3339
    timestamp.
    """

    trash: Optional[bool] = None
    """`true` if the conversation is in the trash."""

    unread: Optional[bool] = None
    """`true` if the conversation contains unread messages."""

    unsnooze_at: Optional[datetime] = None
    """
    If the conversation is snoozed, this is the time it will reappear in the inbox,
    as an RFC 3339 timestamp.
    """

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
