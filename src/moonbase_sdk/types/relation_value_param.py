# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RelationValueParam"]


class RelationValueParam(TypedDict, total=False):
    item: Required["ItemParam"]
    """An Item represents a single record or row within a Collection.

    It holds a set of `values` corresponding to the Collection's `fields`.
    """

    type: Required[Literal["value/relation"]]


from .item_param import ItemParam
