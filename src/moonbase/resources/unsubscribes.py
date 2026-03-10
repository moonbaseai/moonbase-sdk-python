# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import unsubscribe_list_params, unsubscribe_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.unsubscribe import Unsubscribe

__all__ = ["UnsubscribesResource", "AsyncUnsubscribesResource"]


class UnsubscribesResource(SyncAPIResource):
    """Manage your marketing campaigns and forms"""

    @cached_property
    def with_raw_response(self) -> UnsubscribesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UnsubscribesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnsubscribesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return UnsubscribesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Unsubscribe:
        """
        Create a new unsubscribe.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/unsubscribes",
            body=maybe_transform({"email": email}, unsubscribe_create_params.UnsubscribeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Unsubscribe,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Unsubscribe]:
        """
        Returns a list of unsubscribes.

        Args:
          after: When specified, returns results starting immediately after the item identified
              by this cursor. Use the cursor value from the previous response's metadata to
              fetch the next page of results.

          before: When specified, returns results starting immediately before the item identified
              by this cursor. Use the cursor value from the response's metadata to fetch the
              previous page of results.

          limit: Maximum number of items to return per page. Must be between 1 and 100. Defaults
              to 20 if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/unsubscribes",
            page=SyncCursorPage[Unsubscribe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    unsubscribe_list_params.UnsubscribeListParams,
                ),
            ),
            model=Unsubscribe,
        )

    def delete(
        self,
        email: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes an unsubscribe by email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email:
            raise ValueError(f"Expected a non-empty value for `email` but received {email!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/unsubscribes/{email}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUnsubscribesResource(AsyncAPIResource):
    """Manage your marketing campaigns and forms"""

    @cached_property
    def with_raw_response(self) -> AsyncUnsubscribesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUnsubscribesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnsubscribesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return AsyncUnsubscribesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Unsubscribe:
        """
        Create a new unsubscribe.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/unsubscribes",
            body=await async_maybe_transform({"email": email}, unsubscribe_create_params.UnsubscribeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Unsubscribe,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Unsubscribe, AsyncCursorPage[Unsubscribe]]:
        """
        Returns a list of unsubscribes.

        Args:
          after: When specified, returns results starting immediately after the item identified
              by this cursor. Use the cursor value from the previous response's metadata to
              fetch the next page of results.

          before: When specified, returns results starting immediately before the item identified
              by this cursor. Use the cursor value from the response's metadata to fetch the
              previous page of results.

          limit: Maximum number of items to return per page. Must be between 1 and 100. Defaults
              to 20 if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/unsubscribes",
            page=AsyncCursorPage[Unsubscribe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    unsubscribe_list_params.UnsubscribeListParams,
                ),
            ),
            model=Unsubscribe,
        )

    async def delete(
        self,
        email: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes an unsubscribe by email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email:
            raise ValueError(f"Expected a non-empty value for `email` but received {email!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/unsubscribes/{email}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UnsubscribesResourceWithRawResponse:
    def __init__(self, unsubscribes: UnsubscribesResource) -> None:
        self._unsubscribes = unsubscribes

        self.create = to_raw_response_wrapper(
            unsubscribes.create,
        )
        self.list = to_raw_response_wrapper(
            unsubscribes.list,
        )
        self.delete = to_raw_response_wrapper(
            unsubscribes.delete,
        )


class AsyncUnsubscribesResourceWithRawResponse:
    def __init__(self, unsubscribes: AsyncUnsubscribesResource) -> None:
        self._unsubscribes = unsubscribes

        self.create = async_to_raw_response_wrapper(
            unsubscribes.create,
        )
        self.list = async_to_raw_response_wrapper(
            unsubscribes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            unsubscribes.delete,
        )


class UnsubscribesResourceWithStreamingResponse:
    def __init__(self, unsubscribes: UnsubscribesResource) -> None:
        self._unsubscribes = unsubscribes

        self.create = to_streamed_response_wrapper(
            unsubscribes.create,
        )
        self.list = to_streamed_response_wrapper(
            unsubscribes.list,
        )
        self.delete = to_streamed_response_wrapper(
            unsubscribes.delete,
        )


class AsyncUnsubscribesResourceWithStreamingResponse:
    def __init__(self, unsubscribes: AsyncUnsubscribesResource) -> None:
        self._unsubscribes = unsubscribes

        self.create = async_to_streamed_response_wrapper(
            unsubscribes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            unsubscribes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            unsubscribes.delete,
        )
