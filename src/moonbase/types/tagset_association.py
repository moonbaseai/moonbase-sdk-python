# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["TagsetAssociation", "TagsetCallsAssociation", "TagsetMeetingsAssociation", "TagsetInboxAssociation"]


class TagsetCallsAssociation(BaseModel):
    """Makes this tagset available for calls."""

    type: Literal["calls"]
    """String representing the association type.

    Always `calls` for call tagset associations.
    """


class TagsetMeetingsAssociation(BaseModel):
    """Makes this tagset available for meetings."""

    type: Literal["meetings"]
    """String representing the association type.

    Always `meetings` for meeting tagset associations.
    """


class TagsetInboxAssociation(BaseModel):
    """Makes this tagset available in an inbox."""

    id: str
    """Unique identifier of the inbox this tagset is assigned to."""

    type: Literal["inbox"]
    """String representing the association type.

    Always `inbox` for inbox tagset associations.
    """


TagsetAssociation: TypeAlias = Annotated[
    Union[TagsetCallsAssociation, TagsetMeetingsAssociation, TagsetInboxAssociation], PropertyInfo(discriminator="type")
]
