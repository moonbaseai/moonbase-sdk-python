# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ItemSearchParams", "Filter", "FilterCollectionID"]


class ItemSearchParams(TypedDict, total=False):
    query: Required[str]
    """The search text to match against items."""

    filter: Filter
    """Filter results by one or more collection IDs or `ref` values."""


_FilterCollectionIDReservedKeywords = TypedDict(
    "_FilterCollectionIDReservedKeywords",
    {
        "in": SequenceNotStr[str],
    },
    total=False,
)


class FilterCollectionID(_FilterCollectionIDReservedKeywords, total=False):
    pass


class Filter(TypedDict, total=False):
    """Filter results by one or more collection IDs or `ref` values."""

    collection_id: FilterCollectionID
