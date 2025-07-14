# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from moonbase_sdk import Moonbase, AsyncMoonbase
from moonbase_sdk.types import Item

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Moonbase) -> None:
        item = client.items.create(
            collection_id="1CR2QLsnhwrJX7Z33jnyGV",
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "ceo": {
                    "item": {
                        "id": "1CR2QLtx9doK4wFiFB7VAS",
                        "type": "item",
                    },
                    "type": "value/relation",
                },
            },
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Moonbase) -> None:
        response = client.items.with_raw_response.create(
            collection_id="1CR2QLsnhwrJX7Z33jnyGV",
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "ceo": {
                    "item": {
                        "id": "1CR2QLtx9doK4wFiFB7VAS",
                        "type": "item",
                    },
                    "type": "value/relation",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Moonbase) -> None:
        with client.items.with_streaming_response.create(
            collection_id="1CR2QLsnhwrJX7Z33jnyGV",
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "ceo": {
                    "item": {
                        "id": "1CR2QLtx9doK4wFiFB7VAS",
                        "type": "item",
                    },
                    "type": "value/relation",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Moonbase) -> None:
        item = client.items.retrieve(
            "id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Moonbase) -> None:
        response = client.items.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Moonbase) -> None:
        with client.items.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.items.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Moonbase) -> None:
        item = client.items.update(
            id="id",
            values={
                "foo": {
                    "text": "text",
                    "type": "value/text/single_line",
                }
            },
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Moonbase) -> None:
        item = client.items.update(
            id="id",
            values={
                "foo": {
                    "text": "text",
                    "type": "value/text/single_line",
                }
            },
            update_many_strategy="replace",
            update_one_strategy="replace",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Moonbase) -> None:
        response = client.items.with_raw_response.update(
            id="id",
            values={
                "foo": {
                    "text": "text",
                    "type": "value/text/single_line",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Moonbase) -> None:
        with client.items.with_streaming_response.update(
            id="id",
            values={
                "foo": {
                    "text": "text",
                    "type": "value/text/single_line",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.items.with_raw_response.update(
                id="",
                values={
                    "foo": {
                        "text": "text",
                        "type": "value/text/single_line",
                    }
                },
            )

    @parametrize
    def test_method_delete(self, client: Moonbase) -> None:
        item = client.items.delete(
            "id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Moonbase) -> None:
        response = client.items.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Moonbase) -> None:
        with client.items.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Moonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.items.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_upsert(self, client: Moonbase) -> None:
        item = client.items.upsert(
            collection_id="1CR2QLbeMAqKQ6PvQu39pZ",
            identifiers={"domain": []},
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "domain": [],
                "linked_in": {
                    "profile": {},
                    "type": "value/uri/social_linked_in",
                },
            },
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_method_upsert_with_all_params(self, client: Moonbase) -> None:
        item = client.items.upsert(
            collection_id="1CR2QLbeMAqKQ6PvQu39pZ",
            identifiers={"domain": []},
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "domain": [],
                "linked_in": {
                    "profile": {
                        "url": "https://linkedin.com/company/aperturescience",
                        "username": "username",
                    },
                    "type": "value/uri/social_linked_in",
                },
            },
            update_many_strategy="replace",
            update_one_strategy="replace",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_upsert(self, client: Moonbase) -> None:
        response = client.items.with_raw_response.upsert(
            collection_id="1CR2QLbeMAqKQ6PvQu39pZ",
            identifiers={"domain": []},
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "domain": [],
                "linked_in": {
                    "profile": {},
                    "type": "value/uri/social_linked_in",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_streaming_response_upsert(self, client: Moonbase) -> None:
        with client.items.with_streaming_response.upsert(
            collection_id="1CR2QLbeMAqKQ6PvQu39pZ",
            identifiers={"domain": []},
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "domain": [],
                "linked_in": {
                    "profile": {},
                    "type": "value/uri/social_linked_in",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMoonbase) -> None:
        item = await async_client.items.create(
            collection_id="1CR2QLsnhwrJX7Z33jnyGV",
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "ceo": {
                    "item": {
                        "id": "1CR2QLtx9doK4wFiFB7VAS",
                        "type": "item",
                    },
                    "type": "value/relation",
                },
            },
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.items.with_raw_response.create(
            collection_id="1CR2QLsnhwrJX7Z33jnyGV",
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "ceo": {
                    "item": {
                        "id": "1CR2QLtx9doK4wFiFB7VAS",
                        "type": "item",
                    },
                    "type": "value/relation",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMoonbase) -> None:
        async with async_client.items.with_streaming_response.create(
            collection_id="1CR2QLsnhwrJX7Z33jnyGV",
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "ceo": {
                    "item": {
                        "id": "1CR2QLtx9doK4wFiFB7VAS",
                        "type": "item",
                    },
                    "type": "value/relation",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMoonbase) -> None:
        item = await async_client.items.retrieve(
            "id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.items.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMoonbase) -> None:
        async with async_client.items.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.items.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMoonbase) -> None:
        item = await async_client.items.update(
            id="id",
            values={
                "foo": {
                    "text": "text",
                    "type": "value/text/single_line",
                }
            },
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMoonbase) -> None:
        item = await async_client.items.update(
            id="id",
            values={
                "foo": {
                    "text": "text",
                    "type": "value/text/single_line",
                }
            },
            update_many_strategy="replace",
            update_one_strategy="replace",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.items.with_raw_response.update(
            id="id",
            values={
                "foo": {
                    "text": "text",
                    "type": "value/text/single_line",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMoonbase) -> None:
        async with async_client.items.with_streaming_response.update(
            id="id",
            values={
                "foo": {
                    "text": "text",
                    "type": "value/text/single_line",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.items.with_raw_response.update(
                id="",
                values={
                    "foo": {
                        "text": "text",
                        "type": "value/text/single_line",
                    }
                },
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMoonbase) -> None:
        item = await async_client.items.delete(
            "id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.items.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMoonbase) -> None:
        async with async_client.items.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMoonbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.items.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_upsert(self, async_client: AsyncMoonbase) -> None:
        item = await async_client.items.upsert(
            collection_id="1CR2QLbeMAqKQ6PvQu39pZ",
            identifiers={"domain": []},
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "domain": [],
                "linked_in": {
                    "profile": {},
                    "type": "value/uri/social_linked_in",
                },
            },
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncMoonbase) -> None:
        item = await async_client.items.upsert(
            collection_id="1CR2QLbeMAqKQ6PvQu39pZ",
            identifiers={"domain": []},
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "domain": [],
                "linked_in": {
                    "profile": {
                        "url": "https://linkedin.com/company/aperturescience",
                        "username": "username",
                    },
                    "type": "value/uri/social_linked_in",
                },
            },
            update_many_strategy="replace",
            update_one_strategy="replace",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncMoonbase) -> None:
        response = await async_client.items.with_raw_response.upsert(
            collection_id="1CR2QLbeMAqKQ6PvQu39pZ",
            identifiers={"domain": []},
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "domain": [],
                "linked_in": {
                    "profile": {},
                    "type": "value/uri/social_linked_in",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncMoonbase) -> None:
        async with async_client.items.with_streaming_response.upsert(
            collection_id="1CR2QLbeMAqKQ6PvQu39pZ",
            identifiers={"domain": []},
            values={
                "name": {
                    "text": "Aperture Science",
                    "type": "value/text/single_line",
                },
                "domain": [],
                "linked_in": {
                    "profile": {},
                    "type": "value/uri/social_linked_in",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True
