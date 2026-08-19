# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .email_message_address_params import EmailMessageAddressParams
from .shared_params.formatted_text import FormattedText
from .slack_message_address_params import SlackMessageAddressParams

__all__ = ["InboxMessageUpdateParams", "Message", "MessageEmailMessageUpdateParams", "MessageSlackMessageUpdateParams"]


class InboxMessageUpdateParams(TypedDict, total=False):
    message: Required[Message]
    """Parameters for updating a draft message in an existing conversation."""


class MessageEmailMessageUpdateParams(TypedDict, total=False):
    """Parameters for updating a draft message in an existing conversation."""

    lock_version: Required[int]
    """The current lock version of the draft for optimistic concurrency control."""

    type: Required[Literal["email_message"]]

    bcc: Iterable[EmailMessageAddressParams]
    """A list of the BCC recipients."""

    body: FormattedText
    """The email body."""

    cc: Iterable[EmailMessageAddressParams]
    """A list of the CC recipients."""

    subject: str
    """The subject line of the email."""

    to: Iterable[EmailMessageAddressParams]
    """A list of the recipients."""


class MessageSlackMessageUpdateParams(TypedDict, total=False):
    """Parameters for updating a draft message in an existing conversation."""

    lock_version: Required[int]
    """The current lock version of the draft for optimistic concurrency control."""

    type: Required[Literal["slack_message"]]

    body: FormattedText
    """The message body."""

    subject: str
    """The subject line of the conversation (not included in actual Slack message)."""

    to: Iterable[SlackMessageAddressParams]
    """The Slack channel to post the message in."""


Message: TypeAlias = Union[MessageEmailMessageUpdateParams, MessageSlackMessageUpdateParams]
