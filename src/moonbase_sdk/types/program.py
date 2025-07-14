# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["Program", "Links", "ActivityMetrics"]


class Links(BaseModel):
    program_template: str
    """A link to the `ProgramTemplate` for this program."""

    self: str
    """The canonical URL for this object."""


class ActivityMetrics(BaseModel):
    bounced: Optional[int] = None
    """The number of emails that could not be delivered."""

    clicked: Optional[int] = None
    """The number of recipients who clicked at least one link."""

    complained: Optional[int] = None
    """The number of recipients who marked the email as spam."""

    failed: Optional[int] = None
    """The number of emails that failed to send due to a technical issue."""

    opened: Optional[int] = None
    """The number of recipients who opened the email."""

    sent: Optional[int] = None
    """The total number of emails successfully sent."""

    shielded: Optional[int] = None
    """The number of emails blocked by delivery protection rules."""

    unsubscribed: Optional[int] = None
    """The number of recipients who unsubscribed."""


class Program(BaseModel):
    id: str
    """Unique identifier for the object."""

    links: Links

    status: Literal["draft", "published", "paused", "archived"]
    """The current status of the program.

    Can be `draft`, `published`, `paused`, or `archived`.
    """

    trigger: Literal["api", "broadcast"]
    """The sending trigger for the program.

    Can be `api` for transactional sends or `broadcast` for scheduled sends.
    """

    type: Literal["program"]
    """String representing the object’s type. Always `program` for this object."""

    activity_metrics: Optional[ActivityMetrics] = None
    """A `ProgramActivityMetrics` object summarizing engagement for this program."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    display_name: Optional[str] = None
    """The user-facing name of the program."""

    program_template: Optional["ProgramTemplate"] = None
    """The `ProgramTemplate` used for messages in this program."""

    scheduled_at: Optional[datetime] = None
    """
    For `broadcast` programs, the time the program is scheduled to send, as an RFC
    3339 timestamp.
    """

    track_clicks: Optional[bool] = None
    """`true` if link clicks are tracked for this program."""

    track_opens: Optional[bool] = None
    """`true` if email opens are tracked for this program."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""


from .program_template import ProgramTemplate

if PYDANTIC_V2:
    Program.model_rebuild()
    Links.model_rebuild()
    ActivityMetrics.model_rebuild()
else:
    Program.update_forward_refs()  # type: ignore
    Links.update_forward_refs()  # type: ignore
    ActivityMetrics.update_forward_refs()  # type: ignore
