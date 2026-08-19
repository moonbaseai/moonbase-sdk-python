# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemsFilterOrGroupParam"]


class ItemsFilterOrGroupParam(TypedDict, total=False):
    """Include only items that match ANY of the filters in `filters`."""

    filters: Required[Iterable["ItemsFilterParam"]]
    """
    An array of filters, ANY of which must be satisfied for this `or` filter to
    match.
    """

    op: Required[Literal["or"]]


from .items_filter_param import ItemsFilterParam  # noqa: I001
from .items_filter_and_group_param import ItemsFilterAndGroupParam  # noqa: F401 # pyright: ignore [reportUnusedImport]
from .items_filter_not_group_param import ItemsFilterNotGroupParam  # noqa: F401 # pyright: ignore [reportUnusedImport]
