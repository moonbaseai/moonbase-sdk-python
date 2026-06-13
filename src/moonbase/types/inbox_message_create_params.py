# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .email_message_address_params import EmailMessageAddressParams
from .shared_params.formatted_text import FormattedText

__all__ = ["InboxMessageCreateParams", "Variant0", "EmailMessageReplyCreateParams"]


class Variant0(TypedDict, total=False):
    body: Required[FormattedText]
    """The email body."""

    inbox_id: Required[str]
    """The inbox to use for sending the email."""

    subject: Required[str]
    """The subject line of the email."""

    to: Required[Iterable[EmailMessageAddressParams]]
    """A list of recipients."""

    bcc: Iterable[EmailMessageAddressParams]
    """A list of the BCC recipients."""

    cc: Iterable[EmailMessageAddressParams]
    """A list of the CC recipients."""


class EmailMessageReplyCreateParams(TypedDict, total=False):
    body: Required[FormattedText]
    """The email body."""

    conversation_id: Required[str]
    """The ID of the conversation to reply to."""

    inbox_id: Required[str]
    """The inbox to use for sending the email."""

    bcc: Iterable[EmailMessageAddressParams]
    """A list of the BCC recipients."""

    cc: Iterable[EmailMessageAddressParams]
    """A list of the CC recipients."""

    to: Iterable[EmailMessageAddressParams]
    """A list of recipients. If omitted, recipients are derived from the conversation."""


InboxMessageCreateParams: TypeAlias = Union[Variant0, EmailMessageReplyCreateParams]
