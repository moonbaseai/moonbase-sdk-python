# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .item import Item
from .._models import BaseModel

__all__ = ["SearchResponse", "Data"]


class Data(BaseModel):
    """A search result entry"""

    data: Item
    """An Item represents a single record or row within a Collection.

    It holds a set of `values` corresponding to the Collection's `fields`.
    """


class SearchResponse(BaseModel):
    """A list of search results."""

    data: List[Data]

    type: Literal["list"]
