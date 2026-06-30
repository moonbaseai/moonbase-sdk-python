# Shared Types

```python
from moonbase.types import Error, FormattedText, Tag, TagPointerParam
```

# Moonbase

Types:

```python
from moonbase.types import SearchResponse
```

Methods:

- <code title="post /search">client.<a href="./src/moonbase/_client.py">search</a>(\*\*<a href="src/moonbase/types/client_search_params.py">params</a>) -> <a href="./src/moonbase/types/search_response.py">SearchResponse</a></code>

# Funnels

Types:

```python
from moonbase.types import Funnel, FunnelStep, FunnelStepPointer
```

Methods:

- <code title="post /funnels">client.funnels.<a href="./src/moonbase/resources/funnels.py">create</a>(\*\*<a href="src/moonbase/types/funnel_create_params.py">params</a>) -> <a href="./src/moonbase/types/funnel.py">Funnel</a></code>
- <code title="get /funnels/{id}">client.funnels.<a href="./src/moonbase/resources/funnels.py">retrieve</a>(id) -> <a href="./src/moonbase/types/funnel.py">Funnel</a></code>
- <code title="patch /funnels/{id}">client.funnels.<a href="./src/moonbase/resources/funnels.py">update</a>(id, \*\*<a href="src/moonbase/types/funnel_update_params.py">params</a>) -> <a href="./src/moonbase/types/funnel.py">Funnel</a></code>
- <code title="get /funnels">client.funnels.<a href="./src/moonbase/resources/funnels.py">list</a>(\*\*<a href="src/moonbase/types/funnel_list_params.py">params</a>) -> <a href="./src/moonbase/types/funnel.py">SyncCursorPage[Funnel]</a></code>
- <code title="delete /funnels/{id}">client.funnels.<a href="./src/moonbase/resources/funnels.py">delete</a>(id) -> None</code>

# Collections

Types:

```python
from moonbase.types import (
    BooleanField,
    BooleanValue,
    ChoiceField,
    ChoiceFieldOption,
    ChoiceFieldOptionPointer,
    ChoiceValue,
    ChoiceValueParam,
    Collection,
    CollectionPointer,
    CurrentDate,
    CurrentDatetime,
    CurrentMember,
    DateField,
    DateFieldDefaultValueParam,
    DateValue,
    DatetimeField,
    DatetimeFieldDefaultValueParam,
    DatetimeValue,
    DomainField,
    DomainValue,
    EmailField,
    EmailValue,
    Field,
    FieldDefaultValue,
    FieldPointer,
    FieldValue,
    FieldValueParam,
    FloatField,
    FloatValue,
    FunnelPointerParam,
    FunnelStepValue,
    FunnelStepValueParam,
    GeoField,
    GeoValue,
    IdentifierField,
    IdentifierValue,
    IntegerField,
    IntegerValue,
    Item,
    ItemPointer,
    ItemPointerParam,
    ItemsFilter,
    ItemsFilterAndGroup,
    ItemsFilterNotGroup,
    ItemsFilterOrGroup,
    ItemsFilterValueExists,
    ItemsFilterValueMatches,
    MonetaryField,
    MonetaryValue,
    MultiLineTextField,
    MultiLineTextValue,
    PercentageField,
    PercentageValue,
    RelationField,
    RelationFieldDefaultValueParam,
    RelationValue,
    RelationValueParam,
    SingleLineTextField,
    SingleLineTextValue,
    SocialLinkedInField,
    SocialLinkedInValue,
    SocialLinkedInValueParam,
    SocialProfileLinkedInParam,
    SocialProfileXParam,
    SocialXField,
    SocialXValue,
    SocialXValueParam,
    StageField,
    StageFieldCreateParams,
    StageFieldUpdateParams,
    TelephoneNumber,
    TelephoneNumberField,
    URLField,
    URLValue,
    Value,
    ValueParam,
    CollectionListResponse,
)
```

Methods:

