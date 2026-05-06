# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TagsetCreateParams", "Tag"]


class TagsetCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the tagset."""

    description: str
    """An optional description of the tagset's purpose."""

    tags: Iterable[Tag]
    """Optional list of tags to create with this tagset.

    Tags are ordered by their position in the list.
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
