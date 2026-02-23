# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .items_filter_value_exists_param import ItemsFilterValueExistsParam
from .items_filter_value_matches_param import ItemsFilterValueMatchesParam

__all__ = ["ItemsFilterParam"]

if TYPE_CHECKING or not PYDANTIC_V1:
    ItemsFilterParam = TypeAliasType(
        "ItemsFilterParam",
        Union[
            ItemsFilterValueMatchesParam,
            ItemsFilterValueExistsParam,
            "ItemsFilterAndGroupParam",
            "ItemsFilterOrGroupParam",
            "ItemsFilterNotGroupParam",
        ],
    )
else:
    ItemsFilterParam: TypeAlias = Union[
        ItemsFilterValueMatchesParam,
        ItemsFilterValueExistsParam,
        "ItemsFilterAndGroupParam",
        "ItemsFilterOrGroupParam",
        "ItemsFilterNotGroupParam",
    ]

from .items_filter_or_group_param import ItemsFilterOrGroupParam
from .items_filter_and_group_param import ItemsFilterAndGroupParam
from .items_filter_not_group_param import ItemsFilterNotGroupParam
