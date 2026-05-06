# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FormUpdateParams"]


class FormUpdateParams(TypedDict, total=False):
    business_email_required: bool
    """If `true`, submissions require a business email address."""

    name: str
    """The new name for the form."""

    pages_enabled: bool
    """
    If `true`, a Moonbase Pages hosted page is enabled for this form, providing a
    standalone public URL for sharing.
    """

    redirect_url: Optional[str]
    """Updated redirect URL, or `null` to clear.

    Omit to leave the existing value unchanged. Liquid template rendered at
    submission time with form field values under `submission.<key>` (keyed by the
    field's `key`) plus UTM params (`utm_source`, `utm_medium`, `utm_campaign`,
    `utm_term`, `utm_content`) automatically appended. Use the `uri_encode` filter
    for URL-safe values. The rendered URL must parse as a valid URL or the
    submission errors.
    """
