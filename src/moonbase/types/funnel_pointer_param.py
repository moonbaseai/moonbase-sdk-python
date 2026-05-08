# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FunnelPointerParam"]


class FunnelPointerParam(TypedDict, total=False):
    """A pointer to a Funnel, used as a parameter."""

    id: Required[str]
    """The ID of the funnel."""

    type: Required[Literal["funnel"]]
    """String representing the object's type. Always `funnel` for this parameter."""
