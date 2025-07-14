# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MonetaryValueParam", "Amount"]


class Amount(TypedDict, total=False):
    amount_in_minor_units: Required[int]

    currency: Required[str]

    type: Required[Literal["currency"]]


class MonetaryValueParam(TypedDict, total=False):
    amount: Required[Amount]

    type: Required[Literal["value/number/monetary"]]
