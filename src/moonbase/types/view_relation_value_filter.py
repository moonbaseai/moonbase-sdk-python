# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["ViewRelationValueFilter"]


class ViewRelationValueFilter(BaseModel):
    """
    Limits which related items a relation column shows: only related items matching `filter` appear.
    """

    field: str
    """The relation column whose related items are filtered."""

    filter: "ItemsFilter"
    """The filter the related items must match.

    Field paths are relative to the related collection.
    """


from .items_filter import ItemsFilter
