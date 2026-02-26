# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MeetingUpdateParams", "Recording", "Transcript", "TranscriptCue"]


class MeetingUpdateParams(TypedDict, total=False):
    recording: Recording
    """A video recording of the meeting."""

    transcript: Transcript
    """The meeting transcript."""


class Recording(TypedDict, total=False):
    """A video recording of the meeting."""

    content_type: Required[Literal["video/mp4"]]
    """The content type of the recording.

    Note that only `video/mp4` is supported at this time.
    """

    provider_id: Required[str]
    """The unique identifier for the recording from the provider's system."""

    url: Required[str]
    """The URL pointing to the recording."""


_TranscriptCueReservedKeywords = TypedDict(
    "_TranscriptCueReservedKeywords",
    {
        "from": float,
    },
    total=False,
)


class TranscriptCue(_TranscriptCueReservedKeywords, total=False):
    """
    Parameters for creating a `MeetingTranscriptCue` object to capture the text spoken in a specific time slice.
    """

    speaker: Required[str]
    """The name of the person speaking."""

    text: Required[str]
    """The text spoken during the slice."""

    to: Required[float]
    """The end time of the slice, in fractional seconds from the start of the meeting."""


class Transcript(TypedDict, total=False):
    """The meeting transcript."""

    cues: Required[Iterable[TranscriptCue]]
    """
    A list of cues that identify the text spoken in specific time slices of the
    meeting.
    """

    provider: Required[str]
    """Identifies the source of the transcript."""

    provider_id: Required[str]
    """The unique identifier for the transcript from the provider's system."""
