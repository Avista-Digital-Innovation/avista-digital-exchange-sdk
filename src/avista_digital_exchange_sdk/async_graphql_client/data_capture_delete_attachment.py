# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import DataCaptureAttachmentError, DataCaptureAttachmentType


class DataCaptureDeleteAttachment(BaseModel):
    data_capture_delete_attachment: Optional[
        "DataCaptureDeleteAttachmentDataCaptureDeleteAttachment"
    ] = Field(alias="dataCapture_deleteAttachment")


class DataCaptureDeleteAttachmentDataCaptureDeleteAttachment(BaseModel):
    attachment_id: str = Field(alias="attachmentId")
    attachment_type: DataCaptureAttachmentType = Field(alias="attachmentType")
    date_created: Optional[str] = Field(alias="dateCreated")
    date_updated: Optional[str] = Field(alias="dateUpdated")
    description: Optional[str]
    error: Optional[DataCaptureAttachmentError]
    name: Optional[str]
    owner_user_id: str = Field(alias="ownerUserId")


DataCaptureDeleteAttachment.update_forward_refs()
DataCaptureDeleteAttachmentDataCaptureDeleteAttachment.update_forward_refs()
