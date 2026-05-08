# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CurrentDateParam"]


class CurrentDateParam(TypedDict, total=False):
    """Resolves to today's date at the time the record is created."""

    type: Required[Literal["current_date"]]
