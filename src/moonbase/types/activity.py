# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "Activity",
    "CallOccurredActivity",
    "CallOccurredActivityLinks",
    "CallOccurredActivityCall",
    "FormSubmittedActivity",
    "FormSubmittedActivityLinks",
    "FormSubmittedActivityCollection",
    "FormSubmittedActivityRelatedItem",
    "InboxMessageSentActivity",
    "InboxMessageSentActivityLinks",
    "InboxMessageSentActivityMessage",
    "ItemCreatedActivity",
    "ItemCreatedActivityLinks",
    "ItemCreatedActivityCollection",
    "ItemCreatedActivityCreatedItem",
    "ItemMentionedActivity",
    "ItemMentionedActivityLinks",
    "ItemMentionedActivityAuthor",
    "ItemMentionedActivityMentionedItem",
    "ItemMentionedActivityNote",
    "ItemMergedActivity",
    "ItemMergedActivityLinks",
    "ItemMergedActivityDestination",
    "ItemMergedActivityInitiator",
    "ItemMergedActivitySource",
    "MeetingHeldActivity",
    "MeetingHeldActivityLinks",
    "MeetingHeldActivityMeeting",
    "MeetingScheduledActivity",
    "MeetingScheduledActivityLinks",
    "MeetingScheduledActivityMeeting",
    "NoteCreatedActivity",
    "NoteCreatedActivityLinks",
    "NoteCreatedActivityNote",
    "NoteCreatedActivityRelatedItem",
    "NoteCreatedActivityRelatedMeeting",
    "ProgramMessageBouncedActivity",
    "ProgramMessageBouncedActivityLinks",
    "ProgramMessageBouncedActivityProgramMessage",
    "ProgramMessageBouncedActivityRecipient",
    "ProgramMessageClickedActivity",
    "ProgramMessageClickedActivityLinks",
    "ProgramMessageClickedActivityProgramMessage",
    "ProgramMessageClickedActivityRecipient",
    "ProgramMessageComplainedActivity",
    "ProgramMessageComplainedActivityLinks",
    "ProgramMessageComplainedActivityProgramMessage",
    "ProgramMessageComplainedActivityRecipient",
    "ProgramMessageFailedActivity",
    "ProgramMessageFailedActivityLinks",
    "ProgramMessageFailedActivityProgramMessage",
    "ProgramMessageFailedActivityRecipient",
    "ProgramMessageOpenedActivity",
    "ProgramMessageOpenedActivityLinks",
    "ProgramMessageOpenedActivityProgramMessage",
    "ProgramMessageOpenedActivityRecipient",
    "ProgramMessageSentActivity",
    "ProgramMessageSentActivityLinks",
    "ProgramMessageSentActivityProgramMessage",
    "ProgramMessageSentActivityRecipient",
    "ProgramMessageShieldedActivity",
    "ProgramMessageShieldedActivityLinks",
    "ProgramMessageShieldedActivityProgramMessage",
    "ProgramMessageShieldedActivityRecipient",
    "ProgramMessageUnsubscribedActivity",
    "ProgramMessageUnsubscribedActivityLinks",
    "ProgramMessageUnsubscribedActivityProgramMessage",
    "ProgramMessageUnsubscribedActivityRecipient",
]


class CallOccurredActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""


class CallOccurredActivityCall(BaseModel):
    id: str

    type: str


class CallOccurredActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: CallOccurredActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/call_occurred"]
    """The type of activity. Always `activity/call_occurred`."""

    call: Optional[CallOccurredActivityCall] = None
    """The `Call` object associated with this event."""


class FormSubmittedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    collection: Optional[str] = None
    """A link to the `Collection` associated with the form."""

    item: Optional[str] = None
    """A link to the `Item` created by the form submission."""


class FormSubmittedActivityCollection(BaseModel):
    id: str

    type: str


class FormSubmittedActivityRelatedItem(BaseModel):
    id: str

    type: str


class FormSubmittedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: FormSubmittedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/form_submitted"]
    """The type of activity. Always `activity/form_submitted`."""

    collection: Optional[FormSubmittedActivityCollection] = None
    """The `Collection` the new item was added to."""

    related_item: Optional[FormSubmittedActivityRelatedItem] = None


class InboxMessageSentActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    message: Optional[str] = None
    """A link to the `EmailMessage` that was sent."""


class InboxMessageSentActivityMessage(BaseModel):
    id: str

    type: str


class InboxMessageSentActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: InboxMessageSentActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/inbox_message_sent"]
    """The type of activity. Always `activity/inbox_message_sent`."""

    message: Optional[InboxMessageSentActivityMessage] = None
    """The `EmailMessage` that was sent."""


class ItemCreatedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    collection: Optional[str] = None
    """A link to the `Collection` the item belongs to."""

    item: Optional[str] = None
    """A link to the `Item` that was created."""


class ItemCreatedActivityCollection(BaseModel):
    id: str

    type: str


