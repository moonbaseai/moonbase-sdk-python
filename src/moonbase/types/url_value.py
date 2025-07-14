# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["URLValue"]


class URLValue(BaseModel):
    type: Literal["value/uri/url"]

    url: str
