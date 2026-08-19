# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemsFilterValueMatchesParam"]


class ItemsFilterValueMatchesParam(TypedDict, total=False):
    """
    Include only items with a value in the given `field` that satisfies the `op` condition.
    """

    field: Required[str]
    """
    The id or key of the field in which values are matched, or a path to the field
    in which values are matched.
    """

    op: Required[
        Literal["starts_with", "ends_with", "contains", "not_contains", "eq", "not_eq", "gt", "lt", "gte", "lte"]
    ]
    """The matching operator for this filter."""

    value: Required[Union[str, float, bool]]
    """The value to match against.

    Use ISO8601 format for dates and datetime fields. For date fields, the time
    portion of the date-time will be ignored. For currency fields, the amount should
    be in the smallest unit of currency (eg: cents for USD).
    """
