# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FunnelStep", "Step"]


class Step(BaseModel):
    id: str

    type: Literal["funnel_step"]

    name: Optional[str] = None


class FunnelStep(BaseModel):
    step: Step

    type: Literal["value/funnel_step"]
