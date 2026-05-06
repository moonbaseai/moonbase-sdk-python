# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .date_value_param import DateValueParam
from .current_date_param import CurrentDateParam

__all__ = ["DateFieldDefaultValueParam"]

DateFieldDefaultValueParam: TypeAlias = Union[DateValueParam, CurrentDateParam]
