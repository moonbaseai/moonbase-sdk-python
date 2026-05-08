# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import funnel_list_params, funnel_create_params, funnel_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.funnel import Funnel

__all__ = ["FunnelsResource", "AsyncFunnelsResource"]


class FunnelsResource(SyncAPIResource):
    """Manage your collections and items"""

    @cached_property
    def with_raw_response(self) -> FunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return FunnelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        steps: Iterable[funnel_create_params.Step] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Funnel:
        """
        Creates a new funnel.

        Args:
          name: The name of the funnel.

          steps: An ordered list of steps to create. Array order determines step order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/funnels",
            body=maybe_transform(
                {
                    "name": name,
                    "steps": steps,
                },
                funnel_create_params.FunnelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Funnel,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Funnel:
        """
        Retrieves the details of an existing funnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/funnels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Funnel,
        )

    def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        steps: Iterable[funnel_update_params.Step] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Funnel:
        """
        Updates a funnel.

        Args:
          name: The name of the funnel.

          steps: An ordered list of steps. Providing this replaces all existing steps. Omitting
              preserves existing steps.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/funnels/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "steps": steps,
                },
                funnel_update_params.FunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Funnel,
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
    ) -> SyncCursorPage[Funnel]:
        """
        Returns a list of funnels.

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
            "/funnels",
            page=SyncCursorPage[Funnel],
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
                    funnel_list_params.FunnelListParams,
                ),
            ),
            model=Funnel,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a funnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/funnels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFunnelsResource(AsyncAPIResource):
    """Manage your collections and items"""

    @cached_property
    def with_raw_response(self) -> AsyncFunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return AsyncFunnelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        steps: Iterable[funnel_create_params.Step] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Funnel:
        """
        Creates a new funnel.

        Args:
          name: The name of the funnel.

          steps: An ordered list of steps to create. Array order determines step order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/funnels",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "steps": steps,
                },
                funnel_create_params.FunnelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Funnel,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Funnel:
        """
        Retrieves the details of an existing funnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/funnels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Funnel,
        )

    async def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        steps: Iterable[funnel_update_params.Step] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Funnel:
        """
        Updates a funnel.

        Args:
          name: The name of the funnel.

          steps: An ordered list of steps. Providing this replaces all existing steps. Omitting
              preserves existing steps.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/funnels/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "steps": steps,
                },
                funnel_update_params.FunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Funnel,
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
    ) -> AsyncPaginator[Funnel, AsyncCursorPage[Funnel]]:
        """
        Returns a list of funnels.

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
            "/funnels",
            page=AsyncCursorPage[Funnel],
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
                    funnel_list_params.FunnelListParams,
                ),
            ),
            model=Funnel,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a funnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/funnels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FunnelsResourceWithRawResponse:
    def __init__(self, funnels: FunnelsResource) -> None:
        self._funnels = funnels

        self.create = to_raw_response_wrapper(
            funnels.create,
        )
        self.retrieve = to_raw_response_wrapper(
            funnels.retrieve,
        )
        self.update = to_raw_response_wrapper(
            funnels.update,
        )
        self.list = to_raw_response_wrapper(
            funnels.list,
        )
        self.delete = to_raw_response_wrapper(
            funnels.delete,
        )


class AsyncFunnelsResourceWithRawResponse:
    def __init__(self, funnels: AsyncFunnelsResource) -> None:
        self._funnels = funnels

        self.create = async_to_raw_response_wrapper(
            funnels.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            funnels.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            funnels.update,
        )
        self.list = async_to_raw_response_wrapper(
            funnels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            funnels.delete,
        )


class FunnelsResourceWithStreamingResponse:
    def __init__(self, funnels: FunnelsResource) -> None:
        self._funnels = funnels

        self.create = to_streamed_response_wrapper(
            funnels.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            funnels.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            funnels.update,
        )
        self.list = to_streamed_response_wrapper(
            funnels.list,
        )
        self.delete = to_streamed_response_wrapper(
            funnels.delete,
        )


class AsyncFunnelsResourceWithStreamingResponse:
    def __init__(self, funnels: AsyncFunnelsResource) -> None:
        self._funnels = funnels

        self.create = async_to_streamed_response_wrapper(
            funnels.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            funnels.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            funnels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            funnels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            funnels.delete,
        )
