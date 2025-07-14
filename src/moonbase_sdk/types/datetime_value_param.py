# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime as _datetime
from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatetimeValueParam"]


class DatetimeValueParam(TypedDict, total=False):
    datetime: Required[Annotated[Union[str, _datetime.datetime], PropertyInfo(format="iso8601")]]

    type: Required[Literal["value/datetime"]]
