# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import item_create_params, item_update_params, item_upsert_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.item import Item
from .._base_client import make_request_options
from ..types.field_value_param import FieldValueParam

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/moonbase-sdk-python#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection_id: str,
        values: Dict[str, Optional[FieldValueParam]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Creates a new item in a collection.

        Args:
          collection_id: The ID of the `Collection` to create the item in.

          values: A hash where keys are the `ref` of a `Field` and values are the data to be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/items",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "values": values,
                },
                item_create_params.ItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Retrieves the details of an existing item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
        )

    def update(
        self,
        id: str,
        *,
        values: Dict[str, Optional[FieldValueParam]],
        update_many_strategy: Literal["replace", "preserve", "merge"] | NotGiven = NOT_GIVEN,
        update_one_strategy: Literal["replace", "preserve"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Updates an item.

        Args:
          values: A hash where keys are the `ref` of a `Field` and values are the new data to be
              set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "update-many-strategy": str(update_many_strategy) if is_given(update_many_strategy) else NOT_GIVEN,
                    "update-one-strategy": str(update_one_strategy) if is_given(update_one_strategy) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            f"/items/{id}",
            body=maybe_transform({"values": values}, item_update_params.ItemUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Permanently deletes an item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
        )

    def upsert(
        self,
        *,
        collection_id: str,
        identifiers: Dict[str, Optional[FieldValueParam]],
        values: Dict[str, Optional[FieldValueParam]],
        update_many_strategy: Literal["replace", "preserve", "merge"] | NotGiven = NOT_GIVEN,
        update_one_strategy: Literal["replace", "preserve"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Find and update an existing item, or create a new one.

        Args:
          collection_id: The ID of the `Collection` to create the item in.

          identifiers: A hash where keys are the `ref` of a `Field` and values are used to identify the
              item to update. When multiple identifiers are provided, the update will find
              items that match any of the identifiers.

          values: A hash where keys are the `ref` of a `Field` and values are the data to be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "update-many-strategy": str(update_many_strategy) if is_given(update_many_strategy) else NOT_GIVEN,
                    "update-one-strategy": str(update_one_strategy) if is_given(update_one_strategy) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/items/upsert",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "identifiers": identifiers,
                    "values": values,
                },
                item_upsert_params.ItemUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
        )


class AsyncItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/moonbase-sdk-python#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection_id: str,
        values: Dict[str, Optional[FieldValueParam]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Creates a new item in a collection.

        Args:
          collection_id: The ID of the `Collection` to create the item in.

          values: A hash where keys are the `ref` of a `Field` and values are the data to be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/items",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "values": values,
                },
                item_create_params.ItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Retrieves the details of an existing item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
        )

    async def update(
        self,
        id: str,
        *,
        values: Dict[str, Optional[FieldValueParam]],
        update_many_strategy: Literal["replace", "preserve", "merge"] | NotGiven = NOT_GIVEN,
        update_one_strategy: Literal["replace", "preserve"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Updates an item.

        Args:
          values: A hash where keys are the `ref` of a `Field` and values are the new data to be
              set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "update-many-strategy": str(update_many_strategy) if is_given(update_many_strategy) else NOT_GIVEN,
                    "update-one-strategy": str(update_one_strategy) if is_given(update_one_strategy) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            f"/items/{id}",
            body=await async_maybe_transform({"values": values}, item_update_params.ItemUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Permanently deletes an item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
        )

    async def upsert(
        self,
        *,
        collection_id: str,
        identifiers: Dict[str, Optional[FieldValueParam]],
        values: Dict[str, Optional[FieldValueParam]],
        update_many_strategy: Literal["replace", "preserve", "merge"] | NotGiven = NOT_GIVEN,
        update_one_strategy: Literal["replace", "preserve"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Item:
        """
        Find and update an existing item, or create a new one.

        Args:
          collection_id: The ID of the `Collection` to create the item in.

          identifiers: A hash where keys are the `ref` of a `Field` and values are used to identify the
              item to update. When multiple identifiers are provided, the update will find
              items that match any of the identifiers.

          values: A hash where keys are the `ref` of a `Field` and values are the data to be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "update-many-strategy": str(update_many_strategy) if is_given(update_many_strategy) else NOT_GIVEN,
                    "update-one-strategy": str(update_one_strategy) if is_given(update_one_strategy) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/items/upsert",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "identifiers": identifiers,
                    "values": values,
                },
                item_upsert_params.ItemUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Item,
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_raw_response_wrapper(
            items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            items.update,
        )
        self.delete = to_raw_response_wrapper(
            items.delete,
        )
        self.upsert = to_raw_response_wrapper(
            items.upsert,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_raw_response_wrapper(
            items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            items.update,
        )
        self.delete = async_to_raw_response_wrapper(
            items.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            items.upsert,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_streamed_response_wrapper(
            items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            items.update,
        )
        self.delete = to_streamed_response_wrapper(
            items.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            items.upsert,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_streamed_response_wrapper(
            items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            items.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            items.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            items.upsert,
        )
