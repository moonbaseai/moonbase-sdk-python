# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .call_pointer import CallPointer
from .file_pointer import FilePointer
from .item_pointer import ItemPointer
from .note_pointer import NotePointer
from .meeting_pointer import MeetingPointer
from .message_pointer import MessagePointer
from .program_pointer import ProgramPointer
from .collection_pointer import CollectionPointer
from .unsubscribe_pointer import UnsubscribePointer
from .program_message_pointer import ProgramMessagePointer
from .program_template_pointer import ProgramTemplatePointer

__all__ = ["ConstituentEntityPointer"]

ConstituentEntityPointer: TypeAlias = Annotated[
    Union[
        CallPointer,
        CollectionPointer,
        ItemPointer,
        FilePointer,
        MeetingPointer,
        MessagePointer,
        NotePointer,
        ProgramPointer,
        ProgramMessagePointer,
        ProgramTemplatePointer,
        UnsubscribePointer,
    ],
    PropertyInfo(discriminator="type"),
]
