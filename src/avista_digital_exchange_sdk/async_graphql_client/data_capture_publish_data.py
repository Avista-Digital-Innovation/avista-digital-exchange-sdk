# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import DataCaptureRecordError


class DataCapturePublishData(BaseModel):
    data_capture_publish_data: Optional[
        "DataCapturePublishDataDataCapturePublishData"
    ] = Field(alias="dataCapture_publishData")


class DataCapturePublishDataDataCapturePublishData(BaseModel):
    capture_id: str = Field(alias="captureId")
    data_written: Optional[
        List[Optional["DataCapturePublishDataDataCapturePublishDataDataWritten"]]
    ] = Field(alias="dataWritten")
    failed_records: Optional[
        List[Optional["DataCapturePublishDataDataCapturePublishDataFailedRecords"]]
    ] = Field(alias="failedRecords")
    logs: Optional[List[Optional["DataCapturePublishDataDataCapturePublishDataLogs"]]]


class DataCapturePublishDataDataCapturePublishDataDataWritten(BaseModel):
    timestamp: str
    user_defined_id: str = Field(alias="userDefinedId")
    value: str


class DataCapturePublishDataDataCapturePublishDataFailedRecords(BaseModel):
    attribute_index: Optional[int] = Field(alias="attributeIndex")
    error_type: DataCaptureRecordError = Field(alias="errorType")
    message: Optional[str]
    record_index: int = Field(alias="recordIndex")


class DataCapturePublishDataDataCapturePublishDataLogs(BaseModel):
    error: Optional[bool]
    message: Optional[str]


DataCapturePublishData.update_forward_refs()
DataCapturePublishDataDataCapturePublishData.update_forward_refs()
DataCapturePublishDataDataCapturePublishDataDataWritten.update_forward_refs()
DataCapturePublishDataDataCapturePublishDataFailedRecords.update_forward_refs()
DataCapturePublishDataDataCapturePublishDataLogs.update_forward_refs()