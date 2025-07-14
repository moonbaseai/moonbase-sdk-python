# Shared Types

```python
from moonbase.types import Error, View
```

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
