# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .view_aggregate_item_count_param import ViewAggregateItemCountParam
from .view_aggregate_field_statistic_param import ViewAggregateFieldStatisticParam

__all__ = ["ViewAggregateParam"]

ViewAggregateParam: TypeAlias = Union[ViewAggregateItemCountParam, ViewAggregateFieldStatisticParam]
