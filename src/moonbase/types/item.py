# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["Item", "Links"]


class Links(BaseModel):
    collection: Optional[str] = None
    """A link to the `Collection` the item belongs to."""

    self: Optional[str] = None
    """The canonical URL for this object."""


class Item(BaseModel):
    id: str
    """Unique identifier for the object."""

    type: Literal["item"]
    """String representing the object’s type. Always `item` for this object."""

    links: Optional[Links] = None

    values: Optional[Dict[str, Optional["FieldValue"]]] = None
    """
    A hash where keys are the `ref` of a `Field` and values are the data stored for
    that field.
    """


from .field_value import FieldValue

if PYDANTIC_V2:
    Item.model_rebuild()
    Links.model_rebuild()
else:
    Item.update_forward_refs()  # type: ignore
    Links.update_forward_refs()  # type: ignore
