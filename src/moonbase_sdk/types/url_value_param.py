# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["URLValueParam"]


class URLValueParam(TypedDict, total=False):
    type: Required[Literal["value/uri/url"]]

    url: Required[str]
