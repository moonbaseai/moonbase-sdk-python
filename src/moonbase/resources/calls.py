# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import call_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.call import Call
from .._base_client import make_request_options

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        direction: Literal["incoming", "outgoing"],
        participants: Iterable[call_create_params.Participant],
        provider: str,
        provider_id: str,
        start_at: Union[str, datetime],
        status: Literal[
            "queued",
            "initiated",
            "ringing",
            "in_progress",
            "completed",
            "busy",
            "failed",
            "no_answer",
            "canceled",
            "missed",
            "answered",
            "forwarded",
            "abandoned",
        ],
        answered_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        provider_metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Call:
        """
        Logs a phone call.

        Args:
          direction: The direction of the call, either `incoming` or `outgoing`.

          participants: An array of participants involved in the call.

          provider: The name of the phone provider that handled the call (e.g., `openphone`).

          provider_id: The unique identifier for the call from the provider's system.

          start_at: The time the call started, as an RFC 3339 timestamp.

          status: The status of the call.

          answered_at: The time the call was answered, as an RFC 3339 timestamp.

          end_at: The time the call ended, as an RFC 3339 timestamp.

          provider_metadata: A hash of additional metadata from the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calls",
            body=maybe_transform(
                {
                    "direction": direction,
                    "participants": participants,
                    "provider": provider,
                    "provider_id": provider_id,
                    "start_at": start_at,
                    "status": status,
                    "answered_at": answered_at,
                    "end_at": end_at,
                    "provider_metadata": provider_metadata,
                },
                call_create_params.CallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Call,
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        direction: Literal["incoming", "outgoing"],
        participants: Iterable[call_create_params.Participant],
        provider: str,
        provider_id: str,
        start_at: Union[str, datetime],
        status: Literal[
            "queued",
            "initiated",
            "ringing",
            "in_progress",
            "completed",
            "busy",
            "failed",
            "no_answer",
            "canceled",
            "missed",
            "answered",
            "forwarded",
            "abandoned",
        ],
        answered_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        provider_metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Call:
        """
        Logs a phone call.

        Args:
          direction: The direction of the call, either `incoming` or `outgoing`.

          participants: An array of participants involved in the call.

          provider: The name of the phone provider that handled the call (e.g., `openphone`).

          provider_id: The unique identifier for the call from the provider's system.

          start_at: The time the call started, as an RFC 3339 timestamp.

          status: The status of the call.

          answered_at: The time the call was answered, as an RFC 3339 timestamp.

          end_at: The time the call ended, as an RFC 3339 timestamp.

          provider_metadata: A hash of additional metadata from the provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calls",
            body=await async_maybe_transform(
                {
                    "direction": direction,
                    "participants": participants,
                    "provider": provider,
                    "provider_id": provider_id,
                    "start_at": start_at,
                    "status": status,
                    "answered_at": answered_at,
                    "end_at": end_at,
                    "provider_metadata": provider_metadata,
                },
                call_create_params.CallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Call,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.create = to_raw_response_wrapper(
            calls.create,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.create = async_to_raw_response_wrapper(
            calls.create,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.create = to_streamed_response_wrapper(
            calls.create,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.create = async_to_streamed_response_wrapper(
            calls.create,
        )
