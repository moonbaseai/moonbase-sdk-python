# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ActivityListParams",
    "ConstituentEntityID",
    "ConstituentEntityType",
    "ConstituentRelation",
    "OccurredAt",
    "Type",
]


class ActivityListParams(TypedDict, total=False):
    after: str
    """
    When specified, returns results starting immediately after the item identified
    by this cursor. Use the cursor value from the previous response's metadata to
    fetch the next page of results.
    """

    before: str
    """
    When specified, returns results starting immediately before the item identified
    by this cursor. Use the cursor value from the response's metadata to fetch the
    previous page of results.
    """

    constituent_entity_id: ConstituentEntityID
    """Filter activities by which entities were involved.

    Must be paired with constituent_entity_type.
    """

    constituent_entity_type: ConstituentEntityType
    """Filter activities by which entities were involved.

    Must be paired with constituent_entity_id.
    """

    constituent_relation: ConstituentRelation
    """Filter activities by which entities were involved via specific relations.

    Must be paired with constituent_entity_type and constituent_entity_id.
    """

    limit: int
    """Maximum number of items to return per page.

    Must be between 1 and 100. Defaults to 20 if not specified.
    """

    occurred_at: OccurredAt
    """Filter activities by when they occurred."""

    type: Type
    """Filter activities by type."""


class ConstituentEntityID(TypedDict, total=False):
    """Filter activities by which entities were involved.

    Must be paired with constituent_entity_type.
    """

    eq: str


class ConstituentEntityType(TypedDict, total=False):
    """Filter activities by which entities were involved.

    Must be paired with constituent_entity_id.
    """

    eq: Literal[
        "call",
        "collection",
        "file",
        "item",
        "meeting",
        "message",
        "note",
        "program",
        "program_message",
        "program_template",
        "unsubscribe",
    ]
    """The type of the entity involved as a constituent of the activity."""


class ConstituentRelation(TypedDict, total=False):
    """Filter activities by which entities were involved via specific relations.

    Must be paired with constituent_entity_type and constituent_entity_id.
    """

    eq: Literal["actor", "object", "target"]


class OccurredAt(TypedDict, total=False):
    """Filter activities by when they occurred."""

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class Type(TypedDict, total=False):
    """Filter activities by type."""

    eq: Literal[
        "activity/call_occurred",
        "activity/form_submitted",
        "activity/inbox_message_sent",
        "activity/item_created",
        "activity/item_mentioned",
        "activity/item_merged",
        "activity/file_created",
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
