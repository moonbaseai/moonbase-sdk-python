# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SocialProfileXParam"]


class SocialProfileXParam(TypedDict, total=False):
    """
    Social media profile information including both the full URL and extracted username.
    """

    url: str
    """The full URL to the X profile, starting with 'https://x.com/'"""

    username: str
    """
    The X username, up to 15 characters long, containing only lowercase letters
    (a-z), uppercase letters (A-Z), numbers (0-9), and underscores (\\__). Does not
    include the '@' symbol prefix.
    """
