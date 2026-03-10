# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_search_params
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import MoonbaseError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.search_response import SearchResponse

if TYPE_CHECKING:
    from .resources import (
        calls,
        files,
        forms,
        notes,
        views,
        inboxes,
        tagsets,
        meetings,
        programs,
        activities,
        collections,
        unsubscribes,
        agent_settings,
        inbox_messages,
        program_messages,
        program_templates,
        webhook_endpoints,
        inbox_conversations,
    )
    from .resources.calls import CallsResource, AsyncCallsResource
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.forms import FormsResource, AsyncFormsResource
    from .resources.notes import NotesResource, AsyncNotesResource
    from .resources.inboxes import InboxesResource, AsyncInboxesResource
    from .resources.tagsets import TagsetsResource, AsyncTagsetsResource
    from .resources.meetings import MeetingsResource, AsyncMeetingsResource
    from .resources.programs import ProgramsResource, AsyncProgramsResource
    from .resources.activities import ActivitiesResource, AsyncActivitiesResource
    from .resources.views.views import ViewsResource, AsyncViewsResource
    from .resources.unsubscribes import UnsubscribesResource, AsyncUnsubscribesResource
    from .resources.agent_settings import AgentSettingsResource, AsyncAgentSettingsResource
    from .resources.inbox_messages import InboxMessagesResource, AsyncInboxMessagesResource
    from .resources.program_messages import ProgramMessagesResource, AsyncProgramMessagesResource
    from .resources.program_templates import ProgramTemplatesResource, AsyncProgramTemplatesResource
    from .resources.webhook_endpoints import WebhookEndpointsResource, AsyncWebhookEndpointsResource
    from .resources.inbox_conversations import InboxConversationsResource, AsyncInboxConversationsResource
    from .resources.collections.collections import CollectionsResource, AsyncCollectionsResource

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
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def collections(self) -> CollectionsResource:
        """Manage your collections and items"""
        from .resources.collections import CollectionsResource

        return CollectionsResource(self)

    @cached_property
    def views(self) -> ViewsResource:
        """Manage your collections and items"""
        from .resources.views import ViewsResource

        return ViewsResource(self)

    @cached_property
    def inboxes(self) -> InboxesResource:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inboxes import InboxesResource

        return InboxesResource(self)

    @cached_property
    def inbox_conversations(self) -> InboxConversationsResource:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_conversations import InboxConversationsResource

        return InboxConversationsResource(self)

    @cached_property
    def inbox_messages(self) -> InboxMessagesResource:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_messages import InboxMessagesResource

        return InboxMessagesResource(self)

    @cached_property
    def tagsets(self) -> TagsetsResource:
        """Manage your inboxes, conversations, and messages"""
        from .resources.tagsets import TagsetsResource

        return TagsetsResource(self)

    @cached_property
    def programs(self) -> ProgramsResource:
        """Manage your marketing campaigns and forms"""
        from .resources.programs import ProgramsResource

        return ProgramsResource(self)

    @cached_property
    def program_templates(self) -> ProgramTemplatesResource:
        """Manage your marketing campaigns and forms"""
        from .resources.program_templates import ProgramTemplatesResource

        return ProgramTemplatesResource(self)

    @cached_property
    def program_messages(self) -> ProgramMessagesResource:
        """Manage your marketing campaigns and forms"""
        from .resources.program_messages import ProgramMessagesResource

        return ProgramMessagesResource(self)

    @cached_property
    def forms(self) -> FormsResource:
        """Manage your marketing campaigns and forms"""
        from .resources.forms import FormsResource

        return FormsResource(self)

    @cached_property
    def unsubscribes(self) -> UnsubscribesResource:
        """Manage your marketing campaigns and forms"""
        from .resources.unsubscribes import UnsubscribesResource

        return UnsubscribesResource(self)

    @cached_property
    def activities(self) -> ActivitiesResource:
        """View activities and capture calls"""
        from .resources.activities import ActivitiesResource

        return ActivitiesResource(self)

    @cached_property
    def calls(self) -> CallsResource:
        """View activities and capture calls"""
        from .resources.calls import CallsResource

        return CallsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        """Manage your meetings, files, and notes"""
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def meetings(self) -> MeetingsResource:
        """Manage your meetings, files, and notes"""
        from .resources.meetings import MeetingsResource

        return MeetingsResource(self)

    @cached_property
    def notes(self) -> NotesResource:
        """Manage your meetings, files, and notes"""
        from .resources.notes import NotesResource

        return NotesResource(self)

    @cached_property
    def webhook_endpoints(self) -> WebhookEndpointsResource:
        from .resources.webhook_endpoints import WebhookEndpointsResource

        return WebhookEndpointsResource(self)

    @cached_property
    def agent_settings(self) -> AgentSettingsResource:
        from .resources.agent_settings import AgentSettingsResource

        return AgentSettingsResource(self)

    @cached_property
    def with_raw_response(self) -> MoonbaseWithRawResponse:
        return MoonbaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MoonbaseWithStreamedResponse:
        return MoonbaseWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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

    def search(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, client_search_params.ClientSearchParams),
            ),
            cast_to=SearchResponse,
        )

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
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def collections(self) -> AsyncCollectionsResource:
        """Manage your collections and items"""
        from .resources.collections import AsyncCollectionsResource

        return AsyncCollectionsResource(self)

    @cached_property
    def views(self) -> AsyncViewsResource:
        """Manage your collections and items"""
        from .resources.views import AsyncViewsResource

        return AsyncViewsResource(self)

    @cached_property
    def inboxes(self) -> AsyncInboxesResource:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inboxes import AsyncInboxesResource

        return AsyncInboxesResource(self)

    @cached_property
    def inbox_conversations(self) -> AsyncInboxConversationsResource:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_conversations import AsyncInboxConversationsResource

        return AsyncInboxConversationsResource(self)

    @cached_property
    def inbox_messages(self) -> AsyncInboxMessagesResource:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_messages import AsyncInboxMessagesResource

        return AsyncInboxMessagesResource(self)

    @cached_property
    def tagsets(self) -> AsyncTagsetsResource:
        """Manage your inboxes, conversations, and messages"""
        from .resources.tagsets import AsyncTagsetsResource

        return AsyncTagsetsResource(self)

    @cached_property
    def programs(self) -> AsyncProgramsResource:
        """Manage your marketing campaigns and forms"""
        from .resources.programs import AsyncProgramsResource

        return AsyncProgramsResource(self)

    @cached_property
    def program_templates(self) -> AsyncProgramTemplatesResource:
        """Manage your marketing campaigns and forms"""
        from .resources.program_templates import AsyncProgramTemplatesResource

        return AsyncProgramTemplatesResource(self)

    @cached_property
    def program_messages(self) -> AsyncProgramMessagesResource:
        """Manage your marketing campaigns and forms"""
        from .resources.program_messages import AsyncProgramMessagesResource

        return AsyncProgramMessagesResource(self)

    @cached_property
    def forms(self) -> AsyncFormsResource:
        """Manage your marketing campaigns and forms"""
        from .resources.forms import AsyncFormsResource

        return AsyncFormsResource(self)

    @cached_property
    def unsubscribes(self) -> AsyncUnsubscribesResource:
        """Manage your marketing campaigns and forms"""
        from .resources.unsubscribes import AsyncUnsubscribesResource

        return AsyncUnsubscribesResource(self)

    @cached_property
    def activities(self) -> AsyncActivitiesResource:
        """View activities and capture calls"""
        from .resources.activities import AsyncActivitiesResource

        return AsyncActivitiesResource(self)

    @cached_property
    def calls(self) -> AsyncCallsResource:
        """View activities and capture calls"""
        from .resources.calls import AsyncCallsResource

        return AsyncCallsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        """Manage your meetings, files, and notes"""
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def meetings(self) -> AsyncMeetingsResource:
        """Manage your meetings, files, and notes"""
        from .resources.meetings import AsyncMeetingsResource

        return AsyncMeetingsResource(self)

    @cached_property
    def notes(self) -> AsyncNotesResource:
        """Manage your meetings, files, and notes"""
        from .resources.notes import AsyncNotesResource

        return AsyncNotesResource(self)

    @cached_property
    def webhook_endpoints(self) -> AsyncWebhookEndpointsResource:
        from .resources.webhook_endpoints import AsyncWebhookEndpointsResource

        return AsyncWebhookEndpointsResource(self)

    @cached_property
    def agent_settings(self) -> AsyncAgentSettingsResource:
        from .resources.agent_settings import AsyncAgentSettingsResource

        return AsyncAgentSettingsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncMoonbaseWithRawResponse:
        return AsyncMoonbaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMoonbaseWithStreamedResponse:
        return AsyncMoonbaseWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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

    async def search(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, client_search_params.ClientSearchParams),
            ),
            cast_to=SearchResponse,
        )

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
    _client: Moonbase

    def __init__(self, client: Moonbase) -> None:
        self._client = client

        self.search = to_raw_response_wrapper(
            client.search,
        )

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithRawResponse:
        """Manage your collections and items"""
        from .resources.collections import CollectionsResourceWithRawResponse

        return CollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def views(self) -> views.ViewsResourceWithRawResponse:
        """Manage your collections and items"""
        from .resources.views import ViewsResourceWithRawResponse

        return ViewsResourceWithRawResponse(self._client.views)

    @cached_property
    def inboxes(self) -> inboxes.InboxesResourceWithRawResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inboxes import InboxesResourceWithRawResponse

        return InboxesResourceWithRawResponse(self._client.inboxes)

    @cached_property
    def inbox_conversations(self) -> inbox_conversations.InboxConversationsResourceWithRawResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_conversations import InboxConversationsResourceWithRawResponse

        return InboxConversationsResourceWithRawResponse(self._client.inbox_conversations)

    @cached_property
    def inbox_messages(self) -> inbox_messages.InboxMessagesResourceWithRawResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_messages import InboxMessagesResourceWithRawResponse

        return InboxMessagesResourceWithRawResponse(self._client.inbox_messages)

    @cached_property
    def tagsets(self) -> tagsets.TagsetsResourceWithRawResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.tagsets import TagsetsResourceWithRawResponse

        return TagsetsResourceWithRawResponse(self._client.tagsets)

    @cached_property
    def programs(self) -> programs.ProgramsResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.programs import ProgramsResourceWithRawResponse

        return ProgramsResourceWithRawResponse(self._client.programs)

    @cached_property
    def program_templates(self) -> program_templates.ProgramTemplatesResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.program_templates import ProgramTemplatesResourceWithRawResponse

        return ProgramTemplatesResourceWithRawResponse(self._client.program_templates)

    @cached_property
    def program_messages(self) -> program_messages.ProgramMessagesResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.program_messages import ProgramMessagesResourceWithRawResponse

        return ProgramMessagesResourceWithRawResponse(self._client.program_messages)

    @cached_property
    def forms(self) -> forms.FormsResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.forms import FormsResourceWithRawResponse

        return FormsResourceWithRawResponse(self._client.forms)

    @cached_property
    def unsubscribes(self) -> unsubscribes.UnsubscribesResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.unsubscribes import UnsubscribesResourceWithRawResponse

        return UnsubscribesResourceWithRawResponse(self._client.unsubscribes)

    @cached_property
    def activities(self) -> activities.ActivitiesResourceWithRawResponse:
        """View activities and capture calls"""
        from .resources.activities import ActivitiesResourceWithRawResponse

        return ActivitiesResourceWithRawResponse(self._client.activities)

    @cached_property
    def calls(self) -> calls.CallsResourceWithRawResponse:
        """View activities and capture calls"""
        from .resources.calls import CallsResourceWithRawResponse

        return CallsResourceWithRawResponse(self._client.calls)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        """Manage your meetings, files, and notes"""
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def meetings(self) -> meetings.MeetingsResourceWithRawResponse:
        """Manage your meetings, files, and notes"""
        from .resources.meetings import MeetingsResourceWithRawResponse

        return MeetingsResourceWithRawResponse(self._client.meetings)

    @cached_property
    def notes(self) -> notes.NotesResourceWithRawResponse:
        """Manage your meetings, files, and notes"""
        from .resources.notes import NotesResourceWithRawResponse

        return NotesResourceWithRawResponse(self._client.notes)

    @cached_property
    def webhook_endpoints(self) -> webhook_endpoints.WebhookEndpointsResourceWithRawResponse:
        from .resources.webhook_endpoints import WebhookEndpointsResourceWithRawResponse

        return WebhookEndpointsResourceWithRawResponse(self._client.webhook_endpoints)

    @cached_property
    def agent_settings(self) -> agent_settings.AgentSettingsResourceWithRawResponse:
        from .resources.agent_settings import AgentSettingsResourceWithRawResponse

        return AgentSettingsResourceWithRawResponse(self._client.agent_settings)


