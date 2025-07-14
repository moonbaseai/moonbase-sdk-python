# Shared Types

```python
from moonbase.types import Error
```

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
