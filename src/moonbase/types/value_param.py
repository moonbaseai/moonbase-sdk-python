# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
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

__all__ = ["ValueParam"]

if TYPE_CHECKING or PYDANTIC_V2:
    ValueParam = TypeAliasType(
        "ValueParam",
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
        ],
    )
else:
    ValueParam: TypeAlias = Union[
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
    ]

# Import after defining the type alias to avoid circular imports
from .relation_value_param import RelationValueParam

# Manually resolve the forward references for both Pydantic v1 and v2
if TYPE_CHECKING or PYDANTIC_V2:
    # We need to update the TypeAliasType to have the resolved class instead of string
    ValueParam = TypeAliasType(  # type: ignore[misc]
        "ValueParam",
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
            RelationValueParam,  # Now resolved to the actual class
        ],
    )
else:
    # For Pydantic v1, we need to keep the TypeAlias version but with resolved classes
    ValueParam: TypeAlias = Union[
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
        RelationValueParam,  # Now resolved to the actual class
    ]
