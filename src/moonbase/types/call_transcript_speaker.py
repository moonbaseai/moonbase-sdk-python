# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CallTranscriptSpeaker"]


class CallTranscriptSpeaker(BaseModel):
    attendee_id: Optional[str] = None

    label: Optional[str] = None
