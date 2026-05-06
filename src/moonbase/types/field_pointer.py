# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .collection_pointer import CollectionPointer

__all__ = ["FieldPointer"]


class FieldPointer(BaseModel):
    """
    A lightweight reference to a `Field`, containing the minimal information needed to identify it.
    """

    id: str
    """Unique identifier of the field."""

    collection: CollectionPointer
    """A reference to the `Collection` containing this field."""

    ref: str
    """The stable, machine-readable reference identifier of the field."""

    type: Literal["field"]
    """String representing the object’s type. Always `field` for this object."""
