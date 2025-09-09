# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .item_pointer_param import ItemPointerParam
from .shared_params.pointer import Pointer

__all__ = ["RelationValueParam", "Item"]

Item: TypeAlias = Union[ItemPointerParam, Pointer]


class RelationValueParam(TypedDict, total=False):
    item: Required[Item]
    """
    A reference to an `Item` within a specific `Collection`, providing the context
    needed to locate the item.
    """

    type: Required[Literal["value/relation"]]
