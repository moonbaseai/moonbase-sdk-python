# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SocialProfileLinkedInParam"]


class SocialProfileLinkedInParam(TypedDict, total=False):
    """
    Social media profile information including both the full URL and extracted username.
    """

    url: str
    """The full URL to the LinkedIn profile."""

    username: str
    """
    The LinkedIn username, including the prefix 'company/' for company pages or
    'in/' for personal profiles.
    """
