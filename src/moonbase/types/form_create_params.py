# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FormCreateParams"]


class FormCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the form, used as the title on its public page."""

    business_email_required: bool
    """If `true`, submissions require a business email address. Defaults to `false`."""

    pages_enabled: bool
    """
    If `true`, enables a Moonbase Pages hosted page for this form, providing a
    standalone public URL for sharing. Defaults to `false`.
    """

    redirect_url: str
    """Optional URL the user is redirected to after a successful submission.

    Omit to leave submissions without a redirect. Stored as a Liquid template;
    rendered at submission time with form field values under `submission.<key>`
    (keyed by the field's `key`) plus UTM params (`utm_source`, `utm_medium`,
    `utm_campaign`, `utm_term`, `utm_content`) automatically appended. Use the
    `uri_encode` filter for URL-safe values, e.g.
    `https://example.com/thanks?email={{ submission.email | uri_encode }}`. The
    rendered URL must parse as a valid URL or the submission errors.
    """
