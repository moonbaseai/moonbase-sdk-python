# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CurrentDatetimeParam"]


class CurrentDatetimeParam(TypedDict, total=False):
    """Resolves to the current date and time at the time the record is created."""

    type: Required[Literal["current_datetime"]]
