# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .item import Item
from .._models import BaseModel

__all__ = ["ItemSearchResponse"]


class ItemSearchResponse(BaseModel):
    data: List[Item]

    type: Literal["list"]
