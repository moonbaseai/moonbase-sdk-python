# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.formatted_text import FormattedText

__all__ = ["NoteUpdateParams"]


class NoteUpdateParams(TypedDict, total=False):
    body: Required[FormattedText]
    """The main content of the note."""

    lock_version: Required[int]
    """The current lock version of the note for optimistic concurrency control."""
