# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .choice_field_option_pointer_param import ChoiceFieldOptionPointerParam

__all__ = ["ChoiceValueParam"]


class ChoiceValueParam(TypedDict, total=False):
    """Selected choice option"""

    data: Required[ChoiceFieldOptionPointerParam]
    """An option that must match one of the predefined options for the field."""

    type: Required[Literal["value/choice"]]
