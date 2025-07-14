# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union
from typing_extensions import TypeAlias, TypeAliasType

from .choice import Choice
from .._compat import PYDANTIC_V2
from .geo_value import GeoValue
from .url_value import URLValue
from .date_value import DateValue
from .email_value import EmailValue
from .float_value import FloatValue
from .funnel_step import FunnelStep
from .domain_value import DomainValue
from .boolean_value import BooleanValue
from .integer_value import IntegerValue
from .datetime_value import DatetimeValue
from .monetary_value import MonetaryValue
from .social_x_value import SocialXValue
from .percentage_value import PercentageValue
from .telephone_number import TelephoneNumber
from .multi_line_text_value import MultiLineTextValue
from .single_line_text_value import SingleLineTextValue
from .social_linked_in_value import SocialLinkedInValue

__all__ = ["FieldValue"]

if TYPE_CHECKING or PYDANTIC_V2:
    FieldValue = TypeAliasType(
        "FieldValue",
        Union[
            SingleLineTextValue,
            MultiLineTextValue,
            IntegerValue,
            FloatValue,
            MonetaryValue,
            PercentageValue,
            BooleanValue,
            EmailValue,
            URLValue,
            DomainValue,
            SocialXValue,
            SocialLinkedInValue,
            TelephoneNumber,
            GeoValue,
            DateValue,
            DatetimeValue,
            Choice,
            FunnelStep,
            "RelationValue",
            List["Value"],
        ],
    )
else:
    FieldValue: TypeAlias = Union[
        SingleLineTextValue,
        MultiLineTextValue,
        IntegerValue,
        FloatValue,
        MonetaryValue,
        PercentageValue,
        BooleanValue,
        EmailValue,
        URLValue,
        DomainValue,
        SocialXValue,
        SocialLinkedInValue,
        TelephoneNumber,
        GeoValue,
        DateValue,
        DatetimeValue,
        Choice,
        FunnelStep,
        "RelationValue",
        List["Value"],
    ]

from .value import Value
from .relation_value import RelationValue
