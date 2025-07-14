# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PercentageValue"]


class PercentageValue(BaseModel):
    percentage: float

    type: Literal["value/number/percentage"]
