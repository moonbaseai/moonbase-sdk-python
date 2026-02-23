# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ItemSearchParams"]


class ItemSearchParams(TypedDict, total=False):
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

    limit: int
    """Maximum number of items to return per page.

    Must be between 1 and 100. Defaults to 20 if not specified.
    """

    filter: "ItemsFilterParam"
    """Return only items that match the filter conditions.

    Complex filters can be created by nesting filters inside of `AND`, `OR`, and
    `NOT` filters.
    """

    include: SequenceNotStr[str]
    """Include only specific fields in the returned items.

    Specify fields by id or key.
    """

    sort: SequenceNotStr[str]
    """Sort items by the specified field ids or keys.

    Prefix a field with a hyphen/minus (`-`) to sort in descending order by that
    field.
    """


from ..items_filter_param import ItemsFilterParam
