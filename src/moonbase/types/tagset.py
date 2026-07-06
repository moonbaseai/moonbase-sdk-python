# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.tag import Tag
from .tagset_association import TagsetAssociation

__all__ = ["Tagset"]


class Tagset(BaseModel):
    """
    A Tagset is a collection of `Tag` objects whose tags can be applied to conversations, calls, and meetings.
    """

    id: str
    """Unique identifier for the object."""

    associations: List[TagsetAssociation]
    """Where a tagset is available (`calls`, `meetings`, or `inbox` with an inbox ID)."""

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    name: str
    """The name of the tagset."""

    tags: List[Tag]
    """A list of `Tag` objects belonging to this tagset."""

    type: Literal["tagset"]
    """String representing the object’s type. Always `tagset` for this object."""

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""

    description: Optional[str] = None
    """An optional description of the tagset's purpose."""
