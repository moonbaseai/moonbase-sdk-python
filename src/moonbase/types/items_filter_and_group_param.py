# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemsFilterAndGroupParam"]


class ItemsFilterAndGroupParam(TypedDict, total=False):
    """Include only items that match ALL of the filters in `filters`."""

    filters: Required[Iterable["ItemsFilterParam"]]
    """
    An array of filters, ALL of which must be satisfied for this `and` filter to
    match.
    """

    op: Required[Literal["and"]]


from .items_filter_param import ItemsFilterParam
