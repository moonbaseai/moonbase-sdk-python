# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ItemsFilterOrGroup"]


class ItemsFilterOrGroup(BaseModel):
    """Include only items that match ANY of the filters in `filters`."""

    filters: List["ItemsFilter"]
    """
    An array of filters, ANY of which must be satisfied for this `or` filter to
    match.
    """

    op: Literal["or"]


from .items_filter import ItemsFilter
