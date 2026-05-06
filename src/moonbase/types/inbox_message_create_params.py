# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .email_message_address_params import EmailMessageAddressParams
from .shared_params.formatted_text import FormattedText

__all__ = ["InboxMessageCreateParams"]


class InboxMessageCreateParams(TypedDict, total=False):
    body: Required[FormattedText]
    """The email body."""

    inbox_id: Required[str]
    """The inbox to use for sending the email."""

    bcc: Iterable[EmailMessageAddressParams]
    """A list of the BCC recipients."""

    cc: Iterable[EmailMessageAddressParams]
    """A list of the CC recipients."""

    conversation_id: str
    """The ID of the conversation, if responding to an existing conversation."""

    subject: str
    """The subject line of the email."""

    to: Iterable[EmailMessageAddressParams]
    """A list of recipients."""
