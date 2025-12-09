# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SocialLinkedInValue", "Data"]


class Data(BaseModel):
    """The social media profile for the LinkedIn platform"""

    url: str
    """The full URL to the LinkedIn profile."""

    username: str
    """
    The LinkedIn username, including the prefix 'company/' for company pages or
    'in/' for personal profiles.
    """


class SocialLinkedInValue(BaseModel):
    """The social media profile for the LinkedIn platform"""

    data: Data
    """The social media profile for the LinkedIn platform"""

    type: Literal["value/uri/social_linked_in"]
