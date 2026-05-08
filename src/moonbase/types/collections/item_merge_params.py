# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..item_pointer_param import ItemPointerParam

__all__ = ["ItemMergeParams"]


class ItemMergeParams(TypedDict, total=False):
    destination: Required[ItemPointerParam]
    """The destination item pointer. This will be the remaining merged item."""

    source: Required[ItemPointerParam]
    """The source item pointer. This item will be deleted."""
