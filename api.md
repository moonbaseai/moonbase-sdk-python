# Shared Types

```python
from moonbase_sdk.types import Error, View
```

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
