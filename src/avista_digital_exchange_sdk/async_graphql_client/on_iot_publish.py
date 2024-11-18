# Generated by ariadne-codegen on 2024-11-12 13:55
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import IotDataRecordErrorType


class OnIotPublish(BaseModel):
    on_iot_publish: Optional["OnIotPublishOnIotPublish"] = Field(alias="onIotPublish")


class OnIotPublishOnIotPublish(BaseModel):
    iot_endpoint_id: Optional[str] = Field(alias="iotEndpointId")
    failed_records: Optional[
        List[Optional["OnIotPublishOnIotPublishFailedRecords"]]
    ] = Field(alias="failedRecords")
    records_written: Optional[
        List[Optional["OnIotPublishOnIotPublishRecordsWritten"]]
    ] = Field(alias="recordsWritten")


class OnIotPublishOnIotPublishFailedRecords(BaseModel):
    errors: List[Optional["OnIotPublishOnIotPublishFailedRecordsErrors"]]
    record: "OnIotPublishOnIotPublishFailedRecordsRecord"


class OnIotPublishOnIotPublishFailedRecordsErrors(BaseModel):
    error_message: str = Field(alias="errorMessage")
    error_type: IotDataRecordErrorType = Field(alias="errorType")


class OnIotPublishOnIotPublishFailedRecordsRecord(BaseModel):
    attributes: Optional[
        List[Optional["OnIotPublishOnIotPublishFailedRecordsRecordAttributes"]]
    ]
    iot_endpoint_id: Optional[str] = Field(alias="iotEndpointId")
    timestamp: Optional[str]


class OnIotPublishOnIotPublishFailedRecordsRecordAttributes(BaseModel):
    name: Optional[str]
    schema_type: Optional[str] = Field(alias="schemaType")
    value: Optional[str]


class OnIotPublishOnIotPublishRecordsWritten(BaseModel):
    attributes: Optional[
        List[Optional["OnIotPublishOnIotPublishRecordsWrittenAttributes"]]
    ]
    iot_endpoint_id: Optional[str] = Field(alias="iotEndpointId")
    timestamp: Optional[str]


class OnIotPublishOnIotPublishRecordsWrittenAttributes(BaseModel):
    name: Optional[str]
    schema_type: Optional[str] = Field(alias="schemaType")
    value: Optional[str]


OnIotPublish.update_forward_refs()
OnIotPublishOnIotPublish.update_forward_refs()
OnIotPublishOnIotPublishFailedRecords.update_forward_refs()
OnIotPublishOnIotPublishFailedRecordsErrors.update_forward_refs()
OnIotPublishOnIotPublishFailedRecordsRecord.update_forward_refs()
OnIotPublishOnIotPublishFailedRecordsRecordAttributes.update_forward_refs()
OnIotPublishOnIotPublishRecordsWritten.update_forward_refs()
OnIotPublishOnIotPublishRecordsWrittenAttributes.update_forward_refs()
