# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .email_message_address_params import EmailMessageAddressParams
from .shared_params.formatted_text import FormattedText
from .slack_message_address_params import SlackMessageAddressParams

__all__ = [
    "InboxMessageCreateParams",
    "Message",
    "MessageEmailMessageNewConversationCreateParams",
    "MessageSlackMessageNewConversationCreateParams",
    "MessageEmailMessageReplyCreateParams",
    "MessageSlackMessageReplyCreateParams",
]


class InboxMessageCreateParams(TypedDict, total=False):
    message: Required[Message]
    """Parameters for creating an email message draft.

    Provide either the fields for a new conversation, or a `conversation_id` to
    reply to an existing conversation.
    """


class MessageEmailMessageNewConversationCreateParams(TypedDict, total=False):
    """Parameters for creating a draft in a new conversation."""

    body: Required[FormattedText]
    """The email body."""

    inbox_id: Required[str]
    """The inbox to use for sending the email."""

    subject: Required[str]
    """The subject line of the email."""

    to: Required[Iterable[EmailMessageAddressParams]]
    """A list of recipients."""

    type: Required[Literal["email_message"]]

    bcc: Iterable[EmailMessageAddressParams]
    """A list of the BCC recipients."""

    cc: Iterable[EmailMessageAddressParams]
    """A list of the CC recipients."""


class MessageSlackMessageNewConversationCreateParams(TypedDict, total=False):
    """Parameters for creating a draft in a new conversation."""

    body: Required[FormattedText]
    """The message body."""

    inbox_id: Required[str]
    """The inbox to use for sending the Slack message."""

    subject: Required[str]
    """The subject line of the conversation (not included in actual Slack message)."""

    to: Required[Iterable[SlackMessageAddressParams]]
    """The Slack channel to post the message in."""

    type: Required[Literal["slack_message"]]


class MessageEmailMessageReplyCreateParams(TypedDict, total=False):
    """Parameters for creating a draft reply in an existing conversation."""

    body: Required[FormattedText]
    """The email body."""

    conversation_id: Required[str]
    """The ID of the conversation to reply to."""

    inbox_id: Required[str]
    """The inbox to use for sending the email."""

    type: Required[Literal["email_message"]]

    bcc: Iterable[EmailMessageAddressParams]
    """A list of the BCC recipients."""

    cc: Iterable[EmailMessageAddressParams]
    """A list of the CC recipients."""

    to: Iterable[EmailMessageAddressParams]
    """A list of recipients. If omitted, recipients are derived from the conversation."""


class MessageSlackMessageReplyCreateParams(TypedDict, total=False):
    """Parameters for creating a draft reply in an existing conversation."""

    body: Required[FormattedText]
    """The message body."""

    conversation_id: Required[str]
    """The ID of the conversation to reply to."""

    inbox_id: Required[str]
    """The inbox to use for sending the Slack message."""

    type: Required[Literal["slack_message"]]

    to: Iterable[SlackMessageAddressParams]
    """The Slack channel to post the message in."""


Message: TypeAlias = Union[
    MessageEmailMessageNewConversationCreateParams,
    MessageSlackMessageNewConversationCreateParams,
    MessageEmailMessageReplyCreateParams,
    MessageSlackMessageReplyCreateParams,
]
