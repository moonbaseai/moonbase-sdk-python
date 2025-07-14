# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import calls, files, items, notes, views, tagsets, programs, program_templates
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import MoonbaseError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.collections import collections

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Moonbase",
    "AsyncMoonbase",
    "Client",
    "AsyncClient",
]


class Moonbase(SyncAPIClient):
    calls: calls.CallsResource
    collections: collections.CollectionsResource
    files: files.FilesResource
    items: items.ItemsResource
    notes: notes.NotesResource
    program_templates: program_templates.ProgramTemplatesResource
    programs: programs.ProgramsResource
    tagsets: tagsets.TagsetsResource
    views: views.ViewsResource
    with_raw_response: MoonbaseWithRawResponse
    with_streaming_response: MoonbaseWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Moonbase client instance.

        This automatically infers the `api_key` argument from the `MOONBASE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MOONBASE_API_KEY")
        if api_key is None:
            raise MoonbaseError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MOONBASE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("MOONBASE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.moonbase.ai/v0"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.calls = calls.CallsResource(self)
        self.collections = collections.CollectionsResource(self)
        self.files = files.FilesResource(self)
        self.items = items.ItemsResource(self)
        self.notes = notes.NotesResource(self)
        self.program_templates = program_templates.ProgramTemplatesResource(self)
        self.programs = programs.ProgramsResource(self)
        self.tagsets = tagsets.TagsetsResource(self)
        self.views = views.ViewsResource(self)
        self.with_raw_response = MoonbaseWithRawResponse(self)
        self.with_streaming_response = MoonbaseWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMoonbase(AsyncAPIClient):
    calls: calls.AsyncCallsResource
    collections: collections.AsyncCollectionsResource
    files: files.AsyncFilesResource
    items: items.AsyncItemsResource
    notes: notes.AsyncNotesResource
    program_templates: program_templates.AsyncProgramTemplatesResource
    programs: programs.AsyncProgramsResource
    tagsets: tagsets.AsyncTagsetsResource
    views: views.AsyncViewsResource
    with_raw_response: AsyncMoonbaseWithRawResponse
    with_streaming_response: AsyncMoonbaseWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncMoonbase client instance.

        This automatically infers the `api_key` argument from the `MOONBASE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MOONBASE_API_KEY")
        if api_key is None:
            raise MoonbaseError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MOONBASE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("MOONBASE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.moonbase.ai/v0"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.calls = calls.AsyncCallsResource(self)
        self.collections = collections.AsyncCollectionsResource(self)
        self.files = files.AsyncFilesResource(self)
        self.items = items.AsyncItemsResource(self)
        self.notes = notes.AsyncNotesResource(self)
        self.program_templates = program_templates.AsyncProgramTemplatesResource(self)
        self.programs = programs.AsyncProgramsResource(self)
        self.tagsets = tagsets.AsyncTagsetsResource(self)
        self.views = views.AsyncViewsResource(self)
        self.with_raw_response = AsyncMoonbaseWithRawResponse(self)
        self.with_streaming_response = AsyncMoonbaseWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MoonbaseWithRawResponse:
    def __init__(self, client: Moonbase) -> None:
        self.calls = calls.CallsResourceWithRawResponse(client.calls)
        self.collections = collections.CollectionsResourceWithRawResponse(client.collections)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.items = items.ItemsResourceWithRawResponse(client.items)
        self.notes = notes.NotesResourceWithRawResponse(client.notes)
        self.program_templates = program_templates.ProgramTemplatesResourceWithRawResponse(client.program_templates)
        self.programs = programs.ProgramsResourceWithRawResponse(client.programs)
        self.tagsets = tagsets.TagsetsResourceWithRawResponse(client.tagsets)
        self.views = views.ViewsResourceWithRawResponse(client.views)


class AsyncMoonbaseWithRawResponse:
    def __init__(self, client: AsyncMoonbase) -> None:
        self.calls = calls.AsyncCallsResourceWithRawResponse(client.calls)
        self.collections = collections.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.items = items.AsyncItemsResourceWithRawResponse(client.items)
        self.notes = notes.AsyncNotesResourceWithRawResponse(client.notes)
        self.program_templates = program_templates.AsyncProgramTemplatesResourceWithRawResponse(
            client.program_templates
        )
        self.programs = programs.AsyncProgramsResourceWithRawResponse(client.programs)
        self.tagsets = tagsets.AsyncTagsetsResourceWithRawResponse(client.tagsets)
        self.views = views.AsyncViewsResourceWithRawResponse(client.views)


class MoonbaseWithStreamedResponse:
    def __init__(self, client: Moonbase) -> None:
        self.calls = calls.CallsResourceWithStreamingResponse(client.calls)
        self.collections = collections.CollectionsResourceWithStreamingResponse(client.collections)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.items = items.ItemsResourceWithStreamingResponse(client.items)
        self.notes = notes.NotesResourceWithStreamingResponse(client.notes)
        self.program_templates = program_templates.ProgramTemplatesResourceWithStreamingResponse(
            client.program_templates
        )
        self.programs = programs.ProgramsResourceWithStreamingResponse(client.programs)
        self.tagsets = tagsets.TagsetsResourceWithStreamingResponse(client.tagsets)
        self.views = views.ViewsResourceWithStreamingResponse(client.views)


class AsyncMoonbaseWithStreamedResponse:
    def __init__(self, client: AsyncMoonbase) -> None:
        self.calls = calls.AsyncCallsResourceWithStreamingResponse(client.calls)
        self.collections = collections.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.items = items.AsyncItemsResourceWithStreamingResponse(client.items)
        self.notes = notes.AsyncNotesResourceWithStreamingResponse(client.notes)
        self.program_templates = program_templates.AsyncProgramTemplatesResourceWithStreamingResponse(
            client.program_templates
        )
        self.programs = programs.AsyncProgramsResourceWithStreamingResponse(client.programs)
        self.tagsets = tagsets.AsyncTagsetsResourceWithStreamingResponse(client.tagsets)
        self.views = views.AsyncViewsResourceWithStreamingResponse(client.views)


Client = Moonbase

AsyncClient = AsyncMoonbase
