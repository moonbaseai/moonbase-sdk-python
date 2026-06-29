# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ViewRelationValueFilterParam"]


class ViewRelationValueFilterParam(TypedDict, total=False):
    """
    Limits which related items a relation column shows: only related items matching `filter` appear.
    """

    field: Required[str]
    """The relation column whose related items are filtered."""

    filter: Required["ItemsFilterParam"]
    """The filter the related items must match.

    Field paths are relative to the related collection.
    """


from .items_filter_param import ItemsFilterParam
