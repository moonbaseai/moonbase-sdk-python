# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .social_profile_linked_in_param import SocialProfileLinkedInParam

__all__ = ["SocialLinkedInValueParam"]


class SocialLinkedInValueParam(TypedDict, total=False):
    """The social media profile for the LinkedIn platform"""

    data: Required[SocialProfileLinkedInParam]
    """The social media profile for the LinkedIn platform"""

    type: Required[Literal["value/uri/social_linked_in"]]
