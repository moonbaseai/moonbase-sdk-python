# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChoiceFieldOption"]


class ChoiceFieldOption(BaseModel):
    """Represents a single selectable option within a choice field."""

    id: str
    """Unique identifier for the option."""

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
    """The color of the option."""

    name: str
    """The human-readable text displayed for this option."""

    type: Literal["choice_field_option"]
    """String representing the object’s type.

    Always `choice_field_option` for this object.
    """
