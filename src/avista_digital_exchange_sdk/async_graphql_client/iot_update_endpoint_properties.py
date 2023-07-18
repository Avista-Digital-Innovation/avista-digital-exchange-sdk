# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ModelAttributeType, ModelSchemaType


class IotUpdateEndpointProperties(BaseModel):
    iot_update_endpoint_properties: Optional[
        "IotUpdateEndpointPropertiesIotUpdateEndpointProperties"
    ] = Field(alias="iot_updateEndpointProperties")


class IotUpdateEndpointPropertiesIotUpdateEndpointProperties(BaseModel):
    description: Optional[str]
    iot_endpoint_id: str = Field(alias="iotEndpointId")
    iot_hub_id: str = Field(alias="iotHubId")
    model_id: str = Field(alias="modelId")
    name: str
    owner_user_id: str = Field(alias="ownerUserId")
    properties: Optional[
        List[
            Optional["IotUpdateEndpointPropertiesIotUpdateEndpointPropertiesProperties"]
        ]
    ]
    telemetry: Optional[
        List[
            Optional["IotUpdateEndpointPropertiesIotUpdateEndpointPropertiesTelemetry"]
        ]
    ]


class IotUpdateEndpointPropertiesIotUpdateEndpointPropertiesProperties(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    default_value: Optional[str] = Field(alias="defaultValue")
    description: Optional[str]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")
    timestamp: Optional[str]
    value: Optional[str]
    writable: Optional[bool]


class IotUpdateEndpointPropertiesIotUpdateEndpointPropertiesTelemetry(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")


IotUpdateEndpointProperties.update_forward_refs()
IotUpdateEndpointPropertiesIotUpdateEndpointProperties.update_forward_refs()
IotUpdateEndpointPropertiesIotUpdateEndpointPropertiesProperties.update_forward_refs()
IotUpdateEndpointPropertiesIotUpdateEndpointPropertiesTelemetry.update_forward_refs()
