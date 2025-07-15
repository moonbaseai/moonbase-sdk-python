# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .field_value_param import FieldValueParam

__all__ = ["ItemCreateParams"]


class ItemCreateParams(TypedDict, total=False):
    collection_id: Required[str]
    """The ID of the `Collection` to create the item in."""

    values: Required[Dict[str, "FieldValueParam"]]
    """A hash where keys are the `ref` of a `Field` and values are the data to be set."""
