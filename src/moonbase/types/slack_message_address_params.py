# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SlackMessageAddressParams"]


class SlackMessageAddressParams(TypedDict, total=False):
    provider_id: Required[str]
    """The Slack channel ID."""

    type: Required[Literal["slack_channel"]]

    name: str
    """The channel name name."""