class ItemCreatedActivityCreatedItem(BaseModel):
    id: str

    type: str


class ItemCreatedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ItemCreatedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/item_created"]
    """The type of activity. Always `activity/item_created`."""

    collection: Optional[ItemCreatedActivityCollection] = None
    """The `Collection` the item was added to."""

    created_item: Optional[ItemCreatedActivityCreatedItem] = None


class ItemMentionedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    author: Optional[str] = None
    """A link to the `Person` who mentioned the item."""

    item: Optional[str] = None
    """A link to the `Item` that was mentioned."""

    note: Optional[str] = None
    """A link to the `Note` where the item was mentioned."""


class ItemMentionedActivityAuthor(BaseModel):
    id: str

    type: str


class ItemMentionedActivityMentionedItem(BaseModel):
    id: str

    type: str


class ItemMentionedActivityNote(BaseModel):
    id: str

    type: str


class ItemMentionedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ItemMentionedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/item_mentioned"]
    """The type of activity. Always `activity/item_mentioned`."""

    author: Optional[ItemMentionedActivityAuthor] = None

    mentioned_item: Optional[ItemMentionedActivityMentionedItem] = None

    note: Optional[ItemMentionedActivityNote] = None


class ItemMergedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    destination: Optional[str] = None
    """A link to the `Item` that received the data from the source."""

    initiator: Optional[str] = None
    """A link to the person that performed the merge."""


class ItemMergedActivityDestination(BaseModel):
    id: str

    type: str


class ItemMergedActivityInitiator(BaseModel):
    id: str

    type: str


class ItemMergedActivitySource(BaseModel):
    id: str

    type: str


class ItemMergedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ItemMergedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/item_merged"]
    """The type of activity. Always `activity/item_merged`."""

    destination: Optional[ItemMergedActivityDestination] = None
    """A pointer to the `Item` that the data was merged into."""

    initiator: Optional[ItemMergedActivityInitiator] = None
    """The person that performed the merge."""

    source: Optional[ItemMergedActivitySource] = None
    """A pointer to the source `Item`."""


class MeetingHeldActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    meeting: Optional[str] = None
    """A link to the `Meeting` that was held."""


class MeetingHeldActivityMeeting(BaseModel):
    id: str

    type: str


class MeetingHeldActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: MeetingHeldActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/meeting_held"]
    """The type of activity. Always `activity/meeting_held`."""

    meeting: Optional[MeetingHeldActivityMeeting] = None
    """The `Meeting` object associated with this event."""


class MeetingScheduledActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    meeting: Optional[str] = None
    """A link to the `Meeting` that was scheduled."""


class MeetingScheduledActivityMeeting(BaseModel):
    id: str

    type: str


class MeetingScheduledActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: MeetingScheduledActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/meeting_scheduled"]
    """The type of activity. Always `activity/meeting_scheduled`."""

    meeting: Optional[MeetingScheduledActivityMeeting] = None
    """The `Meeting` object associated with this event."""


class NoteCreatedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    note: Optional[str] = None
    """A link to the `Note` that was created."""

    related_item: Optional[str] = None
    """A link to the related `Item`."""

    related_meeting: Optional[str] = None
    """A link to the related `Meeting`."""


class NoteCreatedActivityNote(BaseModel):
    id: str

    type: str


class NoteCreatedActivityRelatedItem(BaseModel):
    id: str

    type: str


class NoteCreatedActivityRelatedMeeting(BaseModel):
    id: str

    type: str


class NoteCreatedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: NoteCreatedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/note_created"]
    """The type of activity. Always `activity/note_created`."""

    note: Optional[NoteCreatedActivityNote] = None
    """The `Note` object that was created."""

    related_item: Optional[NoteCreatedActivityRelatedItem] = None
    """The `Item` this note is related to, if any."""

    related_meeting: Optional[NoteCreatedActivityRelatedMeeting] = None
    """The `Meeting` this note is related to, if any."""


class ProgramMessageBouncedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    recipient: Optional[str] = None
    """A link to the `Address` of the recipient whose message bounced."""


class ProgramMessageBouncedActivityProgramMessage(BaseModel):
    id: str

    type: str


class ProgramMessageBouncedActivityRecipient(BaseModel):
    id: str

    type: str


class ProgramMessageBouncedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageBouncedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_bounced"]
    """The type of activity. Always `activity/program_message_bounced`."""

    bounce_type: Optional[str] = None

    bounced_recipient_emails: Optional[List[str]] = None

    program_message: Optional[ProgramMessageBouncedActivityProgramMessage] = None

    recipient: Optional[ProgramMessageBouncedActivityRecipient] = None
    """A link to the `Address` of the recipient whose message bounced."""


class ProgramMessageClickedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    recipient: Optional[str] = None
    """A link to the `Address` of the recipient who clicked the link."""


class ProgramMessageClickedActivityProgramMessage(BaseModel):
    id: str

    type: str


