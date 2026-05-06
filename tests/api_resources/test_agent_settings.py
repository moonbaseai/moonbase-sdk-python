# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from moonbase import Moonbase, AsyncMoonbase
from tests.utils import assert_matches_type
from moonbase.types import AgentSettingUpdateResponse, AgentSettingRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgentSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Moonbase) -> None:
        agent_setting = client.agent_settings.retrieve()
        assert_matches_type(AgentSettingRetrieveResponse, agent_setting, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Moonbase) -> None:
        response = client.agent_settings.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_setting = response.parse()
        assert_matches_type(AgentSettingRetrieveResponse, agent_setting, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Moonbase) -> None:
        with client.agent_settings.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_setting = response.parse()
            assert_matches_type(AgentSettingRetrieveResponse, agent_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Moonbase) -> None:
        agent_setting = client.agent_settings.update()
        assert_matches_type(AgentSettingUpdateResponse, agent_setting, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Moonbase) -> None:
        agent_setting = client.agent_settings.update(
            deal_summary_prompt="Instructions for the agent to help generate the deal summary",
            meeting_prebrief_prompt="Instructions for the agent to help generate the meeting prebrief note",
            meeting_summary_prompt="Instructions for the agent to help generate the meeting summary note",
            meeting_web_search=False,
            organization_info="Information about the organization using Moonbase",
        )
        assert_matches_type(AgentSettingUpdateResponse, agent_setting, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Moonbase) -> None:
        response = client.agent_settings.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_setting = response.parse()
        assert_matches_type(AgentSettingUpdateResponse, agent_setting, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Moonbase) -> None:
        with client.agent_settings.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_setting = response.parse()
            assert_matches_type(AgentSettingUpdateResponse, agent_setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgentSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMoonbase) -> None:
        agent_setting = await async_client.agent_settings.retrieve()
        assert_matches_type(AgentSettingRetrieveResponse, agent_setting, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.agent_settings.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_setting = await response.parse()
        assert_matches_type(AgentSettingRetrieveResponse, agent_setting, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMoonbase) -> None:
        async with async_client.agent_settings.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_setting = await response.parse()
            assert_matches_type(AgentSettingRetrieveResponse, agent_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncMoonbase) -> None:
        agent_setting = await async_client.agent_settings.update()
        assert_matches_type(AgentSettingUpdateResponse, agent_setting, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMoonbase) -> None:
        agent_setting = await async_client.agent_settings.update(
            deal_summary_prompt="Instructions for the agent to help generate the deal summary",
            meeting_prebrief_prompt="Instructions for the agent to help generate the meeting prebrief note",
            meeting_summary_prompt="Instructions for the agent to help generate the meeting summary note",
            meeting_web_search=False,
            organization_info="Information about the organization using Moonbase",
        )
        assert_matches_type(AgentSettingUpdateResponse, agent_setting, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.agent_settings.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_setting = await response.parse()
        assert_matches_type(AgentSettingUpdateResponse, agent_setting, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMoonbase) -> None:
        async with async_client.agent_settings.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_setting = await response.parse()
            assert_matches_type(AgentSettingUpdateResponse, agent_setting, path=["response"])

        assert cast(Any, response.is_closed) is True
