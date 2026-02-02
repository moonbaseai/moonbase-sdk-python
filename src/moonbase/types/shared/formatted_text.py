# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FormattedText"]


class FormattedText(BaseModel):
    """
    Structured content that can be rendered in multiple formats, currently supporting Markdown.
    """

    markdown: Optional[str] = None
    """The content formatted as Markdown text."""
