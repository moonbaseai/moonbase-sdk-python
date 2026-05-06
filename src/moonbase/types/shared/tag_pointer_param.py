# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TagPointerParam"]


class TagPointerParam(BaseModel):
    """A lightweight reference to a `Tag` used in request bodies."""

    id: str
    """Unique identifier of the tag."""

    type: Literal["tag"]
    """String representing the object’s type. Always `tag` for this object."""
