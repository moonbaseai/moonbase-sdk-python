# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DateValue"]


class DateValue(BaseModel):
    date: datetime.date

    type: Literal["value/date"]
