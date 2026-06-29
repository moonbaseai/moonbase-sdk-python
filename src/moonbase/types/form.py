# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .collection import Collection

__all__ = ["Form"]


class Form(BaseModel):
    """
    A Form provides a way to create `Items` in a `Collection`, often via a public URL for external users. Each form submission creates a new item.
    """

    id: str
    """Unique identifier for the object."""

    business_email_required: bool
    """
    `true` if submissions require a business email address, blocking free and
    disposable providers.
    """

    collection: Collection
    """The `Collection` that submissions to this form are saved to."""

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    name: str
    """The name of the form, used as the title on its public page."""

    pages_enabled: bool
    """
    If `true`, a Moonbase Pages hosted page is enabled for this form, providing a
    standalone public URL for sharing.
    """

    type: Literal["form"]
    """String representing the object’s type. Always `form` for this object."""

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""

    pages_url: Optional[str] = None
    """The public URL for the form, if `pages_enabled` is `true`."""

    redirect_url: Optional[str] = None
    """Optional URL the user is redirected to after a successful submission.

    When unset, no redirect occurs. Stored as a Liquid template; rendered at
    submission time with form field values under `submission.<key>` (keyed by the
    field's `key`) plus UTM params (`utm_source`, `utm_medium`, `utm_campaign`,
    `utm_term`, `utm_content`) automatically appended. Use the `uri_encode` filter
    for URL-safe values, e.g.
    `https://example.com/thanks?email={{ submission.email | uri_encode }}`. The
    rendered URL must parse as a valid URL or the submission errors.
    """
