# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TelephoneNumber"]


class TelephoneNumber(BaseModel):
    telephone_number: str

    type: Literal["value/telephone_number"]
