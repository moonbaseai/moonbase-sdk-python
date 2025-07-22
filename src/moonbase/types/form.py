# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Form", "Links"]


class Links(BaseModel):
    self: str
    """The canonical URL for this object."""

    collection: Optional[str] = None
    """A link to the `Collection` where form submissions are saved."""


class Form(BaseModel):
    id: str
    """Unique identifier for the object."""

    collection: "Collection"
    """The `Collection` that submissions to this form are saved to."""

    links: Links

    name: str
    """The name of the form, used as the title on its public page."""

    type: Literal["form"]
    """String representing the object’s type. Always `form` for this object."""

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    pages_enabled: Optional[bool] = None
    """`true` if the form is available at a public URL."""

    pages_url: Optional[str] = None
    """The public URL for the form, if `pages_enabled` is `true`."""

    redirect_url: Optional[str] = None
    """An optional URL to redirect users to after a successful submission."""

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""


from .collection import Collection
