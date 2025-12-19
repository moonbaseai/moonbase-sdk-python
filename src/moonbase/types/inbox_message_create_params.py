# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["InboxMessageCreateParams", "Bcc", "Cc", "To"]


class InboxMessageCreateParams(TypedDict, total=False):
    body: Required[str]
    """The content of the email body in Markdown format."""

    inbox_id: Required[str]
    """The inbox to use for sending the email."""

    bcc: Iterable[Bcc]
    """A list of `Address` objects for the BCC recipients."""

    cc: Iterable[Cc]
    """A list of `Address` objects for the CC recipients."""

    conversation_id: str
    """The ID of the conversation, if responding to an existing conversation."""

    subject: str
    """The subject line of the email."""

    to: Iterable[To]
    """A list of `Address` objects for the recipients."""


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
