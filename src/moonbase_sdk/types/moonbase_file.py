# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MoonbaseFile", "Links"]


class Links(BaseModel):
    download_url: str
    """A temporary, signed URL to download the file content.

    The URL expires after one hour.
    """

    self: str
    """The canonical URL for this object."""


class MoonbaseFile(BaseModel):
    id: str
    """Unique identifier for the object."""

    filename: str
    """The original filename of the uploaded file."""

    links: Links

    name: str
    """The display name of the file."""

    size: float
    """The size of the file in bytes."""

    type: Literal["file"]
    """String representing the object’s type. Always `file` for this object."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
