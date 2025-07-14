# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["FormRetrieveParams"]


class FormRetrieveParams(TypedDict, total=False):
    include: List[Literal["collection.fields"]]
    """Specifies which related objects to include in the response.

    Valid option is `collection.fields`.
    """
