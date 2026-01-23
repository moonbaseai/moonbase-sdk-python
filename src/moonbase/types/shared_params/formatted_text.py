# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FormattedText"]


class FormattedText(TypedDict, total=False):
    """
    Structured content that can be rendered in multiple formats, currently supporting Markdown.
    """

    markdown: str
    """The content formatted as Markdown text."""
