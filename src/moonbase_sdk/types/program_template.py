# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["ProgramTemplate", "Links"]


class Links(BaseModel):
    self: str
    """The canonical URL for this object."""

    program: Optional[str] = None
    """A link to the `Program` using this template."""


class ProgramTemplate(BaseModel):
    id: str
    """Unique identifier for the object."""

    body: str
    """The body content of the email, which can include Liquid variables."""

    links: Links

    subject: str
    """The subject line of the email, which can include Liquid variables."""

    type: Literal["program_template"]
    """String representing the object’s type.

    Always `program_template` for this object.
    """

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    program: Optional["Program"] = None
    """The `Program` that uses this template."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""


from .program import Program

if PYDANTIC_V2:
    ProgramTemplate.model_rebuild()
    Links.model_rebuild()
else:
    ProgramTemplate.update_forward_refs()  # type: ignore
    Links.update_forward_refs()  # type: ignore
