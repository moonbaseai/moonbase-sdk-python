# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentSettingUpdateParams"]


class AgentSettingUpdateParams(TypedDict, total=False):
    deal_summary_prompt: str

    meeting_prebrief_prompt: str

    meeting_summary_prompt: str

    meeting_web_search: bool

    organization_info: str
