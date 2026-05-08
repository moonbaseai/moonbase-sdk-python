# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IdentifierValueParam"]


class IdentifierValueParam(TypedDict, total=False):
    """Identifier string"""

    data: Required[str]
    """An external identifier as text, uo to 255 characters in length."""

    type: Required[Literal["value/identifier"]]
