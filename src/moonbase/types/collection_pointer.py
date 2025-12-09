# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CollectionPointer"]


class CollectionPointer(BaseModel):
    """
    A lightweight reference to a `Collection`, containing the minimal information needed to identify it.
    """

    id: str
    """Unique identifier of the collection."""

    ref: str
    """The stable, machine-readable reference identifier of the collection."""

    type: Literal["collection"]
    """String representing the object’s type. Always `collection` for this object."""
