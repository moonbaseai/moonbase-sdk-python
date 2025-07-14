# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .call import Call
from .note import Note
from .._utils import PropertyInfo
from .address import Address
from .meeting import Meeting
from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .attendee import Attendee
from .organizer import Organizer
from .email_message import EmailMessage

__all__ = [
    "Activity",
    "CallOccurredActivity",
    "CallOccurredActivityLinks",
    "FormSubmittedActivity",
    "FormSubmittedActivityLinks",
    "InboxMessageSentActivity",
    "InboxMessageSentActivityLinks",
    "ItemCreatedActivity",
    "ItemCreatedActivityLinks",
    "ItemMentionedActivity",
    "ItemMentionedActivityLinks",
    "MeetingHeldActivity",
    "MeetingHeldActivityLinks",
    "MeetingScheduledActivity",
    "MeetingScheduledActivityLinks",
    "NoteCreatedActivity",
    "NoteCreatedActivityLinks",
    "ProgramMessageBouncedActivity",
    "ProgramMessageBouncedActivityLinks",
    "ProgramMessageClickedActivity",
    "ProgramMessageClickedActivityLinks",
    "ProgramMessageComplainedActivity",
    "ProgramMessageComplainedActivityLinks",
    "ProgramMessageFailedActivity",
    "ProgramMessageFailedActivityLinks",
    "ProgramMessageOpenedActivity",
    "ProgramMessageOpenedActivityLinks",
    "ProgramMessageSentActivity",
    "ProgramMessageSentActivityLinks",
    "ProgramMessageShieldedActivity",
    "ProgramMessageShieldedActivityLinks",
    "ProgramMessageUnsubscribedActivity",
    "ProgramMessageUnsubscribedActivityLinks",
]


class CallOccurredActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class CallOccurredActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: CallOccurredActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/call_occurred"]
    """The type of activity. Always `activity/call_occurred`."""

    call: Optional[Call] = None
    """The `Call` object associated with this event."""


class FormSubmittedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    collection: Optional[str] = None
    """A link to the `Collection` associated with the form."""

    item: Optional[str] = None
    """A link to the `Item` created by the form submission."""


class FormSubmittedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: FormSubmittedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/form_submitted"]
    """The type of activity. Always `activity/form_submitted`."""

    collection: Optional["Collection"] = None
    """The `Collection` the new item was added to."""

    item: Optional["Item"] = None
    """The `Item` that was created by the form submission."""


class InboxMessageSentActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    message: Optional[str] = None
    """A link to the `EmailMessage` that was sent."""


class InboxMessageSentActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: InboxMessageSentActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/inbox_message_sent"]
    """The type of activity. Always `activity/inbox_message_sent`."""

    message: Optional[EmailMessage] = None
    """The `EmailMessage` that was sent."""

    recipients: Optional[List[Address]] = None
    """A list of `Address` objects for the recipients."""

    sender: Optional[Address] = None
    """The `Address` of the sender."""


class ItemCreatedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    collection: Optional[str] = None
    """A link to the `Collection` the item belongs to."""

    item: Optional[str] = None
    """A link to the `Item` that was created."""


class ItemCreatedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ItemCreatedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/item_created"]
    """The type of activity. Always `activity/item_created`."""

    collection: Optional["Collection"] = None
    """The `Collection` the item was added to."""

    item: Optional["Item"] = None
    """The `Item` that was created."""


class ItemMentionedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    collection: Optional[str] = None
    """A link to the `Collection` the item belongs to."""

    item: Optional[str] = None
    """A link to the `Item` that was mentioned."""


class ItemMentionedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ItemMentionedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/item_mentioned"]
    """The type of activity. Always `activity/item_mentioned`."""

    collection: Optional["Collection"] = None
    """The `Collection` the item belongs to."""

    item: Optional["Item"] = None
    """The `Item` that was mentioned."""


class MeetingHeldActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    meeting: Optional[str] = None
    """A link to the `Meeting` that was held."""


class MeetingHeldActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: MeetingHeldActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/meeting_held"]
    """The type of activity. Always `activity/meeting_held`."""

    attendees: Optional[List[Attendee]] = None
    """A list of `Attendee` objects who were part of the meeting."""

    meeting: Optional[Meeting] = None
    """The `Meeting` object associated with this event."""


class MeetingScheduledActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    meeting: Optional[str] = None
    """A link to the `Meeting` that was scheduled."""


class MeetingScheduledActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: MeetingScheduledActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/meeting_scheduled"]
    """The type of activity. Always `activity/meeting_scheduled`."""

    attendees: Optional[List[Attendee]] = None
    """The list of `Attendee` objects invited to the meeting."""

    meeting: Optional[Meeting] = None
    """The `Meeting` object associated with this event."""

    organizer: Optional[Organizer] = None
    """The `Organizer` of the meeting."""


class NoteCreatedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    note: Optional[str] = None
    """A link to the `Note` that was created."""

    related_item: Optional[str] = None
    """A link to the related `Item`."""

    related_meeting: Optional[str] = None
    """A link to the related `Meeting`."""


class NoteCreatedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: NoteCreatedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/note_created"]
    """The type of activity. Always `activity/note_created`."""

    note: Optional[Note] = None
    """The `Note` object that was created."""

    related_item: Optional["Item"] = None
    """The `Item` this note is related to, if any."""

    related_meeting: Optional[Meeting] = None
    """The `Meeting` this note is related to, if any."""


class ProgramMessageBouncedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class ProgramMessageBouncedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageBouncedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_bounced"]
    """The type of activity. Always `activity/program_message_bounced`."""

    recipient: Optional[Address] = None
    """The `Address` of the recipient whose message bounced."""


class ProgramMessageClickedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class ProgramMessageClickedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageClickedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_clicked"]
    """The type of activity. Always `activity/program_message_clicked`."""

    link_text: Optional[str] = None
    """The text of the link that was clicked."""

    link_url_unsafe: Optional[str] = None
    """The URL of the link that was clicked."""

    recipient: Optional[Address] = None
    """The `Address` of the recipient who clicked the link."""


class ProgramMessageComplainedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class ProgramMessageComplainedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageComplainedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_complained"]
    """The type of activity. Always `activity/program_message_complained`."""

    recipient: Optional[Address] = None
    """The `Address` of the recipient who complained."""


class ProgramMessageFailedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class ProgramMessageFailedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageFailedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_failed"]
    """The type of activity. Always `activity/program_message_failed`."""

    recipient: Optional[Address] = None
    """The `Address` of the recipient whose message failed."""


class ProgramMessageOpenedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class ProgramMessageOpenedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageOpenedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_opened"]
    """The type of activity. Always `activity/program_message_opened`."""

    recipient: Optional[Address] = None
    """The `Address` of the recipient who opened the message."""


class ProgramMessageSentActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class ProgramMessageSentActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageSentActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_sent"]
    """The type of activity. Always `activity/program_message_sent`."""

    recipient: Optional[Address] = None
    """The `Address` of the recipient the message was sent to."""


class ProgramMessageShieldedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class ProgramMessageShieldedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageShieldedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_shielded"]
    """The type of activity. Always `activity/program_message_shielded`."""

    recipient: Optional[Address] = None
    """The `Address` of the recipient whose message was shielded."""


class ProgramMessageUnsubscribedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class ProgramMessageUnsubscribedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageUnsubscribedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_unsubscribed"]
    """The type of activity. Always `activity/program_message_unsubscribed`."""

    recipient: Optional[Address] = None
    """The `Address` of the recipient who unsubscribed."""


Activity: TypeAlias = Annotated[
    Union[
        CallOccurredActivity,
        FormSubmittedActivity,
        InboxMessageSentActivity,
        ItemCreatedActivity,
        ItemMentionedActivity,
        MeetingHeldActivity,
        MeetingScheduledActivity,
        NoteCreatedActivity,
        ProgramMessageBouncedActivity,
        ProgramMessageClickedActivity,
        ProgramMessageComplainedActivity,
        ProgramMessageFailedActivity,
        ProgramMessageOpenedActivity,
        ProgramMessageSentActivity,
        ProgramMessageShieldedActivity,
        ProgramMessageUnsubscribedActivity,
    ],
    PropertyInfo(discriminator="type"),
]

from .item import Item
from .collection import Collection

