# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CurrentDate"]


class CurrentDate(BaseModel):
    """Resolves to today's date at the time the record is created."""

    type: Literal["current_date"]
