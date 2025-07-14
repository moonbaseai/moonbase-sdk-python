# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tagset", "Links", "Tag"]


class Links(BaseModel):
    self: str
    """The canonical URL for this object."""


class Tag(BaseModel):
    id: str
    """Unique identifier for the object."""

    name: str
    """The name of the tag."""

    type: Literal["tag"]
    """String representing the object’s type. Always `tag` for this object."""


class Tagset(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: Links

    name: str
    """The name of the tagset."""

    type: Literal["tagset"]
    """String representing the object’s type. Always `tagset` for this object."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    description: Optional[str] = None
    """An optional description of the tagset's purpose."""

    tags: Optional[List[Tag]] = None
    """A list of `Tag` objects belonging to this tagset."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
