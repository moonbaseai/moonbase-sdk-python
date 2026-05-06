# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .call_transcript_cue import CallTranscriptCue

__all__ = ["CallTranscript"]


class CallTranscript(BaseModel):
    cues: List[CallTranscriptCue]
