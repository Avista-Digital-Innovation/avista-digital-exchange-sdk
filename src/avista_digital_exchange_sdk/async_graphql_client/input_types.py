# Generated by ariadne-codegen on 2023-07-17 11:23
# Source: ../input/schema.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    CaptureSortBy,
    DataCaptureAssetAttributeSchemaType,
    DataCaptureAssetAttributeType,
    DataCaptureState,
    DataStoreObjectType,
    DimensionValueType,
    MeasureValueType,
    ModelSchemaType,
    TimeUnit,
)


class DataCaptureAssetAttributeInput(BaseModel):
    attribute_type: DataCaptureAssetAttributeType = Field(alias="attributeType")
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    schema_type: DataCaptureAssetAttributeSchemaType = Field(alias="schemaType")
    unit: Optional[str]
    user_defined_id: str = Field(alias="userDefinedId")


class DataCaptureAssetInput(BaseModel):
    attributes: List["DataCaptureAssetAttributeInput"]
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    user_defined_id: str = Field(alias="userDefinedId")


class DataCaptureAttributeValueInput(BaseModel):
    user_defined_id: str = Field(alias="userDefinedId")
    value: str


class DataCaptureDataModelInput(BaseModel):
    assets: List["DataCaptureAssetInput"]


class DataCaptureDataRecordInput(BaseModel):
    attribute_values: List["DataCaptureAttributeValueInput"] = Field(
        alias="attributeValues"
    )
    timestamp: str


class DataStoreObjectIdInput(BaseModel):
    data_store_directory_id: Optional[str] = Field(alias="dataStoreDirectoryId")
    data_store_file_id: Optional[str] = Field(alias="dataStoreFileId")
    object_type: DataStoreObjectType = Field(alias="objectType")


class EndpointPropertyInput(BaseModel):
    name: str
    timestamp: str
    value: str


class EndpointQueryFilter(BaseModel):
    attribute_names: List[str] = Field(alias="attributeNames")
    iot_endpoint_id: str = Field(alias="iotEndpointId")


class IotAttributeValueInput(BaseModel):
    name: str
    value: str


class IotDataRecordInput(BaseModel):
    attributes: Optional[List[Optional["IotAttributeValueInput"]]]
    time_unit: Optional[TimeUnit] = Field(alias="timeUnit")
    timestamp: Optional[str]


class ListCapturesFilterInput(BaseModel):
    sort_by: Optional[CaptureSortBy] = Field(alias="sortBy")
    state: Optional[DataCaptureState]


class MeasureValueInput(BaseModel):
    name: str = Field(alias="Name")
    type: MeasureValueType = Field(alias="Type")
    value: str = Field(alias="Value")


class ModelPropertyInput(BaseModel):
    default_value: Optional[str] = Field(alias="defaultValue")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")
    writable: Optional[bool]


class ModelTelemetryInput(BaseModel):
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")


class S3ObjectInput(BaseModel):
    bucket: Optional[str]
    key: Optional[str]
    mime_type: Optional[str] = Field(alias="mimeType")
    region: Optional[str]
    upload_url: Optional[str] = Field(alias="uploadUrl")
    url: Optional[str]


class TimeSeriesDbCommonAttributesInput(BaseModel):
    measure_name: Optional[str] = Field(alias="MeasureName")
    measure_value: Optional[str] = Field(alias="MeasureValue")
    measure_value_type: Optional[MeasureValueType] = Field(alias="MeasureValueType")
    measure_values: Optional[List[Optional["MeasureValueInput"]]] = Field(
        alias="MeasureValues"
    )
    time: Optional[str] = Field(alias="Time")
    time_unit: Optional[TimeUnit] = Field(alias="TimeUnit")
    version: Optional[int] = Field(alias="Version")
    dimensions: Optional[List[Optional["TimeSeriesDbDimensionInput"]]]


class TimeSeriesDbDataInput(BaseModel):
    records: List["TimeSeriesDbRecordInput"]


class TimeSeriesDbDimensionInput(BaseModel):
    dimension_value_type: Optional[DimensionValueType] = Field(
        alias="DimensionValueType"
    )
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class TimeSeriesDbRecordInput(BaseModel):
    dimensions: Optional[List[Optional["TimeSeriesDbDimensionInput"]]] = Field(
        alias="Dimensions"
    )
    measure_name: Optional[str] = Field(alias="MeasureName")
    measure_value: Optional[str] = Field(alias="MeasureValue")
    measure_value_type: Optional[MeasureValueType] = Field(alias="MeasureValueType")
    measure_values: Optional[List[Optional["MeasureValueInput"]]] = Field(
        alias="MeasureValues"
    )
    time: Optional[str] = Field(alias="Time")
    time_unit: Optional[TimeUnit] = Field(alias="TimeUnit")
    version: Optional[int] = Field(alias="Version")


class TimeSeriesQueryAssetInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    attribute_names_filter: Optional[List[Optional[str]]] = Field(
        alias="attributeNamesFilter"
    )


DataCaptureAssetAttributeInput.update_forward_refs()
DataCaptureAssetInput.update_forward_refs()
DataCaptureAttributeValueInput.update_forward_refs()
DataCaptureDataModelInput.update_forward_refs()
DataCaptureDataRecordInput.update_forward_refs()
DataStoreObjectIdInput.update_forward_refs()
EndpointPropertyInput.update_forward_refs()
EndpointQueryFilter.update_forward_refs()
IotAttributeValueInput.update_forward_refs()
IotDataRecordInput.update_forward_refs()
ListCapturesFilterInput.update_forward_refs()
MeasureValueInput.update_forward_refs()
ModelPropertyInput.update_forward_refs()
ModelTelemetryInput.update_forward_refs()
S3ObjectInput.update_forward_refs()
TimeSeriesDbCommonAttributesInput.update_forward_refs()
TimeSeriesDbDataInput.update_forward_refs()
TimeSeriesDbDimensionInput.update_forward_refs()
TimeSeriesDbRecordInput.update_forward_refs()
TimeSeriesQueryAssetInput.update_forward_refs()