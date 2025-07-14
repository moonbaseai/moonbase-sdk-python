# Shared Types

```python
from moonbase.types import Error, View
```

# Activities

Types:

```python
from moonbase.types import Activity
```

Methods:

- <code title="get /activities/{id}">client.activities.<a href="./src/moonbase/resources/activities.py">retrieve</a>(id) -> <a href="./src/moonbase/types/activity.py">Activity</a></code>
- <code title="get /activities">client.activities.<a href="./src/moonbase/resources/activities.py">list</a>(\*\*<a href="src/moonbase/types/activity_list_params.py">params</a>) -> <a href="./src/moonbase/types/activity.py">SyncCursorPage[Activity]</a></code>

# Calls

Types:

```python
from moonbase.types import Call
```

Methods:

- <code title="post /calls">client.calls.<a href="./src/moonbase/resources/calls.py">create</a>(\*\*<a href="src/moonbase/types/call_create_params.py">params</a>) -> <a href="./src/moonbase/types/call.py">Call</a></code>

# Collections

Types:

```python
from moonbase.types import Collection, Field
```

Methods:

- <code title="get /collections/{id}">client.collections.<a href="./src/moonbase/resources/collections/collections.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/collection_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/collection.py">Collection</a></code>
- <code title="get /collections">client.collections.<a href="./src/moonbase/resources/collections/collections.py">list</a>(\*\*<a href="src/moonbase/types/collection_list_params.py">params</a>) -> <a href="./src/moonbase/types/collection.py">SyncCursorPage[Collection]</a></code>

## Fields

Methods:

- <code title="get /collections/{collection_id}/fields/{id}">client.collections.fields.<a href="./src/moonbase/resources/collections/fields.py">retrieve</a>(id, \*, collection_id) -> <a href="./src/moonbase/types/field.py">Field</a></code>

# Files

Types:

```python
from moonbase.types import MoonbaseFile
```

Methods:

- <code title="get /files/{id}">client.files.<a href="./src/moonbase/resources/files.py">retrieve</a>(id) -> <a href="./src/moonbase/types/moonbase_file.py">MoonbaseFile</a></code>
- <code title="get /files">client.files.<a href="./src/moonbase/resources/files.py">list</a>(\*\*<a href="src/moonbase/types/file_list_params.py">params</a>) -> <a href="./src/moonbase/types/moonbase_file.py">SyncCursorPage[MoonbaseFile]</a></code>

# Forms

Types:

```python
from moonbase.types import Form
```

Methods:

- <code title="get /forms/{id}">client.forms.<a href="./src/moonbase/resources/forms.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/form_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/form.py">Form</a></code>
- <code title="get /forms">client.forms.<a href="./src/moonbase/resources/forms.py">list</a>(\*\*<a href="src/moonbase/types/form_list_params.py">params</a>) -> <a href="./src/moonbase/types/form.py">SyncCursorPage[Form]</a></code>

# InboxConversations

Types:

```python
from moonbase.types import InboxConversation
```

Methods:

- <code title="get /inbox_conversations/{id}">client.inbox_conversations.<a href="./src/moonbase/resources/inbox_conversations.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/inbox_conversation_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/inbox_conversation.py">InboxConversation</a></code>
- <code title="get /inbox_conversations">client.inbox_conversations.<a href="./src/moonbase/resources/inbox_conversations.py">list</a>(\*\*<a href="src/moonbase/types/inbox_conversation_list_params.py">params</a>) -> <a href="./src/moonbase/types/inbox_conversation.py">SyncCursorPage[InboxConversation]</a></code>

# InboxMessages

Types:

```python
from moonbase.types import Address, EmailMessage
```

Methods:

- <code title="get /inbox_messages/{id}">client.inbox_messages.<a href="./src/moonbase/resources/inbox_messages.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/inbox_message_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/email_message.py">EmailMessage</a></code>
- <code title="get /inbox_messages">client.inbox_messages.<a href="./src/moonbase/resources/inbox_messages.py">list</a>(\*\*<a href="src/moonbase/types/inbox_message_list_params.py">params</a>) -> <a href="./src/moonbase/types/email_message.py">SyncCursorPage[EmailMessage]</a></code>

# Inboxes

Types:

```python
from moonbase.types import Inbox
```

Methods:

- <code title="get /inboxes/{id}">client.inboxes.<a href="./src/moonbase/resources/inboxes.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/inbox_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/inbox.py">Inbox</a></code>
- <code title="get /inboxes">client.inboxes.<a href="./src/moonbase/resources/inboxes.py">list</a>(\*\*<a href="src/moonbase/types/inbox_list_params.py">params</a>) -> <a href="./src/moonbase/types/inbox.py">SyncCursorPage[Inbox]</a></code>

# Items

Types:

