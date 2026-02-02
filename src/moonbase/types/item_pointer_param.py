# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .collection_pointer_param import CollectionPointerParam

__all__ = ["ItemPointerParam"]


class ItemPointerParam(TypedDict, total=False):
    """
    A reference to an `Item` within a specific `Collection`, providing the context needed to locate the item.
    """

    id: Required[str]
    """Unique identifier of the item."""

    collection: Required[CollectionPointerParam]
    """A reference to the `Collection` containing this item."""

    type: Required[Literal["item"]]
    """String representing the object’s type. Always `item` for this object."""
