# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.formatted_text import FormattedText
from .note_association_param_pointer_param import NoteAssociationParamPointerParam

__all__ = ["NoteCreateParams"]


class NoteCreateParams(TypedDict, total=False):
    body: Required[FormattedText]
    """The main content of the note."""

    associations: Iterable[NoteAssociationParamPointerParam]
    """
    Link the Note to Moonbase items (person, organization, deal, task, or an item in
    a custom collection), meetings, or calls.
    """
