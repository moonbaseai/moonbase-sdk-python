# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .view_aggregate_item_count import ViewAggregateItemCount
from .view_aggregate_field_statistic import ViewAggregateFieldStatistic

__all__ = ["ViewAggregate"]

ViewAggregate: TypeAlias = Annotated[
    Union[ViewAggregateItemCount, ViewAggregateFieldStatistic], PropertyInfo(discriminator="type")
]
