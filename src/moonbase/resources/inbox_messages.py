# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    inbox_message_list_params,
    inbox_message_create_params,
    inbox_message_update_params,
    inbox_message_retrieve_params,
)
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
from ..types.email_message import EmailMessage
from ..types.shared_params.formatted_text import FormattedText

__all__ = ["InboxMessagesResource", "AsyncInboxMessagesResource"]


class InboxMessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboxMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InboxMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboxMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return InboxMessagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: FormattedText,
        inbox_id: str,
        bcc: Iterable[inbox_message_create_params.Bcc] | Omit = omit,
        cc: Iterable[inbox_message_create_params.Cc] | Omit = omit,
        conversation_id: str | Omit = omit,
        subject: str | Omit = omit,
        to: Iterable[inbox_message_create_params.To] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessage:
        """
        Creates a new message draft.

        Args:
          body: The email body.

          inbox_id: The inbox to use for sending the email.

          bcc: A list of the BCC recipients.

          cc: A list of the CC recipients.

          conversation_id: The ID of the conversation, if responding to an existing conversation.

          subject: The subject line of the email.

          to: A list of recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/inbox_messages",
            body=maybe_transform(
                {
                    "body": body,
                    "inbox_id": inbox_id,
                    "bcc": bcc,
                    "cc": cc,
                    "conversation_id": conversation_id,
                    "subject": subject,
                    "to": to,
                },
                inbox_message_create_params.InboxMessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessage,
        )

    def retrieve(
        self,
        id: str,
        *,
        include: List[Literal["addresses", "attachments", "conversation"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessage:
        """
        Retrieves the details of an existing message.

        Args:
          include: Specifies which related objects to include in the response. Valid options are
              `addresses`, `attachments`, and `conversation`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/inbox_messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, inbox_message_retrieve_params.InboxMessageRetrieveParams),
            ),
            cast_to=EmailMessage,
        )

    def update(
        self,
        id: str,
        *,
        lock_version: int,
        bcc: Iterable[inbox_message_update_params.Bcc] | Omit = omit,
        body: FormattedText | Omit = omit,
        cc: Iterable[inbox_message_update_params.Cc] | Omit = omit,
        subject: str | Omit = omit,
        to: Iterable[inbox_message_update_params.To] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessage:
        """
        Updates an existing message draft.

        Args:
          lock_version: The current lock version of the draft for optimistic concurrency control.

          bcc: A list of the BCC recipients.

          body: The email body.

          cc: A list of the CC recipients.

          subject: The subject line of the email.

          to: A list of the recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/inbox_messages/{id}",
            body=maybe_transform(
                {
                    "lock_version": lock_version,
                    "bcc": bcc,
                    "body": body,
                    "cc": cc,
                    "subject": subject,
                    "to": to,
                },
                inbox_message_update_params.InboxMessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessage,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        filter: inbox_message_list_params.Filter | Omit = omit,
        include: List[Literal["addresses", "attachments", "conversation"]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[EmailMessage]:
        """
        Returns a list of messages.

        Args:
          after: When specified, returns results starting immediately after the item identified
              by this cursor. Use the cursor value from the previous response's metadata to
              fetch the next page of results.

          before: When specified, returns results starting immediately before the item identified
              by this cursor. Use the cursor value from the response's metadata to fetch the
              previous page of results.

          include: Specifies which related objects to include in the response. Valid options are
              `addresses`, `attachments`, and `conversation`.

          limit: Maximum number of items to return per page. Must be between 1 and 100. Defaults
              to 20 if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbox_messages",
            page=SyncCursorPage[EmailMessage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "filter": filter,
                        "include": include,
                        "limit": limit,
                    },
                    inbox_message_list_params.InboxMessageListParams,
                ),
            ),
            model=EmailMessage,
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
        Permanently deletes a message draft.

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
            f"/inbox_messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInboxMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboxMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboxMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboxMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return AsyncInboxMessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: FormattedText,
        inbox_id: str,
        bcc: Iterable[inbox_message_create_params.Bcc] | Omit = omit,
        cc: Iterable[inbox_message_create_params.Cc] | Omit = omit,
        conversation_id: str | Omit = omit,
        subject: str | Omit = omit,
        to: Iterable[inbox_message_create_params.To] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessage:
        """
        Creates a new message draft.

        Args:
          body: The email body.

          inbox_id: The inbox to use for sending the email.

          bcc: A list of the BCC recipients.

          cc: A list of the CC recipients.

          conversation_id: The ID of the conversation, if responding to an existing conversation.

          subject: The subject line of the email.

          to: A list of recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/inbox_messages",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "inbox_id": inbox_id,
                    "bcc": bcc,
                    "cc": cc,
                    "conversation_id": conversation_id,
                    "subject": subject,
                    "to": to,
                },
                inbox_message_create_params.InboxMessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessage,
        )

    async def retrieve(
        self,
        id: str,
        *,
        include: List[Literal["addresses", "attachments", "conversation"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessage:
        """
        Retrieves the details of an existing message.

        Args:
          include: Specifies which related objects to include in the response. Valid options are
              `addresses`, `attachments`, and `conversation`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/inbox_messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include": include}, inbox_message_retrieve_params.InboxMessageRetrieveParams
                ),
            ),
            cast_to=EmailMessage,
        )

    async def update(
        self,
        id: str,
        *,
        lock_version: int,
        bcc: Iterable[inbox_message_update_params.Bcc] | Omit = omit,
        body: FormattedText | Omit = omit,
        cc: Iterable[inbox_message_update_params.Cc] | Omit = omit,
        subject: str | Omit = omit,
        to: Iterable[inbox_message_update_params.To] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessage:
        """
        Updates an existing message draft.

        Args:
          lock_version: The current lock version of the draft for optimistic concurrency control.

          bcc: A list of the BCC recipients.

          body: The email body.

          cc: A list of the CC recipients.

          subject: The subject line of the email.

          to: A list of the recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/inbox_messages/{id}",
            body=await async_maybe_transform(
                {
                    "lock_version": lock_version,
                    "bcc": bcc,
                    "body": body,
                    "cc": cc,
                    "subject": subject,
                    "to": to,
                },
                inbox_message_update_params.InboxMessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessage,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        filter: inbox_message_list_params.Filter | Omit = omit,
        include: List[Literal["addresses", "attachments", "conversation"]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmailMessage, AsyncCursorPage[EmailMessage]]:
        """
        Returns a list of messages.

        Args:
          after: When specified, returns results starting immediately after the item identified
              by this cursor. Use the cursor value from the previous response's metadata to
              fetch the next page of results.

          before: When specified, returns results starting immediately before the item identified
              by this cursor. Use the cursor value from the response's metadata to fetch the
              previous page of results.

          include: Specifies which related objects to include in the response. Valid options are
              `addresses`, `attachments`, and `conversation`.

          limit: Maximum number of items to return per page. Must be between 1 and 100. Defaults
              to 20 if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbox_messages",
            page=AsyncCursorPage[EmailMessage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "filter": filter,
                        "include": include,
                        "limit": limit,
                    },
                    inbox_message_list_params.InboxMessageListParams,
                ),
            ),
            model=EmailMessage,
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
        Permanently deletes a message draft.

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
            f"/inbox_messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InboxMessagesResourceWithRawResponse:
    def __init__(self, inbox_messages: InboxMessagesResource) -> None:
        self._inbox_messages = inbox_messages

        self.create = to_raw_response_wrapper(
            inbox_messages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            inbox_messages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            inbox_messages.update,
        )
        self.list = to_raw_response_wrapper(
            inbox_messages.list,
        )
        self.delete = to_raw_response_wrapper(
            inbox_messages.delete,
        )


class AsyncInboxMessagesResourceWithRawResponse:
    def __init__(self, inbox_messages: AsyncInboxMessagesResource) -> None:
        self._inbox_messages = inbox_messages

        self.create = async_to_raw_response_wrapper(
            inbox_messages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            inbox_messages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            inbox_messages.update,
        )
        self.list = async_to_raw_response_wrapper(
            inbox_messages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            inbox_messages.delete,
        )


class InboxMessagesResourceWithStreamingResponse:
    def __init__(self, inbox_messages: InboxMessagesResource) -> None:
        self._inbox_messages = inbox_messages

        self.create = to_streamed_response_wrapper(
            inbox_messages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            inbox_messages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            inbox_messages.update,
        )
        self.list = to_streamed_response_wrapper(
            inbox_messages.list,
        )
        self.delete = to_streamed_response_wrapper(
            inbox_messages.delete,
        )


class AsyncInboxMessagesResourceWithStreamingResponse:
    def __init__(self, inbox_messages: AsyncInboxMessagesResource) -> None:
        self._inbox_messages = inbox_messages

        self.create = async_to_streamed_response_wrapper(
            inbox_messages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            inbox_messages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            inbox_messages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            inbox_messages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            inbox_messages.delete,
        )
