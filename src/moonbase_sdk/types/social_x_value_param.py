# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SocialXValueParam", "Profile"]


class Profile(TypedDict, total=False):
    url: str

    username: str


class SocialXValueParam(TypedDict, total=False):
    profile: Required[Profile]

    type: Required[Literal["value/uri/social_x"]]
