# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Choice", "Option"]


class Option(BaseModel):
    id: str

    type: Literal["field_option"]

    label: Optional[str] = None


class Choice(BaseModel):
    option: Option

    type: Literal["value/choice"]
