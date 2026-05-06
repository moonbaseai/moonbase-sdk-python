# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CurrentDatetime"]


class CurrentDatetime(BaseModel):
    """Resolves to the current date and time at the time the record is created."""

    type: Literal["current_datetime"]
