# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChoiceParam", "Option"]


class Option(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["field_option"]]

    label: str


class ChoiceParam(TypedDict, total=False):
    option: Required[Option]

    type: Required[Literal["value/choice"]]
