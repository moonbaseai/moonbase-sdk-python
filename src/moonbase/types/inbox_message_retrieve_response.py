# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .email_message import EmailMessage
from .slack_message import SlackMessage

__all__ = ["InboxMessageRetrieveResponse"]

InboxMessageRetrieveResponse: TypeAlias = Annotated[
    Union[EmailMessage, SlackMessage], PropertyInfo(discriminator="type")
]
