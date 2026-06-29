# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ItemsFilterAndGroup"]


class ItemsFilterAndGroup(BaseModel):
    """Include only items that match ALL of the filters in `filters`."""

    filters: List["ItemsFilter"]
    """
    An array of filters, ALL of which must be satisfied for this `and` filter to
    match.
    """

    op: Literal["and"]


from .items_filter import ItemsFilter
