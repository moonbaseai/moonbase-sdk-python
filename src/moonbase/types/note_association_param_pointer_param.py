# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .call_pointer_param import CallPointerParam
from .item_pointer_param import ItemPointerParam
from .meeting_pointer_param import MeetingPointerParam

__all__ = ["NoteAssociationParamPointerParam"]

NoteAssociationParamPointerParam: TypeAlias = Union[CallPointerParam, ItemPointerParam, MeetingPointerParam]
