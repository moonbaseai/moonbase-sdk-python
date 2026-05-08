# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .funnel_step import FunnelStep

__all__ = ["Funnel"]


class Funnel(BaseModel):
    """A Funnel represents a series of steps used to track progression."""

    id: str
    """Unique identifier for the object."""

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    name: str
    """The name of the funnel."""

    steps: List[FunnelStep]
    """An ordered list of `FunnelStep` objects that make up the funnel."""

    type: Literal["funnel"]
    """String representing the object’s type. Always `funnel` for this object."""

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""
