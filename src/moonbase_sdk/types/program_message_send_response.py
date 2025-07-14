# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["ProgramMessageSendResponse", "Links"]


class Links(BaseModel):
    program_template: str
    """A link to the `ProgramTemplate` used."""


class ProgramMessageSendResponse(BaseModel):
    id: str
    """Unique identifier for the object."""

    created_at: datetime
    """
    Time at which the message was created and enqueued for sending, as an RFC 3339
    timestamp.
    """

    links: Links

    program_template: "ProgramTemplate"
    """The `ProgramTemplate` used to generate this message."""

    type: Literal["program_message"]
    """String representing the object’s type.

    Always `program_message` for this object.
    """

    updated_at: datetime
    """Time at which the object was last updated, as an RFC 3339 timestamp."""


from .program_template import ProgramTemplate

if PYDANTIC_V2:
    ProgramMessageSendResponse.model_rebuild()
    Links.model_rebuild()
else:
    ProgramMessageSendResponse.update_forward_refs()  # type: ignore
    Links.update_forward_refs()  # type: ignore
