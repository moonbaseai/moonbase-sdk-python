# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime as _datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DatetimeValue"]


class DatetimeValue(BaseModel):
    datetime: _datetime.datetime

    type: Literal["value/datetime"]
