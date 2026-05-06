# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentSettingUpdateResponse"]


class AgentSettingUpdateResponse(BaseModel):
    created_at: datetime

    type: Literal["agent_settings"]

    updated_at: datetime

    deal_summary_prompt: Optional[str] = None

    meeting_prebrief_prompt: Optional[str] = None

    meeting_summary_prompt: Optional[str] = None

    meeting_web_search: Optional[bool] = None

    organization_info: Optional[str] = None