- <code title="post /collections">client.collections.<a href="./src/moonbase/resources/collections/collections.py">create</a>(\*\*<a href="src/moonbase/types/collection_create_params.py">params</a>) -> <a href="./src/moonbase/types/collection.py">Collection</a></code>
- <code title="get /collections/{id}">client.collections.<a href="./src/moonbase/resources/collections/collections.py">retrieve</a>(id) -> <a href="./src/moonbase/types/collection.py">Collection</a></code>
- <code title="patch /collections/{id}">client.collections.<a href="./src/moonbase/resources/collections/collections.py">update</a>(id, \*\*<a href="src/moonbase/types/collection_update_params.py">params</a>) -> <a href="./src/moonbase/types/collection.py">Collection</a></code>
- <code title="get /collections">client.collections.<a href="./src/moonbase/resources/collections/collections.py">list</a>(\*\*<a href="src/moonbase/types/collection_list_params.py">params</a>) -> <a href="./src/moonbase/types/collection_list_response.py">SyncCursorPage[CollectionListResponse]</a></code>
- <code title="delete /collections/{id}">client.collections.<a href="./src/moonbase/resources/collections/collections.py">delete</a>(id) -> None</code>

## Fields

Methods:

- <code title="post /collections/{collection_id}/fields">client.collections.fields.<a href="./src/moonbase/resources/collections/fields.py">create</a>(collection_id, \*\*<a href="src/moonbase/types/collections/field_create_params.py">params</a>) -> <a href="./src/moonbase/types/field.py">Field</a></code>
- <code title="get /collections/{collection_id}/fields/{id}">client.collections.fields.<a href="./src/moonbase/resources/collections/fields.py">retrieve</a>(id, \*, collection_id) -> <a href="./src/moonbase/types/field.py">Field</a></code>
- <code title="patch /collections/{collection_id}/fields/{id}">client.collections.fields.<a href="./src/moonbase/resources/collections/fields.py">update</a>(id, \*, collection_id, \*\*<a href="src/moonbase/types/collections/field_update_params.py">params</a>) -> <a href="./src/moonbase/types/field.py">Field</a></code>
- <code title="delete /collections/{collection_id}/fields/{id}">client.collections.fields.<a href="./src/moonbase/resources/collections/fields.py">delete</a>(id, \*, collection_id) -> None</code>

## Items

Types:

```python
from moonbase.types.collections import ItemSearchResponse
```

Methods:

- <code title="post /collections/{collection_id}/items">client.collections.items.<a href="./src/moonbase/resources/collections/items.py">create</a>(collection_id, \*\*<a href="src/moonbase/types/collections/item_create_params.py">params</a>) -> <a href="./src/moonbase/types/item.py">Item</a></code>
- <code title="get /collections/{collection_id}/items/{id}">client.collections.items.<a href="./src/moonbase/resources/collections/items.py">retrieve</a>(id, \*, collection_id) -> <a href="./src/moonbase/types/item.py">Item</a></code>
- <code title="patch /collections/{collection_id}/items/{id}">client.collections.items.<a href="./src/moonbase/resources/collections/items.py">update</a>(id, \*, collection_id, \*\*<a href="src/moonbase/types/collections/item_update_params.py">params</a>) -> <a href="./src/moonbase/types/item.py">Item</a></code>
- <code title="get /collections/{collection_id}/items">client.collections.items.<a href="./src/moonbase/resources/collections/items.py">list</a>(collection_id, \*\*<a href="src/moonbase/types/collections/item_list_params.py">params</a>) -> <a href="./src/moonbase/types/item_pointer.py">SyncCursorPage[ItemPointer]</a></code>
- <code title="delete /collections/{collection_id}/items/{id}">client.collections.items.<a href="./src/moonbase/resources/collections/items.py">delete</a>(id, \*, collection_id) -> None</code>
- <code title="post /collections/{collection_id}/items/merge">client.collections.items.<a href="./src/moonbase/resources/collections/items.py">merge</a>(collection_id, \*\*<a href="src/moonbase/types/collections/item_merge_params.py">params</a>) -> <a href="./src/moonbase/types/item.py">Item</a></code>
- <code title="post /collections/{collection_id}/items/search">client.collections.items.<a href="./src/moonbase/resources/collections/items.py">search</a>(collection_id, \*\*<a href="src/moonbase/types/collections/item_search_params.py">params</a>) -> <a href="./src/moonbase/types/collections/item_search_response.py">SyncCursorPage[ItemSearchResponse]</a></code>
- <code title="post /collections/{collection_id}/items/upsert">client.collections.items.<a href="./src/moonbase/resources/collections/items.py">upsert</a>(collection_id, \*\*<a href="src/moonbase/types/collections/item_upsert_params.py">params</a>) -> <a href="./src/moonbase/types/item.py">Item</a></code>

