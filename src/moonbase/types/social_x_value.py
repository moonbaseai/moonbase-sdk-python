# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SocialXValue", "Profile"]


class Profile(BaseModel):
    url: Optional[str] = None

    username: Optional[str] = None


class SocialXValue(BaseModel):
    profile: Profile

    type: Literal["value/uri/social_x"]
