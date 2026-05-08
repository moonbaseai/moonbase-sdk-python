# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .funnel_step_pointer_param import FunnelStepPointerParam

__all__ = ["FunnelStepValueParam"]


class FunnelStepValueParam(TypedDict, total=False):
    """Funnel step value"""

    data: Required[FunnelStepPointerParam]
    """A specific funnel step, as configured on the Funnel."""

    type: Required[Literal["value/funnel_step"]]
