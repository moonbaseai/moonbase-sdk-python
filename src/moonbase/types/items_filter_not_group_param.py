# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemsFilterNotGroupParam"]


class ItemsFilterNotGroupParam(TypedDict, total=False):
    filter: Required["ItemsFilterParam"]
    """A nested filter which must NOT match in order for this `not` filter to match."""

    op: Required[Literal["not"]]


from .items_filter_param import ItemsFilterParam
