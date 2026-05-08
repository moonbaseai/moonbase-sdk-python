# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FunnelCreateParams", "Step"]


class FunnelCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the funnel."""

    steps: Iterable[Step]
    """An ordered list of steps to create. Array order determines step order."""


class Step(TypedDict, total=False):
    """Parameters for creating a funnel step."""

    color: Required[
        Literal[
            "amber",
            "blue",
            "cyan",
            "emerald",
            "fuchsia",
            "green",
            "indigo",
            "lime",
            "lunar",
            "orange",
            "pink",
            "purple",
            "red",
            "rose",
            "sky",
            "teal",
            "violet",
            "yellow",
        ]
    ]
    """The display color of the step."""

    name: Required[str]
    """The name of the step."""

    step_type: Required[Literal["active", "success", "failure"]]
    """The status of the step in the funnel flow.

    - `active`: represents an in progress state within the funnel
    - `success`: completed successfully and exited the funnel
    - `failure`: exited the funnel without conversion
    """
