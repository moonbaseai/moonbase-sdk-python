# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .call_pointer import CallPointer
from .item_pointer import ItemPointer
from .meeting_pointer import MeetingPointer

__all__ = ["NoteAssociationPointer"]

NoteAssociationPointer: TypeAlias = Annotated[
    Union[CallPointer, ItemPointer, MeetingPointer], PropertyInfo(discriminator="type")
]