class ProgramMessageClickedActivityRecipient(BaseModel):
    id: str

    type: str


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

    program_message: Optional[ProgramMessageClickedActivityProgramMessage] = None

    recipient: Optional[ProgramMessageClickedActivityRecipient] = None
    """A link to the `Address` of the recipient who clicked the link."""


class ProgramMessageComplainedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    recipient: Optional[str] = None
    """A link to the `Address` of the recipient who complained."""


class ProgramMessageComplainedActivityProgramMessage(BaseModel):
    id: str

    type: str


class ProgramMessageComplainedActivityRecipient(BaseModel):
    id: str

    type: str


class ProgramMessageComplainedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageComplainedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_complained"]
    """The type of activity. Always `activity/program_message_complained`."""

    program_message: Optional[ProgramMessageComplainedActivityProgramMessage] = None

    recipient: Optional[ProgramMessageComplainedActivityRecipient] = None
    """A link to the `Address` of the recipient who complained."""


class ProgramMessageFailedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    recipient: Optional[str] = None
    """A link to the `Address` of the recipient whose message failed."""


class ProgramMessageFailedActivityProgramMessage(BaseModel):
    id: str

    type: str


class ProgramMessageFailedActivityRecipient(BaseModel):
    id: str

    type: str


class ProgramMessageFailedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageFailedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_failed"]
    """The type of activity. Always `activity/program_message_failed`."""

    program_message: Optional[ProgramMessageFailedActivityProgramMessage] = None

    reason_code: Optional[str] = None

    recipient: Optional[ProgramMessageFailedActivityRecipient] = None
    """A link to the `Address` of the recipient whose message failed."""


class ProgramMessageOpenedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    recipient: Optional[str] = None
    """A link to the `Address` of the recipient who opened the message."""


class ProgramMessageOpenedActivityProgramMessage(BaseModel):
    id: str

    type: str


class ProgramMessageOpenedActivityRecipient(BaseModel):
    id: str

    type: str


class ProgramMessageOpenedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageOpenedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_opened"]
    """The type of activity. Always `activity/program_message_opened`."""

    program_message: Optional[ProgramMessageOpenedActivityProgramMessage] = None

    recipient: Optional[ProgramMessageOpenedActivityRecipient] = None
    """A link to the `Address` of the recipient who opened the message."""


class ProgramMessageSentActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    recipient: Optional[str] = None
    """A link to the `Address` of the recipient the message was sent to."""


class ProgramMessageSentActivityProgramMessage(BaseModel):
    id: str

    type: str


class ProgramMessageSentActivityRecipient(BaseModel):
    id: str

    type: str


class ProgramMessageSentActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageSentActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_sent"]
    """The type of activity. Always `activity/program_message_sent`."""

    program_message: Optional[ProgramMessageSentActivityProgramMessage] = None

    recipient: Optional[ProgramMessageSentActivityRecipient] = None
    """A link to the `Address` of the recipient the message was sent to."""

    recipient_emails: Optional[List[str]] = None


class ProgramMessageShieldedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    recipient: Optional[str] = None
    """A link to the `Address` of the recipient whose message was shielded."""


class ProgramMessageShieldedActivityProgramMessage(BaseModel):
    id: str

    type: str


class ProgramMessageShieldedActivityRecipient(BaseModel):
    id: str

    type: str


class ProgramMessageShieldedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageShieldedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_shielded"]
    """The type of activity. Always `activity/program_message_shielded`."""

    program_message: Optional[ProgramMessageShieldedActivityProgramMessage] = None

    reason_code: Optional[str] = None

    recipient: Optional[ProgramMessageShieldedActivityRecipient] = None
    """A link to the `Address` of the recipient whose message was shielded."""


class ProgramMessageUnsubscribedActivityLinks(BaseModel):
    self: str
    """The canonical URL for this object."""

    recipient: Optional[str] = None
    """A link to the `Address` of the recipient who unsubscribed."""


class ProgramMessageUnsubscribedActivityProgramMessage(BaseModel):
    id: str

    type: str


class ProgramMessageUnsubscribedActivityRecipient(BaseModel):
    id: str

    type: str


class ProgramMessageUnsubscribedActivity(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: ProgramMessageUnsubscribedActivityLinks

    occurred_at: datetime
    """The time at which the event occurred, as an RFC 3339 timestamp."""

    type: Literal["activity/program_message_unsubscribed"]
    """The type of activity. Always `activity/program_message_unsubscribed`."""

    email: Optional[str] = None

    program_message: Optional[ProgramMessageUnsubscribedActivityProgramMessage] = None

    recipient: Optional[ProgramMessageUnsubscribedActivityRecipient] = None
    """A link to the `Address` of the recipient who unsubscribed."""


Activity: TypeAlias = Annotated[
    Union[
        CallOccurredActivity,
        FormSubmittedActivity,
        InboxMessageSentActivity,
        ItemCreatedActivity,
        ItemMentionedActivity,
        ItemMergedActivity,
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