# Views

Types:

```python
from moonbase.types import (
    View,
    ViewAggregate,
    ViewAggregateFieldStatistic,
    ViewAggregateItemCount,
    ViewField,
    ViewRelationValueFilter,
    ViewListResponse,
)
```

Methods:

- <code title="post /views">client.views.<a href="./src/moonbase/resources/views/views.py">create</a>(\*\*<a href="src/moonbase/types/view_create_params.py">params</a>) -> <a href="./src/moonbase/types/view.py">View</a></code>
- <code title="get /views/{id}">client.views.<a href="./src/moonbase/resources/views/views.py">retrieve</a>(id) -> <a href="./src/moonbase/types/view.py">View</a></code>
- <code title="patch /views/{id}">client.views.<a href="./src/moonbase/resources/views/views.py">update</a>(id, \*\*<a href="src/moonbase/types/view_update_params.py">params</a>) -> <a href="./src/moonbase/types/view.py">View</a></code>
- <code title="get /views">client.views.<a href="./src/moonbase/resources/views/views.py">list</a>(\*\*<a href="src/moonbase/types/view_list_params.py">params</a>) -> <a href="./src/moonbase/types/view_list_response.py">SyncCursorPage[ViewListResponse]</a></code>
- <code title="delete /views/{id}">client.views.<a href="./src/moonbase/resources/views/views.py">delete</a>(id) -> None</code>

## Items

Methods:

- <code title="get /views/{id}/items">client.views.items.<a href="./src/moonbase/resources/views/items.py">list</a>(id, \*\*<a href="src/moonbase/types/views/item_list_params.py">params</a>) -> <a href="./src/moonbase/types/item.py">SyncCursorPage[Item]</a></code>

# Inboxes

Types:

```python
from moonbase.types import Inbox
```

Methods:

- <code title="get /inboxes/{id}">client.inboxes.<a href="./src/moonbase/resources/inboxes.py">retrieve</a>(id) -> <a href="./src/moonbase/types/inbox.py">Inbox</a></code>
- <code title="get /inboxes">client.inboxes.<a href="./src/moonbase/resources/inboxes.py">list</a>(\*\*<a href="src/moonbase/types/inbox_list_params.py">params</a>) -> <a href="./src/moonbase/types/inbox.py">SyncCursorPage[Inbox]</a></code>

# InboxConversations

Types:

```python
from moonbase.types import InboxConversation, InboxConversationListResponse
```

Methods:

- <code title="get /inbox_conversations/{id}">client.inbox_conversations.<a href="./src/moonbase/resources/inbox_conversations.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/inbox_conversation_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/inbox_conversation.py">InboxConversation</a></code>
- <code title="get /inbox_conversations">client.inbox_conversations.<a href="./src/moonbase/resources/inbox_conversations.py">list</a>(\*\*<a href="src/moonbase/types/inbox_conversation_list_params.py">params</a>) -> <a href="./src/moonbase/types/inbox_conversation_list_response.py">SyncCursorPage[InboxConversationListResponse]</a></code>

