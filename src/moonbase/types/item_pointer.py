# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .collection_pointer import CollectionPointer

__all__ = ["ItemPointer"]


class ItemPointer(BaseModel):
    """
    A reference to an `Item` within a specific `Collection`, providing the context needed to locate the item.
    """

    id: str
    """Unique identifier of the item."""

    collection: CollectionPointer
    """A reference to the `Collection` containing this item."""

    type: Literal["item"]
    """String representing the object’s type. Always `item` for this object."""
