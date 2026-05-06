# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .funnel_pointer_param import FunnelPointerParam
from .funnel_step_value_param import FunnelStepValueParam

__all__ = ["StageFieldCreateParams"]


class StageFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a stage field."""

    funnel: Required[FunnelPointerParam]
    """The funnel that defines the available stages for this field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/stage"]]
    """The field type. Must be `field/stage`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[FunnelStepValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""
