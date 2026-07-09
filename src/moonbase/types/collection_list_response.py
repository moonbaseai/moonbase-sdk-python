# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CollectionListResponse"]


class CollectionListResponse(BaseModel):
    """
    Information about the most essential attributes of a Collection (does not include the collection's field definitions).
    """

    id: str

    created_at: datetime

    kind: Literal["system", "form", "custom"]

    name: str

    ref: str

    type: Literal["collection"]

    updated_at: datetime

    description: Optional[str] = None

    icon_name: Optional[str] = None
