# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .current_member_param import CurrentMemberParam
from .relation_value_param import RelationValueParam

__all__ = ["RelationFieldDefaultValueParam"]

RelationFieldDefaultValueParam: TypeAlias = Union[RelationValueParam, CurrentMemberParam]
