# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V2
from .choice_param import ChoiceParam
from .geo_value_param import GeoValueParam
from .url_value_param import URLValueParam
from .date_value_param import DateValueParam
from .email_value_param import EmailValueParam
from .float_value_param import FloatValueParam
from .funnel_step_param import FunnelStepParam
from .domain_value_param import DomainValueParam
from .boolean_value_param import BooleanValueParam
from .integer_value_param import IntegerValueParam
from .datetime_value_param import DatetimeValueParam
from .monetary_value_param import MonetaryValueParam
from .social_x_value_param import SocialXValueParam
from .percentage_value_param import PercentageValueParam
from .telephone_number_param import TelephoneNumberParam
from .multi_line_text_value_param import MultiLineTextValueParam
from .single_line_text_value_param import SingleLineTextValueParam
from .social_linked_in_value_param import SocialLinkedInValueParam

__all__ = ["FieldValueParam"]

if TYPE_CHECKING or PYDANTIC_V2:
    FieldValueParam = TypeAliasType(
        "FieldValueParam",
        Union[
            SingleLineTextValueParam,
            MultiLineTextValueParam,
            IntegerValueParam,
            FloatValueParam,
            MonetaryValueParam,
            PercentageValueParam,
            BooleanValueParam,
            EmailValueParam,
            URLValueParam,
            DomainValueParam,
            SocialXValueParam,
            SocialLinkedInValueParam,
            TelephoneNumberParam,
            GeoValueParam,
            DateValueParam,
            DatetimeValueParam,
            ChoiceParam,
            FunnelStepParam,
            "RelationValueParam",
            Iterable["ValueParam"],
        ],
    )
else:
    FieldValueParam: TypeAlias = Union[
        SingleLineTextValueParam,
        MultiLineTextValueParam,
        IntegerValueParam,
        FloatValueParam,
        MonetaryValueParam,
        PercentageValueParam,
        BooleanValueParam,
        EmailValueParam,
        URLValueParam,
        DomainValueParam,
        SocialXValueParam,
        SocialLinkedInValueParam,
        TelephoneNumberParam,
        GeoValueParam,
        DateValueParam,
        DatetimeValueParam,
        ChoiceParam,
        FunnelStepParam,
        "RelationValueParam",
        Iterable["ValueParam"],
    ]

from .value_param import ValueParam
from .relation_value_param import RelationValueParam
