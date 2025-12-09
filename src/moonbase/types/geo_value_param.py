# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GeoValueParam"]


class GeoValueParam(TypedDict, total=False):
    """Geographic coordinate value"""

    data: Required[str]
    """A string that represents some geographic location.

    The exact format may vary based on context.
    """

    type: Required[Literal["value/geo"]]
