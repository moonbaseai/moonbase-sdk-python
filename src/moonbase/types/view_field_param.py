# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ViewFieldParam"]


class ViewFieldParam(TypedDict, total=False):
    """A column of the view."""

    field: Required[str]
    """The field shown in this column."""

    display_fields: SequenceNotStr[str]
    """Which fields of the related item to show, relative to the related collection.

    Omitted means the related collection's default display fields.
    """

    is_pinned: bool
    """Whether the column is pinned."""

    is_wrapped: bool
    """Whether the column wraps its content."""

    size: Union[float, Literal["fit", "flex"]]
    """
    The column width: a number of pixels, or `fit` (size to content), or `flex`
    (fill available space).
    """
