# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MultiLineTextValueParam"]


class MultiLineTextValueParam(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["value/text/multi_line"]]
