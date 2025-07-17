# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["Item", "Links"]


class Links(BaseModel):
    collection: Optional[str] = None
    """A link to the `Collection` the item belongs to."""

    self: Optional[str] = None
    """The canonical URL for this object."""

if TYPE_CHECKING:
    from .field_value import FieldValue


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


# Import these to ensure they're available when forward refs are resolved
from .value import Value
from .field_value import FieldValue

# Now rebuild/update forward refs
if PYDANTIC_V2:
    # For Pydantic v2, we need to rebuild both models
    from . import relation_value

    relation_value.RelationValue.model_rebuild()
    Item.model_rebuild()
    Links.model_rebuild()
else:
    # For Pydantic v1, update forward refs with the proper namespace
    from . import relation_value

    relation_value.RelationValue.update_forward_refs(Item=Item)  # type: ignore
    Item.update_forward_refs(FieldValue=FieldValue, Value=Value, RelationValue=relation_value.RelationValue)  # type: ignore
    Links.update_forward_refs()  # type: ignore
