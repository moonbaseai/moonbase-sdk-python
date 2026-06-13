# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from moonbase import Moonbase, AsyncMoonbase
from tests.utils import assert_matches_type
from moonbase.types import (
    EmailMessage,
    EmailMessagePointer,
)
from moonbase.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboxMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.create(
            body={},
            inbox_id="inbox_id",
            subject="subject",
            to=[{"email": "dev@stainless.com"}],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.create(
            body={"markdown": "markdown"},
            inbox_id="inbox_id",
            subject="subject",
            to=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
            bcc=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
            cc=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Moonbase) -> None:
        response = client.inbox_messages.with_raw_response.create(
            body={},
            inbox_id="inbox_id",
            subject="subject",
            to=[{"email": "dev@stainless.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = response.parse()
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Moonbase) -> None:
        with client.inbox_messages.with_streaming_response.create(
            body={},
            inbox_id="inbox_id",
            subject="subject",
            to=[{"email": "dev@stainless.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = response.parse()
            assert_matches_type(EmailMessage, inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.create(
            body={},
            conversation_id="conversation_id",
            inbox_id="inbox_id",
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.create(
            body={"markdown": "markdown"},
            conversation_id="conversation_id",
            inbox_id="inbox_id",
            bcc=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
            cc=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
            to=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Moonbase) -> None:
        response = client.inbox_messages.with_raw_response.create(
            body={},
            conversation_id="conversation_id",
            inbox_id="inbox_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = response.parse()
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Moonbase) -> None:
        with client.inbox_messages.with_streaming_response.create(
            body={},
            conversation_id="conversation_id",
            inbox_id="inbox_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = response.parse()
            assert_matches_type(EmailMessage, inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.retrieve(
            id="id",
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.retrieve(
            id="id",
            include=["addresses"],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Moonbase) -> None:
        response = client.inbox_messages.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = response.parse()
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Moonbase) -> None:
        with client.inbox_messages.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = response.parse()
            assert_matches_type(EmailMessage, inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.inbox_messages.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.update(
            id="id",
            lock_version=0,
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.update(
            id="id",
            lock_version=0,
            bcc=[
                {
                    "email": "steve@example.com",
                    "name": "Steve",
                }
            ],
            body={
                "markdown": "This is the body of the message. It supports [markdown](https://en.wikipedia.org/wiki/Markdown)."
            },
            cc=[
                {
                    "email": "joe@example.com",
                    "name": "Joe",
                }
            ],
            subject="Test Subject",
            to=[
                {
                    "email": "bob@example.com",
                    "name": "Bob",
                },
                {
                    "email": "jack@example.com",
                    "name": "name",
                },
            ],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Moonbase) -> None:
        response = client.inbox_messages.with_raw_response.update(
            id="id",
            lock_version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = response.parse()
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Moonbase) -> None:
        with client.inbox_messages.with_streaming_response.update(
            id="id",
            lock_version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = response.parse()
            assert_matches_type(EmailMessage, inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.inbox_messages.with_raw_response.update(
                id="",
                lock_version=0,
            )

    @parametrize
    def test_method_list(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.list()
        assert_matches_type(SyncCursorPage[EmailMessagePointer], inbox_message, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.list(
            after="after",
            before="before",
            conversation_id={"eq": "eq"},
            inbox_id={"eq": "eq"},
            limit=1,
        )
        assert_matches_type(SyncCursorPage[EmailMessagePointer], inbox_message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Moonbase) -> None:
        response = client.inbox_messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = response.parse()
        assert_matches_type(SyncCursorPage[EmailMessagePointer], inbox_message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Moonbase) -> None:
        with client.inbox_messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = response.parse()
            assert_matches_type(SyncCursorPage[EmailMessagePointer], inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Moonbase) -> None:
        inbox_message = client.inbox_messages.delete(
            "id",
        )
        assert inbox_message is None

    @parametrize
    def test_raw_response_delete(self, client: Moonbase) -> None:
        response = client.inbox_messages.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = response.parse()
        assert inbox_message is None

    @parametrize
    def test_streaming_response_delete(self, client: Moonbase) -> None:
        with client.inbox_messages.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = response.parse()
            assert inbox_message is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.inbox_messages.with_raw_response.delete(
                "",
            )


class TestAsyncInboxMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.create(
            body={},
            inbox_id="inbox_id",
            subject="subject",
            to=[{"email": "dev@stainless.com"}],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.create(
            body={"markdown": "markdown"},
            inbox_id="inbox_id",
            subject="subject",
            to=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
            bcc=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
            cc=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.inbox_messages.with_raw_response.create(
            body={},
            inbox_id="inbox_id",
            subject="subject",
            to=[{"email": "dev@stainless.com"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = await response.parse()
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncMoonbase) -> None:
        async with async_client.inbox_messages.with_streaming_response.create(
            body={},
            inbox_id="inbox_id",
            subject="subject",
            to=[{"email": "dev@stainless.com"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = await response.parse()
            assert_matches_type(EmailMessage, inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.create(
            body={},
            conversation_id="conversation_id",
            inbox_id="inbox_id",
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.create(
            body={"markdown": "markdown"},
            conversation_id="conversation_id",
            inbox_id="inbox_id",
            bcc=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
            cc=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
            to=[
                {
                    "email": "dev@stainless.com",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.inbox_messages.with_raw_response.create(
            body={},
            conversation_id="conversation_id",
            inbox_id="inbox_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = await response.parse()
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncMoonbase) -> None:
        async with async_client.inbox_messages.with_streaming_response.create(
            body={},
            conversation_id="conversation_id",
            inbox_id="inbox_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = await response.parse()
            assert_matches_type(EmailMessage, inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.retrieve(
            id="id",
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.retrieve(
            id="id",
            include=["addresses"],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.inbox_messages.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = await response.parse()
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMoonbase) -> None:
        async with async_client.inbox_messages.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = await response.parse()
            assert_matches_type(EmailMessage, inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.inbox_messages.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.update(
            id="id",
            lock_version=0,
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.update(
            id="id",
            lock_version=0,
            bcc=[
                {
                    "email": "steve@example.com",
                    "name": "Steve",
                }
            ],
            body={
                "markdown": "This is the body of the message. It supports [markdown](https://en.wikipedia.org/wiki/Markdown)."
            },
            cc=[
                {
                    "email": "joe@example.com",
                    "name": "Joe",
                }
            ],
            subject="Test Subject",
            to=[
                {
                    "email": "bob@example.com",
                    "name": "Bob",
                },
                {
                    "email": "jack@example.com",
                    "name": "name",
                },
            ],
        )
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.inbox_messages.with_raw_response.update(
            id="id",
            lock_version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = await response.parse()
        assert_matches_type(EmailMessage, inbox_message, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMoonbase) -> None:
        async with async_client.inbox_messages.with_streaming_response.update(
            id="id",
            lock_version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = await response.parse()
            assert_matches_type(EmailMessage, inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.inbox_messages.with_raw_response.update(
                id="",
                lock_version=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.list()
        assert_matches_type(AsyncCursorPage[EmailMessagePointer], inbox_message, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.list(
            after="after",
            before="before",
            conversation_id={"eq": "eq"},
            inbox_id={"eq": "eq"},
            limit=1,
        )
        assert_matches_type(AsyncCursorPage[EmailMessagePointer], inbox_message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.inbox_messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = await response.parse()
        assert_matches_type(AsyncCursorPage[EmailMessagePointer], inbox_message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMoonbase) -> None:
        async with async_client.inbox_messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = await response.parse()
            assert_matches_type(AsyncCursorPage[EmailMessagePointer], inbox_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMoonbase) -> None:
        inbox_message = await async_client.inbox_messages.delete(
            "id",
        )
        assert inbox_message is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.inbox_messages.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox_message = await response.parse()
        assert inbox_message is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMoonbase) -> None:
        async with async_client.inbox_messages.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox_message = await response.parse()
            assert inbox_message is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.inbox_messages.with_raw_response.delete(
                "",
            )
