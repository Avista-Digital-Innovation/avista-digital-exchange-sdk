# Generated by ariadne-codegen on 2024-11-12 13:55
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import DataCaptureRecordError


class OnCapturePublishData(BaseModel):
    on_capture_publish_data: Optional[
        "OnCapturePublishDataOnCapturePublishData"
    ] = Field(alias="onCapturePublishData")


class OnCapturePublishDataOnCapturePublishData(BaseModel):
    capture_id: str = Field(alias="captureId")
    data_written: Optional[
        List[Optional["OnCapturePublishDataOnCapturePublishDataDataWritten"]]
    ] = Field(alias="dataWritten")
    failed_records: Optional[
        List[Optional["OnCapturePublishDataOnCapturePublishDataFailedRecords"]]
    ] = Field(alias="failedRecords")
    logs: Optional[List[Optional["OnCapturePublishDataOnCapturePublishDataLogs"]]]


class OnCapturePublishDataOnCapturePublishDataDataWritten(BaseModel):
    timestamp: str
    user_defined_id: str = Field(alias="userDefinedId")
    value: str


class OnCapturePublishDataOnCapturePublishDataFailedRecords(BaseModel):
    attribute_index: Optional[int] = Field(alias="attributeIndex")
    error_type: DataCaptureRecordError = Field(alias="errorType")
    message: Optional[str]
    record_index: int = Field(alias="recordIndex")


class OnCapturePublishDataOnCapturePublishDataLogs(BaseModel):
    error: Optional[bool]
    message: Optional[str]


OnCapturePublishData.update_forward_refs()
OnCapturePublishDataOnCapturePublishData.update_forward_refs()
OnCapturePublishDataOnCapturePublishDataDataWritten.update_forward_refs()
OnCapturePublishDataOnCapturePublishDataFailedRecords.update_forward_refs()
OnCapturePublishDataOnCapturePublishDataLogs.update_forward_refs()