# InboxMessages

Types:

```python
from moonbase.types import (
    EmailMessage,
    EmailMessageAddress,
    EmailMessageAddressParams,
    MessageAttachment,
    MessagePointer,
    SlackMessage,
    SlackMessageAddress,
    SlackMessageAddressParams,
    InboxMessageCreateResponse,
    InboxMessageRetrieveResponse,
    InboxMessageUpdateResponse,
)
```

Methods:

- <code title="post /inbox_messages">client.inbox_messages.<a href="./src/moonbase/resources/inbox_messages/inbox_messages.py">create</a>(\*\*<a href="src/moonbase/types/inbox_message_create_params.py">params</a>) -> <a href="./src/moonbase/types/inbox_message_create_response.py">InboxMessageCreateResponse</a></code>
- <code title="get /inbox_messages/{id}">client.inbox_messages.<a href="./src/moonbase/resources/inbox_messages/inbox_messages.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/inbox_message_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/inbox_message_retrieve_response.py">InboxMessageRetrieveResponse</a></code>
- <code title="patch /inbox_messages/{id}">client.inbox_messages.<a href="./src/moonbase/resources/inbox_messages/inbox_messages.py">update</a>(id, \*\*<a href="src/moonbase/types/inbox_message_update_params.py">params</a>) -> <a href="./src/moonbase/types/inbox_message_update_response.py">InboxMessageUpdateResponse</a></code>
- <code title="get /inbox_messages">client.inbox_messages.<a href="./src/moonbase/resources/inbox_messages/inbox_messages.py">list</a>(\*\*<a href="src/moonbase/types/inbox_message_list_params.py">params</a>) -> <a href="./src/moonbase/types/message_pointer.py">SyncCursorPage[MessagePointer]</a></code>
- <code title="delete /inbox_messages/{id}">client.inbox_messages.<a href="./src/moonbase/resources/inbox_messages/inbox_messages.py">delete</a>(id) -> None</code>

## Attachments

Methods:

- <code title="post /inbox_messages/{inbox_message_id}/attachments">client.inbox_messages.attachments.<a href="./src/moonbase/resources/inbox_messages/attachments.py">create</a>(inbox_message_id, \*\*<a href="src/moonbase/types/inbox_messages/attachment_create_params.py">params</a>) -> <a href="./src/moonbase/types/message_attachment.py">MessageAttachment</a></code>
- <code title="delete /inbox_messages/{inbox_message_id}/attachments/{id}">client.inbox_messages.attachments.<a href="./src/moonbase/resources/inbox_messages/attachments.py">delete</a>(id, \*, inbox_message_id) -> None</code>

# Tagsets

Types:

```python
from moonbase.types import Tagset, TagsetPointer
```

Methods:

- <code title="post /tagsets">client.tagsets.<a href="./src/moonbase/resources/tagsets.py">create</a>(\*\*<a href="src/moonbase/types/tagset_create_params.py">params</a>) -> <a href="./src/moonbase/types/tagset.py">Tagset</a></code>
- <code title="get /tagsets/{id}">client.tagsets.<a href="./src/moonbase/resources/tagsets.py">retrieve</a>(id) -> <a href="./src/moonbase/types/tagset.py">Tagset</a></code>
- <code title="patch /tagsets/{id}">client.tagsets.<a href="./src/moonbase/resources/tagsets.py">update</a>(id, \*\*<a href="src/moonbase/types/tagset_update_params.py">params</a>) -> <a href="./src/moonbase/types/tagset.py">Tagset</a></code>
- <code title="get /tagsets">client.tagsets.<a href="./src/moonbase/resources/tagsets.py">list</a>(\*\*<a href="src/moonbase/types/tagset_list_params.py">params</a>) -> <a href="./src/moonbase/types/tagset.py">SyncCursorPage[Tagset]</a></code>
- <code title="delete /tagsets/{id}">client.tagsets.<a href="./src/moonbase/resources/tagsets.py">delete</a>(id) -> None</code>

