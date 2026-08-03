# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .inbox import Inbox
from .._models import BaseModel
from .shared.tag import Tag

__all__ = ["InboxConversation"]


class InboxConversation(BaseModel):
    """The Conversation object represents a thread of related messages."""

    id: str
    """Unique identifier for the object."""

    bulk: bool
    """`true` if the conversation appears to be part of a bulk mailing."""

    channel: Literal["email", "chat", "slack"]
    """
    The communication channel of the conversation, which can be `email`, `chat`, or
    `slack`.
    """

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    draft: bool
    """`true` if a new draft reply to this conversation has been started."""

    follow_up: bool
    """Whether the conversation is marked for follow-up."""

    last_message_at: datetime
    """
    The time of the most recent activity in the conversation, as an ISO 8601
    timestamp in UTC.
    """

    spam: bool
    """`true` if the conversation is marked as spam."""

    state: Literal["unassigned", "active", "closed", "waiting"]
    """The current state, which can be `unassigned`, `active`, `closed`, or `waiting`."""

    subject: str
    """The subject line of the conversation."""

    tags: List[Tag]
    """A list of `Tag` objects applied to this conversation."""

    trash: bool
    """`true` if the conversation is in the trash."""

    type: Literal["inbox_conversation"]
    """String representing the object’s type.

    Always `inbox_conversation` for this object.
    """

    unread: bool
    """`true` if the conversation contains unread messages."""

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""

    inbox: Optional[Inbox] = None
    """The `Inbox` that this conversations belongs to.

    **Note:** Only present when requested using the `include` query parameter.
    """

    messages: Optional[List[object]] = None
    """The `Message` objects that belong to this conversation.

    **Note:** Only present when requested using the `include` query parameter.
    """

    unsnooze_at: Optional[datetime] = None
    """
    If the conversation is snoozed, this is the time it will reappear in the inbox,
    as an ISO 8601 timestamp in UTC.
    """
