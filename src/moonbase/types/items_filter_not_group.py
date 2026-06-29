# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ItemsFilterNotGroup"]


class ItemsFilterNotGroup(BaseModel):
    """Include only items that do NOT match the nested `filter`."""

    filter: "ItemsFilter"
    """A nested filter which must NOT match in order for this `not` filter to match."""

    op: Literal["not"]


from .items_filter import ItemsFilter
