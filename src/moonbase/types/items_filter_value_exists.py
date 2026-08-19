# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ItemsFilterValueExists"]


class ItemsFilterValueExists(BaseModel):
    """Include only items that have a value in the given `field`."""

    field: str
    """
    The id or key of the field for which a value must exist, or a path to the field
    for which a value must exist.
    """

    op: Literal["exists"]
