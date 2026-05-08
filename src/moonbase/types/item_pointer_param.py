# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemPointerParam"]


class ItemPointerParam(TypedDict, total=False):
    """A lightweight reference to an `Item` used in request bodies."""

    id: Required[str]
    """Unique identifier of the item."""

    type: Required[Literal["item"]]
    """String representing the object’s type. Always `item` for this object."""
