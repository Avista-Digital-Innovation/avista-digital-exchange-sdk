# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ModelAttributeType, ModelSchemaType


class IotDeleteEndpoint(BaseModel):
    iot_delete_endpoint: Optional["IotDeleteEndpointIotDeleteEndpoint"] = Field(
        alias="iot_deleteEndpoint"
    )


class IotDeleteEndpointIotDeleteEndpoint(BaseModel):
    description: Optional[str]
    iot_endpoint_id: str = Field(alias="iotEndpointId")
    iot_hub_id: str = Field(alias="iotHubId")
    model_id: str = Field(alias="modelId")
    name: str
    owner_user_id: str = Field(alias="ownerUserId")
    properties: Optional[List[Optional["IotDeleteEndpointIotDeleteEndpointProperties"]]]
    telemetry: Optional[List[Optional["IotDeleteEndpointIotDeleteEndpointTelemetry"]]]


class IotDeleteEndpointIotDeleteEndpointProperties(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    default_value: Optional[str] = Field(alias="defaultValue")
    description: Optional[str]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")
    timestamp: Optional[str]
    value: Optional[str]
    writable: Optional[bool]


class IotDeleteEndpointIotDeleteEndpointTelemetry(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")


IotDeleteEndpoint.update_forward_refs()
IotDeleteEndpointIotDeleteEndpoint.update_forward_refs()
IotDeleteEndpointIotDeleteEndpointProperties.update_forward_refs()
IotDeleteEndpointIotDeleteEndpointTelemetry.update_forward_refs()