# Programs

Types:

```python
from moonbase.types import Program, ProgramActivityMetrics, ProgramPointer
```

Methods:

- <code title="get /programs/{id}">client.programs.<a href="./src/moonbase/resources/programs.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/program_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/program.py">Program</a></code>
- <code title="get /programs">client.programs.<a href="./src/moonbase/resources/programs.py">list</a>(\*\*<a href="src/moonbase/types/program_list_params.py">params</a>) -> <a href="./src/moonbase/types/program.py">SyncCursorPage[Program]</a></code>

# ProgramTemplates

Types:

```python
from moonbase.types import ProgramTemplate, ProgramTemplatePointer
```

Methods:

- <code title="get /program_templates/{id}">client.program_templates.<a href="./src/moonbase/resources/program_templates.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/program_template_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/program_template.py">ProgramTemplate</a></code>
- <code title="get /program_templates">client.program_templates.<a href="./src/moonbase/resources/program_templates.py">list</a>(\*\*<a href="src/moonbase/types/program_template_list_params.py">params</a>) -> <a href="./src/moonbase/types/program_template.py">SyncCursorPage[ProgramTemplate]</a></code>

# ProgramMessages

Types:

```python
from moonbase.types import ProgramMessage, ProgramMessagePointer
```

Methods:

- <code title="post /program_messages">client.program_messages.<a href="./src/moonbase/resources/program_messages.py">send</a>(\*\*<a href="src/moonbase/types/program_message_send_params.py">params</a>) -> <a href="./src/moonbase/types/program_message.py">ProgramMessage</a></code>

# Forms

Types:

```python
from moonbase.types import Form
```

Methods:

- <code title="post /forms">client.forms.<a href="./src/moonbase/resources/forms.py">create</a>(\*\*<a href="src/moonbase/types/form_create_params.py">params</a>) -> <a href="./src/moonbase/types/form.py">Form</a></code>
- <code title="get /forms/{id}">client.forms.<a href="./src/moonbase/resources/forms.py">retrieve</a>(id) -> <a href="./src/moonbase/types/form.py">Form</a></code>
- <code title="patch /forms/{id}">client.forms.<a href="./src/moonbase/resources/forms.py">update</a>(id, \*\*<a href="src/moonbase/types/form_update_params.py">params</a>) -> <a href="./src/moonbase/types/form.py">Form</a></code>
- <code title="get /forms">client.forms.<a href="./src/moonbase/resources/forms.py">list</a>(\*\*<a href="src/moonbase/types/form_list_params.py">params</a>) -> <a href="./src/moonbase/types/form.py">SyncCursorPage[Form]</a></code>
- <code title="delete /forms/{id}">client.forms.<a href="./src/moonbase/resources/forms.py">delete</a>(id) -> None</code>

# Unsubscribes

Types:

```python
from moonbase.types import Unsubscribe, UnsubscribePointer
```

Methods:

- <code title="post /unsubscribes">client.unsubscribes.<a href="./src/moonbase/resources/unsubscribes.py">create</a>(\*\*<a href="src/moonbase/types/unsubscribe_create_params.py">params</a>) -> <a href="./src/moonbase/types/unsubscribe.py">Unsubscribe</a></code>
- <code title="get /unsubscribes">client.unsubscribes.<a href="./src/moonbase/resources/unsubscribes.py">list</a>(\*\*<a href="src/moonbase/types/unsubscribe_list_params.py">params</a>) -> <a href="./src/moonbase/types/unsubscribe.py">SyncCursorPage[Unsubscribe]</a></code>
- <code title="delete /unsubscribes/{email}">client.unsubscribes.<a href="./src/moonbase/resources/unsubscribes.py">delete</a>(email) -> None</code>

# Activities

Types:

