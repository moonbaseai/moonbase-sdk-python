# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from moonbase import Moonbase, AsyncMoonbase
from tests.utils import assert_matches_type
from moonbase.types import Call
from moonbase._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Moonbase) -> None:
        call = client.calls.create(
            direction="incoming",
            participants=[
                {
                    "phone": "phone",
                    "role": "caller",
                }
            ],
            provider="provider",
            provider_id="provider_id",
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="queued",
        )
        assert_matches_type(Call, call, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Moonbase) -> None:
        call = client.calls.create(
            direction="incoming",
            participants=[
                {
                    "phone": "phone",
                    "role": "caller",
                }
            ],
            provider="provider",
            provider_id="provider_id",
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="queued",
            answered_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            end_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            provider_metadata={"foo": "bar"},
        )
        assert_matches_type(Call, call, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Moonbase) -> None:
        response = client.calls.with_raw_response.create(
            direction="incoming",
            participants=[
                {
                    "phone": "phone",
                    "role": "caller",
                }
            ],
            provider="provider",
            provider_id="provider_id",
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="queued",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(Call, call, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Moonbase) -> None:
        with client.calls.with_streaming_response.create(
            direction="incoming",
            participants=[
                {
                    "phone": "phone",
                    "role": "caller",
                }
            ],
            provider="provider",
            provider_id="provider_id",
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="queued",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(Call, call, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMoonbase) -> None:
        call = await async_client.calls.create(
            direction="incoming",
            participants=[
                {
                    "phone": "phone",
                    "role": "caller",
                }
            ],
            provider="provider",
            provider_id="provider_id",
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="queued",
        )
        assert_matches_type(Call, call, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMoonbase) -> None:
        call = await async_client.calls.create(
            direction="incoming",
            participants=[
                {
                    "phone": "phone",
                    "role": "caller",
                }
            ],
            provider="provider",
            provider_id="provider_id",
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="queued",
            answered_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            end_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            provider_metadata={"foo": "bar"},
        )
        assert_matches_type(Call, call, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.calls.with_raw_response.create(
            direction="incoming",
            participants=[
                {
                    "phone": "phone",
                    "role": "caller",
                }
            ],
            provider="provider",
            provider_id="provider_id",
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="queued",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(Call, call, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMoonbase) -> None:
        async with async_client.calls.with_streaming_response.create(
            direction="incoming",
            participants=[
                {
                    "phone": "phone",
                    "role": "caller",
                }
            ],
            provider="provider",
            provider_id="provider_id",
            start_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="queued",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(Call, call, path=["response"])

        assert cast(Any, response.is_closed) is True
