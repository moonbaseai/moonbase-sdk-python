# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    """
    A Tag is a label that can be applied to supported resources (such as conversations, calls, and meetings) for organization and filtering.
    """

    id: str
    """Unique identifier for the object."""

    color: Literal[
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
    """The color for the tag."""

    name: str
    """The name of the tag."""

    type: Literal["tag"]
    """String representing the object’s type. Always `tag` for this object."""