class AsyncMoonbaseWithRawResponse:
    _client: AsyncMoonbase

    def __init__(self, client: AsyncMoonbase) -> None:
        self._client = client

        self.search = async_to_raw_response_wrapper(
            client.search,
        )

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithRawResponse:
        """Manage your collections and items"""
        from .resources.collections import AsyncCollectionsResourceWithRawResponse

        return AsyncCollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def views(self) -> views.AsyncViewsResourceWithRawResponse:
        """Manage your collections and items"""
        from .resources.views import AsyncViewsResourceWithRawResponse

        return AsyncViewsResourceWithRawResponse(self._client.views)

    @cached_property
    def inboxes(self) -> inboxes.AsyncInboxesResourceWithRawResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inboxes import AsyncInboxesResourceWithRawResponse

        return AsyncInboxesResourceWithRawResponse(self._client.inboxes)

    @cached_property
    def inbox_conversations(self) -> inbox_conversations.AsyncInboxConversationsResourceWithRawResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_conversations import AsyncInboxConversationsResourceWithRawResponse

        return AsyncInboxConversationsResourceWithRawResponse(self._client.inbox_conversations)

    @cached_property
    def inbox_messages(self) -> inbox_messages.AsyncInboxMessagesResourceWithRawResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_messages import AsyncInboxMessagesResourceWithRawResponse

        return AsyncInboxMessagesResourceWithRawResponse(self._client.inbox_messages)

    @cached_property
    def tagsets(self) -> tagsets.AsyncTagsetsResourceWithRawResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.tagsets import AsyncTagsetsResourceWithRawResponse

        return AsyncTagsetsResourceWithRawResponse(self._client.tagsets)

    @cached_property
    def programs(self) -> programs.AsyncProgramsResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.programs import AsyncProgramsResourceWithRawResponse

        return AsyncProgramsResourceWithRawResponse(self._client.programs)

    @cached_property
    def program_templates(self) -> program_templates.AsyncProgramTemplatesResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.program_templates import AsyncProgramTemplatesResourceWithRawResponse

        return AsyncProgramTemplatesResourceWithRawResponse(self._client.program_templates)

    @cached_property
    def program_messages(self) -> program_messages.AsyncProgramMessagesResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.program_messages import AsyncProgramMessagesResourceWithRawResponse

        return AsyncProgramMessagesResourceWithRawResponse(self._client.program_messages)

    @cached_property
    def forms(self) -> forms.AsyncFormsResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.forms import AsyncFormsResourceWithRawResponse

        return AsyncFormsResourceWithRawResponse(self._client.forms)

    @cached_property
    def unsubscribes(self) -> unsubscribes.AsyncUnsubscribesResourceWithRawResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.unsubscribes import AsyncUnsubscribesResourceWithRawResponse

        return AsyncUnsubscribesResourceWithRawResponse(self._client.unsubscribes)

    @cached_property
    def activities(self) -> activities.AsyncActivitiesResourceWithRawResponse:
        """View activities and capture calls"""
        from .resources.activities import AsyncActivitiesResourceWithRawResponse

        return AsyncActivitiesResourceWithRawResponse(self._client.activities)

    @cached_property
    def calls(self) -> calls.AsyncCallsResourceWithRawResponse:
        """View activities and capture calls"""
        from .resources.calls import AsyncCallsResourceWithRawResponse

        return AsyncCallsResourceWithRawResponse(self._client.calls)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        """Manage your meetings, files, and notes"""
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def meetings(self) -> meetings.AsyncMeetingsResourceWithRawResponse:
        """Manage your meetings, files, and notes"""
        from .resources.meetings import AsyncMeetingsResourceWithRawResponse

        return AsyncMeetingsResourceWithRawResponse(self._client.meetings)

    @cached_property
    def notes(self) -> notes.AsyncNotesResourceWithRawResponse:
        """Manage your meetings, files, and notes"""
        from .resources.notes import AsyncNotesResourceWithRawResponse

        return AsyncNotesResourceWithRawResponse(self._client.notes)

    @cached_property
    def webhook_endpoints(self) -> webhook_endpoints.AsyncWebhookEndpointsResourceWithRawResponse:
        from .resources.webhook_endpoints import AsyncWebhookEndpointsResourceWithRawResponse

        return AsyncWebhookEndpointsResourceWithRawResponse(self._client.webhook_endpoints)

    @cached_property
    def agent_settings(self) -> agent_settings.AsyncAgentSettingsResourceWithRawResponse:
        from .resources.agent_settings import AsyncAgentSettingsResourceWithRawResponse

        return AsyncAgentSettingsResourceWithRawResponse(self._client.agent_settings)


