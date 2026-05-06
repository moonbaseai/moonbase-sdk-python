# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageAttachment"]


class MessageAttachment(BaseModel):
    """The Attachment object represents a file attached to a message.

    You can download the file content via the `download_url`.
    """

    id: str
    """Unique identifier for the object."""

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    download_url: str
    """A temporary, signed URL to download the file content.

    The URL expires after one hour.
    """

    filename: str
    """The original name of the uploaded file, including its extension."""

    size: int
    """The size of the file in bytes."""

    type: Literal["message_attachment"]
    """String representing the object’s type.

    Always `message_attachment` for this object.
    """
