# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo

__all__ = ["InboxMessageUpdateResponse"]

InboxMessageUpdateResponse: TypeAlias = Annotated[
    Union["EmailMessage", "SlackMessage"], PropertyInfo(discriminator="type")
]

from .email_message import EmailMessage
from .slack_message import SlackMessage
