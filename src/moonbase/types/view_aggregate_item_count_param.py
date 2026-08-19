# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ViewAggregateItemCountParam"]


class ViewAggregateItemCountParam(TypedDict, total=False):
    """Counts the view's items."""

    type: Required[Literal["item_count"]]

    group: str
    """An optional field whose values bucket the counts."""
