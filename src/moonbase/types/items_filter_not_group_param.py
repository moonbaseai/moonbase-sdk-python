# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemsFilterNotGroupParam"]


class ItemsFilterNotGroupParam(TypedDict, total=False):
    """Include only items that do NOT match the nested `filter`."""

    filter: Required["ItemsFilterParam"]
    """A nested filter which must NOT match in order for this `not` filter to match."""

    op: Required[Literal["not"]]


from .items_filter_param import ItemsFilterParam  # noqa: I001
from .items_filter_and_group_param import ItemsFilterAndGroupParam  # noqa: F401 # pyright: ignore [reportUnusedImport]
from .items_filter_or_group_param import ItemsFilterOrGroupParam  # noqa: F401 # pyright: ignore [reportUnusedImport]
