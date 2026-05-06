# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .meeting_transcript_cue import MeetingTranscriptCue

__all__ = ["MeetingTranscript"]


class MeetingTranscript(BaseModel):
    cues: List[MeetingTranscriptCue]
