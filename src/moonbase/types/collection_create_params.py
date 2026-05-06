# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CollectionCreateParams"]


class CollectionCreateParams(TypedDict, total=False):
    name: Required[str]
    """The user-facing name of the collection (e.g., "Leads").

    A `ref` is automatically derived from the name.
    """

    description: str
    """An optional, longer-form description of the collection's purpose."""
