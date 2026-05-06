# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .datetime_value_param import DatetimeValueParam
from .current_datetime_param import CurrentDatetimeParam

__all__ = ["DatetimeFieldDefaultValueParam"]

DatetimeFieldDefaultValueParam: TypeAlias = Union[DatetimeValueParam, CurrentDatetimeParam]
