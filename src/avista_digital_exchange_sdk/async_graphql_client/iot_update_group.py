# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ModelAttributeType, ModelSchemaType


class IotUpdateGroup(BaseModel):
    iot_update_group: Optional["IotUpdateGroupIotUpdateGroup"] = Field(
        alias="iot_updateGroup"
    )


class IotUpdateGroupIotUpdateGroup(BaseModel):
    description: Optional[str]
    endpoints: Optional[List[Optional["IotUpdateGroupIotUpdateGroupEndpoints"]]]
    iot_endpoint_ids: Optional[List[Optional[str]]] = Field(alias="iotEndpointIds")
    iot_group_id: str = Field(alias="iotGroupId")
    iot_hub_id: str = Field(alias="iotHubId")
    name: str
    owner_user_id: str = Field(alias="ownerUserId")


class IotUpdateGroupIotUpdateGroupEndpoints(BaseModel):
    description: Optional[str]
    iot_endpoint_id: str = Field(alias="iotEndpointId")
    iot_hub_id: str = Field(alias="iotHubId")
    model_id: str = Field(alias="modelId")
    name: str
    owner_user_id: str = Field(alias="ownerUserId")
    properties: Optional[
        List[Optional["IotUpdateGroupIotUpdateGroupEndpointsProperties"]]
    ]
    telemetry: Optional[
        List[Optional["IotUpdateGroupIotUpdateGroupEndpointsTelemetry"]]
    ]


class IotUpdateGroupIotUpdateGroupEndpointsProperties(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    default_value: Optional[str] = Field(alias="defaultValue")
    description: Optional[str]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")
    timestamp: Optional[str]
    value: Optional[str]
    writable: Optional[bool]


class IotUpdateGroupIotUpdateGroupEndpointsTelemetry(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")


IotUpdateGroup.update_forward_refs()
IotUpdateGroupIotUpdateGroup.update_forward_refs()
IotUpdateGroupIotUpdateGroupEndpoints.update_forward_refs()
IotUpdateGroupIotUpdateGroupEndpointsProperties.update_forward_refs()
IotUpdateGroupIotUpdateGroupEndpointsTelemetry.update_forward_refs()
