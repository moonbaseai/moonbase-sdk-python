# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .field_pointer import FieldPointer
from .collection_pointer import CollectionPointer
from .field_default_value import FieldDefaultValue

__all__ = ["RelationField"]


class RelationField(BaseModel):
    """
    A field that creates a link between items in different collections, enabling cross-collection relationships.
    """

    id: str
    """Unique identifier for the object."""

    allowed_collections: List[CollectionPointer]
    """The set of collections that are valid targets for this relation."""

    cardinality: Literal["one", "many"]
    """
    Specifies whether the field can hold a single value (`one`) or multiple values
    (`many`).
    """

    created_at: datetime
    """Time at which the object was created, as an ISO 8601 timestamp in UTC."""

    default_values: List[FieldDefaultValue]

    kind: Literal["system", "inverse", "custom"]
    """
    `system` fields are managed by Moonbase, `inverse` fields are the reverse side
    of a two-way relation, and `custom` fields are user-created.
    """

    name: str
    """The human-readable name of the field (e.g., "Account")."""

    readonly: bool
    """
    If `true`, the value of this field is system-managed and cannot be updated via
    the API.
    """

    ref: str
    """
    A unique, stable, machine-readable identifier for the field within its
    collection (e.g., `account`).
    """

    relation_type: Literal["one_way", "two_way"]
    """The type of relationship.

    Can be `one_way` for simple references or `two_way` for bidirectional
    relationships.
    """

    required: bool
    """If `true`, this field must have a value."""

    type: Literal["field/relation"]
    """The data type of the field. Always `field/relation` for this field."""

    unique: bool
    """
    If `true`, values for this field must be unique across all items in the
    collection.
    """

    updated_at: datetime
    """Time at which the object was last updated, as an ISO 8601 timestamp in UTC."""

    description: Optional[str] = None
    """An optional, longer-form description of the field's purpose."""

    reverse_field_name: Optional[str] = None
    """The name given to auto-created reverse fields on target collections.

    Only present on `two_way` source fields.
    """

    reverse_fields: Optional[List[FieldPointer]] = None
    """A list of reverse fields created on each target collection.

    Only present on `two_way` source fields.
    """

    source_field: Optional[FieldPointer] = None
    """A reference to the source field that manages this reverse field.

    Only present on reverse (contingent) fields.
    """
