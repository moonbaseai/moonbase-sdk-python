# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TagPointerParam"]


class TagPointerParam(TypedDict, total=False):
    """A lightweight reference to a `Tag` used in request bodies."""

    id: Required[str]
    """Unique identifier of the tag."""

    type: Required[Literal["tag"]]
    """String representing the object’s type. Always `tag` for this object."""
