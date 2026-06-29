# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .items_filter_value_exists import ItemsFilterValueExists
from .items_filter_value_matches import ItemsFilterValueMatches

__all__ = ["ItemsFilter"]

if TYPE_CHECKING or not PYDANTIC_V1:
    ItemsFilter = TypeAliasType(
        "ItemsFilter",
        Union[
            ItemsFilterValueMatches,
            ItemsFilterValueExists,
            "ItemsFilterAndGroup",
            "ItemsFilterOrGroup",
            "ItemsFilterNotGroup",
        ],
    )
else:
    ItemsFilter: TypeAlias = Union[
        ItemsFilterValueMatches,
        ItemsFilterValueExists,
        "ItemsFilterAndGroup",
        "ItemsFilterOrGroup",
        "ItemsFilterNotGroup",
    ]

from .items_filter_or_group import ItemsFilterOrGroup
from .items_filter_and_group import ItemsFilterAndGroup
from .items_filter_not_group import ItemsFilterNotGroup
