# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .program_activity_metrics import ProgramActivityMetrics

__all__ = ["Program"]


class Program(BaseModel):
    """The Program object represents an email campaign.

    It defines the sending behavior and tracks engagement metrics.
    """

    id: str
    """Unique identifier for the object."""

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    status: Literal["draft", "published", "paused", "archived"]
    """The current status of the program.

    Can be `draft`, `published`, `paused`, or `archived`.
    """

    track_clicks: bool
    """`true` if link clicks are tracked for this program."""

    track_opens: bool
    """`true` if email opens are tracked for this program."""

    trigger: Literal["api", "broadcast"]
    """The sending trigger for the program.

    Can be `api` for transactional sends or `broadcast` for scheduled sends.
    """

    type: Literal["program"]
    """String representing the object’s type. Always `program` for this object."""

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""

    activity_metrics: Optional[ProgramActivityMetrics] = None
    """A `ProgramActivityMetrics` object summarizing engagement for this program.

    **Note:** Only present when requested using the `include` query parameter.
    """

    display_name: Optional[str] = None
    """The user-facing name of the program."""

    program_template: Optional["ProgramTemplate"] = None
    """The `ProgramTemplate` used for messages in this program.

    **Note:** Only present when requested using the `include` query parameter.
    """

    scheduled_at: Optional[datetime] = None
    """
    For `broadcast` programs, the time the program is scheduled to send, as an ISO
    8601 timestamp in UTC.
    """


from .program_template import ProgramTemplate
