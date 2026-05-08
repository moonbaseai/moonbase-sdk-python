# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ProgramActivityMetrics"]


class ProgramActivityMetrics(BaseModel):
    """
    The ProgramActivityMetrics object provides a summary of engagement and delivery statistics for a marketing program.
    """

    bounced: int
    """The number of emails that could not be delivered."""

    clicked: int
    """The number of recipients who clicked at least one link."""

    complained: int
    """The number of recipients who marked the email as spam."""

    failed: int
    """The number of emails that failed to send due to a technical issue."""

    opened: int
    """The number of recipients who opened the email."""

    sent: int
    """The total number of emails successfully sent."""

    shielded: int
    """The number of emails blocked by delivery protection rules."""

    unsubscribed: int
    """The number of recipients who unsubscribed."""
