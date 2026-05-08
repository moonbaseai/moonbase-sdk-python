# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from .item import Item
from .._utils import PropertyInfo
from .._models import BaseModel
from .moonbase_file import MoonbaseFile

__all__ = ["SearchResponse", "Data", "DataData"]

DataData: TypeAlias = Annotated[Union[Item, MoonbaseFile], PropertyInfo(discriminator="type")]


class Data(BaseModel):
    """A search result entry."""

    data: DataData
    """An Item represents a single record or row within a Collection.

    It holds a set of `values` corresponding to the Collection's `fields`.
    """

    type: Literal["search_result"]


class SearchResponse(BaseModel):
    """A list of search results."""

    data: List[Data]

    type: Literal["list"]
