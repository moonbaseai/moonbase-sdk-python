# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IdentifierValue"]


class IdentifierValue(BaseModel):
    """Identifier string"""

    data: str
    """An external identifier as text, uo to 255 characters in length."""

    type: Literal["value/identifier"]
