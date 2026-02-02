# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.formatted_text import FormattedText

__all__ = ["InboxMessageUpdateParams", "Bcc", "Cc", "To"]


class InboxMessageUpdateParams(TypedDict, total=False):
    lock_version: Required[int]
    """The current lock version of the draft for optimistic concurrency control."""

    bcc: Iterable[Bcc]
    """A list of the BCC recipients."""

    body: FormattedText
    """The email body."""

    cc: Iterable[Cc]
    """A list of the CC recipients."""

    subject: str
    """The subject line of the email."""

    to: Iterable[To]
    """A list of the recipients."""


class Bcc(TypedDict, total=False):
    email: Required[str]
    """The email address."""

    name: str
    """The recipient's name."""


class Cc(TypedDict, total=False):
    email: Required[str]
    """The email address."""

    name: str
    """The recipient's name."""


class To(TypedDict, total=False):
    email: Required[str]
    """The email address."""

    name: str
    """The recipient's name."""
