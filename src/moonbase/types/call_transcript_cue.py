# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .call_transcript_speaker import CallTranscriptSpeaker

__all__ = ["CallTranscriptCue"]


class CallTranscriptCue(BaseModel):
    from_: float = FieldInfo(alias="from")

    speaker: CallTranscriptSpeaker

    text: str

    to: float
