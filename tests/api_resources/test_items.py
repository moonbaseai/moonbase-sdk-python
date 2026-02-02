# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from moonbase import Moonbase, AsyncMoonbase
from tests.utils import assert_matches_type
from moonbase.types import ItemSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search(self, client: Moonbase) -> None:
        item = client.items.search(
            query="query",
        )
        assert_matches_type(ItemSearchResponse, item, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Moonbase) -> None:
        item = client.items.search(
            query="query",
            filter={"collection_id": {"in": ["string"]}},
        )
        assert_matches_type(ItemSearchResponse, item, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Moonbase) -> None:
        response = client.items.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemSearchResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Moonbase) -> None:
        with client.items.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemSearchResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_search(self, async_client: AsyncMoonbase) -> None:
        item = await async_client.items.search(
            query="query",
        )
        assert_matches_type(ItemSearchResponse, item, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncMoonbase) -> None:
        item = await async_client.items.search(
            query="query",
            filter={"collection_id": {"in": ["string"]}},
        )
        assert_matches_type(ItemSearchResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.items.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemSearchResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMoonbase) -> None:
        async with async_client.items.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemSearchResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True
