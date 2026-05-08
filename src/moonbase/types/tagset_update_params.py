# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TagsetUpdateParams", "Tag"]


class TagsetUpdateParams(TypedDict, total=False):
    description: str
    """An updated description of the tagset."""

    name: str
    """The new name of the tagset."""

    tags: Iterable[Tag]
    """Optional full list of tags for this tagset.

    If provided, tags are ordered by array position.
    """


class Tag(TypedDict, total=False):
    """Parameters for creating or updating a tag within a tagset."""

    color: Required[
        Literal[
            "amber",
            "blue",
            "cyan",
            "emerald",
            "fuchsia",
            "green",
            "indigo",
            "lime",
            "lunar",
            "orange",
            "pink",
            "purple",
            "red",
            "rose",
            "sky",
            "teal",
            "violet",
            "yellow",
        ]
    ]
    """The color for the tag."""

    name: Required[str]
    """The name of the tag."""

    id: str
    """Existing tag identifier.

    Include to update an existing tag, omit to create a new tag.
    """
