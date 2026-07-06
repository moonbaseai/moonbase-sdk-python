# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .collection_pointer import CollectionPointer

__all__ = ["FormListResponse"]


class FormListResponse(BaseModel):
    """
    Information about the most essential attributes of a Form (does not include the embed HTML).
    """

    id: str

    business_email_required: bool

    collection: CollectionPointer
    """
    A lightweight reference to a `Collection`, containing the minimal information
    needed to identify it.
    """

    created_at: datetime

    name: str

    pages_enabled: bool

    type: Literal["form"]

    updated_at: datetime

    pages_url: Optional[str] = None

    redirect_url: Optional[str] = None