if PYDANTIC_V2:
    CallOccurredActivity.model_rebuild()
    CallOccurredActivityLinks.model_rebuild()
    FormSubmittedActivity.model_rebuild()
    FormSubmittedActivityLinks.model_rebuild()
    InboxMessageSentActivity.model_rebuild()
    InboxMessageSentActivityLinks.model_rebuild()
    ItemCreatedActivity.model_rebuild()
    ItemCreatedActivityLinks.model_rebuild()
    ItemMentionedActivity.model_rebuild()
    ItemMentionedActivityLinks.model_rebuild()
    MeetingHeldActivity.model_rebuild()
    MeetingHeldActivityLinks.model_rebuild()
    MeetingScheduledActivity.model_rebuild()
    MeetingScheduledActivityLinks.model_rebuild()
    NoteCreatedActivity.model_rebuild()
    NoteCreatedActivityLinks.model_rebuild()
    ProgramMessageBouncedActivity.model_rebuild()
    ProgramMessageBouncedActivityLinks.model_rebuild()
    ProgramMessageClickedActivity.model_rebuild()
    ProgramMessageClickedActivityLinks.model_rebuild()
    ProgramMessageComplainedActivity.model_rebuild()
    ProgramMessageComplainedActivityLinks.model_rebuild()
    ProgramMessageFailedActivity.model_rebuild()
    ProgramMessageFailedActivityLinks.model_rebuild()
    ProgramMessageOpenedActivity.model_rebuild()
    ProgramMessageOpenedActivityLinks.model_rebuild()
    ProgramMessageSentActivity.model_rebuild()
    ProgramMessageSentActivityLinks.model_rebuild()
    ProgramMessageShieldedActivity.model_rebuild()
    ProgramMessageShieldedActivityLinks.model_rebuild()
    ProgramMessageUnsubscribedActivity.model_rebuild()
    ProgramMessageUnsubscribedActivityLinks.model_rebuild()
else:
    CallOccurredActivity.update_forward_refs()  # type: ignore
    CallOccurredActivityLinks.update_forward_refs()  # type: ignore
    FormSubmittedActivity.update_forward_refs()  # type: ignore
    FormSubmittedActivityLinks.update_forward_refs()  # type: ignore
    InboxMessageSentActivity.update_forward_refs()  # type: ignore
    InboxMessageSentActivityLinks.update_forward_refs()  # type: ignore
    ItemCreatedActivity.update_forward_refs()  # type: ignore
    ItemCreatedActivityLinks.update_forward_refs()  # type: ignore
    ItemMentionedActivity.update_forward_refs()  # type: ignore
    ItemMentionedActivityLinks.update_forward_refs()  # type: ignore
    MeetingHeldActivity.update_forward_refs()  # type: ignore
    MeetingHeldActivityLinks.update_forward_refs()  # type: ignore
    MeetingScheduledActivity.update_forward_refs()  # type: ignore
    MeetingScheduledActivityLinks.update_forward_refs()  # type: ignore
    NoteCreatedActivity.update_forward_refs()  # type: ignore
    NoteCreatedActivityLinks.update_forward_refs()  # type: ignore
    ProgramMessageBouncedActivity.update_forward_refs()  # type: ignore
    ProgramMessageBouncedActivityLinks.update_forward_refs()  # type: ignore
    ProgramMessageClickedActivity.update_forward_refs()  # type: ignore
    ProgramMessageClickedActivityLinks.update_forward_refs()  # type: ignore
    ProgramMessageComplainedActivity.update_forward_refs()  # type: ignore
    ProgramMessageComplainedActivityLinks.update_forward_refs()  # type: ignore
    ProgramMessageFailedActivity.update_forward_refs()  # type: ignore
    ProgramMessageFailedActivityLinks.update_forward_refs()  # type: ignore
    ProgramMessageOpenedActivity.update_forward_refs()  # type: ignore
    ProgramMessageOpenedActivityLinks.update_forward_refs()  # type: ignore
    ProgramMessageSentActivity.update_forward_refs()  # type: ignore
    ProgramMessageSentActivityLinks.update_forward_refs()  # type: ignore
    ProgramMessageShieldedActivity.update_forward_refs()  # type: ignore
    ProgramMessageShieldedActivityLinks.update_forward_refs()  # type: ignore
    ProgramMessageUnsubscribedActivity.update_forward_refs()  # type: ignore
    ProgramMessageUnsubscribedActivityLinks.update_forward_refs()  # type: ignore
