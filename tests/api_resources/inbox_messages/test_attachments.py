# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from moonbase import Moonbase, AsyncMoonbase
from tests.utils import assert_matches_type
from moonbase.types import MessageAttachment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttachments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Moonbase) -> None:
        attachment = client.inbox_messages.attachments.create(
            inbox_message_id="inbox_message_id",
        )
        assert_matches_type(MessageAttachment, attachment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Moonbase) -> None:
        attachment = client.inbox_messages.attachments.create(
            inbox_message_id="inbox_message_id",
            file=b"Example data",
            file_id="file_id",
        )
        assert_matches_type(MessageAttachment, attachment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Moonbase) -> None:
        response = client.inbox_messages.attachments.with_raw_response.create(
            inbox_message_id="inbox_message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(MessageAttachment, attachment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Moonbase) -> None:
        with client.inbox_messages.attachments.with_streaming_response.create(
            inbox_message_id="inbox_message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(MessageAttachment, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_message_id` but received ''"):
            client.inbox_messages.attachments.with_raw_response.create(
                inbox_message_id="",
            )

    @parametrize
    def test_method_delete(self, client: Moonbase) -> None:
        attachment = client.inbox_messages.attachments.delete(
            id="id",
            inbox_message_id="inbox_message_id",
        )
        assert attachment is None

    @parametrize
    def test_raw_response_delete(self, client: Moonbase) -> None:
        response = client.inbox_messages.attachments.with_raw_response.delete(
            id="id",
            inbox_message_id="inbox_message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert attachment is None

    @parametrize
    def test_streaming_response_delete(self, client: Moonbase) -> None:
        with client.inbox_messages.attachments.with_streaming_response.delete(
            id="id",
            inbox_message_id="inbox_message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert attachment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_message_id` but received ''"):
            client.inbox_messages.attachments.with_raw_response.delete(
                id="id",
                inbox_message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.inbox_messages.attachments.with_raw_response.delete(
                id="",
                inbox_message_id="inbox_message_id",
            )


class TestAsyncAttachments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMoonbase) -> None:
        attachment = await async_client.inbox_messages.attachments.create(
            inbox_message_id="inbox_message_id",
        )
        assert_matches_type(MessageAttachment, attachment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMoonbase) -> None:
        attachment = await async_client.inbox_messages.attachments.create(
            inbox_message_id="inbox_message_id",
            file=b"Example data",
            file_id="file_id",
        )
        assert_matches_type(MessageAttachment, attachment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.inbox_messages.attachments.with_raw_response.create(
            inbox_message_id="inbox_message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(MessageAttachment, attachment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMoonbase) -> None:
        async with async_client.inbox_messages.attachments.with_streaming_response.create(
            inbox_message_id="inbox_message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(MessageAttachment, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_message_id` but received ''"):
            await async_client.inbox_messages.attachments.with_raw_response.create(
                inbox_message_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMoonbase) -> None:
        attachment = await async_client.inbox_messages.attachments.delete(
            id="id",
            inbox_message_id="inbox_message_id",
        )
        assert attachment is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.inbox_messages.attachments.with_raw_response.delete(
            id="id",
            inbox_message_id="inbox_message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert attachment is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMoonbase) -> None:
        async with async_client.inbox_messages.attachments.with_streaming_response.delete(
            id="id",
            inbox_message_id="inbox_message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert attachment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_message_id` but received ''"):
            await async_client.inbox_messages.attachments.with_raw_response.delete(
                id="id",
                inbox_message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.inbox_messages.attachments.with_raw_response.delete(
                id="",
                inbox_message_id="inbox_message_id",
            )
