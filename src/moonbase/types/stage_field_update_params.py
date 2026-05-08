# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .funnel_pointer_param import FunnelPointerParam
from .funnel_step_value_param import FunnelStepValueParam

__all__ = ["StageFieldUpdateParams"]


class StageFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a stage field."""

    type: Required[Literal["field/stage"]]
    """The field type. Must be `field/stage`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[FunnelStepValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    funnel: FunnelPointerParam
    """A new funnel to use for this field, or omit to keep the current funnel."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""
