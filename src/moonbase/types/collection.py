# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .field import Field
from .._models import BaseModel

__all__ = ["Collection", "Links"]


class Links(BaseModel):
    self: str
    """The canonical URL for this object."""


class Collection(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: Links
    """A hash of related links."""

    name: str
    """The user-facing name of the collection (e.g., “Organizations”)."""

    ref: str
    """A unique, stable, machine-readable identifier for the collection.

    This reference is used in API requests and does not change even if the `name` is
    updated.
    """

    type: Literal["collection"]
    """String representing the object’s type. Always `collection` for this object."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    description: Optional[str] = None
    """An optional, longer-form description of the collection's purpose."""

    fields: Optional[List[Field]] = None
    """A list of `Field` objects that define the schema for items in this collection."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""

    views: Optional[List[object]] = None
    """A list of saved `View` objects for presenting the collection's data."""
