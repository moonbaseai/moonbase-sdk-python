# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["RelationValue"]


class RelationValue(BaseModel):
    item: "Item"
    """An Item represents a single record or row within a Collection.

    It holds a set of `values` corresponding to the Collection's `fields`.
    """

    type: Literal["value/relation"]


from .item import Item

if PYDANTIC_V2:
    RelationValue.model_rebuild()
else:
    RelationValue.update_forward_refs()  # type: ignore
