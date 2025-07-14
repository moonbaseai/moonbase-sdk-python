# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonetaryValue", "Amount"]


class Amount(BaseModel):
    amount_in_minor_units: int

    currency: str

    type: Literal["currency"]


class MonetaryValue(BaseModel):
    amount: Amount

    type: Literal["value/number/monetary"]
