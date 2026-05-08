# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from moonbase import Moonbase, AsyncMoonbase
from tests.utils import assert_matches_type
from moonbase.types import Unsubscribe
from moonbase.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUnsubscribes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Moonbase) -> None:
        unsubscribe = client.unsubscribes.create(
            email="yoda@moonbase.ai",
        )
        assert_matches_type(Unsubscribe, unsubscribe, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Moonbase) -> None:
        response = client.unsubscribes.with_raw_response.create(
            email="yoda@moonbase.ai",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unsubscribe = response.parse()
        assert_matches_type(Unsubscribe, unsubscribe, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Moonbase) -> None:
        with client.unsubscribes.with_streaming_response.create(
            email="yoda@moonbase.ai",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unsubscribe = response.parse()
            assert_matches_type(Unsubscribe, unsubscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Moonbase) -> None:
        unsubscribe = client.unsubscribes.list()
        assert_matches_type(SyncCursorPage[Unsubscribe], unsubscribe, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Moonbase) -> None:
        unsubscribe = client.unsubscribes.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorPage[Unsubscribe], unsubscribe, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Moonbase) -> None:
        response = client.unsubscribes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unsubscribe = response.parse()
        assert_matches_type(SyncCursorPage[Unsubscribe], unsubscribe, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Moonbase) -> None:
        with client.unsubscribes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unsubscribe = response.parse()
            assert_matches_type(SyncCursorPage[Unsubscribe], unsubscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Moonbase) -> None:
        unsubscribe = client.unsubscribes.delete(
            "email",
        )
        assert unsubscribe is None

    @parametrize
    def test_raw_response_delete(self, client: Moonbase) -> None:
        response = client.unsubscribes.with_raw_response.delete(
            "email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unsubscribe = response.parse()
        assert unsubscribe is None

    @parametrize
    def test_streaming_response_delete(self, client: Moonbase) -> None:
        with client.unsubscribes.with_streaming_response.delete(
            "email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unsubscribe = response.parse()
            assert unsubscribe is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email` but received ''"):
            client.unsubscribes.with_raw_response.delete(
                "",
            )


class TestAsyncUnsubscribes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMoonbase) -> None:
        unsubscribe = await async_client.unsubscribes.create(
            email="yoda@moonbase.ai",
        )
        assert_matches_type(Unsubscribe, unsubscribe, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.unsubscribes.with_raw_response.create(
            email="yoda@moonbase.ai",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unsubscribe = await response.parse()
        assert_matches_type(Unsubscribe, unsubscribe, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMoonbase) -> None:
        async with async_client.unsubscribes.with_streaming_response.create(
            email="yoda@moonbase.ai",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unsubscribe = await response.parse()
            assert_matches_type(Unsubscribe, unsubscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMoonbase) -> None:
        unsubscribe = await async_client.unsubscribes.list()
        assert_matches_type(AsyncCursorPage[Unsubscribe], unsubscribe, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMoonbase) -> None:
        unsubscribe = await async_client.unsubscribes.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorPage[Unsubscribe], unsubscribe, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.unsubscribes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unsubscribe = await response.parse()
        assert_matches_type(AsyncCursorPage[Unsubscribe], unsubscribe, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMoonbase) -> None:
        async with async_client.unsubscribes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unsubscribe = await response.parse()
            assert_matches_type(AsyncCursorPage[Unsubscribe], unsubscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMoonbase) -> None:
        unsubscribe = await async_client.unsubscribes.delete(
            "email",
        )
        assert unsubscribe is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.unsubscribes.with_raw_response.delete(
            "email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unsubscribe = await response.parse()
        assert unsubscribe is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMoonbase) -> None:
        async with async_client.unsubscribes.with_streaming_response.delete(
            "email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unsubscribe = await response.parse()
            assert unsubscribe is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email` but received ''"):
            await async_client.unsubscribes.with_raw_response.delete(
                "",
            )
