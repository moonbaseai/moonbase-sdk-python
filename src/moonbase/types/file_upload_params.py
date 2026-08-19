# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import FileTypes
from .item_pointer_param import ItemPointerParam

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The raw file content to upload in a multipart/form-data request.

    Must be 5 MB or smaller.
    """

    associations: Iterable[ItemPointerParam]
    """
    Link the File to Moonbase items like a person, organization, deal, task, or an
    item in a custom collection.
    """

    name: str
    """The display name of the file."""
