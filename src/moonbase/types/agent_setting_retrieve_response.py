# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentSettingRetrieveResponse"]


class AgentSettingRetrieveResponse(BaseModel):
    created_at: datetime

    type: Literal["agent_settings"]

    updated_at: datetime

    deal_summary_model: Optional[str] = None

    deal_summary_prompt: Optional[str] = None

    meeting_prebrief_model: Optional[str] = None

    meeting_prebrief_prompt: Optional[str] = None

    meeting_web_search: Optional[bool] = None

    organization_info: Optional[str] = None
