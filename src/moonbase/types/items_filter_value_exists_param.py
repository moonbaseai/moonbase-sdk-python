# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemsFilterValueExistsParam"]


class ItemsFilterValueExistsParam(TypedDict, total=False):
    """Include only items that have a value in the given `field`."""

    field: Required[str]
    """The id or key of the field for which a value must exist."""

    op: Required[Literal["exists"]]
