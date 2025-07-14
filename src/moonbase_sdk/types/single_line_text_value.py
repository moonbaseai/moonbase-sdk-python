# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SingleLineTextValue"]


class SingleLineTextValue(BaseModel):
    text: str

    type: Literal["value/text/single_line"]
