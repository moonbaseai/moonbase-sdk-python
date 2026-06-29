# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ViewAggregateFieldStatistic"]


class ViewAggregateFieldStatistic(BaseModel):
    """Computes a statistic over the values of a field."""

    statistic: Literal["count", "sum", "mean", "max", "min", "filled_percentage"]
    """The statistic to compute.

    Scalar statistics (sum, mean, max, min) require a number field as `value`.
    """

    type: Literal["field_statistic"]

    value: str
    """The field whose values the statistic is computed over."""

    group: Optional[str] = None
    """An optional field whose values bucket the statistic."""

    weight: Optional[str] = None
    """An optional percentage field used to weight the statistic.

    Only supported for scalar statistics.
    """
