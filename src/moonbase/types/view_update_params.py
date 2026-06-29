# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .view_field_param import ViewFieldParam
from .view_aggregate_param import ViewAggregateParam

__all__ = ["ViewUpdateParams"]


class ViewUpdateParams(TypedDict, total=False):
    aggregates: Iterable[ViewAggregateParam]
    """The metrics computed over the view's items. An empty array clears them."""

    fields: Iterable[ViewFieldParam]
    """The view's columns, in display order.

    If provided, it must contain at least one column.
    """

    filter: Optional["ItemsFilterParam"]
    """Return only items that match the filter conditions.

    Complex filters can be created by nesting filters inside of `AND`, `OR`, and
    `NOT` filters.
    """

    groups: SequenceNotStr[str]
    """Fields whose values group the view's items. An empty array clears the grouping."""

    name: str
    """The name of the view."""

    relation_value_filters: Iterable["ViewRelationValueFilterParam"]
    """Filters limiting which related items the view's relation columns show.

    An empty array clears them.
    """

    sort: SequenceNotStr[str]
    """Sort items returned by the specified fields. An empty array clears the sort."""

    view_type: Literal["table", "board"]
    """The type of view, `table` or `board`."""


from .items_filter_param import ItemsFilterParam
from .view_relation_value_filter_param import ViewRelationValueFilterParam
