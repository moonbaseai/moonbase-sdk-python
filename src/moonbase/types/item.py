# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from .._models import BaseModel
from .field_value import FieldValue
from .collection_pointer import CollectionPointer

__all__ = ["Item"]


class Item(BaseModel):
    """An Item represents a single record or row within a Collection.

    It holds a set of `values` corresponding to the Collection's `fields`.
    """

    id: str
    """Unique identifier for the object."""

    collection: CollectionPointer
    """
    A lightweight reference to a `Collection`, containing the minimal information
    needed to identify it.
    """

    type: Literal["item"]
    """String representing the object’s type. Always `item` for this object."""

    values: Dict[str, FieldValue]
    """
    A hash where keys are the `ref` of a `Field` and values are the data stored for
    that field.
    """
