# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .collection_pointer import CollectionPointer

__all__ = ["ViewListResponse"]


class ViewListResponse(BaseModel):
    id: str

    collection: CollectionPointer
    """
    A lightweight reference to a `Collection`, containing the minimal information
    needed to identify it.
    """

    created_at: datetime

    name: str

    type: Literal["view"]

    updated_at: datetime

    view_type: Literal["table", "board"]
