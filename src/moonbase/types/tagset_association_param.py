# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["TagsetAssociationParam", "TagsetCallsAssociation", "TagsetMeetingsAssociation", "TagsetInboxAssociation"]


class TagsetCallsAssociation(TypedDict, total=False):
    """Makes this tagset available for calls."""

    type: Required[Literal["calls"]]
    """String representing the association type.

    Always `calls` for call tagset associations.
    """


class TagsetMeetingsAssociation(TypedDict, total=False):
    """Makes this tagset available for meetings."""

    type: Required[Literal["meetings"]]
    """String representing the association type.

    Always `meetings` for meeting tagset associations.
    """


class TagsetInboxAssociation(TypedDict, total=False):
    """Makes this tagset available in an inbox."""

    id: Required[str]
    """Unique identifier of the inbox this tagset is assigned to."""

    type: Required[Literal["inbox"]]
    """String representing the association type.

    Always `inbox` for inbox tagset associations.
    """


TagsetAssociationParam: TypeAlias = Union[TagsetCallsAssociation, TagsetMeetingsAssociation, TagsetInboxAssociation]
