# Shared Types

```python
from moonbase_sdk.types import Error
```

# Activities

Types:

```python
from moonbase_sdk.types import Activity
```

Methods:

- <code title="get /activities/{id}">client.activities.<a href="./src/moonbase_sdk/resources/activities.py">retrieve</a>(id) -> <a href="./src/moonbase_sdk/types/activity.py">Activity</a></code>
- <code title="get /activities">client.activities.<a href="./src/moonbase_sdk/resources/activities.py">list</a>(\*\*<a href="src/moonbase_sdk/types/activity_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/activity.py">SyncCursorPage[Activity]</a></code>

# Calls

Types:

```python
from moonbase_sdk.types import Call
```

Methods:

- <code title="post /calls">client.calls.<a href="./src/moonbase_sdk/resources/calls.py">create</a>(\*\*<a href="src/moonbase_sdk/types/call_create_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/call.py">Call</a></code>

# Collections

Types:

```python
from moonbase_sdk.types import Collection, Field
```

Methods:

- <code title="get /collections/{id}">client.collections.<a href="./src/moonbase_sdk/resources/collections/collections.py">retrieve</a>(id, \*\*<a href="src/moonbase_sdk/types/collection_retrieve_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/collection.py">Collection</a></code>
- <code title="get /collections">client.collections.<a href="./src/moonbase_sdk/resources/collections/collections.py">list</a>(\*\*<a href="src/moonbase_sdk/types/collection_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/collection.py">SyncCursorPage[Collection]</a></code>

## Fields

Methods:

- <code title="get /collections/{collection_id}/fields/{id}">client.collections.fields.<a href="./src/moonbase_sdk/resources/collections/fields.py">retrieve</a>(id, \*, collection_id) -> <a href="./src/moonbase_sdk/types/field.py">Field</a></code>

# Files

Types:

```python
from moonbase_sdk.types import MoonbaseFile
```

Methods:

- <code title="get /files/{id}">client.files.<a href="./src/moonbase_sdk/resources/files.py">retrieve</a>(id) -> <a href="./src/moonbase_sdk/types/moonbase_file.py">MoonbaseFile</a></code>
- <code title="get /files">client.files.<a href="./src/moonbase_sdk/resources/files.py">list</a>(\*\*<a href="src/moonbase_sdk/types/file_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/moonbase_file.py">SyncCursorPage[MoonbaseFile]</a></code>

# Forms

Types:

```python
from moonbase_sdk.types import Form
```

Methods:

- <code title="get /forms/{id}">client.forms.<a href="./src/moonbase_sdk/resources/forms.py">retrieve</a>(id, \*\*<a href="src/moonbase_sdk/types/form_retrieve_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/form.py">Form</a></code>
- <code title="get /forms">client.forms.<a href="./src/moonbase_sdk/resources/forms.py">list</a>(\*\*<a href="src/moonbase_sdk/types/form_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/form.py">SyncCursorPage[Form]</a></code>

# InboxConversations

Types:

```python
from moonbase_sdk.types import InboxConversation
```

Methods:

- <code title="get /inbox_conversations/{id}">client.inbox_conversations.<a href="./src/moonbase_sdk/resources/inbox_conversations.py">retrieve</a>(id, \*\*<a href="src/moonbase_sdk/types/inbox_conversation_retrieve_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/inbox_conversation.py">InboxConversation</a></code>
- <code title="get /inbox_conversations">client.inbox_conversations.<a href="./src/moonbase_sdk/resources/inbox_conversations.py">list</a>(\*\*<a href="src/moonbase_sdk/types/inbox_conversation_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/inbox_conversation.py">SyncCursorPage[InboxConversation]</a></code>

# InboxMessages

Types:

```python
from moonbase_sdk.types import Address, EmailMessage
```

Methods:

- <code title="get /inbox_messages/{id}">client.inbox_messages.<a href="./src/moonbase_sdk/resources/inbox_messages.py">retrieve</a>(id, \*\*<a href="src/moonbase_sdk/types/inbox_message_retrieve_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/email_message.py">EmailMessage</a></code>
- <code title="get /inbox_messages">client.inbox_messages.<a href="./src/moonbase_sdk/resources/inbox_messages.py">list</a>(\*\*<a href="src/moonbase_sdk/types/inbox_message_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/email_message.py">SyncCursorPage[EmailMessage]</a></code>

# Inboxes

Types:

```python
from moonbase_sdk.types import Inbox
```

Methods:

- <code title="get /inboxes/{id}">client.inboxes.<a href="./src/moonbase_sdk/resources/inboxes.py">retrieve</a>(id, \*\*<a href="src/moonbase_sdk/types/inbox_retrieve_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/inbox.py">Inbox</a></code>
- <code title="get /inboxes">client.inboxes.<a href="./src/moonbase_sdk/resources/inboxes.py">list</a>(\*\*<a href="src/moonbase_sdk/types/inbox_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/inbox.py">SyncCursorPage[Inbox]</a></code>

# Items

Types:

```python
from moonbase_sdk.types import (
    BooleanValue,
    Choice,
    DateValue,
    DatetimeValue,
    DomainValue,
    EmailValue,
    FieldValue,
    FloatValue,
    FunnelStep,
    GeoValue,
    IntegerValue,
    Item,
    MonetaryValue,
    MultiLineTextValue,
    PercentageValue,
    RelationValue,
    SingleLineTextValue,
    SocialLinkedInValue,
    SocialXValue,
    TelephoneNumber,
    URLValue,
    Value,
)
```

Methods:

- <code title="post /items">client.items.<a href="./src/moonbase_sdk/resources/items.py">create</a>(\*\*<a href="src/moonbase_sdk/types/item_create_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/item.py">Item</a></code>
- <code title="get /items/{id}">client.items.<a href="./src/moonbase_sdk/resources/items.py">retrieve</a>(id) -> <a href="./src/moonbase_sdk/types/item.py">Item</a></code>
- <code title="patch /items/{id}">client.items.<a href="./src/moonbase_sdk/resources/items.py">update</a>(id, \*\*<a href="src/moonbase_sdk/types/item_update_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/item.py">Item</a></code>
- <code title="delete /items/{id}">client.items.<a href="./src/moonbase_sdk/resources/items.py">delete</a>(id) -> <a href="./src/moonbase_sdk/types/item.py">Item</a></code>
- <code title="post /items/upsert">client.items.<a href="./src/moonbase_sdk/resources/items.py">upsert</a>(\*\*<a href="src/moonbase_sdk/types/item_upsert_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/item.py">Item</a></code>

# Meetings

Types:

```python
from moonbase_sdk.types import Attendee, Meeting, Organizer
```

Methods:

- <code title="get /meetings/{id}">client.meetings.<a href="./src/moonbase_sdk/resources/meetings.py">retrieve</a>(id, \*\*<a href="src/moonbase_sdk/types/meeting_retrieve_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/meeting.py">Meeting</a></code>
- <code title="get /meetings">client.meetings.<a href="./src/moonbase_sdk/resources/meetings.py">list</a>(\*\*<a href="src/moonbase_sdk/types/meeting_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/meeting.py">SyncCursorPage[Meeting]</a></code>

# Notes

Types:

```python
from moonbase_sdk.types import Note
```

Methods:

- <code title="get /notes/{id}">client.notes.<a href="./src/moonbase_sdk/resources/notes.py">retrieve</a>(id) -> <a href="./src/moonbase_sdk/types/note.py">Note</a></code>
- <code title="get /notes">client.notes.<a href="./src/moonbase_sdk/resources/notes.py">list</a>(\*\*<a href="src/moonbase_sdk/types/note_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/note.py">SyncCursorPage[Note]</a></code>

# ProgramMessages

Types:

```python
from moonbase_sdk.types import ProgramMessageSendResponse
```

Methods:

- <code title="post /program_messages">client.program_messages.<a href="./src/moonbase_sdk/resources/program_messages.py">send</a>(\*\*<a href="src/moonbase_sdk/types/program_message_send_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/program_message_send_response.py">ProgramMessageSendResponse</a></code>

# ProgramTemplates

Types:

```python
from moonbase_sdk.types import ProgramTemplate
```

Methods:

- <code title="get /program_templates/{id}">client.program_templates.<a href="./src/moonbase_sdk/resources/program_templates.py">retrieve</a>(id, \*\*<a href="src/moonbase_sdk/types/program_template_retrieve_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/program_template.py">ProgramTemplate</a></code>
- <code title="get /program_templates">client.program_templates.<a href="./src/moonbase_sdk/resources/program_templates.py">list</a>(\*\*<a href="src/moonbase_sdk/types/program_template_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/program_template.py">SyncCursorPage[ProgramTemplate]</a></code>

# Programs

Types:

```python
from moonbase_sdk.types import Program
```

Methods:

- <code title="get /programs/{id}">client.programs.<a href="./src/moonbase_sdk/resources/programs.py">retrieve</a>(id, \*\*<a href="src/moonbase_sdk/types/program_retrieve_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/program.py">Program</a></code>
- <code title="get /programs">client.programs.<a href="./src/moonbase_sdk/resources/programs.py">list</a>(\*\*<a href="src/moonbase_sdk/types/program_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/program.py">SyncCursorPage[Program]</a></code>

# Tagsets

Types:

```python
from moonbase_sdk.types import Tagset
```

Methods:

- <code title="get /tagsets/{id}">client.tagsets.<a href="./src/moonbase_sdk/resources/tagsets.py">retrieve</a>(id) -> <a href="./src/moonbase_sdk/types/tagset.py">Tagset</a></code>
- <code title="get /tagsets">client.tagsets.<a href="./src/moonbase_sdk/resources/tagsets.py">list</a>(\*\*<a href="src/moonbase_sdk/types/tagset_list_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/tagset.py">SyncCursorPage[Tagset]</a></code>

# Views

Types:

```python
from moonbase_sdk.types import View
```

Methods:

- <code title="get /views/{id}">client.views.<a href="./src/moonbase_sdk/resources/views.py">retrieve</a>(id, \*\*<a href="src/moonbase_sdk/types/view_retrieve_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/view.py">View</a></code>
- <code title="get /views/{id}/items">client.views.<a href="./src/moonbase_sdk/resources/views.py">list_items</a>(id, \*\*<a href="src/moonbase_sdk/types/view_list_items_params.py">params</a>) -> <a href="./src/moonbase_sdk/types/item.py">SyncCursorPage[Item]</a></code>