```python
from moonbase.types import (
    Activity,
    ActivityCallOccurred,
    ActivityFormSubmitted,
    ActivityInboxMessageSent,
    ActivityItemCreated,
    ActivityItemMentioned,
    ActivityItemMerged,
    ActivityMeetingHeld,
    ActivityMeetingScheduled,
    ActivityNoteCreated,
    ActivityProgramMessageBounced,
    ActivityProgramMessageClicked,
    ActivityProgramMessageComplained,
    ActivityProgramMessageFailed,
    ActivityProgramMessageOpened,
    ActivityProgramMessageSent,
    ActivityProgramMessageShielded,
    ActivityProgramMessageUnsubscribed,
    Constituent,
    ConstituentEntityPointer,
)
```

Methods:

- <code title="get /activities/{id}">client.activities.<a href="./src/moonbase/resources/activities.py">retrieve</a>(id) -> <a href="./src/moonbase/types/activity.py">Activity</a></code>
- <code title="get /activities">client.activities.<a href="./src/moonbase/resources/activities.py">list</a>(\*\*<a href="src/moonbase/types/activity_list_params.py">params</a>) -> <a href="./src/moonbase/types/activity.py">SyncCursorPage[Activity]</a></code>

# Calls

Types:

```python
from moonbase.types import (
    Call,
    CallParticipant,
    CallPointer,
    CallTranscript,
    CallTranscriptCue,
    CallTranscriptSpeaker,
)
```

Methods:

- <code title="post /calls">client.calls.<a href="./src/moonbase/resources/calls.py">create</a>(\*\*<a href="src/moonbase/types/call_create_params.py">params</a>) -> <a href="./src/moonbase/types/call.py">Call</a></code>
- <code title="get /calls/{id}">client.calls.<a href="./src/moonbase/resources/calls.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/call_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/call.py">Call</a></code>
- <code title="get /calls">client.calls.<a href="./src/moonbase/resources/calls.py">list</a>(\*\*<a href="src/moonbase/types/call_list_params.py">params</a>) -> <a href="./src/moonbase/types/call.py">SyncCursorPage[Call]</a></code>
- <code title="post /calls/upsert">client.calls.<a href="./src/moonbase/resources/calls.py">upsert</a>(\*\*<a href="src/moonbase/types/call_upsert_params.py">params</a>) -> <a href="./src/moonbase/types/call.py">Call</a></code>

# Files

Types:

```python
from moonbase.types import FilePointer, MoonbaseFile
```

Methods:

- <code title="get /files/{id}">client.files.<a href="./src/moonbase/resources/files.py">retrieve</a>(id) -> <a href="./src/moonbase/types/moonbase_file.py">MoonbaseFile</a></code>
- <code title="get /files">client.files.<a href="./src/moonbase/resources/files.py">list</a>(\*\*<a href="src/moonbase/types/file_list_params.py">params</a>) -> <a href="./src/moonbase/types/moonbase_file.py">SyncCursorPage[MoonbaseFile]</a></code>
- <code title="delete /files/{id}">client.files.<a href="./src/moonbase/resources/files.py">delete</a>(id) -> None</code>
- <code title="post /files">client.files.<a href="./src/moonbase/resources/files.py">upload</a>(\*\*<a href="src/moonbase/types/file_upload_params.py">params</a>) -> <a href="./src/moonbase/types/moonbase_file.py">MoonbaseFile</a></code>

# Meetings

Types:

```python
from moonbase.types import (
    Attendee,
    Meeting,
    MeetingPointer,
    MeetingTranscript,
    MeetingTranscriptCue,
    MeetingTranscriptSpeaker,
    Organizer,
)
```

Methods:

- <code title="get /meetings/{id}">client.meetings.<a href="./src/moonbase/resources/meetings.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/meeting_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/meeting.py">Meeting</a></code>
- <code title="patch /meetings/{id}">client.meetings.<a href="./src/moonbase/resources/meetings.py">update</a>(id, \*\*<a href="src/moonbase/types/meeting_update_params.py">params</a>) -> <a href="./src/moonbase/types/meeting.py">Meeting</a></code>
- <code title="get /meetings">client.meetings.<a href="./src/moonbase/resources/meetings.py">list</a>(\*\*<a href="src/moonbase/types/meeting_list_params.py">params</a>) -> <a href="./src/moonbase/types/meeting_pointer.py">SyncCursorPage[MeetingPointer]</a></code>

