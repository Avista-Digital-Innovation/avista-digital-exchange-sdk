# Generated by ariadne-codegen on 2023-07-17 15:57
# Source: ../step_1_gqlg/output/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ModelAttributeType, ModelSchemaType


class IotGetModel(BaseModel):
    iot_get_model: Optional["IotGetModelIotGetModel"] = Field(alias="iot_getModel")


class IotGetModelIotGetModel(BaseModel):
    description: Optional[str]
    display_name: str = Field(alias="displayName")
    dtmi: str
    model_id: str = Field(alias="modelId")
    owner_user_id: str = Field(alias="ownerUserId")
    properties: Optional[List[Optional["IotGetModelIotGetModelProperties"]]]
    telemetry: Optional[List[Optional["IotGetModelIotGetModelTelemetry"]]]


class IotGetModelIotGetModelProperties(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    default_value: Optional[str] = Field(alias="defaultValue")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")
    writable: Optional[bool]


class IotGetModelIotGetModelTelemetry(BaseModel):
    attribute_type: ModelAttributeType = Field(alias="attributeType")
    description: Optional[str]
    index: Optional[int]
    name: str
    schema_type: ModelSchemaType = Field(alias="schemaType")


IotGetModel.update_forward_refs()
IotGetModelIotGetModel.update_forward_refs()
IotGetModelIotGetModelProperties.update_forward_refs()
IotGetModelIotGetModelTelemetry.update_forward_refs()
