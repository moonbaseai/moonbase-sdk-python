# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .constituent_entity_pointer import ConstituentEntityPointer

__all__ = ["Constituent"]


class Constituent(BaseModel):
    """
    The Constituent object represents information about something that was involved in a particular activity.
    """

    entity: ConstituentEntityPointer
    """
    A lightweight reference to the entity of `Constituent`, containing information
    about what type of entity it is as well as the entity's id.
    """

    relation: Literal["actor", "object", "target"]

    type: Literal["constituent"]
