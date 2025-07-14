# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Field", "Links", "FieldOption", "Funnel", "FunnelStep"]


class Links(BaseModel):
    collection: str
    """The `Collection` this field belongs to."""

    self: str
    """The canonical URL for this object."""


class FieldOption(BaseModel):
    id: str
    """Unique identifier for the object."""

    label: str
    """The human-readable text for the option."""

    type: Literal["field_option"]
    """String representing the object’s type. Always `field_option` for this object."""


class FunnelStep(BaseModel):
    id: str
    """Unique identifier for the object."""

    name: str
    """The name of the step."""

    type: Literal["funnel_step/active", "funnel_step/success", "funnel_step/failure"]
    """
    The type of step, which can be `funnel_step/active`, `funnel_step/success`, or
    `funnel_step/failure`.
    """


class Funnel(BaseModel):
    id: str
    """Unique identifier for the object."""

    type: Literal["funnel"]
    """String representing the object’s type. Always `funnel` for this object."""

    steps: Optional[List[FunnelStep]] = None
    """An ordered list of `FunnelStep` objects that make up the funnel."""


class Field(BaseModel):
    id: str
    """Unique identifier for the object."""

    cardinality: Literal["one", "many"]
    """
    Specifies whether the field can hold a single value (`one`) or multiple values
    (`many`).
    """

    links: Links

    name: str
    """The human-readable name of the field (e.g., “Due Date”)."""

    ref: str
    """
    A unique, stable, machine-readable identifier for the field within its
    collection (e.g., `due_date`).
    """

    type: Literal[
        "field/text/single_line",
        "field/text/multi_line",
        "field/number/unitless_integer",
        "field/number/unitless_float",
        "field/number/monetary",
        "field/number/percentage",
        "field/boolean",
        "field/email",
        "field/uri/url",
        "field/uri/domain",
        "field/uri/social_x",
        "field/uri/social_linked_in",
        "field/telephone_number",
        "field/geo",
        "field/date",
        "field/datetime",
        "field/choice",
        "field/stage",
        "field/relation/one_way",
        "field/relation/two_way",
    ]
    """The data type of the field.

    This determines how values are stored, validated, and rendered.
    """

    created_at: Optional[datetime] = None
    """Time at which the object was created, as an RFC 3339 timestamp."""

    description: Optional[str] = None
    """An optional, longer-form description of the field's purpose."""

    field_options: Optional[List[FieldOption]] = None
    """
    If the field `type` is `field/choice`, this is the list of available
    `FieldOption` objects.
    """

    funnel: Optional[Funnel] = None
    """If the field `type` is `field/stage`, this is the associated `Funnel` object."""

    readonly: Optional[bool] = None
    """
    If `true`, the value of this field is system-managed and cannot be updated via
    the API.
    """

    required: Optional[bool] = None
    """If `true`, this field must have a value."""

    unique: Optional[bool] = None
    """
    If `true`, values for this field must be unique across all items in the
    collection.
    """

    updated_at: Optional[datetime] = None
    """Time at which the object was last updated, as an RFC 3339 timestamp."""