# Notes

Types:

```python
from moonbase.types import Note, NoteAssociationParamPointer, NoteAssociationPointer, NotePointer
```

Methods:

- <code title="post /notes">client.notes.<a href="./src/moonbase/resources/notes.py">create</a>(\*\*<a href="src/moonbase/types/note_create_params.py">params</a>) -> <a href="./src/moonbase/types/note.py">Note</a></code>
- <code title="get /notes/{id}">client.notes.<a href="./src/moonbase/resources/notes.py">retrieve</a>(id) -> <a href="./src/moonbase/types/note.py">Note</a></code>
- <code title="patch /notes/{id}">client.notes.<a href="./src/moonbase/resources/notes.py">update</a>(id, \*\*<a href="src/moonbase/types/note_update_params.py">params</a>) -> <a href="./src/moonbase/types/note.py">Note</a></code>
- <code title="get /notes">client.notes.<a href="./src/moonbase/resources/notes.py">list</a>(\*\*<a href="src/moonbase/types/note_list_params.py">params</a>) -> <a href="./src/moonbase/types/note.py">SyncCursorPage[Note]</a></code>
- <code title="delete /notes/{id}">client.notes.<a href="./src/moonbase/resources/notes.py">delete</a>(id) -> None</code>

# WebhookEndpoints

Types:

```python
from moonbase.types import Endpoint, Subscription
```

Methods:

- <code title="post /webhook_endpoints">client.webhook_endpoints.<a href="./src/moonbase/resources/webhook_endpoints.py">create</a>(\*\*<a href="src/moonbase/types/webhook_endpoint_create_params.py">params</a>) -> <a href="./src/moonbase/types/endpoint.py">Endpoint</a></code>
- <code title="get /webhook_endpoints/{id}">client.webhook_endpoints.<a href="./src/moonbase/resources/webhook_endpoints.py">retrieve</a>(id) -> <a href="./src/moonbase/types/endpoint.py">Endpoint</a></code>
- <code title="patch /webhook_endpoints/{id}">client.webhook_endpoints.<a href="./src/moonbase/resources/webhook_endpoints.py">update</a>(id, \*\*<a href="src/moonbase/types/webhook_endpoint_update_params.py">params</a>) -> <a href="./src/moonbase/types/endpoint.py">Endpoint</a></code>
- <code title="get /webhook_endpoints">client.webhook_endpoints.<a href="./src/moonbase/resources/webhook_endpoints.py">list</a>(\*\*<a href="src/moonbase/types/webhook_endpoint_list_params.py">params</a>) -> <a href="./src/moonbase/types/endpoint.py">SyncCursorPage[Endpoint]</a></code>
- <code title="delete /webhook_endpoints/{id}">client.webhook_endpoints.<a href="./src/moonbase/resources/webhook_endpoints.py">delete</a>(id) -> None</code>

# AgentSettings

Types:

```python
from moonbase.types import AgentSettingRetrieveResponse, AgentSettingUpdateResponse
```

Methods:

- <code title="get /agent_settings">client.agent_settings.<a href="./src/moonbase/resources/agent_settings.py">retrieve</a>() -> <a href="./src/moonbase/types/agent_setting_retrieve_response.py">AgentSettingRetrieveResponse</a></code>
- <code title="patch /agent_settings">client.agent_settings.<a href="./src/moonbase/resources/agent_settings.py">update</a>(\*\*<a href="src/moonbase/types/agent_setting_update_params.py">params</a>) -> <a href="./src/moonbase/types/agent_setting_update_response.py">AgentSettingUpdateResponse</a></code>