```python
from moonbase.types import (
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

- <code title="post /items">client.items.<a href="./src/moonbase/resources/items.py">create</a>(\*\*<a href="src/moonbase/types/item_create_params.py">params</a>) -> <a href="./src/moonbase/types/item.py">Item</a></code>
- <code title="get /items/{id}">client.items.<a href="./src/moonbase/resources/items.py">retrieve</a>(id) -> <a href="./src/moonbase/types/item.py">Item</a></code>
- <code title="patch /items/{id}">client.items.<a href="./src/moonbase/resources/items.py">update</a>(id, \*\*<a href="src/moonbase/types/item_update_params.py">params</a>) -> <a href="./src/moonbase/types/item.py">Item</a></code>
- <code title="delete /items/{id}">client.items.<a href="./src/moonbase/resources/items.py">delete</a>(id) -> <a href="./src/moonbase/types/item.py">Item</a></code>
- <code title="post /items/upsert">client.items.<a href="./src/moonbase/resources/items.py">upsert</a>(\*\*<a href="src/moonbase/types/item_upsert_params.py">params</a>) -> <a href="./src/moonbase/types/item.py">Item</a></code>

# Meetings

Types:

```python
from moonbase.types import Attendee, Meeting, Organizer
```

Methods:

- <code title="get /meetings/{id}">client.meetings.<a href="./src/moonbase/resources/meetings.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/meeting_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/meeting.py">Meeting</a></code>
- <code title="get /meetings">client.meetings.<a href="./src/moonbase/resources/meetings.py">list</a>(\*\*<a href="src/moonbase/types/meeting_list_params.py">params</a>) -> <a href="./src/moonbase/types/meeting.py">SyncCursorPage[Meeting]</a></code>

# Notes

Types:

```python
from moonbase.types import Note
```

Methods:

- <code title="get /notes/{id}">client.notes.<a href="./src/moonbase/resources/notes.py">retrieve</a>(id) -> <a href="./src/moonbase/types/note.py">Note</a></code>
- <code title="get /notes">client.notes.<a href="./src/moonbase/resources/notes.py">list</a>(\*\*<a href="src/moonbase/types/note_list_params.py">params</a>) -> <a href="./src/moonbase/types/note.py">SyncCursorPage[Note]</a></code>

# ProgramMessages

Types:

```python
from moonbase.types import ProgramMessageSendResponse
```

Methods:

- <code title="post /program_messages">client.program_messages.<a href="./src/moonbase/resources/program_messages.py">send</a>(\*\*<a href="src/moonbase/types/program_message_send_params.py">params</a>) -> <a href="./src/moonbase/types/program_message_send_response.py">ProgramMessageSendResponse</a></code>

# ProgramTemplates

Types:

```python
from moonbase.types import ProgramTemplate
```

Methods:

- <code title="get /program_templates/{id}">client.program_templates.<a href="./src/moonbase/resources/program_templates.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/program_template_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/program_template.py">ProgramTemplate</a></code>
- <code title="get /program_templates">client.program_templates.<a href="./src/moonbase/resources/program_templates.py">list</a>(\*\*<a href="src/moonbase/types/program_template_list_params.py">params</a>) -> <a href="./src/moonbase/types/program_template.py">SyncCursorPage[ProgramTemplate]</a></code>

# Programs

Types:

```python
from moonbase.types import Program
```

Methods:

- <code title="get /programs/{id}">client.programs.<a href="./src/moonbase/resources/programs.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/program_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/program.py">Program</a></code>
- <code title="get /programs">client.programs.<a href="./src/moonbase/resources/programs.py">list</a>(\*\*<a href="src/moonbase/types/program_list_params.py">params</a>) -> <a href="./src/moonbase/types/program.py">SyncCursorPage[Program]</a></code>

# Tagsets

Types:

```python
from moonbase.types import Tagset
```

Methods:

- <code title="get /tagsets/{id}">client.tagsets.<a href="./src/moonbase/resources/tagsets.py">retrieve</a>(id) -> <a href="./src/moonbase/types/tagset.py">Tagset</a></code>
- <code title="get /tagsets">client.tagsets.<a href="./src/moonbase/resources/tagsets.py">list</a>(\*\*<a href="src/moonbase/types/tagset_list_params.py">params</a>) -> <a href="./src/moonbase/types/tagset.py">SyncCursorPage[Tagset]</a></code>

# Views

Methods:

- <code title="get /views/{id}">client.views.<a href="./src/moonbase/resources/views/views.py">retrieve</a>(id, \*\*<a href="src/moonbase/types/view_retrieve_params.py">params</a>) -> <a href="./src/moonbase/types/shared/view.py">View</a></code>

## Items

Methods:

- <code title="get /views/{id}/items">client.views.items.<a href="./src/moonbase/resources/views/items.py">list</a>(id, \*\*<a href="src/moonbase/types/views/item_list_params.py">params</a>) -> <a href="./src/moonbase/types/item.py">SyncCursorPage[Item]</a></code>
