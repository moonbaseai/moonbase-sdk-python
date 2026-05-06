# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .item_pointer_param import ItemPointerParam

__all__ = ["RelationValueParam"]


class RelationValueParam(TypedDict, total=False):
    """Related item reference"""

    data: Required[ItemPointerParam]
    """A reference to another Moonbase item."""

    type: Required[Literal["value/relation"]]
