# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Unsubscribe"]


class Unsubscribe(BaseModel):
    created_at: datetime

    email: str

    type: Literal["unsubscribe"]
