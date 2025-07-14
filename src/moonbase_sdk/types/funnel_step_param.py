# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FunnelStepParam", "Step"]


class Step(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["funnel_step"]]

    name: str


class FunnelStepParam(TypedDict, total=False):
    step: Required[Step]

    type: Required[Literal["value/funnel_step"]]