class MoonbaseWithStreamedResponse:
    _client: Moonbase

    def __init__(self, client: Moonbase) -> None:
        self._client = client

        self.search = to_streamed_response_wrapper(
            client.search,
        )

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithStreamingResponse:
        """Manage your collections and items"""
        from .resources.collections import CollectionsResourceWithStreamingResponse

        return CollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def views(self) -> views.ViewsResourceWithStreamingResponse:
        """Manage your collections and items"""
        from .resources.views import ViewsResourceWithStreamingResponse

        return ViewsResourceWithStreamingResponse(self._client.views)

    @cached_property
    def inboxes(self) -> inboxes.InboxesResourceWithStreamingResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inboxes import InboxesResourceWithStreamingResponse

        return InboxesResourceWithStreamingResponse(self._client.inboxes)

    @cached_property
    def inbox_conversations(self) -> inbox_conversations.InboxConversationsResourceWithStreamingResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_conversations import InboxConversationsResourceWithStreamingResponse

        return InboxConversationsResourceWithStreamingResponse(self._client.inbox_conversations)

    @cached_property
    def inbox_messages(self) -> inbox_messages.InboxMessagesResourceWithStreamingResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_messages import InboxMessagesResourceWithStreamingResponse

        return InboxMessagesResourceWithStreamingResponse(self._client.inbox_messages)

    @cached_property
    def tagsets(self) -> tagsets.TagsetsResourceWithStreamingResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.tagsets import TagsetsResourceWithStreamingResponse

        return TagsetsResourceWithStreamingResponse(self._client.tagsets)

    @cached_property
    def programs(self) -> programs.ProgramsResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.programs import ProgramsResourceWithStreamingResponse

        return ProgramsResourceWithStreamingResponse(self._client.programs)

    @cached_property
    def program_templates(self) -> program_templates.ProgramTemplatesResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.program_templates import ProgramTemplatesResourceWithStreamingResponse

        return ProgramTemplatesResourceWithStreamingResponse(self._client.program_templates)

    @cached_property
    def program_messages(self) -> program_messages.ProgramMessagesResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.program_messages import ProgramMessagesResourceWithStreamingResponse

        return ProgramMessagesResourceWithStreamingResponse(self._client.program_messages)

    @cached_property
    def forms(self) -> forms.FormsResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.forms import FormsResourceWithStreamingResponse

        return FormsResourceWithStreamingResponse(self._client.forms)

    @cached_property
    def unsubscribes(self) -> unsubscribes.UnsubscribesResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.unsubscribes import UnsubscribesResourceWithStreamingResponse

        return UnsubscribesResourceWithStreamingResponse(self._client.unsubscribes)

    @cached_property
    def activities(self) -> activities.ActivitiesResourceWithStreamingResponse:
        """View activities and capture calls"""
        from .resources.activities import ActivitiesResourceWithStreamingResponse

        return ActivitiesResourceWithStreamingResponse(self._client.activities)

    @cached_property
    def calls(self) -> calls.CallsResourceWithStreamingResponse:
        """View activities and capture calls"""
        from .resources.calls import CallsResourceWithStreamingResponse

        return CallsResourceWithStreamingResponse(self._client.calls)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        """Manage your meetings, files, and notes"""
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def meetings(self) -> meetings.MeetingsResourceWithStreamingResponse:
        """Manage your meetings, files, and notes"""
        from .resources.meetings import MeetingsResourceWithStreamingResponse

        return MeetingsResourceWithStreamingResponse(self._client.meetings)

    @cached_property
    def notes(self) -> notes.NotesResourceWithStreamingResponse:
        """Manage your meetings, files, and notes"""
        from .resources.notes import NotesResourceWithStreamingResponse

        return NotesResourceWithStreamingResponse(self._client.notes)

    @cached_property
    def webhook_endpoints(self) -> webhook_endpoints.WebhookEndpointsResourceWithStreamingResponse:
        from .resources.webhook_endpoints import WebhookEndpointsResourceWithStreamingResponse

        return WebhookEndpointsResourceWithStreamingResponse(self._client.webhook_endpoints)

    @cached_property
    def agent_settings(self) -> agent_settings.AgentSettingsResourceWithStreamingResponse:
        from .resources.agent_settings import AgentSettingsResourceWithStreamingResponse

        return AgentSettingsResourceWithStreamingResponse(self._client.agent_settings)


