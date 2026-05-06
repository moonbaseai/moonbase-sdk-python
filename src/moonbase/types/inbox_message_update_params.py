# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .email_message_address_params import EmailMessageAddressParams
from .shared_params.formatted_text import FormattedText

__all__ = ["InboxMessageUpdateParams"]


class InboxMessageUpdateParams(TypedDict, total=False):
    lock_version: Required[int]
    """The current lock version of the draft for optimistic concurrency control."""

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
