# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmailMessagePointer"]


class EmailMessagePointer(BaseModel):
    id: str

    type: Literal["email_message"]