class AsyncMoonbaseWithStreamedResponse:
    _client: AsyncMoonbase

    def __init__(self, client: AsyncMoonbase) -> None:
        self._client = client

        self.search = async_to_streamed_response_wrapper(
            client.search,
        )

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithStreamingResponse:
        """Manage your collections and items"""
        from .resources.collections import AsyncCollectionsResourceWithStreamingResponse

        return AsyncCollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def views(self) -> views.AsyncViewsResourceWithStreamingResponse:
        """Manage your collections and items"""
        from .resources.views import AsyncViewsResourceWithStreamingResponse

        return AsyncViewsResourceWithStreamingResponse(self._client.views)

    @cached_property
    def inboxes(self) -> inboxes.AsyncInboxesResourceWithStreamingResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inboxes import AsyncInboxesResourceWithStreamingResponse

        return AsyncInboxesResourceWithStreamingResponse(self._client.inboxes)

    @cached_property
    def inbox_conversations(self) -> inbox_conversations.AsyncInboxConversationsResourceWithStreamingResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_conversations import AsyncInboxConversationsResourceWithStreamingResponse

        return AsyncInboxConversationsResourceWithStreamingResponse(self._client.inbox_conversations)

    @cached_property
    def inbox_messages(self) -> inbox_messages.AsyncInboxMessagesResourceWithStreamingResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.inbox_messages import AsyncInboxMessagesResourceWithStreamingResponse

        return AsyncInboxMessagesResourceWithStreamingResponse(self._client.inbox_messages)

    @cached_property
    def tagsets(self) -> tagsets.AsyncTagsetsResourceWithStreamingResponse:
        """Manage your inboxes, conversations, and messages"""
        from .resources.tagsets import AsyncTagsetsResourceWithStreamingResponse

        return AsyncTagsetsResourceWithStreamingResponse(self._client.tagsets)

    @cached_property
    def programs(self) -> programs.AsyncProgramsResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.programs import AsyncProgramsResourceWithStreamingResponse

        return AsyncProgramsResourceWithStreamingResponse(self._client.programs)

    @cached_property
    def program_templates(self) -> program_templates.AsyncProgramTemplatesResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.program_templates import AsyncProgramTemplatesResourceWithStreamingResponse

        return AsyncProgramTemplatesResourceWithStreamingResponse(self._client.program_templates)

    @cached_property
    def program_messages(self) -> program_messages.AsyncProgramMessagesResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.program_messages import AsyncProgramMessagesResourceWithStreamingResponse

        return AsyncProgramMessagesResourceWithStreamingResponse(self._client.program_messages)

    @cached_property
    def forms(self) -> forms.AsyncFormsResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.forms import AsyncFormsResourceWithStreamingResponse

        return AsyncFormsResourceWithStreamingResponse(self._client.forms)

    @cached_property
    def unsubscribes(self) -> unsubscribes.AsyncUnsubscribesResourceWithStreamingResponse:
        """Manage your marketing campaigns and forms"""
        from .resources.unsubscribes import AsyncUnsubscribesResourceWithStreamingResponse

        return AsyncUnsubscribesResourceWithStreamingResponse(self._client.unsubscribes)

    @cached_property
    def activities(self) -> activities.AsyncActivitiesResourceWithStreamingResponse:
        """View activities and capture calls"""
        from .resources.activities import AsyncActivitiesResourceWithStreamingResponse

        return AsyncActivitiesResourceWithStreamingResponse(self._client.activities)

    @cached_property
    def calls(self) -> calls.AsyncCallsResourceWithStreamingResponse:
        """View activities and capture calls"""
        from .resources.calls import AsyncCallsResourceWithStreamingResponse

        return AsyncCallsResourceWithStreamingResponse(self._client.calls)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        """Manage your meetings, files, and notes"""
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def meetings(self) -> meetings.AsyncMeetingsResourceWithStreamingResponse:
        """Manage your meetings, files, and notes"""
        from .resources.meetings import AsyncMeetingsResourceWithStreamingResponse

        return AsyncMeetingsResourceWithStreamingResponse(self._client.meetings)

    @cached_property
    def notes(self) -> notes.AsyncNotesResourceWithStreamingResponse:
        """Manage your meetings, files, and notes"""
        from .resources.notes import AsyncNotesResourceWithStreamingResponse

        return AsyncNotesResourceWithStreamingResponse(self._client.notes)

    @cached_property
    def webhook_endpoints(self) -> webhook_endpoints.AsyncWebhookEndpointsResourceWithStreamingResponse:
        from .resources.webhook_endpoints import AsyncWebhookEndpointsResourceWithStreamingResponse

        return AsyncWebhookEndpointsResourceWithStreamingResponse(self._client.webhook_endpoints)

    @cached_property
    def agent_settings(self) -> agent_settings.AsyncAgentSettingsResourceWithStreamingResponse:
        from .resources.agent_settings import AsyncAgentSettingsResourceWithStreamingResponse

        return AsyncAgentSettingsResourceWithStreamingResponse(self._client.agent_settings)


Client = Moonbase

AsyncClient = AsyncMoonbase
