# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .meeting_transcript_speaker import MeetingTranscriptSpeaker

__all__ = ["MeetingTranscriptCue"]


class MeetingTranscriptCue(BaseModel):
    from_: float = FieldInfo(alias="from")

    speaker: MeetingTranscriptSpeaker

    text: str

    to: float
