# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..geo_value_param import GeoValueParam
from ..url_value_param import URLValueParam
from ..email_value_param import EmailValueParam
from ..float_value_param import FloatValueParam
from ..choice_value_param import ChoiceValueParam
from ..domain_value_param import DomainValueParam
from ..boolean_value_param import BooleanValueParam
from ..integer_value_param import IntegerValueParam
from ..monetary_value_param import MonetaryValueParam
from ..social_x_value_param import SocialXValueParam
from ..percentage_value_param import PercentageValueParam
from ..telephone_number_param import TelephoneNumberParam
from ..stage_field_update_params import StageFieldUpdateParams
from ..multi_line_text_value_param import MultiLineTextValueParam
from ..single_line_text_value_param import SingleLineTextValueParam
from ..social_linked_in_value_param import SocialLinkedInValueParam
from ..date_field_default_value_param import DateFieldDefaultValueParam
from ..datetime_field_default_value_param import DatetimeFieldDefaultValueParam
from ..relation_field_default_value_param import RelationFieldDefaultValueParam

__all__ = [
    "FieldUpdateParams",
    "Field",
    "FieldSingleLineTextFieldUpdateParams",
    "FieldMultiLineTextFieldUpdateParams",
    "FieldIntegerFieldUpdateParams",
    "FieldFloatFieldUpdateParams",
    "FieldMonetaryFieldUpdateParams",
    "FieldPercentageFieldUpdateParams",
    "FieldBooleanFieldUpdateParams",
    "FieldEmailFieldUpdateParams",
    "FieldURLFieldUpdateParams",
    "FieldDomainFieldUpdateParams",
    "FieldSocialXFieldUpdateParams",
    "FieldSocialLinkedInFieldUpdateParams",
    "FieldTelephoneNumberFieldUpdateParams",
    "FieldGeoFieldUpdateParams",
    "FieldDateFieldUpdateParams",
    "FieldDatetimeFieldUpdateParams",
    "FieldChoiceFieldUpdateParams",
    "FieldChoiceFieldUpdateParamsOption",
    "FieldRelationFieldUpdateParams",
    "FieldRelationFieldUpdateParamsAllowedCollection",
]


class FieldUpdateParams(TypedDict, total=False):
    collection_id: Required[str]

    field: Required[Field]
    """Parameters for updating a field, discriminated by `type`."""


class FieldSingleLineTextFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a single-line text field."""

    type: Required[Literal["field/text/single_line"]]
    """The field type. Must be `field/text/single_line`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[SingleLineTextValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldMultiLineTextFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a multi-line text field."""

    type: Required[Literal["field/text/multi_line"]]
    """The field type. Must be `field/text/multi_line`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[MultiLineTextValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldIntegerFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating an integer field."""

    type: Required[Literal["field/number/unitless_integer"]]
    """The field type. Must be `field/number/unitless_integer`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[IntegerValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldFloatFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a decimal number field."""

    type: Required[Literal["field/number/unitless_float"]]
    """The field type. Must be `field/number/unitless_float`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[FloatValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldMonetaryFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a monetary field."""

    type: Required[Literal["field/number/monetary"]]
    """The field type. Must be `field/number/monetary`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_unit: str
    """
    The default currency for the field, as a 3-letter ISO 4217 code (e.g., `USD`,
    `EUR`, `GBP`).
    """

    default_values: Optional[Iterable[MonetaryValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldPercentageFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a percentage field."""

    type: Required[Literal["field/number/percentage"]]
    """The field type. Must be `field/number/percentage`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[PercentageValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldBooleanFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a boolean field."""

    type: Required[Literal["field/boolean"]]
    """The field type. Must be `field/boolean`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[BooleanValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldEmailFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating an email field."""

    type: Required[Literal["field/email"]]
    """The field type. Must be `field/email`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[EmailValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldURLFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a URL field."""

    type: Required[Literal["field/uri/url"]]
    """The field type. Must be `field/uri/url`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[URLValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldDomainFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a domain field."""

    type: Required[Literal["field/uri/domain"]]
    """The field type. Must be `field/uri/domain`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[DomainValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldSocialXFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating an X (formerly Twitter) profile field."""

    type: Required[Literal["field/uri/social_x"]]
    """The field type. Must be `field/uri/social_x`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[SocialXValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldSocialLinkedInFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a LinkedIn profile field."""

    type: Required[Literal["field/uri/social_linked_in"]]
    """The field type. Must be `field/uri/social_linked_in`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[SocialLinkedInValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldTelephoneNumberFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a telephone number field."""

    type: Required[Literal["field/telephone_number"]]
    """The field type. Must be `field/telephone_number`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[TelephoneNumberParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldGeoFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a geographic location field."""

    type: Required[Literal["field/geo"]]
    """The field type. Must be `field/geo`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[GeoValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldDateFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a date field."""

    type: Required[Literal["field/date"]]
    """The field type. Must be `field/date`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[DateFieldDefaultValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldDatetimeFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a date and time field."""

    type: Required[Literal["field/datetime"]]
    """The field type. Must be `field/datetime`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[DatetimeFieldDefaultValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldChoiceFieldUpdateParamsOption(TypedDict, total=False):
    """A choice field option.

    Items with an `id` update existing options; items without an `id` are added as new options.
    """

    color: Required[
        Literal[
            "amber",
            "blue",
            "cyan",
            "emerald",
            "fuchsia",
            "green",
            "indigo",
            "lime",
            "lunar",
            "orange",
            "pink",
            "purple",
            "red",
            "rose",
            "sky",
            "teal",
            "violet",
            "yellow",
        ]
    ]
    """The color of the option."""

    name: Required[str]
    """The display name of the option."""

    id: str
    """The ID of an existing option to update. When absent, a new option is created."""


class FieldChoiceFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a choice field."""

    type: Required[Literal["field/choice"]]
    """The field type. Must be `field/choice`."""

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[ChoiceValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    options: Iterable[FieldChoiceFieldUpdateParamsOption]
    """The complete set of options for this field.

    Omit to leave unchanged. Array order determines display order.
    """

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


class FieldRelationFieldUpdateParamsAllowedCollection(TypedDict, total=False):
    """A reference to a `Collection` used in request bodies.

    Provide at least one of `id` or `ref` to identify the collection.
    """

    type: Required[Literal["collection"]]
    """String representing the object’s type. Always `collection` for this object."""

    id: str
    """Unique identifier of the collection."""

    ref: str
    """The stable, machine-readable reference identifier of the collection."""


class FieldRelationFieldUpdateParams(TypedDict, total=False):
    """Parameters for updating a relation field."""

    type: Required[Literal["field/relation"]]
    """The field type. Must be `field/relation`."""

    allowed_collections: Iterable[FieldRelationFieldUpdateParamsAllowedCollection]
    """The complete set of allowed collections.

    Omit to leave unchanged. Array replaces the current set.
    """

    cardinality: Literal["one", "many"]
    """Updated cardinality: `one` or `many`."""

    default_values: Optional[Iterable[RelationFieldDefaultValueParam]]

    description: Optional[str]
    """An updated description, or `null` to clear it."""

    name: str
    """The new name for the field."""

    relation_type: Literal["one_way", "two_way"]
    """
    The type of relationship: `one_way` for simple references, or `two_way` for
    bidirectional relationships.
    """

    required: bool
    """If `true`, items must have a value for this field."""

    unique: bool
    """If `true`, values must be unique across all items."""


Field: TypeAlias = Union[
    FieldSingleLineTextFieldUpdateParams,
    FieldMultiLineTextFieldUpdateParams,
    FieldIntegerFieldUpdateParams,
    FieldFloatFieldUpdateParams,
    FieldMonetaryFieldUpdateParams,
    FieldPercentageFieldUpdateParams,
    FieldBooleanFieldUpdateParams,
    FieldEmailFieldUpdateParams,
    FieldURLFieldUpdateParams,
    FieldDomainFieldUpdateParams,
    FieldSocialXFieldUpdateParams,
    FieldSocialLinkedInFieldUpdateParams,
    FieldTelephoneNumberFieldUpdateParams,
    FieldGeoFieldUpdateParams,
    FieldDateFieldUpdateParams,
    FieldDatetimeFieldUpdateParams,
    FieldChoiceFieldUpdateParams,
    StageFieldUpdateParams,
    FieldRelationFieldUpdateParams,
]
