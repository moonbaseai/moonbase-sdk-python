# Shared Types

```python
from moonbase_sdk.types import Error, View
```

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
