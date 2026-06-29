# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ViewAggregateItemCount"]


class ViewAggregateItemCount(BaseModel):
    """Counts the view's items."""

    type: Literal["item_count"]

    group: Optional[str] = None
    """An optional field whose values bucket the counts."""
