# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CurrentMemberParam"]


class CurrentMemberParam(TypedDict, total=False):
    """Resolves to the team member who creates the record."""

    type: Required[Literal["current_member"]]
