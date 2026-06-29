# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ViewField"]


class ViewField(BaseModel):
    """A column of the view."""

    field: str
    """The field shown in this column."""

    display_fields: Optional[List[str]] = None
    """Which fields of the related item to show, relative to the related collection.

    Omitted means the related collection's default display fields.
    """

    is_pinned: Optional[bool] = None
    """Whether the column is pinned."""

    is_wrapped: Optional[bool] = None
    """Whether the column wraps its content."""

    size: Union[float, Literal["fit", "flex"], None] = None
    """
    The column width: a number of pixels, or `fit` (size to content), or `flex`
    (fill available space).
    """
