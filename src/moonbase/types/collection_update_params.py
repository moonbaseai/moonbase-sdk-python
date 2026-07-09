# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CollectionUpdateParams"]


class CollectionUpdateParams(TypedDict, total=False):
    description: str
    """An optional, longer-form description of the collection's purpose."""

    icon_name: Optional[str]
    """The collection's icon, as a Phosphor icon name in kebab-case (e.g.

    `users`, `chart-bar`), or `null` to clear it.
    """

    name: str
    """The user-facing name of the collection."""
