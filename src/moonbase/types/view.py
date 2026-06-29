# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .view_field import ViewField
from .view_aggregate import ViewAggregate
from .collection_pointer import CollectionPointer

__all__ = ["View"]


class View(BaseModel):
    """
    A View represents a saved configuration for displaying items in a collection, including filters and sorting rules.
    """

    id: str
    """Unique identifier for the object."""

    aggregates: List[ViewAggregate]
    """The metrics computed over the view's items."""

    collection: CollectionPointer
    """The `Collection` this view belongs to."""

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    fields: List[ViewField]
    """The view's columns, in display order."""

    filter: Optional["ItemsFilter"] = None
    """Return only items that match the filter conditions.

    Complex filters can be created by nesting filters inside of `AND`, `OR`, and
    `NOT` filters.
    """

    groups: List[str]
    """Fields whose values group the view's items. Empty when the view is not grouped."""

    name: str
    """The name of the view."""

    relation_value_filters: List["ViewRelationValueFilter"]
    """Filters limiting which related items the view's relation columns show."""

    sort: List[str]
    """Sort items returned by the specified fields. Empty when the view has no sort."""

    type: Literal["view"]
    """String representing the object’s type. Always `view` for this object."""

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""

    view_type: Literal["table", "board"]
    """The type of view, such as `table` or `board`."""


from .items_filter import ItemsFilter
from .view_relation_value_filter import ViewRelationValueFilter
