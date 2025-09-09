# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FunnelStep"]


class FunnelStep(BaseModel):
    id: str
    """Unique identifier for the object."""

    name: str
    """The name of the step."""

    step_type: Literal["active", "success", "failure"]
    """The type of step, which can be `active`, `success`, or `failure`."""

    type: Literal["funnel_step"]
    """String representing the object’s type. Always `funnel_step` for this object."""
