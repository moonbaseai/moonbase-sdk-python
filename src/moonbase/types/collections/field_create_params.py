# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
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
from ..stage_field_create_params import StageFieldCreateParams
from ..multi_line_text_value_param import MultiLineTextValueParam
from ..single_line_text_value_param import SingleLineTextValueParam
from ..social_linked_in_value_param import SocialLinkedInValueParam
from ..date_field_default_value_param import DateFieldDefaultValueParam
from ..datetime_field_default_value_param import DatetimeFieldDefaultValueParam
from ..relation_field_default_value_param import RelationFieldDefaultValueParam

__all__ = [
    "FieldCreateParams",
    "Field",
    "FieldSingleLineTextFieldCreateParams",
    "FieldMultiLineTextFieldCreateParams",
    "FieldIntegerFieldCreateParams",
    "FieldFloatFieldCreateParams",
    "FieldMonetaryFieldCreateParams",
    "FieldPercentageFieldCreateParams",
    "FieldBooleanFieldCreateParams",
    "FieldEmailFieldCreateParams",
    "FieldURLFieldCreateParams",
    "FieldDomainFieldCreateParams",
    "FieldSocialXFieldCreateParams",
    "FieldSocialLinkedInFieldCreateParams",
    "FieldTelephoneNumberFieldCreateParams",
    "FieldGeoFieldCreateParams",
    "FieldDateFieldCreateParams",
    "FieldDatetimeFieldCreateParams",
    "FieldChoiceFieldCreateParams",
    "FieldChoiceFieldCreateParamsOption",
    "FieldRelationFieldCreateParams",
    "FieldRelationFieldCreateParamsAllowedCollection",
]


class FieldCreateParams(TypedDict, total=False):
    field: Required[Field]
    """Parameters for creating a field, discriminated by `type`."""


class FieldSingleLineTextFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a single-line text field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/text/single_line"]]
    """The field type. Must be `field/text/single_line`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[SingleLineTextValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldMultiLineTextFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a multi-line text field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/text/multi_line"]]
    """The field type. Must be `field/text/multi_line`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[MultiLineTextValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldIntegerFieldCreateParams(TypedDict, total=False):
    """Parameters for creating an integer field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/number/unitless_integer"]]
    """The field type. Must be `field/number/unitless_integer`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[IntegerValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldFloatFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a decimal number field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/number/unitless_float"]]
    """The field type. Must be `field/number/unitless_float`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[FloatValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldMonetaryFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a monetary field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/number/monetary"]]
    """The field type. Must be `field/number/monetary`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_unit: str
    """
    The default currency for the field, as a 3-letter ISO 4217 code (e.g., `USD`,
    `EUR`, `GBP`).
    """

    default_values: Iterable[MonetaryValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldPercentageFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a percentage field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/number/percentage"]]
    """The field type. Must be `field/number/percentage`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[PercentageValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldBooleanFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a boolean field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/boolean"]]
    """The field type. Must be `field/boolean`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[BooleanValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldEmailFieldCreateParams(TypedDict, total=False):
    """Parameters for creating an email field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/email"]]
    """The field type. Must be `field/email`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[EmailValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldURLFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a URL field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/uri/url"]]
    """The field type. Must be `field/uri/url`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[URLValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldDomainFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a domain field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/uri/domain"]]
    """The field type. Must be `field/uri/domain`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[DomainValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldSocialXFieldCreateParams(TypedDict, total=False):
    """Parameters for creating an X (formerly Twitter) profile field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/uri/social_x"]]
    """The field type. Must be `field/uri/social_x`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[SocialXValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldSocialLinkedInFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a LinkedIn profile field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/uri/social_linked_in"]]
    """The field type. Must be `field/uri/social_linked_in`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[SocialLinkedInValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldTelephoneNumberFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a telephone number field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/telephone_number"]]
    """The field type. Must be `field/telephone_number`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[TelephoneNumberParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldGeoFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a geographic location field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/geo"]]
    """The field type. Must be `field/geo`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[GeoValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldDateFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a date field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/date"]]
    """The field type. Must be `field/date`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[DateFieldDefaultValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldDatetimeFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a date and time field."""

    name: Required[str]
    """The human-readable name for the field."""

    type: Required[Literal["field/datetime"]]
    """The field type. Must be `field/datetime`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[DatetimeFieldDefaultValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldChoiceFieldCreateParamsOption(TypedDict, total=False):
    """Parameters for defining an option in a choice field."""

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


class FieldChoiceFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a choice field with predefined options."""

    name: Required[str]
    """The human-readable name for the field."""

    options: Required[Iterable[FieldChoiceFieldCreateParamsOption]]
    """A list of options to create for the field. Each option must have a `name`."""

    type: Required[Literal["field/choice"]]
    """The field type. Must be `field/choice`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[ChoiceValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


class FieldRelationFieldCreateParamsAllowedCollection(TypedDict, total=False):
    """A reference to a `Collection` used in request bodies.

    Provide at least one of `id` or `ref` to identify the collection.
    """

    type: Required[Literal["collection"]]
    """String representing the object’s type. Always `collection` for this object."""

    id: str
    """Unique identifier of the collection."""

    ref: str
    """The stable, machine-readable reference identifier of the collection."""


class FieldRelationFieldCreateParams(TypedDict, total=False):
    """Parameters for creating a relation field that links items across collections."""

    allowed_collections: Required[Iterable[FieldRelationFieldCreateParamsAllowedCollection]]
    """
    A list of collection IDs or `ref` values that are valid targets for this
    relation.
    """

    name: Required[str]
    """The human-readable name for the field."""

    relation_type: Required[Literal["one_way", "two_way"]]
    """
    The type of relationship: `one_way` for simple references, or `two_way` for
    bidirectional relationships.
    """

    type: Required[Literal["field/relation"]]
    """The field type. Must be `field/relation`."""

    cardinality: Literal["one", "many"]
    """Whether the field holds a single value (`one`) or multiple values (`many`).

    Defaults to `one`.
    """

    default_values: Iterable[RelationFieldDefaultValueParam]

    description: str
    """An optional description of the field's purpose."""

    required: bool
    """If `true`, items must have a value for this field. Defaults to `false`."""

    reverse_field_name: str
    """
    For `two_way` relations, the name of the reverse field created on the target
    collection.
    """

    unique: bool
    """If `true`, values must be unique across all items. Defaults to `false`."""


Field: TypeAlias = Union[
    FieldSingleLineTextFieldCreateParams,
    FieldMultiLineTextFieldCreateParams,
    FieldIntegerFieldCreateParams,
    FieldFloatFieldCreateParams,
    FieldMonetaryFieldCreateParams,
    FieldPercentageFieldCreateParams,
    FieldBooleanFieldCreateParams,
    FieldEmailFieldCreateParams,
    FieldURLFieldCreateParams,
    FieldDomainFieldCreateParams,
    FieldSocialXFieldCreateParams,
    FieldSocialLinkedInFieldCreateParams,
    FieldTelephoneNumberFieldCreateParams,
    FieldGeoFieldCreateParams,
    FieldDateFieldCreateParams,
    FieldDatetimeFieldCreateParams,
    FieldChoiceFieldCreateParams,
    StageFieldCreateParams,
    FieldRelationFieldCreateParams,
]
