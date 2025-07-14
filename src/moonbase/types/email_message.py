# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .address import Address
from .._models import BaseModel
from .inbox_conversation import InboxConversation

__all__ = ["EmailMessage", "Links", "Attachment", "AttachmentLinks"]


class Links(BaseModel):
    conversation: str
    """A link to the `Conversation` this message belongs to."""

    self: str
    """The canonical URL for this object."""


class AttachmentLinks(BaseModel):
    conversation: str
    """A link to the `Conversation` this attachment belongs to."""

    download_url: str
    """A temporary, signed URL to download the file content.

    The URL expires after one hour.
    """

    message: str
    """A link to the `Message` this attachment belongs to."""


class Attachment(BaseModel):
    id: str
    """Unique identifier for the object."""

    filename: str
    """The original name of the uploaded file, including its extension."""

    links: AttachmentLinks
    """A hash of related links."""

    size: int
    """The size of the file in bytes."""

    type: Literal["attachment"]
    """String representing the object’s type. Always `attachment` for this object."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    updated_at: Optional[str] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""


class EmailMessage(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: Links

    rfc822_message_id: str
    """The globally unique `Message-ID` header of the email."""

    subject: str
    """The subject line of the email."""

    type: Literal["email_message"]
    """String representing the object’s type. Always `email_message` for this object."""

    addresses: Optional[List[Address]] = None
    """
    A list of `Address` objects associated with the message (sender and recipients).
    """

    attachments: Optional[List[Attachment]] = None
    """A list of `Attachment` objects on the message."""

    body_html: Optional[str] = None
    """The HTML content of the email body."""

    body_plain: Optional[str] = None
    """The plain text content of the email body."""

    bulk: Optional[bool] = None
    """`true` if the message appears to be part of a bulk mailing."""

    conversation: Optional[InboxConversation] = None
    """The `Conversation` thread this message is part of."""

    created_at: Optional[datetime] = None
    """The time the message was received, as an RFC 3339 timestamp."""

    draft: Optional[bool] = None
    """`true` if the message is a draft that has not been sent."""

    in_reply_to_rfc822_message_id: Optional[str] = None
    """The `Message-ID` of the email this message is a reply to."""

    spam: Optional[bool] = None
    """`true` if the message is classified as spam."""

    summary: Optional[str] = None
    """A concise, system-generated summary of the email content."""

    trash: Optional[bool] = None
    """`true` if the message is in the trash."""

    unread: Optional[bool] = None
    """`true` if the message has not been read."""
