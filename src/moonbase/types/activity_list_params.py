# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ActivityListParams", "Filter", "FilterItemID", "FilterOccurredAt", "FilterType"]


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

    filter: Filter
    """Filter activities by type, date, or item."""

    limit: int
    """Maximum number of items to return per page.

    Must be between 1 and 100. Defaults to 20 if not specified.
    """


class FilterItemID(TypedDict, total=False):
    eq: str


class FilterOccurredAt(TypedDict, total=False):
    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


_FilterTypeReservedKeywords = TypedDict(
    "_FilterTypeReservedKeywords",
    {
        "in": List[
            Literal[
                "activity/call_occurred",
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
        ],
    },
    total=False,
)


class FilterType(_FilterTypeReservedKeywords, total=False):
    pass


class Filter(TypedDict, total=False):
    """Filter activities by type, date, or item."""

    item_id: FilterItemID

    occurred_at: FilterOccurredAt

    type: FilterType
