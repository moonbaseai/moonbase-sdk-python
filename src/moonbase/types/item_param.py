# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemParam"]


class ItemParam(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the object."""

    type: Required[Literal["item"]]
    """String representing the object’s type. Always `item` for this object."""

    values: Dict[str, Optional["FieldValueParam"]]
    """
    A hash where keys are the `ref` of a `Field` and values are the data stored for
    that field.
    """


from .field_value_param import FieldValueParam
