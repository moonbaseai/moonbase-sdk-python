# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import tagset_list_params, tagset_create_params, tagset_update_params
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
from ..types.tagset import Tagset

__all__ = ["TagsetsResource", "AsyncTagsetsResource"]


class TagsetsResource(SyncAPIResource):
    """Manage your meetings, files, and notes"""

    @cached_property
    def with_raw_response(self) -> TagsetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TagsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return TagsetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        tags: Iterable[tagset_create_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tagset:
        """
        Create a new tagset.

        Args:
          name: The name of the tagset.

          description: An optional description of the tagset's purpose.

          tags: Optional list of tags to create with this tagset. Tags are ordered by their
              position in the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tagsets",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "tags": tags,
                },
                tagset_create_params.TagsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tagset,
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
    ) -> Tagset:
        """
        Retrieves the details of an existing tagset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/tagsets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tagset,
        )

    def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        tags: Iterable[tagset_update_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tagset:
        """
        Updates an existing tagset.

        Args:
          description: An updated description of the tagset.

          name: The new name of the tagset.

          tags: Optional full list of tags for this tagset. If provided, tags are ordered by
              array position.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/tagsets/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "tags": tags,
                },
                tagset_update_params.TagsetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tagset,
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
    ) -> SyncCursorPage[Tagset]:
        """
        Returns a list of your tagsets.

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
            "/tagsets",
            page=SyncCursorPage[Tagset],
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
                    tagset_list_params.TagsetListParams,
                ),
            ),
            model=Tagset,
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
        Permanently deletes a tagset.

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
            path_template("/tagsets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTagsetsResource(AsyncAPIResource):
    """Manage your meetings, files, and notes"""

    @cached_property
    def with_raw_response(self) -> AsyncTagsetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagsetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return AsyncTagsetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        tags: Iterable[tagset_create_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tagset:
        """
        Create a new tagset.

        Args:
          name: The name of the tagset.

          description: An optional description of the tagset's purpose.

          tags: Optional list of tags to create with this tagset. Tags are ordered by their
              position in the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tagsets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "tags": tags,
                },
                tagset_create_params.TagsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tagset,
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
    ) -> Tagset:
        """
        Retrieves the details of an existing tagset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/tagsets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tagset,
        )

    async def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        tags: Iterable[tagset_update_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tagset:
        """
        Updates an existing tagset.

        Args:
          description: An updated description of the tagset.

          name: The new name of the tagset.

          tags: Optional full list of tags for this tagset. If provided, tags are ordered by
              array position.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/tagsets/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "tags": tags,
                },
                tagset_update_params.TagsetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tagset,
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
    ) -> AsyncPaginator[Tagset, AsyncCursorPage[Tagset]]:
        """
        Returns a list of your tagsets.

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
            "/tagsets",
            page=AsyncCursorPage[Tagset],
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
                    tagset_list_params.TagsetListParams,
                ),
            ),
            model=Tagset,
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
        Permanently deletes a tagset.

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
            path_template("/tagsets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TagsetsResourceWithRawResponse:
    def __init__(self, tagsets: TagsetsResource) -> None:
        self._tagsets = tagsets

        self.create = to_raw_response_wrapper(
            tagsets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tagsets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tagsets.update,
        )
        self.list = to_raw_response_wrapper(
            tagsets.list,
        )
        self.delete = to_raw_response_wrapper(
            tagsets.delete,
        )


class AsyncTagsetsResourceWithRawResponse:
    def __init__(self, tagsets: AsyncTagsetsResource) -> None:
        self._tagsets = tagsets

        self.create = async_to_raw_response_wrapper(
            tagsets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tagsets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tagsets.update,
        )
        self.list = async_to_raw_response_wrapper(
            tagsets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tagsets.delete,
        )


class TagsetsResourceWithStreamingResponse:
    def __init__(self, tagsets: TagsetsResource) -> None:
        self._tagsets = tagsets

        self.create = to_streamed_response_wrapper(
            tagsets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tagsets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tagsets.update,
        )
        self.list = to_streamed_response_wrapper(
            tagsets.list,
        )
        self.delete = to_streamed_response_wrapper(
            tagsets.delete,
        )


class AsyncTagsetsResourceWithStreamingResponse:
    def __init__(self, tagsets: AsyncTagsetsResource) -> None:
        self._tagsets = tagsets

        self.create = async_to_streamed_response_wrapper(
            tagsets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tagsets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tagsets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tagsets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tagsets.delete,
        )
