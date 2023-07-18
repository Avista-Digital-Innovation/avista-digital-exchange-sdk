# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ModelAttributeType, ModelSchemaType


class IotListHubsEndpointsLastValues(BaseModel):
    iot_list_hubs_endpoints_last_values: Optional[
        "IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValues"
    ] = Field(alias="iot_listHubsEndpointsLastValues")


class IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValues(BaseModel):
    client_token: str = Field(alias="clientToken")
    data: List[
        Optional["IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValuesData"]
    ]
    next_token: Optional[str] = Field(alias="nextToken")
    presigned_url: Optional[str] = Field(alias="presignedUrl")
    query_id: Optional[str] = Field(alias="queryId")
    result_chunk_index: Optional[str] = Field(alias="resultChunkIndex")
    result_stored_in_s3: bool = Field(alias="resultStoredInS3")


class IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValuesData(BaseModel):
    iot_endpoint_id: str = Field(alias="iotEndpointId")
    telemetry_values: Optional[
        List[
            Optional[
                "IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValuesDataTelemetryValues"
            ]
        ]
    ] = Field(alias="telemetryValues")


class IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValuesDataTelemetryValues(
    BaseModel
):
    telemetry_model: Optional[
        "IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValuesDataTelemetryValuesTelemetryModel"
    ] = Field(alias="telemetryModel")
    timestamp: Optional[str]
    value: Optional[str]


class IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValuesDataTelemetryValuesTelemetryModel(
    BaseModel
):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")


IotListHubsEndpointsLastValues.update_forward_refs()
IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValues.update_forward_refs()
IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValuesData.update_forward_refs()
IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValuesDataTelemetryValues.update_forward_refs()
IotListHubsEndpointsLastValuesIotListHubsEndpointsLastValuesDataTelemetryValuesTelemetryModel.update_forward_refs()
