# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ViewAggregateFieldStatisticParam"]


class ViewAggregateFieldStatisticParam(TypedDict, total=False):
    """Computes a statistic over the values of a field."""

    statistic: Required[Literal["count", "sum", "mean", "max", "min", "filled_percentage"]]
    """The statistic to compute.

    Scalar statistics (sum, mean, max, min) require a number field as `value`.
    """

    type: Required[Literal["field_statistic"]]

    value: Required[str]
    """The field whose values the statistic is computed over."""

    group: str
    """An optional field whose values bucket the statistic."""

    weight: str
    """An optional percentage field used to weight the statistic.

    Only supported for scalar statistics.
    """
