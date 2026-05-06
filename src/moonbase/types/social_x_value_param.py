# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .social_profile_x_param import SocialProfileXParam

__all__ = ["SocialXValueParam"]


class SocialXValueParam(TypedDict, total=False):
    """The social media profile for the X (formerly Twitter) platform"""

    data: Required[SocialProfileXParam]
    """
    Social media profile information including both the full URL and extracted
    username.
    """

    type: Required[Literal["value/uri/social_x"]]
