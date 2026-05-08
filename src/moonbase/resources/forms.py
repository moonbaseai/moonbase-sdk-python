# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import form_list_params, form_create_params, form_update_params
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
from ..types.form import Form
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["FormsResource", "AsyncFormsResource"]


class FormsResource(SyncAPIResource):
    """Manage your marketing campaigns and forms"""

    @cached_property
    def with_raw_response(self) -> FormsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return FormsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        business_email_required: bool | Omit = omit,
        pages_enabled: bool | Omit = omit,
        redirect_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Form:
        """
        Creates a new form with an auto-generated collection and default fields.

        Args:
          name: The name of the form, used as the title on its public page.

          business_email_required: If `true`, submissions require a business email address. Defaults to `false`.

          pages_enabled: If `true`, enables a Moonbase Pages hosted page for this form, providing a
              standalone public URL for sharing. Defaults to `false`.

          redirect_url: Optional URL the user is redirected to after a successful submission. Omit to
              leave submissions without a redirect. Stored as a Liquid template; rendered at
              submission time with form field values under `submission.<key>` (keyed by the
              field's `key`) plus UTM params (`utm_source`, `utm_medium`, `utm_campaign`,
              `utm_term`, `utm_content`) automatically appended. Use the `uri_encode` filter
              for URL-safe values, e.g.
              `https://example.com/thanks?email={{ submission.email | uri_encode }}`. The
              rendered URL must parse as a valid URL or the submission errors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/forms",
            body=maybe_transform(
                {
                    "name": name,
                    "business_email_required": business_email_required,
                    "pages_enabled": pages_enabled,
                    "redirect_url": redirect_url,
                },
                form_create_params.FormCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Form,
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
    ) -> Form:
        """
        Retrieves the details of an existing form.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/forms/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Form,
        )

    def update(
        self,
        id: str,
        *,
        business_email_required: bool | Omit = omit,
        name: str | Omit = omit,
        pages_enabled: bool | Omit = omit,
        redirect_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Form:
        """
        Updates an existing form.

        Args:
          business_email_required: If `true`, submissions require a business email address.

          name: The new name for the form.

          pages_enabled: If `true`, a Moonbase Pages hosted page is enabled for this form, providing a
              standalone public URL for sharing.

          redirect_url: Updated redirect URL, or `null` to clear. Omit to leave the existing value
              unchanged. Liquid template rendered at submission time with form field values
              under `submission.<key>` (keyed by the field's `key`) plus UTM params
              (`utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`)
              automatically appended. Use the `uri_encode` filter for URL-safe values. The
              rendered URL must parse as a valid URL or the submission errors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/forms/{id}", id=id),
            body=maybe_transform(
                {
                    "business_email_required": business_email_required,
                    "name": name,
                    "pages_enabled": pages_enabled,
                    "redirect_url": redirect_url,
                },
                form_update_params.FormUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Form,
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
    ) -> SyncCursorPage[Form]:
        """
        Returns a list of your forms.

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
            "/forms",
            page=SyncCursorPage[Form],
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
                    form_list_params.FormListParams,
                ),
            ),
            model=Form,
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
        """Permanently deletes a form.

        The backing collection is preserved.

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
            path_template("/forms/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFormsResource(AsyncAPIResource):
    """Manage your marketing campaigns and forms"""

    @cached_property
    def with_raw_response(self) -> AsyncFormsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/moonbaseai/moonbase-sdk-python#with_streaming_response
        """
        return AsyncFormsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        business_email_required: bool | Omit = omit,
        pages_enabled: bool | Omit = omit,
        redirect_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Form:
        """
        Creates a new form with an auto-generated collection and default fields.

        Args:
          name: The name of the form, used as the title on its public page.

          business_email_required: If `true`, submissions require a business email address. Defaults to `false`.

          pages_enabled: If `true`, enables a Moonbase Pages hosted page for this form, providing a
              standalone public URL for sharing. Defaults to `false`.

          redirect_url: Optional URL the user is redirected to after a successful submission. Omit to
              leave submissions without a redirect. Stored as a Liquid template; rendered at
              submission time with form field values under `submission.<key>` (keyed by the
              field's `key`) plus UTM params (`utm_source`, `utm_medium`, `utm_campaign`,
              `utm_term`, `utm_content`) automatically appended. Use the `uri_encode` filter
              for URL-safe values, e.g.
              `https://example.com/thanks?email={{ submission.email | uri_encode }}`. The
              rendered URL must parse as a valid URL or the submission errors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/forms",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "business_email_required": business_email_required,
                    "pages_enabled": pages_enabled,
                    "redirect_url": redirect_url,
                },
                form_create_params.FormCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Form,
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
    ) -> Form:
        """
        Retrieves the details of an existing form.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/forms/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Form,
        )

    async def update(
        self,
        id: str,
        *,
        business_email_required: bool | Omit = omit,
        name: str | Omit = omit,
        pages_enabled: bool | Omit = omit,
        redirect_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Form:
        """
        Updates an existing form.

        Args:
          business_email_required: If `true`, submissions require a business email address.

          name: The new name for the form.

          pages_enabled: If `true`, a Moonbase Pages hosted page is enabled for this form, providing a
              standalone public URL for sharing.

          redirect_url: Updated redirect URL, or `null` to clear. Omit to leave the existing value
              unchanged. Liquid template rendered at submission time with form field values
              under `submission.<key>` (keyed by the field's `key`) plus UTM params
              (`utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`)
              automatically appended. Use the `uri_encode` filter for URL-safe values. The
              rendered URL must parse as a valid URL or the submission errors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/forms/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "business_email_required": business_email_required,
                    "name": name,
                    "pages_enabled": pages_enabled,
                    "redirect_url": redirect_url,
                },
                form_update_params.FormUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Form,
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
    ) -> AsyncPaginator[Form, AsyncCursorPage[Form]]:
        """
        Returns a list of your forms.

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
            "/forms",
            page=AsyncCursorPage[Form],
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
                    form_list_params.FormListParams,
                ),
            ),
            model=Form,
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
        """Permanently deletes a form.

        The backing collection is preserved.

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
            path_template("/forms/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FormsResourceWithRawResponse:
    def __init__(self, forms: FormsResource) -> None:
        self._forms = forms

        self.create = to_raw_response_wrapper(
            forms.create,
        )
        self.retrieve = to_raw_response_wrapper(
            forms.retrieve,
        )
        self.update = to_raw_response_wrapper(
            forms.update,
        )
        self.list = to_raw_response_wrapper(
            forms.list,
        )
        self.delete = to_raw_response_wrapper(
            forms.delete,
        )


class AsyncFormsResourceWithRawResponse:
    def __init__(self, forms: AsyncFormsResource) -> None:
        self._forms = forms

        self.create = async_to_raw_response_wrapper(
            forms.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            forms.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            forms.update,
        )
        self.list = async_to_raw_response_wrapper(
            forms.list,
        )
        self.delete = async_to_raw_response_wrapper(
            forms.delete,
        )


class FormsResourceWithStreamingResponse:
    def __init__(self, forms: FormsResource) -> None:
        self._forms = forms

        self.create = to_streamed_response_wrapper(
            forms.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            forms.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            forms.update,
        )
        self.list = to_streamed_response_wrapper(
            forms.list,
        )
        self.delete = to_streamed_response_wrapper(
            forms.delete,
        )


class AsyncFormsResourceWithStreamingResponse:
    def __init__(self, forms: AsyncFormsResource) -> None:
        self._forms = forms

        self.create = async_to_streamed_response_wrapper(
            forms.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            forms.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            forms.update,
        )
        self.list = async_to_streamed_response_wrapper(
            forms.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            forms.delete,
        )
