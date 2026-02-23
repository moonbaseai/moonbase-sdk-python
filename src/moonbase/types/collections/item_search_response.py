# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..item import Item
from ..._models import BaseModel

__all__ = ["ItemSearchResponse"]


class ItemSearchResponse(BaseModel):
    """A search result entry"""

    data: Item
    """An Item represents a single record or row within a Collection.

    It holds a set of `values` corresponding to the Collection's `fields`.
    """
