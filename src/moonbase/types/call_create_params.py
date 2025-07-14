# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallCreateParams", "Participant"]


class CallCreateParams(TypedDict, total=False):
    direction: Required[Literal["incoming", "outgoing"]]
    """The direction of the call, either `incoming` or `outgoing`."""

    participants: Required[Iterable[Participant]]
    """An array of participants involved in the call."""

    provider: Required[str]
    """The name of the phone provider that handled the call (e.g., `openphone`)."""

    provider_id: Required[str]
    """The unique identifier for the call from the provider's system."""

    start_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The time the call started, as an RFC 3339 timestamp."""

    status: Required[
        Literal[
            "queued",
            "initiated",
            "ringing",
            "in_progress",
            "completed",
            "busy",
            "failed",
            "no_answer",
            "canceled",
            "missed",
            "answered",
            "forwarded",
            "abandoned",
        ]
    ]
    """The status of the call."""

    answered_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time the call was answered, as an RFC 3339 timestamp."""

    end_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time the call ended, as an RFC 3339 timestamp."""

    provider_metadata: Dict[str, object]
    """A hash of additional metadata from the provider."""


class Participant(TypedDict, total=False):
    phone: Required[str]
    """The E.164 formatted phone number of the participant."""

    role: Required[Literal["caller", "callee", "other"]]
    """The role of the participant in the call. Can be `caller`, `callee`, or `other`."""
