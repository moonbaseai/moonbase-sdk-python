# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ...types import view_list_params, view_create_params, view_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ...types.view import View
from ..._base_client import AsyncPaginator, make_request_options
from ...types.view_field_param import ViewFieldParam
from ...types.items_filter_param import ItemsFilterParam
from ...types.view_list_response import ViewListResponse
from ...types.view_aggregate_param import ViewAggregateParam
from ...types.view_relation_value_filter_param import ViewRelationValueFilterParam

__all__ = ["ViewsResource", "AsyncViewsResource"]


class ViewsResource(SyncAPIResource):
    """Manage your collections and items"""

    @cached_property
    def items(self) -> ItemsResource:
        """Manage your collections and items"""
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return ViewsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection: view_create_params.Collection,
        fields: Iterable[ViewFieldParam],
        name: str,
        view_type: Literal["table", "board"],
        aggregates: Iterable[ViewAggregateParam] | Omit = omit,
        filter: ItemsFilterParam | Omit = omit,
        groups: SequenceNotStr[str] | Omit = omit,
        relation_value_filters: Iterable[ViewRelationValueFilterParam] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> View:
        """
        Creates a new view in a collection.

        Args:
          collection: A pointer to the `Collection` the view belongs to.

          fields: The view's columns, in display order.

          name: The name of the view.

          view_type: The type of view, `table` or `board`.

          aggregates: The metrics computed over the view's items.

          filter: The filter applied to the view's items.

          groups: Fields whose values group the view's items.

          relation_value_filters: Filters limiting which related items the view's relation columns show.

          sort: Sort items returned by the specified fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/views",
            body=maybe_transform(
                {
                    "collection": collection,
                    "fields": fields,
                    "name": name,
                    "view_type": view_type,
                    "aggregates": aggregates,
                    "filter": filter,
                    "groups": groups,
                    "relation_value_filters": relation_value_filters,
                    "sort": sort,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
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
    ) -> View:
        """
        Retrieves the details of an existing view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/views/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
        )

    def update(
        self,
        id: str,
        *,
        aggregates: Iterable[ViewAggregateParam] | Omit = omit,
        fields: Iterable[ViewFieldParam] | Omit = omit,
        filter: Optional[ItemsFilterParam] | Omit = omit,
        groups: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        relation_value_filters: Iterable[ViewRelationValueFilterParam] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        view_type: Literal["table", "board"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> View:
        """Updates a view.

        The change applies to the shared view that everyone in the
        workspace sees.

        Args:
          aggregates: The metrics computed over the view's items. An empty array clears them.

          fields: The view's columns, in display order. If provided, it must contain at least one
              column.

          filter: Return only items that match the filter conditions. Complex filters can be
              created by nesting filters inside of `AND`, `OR`, and `NOT` filters.

          groups: Fields whose values group the view's items. An empty array clears the grouping.

          name: The name of the view.

          relation_value_filters: Filters limiting which related items the view's relation columns show. An empty
              array clears them.

          sort: Sort items returned by the specified fields. An empty array clears the sort.

          view_type: The type of view, `table` or `board`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/views/{id}", id=id),
            body=maybe_transform(
                {
                    "aggregates": aggregates,
                    "fields": fields,
                    "filter": filter,
                    "groups": groups,
                    "name": name,
                    "relation_value_filters": relation_value_filters,
                    "sort": sort,
                    "view_type": view_type,
                },
                view_update_params.ViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
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
    ) -> SyncCursorPage[ViewListResponse]:
        """
        Returns a list of views.

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
            "/views",
            page=SyncCursorPage[ViewListResponse],
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
                    view_list_params.ViewListParams,
                ),
            ),
            model=ViewListResponse,
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
        """Permanently deletes a view.

        The default view of a collection cannot be deleted.

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
            path_template("/views/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncViewsResource(AsyncAPIResource):
    """Manage your collections and items"""

    @cached_property
    def items(self) -> AsyncItemsResource:
        """Manage your collections and items"""
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return AsyncViewsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection: view_create_params.Collection,
        fields: Iterable[ViewFieldParam],
        name: str,
        view_type: Literal["table", "board"],
        aggregates: Iterable[ViewAggregateParam] | Omit = omit,
        filter: ItemsFilterParam | Omit = omit,
        groups: SequenceNotStr[str] | Omit = omit,
        relation_value_filters: Iterable[ViewRelationValueFilterParam] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> View:
        """
        Creates a new view in a collection.

        Args:
          collection: A pointer to the `Collection` the view belongs to.

          fields: The view's columns, in display order.

          name: The name of the view.

          view_type: The type of view, `table` or `board`.

          aggregates: The metrics computed over the view's items.

          filter: The filter applied to the view's items.

          groups: Fields whose values group the view's items.

          relation_value_filters: Filters limiting which related items the view's relation columns show.

          sort: Sort items returned by the specified fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/views",
            body=await async_maybe_transform(
                {
                    "collection": collection,
                    "fields": fields,
                    "name": name,
                    "view_type": view_type,
                    "aggregates": aggregates,
                    "filter": filter,
                    "groups": groups,
                    "relation_value_filters": relation_value_filters,
                    "sort": sort,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
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
    ) -> View:
        """
        Retrieves the details of an existing view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/views/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
        )

    async def update(
        self,
        id: str,
        *,
        aggregates: Iterable[ViewAggregateParam] | Omit = omit,
        fields: Iterable[ViewFieldParam] | Omit = omit,
        filter: Optional[ItemsFilterParam] | Omit = omit,
        groups: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        relation_value_filters: Iterable[ViewRelationValueFilterParam] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        view_type: Literal["table", "board"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> View:
        """Updates a view.

        The change applies to the shared view that everyone in the
        workspace sees.

        Args:
          aggregates: The metrics computed over the view's items. An empty array clears them.

          fields: The view's columns, in display order. If provided, it must contain at least one
              column.

          filter: Return only items that match the filter conditions. Complex filters can be
              created by nesting filters inside of `AND`, `OR`, and `NOT` filters.

          groups: Fields whose values group the view's items. An empty array clears the grouping.

          name: The name of the view.

          relation_value_filters: Filters limiting which related items the view's relation columns show. An empty
              array clears them.

          sort: Sort items returned by the specified fields. An empty array clears the sort.

          view_type: The type of view, `table` or `board`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/views/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "aggregates": aggregates,
                    "fields": fields,
                    "filter": filter,
                    "groups": groups,
                    "name": name,
                    "relation_value_filters": relation_value_filters,
                    "sort": sort,
                    "view_type": view_type,
                },
                view_update_params.ViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
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
    ) -> AsyncPaginator[ViewListResponse, AsyncCursorPage[ViewListResponse]]:
        """
        Returns a list of views.

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
            "/views",
            page=AsyncCursorPage[ViewListResponse],
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
                    view_list_params.ViewListParams,
                ),
            ),
            model=ViewListResponse,
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
        """Permanently deletes a view.

        The default view of a collection cannot be deleted.

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
            path_template("/views/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ViewsResourceWithRawResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_raw_response_wrapper(
            views.create,
        )
        self.retrieve = to_raw_response_wrapper(
            views.retrieve,
        )
        self.update = to_raw_response_wrapper(
            views.update,
        )
        self.list = to_raw_response_wrapper(
            views.list,
        )
        self.delete = to_raw_response_wrapper(
            views.delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        """Manage your collections and items"""
        return ItemsResourceWithRawResponse(self._views.items)


class AsyncViewsResourceWithRawResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_raw_response_wrapper(
            views.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            views.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            views.update,
        )
        self.list = async_to_raw_response_wrapper(
            views.list,
        )
        self.delete = async_to_raw_response_wrapper(
            views.delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        """Manage your collections and items"""
        return AsyncItemsResourceWithRawResponse(self._views.items)


class ViewsResourceWithStreamingResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_streamed_response_wrapper(
            views.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            views.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            views.update,
        )
        self.list = to_streamed_response_wrapper(
            views.list,
        )
        self.delete = to_streamed_response_wrapper(
            views.delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        """Manage your collections and items"""
        return ItemsResourceWithStreamingResponse(self._views.items)


class AsyncViewsResourceWithStreamingResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_streamed_response_wrapper(
            views.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            views.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            views.update,
        )
        self.list = async_to_streamed_response_wrapper(
            views.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            views.delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        """Manage your collections and items"""
        return AsyncItemsResourceWithStreamingResponse(self._views.items)
