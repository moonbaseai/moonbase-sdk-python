# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .view_field_param import ViewFieldParam
from .view_aggregate_param import ViewAggregateParam

__all__ = ["ViewCreateParams", "Collection"]


class ViewCreateParams(TypedDict, total=False):
    collection: Required[Collection]
    """A pointer to the `Collection` the view belongs to."""

    fields: Required[Iterable[ViewFieldParam]]
    """The view's columns, in display order."""

    name: Required[str]
    """The name of the view."""

    view_type: Required[Literal["table", "board"]]
    """The type of view, `table` or `board`."""

    aggregates: Iterable[ViewAggregateParam]
    """The metrics computed over the view's items."""

    filter: "ItemsFilterParam"
    """The filter applied to the view's items."""

    groups: SequenceNotStr[str]
    """Fields whose values group the view's items."""

    relation_value_filters: Iterable["ViewRelationValueFilterParam"]
    """Filters limiting which related items the view's relation columns show."""

    sort: SequenceNotStr[str]
    """Sort items returned by the specified fields."""


class Collection(TypedDict, total=False):
    """A pointer to the `Collection` the view belongs to."""

    type: Required[Literal["collection"]]
    """String representing the object’s type. Always `collection` for this object."""

    id: str
    """Unique identifier of the collection."""

    ref: str
    """The stable, machine-readable reference identifier of the collection."""


from .items_filter_param import ItemsFilterParam  # noqa: I001
from .view_relation_value_filter_param import ViewRelationValueFilterParam
from .items_filter_and_group_param import ItemsFilterAndGroupParam  # noqa: F401 # pyright: ignore [reportUnusedImport]
from .items_filter_not_group_param import ItemsFilterNotGroupParam  # noqa: F401 # pyright: ignore [reportUnusedImport]
from .items_filter_or_group_param import ItemsFilterOrGroupParam  # noqa: F401 # pyright: ignore [reportUnusedImport]
