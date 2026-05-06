# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import agent_setting_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.agent_setting_update_response import AgentSettingUpdateResponse
from ..types.agent_setting_retrieve_response import AgentSettingRetrieveResponse

__all__ = ["AgentSettingsResource", "AsyncAgentSettingsResource"]


class AgentSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AgentSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return AgentSettingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSettingRetrieveResponse:
        return self._get(
            "/agent_settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSettingRetrieveResponse,
        )

    def update(
        self,
        *,
        deal_summary_prompt: str | Omit = omit,
        meeting_prebrief_prompt: str | Omit = omit,
        meeting_summary_prompt: str | Omit = omit,
        meeting_web_search: bool | Omit = omit,
        organization_info: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSettingUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/agent_settings",
            body=maybe_transform(
                {
                    "deal_summary_prompt": deal_summary_prompt,
                    "meeting_prebrief_prompt": meeting_prebrief_prompt,
                    "meeting_summary_prompt": meeting_summary_prompt,
                    "meeting_web_search": meeting_web_search,
                    "organization_info": organization_info,
                },
                agent_setting_update_params.AgentSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSettingUpdateResponse,
        )


class AsyncAgentSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return AsyncAgentSettingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSettingRetrieveResponse:
        return await self._get(
            "/agent_settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSettingRetrieveResponse,
        )

    async def update(
        self,
        *,
        deal_summary_prompt: str | Omit = omit,
        meeting_prebrief_prompt: str | Omit = omit,
        meeting_summary_prompt: str | Omit = omit,
        meeting_web_search: bool | Omit = omit,
        organization_info: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSettingUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/agent_settings",
            body=await async_maybe_transform(
                {
                    "deal_summary_prompt": deal_summary_prompt,
                    "meeting_prebrief_prompt": meeting_prebrief_prompt,
                    "meeting_summary_prompt": meeting_summary_prompt,
                    "meeting_web_search": meeting_web_search,
                    "organization_info": organization_info,
                },
                agent_setting_update_params.AgentSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSettingUpdateResponse,
        )


class AgentSettingsResourceWithRawResponse:
    def __init__(self, agent_settings: AgentSettingsResource) -> None:
        self._agent_settings = agent_settings

        self.retrieve = to_raw_response_wrapper(
            agent_settings.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agent_settings.update,
        )


class AsyncAgentSettingsResourceWithRawResponse:
    def __init__(self, agent_settings: AsyncAgentSettingsResource) -> None:
        self._agent_settings = agent_settings

        self.retrieve = async_to_raw_response_wrapper(
            agent_settings.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agent_settings.update,
        )


class AgentSettingsResourceWithStreamingResponse:
    def __init__(self, agent_settings: AgentSettingsResource) -> None:
        self._agent_settings = agent_settings

        self.retrieve = to_streamed_response_wrapper(
            agent_settings.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agent_settings.update,
        )


class AsyncAgentSettingsResourceWithStreamingResponse:
    def __init__(self, agent_settings: AsyncAgentSettingsResource) -> None:
        self._agent_settings = agent_settings

        self.retrieve = async_to_streamed_response_wrapper(
            agent_settings.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agent_settings.update,
        )
