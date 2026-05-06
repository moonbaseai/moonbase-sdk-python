# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .constituent import Constituent

__all__ = ["Activity"]


class Activity(BaseModel):
    """
    The Activity object represents a specific event that has occurred, such as a meeting being scheduled or a form being submitted.
    """

    id: str
    """Unique identifier for the object."""

    constituents: List[Constituent]
    """
    An array of entities involved along with each entity's relation to the activity.
    """

    occurred_at: datetime
    """The time at which the event occurred, as an ISO 8601 timestamp in UTC."""

    type: Literal[
        "activity/call_occurred",
        "activity/file_created",
        "activity/form_submitted",
        "activity/inbox_message_sent",
        "activity/item_created",
        "activity/item_mentioned",
        "activity/item_merged",
        "activity/meeting_held",
        "activity/meeting_scheduled",
        "activity/note_created",
        "activity/program_message_bounced",
        "activity/program_message_clicked",
        "activity/program_message_complained",
        "activity/program_message_failed",
        "activity/program_message_opened",
        "activity/program_message_sent",
        "activity/program_message_shielded",
        "activity/program_message_unsubscribed",
    ]
    """The type of activity."""
