# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from moonbase import Moonbase, AsyncMoonbase
from tests.utils import assert_matches_type
from moonbase.types import View, ViewListResponse
from moonbase.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestViews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Moonbase) -> None:
        view = client.views.create(
            collection={"type": "collection"},
            fields=[{"field": "name"}, {"field": "email"}],
            name="Active leads",
            view_type="table",
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Moonbase) -> None:
        view = client.views.create(
            collection={
                "type": "collection",
                "id": "id",
                "ref": "people",
            },
            fields=[
                {
                    "field": "name",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "email",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
            ],
            name="Active leads",
            view_type="table",
            aggregates=[
                {
                    "type": "item_count",
                    "group": "group",
                }
            ],
            filter={
                "field": "name",
                "op": "contains",
                "value": "Acme",
            },
            groups=["string"],
            relation_value_filters=[
                {
                    "field": "field",
                    "filter": {
                        "field": "field",
                        "op": "starts_with",
                        "value": "string",
                    },
                }
            ],
            sort=["-name"],
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Moonbase) -> None:
        response = client.views.with_raw_response.create(
            collection={"type": "collection"},
            fields=[{"field": "name"}, {"field": "email"}],
            name="Active leads",
            view_type="table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(View, view, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Moonbase) -> None:
        with client.views.with_streaming_response.create(
            collection={"type": "collection"},
            fields=[{"field": "name"}, {"field": "email"}],
            name="Active leads",
            view_type="table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(View, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Moonbase) -> None:
        view = client.views.retrieve(
            "id",
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Moonbase) -> None:
        response = client.views.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(View, view, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Moonbase) -> None:
        with client.views.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(View, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.views.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Moonbase) -> None:
        view = client.views.update(
            id="id",
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Moonbase) -> None:
        view = client.views.update(
            id="id",
            aggregates=[
                {
                    "type": "item_count",
                    "group": "stage",
                }
            ],
            fields=[
                {
                    "field": "name",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "amount",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "stage",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "owner",
                    "display_fields": ["name", "email"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "related_tasks",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
            ],
            filter={
                "field": "name",
                "op": "eq",
                "value": "Acme",
            },
            groups=["stage"],
            name="Active deals",
            relation_value_filters=[
                {
                    "field": "related_tasks",
                    "filter": {
                        "field": "state",
                        "op": "eq",
                        "value": "Open",
                    },
                }
            ],
            sort=["-name"],
            view_type="table",
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Moonbase) -> None:
        response = client.views.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(View, view, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Moonbase) -> None:
        with client.views.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(View, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.views.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Moonbase) -> None:
        view = client.views.list()
        assert_matches_type(SyncCursorPage[ViewListResponse], view, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Moonbase) -> None:
        view = client.views.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorPage[ViewListResponse], view, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Moonbase) -> None:
        response = client.views.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(SyncCursorPage[ViewListResponse], view, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Moonbase) -> None:
        with client.views.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(SyncCursorPage[ViewListResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Moonbase) -> None:
        view = client.views.delete(
            "id",
        )
        assert view is None

    @parametrize
    def test_raw_response_delete(self, client: Moonbase) -> None:
        response = client.views.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert view is None

    @parametrize
    def test_streaming_response_delete(self, client: Moonbase) -> None:
        with client.views.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert view is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.views.with_raw_response.delete(
                "",
            )


class TestAsyncViews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMoonbase) -> None:
        view = await async_client.views.create(
            collection={"type": "collection"},
            fields=[{"field": "name"}, {"field": "email"}],
            name="Active leads",
            view_type="table",
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMoonbase) -> None:
        view = await async_client.views.create(
            collection={
                "type": "collection",
                "id": "id",
                "ref": "people",
            },
            fields=[
                {
                    "field": "name",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "email",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
            ],
            name="Active leads",
            view_type="table",
            aggregates=[
                {
                    "type": "item_count",
                    "group": "group",
                }
            ],
            filter={
                "field": "name",
                "op": "contains",
                "value": "Acme",
            },
            groups=["string"],
            relation_value_filters=[
                {
                    "field": "field",
                    "filter": {
                        "field": "field",
                        "op": "starts_with",
                        "value": "string",
                    },
                }
            ],
            sort=["-name"],
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.views.with_raw_response.create(
            collection={"type": "collection"},
            fields=[{"field": "name"}, {"field": "email"}],
            name="Active leads",
            view_type="table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(View, view, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMoonbase) -> None:
        async with async_client.views.with_streaming_response.create(
            collection={"type": "collection"},
            fields=[{"field": "name"}, {"field": "email"}],
            name="Active leads",
            view_type="table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(View, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMoonbase) -> None:
        view = await async_client.views.retrieve(
            "id",
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.views.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(View, view, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMoonbase) -> None:
        async with async_client.views.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(View, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.views.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMoonbase) -> None:
        view = await async_client.views.update(
            id="id",
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMoonbase) -> None:
        view = await async_client.views.update(
            id="id",
            aggregates=[
                {
                    "type": "item_count",
                    "group": "stage",
                }
            ],
            fields=[
                {
                    "field": "name",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "amount",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "stage",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "owner",
                    "display_fields": ["name", "email"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
                {
                    "field": "related_tasks",
                    "display_fields": ["string"],
                    "is_pinned": True,
                    "is_wrapped": True,
                    "size": "fit",
                },
            ],
            filter={
                "field": "name",
                "op": "eq",
                "value": "Acme",
            },
            groups=["stage"],
            name="Active deals",
            relation_value_filters=[
                {
                    "field": "related_tasks",
                    "filter": {
                        "field": "state",
                        "op": "eq",
                        "value": "Open",
                    },
                }
            ],
            sort=["-name"],
            view_type="table",
        )
        assert_matches_type(View, view, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.views.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(View, view, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMoonbase) -> None:
        async with async_client.views.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(View, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.views.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMoonbase) -> None:
        view = await async_client.views.list()
        assert_matches_type(AsyncCursorPage[ViewListResponse], view, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMoonbase) -> None:
        view = await async_client.views.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorPage[ViewListResponse], view, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.views.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(AsyncCursorPage[ViewListResponse], view, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMoonbase) -> None:
        async with async_client.views.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(AsyncCursorPage[ViewListResponse], view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMoonbase) -> None:
        view = await async_client.views.delete(
            "id",
        )
        assert view is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.views.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert view is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMoonbase) -> None:
        async with async_client.views.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert view is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.views.with_raw_response.delete(
                "",
            )
