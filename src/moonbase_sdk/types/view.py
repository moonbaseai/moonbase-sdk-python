# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["View", "Links"]


class Links(BaseModel):
    collection: str
    """A link to the `Collection` this view belongs to."""

    items: str
    """A link to the list of `Item` objects that are visible in this view."""

    self: str
    """The canonical URL for this object."""


class View(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: Links

    name: str
    """The name of the view."""

    type: Literal["view"]
    """String representing the object’s type. Always `view` for this object."""

    collection: Optional["Collection"] = None
    """The `Collection` this view belongs to."""

    view_type: Optional[Literal["table", "board"]] = None
    """The type of view, such as `table` or `board`."""


from .collection import Collection

if PYDANTIC_V2:
    View.model_rebuild()
    Links.model_rebuild()
else:
    View.update_forward_refs()  # type: ignore
    Links.update_forward_refs()  # type: ignore
