# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..item import Item
from ..._models import BaseModel

__all__ = ["ItemSearchResponse"]


class ItemSearchResponse(BaseModel):
    """A collection search result entry containing an item."""

    data: Item
    """An Item represents a single record or row within a Collection.

    It holds a set of `values` corresponding to the Collection's `fields`.
    """

    type: Literal["search_result"]
