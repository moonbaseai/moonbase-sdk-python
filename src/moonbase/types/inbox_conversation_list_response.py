# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboxConversationListResponse"]


class InboxConversationListResponse(BaseModel):
    id: str

    type: Literal["inbox_conversation"]
